from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.run_real_sleep_real_chain import run_chain


DEFAULT_PAIRS = [
    (
        "multi_axis_sideways_0_to_2000",
        "data/segment_sideways_2026_10k_start0_size2000.csv",
        "data/segment_sideways_2026_10k_start2000_size2000.csv",
        "sideways",
    ),
    (
        "multi_axis_sideways_4000_to_6000",
        "data/segment_sideways_2026_10k_start4000_size2000.csv",
        "data/segment_sideways_2026_10k_start6000_size2000.csv",
        "sideways",
    ),
    (
        "multi_axis_stress_2000_to_4000",
        "data/segment_negative_stress_2023_10k_start2000_size2000.csv",
        "data/segment_negative_stress_2023_10k_start4000_size2000.csv",
        "negative_stress",
    ),
    (
        "multi_axis_stress_4000_to_6000",
        "data/segment_negative_stress_2023_10k_start4000_size2000.csv",
        "data/segment_negative_stress_2023_10k_start6000_size2000.csv",
        "negative_stress",
    ),
    (
        "multi_axis_expansion_4000_to_6000",
        "data/segment_positive_expansion_2023_10k_start4000_size2000.csv",
        "data/segment_positive_expansion_2023_10k_start6000_size2000.csv",
        "positive_expansion",
    ),
    (
        "multi_axis_expansion_2000_to_4000",
        "data/segment_positive_expansion_2023_10k_start2000_size2000.csv",
        "data/segment_positive_expansion_2023_10k_start4000_size2000.csv",
        "positive_expansion",
    ),
]


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _rel(path: Path) -> str:
    path = path.resolve()
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _metric(summary: dict, name: str, side: str = "real_a") -> float:
    metrics = dict(dict(summary.get("comparison", {}) or {}).get("metrics", {}) or {})
    item = dict(metrics.get(name, {}) or {})
    return _float(item.get(side))


def _state_counts(summary: dict) -> dict[str, int]:
    memory = dict(summary.get("memory_a_summary", {}) or {})
    roles = dict(memory.get("field_roles", {}) or {})
    if roles:
        return {str(key): _int(value) for key, value in roles.items()}
    return {str(key): _int(value) for key, value in dict(summary.get("comparison", {}).get("real_a_episode_states", {}) or {}).items()}


def _effect_counts(summary: dict) -> dict[str, int]:
    effects = dict(summary.get("comparison", {}).get("real_a_effect_classes", {}) or {})
    return {str(key): _int(value) for key, value in effects.items()}


def _combination_rows(summary: dict) -> list[dict]:
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})
    return [dict(row) for row in followup.get("combination_traces", []) or [] if isinstance(row, dict)]


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _classify_width(role_count: int, combo_count: int) -> str:
    if role_count <= 2 and combo_count <= 1:
        return "kompakt"
    if role_count >= 5 or combo_count >= 10:
        return "verteilt"
    return "mittel"


def _classify_axis(row: dict[str, object]) -> str:
    width = str(row.get("rollenbreite_klasse", ""))
    afterimage = _float(row.get("nachhall"))
    rekopplung = _float(row.get("rekopplung"))
    kippend = _int(row.get("kippend"))
    gespannt = _int(row.get("gespannt"))
    if kippend + gespannt >= 25:
        return "rand_kippnah"
    if width == "verteilt" and rekopplung >= 0.695:
        return "verteilt_rekoppelnd"
    if width == "kompakt" and afterimage >= 0.16:
        return "kompakt_nachhallend"
    if width == "kompakt":
        return "kompakt_gebunden"
    if width == "verteilt":
        return "verteilt_offen"
    return "mittlere_uebergangsphase"


def _row_from_summary(summary: dict, group: str) -> dict[str, object]:
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})
    states = _state_counts(summary)
    effects = _effect_counts(summary)
    combos = _combination_rows(summary)
    role_count = _int(followup.get("touched_role_count"))
    combo_count = _int(followup.get("combination_trace_count"))
    cross_count = sum(1 for item in combos if str(item.get("combination_state", "")) == "sleep_cross_state_combination")
    same_count = sum(1 for item in combos if str(item.get("combination_state", "")) == "sleep_same_role_family_combination")
    co_touch = [_float(item.get("co_touch_ratio")) for item in combos]
    resonance = [_float(item.get("avg_pair_sleep_resonance")) for item in combos]
    row: dict[str, object] = {
        "label": str(summary.get("label", "")),
        "weltgruppe": group,
        "data_path": str(summary.get("data_path", "")),
        "follow_data_path": str(summary.get("follow_data_path", "")),
        "rollen": role_count,
        "kombinationen": combo_count,
        "rollen_reaktiviert": _int(followup.get("reactivated_role_count")),
        "kombinationen_voll": _int(followup.get("combination_fully_reactivated_count")),
        "reaktivierungsquote": _float(followup.get("reactivation_ratio")),
        "kombinationsquote": _float(followup.get("combination_reactivation_ratio")),
        "cross_state": cross_count,
        "same_state": same_count,
        "avg_co_touch": _avg(co_touch),
        "min_co_touch": min(co_touch) if co_touch else 0.0,
        "avg_resonanz": _avg(resonance),
        "syntax": _int(_metric(summary, "unique_symbols")),
        "stabil": _int(effects.get("stabil")),
        "tragend_unruhig": _int(effects.get("tragend_unruhig")),
        "kippend": _int(effects.get("kippend")),
        "gespannt": _int(effects.get("gespannt")),
        "field_carried": _int(states.get("field_carried")),
        "field_strained": _int(states.get("field_strained")),
        "rekopplung": _metric(summary, "avg_mcm_rekopplung_quality"),
        "adaptive_rekopplung": _metric(summary, "avg_mcm_adaptive_rekopplung_quality"),
        "adaptive_rekopplung_experience": _metric(summary, "avg_mcm_adaptive_rekopplung_experience"),
        "adaptive_weight_carry": _metric(summary, "avg_mcm_adaptive_weight_carry"),
        "adaptive_weight_alignment": _metric(summary, "avg_mcm_adaptive_weight_alignment"),
        "adaptive_weight_strain_relief": _metric(summary, "avg_mcm_adaptive_weight_strain_relief"),
        "adaptive_weight_sensory": _metric(summary, "avg_mcm_adaptive_weight_sensory"),
        "carry": _metric(summary, "avg_mcm_carry_quality"),
        "strain": _metric(summary, "avg_mcm_strain_quality"),
        "sensory": _metric(summary, "avg_mcm_sensory_coupling"),
        "nachhall": _metric(summary, "avg_mini_afterimage"),
        "neuro_load": _metric(summary, "avg_mini_neuro_load"),
        "neuro_balance": _metric(summary, "avg_mini_neuro_balance"),
    }
    row["adaptive_rekopplung_delta"] = _float(row["adaptive_rekopplung"]) - _float(row["rekopplung"])
    row["rollenbreite_klasse"] = _classify_width(role_count, combo_count)
    row["achsenklasse"] = _classify_axis(row)
    return row


def _parse_pair(text: str) -> tuple[str, str, str, str]:
    parts = [part.strip() for part in text.split("|")]
    if len(parts) != 4:
        raise ValueError("--pair erwartet Format label|data|follow_data|gruppe")
    return parts[0], parts[1], parts[2], parts[3]


def _run_or_load(
    label: str,
    data: str,
    follow: str,
    group: str,
    *,
    reuse: bool,
    ticks: int,
    intensity: float,
    role_limit: int,
    max_active_roles: int,
    activation_floor: float,
    sense_mode: str,
) -> dict:
    summary_path = ROOT / "debug" / "multiworld_axis_map" / label / "real_sleep_real_summary.json"
    if reuse and summary_path.exists():
        return _load_json(summary_path)
    return run_chain(
        data_path=Path(data),
        follow_data_path=Path(follow),
        label=label,
        debug_root=Path("debug/multiworld_axis_map"),
        memory_root=Path("memory/multiworld_axis_map"),
        out_path=Path("debug/multiworld_axis_map") / label / "real_sleep_real_chain.md",
        ticks=ticks,
        intensity=intensity,
        role_limit=role_limit,
        max_active_roles=max_active_roles,
        activation_floor=activation_floor,
        sense_mode=sense_mode,
        write_sleep_memory=True,
    )


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "label",
        "weltgruppe",
        "achsenklasse",
        "rollenbreite_klasse",
        "rollen",
        "kombinationen",
        "rollen_reaktiviert",
        "kombinationen_voll",
        "reaktivierungsquote",
        "kombinationsquote",
        "cross_state",
        "same_state",
        "avg_co_touch",
        "min_co_touch",
        "avg_resonanz",
        "syntax",
        "stabil",
        "tragend_unruhig",
        "kippend",
        "gespannt",
        "field_carried",
        "field_strained",
        "rekopplung",
        "adaptive_rekopplung",
        "adaptive_rekopplung_delta",
        "adaptive_rekopplung_experience",
        "adaptive_weight_carry",
        "adaptive_weight_alignment",
        "adaptive_weight_strain_relief",
        "adaptive_weight_sensory",
        "carry",
        "strain",
        "sensory",
        "nachhall",
        "neuro_load",
        "neuro_balance",
        "data_path",
        "follow_data_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, csv_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    class_counts: dict[str, int] = {}
    for row in rows:
        key = str(row.get("achsenklasse", "-"))
        class_counts[key] = class_counts.get(key, 0) + 1
    adaptive_deltas = [_float(row.get("adaptive_rekopplung_delta")) for row in rows]
    adaptive_experience = [_float(row.get("adaptive_rekopplung_experience")) for row in rows]
    adaptive_weights = {
        "carry": [_float(row.get("adaptive_weight_carry")) for row in rows],
        "alignment": [_float(row.get("adaptive_weight_alignment")) for row in rows],
        "strain_relief": [_float(row.get("adaptive_weight_strain_relief")) for row in rows],
        "sensory": [_float(row.get("adaptive_weight_sensory")) for row in rows],
    }
    weight_spreads = {
        key: (max(values) - min(values)) if values else 0.0
        for key, values in adaptive_weights.items()
    }
    max_weight_spread = max(weight_spreads.values()) if weight_spreads else 0.0
    if adaptive_deltas and max_weight_spread <= 0.01:
        adaptive_reading = "adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig"
    elif adaptive_deltas:
        adaptive_reading = "adaptive_rekopplung_aktiv_und_gewichte_differenzieren"
    else:
        adaptive_reading = "adaptive_rekopplung_nicht_gelesen"
    lines = [
        "# Automatisierter Mehrwelt-Achsenreport",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:",
        "",
        "```text",
        "Topologie",
        "Feldzeit",
        "Nachhall",
        "Rollenbreite",
        "```",
        "",
        "Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.",
        "",
        f"CSV: `{_rel(csv_path)}`",
        "",
        "## Achsentabelle",
        "",
        "| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["label"]),
                    str(row["weltgruppe"]),
                    str(row["achsenklasse"]),
                    str(row["rollenbreite_klasse"]),
                    str(row["rollen"]),
                    str(row["kombinationen"]),
                    str(row["cross_state"]),
                    str(row["same_state"]),
                    _fmt(row["rekopplung"]),
                    _fmt(row["adaptive_rekopplung"]),
                    _fmt(row["adaptive_rekopplung_delta"]),
                    _fmt(row["adaptive_rekopplung_experience"]),
                    _fmt(row["nachhall"]),
                    str(row["stabil"]),
                    str(row["tragend_unruhig"]),
                    str(row["kippend"]),
                    str(row["gespannt"]),
                ]
            )
            + " |"
        )
    lines.extend(["", "## Klassenverteilung", ""])
    for key, value in sorted(class_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Adaptive Rekopplung",
            "",
            f"Lesung: `{adaptive_reading}`",
            "",
            "| Messung | Minimum | Maximum | Spanne |",
            "|---|---:|---:|---:|",
            f"| Delta adaptiv-statisch | {_fmt(min(adaptive_deltas) if adaptive_deltas else 0.0)} | {_fmt(max(adaptive_deltas) if adaptive_deltas else 0.0)} | {_fmt((max(adaptive_deltas) - min(adaptive_deltas)) if adaptive_deltas else 0.0)} |",
            f"| Erfahrung | {_fmt(min(adaptive_experience) if adaptive_experience else 0.0)} | {_fmt(max(adaptive_experience) if adaptive_experience else 0.0)} | {_fmt((max(adaptive_experience) - min(adaptive_experience)) if adaptive_experience else 0.0)} |",
        ]
    )
    for key, values in adaptive_weights.items():
        lines.append(
            f"| Gewicht {key} | {_fmt(min(values) if values else 0.0)} | {_fmt(max(values) if values else 0.0)} | {_fmt(weight_spreads.get(key, 0.0))} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.",
            "",
            "Wichtig ist die gemeinsame Lesung:",
            "",
            "```text",
            "Rollenbreite allein reicht nicht.",
            "Nachhall allein reicht nicht.",
            "Topologie allein reicht nicht.",
            "Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.",
            "```",
            "",
            "Die adaptive Rekopplung wird als passive Zusatzlesung ausgewiesen. Sie zeigt, ob Erfahrung die Rueckfuehrung gegenueber der statischen Referenz anhebt, daempft oder nahe am Grundwert haelt.",
            "",
            "Wenn die adaptiven Gewichte nur sehr wenig streuen, ist die Schicht technisch aktiv, aber noch nicht stark welt- oder familienselektiv. Dann liegt die naechste Arbeit nicht in mehr Daten, sondern in genauerer Erfahrungskopplung pro Feldrolle.",
            "",
            "## Grenze",
            "",
            "Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieser Report auf neue Assets oder neue synthetische Kontrollwelten angewendet werden. Ziel ist zu pruefen, ob die Achsenklassen stabil bleiben oder neue Feldmilieus entstehen.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a combined passive multiworld axis report.")
    parser.add_argument("--pair", action="append", default=[], help="Format: label|data|follow_data|gruppe")
    parser.add_argument("--reuse", action="store_true", help="Reuse existing debug/multiworld_axis_map summaries.")
    parser.add_argument("--out", default="docs/befunde/1674_AUTOMATISIERTER_MEHRWELT_ACHSENREPORT.md")
    parser.add_argument("--csv", default="docs/befunde/1674_AUTOMATISIERTER_MEHRWELT_ACHSENREPORT.csv")
    parser.add_argument("--ticks", type=int, default=300)
    parser.add_argument("--intensity", type=float, default=0.42)
    parser.add_argument("--role-limit", type=int, default=24)
    parser.add_argument("--max-active-roles", type=int, default=5)
    parser.add_argument("--activation-floor", type=float, default=0.45)
    parser.add_argument(
        "--sense-mode",
        choices=(
            "fixed",
            "world_relative",
            "rolling_relative",
            "adaptive_relative",
            "calibrated_relative",
            "phase_afterimage_relative",
        ),
        default="calibrated_relative",
    )
    args = parser.parse_args()
    pairs = [_parse_pair(item) for item in args.pair] if args.pair else DEFAULT_PAIRS
    rows: list[dict[str, object]] = []
    for label, data, follow, group in pairs:
        summary = _run_or_load(
            label,
            data,
            follow,
            group,
            reuse=bool(args.reuse),
            ticks=int(args.ticks),
            intensity=float(args.intensity),
            role_limit=int(args.role_limit),
            max_active_roles=int(args.max_active_roles),
            activation_floor=float(args.activation_floor),
            sense_mode=str(args.sense_mode),
        )
        rows.append(_row_from_summary(summary, group))
    out_path = ROOT / args.out
    csv_path = ROOT / args.csv
    _write_csv(rows, csv_path)
    _write_markdown(rows, out_path, csv_path)
    print(json.dumps({"out": _rel(out_path), "csv": _rel(csv_path), "rows": rows}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
