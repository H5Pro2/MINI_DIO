from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_movement_memory import MCMRoleMovementMemory


def _table(rows: list[dict[str, object]], limit: int = 16) -> list[str]:
    lines = [
        "| Symbol | Token | Bewegung | Stabilitaet | Drift | Klassenfolge |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows[:limit]:
        lines.append(
            f"| `{row.get('role_symbol', '-')}` | `{row.get('short_token', '-')}` | {row.get('role_movement_quality', '-')} | {row.get('stability_quality', '-')} | {row.get('drift_quality', '-')} | {row.get('class_sequence', '-')} |"
        )
    return lines


def _profile_lines(profile: dict[str, object], key: str) -> list[str]:
    values = profile.get(key, {})
    if not isinstance(values, dict):
        return []
    return [f"- {name}: `{count}`" for name, count in values.items()]


def _write_md(path: Path, memory: MCMRoleMovementMemory) -> None:
    profile = memory.quality_profile()
    rows = sorted(
        memory.to_rows(),
        key=lambda row: (
            str(row.get("role_movement_quality", "")),
            -int(row.get("max_rank", 0) or 0),
            str(row.get("short_token", "")),
        ),
    )
    lines: list[str] = []
    lines.append("# MCM-Rollenbewegungs-Memory")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Datei uebersetzt die Mehrlandschafts-Rollenfolge aus 912 in eine passive semantische Memory-Struktur.")
    lines.append("Gespeichert wird nicht eine harte Klasse, sondern Rollenbewegung, Stabilitaet und Driftqualitaet.")
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
    lines.append("### Bewegungsqualitaet")
    lines.extend(_profile_lines(profile, "movement_quality"))
    lines.append("")
    lines.append("### Stabilitaetsqualitaet")
    lines.extend(_profile_lines(profile, "stability_quality"))
    lines.append("")
    lines.append("### Driftqualitaet")
    lines.extend(_profile_lines(profile, "drift_quality"))
    lines.append("")
    lines.append("## Beispielhafte Records")
    lines.append("")
    lines.extend(_table(rows))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Rollenfolge kann als semantische Bewegung gespeichert werden, ohne das Feld starr zu klassifizieren.")
    lines.append("Damit wird Mini-DIOs Memory naeher an der aktuellen MCM-Lesung gehalten:")
    lines.append("")
    lines.append("```text")
    lines.append("Nicht: dieses Zeichen ist immer X.")
    lines.append("Sondern: dieses Zeichen bewegte sich zwischen Rollen und trug dabei diese Stabilitaets- oder Driftqualitaet.")
    lines.append("```")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte diese passive Rollenbewegungs-Memory gegen neue Welten gelesen werden: bleibt ein role_symbol stabil, verdichtet es weiter, oder driftet es?")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    args = parser.parse_args()

    memory = MCMRoleMovementMemory.from_csv(args.roles)
    memory.write_csv(args.out_csv)
    memory.write_json(args.out_json)
    _write_md(args.out_md, memory)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
