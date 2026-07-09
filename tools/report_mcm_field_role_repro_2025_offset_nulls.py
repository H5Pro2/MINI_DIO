from __future__ import annotations

import csv
from collections import Counter

from report_mcm_field_role_repro_2025 import (
    ROOT,
    SOURCE_2024,
    _comparison_rows,
    _float,
    _mean,
    _phase_family_rows,
    _read_csv,
)


OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1843_MCM_FELDROLLEN_MEMORY_REPRO_2025_OFFSET_NULLKONTROLLE.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1843_MCM_FELDROLLEN_MEMORY_REPRO_2025_OFFSET_NULLKONTROLLE.md"

RUNS = [
    ("BTC", "offset17000_real_17k", "real", "debug/1842_repro_2025_offset/btc_2025_offset17000_real_17k/dio_mini_lauf_1"),
    ("BTC", "offset17000_random_17k", "null_random", "debug/1842_repro_2025_offset/btc_2025_offset17000_random_17k/dio_mini_lauf_1"),
    ("BTC", "offset17000_shuffle_17k", "null_shuffle", "debug/1842_repro_2025_offset/btc_2025_offset17000_shuffle_17k/dio_mini_lauf_1"),
    ("SOL", "offset17000_real_17k", "real", "debug/1842_repro_2025_offset/sol_2025_offset17000_real_17k/dio_mini_lauf_1"),
    ("SOL", "offset17000_random_17k", "null_random", "debug/1842_repro_2025_offset/sol_2025_offset17000_random_17k/dio_mini_lauf_1"),
    ("SOL", "offset17000_shuffle_17k", "null_shuffle", "debug/1842_repro_2025_offset/sol_2025_offset17000_shuffle_17k/dio_mini_lauf_1"),
]


def _write_csv(rows: list[dict[str, object]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _kind_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for kind in ["real", "null_random", "null_shuffle"]:
        group = [row for row in rows if row.get("kind") == kind]
        out.append(
            {
                "kind": kind,
                "worlds": len(group),
                "avg_kernfamilien": _mean([_float(row["kernfamilien"]) for row in group]),
                "avg_source_family_overlap": _mean([_float(row["source_family_overlap"]) for row in group]),
                "avg_source_kern_overlap": _mean([_float(row["source_kern_overlap"]) for row in group]),
                "avg_afterimage_delta": _mean([_float(row["avg_afterimage_delta"]) for row in group]),
                "avg_temporal_delta": _mean([_float(row["avg_temporal_delta"]) for row in group]),
                "states": "; ".join(f"{name}:{count}" for name, count in Counter(str(row["reproduction_state"]) for row in group).most_common()),
            }
        )
    return out


def _write_md(summary_rows: list[dict[str, object]], kind_rows: list[dict[str, object]]) -> None:
    real = next(row for row in kind_rows if row["kind"] == "real")
    random = next(row for row in kind_rows if row["kind"] == "null_random")
    shuffle = next(row for row in kind_rows if row["kind"] == "null_shuffle")
    source_edge = _float(real["avg_source_family_overlap"]) - max(
        _float(random["avg_source_family_overlap"]), _float(shuffle["avg_source_family_overlap"])
    )
    kern_edge = _float(real["avg_source_kern_overlap"]) - max(
        _float(random["avg_source_kern_overlap"]), _float(shuffle["avg_source_kern_overlap"])
    )
    lines = [
        "# 1843 - MCM-Feldrollen-Memory: 2025-Offset-Nullkontrolle",
        "",
        "## Grundfrage",
        "",
        "Bleibt der Realwelt-Vorsprung sichtbar, wenn BTC und SOL nicht am Jahresanfang, sondern ab Zeile 17.000 gelesen werden?",
        "",
        "## Gruppenvergleich",
        "",
        "| Gruppe | Welten | Kernfamilien Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in kind_rows:
        lines.append(
            f"| `{row['kind']}` | {row['worlds']} | {_float(row['avg_kernfamilien']):.2f} | "
            f"{_float(row['avg_source_family_overlap']):.3f} | {_float(row['avg_source_kern_overlap']):.3f} | "
            f"{_float(row['avg_afterimage_delta']):.4f} | {_float(row['avg_temporal_delta']):.4f} | `{row['states']}` |"
        )
    lines.extend(
        [
            "",
            "## Einzelwelten",
            "",
            "| Welt | Art | Kern | Quellennähe | Kernnähe | Nachhall-Delta | Feldzeit-Delta | Lesung |",
            "|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in summary_rows:
        lines.append(
            f"| {row['asset']} {row['label']} | `{row['kind']}` | {row['kernfamilien']} | "
            f"{_float(row['source_family_overlap']):.3f} | {_float(row['source_kern_overlap']):.3f} | "
            f"{_float(row['avg_afterimage_delta']):.4f} | {_float(row['avg_temporal_delta']):.4f} | `{row['reproduction_state']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Offset-Realwelten liegen in Quellennähe um `{source_edge:.3f}` über der stärksten Nullgruppe.",
            f"- Offset-Realwelten liegen in Kernnähe um `{kern_edge:.3f}` über der stärksten Nullgruppe.",
            "- Der Test ist kleiner als 1842, weil hier nur BTC und SOL als lange 2025-Jahresdateien verfügbar waren.",
            "- Der Realwelt-Vorsprung bleibt nicht einfach identisch; er muss je Fenster geprüft werden.",
            "",
            "Damit ist die bisherige Lesung vorsichtiger zu formulieren:",
            "Die Reifungsbahn bleibt sichtbar, aber die Trennung Realwelt/Nullwelt ist eine graduelle Feldqualität, kein harter Schnitt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte keine neue Mechanik eingebaut werden.",
            "Sinnvoll ist eine kompakte Gesamtübersicht aus 1841 bis 1843: was reproduziert, was nur graduell ist, und welche Aussage wissenschaftlich haltbar bleibt.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    source_rows = _read_csv(SOURCE_2024)
    detail_rows: list[dict[str, object]] = []
    kind_by_label: dict[tuple[str, str], str] = {}
    for asset, label, kind, run_dir in RUNS:
        kind_by_label[(asset, label)] = kind
        for row in _phase_family_rows(asset, label, run_dir):
            row["kind"] = kind
            detail_rows.append(row)
    summary_rows = _comparison_rows(source_rows, detail_rows)
    for row in summary_rows:
        row["kind"] = kind_by_label[(str(row["asset"]), str(row["label"]))]
    kind_rows = _kind_summary(summary_rows)
    _write_csv(
        [{**row, "row_type": "summary"} for row in summary_rows]
        + [{**row, "row_type": "kind_summary"} for row in kind_rows]
        + [{**row, "row_type": "detail"} for row in detail_rows]
    )
    _write_md(summary_rows, kind_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
