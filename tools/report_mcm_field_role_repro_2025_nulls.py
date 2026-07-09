from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from report_mcm_field_role_repro_2025 import (
    ROOT,
    SOURCE_2024,
    _comparison_rows,
    _float,
    _mean,
    _phase_family_rows,
    _read_csv,
)


OUT_CSV = ROOT / "docs/befunde/1001-2000/1751-2000/1842_MCM_FELDROLLEN_MEMORY_REPRO_2025_NULLKONTROLLE.csv"
OUT_MD = ROOT / "docs/befunde/1001-2000/1751-2000/1842_MCM_FELDROLLEN_MEMORY_REPRO_2025_NULLKONTROLLE.md"

RUNS = [
    ("BTC", "real_2025_17k", "real", "debug/1841_repro_2025/btc_2025_17k/dio_mini_lauf_1"),
    ("BTC", "random_2025_17k", "null_random", "debug/1841_repro_2025_null/btc_2025_random_17k/dio_mini_lauf_1"),
    ("BTC", "shuffle_2025_17k", "null_shuffle", "debug/1841_repro_2025_null/btc_2025_shuffle_17k/dio_mini_lauf_1"),
    ("SOL", "real_2025_17k", "real", "debug/1841_repro_2025/sol_2025_17k/dio_mini_lauf_1"),
    ("SOL", "random_2025_17k", "null_random", "debug/1841_repro_2025_null/sol_2025_random_17k/dio_mini_lauf_1"),
    ("SOL", "shuffle_2025_17k", "null_shuffle", "debug/1841_repro_2025_null/sol_2025_shuffle_17k/dio_mini_lauf_1"),
    ("DOGE", "real_2025_16992", "real", "debug/1841_repro_2025/doge_2025_16992/dio_mini_lauf_1"),
    ("DOGE", "random_2025_16992", "null_random", "debug/1841_repro_2025_null/doge_2025_random_16992/dio_mini_lauf_1"),
    ("DOGE", "shuffle_2025_16992", "null_shuffle", "debug/1841_repro_2025_null/doge_2025_shuffle_16992/dio_mini_lauf_1"),
    ("PAXG", "real_2025_16992", "real", "debug/1841_repro_2025/paxg_2025_16992/dio_mini_lauf_1"),
    ("PAXG", "random_2025_16992", "null_random", "debug/1841_repro_2025_null/paxg_2025_random_16992/dio_mini_lauf_1"),
    ("PAXG", "shuffle_2025_16992", "null_shuffle", "debug/1841_repro_2025_null/paxg_2025_shuffle_16992/dio_mini_lauf_1"),
    ("XRP", "real_2025_16992", "real", "debug/1841_repro_2025/xrp_2025_16992/dio_mini_lauf_1"),
    ("XRP", "random_2025_16992", "null_random", "debug/1841_repro_2025_null/xrp_2025_random_16992/dio_mini_lauf_1"),
    ("XRP", "shuffle_2025_16992", "null_shuffle", "debug/1841_repro_2025_null/xrp_2025_shuffle_16992/dio_mini_lauf_1"),
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
                "avg_oberflaechen": _mean([_float(row["oberflaechen"]) for row in group]),
                "avg_source_family_overlap": _mean([_float(row["source_family_overlap"]) for row in group]),
                "avg_source_kern_overlap": _mean([_float(row["source_kern_overlap"]) for row in group]),
                "avg_afterimage_delta": _mean([_float(row["avg_afterimage_delta"]) for row in group]),
                "avg_temporal_delta": _mean([_float(row["avg_temporal_delta"]) for row in group]),
                "states": "; ".join(f"{name}:{count}" for name, count in Counter(str(row["reproduction_state"]) for row in group).most_common()),
            }
        )
    return out


def _write_md(summary_rows: list[dict[str, object]], kind_rows: list[dict[str, object]], detail_rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1842 - MCM-Feldrollen-Memory: 2025-Nullkontrolle",
        "",
        "## Grundfrage",
        "",
        "Bleibt die passive Reifungsrollen-Lesung in echten 2025-Welten staerker als in assetnahen Random/Shuffle-Nullwelten?",
        "",
        "## Methode",
        "",
        "- Realwelten: BTC, SOL, DOGE, PAXG und XRP 2025.",
        "- Nullwelten: je Asset eine Random-Sign- und eine Shuffle-Order-Welt gleicher Laenge.",
        "- Bewertet wird nicht der Name einer Familie allein, sondern Reifungsprofil: Phase, Nachhall, Feldzeit, Strain und Quellennaehe.",
        "",
        "## Gruppenvergleich",
        "",
        "| Gruppe | Welten | Kernfamilien Ø | Oberfläche Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in kind_rows:
        lines.append(
            f"| `{row['kind']}` | {row['worlds']} | {_float(row['avg_kernfamilien']):.2f} | "
            f"{_float(row['avg_oberflaechen']):.2f} | {_float(row['avg_source_family_overlap']):.3f} | "
            f"{_float(row['avg_source_kern_overlap']):.3f} | {_float(row['avg_afterimage_delta']):.4f} | "
            f"{_float(row['avg_temporal_delta']):.4f} | `{row['states']}` |"
        )

    lines.extend(
        [
            "",
            "## Einzelwelten",
            "",
            "| Welt | Art | Kern | Oberfläche | Quellennähe | Kernnähe | Nachhall-Delta | Feldzeit-Delta | Lesung |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in summary_rows:
        lines.append(
            f"| {row['asset']} {row['label']} | `{row['kind']}` | {row['kernfamilien']} | {row['oberflaechen']} | "
            f"{_float(row['source_family_overlap']):.3f} | {_float(row['source_kern_overlap']):.3f} | "
            f"{_float(row['avg_afterimage_delta']):.4f} | {_float(row['avg_temporal_delta']):.4f} | `{row['reproduction_state']}` |"
        )

    real = next(row for row in kind_rows if row["kind"] == "real")
    random = next(row for row in kind_rows if row["kind"] == "null_random")
    shuffle = next(row for row in kind_rows if row["kind"] == "null_shuffle")
    real_edge = _float(real["avg_source_family_overlap"]) - max(
        _float(random["avg_source_family_overlap"]), _float(shuffle["avg_source_family_overlap"])
    )
    kern_edge = _float(real["avg_source_kern_overlap"]) - max(
        _float(random["avg_source_kern_overlap"]), _float(shuffle["avg_source_kern_overlap"])
    )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Realwelten liegen in Quellennähe um `{real_edge:.3f}` über der stärksten Nullgruppe.",
            f"- Realwelten liegen in Kernnähe um `{kern_edge:.3f}` über der stärksten Nullgruppe.",
            "- Die Nullwelten bilden ebenfalls stabile Oberflächen und einzelne Kernlesungen.",
            "- Der Unterschied liegt nicht in Ja/Nein, sondern in stärkerer Anschluss- und Kernnähe der realen Weltzeit.",
            "",
            "Damit ist der Befund kein einfacher Beweis gegen Rauschen, aber ein stärkerer Hinweis:",
            "MINI_DIO liest in realer Weltzeit mehr zusammenhängende Reifungsnähe als in assetnaher synthetischer Umordnung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte die Reifungsrollen-Memory nicht erweitert, sondern strenger geprüft werden:",
            "ein zweiter 2025-Ausschnitt mit anderem Startpunkt zeigt, ob dieselbe Differenz auch außerhalb des Jahresanfangs sichtbar bleibt.",
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
    csv_rows = [{**row, "row_type": "summary"} for row in summary_rows] + [
        {**row, "row_type": "kind_summary"} for row in kind_rows
    ] + [{**row, "row_type": "detail"} for row in detail_rows]
    _write_csv(csv_rows)
    _write_md(summary_rows, kind_rows, detail_rows)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
