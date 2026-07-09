from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_meaning_structure_memory import MCMMeaningStructureMemory


def _read_asset_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [
            row
            for row in csv.DictReader(handle)
            if str(row.get("group_type", "")) == "asset"
        ]


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    field_forms = sorted({str(row["field_form"]) for row in rows})
    lines = [
        "# Passive MCM-Bedeutungsstruktur",
        "",
        "Diese Datei verdichtet den balancierten Zwischenlagenbefund in eine passive Bedeutungsstruktur.",
        "",
        "Getrennt gespeichert werden:",
        "",
        "- Feldform",
        "- Assetfaerbung",
        "- dominante Lagefolge",
        "- Rohweltprofil",
        "- mehrskaliges Profil",
        "- Sinnesprofil",
        "",
        "Die Struktur ist passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.",
        "",
        "## Feldformen",
        "",
    ]
    for field_form in field_forms:
        lines.append(f"- `{field_form}`")

    lines.extend(
        [
            "",
            "## Bedeutungszeilen",
            "",
            "| Bedeutung | Feldform | Faerbung | Folge | Rohprofil | Sinnesprofil | Fenster |",
            "|---|---|---|---|---|---|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| `{meaning_key}` | `{field_form}` | `{asset_coloring}` | `{dominant_sequence}` | `{raw_profile}` | `{sensory_profile}` | {windows} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die Zwischenlage wird nicht als ein einzelner Rohwert gespeichert.",
            "",
            "Sie wird als zusammengesetzte Bedeutung gehalten:",
            "",
            "```text",
            "Feldform + Assetfaerbung + Folge + Rohprofil + Sinnesprofil",
            "```",
            "",
            "Damit kann MINI_DIO eine gemeinsame Feldbedeutung halten, ohne die Weltoberflaeche zu verlieren.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1001-2000/1001-1500/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1317_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1317_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.csv")
    args = parser.parse_args()

    memory = MCMMeaningStructureMemory()
    for row in _read_asset_rows(Path(args.input)):
        memory.observe_asset_row(row)
    rows = memory.rows()
    if not rows:
        raise RuntimeError("no meaning structure rows")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
