from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_fragmentation_memory import MCMFragmentationMemory


def _write_md(path: Path, memory: MCMFragmentationMemory) -> None:
    rows = memory.to_rows()
    profile = memory.quality_profile()
    lines: list[str] = [
        "# MCM-Fragmentierungs-Memory",
        "",
        "## Zweck",
        "",
        "Diese Datei speichert passiv den Oberflaechenzustand einer Weltgruppe.",
        "Sie speichert keine Handlung, keine Richtung und kein Gate.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passiv only",
        "- keine Entry-Wirkung",
        "- keine Motorik",
        "- keine Richtungsvorgabe",
        "- keine harte Regel",
        "",
        "## Profil",
        "",
        f"- Records: `{profile['records']}`",
        "",
        "### Fragmentierungsklassen",
        "",
    ]
    for key, count in dict(profile.get("fragmentation_class", {})).items():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "## Records",
            "",
            "| Symbol | Welt | Klasse | Zonen | junge Spuren | dominant | sekundaer | Rand | schwaches Zentrum | Rekopplung |",
            "|---|---|---|---:|---:|---|---|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['fragmentation_symbol']}` | `{row['world_label']}` | `{row['fragmentation_class']}` | {row['zones_total']} | {row['young_spur_count']} | `{row['dominant_surface_class']}` | `{row['secondary_surface_class']}` | {row['rand_count']} | {row['weak_center_count']} | {row['rekopplung_count']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Fragmentierungs-Memory beschreibt, wie stark eine Weltoberflaeche in junge, offene, randnahe oder schwach zentrierte Spuren zerfaellt.",
            "Damit wird eine dritte Ordnungsart neben Brueckenordnung und Rollenwechselordnung lesbar.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese `dio_frag_*` Memory gegen eine weitere Welt gelesen werden.",
            "Dann wird sichtbar, ob Fragmentierung eine stabile Weltklasse ist oder ob aus ihr spaeter wieder Rollenbindung entsteht.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-label", required=True)
    parser.add_argument("--nonbridge", required=True, type=Path)
    parser.add_argument("--zones", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    args = parser.parse_args()

    memory = MCMFragmentationMemory.from_csvs(args.world_label, args.nonbridge, args.zones)
    memory.write_csv(args.out_csv)
    memory.write_json(args.out_json)
    _write_md(args.out_md, memory)
    print(f"records={len(memory.records)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
