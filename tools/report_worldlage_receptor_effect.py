from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.worldlage_classifier import classify_adaptation_delta, classify_worldlage


DEFAULT_INPUTS = [
    "docs/befunde/1001-2000/1001-1500/1281_REZEPTORHALTUNG_AB_TEST.csv",
    "docs/befunde/1001-2000/1001-1500/1283_REZEPTORHALTUNG_AB_TEST_MEHRWELTEN.csv",
    "docs/befunde/1001-2000/1001-1500/1286_REZEPTORHALTUNG_AB_TEST_NEUE_WELTEN.csv",
    "docs/befunde/1001-2000/1001-1500/1289_REZEPTORHALTUNG_AB_TEST_WIDERSPRUCH.csv",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _pairs(rows: list[dict[str, str]]) -> list[tuple[dict[str, str], dict[str, str]]]:
    grouped: dict[str, dict[str, dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(str(row.get("world", "") or "unknown"), {})[str(row.get("mode", "") or "unknown")] = row
    out: list[tuple[dict[str, str], dict[str, str]]] = []
    for modes in grouped.values():
        base = modes.get("A_BASE")
        adapted = modes.get("B_PREF")
        if base and adapted:
            out.append((base, adapted))
    return out


def _to_float(value: object) -> float:
    try:
        number = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if number != number else number


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    buckets: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[str(row["worldlage"])].append(row)
    summary: list[dict[str, object]] = []
    for worldlage, items in sorted(buckets.items()):
        count = len(items)
        outcomes = Counter(str(item["adaptation_outcome"]) for item in items)
        summary.append(
            {
                "worldlage": worldlage,
                "worlds": count,
                "dominant_outcome": outcomes.most_common(1)[0][0],
                "outcome_counts": ";".join(f"{key}:{value}" for key, value in outcomes.most_common()),
                "avg_delta_zentrum": round(sum(_to_float(item["delta_zentrum"]) for item in items) / max(1, count), 6),
                "avg_delta_rand": round(sum(_to_float(item["delta_rand"]) for item in items) / max(1, count), 6),
                "avg_delta_rekopplung": round(sum(_to_float(item["delta_rekopplung"]) for item in items) / max(1, count), 6),
                "avg_delta_strain": round(sum(_to_float(item["delta_strain"]) for item in items) / max(1, count), 6),
                "avg_base_zentrum": round(sum(_to_float(item["base_zentrum"]) for item in items) / max(1, count), 6),
                "avg_base_rand": round(sum(_to_float(item["base_rand"]) for item in items) / max(1, count), 6),
                "avg_base_rekopplung": round(sum(_to_float(item["base_rekopplung"]) for item in items) / max(1, count), 6),
                "avg_base_strain": round(sum(_to_float(item["base_strain"]) for item in items) / max(1, count), 6),
            }
        )
    return summary


def _write_markdown(summary: list[dict[str, object]], detail_rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Weltlage-Rezeptorwirkung",
        "",
        "Passive Klassifikation der Weltlage aus Messwerten, nicht aus Dateinamen.",
        "",
        "Die Klassifikation nutzt Zentrum, Rand/Kipp, Rekopplung, Strain, Rohfeld, Ton und Sicht aus dem A-Zustand.",
        "",
        "## Zusammenfassung",
        "",
        "| Weltlage | Welten | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain | Basis Zentrum | Basis Rand |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            "| {worldlage} | {worlds} | {dominant_outcome} | {outcome_counts} | {avg_delta_zentrum:.4f} | {avg_delta_rand:.4f} | {avg_delta_rekopplung:.4f} | {avg_delta_strain:.4f} | {avg_base_zentrum:.4f} | {avg_base_rand:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Einzelwelten",
            "",
            "| Welt | Weltlage | Folge | dZentrum | dRand | dRekopplung | dStrain |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(detail_rows, key=lambda item: (str(item["worldlage"]), str(item["world"]))):
        lines.append(
            "| {world} | {worldlage} | {adaptation_outcome} | {delta_zentrum:.4f} | {delta_rand:.4f} | {delta_rekopplung:.4f} | {delta_strain:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Diese Diagnose ersetzt keine spaetere interne Erkennung. Sie prueft nur, ob eine Weltlage aus Messwerten grob lesbar ist.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "```text",
            "Dateiname -> darf nicht Grundlage der Mechanik sein.",
            "Messwerte -> duerfen Grundlage passiver Weltlagenlesung sein.",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1295_WELTLAGE_REZEPTORWIRKUNG.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1295_WELTLAGE_REZEPTORWIRKUNG.csv")
    parser.add_argument("--summary-out", default="docs/befunde/1001-2000/1001-1500/1295_WELTLAGE_REZEPTORWIRKUNG_SUMMARY.csv")
    args = parser.parse_args()

    detail_rows: list[dict[str, object]] = []
    for input_path in args.input or DEFAULT_INPUTS:
        for base, adapted in _pairs(_load(Path(input_path))):
            deltas = classify_adaptation_delta(base, adapted)
            detail_rows.append(
                {
                    "world": str(base.get("world", "") or "unknown"),
                    "worldlage": classify_worldlage(base),
                    "base_zentrum": _to_float(base.get("zentrum_ratio")),
                    "base_rand": _to_float(base.get("rand_ratio")),
                    "base_rekopplung": _to_float(base.get("avg_rekopplung")),
                    "base_strain": _to_float(base.get("avg_strain")),
                    **deltas,
                }
            )
    summary = _summarize(detail_rows)
    _write_csv(detail_rows, Path(args.csv_out))
    _write_csv(summary, Path(args.summary_out))
    _write_markdown(summary, detail_rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.summary_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
