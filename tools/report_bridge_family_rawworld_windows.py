from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


PATTERNS = {
    "tragende_verarbeitung": {
        "tonal_band": "tonal_mid",
        "target_role": "zentrum_rekoppelnd",
    },
    "kippnaehe": {
        "tonal_band": "tonal_high",
        "target_role": "rand_kipp",
    },
}

RAW_WORLD_METRICS = [
    "sehen_form_flow",
    "sehen_form_stability",
    "sehen_form_change",
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "rezeptor_visual_form_salience",
    "rezeptor_auditory_stimulation",
    "rezeptor_field_intake_pressure",
    "perception_auditory_loudness",
    "perception_auditory_listen_tendency",
    "perception_visual_sharpness",
    "perception_visual_distance_tendency",
    "perception_raw_field_intake_pressure",
    "perception_adapted_field_intake_pressure",
    "mcm_rekopplung_quality",
    "mcm_strain_quality",
    "mcm_feldwirkung_mcm_coherence",
    "mcm_feldwirkung_mcm_tension",
    "mcm_feldwirkung_mcm_asymmetry",
]


def _float(row: dict[str, str], key: str, default: float = 0.0) -> float:
    try:
        return float(row.get(key, "") or default)
    except (TypeError, ValueError):
        return default


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[idx]


def _band(value: float, q33: float, q66: float) -> str:
    if value <= q33:
        return "tonal_low"
    if value >= q66:
        return "tonal_high"
    return "tonal_mid"


def _role(row: dict[str, str], qs: dict[str, float]) -> str:
    field_class = (row.get("passive_mcm_effect_class") or "").strip()
    rekopplung = _float(row, "mcm_rekopplung_quality")
    strain = _float(row, "mcm_strain_quality")
    carry = _float(row, "mcm_carry_quality")
    tension = _float(row, "mcm_feldwirkung_mcm_tension")

    if field_class in {"kippend", "gespannt"} or (
        strain >= qs["strain_q66"] and rekopplung <= qs["rekopplung_q33"]
    ):
        return "rand_kipp"
    if field_class == "stabil" and rekopplung >= qs["rekopplung_q66"] and strain <= qs["strain_q33"]:
        return "zentrum_rekoppelnd"
    if carry >= qs["carry_q66"] and rekopplung >= qs["rekopplung_q50"] and strain < qs["strain_q66"]:
        return "bruecke_tragend"
    if field_class == "tragend_unruhig" or tension >= qs["tension_q66"] or strain >= qs["strain_q50"]:
        return "offen_unruhig"
    return "offenes_feld"


def _iter_episode_files(world_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for world_dir in world_dirs:
        if world_dir.is_file() and world_dir.name == "episodes.csv":
            files.append(world_dir)
        elif world_dir.is_dir():
            files.extend(sorted(world_dir.glob("**/episodes.csv")))
    return files


def _world_group(path: Path) -> str:
    name = path.parent.parent.name.lower()
    if "synth" in name:
        return "synthetisch"
    if "state" in name:
        return "regime"
    if "real_quiet" in name or "sequence_break" in name:
        return "real_segment"
    if "adapted_time" in name or "_1h" in name:
        return "zeit_1h"
    if "adapted_field" in name or "_5m" in name:
        return "feld_5m"
    return "sonstige"


def _visual_label(row: dict[str, str]) -> str:
    stability = _float(row, "sehen_form_stability")
    change = _float(row, "sehen_form_change")
    sharpness = _float(row, "perception_visual_sharpness")
    distance = _float(row, "perception_visual_distance_tendency")
    if stability >= change and sharpness >= distance:
        return "stabile_scharfe_form"
    if change > stability and distance > sharpness:
        return "wechselnde_distanzform"
    if stability >= change:
        return "stabile_form"
    return "wechselnde_form"


def _tone_label(row: dict[str, str]) -> str:
    loudness = _float(row, "perception_auditory_loudness")
    listen = _float(row, "perception_auditory_listen_tendency")
    shift = abs(_float(row, "hoeren_energy_shift"))
    if loudness > listen and shift >= 0.12:
        return "lauter_wechsel"
    if loudness > listen:
        return "laute_spannung"
    if listen >= loudness and shift >= 0.12:
        return "geordnetes_hinhoeren_mit_wechsel"
    return "geordnetes_hinhoeren"


def _field_label(row: dict[str, str]) -> str:
    rec = _float(row, "mcm_rekopplung_quality")
    strain = _float(row, "mcm_strain_quality")
    tension = _float(row, "mcm_feldwirkung_mcm_tension")
    if rec >= 0.72 and strain <= 0.14:
        return "rekoppelt"
    if strain >= 0.18 or tension >= 0.16:
        return "belastet_kippnah"
    return "offen"


def _episode_matches(row: dict[str, str], pattern: str, qs: dict[str, float]) -> bool:
    spec = PATTERNS[pattern]
    band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
    role = _role(row, qs)
    return band == spec["tonal_band"] and role == spec["target_role"]


def _summarize_file(path: Path, families: set[str], window: int) -> list[dict[str, object]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return []
    tone_values = [_float(row, "hoeren_energy_tone") for row in rows]
    qs = {
        "tone_q33": _quantile(tone_values, 0.33),
        "tone_q66": _quantile(tone_values, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }
    buckets: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    before_buckets: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    ticks: dict[tuple[str, str, str], list[int]] = defaultdict(list)
    for idx, row in enumerate(rows):
        family = (row.get("symbol_family") or "").strip()
        if family not in families:
            continue
        for pattern in PATTERNS:
            if _episode_matches(row, pattern, qs):
                key = (_world_group(path), family, pattern)
                buckets[key].append(row)
                before_buckets[key].extend(rows[max(0, idx - window) : idx])
                ticks[key].append(int(_float(row, "tick")))

    out: list[dict[str, object]] = []
    for key, target_rows in buckets.items():
        world_group, family, pattern = key
        before_rows = before_buckets[key] or target_rows
        visual_counter = Counter(_visual_label(row) for row in target_rows)
        tone_counter = Counter(_tone_label(row) for row in target_rows)
        field_counter = Counter(_field_label(row) for row in target_rows)
        before_visual_counter = Counter(_visual_label(row) for row in before_rows)
        before_tone_counter = Counter(_tone_label(row) for row in before_rows)
        before_field_counter = Counter(_field_label(row) for row in before_rows)
        base = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "world_group": world_group,
            "world": path.parent.parent.name,
            "run": path.parent.name,
            "family": family,
            "pattern": pattern,
            "events": len(target_rows),
            "tick_min": min(ticks[key]),
            "tick_max": max(ticks[key]),
            "before_window_ticks": window,
            "dominant_visual": visual_counter.most_common(1)[0][0],
            "dominant_tone": tone_counter.most_common(1)[0][0],
            "dominant_field": field_counter.most_common(1)[0][0],
            "before_dominant_visual": before_visual_counter.most_common(1)[0][0],
            "before_dominant_tone": before_tone_counter.most_common(1)[0][0],
            "before_dominant_field": before_field_counter.most_common(1)[0][0],
        }
        for metric in RAW_WORLD_METRICS:
            base[f"target_{metric}"] = _mean([_float(row, metric) for row in target_rows])
            base[f"before_{metric}"] = _mean([_float(row, metric) for row in before_rows])
            base[f"delta_{metric}"] = float(base[f"target_{metric}"]) - float(base[f"before_{metric}"])
        out.append(base)
    return out


def _aggregate(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["world_group"]), str(row["family"]), str(row["pattern"]))].append(row)
    out: list[dict[str, object]] = []
    for (world_group, family, pattern), group in sorted(groups.items()):
        row: dict[str, object] = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "world_group": world_group,
            "family": family,
            "pattern": pattern,
            "runs": len(group),
            "events": sum(int(item["events"]) for item in group),
            "tick_min": min(int(item["tick_min"]) for item in group),
            "tick_max": max(int(item["tick_max"]) for item in group),
            "dominant_visual": Counter(str(item["dominant_visual"]) for item in group).most_common(1)[0][0],
            "dominant_tone": Counter(str(item["dominant_tone"]) for item in group).most_common(1)[0][0],
            "dominant_field": Counter(str(item["dominant_field"]) for item in group).most_common(1)[0][0],
            "before_dominant_visual": Counter(str(item["before_dominant_visual"]) for item in group).most_common(1)[0][0],
            "before_dominant_tone": Counter(str(item["before_dominant_tone"]) for item in group).most_common(1)[0][0],
            "before_dominant_field": Counter(str(item["before_dominant_field"]) for item in group).most_common(1)[0][0],
        }
        for metric in RAW_WORLD_METRICS:
            row[f"target_{metric}"] = _mean([float(item[f"target_{metric}"]) for item in group])
            row[f"before_{metric}"] = _mean([float(item[f"before_{metric}"]) for item in group])
            row[f"delta_{metric}"] = _mean([float(item[f"delta_{metric}"]) for item in group])
        out.append(row)
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _report_title(path: Path, fallback: str) -> str:
    stem = path.stem
    if "_" not in stem:
        return fallback
    prefix, rest = stem.split("_", 1)
    if not prefix.isdigit():
        return fallback
    return f"{prefix} - {rest.replace('_', ' ').title()}"


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_family: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_family[str(row["family"])].append(row)

    lines = [
        f"# {_report_title(path, 'Brueckenfamilien gegen Rohweltfenster')}",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Welche uebersetzten Rohweltfenster liegen unter realen Brueckenfamilien, wenn dieselbe Symbolfamilie einmal als `tragende_verarbeitung` und einmal als `kippnaehe` erscheint?",
        "",
        "## Methode",
        "",
        "- Geprueft werden ausgewaehlte reale Brueckenfamilien aus 1072.",
        "- Pro Fundstelle werden Ziel-Episode und Vorfenster gelesen.",
        "- Rohwelt meint hier die MINI_DIO-Weltuebersetzung: Sehen, Hoeren, Rezeptoren und MCM-Feldwirkung.",
        "- Keine OHLC-Handlungslesung, keine Strategie, keine Runtime-Regel.",
        "",
        "## Familienvergleich",
        "",
        "| Weltgruppe | Familie | Muster | Events | Ticks | Visual | Ton | Feld | Vorfeld | Target Spannung | Vor Spannung | Delta Spannung | Target Rekopplung | Target Strain |",
        "|---|---|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: (str(item["family"]), str(item["world_group"]), str(item["pattern"]))):
        lines.append(
            "| {world_group} | {family} | {pattern} | {events} | {tick_min}-{tick_max} | {dominant_visual} | {dominant_tone} | {dominant_field} | {before_dominant_field} | {target_mcm_feldwirkung_mcm_tension:.4f} | {before_mcm_feldwirkung_mcm_tension:.4f} | {delta_mcm_feldwirkung_mcm_tension:.4f} | {target_mcm_rekopplung_quality:.4f} | {target_mcm_strain_quality:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.",
            "",
            "Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.",
            "",
            "## Schluss",
            "",
            "Diese Pruefung schliesst direkt an 1074 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste reale Familie aus dieser Tabelle einzeln visualisiert werden: Tickfenster, Vorfenster, Tonlage und Feldwirkung nebeneinander.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--family", action="append", required=True)
    parser.add_argument("--window", type=int, default=8)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    families = set(args.family)
    rows: list[dict[str, object]] = []
    for episode_file in _iter_episode_files([Path(item) for item in args.world_dir]):
        rows.extend(_summarize_file(episode_file, families, args.window))
    aggregate = _aggregate(rows)
    _write_csv(aggregate, Path(args.out_csv))
    _write_md(aggregate, Path(args.out_md))
    print(f"raw_rows={len(rows)}")
    print(f"aggregate_rows={len(aggregate)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
