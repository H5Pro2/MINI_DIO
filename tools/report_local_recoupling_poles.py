from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from report_recoupling_quality import _row as recoupling_row
from report_recoupling_quality import _load_json, _resolve


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "214_LOKALE_REKOPPLUNGSPOLE_DIAGNOSE.md"


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _group_label(name: str) -> str:
    lowered = name.lower()
    if "quiet" in lowered or "ruhe" in lowered:
        return "ruhe"
    if "stress" in lowered:
        return "stress"
    return "sonstige"


def _contrast_score(row: dict) -> float:
    return float(row["binding_sum"]) - float(row["reiz_aktiv_rekoppelnd"])


def _write_csv(rows: list[dict], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "name",
                "group",
                "role",
                "rekopplung",
                "field_strain",
                "memory_load",
                "attention_load",
                "afterimage_load",
                "active",
                "binding_sum",
                "contrast",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "name": row["name"],
                    "group": row["group"],
                    "role": row["dominant_role"],
                    "rekopplung": _fmt(row["rekopplung"], 6),
                    "field_strain": _fmt(row["field_strain"], 6),
                    "memory_load": _fmt(row["memory_load"], 6),
                    "attention_load": _fmt(row["attention_load"], 6),
                    "afterimage_load": _fmt(row["afterimage_load"], 6),
                    "active": _fmt(row["reiz_aktiv_rekoppelnd"], 6),
                    "binding_sum": _fmt(row["binding_sum"], 6),
                    "contrast": _fmt(_contrast_score(row), 6),
                }
            )


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))
    _write_csv(rows, out_path)

    group_counts: dict[str, Counter] = {}
    for row in rows:
        group_counts.setdefault(row["group"], Counter())[row["dominant_role"]] += 1

    stress_rows = [row for row in rows if row["group"] == "stress"]
    quiet_rows = [row for row in rows if row["group"] == "ruhe"]
    strongest_binding = sorted(rows, key=lambda row: row["binding_sum"], reverse=True)[:6]
    strongest_active = sorted(rows, key=lambda row: row["reiz_aktiv_rekoppelnd"], reverse=True)[:6]

    lines = [
        "# Lokale Rekopplungspole - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft lokale Stresssegmente gegen lokale Ruhe-/Entlastungssegmente.",
        "Sie nutzt die bestehende Rekopplungsrollen-Lesung und erzeugt keine neue Runtime-Mechanik.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Treten `last_memory_bindend` und `reiz_aktiv_rekoppelnd` als lokale Gegenpole auf?",
        "2. Unterpruefung: Stresssegmente gegen Quiet-Segmente vergleichen.",
        "3. Folgeschritt: Entscheiden, ob lokale Rekopplungspole eine stabile passive MCM-Landkarte bilden.",
        "",
        "## Rollen nach Gruppe",
        "",
        "| Gruppe | Rolle | Anzahl |",
        "|---|---|---:|",
    ]
    for group in sorted(group_counts):
        for role, count in group_counts[group].most_common():
            lines.append(f"| {group} | {role} | {count} |")

    lines.extend(
        [
            "",
            "## Einzelwerte",
            "",
            "| Welt | Gruppe | Rolle | Rekopplung | Feldlast | Memorylast | Aufmerksamkeit | aktiv-rekoppelnd | Bindungssumme | Kontrast Bindung-Aktiv |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["dominant_role"],
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["attention_load"], 4),
                    _fmt(row["reiz_aktiv_rekoppelnd"], 4),
                    _fmt(row["binding_sum"], 4),
                    _fmt(_contrast_score(row), 4),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Staerkste Bindung", ""])
    for row in strongest_binding:
        lines.append(
            f"- `{row['name']}` ({row['group']}): Rolle `{row['dominant_role']}`, "
            f"Bindung `{_fmt(row['binding_sum'], 4)}`, Aktiv `{_fmt(row['reiz_aktiv_rekoppelnd'], 4)}`, "
            f"Kontrast `{_fmt(_contrast_score(row), 4)}`"
        )

    lines.extend(["", "## Staerkste aktive Rekopplung", ""])
    for row in strongest_active:
        lines.append(
            f"- `{row['name']}` ({row['group']}): Rolle `{row['dominant_role']}`, "
            f"Aktiv `{_fmt(row['reiz_aktiv_rekoppelnd'], 4)}`, Bindung `{_fmt(row['binding_sum'], 4)}`"
        )

    if stress_rows and quiet_rows:
        avg_stress_contrast = sum(_contrast_score(row) for row in stress_rows) / len(stress_rows)
        avg_quiet_contrast = sum(_contrast_score(row) for row in quiet_rows) / len(quiet_rows)
        avg_stress_field = sum(row["field_strain"] for row in stress_rows) / len(stress_rows)
        avg_quiet_field = sum(row["field_strain"] for row in quiet_rows) / len(quiet_rows)
        lines.extend(
            [
                "",
                "## Gruppenvergleich",
                "",
                f"- Stress-Kontrast Bindung-Aktiv: `{_fmt(avg_stress_contrast, 4)}`",
                f"- Ruhe-Kontrast Bindung-Aktiv: `{_fmt(avg_quiet_contrast, 4)}`",
                f"- Stress-Feldlast: `{_fmt(avg_stress_field, 4)}`",
                f"- Ruhe-Feldlast: `{_fmt(avg_quiet_field, 4)}`",
            ]
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Lokale Rekopplungspole sind nur dann plausibel, wenn Stresssegmente systematisch mehr Bindung und Ruhe-/Entlastungssegmente systematisch mehr aktive Rekopplung zeigen.",
            "",
            "Der Kontrast `Bindung-Aktiv` ist dabei die einfache passive Lesegroesse:",
            "",
            "```text",
            "negativ -> aktive Rekopplung dominiert",
            "positiv -> Feld-/Memorybindung dominiert",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird aus dieser Diagnose ein Befund geschrieben.",
            "Darin wird bewertet, ob lokale Stress- und Ruheabschnitte wirklich als MCM-Gegenpole gelesen werden koennen.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Vergleicht lokale Stress- und Ruhe-Rekopplungspole.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        row = recoupling_row(name, _load_json(_resolve(path_text)))
        row["group"] = _group_label(name)
        rows.append(row)
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
