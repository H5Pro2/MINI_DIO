from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.receptor_adaptation_memory import ReceptorAdaptationMemory
from mini_dio.worldlage_classifier import classify_worldlage


DEFAULT_INPUTS = [
    "docs/befunde/1001-2000/1001-1500/1281_REZEPTORHALTUNG_AB_TEST.csv",
    "docs/befunde/1001-2000/1001-1500/1283_REZEPTORHALTUNG_AB_TEST_MEHRWELTEN.csv",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _world_pairs(rows: list[dict[str, str]]) -> list[tuple[str, dict[str, str], dict[str, str]]]:
    by_world: dict[str, dict[str, dict[str, str]]] = {}
    for row in rows:
        world = str(row.get("world", "") or "unknown")
        mode = str(row.get("mode", "") or "unknown")
        by_world.setdefault(world, {})[mode] = row
    pairs: list[tuple[str, dict[str, str], dict[str, str]]] = []
    for world, modes in sorted(by_world.items()):
        base = modes.get("A_BASE")
        adapted = modes.get("B_PREF")
        if base and adapted:
            pairs.append((world, base, adapted))
    return pairs


def _world_kind(world: str) -> str:
    name = str(world or "").upper()
    if any(token in name for token in ("DESYNC", "PURE_HEARING", "VISUAL_", "CHAOTIC", "RAND_KIPP", "RECOUPLING")):
        return "sinneswiderspruch"
    if any(token in name for token in ("STRESS", "NEG")):
        return "stress_last"
    if any(token in name for token in ("SIDE", "STABLE", "QUIET")):
        return "ruhig_stabil"
    if "PAXG" in name:
        return "gold_kontrast"
    if "KAS" in name:
        return "leise_assetnaehe"
    if any(token in name for token in ("BTC", "DOGE", "XRP", "SOL")):
        return "markt_weltspur"
    return "unbestimmt"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Rezeptor Adaptation Memory",
        "",
        "Passive Verdichtung der A/B-Folgen einer Sinneshaltung.",
        "",
        "Diese Memory speichert keine Regel. Sie speichert, ob eine gelesene Rezeptorhaltung in beobachteten Welten das MCM-Feld eher beruhigt, neutral laesst oder verschiebt.",
        "",
        "## Verdichtung",
        "",
        "| Haltung | Welten | bekannte Ticks | angewendet | Folge | Qualitaet | dZentrum | dRand | dRekopplung | dStrain | dRohfeld | dTon | dSicht |",
        "|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {adaptation_label} | {worlds} | {known_ticks} | {applied_ticks} | {dominant_outcome} | {adaptation_quality:.4f} | {avg_delta_zentrum:.4f} | {avg_delta_rand:.4f} | {avg_delta_rekopplung:.4f} | {avg_delta_strain:.4f} | {avg_delta_raw_field:.4f} | {avg_delta_auditory:.4f} | {avg_delta_visual:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die bisher getestete Rezeptorhaltung zeigt eine beruhigende Folge: Rand/Kipp und Strain sinken leicht, Zentrum und Rekopplung bleiben erhalten oder steigen minimal.",
            "",
            "Das ist fachlich wichtig, weil die Anpassung nicht als harte Normalisierung erscheint. Sie wirkt eher wie eine gelernte Aufnahmehaltung vor dem Feld.",
            "",
            "## Grenze",
            "",
            "Die Memory ist passiv. Sie steuert Mini-DIO noch nicht aktiv.",
            "",
            "Sie beantwortet nur:",
            "",
            "```text",
            "Welche Sinneshaltung hatte in welchen Welten welche Feldfolge?",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--group-by-world-kind", action="store_true")
    parser.add_argument("--group-by-measured-worldlage", action="store_true")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1285_REZEPTOR_ADAPTATION_MEMORY.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1285_REZEPTOR_ADAPTATION_MEMORY.csv")
    args = parser.parse_args()

    memory = ReceptorAdaptationMemory()
    inputs = args.input or DEFAULT_INPUTS
    for input_path in inputs:
        rows = _load(Path(input_path))
        for world, base, adapted in _world_pairs(rows):
            label = "achsenweise_rezeptorhaltung"
            if args.group_by_measured_worldlage:
                label = f"{label}_{classify_worldlage(base)}"
            if args.group_by_world_kind:
                label = f"{label}_{_world_kind(world)}"
            memory.observe_ab_pair(label=label, base=base, adapted=adapted)
    output_rows = memory.rows()
    _write_csv(output_rows, Path(args.csv_out))
    _write_markdown(output_rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
