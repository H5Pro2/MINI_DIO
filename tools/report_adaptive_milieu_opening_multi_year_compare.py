from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


FIELDS = [
    "family",
    "year",
    "world_hits",
    "occurrences",
    "hearing_delta",
    "tension_delta",
    "range_delta",
]


def read_summary(path: Path, year: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                {
                    "family": row["family"],
                    "year": year,
                    "world_hits": row.get("world_hits", "0"),
                    "occurrences": row.get("occurrences", "0"),
                    "hearing_delta": row.get("hearing_delta", "0"),
                    "tension_delta": row.get("tension_delta", "0"),
                    "range_delta": row.get("range_delta", "0"),
                }
            )
    return rows


def fmt(value: str) -> str:
    try:
        return f"{float(value):.6f}"
    except ValueError:
        return value


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_md(path: Path, rows: list[dict[str, str]], sources: list[tuple[str, Path]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# 1707 - Dreijahresvergleich Oeffnungs-Vorform")
    lines.append("")
    lines.append(f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose liest die Oeffnungs-Vorform ueber mehrere Jahres-/Weltgruppen. "
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung."
    )
    lines.append("")
    lines.append("## Hierarchie")
    lines.append("")
    lines.append("1. Grundfrage: Bleibt `milieu_oeffnet_nach_entlastung` ueber mehrere Weltjahre sichtbar?")
    lines.append("2. Unterpruefung: Delta Hoeren, Delta Spannung und Delta Range je Familie vergleichen.")
    lines.append("3. Folgeschritt: Gegen synthetische Kontrollwelten halten.")
    lines.append("")
    lines.append("## Vergleich")
    lines.append("")
    lines.append(
        "| Familie | Jahr | Welten mit Treffer | Vorkommen | Delta Hoeren | Delta Spannung | Delta Range |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["family"],
                    row["year"],
                    row["world_hits"],
                    row["occurrences"],
                    fmt(row["hearing_delta"]),
                    fmt(row["tension_delta"]),
                    fmt(row["range_delta"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Lesung")
    lines.append("")
    lines.append(
        "Wenn Hoeren- und Spannungsdelta ueber die Jahre negativ bleiben, wirkt die Form nicht wie ein einzelnes Fensterartefakt."
    )
    lines.append("")
    lines.append("Wichtig ist die Grenze:")
    lines.append("")
    lines.append("```text")
    lines.append("negatives Delta = Zielzeichen tritt nach hoeherer Vorlast auf")
    lines.append("das ist eine passive Entlastungslesung")
    lines.append("es ist keine Handlungsregel")
    lines.append("```")
    lines.append("")
    lines.append("## Quellen")
    lines.append("")
    for year, source in sources:
        lines.append(f"- {year}: `{source.as_posix()}`")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", nargs=2, action="append", metavar=("YEAR", "SUMMARY"), required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    sources = [(year, Path(summary)) for year, summary in args.source]
    rows: list[dict[str, str]] = []
    for year, summary in sources:
        rows.extend(read_summary(summary, year))

    out_md = Path(args.out_md)
    out_csv = out_md.with_suffix(".csv")
    write_csv(out_csv, rows)
    write_md(out_md, rows, sources)
    print({"out_md": str(out_md.resolve()), "out_csv": str(out_csv.resolve()), "rows": len(rows)})


if __name__ == "__main__":
    main()
