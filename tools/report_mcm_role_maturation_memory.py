from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_maturation_memory import MCMRoleMaturationMemory


def _profile_lines(profile: dict[str, object], key: str) -> list[str]:
    values = profile.get(key, {})
    if not isinstance(values, dict):
        return []
    return [f"- {name}: `{count}`" for name, count in values.items()]


def _table(rows: list[dict[str, object]], limit: int = 16) -> list[str]:
    lines = [
        "| Symbol | Token | Reifung | Segment | Feld | Folge |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows[:limit]:
        lines.append(
            f"| `{row.get('maturation_symbol', '-')}` | `{row.get('short_token', '-')}` | {row.get('maturation_quality', '-')} | {row.get('segment_quality', '-')} | {row.get('field_quality', '-')} | {row.get('follow_state', '-')} |"
        )
    return lines


def _write_md(path: Path, memory: MCMRoleMaturationMemory) -> None:
    profile = memory.quality_profile()
    rows = sorted(
        memory.to_rows(),
        key=lambda row: (
            str(row.get("maturation_quality", "")),
            str(row.get("segment_quality", "")),
            str(row.get("short_token", "")),
        ),
    )
    lines: list[str] = []
    lines.append("# MCM-Rollenreifungs-Memory")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Datei uebersetzt Reorganisationsfolge und Segmentlupe in eine passive Reifungs-Memory.")
    lines.append("Gespeichert wird nicht, was MINI_DIO tun soll, sondern ob eine Spur jung bleibt, reift, gehalten wird, belastet ist oder verschwindet.")
    lines.append("")
    lines.append("## Grenze")
    lines.append("")
    lines.append("Diese Memory-Schicht ist passiv:")
    lines.append("")
    lines.append("- keine Handlung,")
    lines.append("- kein Gate,")
    lines.append("- kein Entry-Signal,")
    lines.append("- keine Richtungsvorgabe,")
    lines.append("- keine motorische Steuerung.")
    lines.append("")
    lines.append("## Profil")
    lines.append("")
    lines.append(f"- Records: `{profile.get('records', 0)}`")
    lines.append("")
    lines.append("### Reifungsqualitaet")
    lines.extend(_profile_lines(profile, "maturation_quality"))
    lines.append("")
    lines.append("### Segmentqualitaet")
    lines.extend(_profile_lines(profile, "segment_quality"))
    lines.append("")
    lines.append("### Feldqualitaet")
    lines.extend(_profile_lines(profile, "field_quality"))
    lines.append("")
    lines.append("## Records")
    lines.append("")
    lines.extend(_table(rows))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Reifung ist als eigene passive Qualitaet speicherbar.")
    lines.append("Damit bleibt die Trennung erhalten:")
    lines.append("")
    lines.append("```text")
    lines.append("Rollenbewegung: welche Rolle bewegt sich wie?")
    lines.append("Reifungsbewegung: wird diese Bewegung jung gehalten, getragen, belastet, gereift oder entlastet?")
    lines.append("```")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte diese Reifungs-Memory gegen eine weitere Welt gelesen werden: bestaetigt sich `dio_mature_*`, oder veraendert sich die Reifungsqualitaet?")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--follow", required=True, type=Path)
    parser.add_argument("--segments", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    args = parser.parse_args()

    memory = MCMRoleMaturationMemory.from_csvs(args.follow, args.segments)
    memory.write_csv(args.out_csv)
    memory.write_json(args.out_json)
    _write_md(args.out_md, memory)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
