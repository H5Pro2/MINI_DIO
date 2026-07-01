from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from data_builder.synthetic_desync_world_builder import PHASE_PRESETS  # noqa: E402


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _label_phases(phases: tuple[tuple[str, int], ...]) -> tuple[tuple[str, int], ...]:
    totals = Counter(name for name, _length in phases)
    seen: Counter[str] = Counter()
    labelled: list[tuple[str, int]] = []
    for name, length in phases:
        seen[name] += 1
        label = f"{name}_{seen[name]}" if totals[name] > 1 else name
        labelled.append((label, length))
    return tuple(labelled)


def _phase_for_tick(tick: int, phases: tuple[tuple[str, int], ...]) -> str:
    index = max(0, tick - 1)
    offset = 0
    for name, length in phases:
        if index < offset + length:
            return name
        offset += length
    return phases[-1][0]


def _topology_role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    strain = _float(row.get("mcm_strain_quality"))
    rekopplung = _float(row.get("mcm_rekopplung_quality"))
    sensory = _float(row.get("mcm_sensory_coupling"))

    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    if rekopplung >= 0.58 and strain <= 0.26 and sensory >= 0.70:
        return "rekopplungsnaehe"
    if strain >= 0.28:
        return "spannungsrand_kippnaehe"
    return "unbestimmt"


def _dominant(values: list[str]) -> str:
    cleaned = [str(item or "-") for item in values if str(item or "-") != "-"]
    if not cleaned:
        return "-"
    return Counter(cleaned).most_common(1)[0][0]


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_phase_rows(episodes: Path, variant: str) -> list[dict[str, object]]:
    phases = _label_phases(PHASE_PRESETS[variant])
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in _load_rows(episodes):
        tick = int(_float(row.get("tick")))
        grouped[_phase_for_tick(tick, phases)].append(row)

    phase_rows: list[dict[str, object]] = []
    for phase_name, length in phases:
        items = grouped.get(phase_name, [])
        total = max(1, len(items))
        roles = Counter(_topology_role(item) for item in items)
        phase_rows.append(
            {
                "phase": phase_name,
                "phase_length": length,
                "episodes": len(items),
                "zentrum_share": roles["zentrum_stabil"] / total,
                "open_share": roles["offene_variante"] / total,
                "rand_kipp_share": roles["spannungsrand_kippnaehe"] / total,
                "rekopplungsnaehe_share": roles["rekopplungsnaehe"] / total,
                "avg_rekopplung": _mean([_float(item.get("mcm_rekopplung_quality")) for item in items]),
                "avg_carry": _mean([_float(item.get("mcm_carry_quality")) for item in items]),
                "avg_strain": _mean([_float(item.get("mcm_strain_quality")) for item in items]),
                "avg_sensory": _mean([_float(item.get("mcm_sensory_coupling")) for item in items]),
                "avg_visual_gap": _mean([_float(item.get("mcm_visual_field_gap")) for item in items]),
                "avg_hearing_gap": _mean([_float(item.get("mcm_hearing_field_gap")) for item in items]),
                "avg_auditory_loudness": _mean([_float(item.get("perception_auditory_loudness")) for item in items]),
                "avg_adapted_field_intake": _mean(
                    [_float(item.get("perception_adapted_field_intake_pressure")) for item in items]
                ),
                "dominant_effect_class": _dominant([item.get("passive_mcm_effect_class", "-") for item in items]),
                "dominant_awareness": _dominant(
                    [item.get("passive_inner_effect_awareness_state", "-") for item in items]
                ),
                "dominant_symbol_family": _dominant([item.get("symbol_family", "-") for item in items]),
                "dominant_preview_symbol": _dominant(
                    [item.get("mcm_field_episode_preview_symbol", "-") for item in items]
                ),
            }
        )
    return phase_rows


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, object]], path: Path, title: str, source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?",
        "",
        "Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.",
        "",
        "## Datengrundlage",
        "",
        f"- Quelle: `{source}`",
        "- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.",
        "",
        "## Phasenmatrix",
        "",
        "| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {phase} | {episodes} | {zentrum_share:.4f} | {open_share:.4f} | {rand_kipp_share:.4f} | {rekopplungsnaehe_share:.4f} | {avg_rekopplung:.4f} | {avg_carry:.4f} | {avg_strain:.4f} | {avg_sensory:.4f} | {avg_hearing_gap:.4f} | {avg_auditory_loudness:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Dominante Innenfeld-Signatur",
            "",
            "| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |",
            "|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| {phase} | `{dominant_effect_class}` | `{dominant_awareness}` | `{dominant_symbol_family}` | `{dominant_preview_symbol}` |".format(
                **row
            )
        )

    max_open = max(rows, key=lambda item: float(item["open_share"]))
    max_rand = max(rows, key=lambda item: float(item["rand_kipp_share"]))
    max_center = max(rows, key=lambda item: float(item["zentrum_share"]))
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste offene Variante: `{max_open['phase']}` mit `{float(max_open['open_share']):.4f}`.",
            f"- Staerkste Rand-/Kippnaehe: `{max_rand['phase']}` mit `{float(max_rand['rand_kipp_share']):.4f}`.",
            f"- Staerkste Zentrierung: `{max_center['phase']}` mit `{float(max_center['zentrum_share']):.4f}`.",
            "",
            "Lesart:",
            "",
            "- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.",
            "- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.",
            "- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.",
            "",
            "Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", required=True)
    parser.add_argument("--variant", choices=sorted(PHASE_PRESETS), required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    rows = build_phase_rows(Path(args.episodes), args.variant)
    write_csv(rows, Path(args.csv_out))
    write_md(rows, Path(args.out), args.title, args.episodes)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
