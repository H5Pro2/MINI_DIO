from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_shift_memory import MCMRoleShiftMemory


def _write_md(path: Path, memory: MCMRoleShiftMemory) -> None:
    rows = memory.to_rows()
    profile = memory.quality_profile()
    lines: list[str] = [
        "# MCM-Rollenwechsel-Memory",
        "",
        "## Zweck",
        "",
        "Diese Datei speichert passiv, wenn ein bekanntes MCM-Zeichen seine Rolle wechselt.",
        "Sie beschreibt keine Handlung, kein Gate und keine Richtung.",
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
        "### Wechselqualitaeten",
        "",
    ]
    for key, count in dict(profile.get("shift_quality", {})).items():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "### Zielrollen",
            "",
        ]
    )
    for key, count in dict(profile.get("to_nonbridge_class", {})).items():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "## Records",
            "",
            "| Shift | Token | Von | Nach | Beobachtungen | Welten | Note |",
            "|---|---|---|---|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['shift_symbol']}` | `{row['short_token']}` | `{row['from_longterm_class']}` / `{row['from_role_class']}` | `{row['to_nonbridge_class']}` / `{row['to_zone']}` | {row['observations']} | {row['worlds']} | {row['shift_note']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Rollenwechsel-Memory trennt Bedeutungsverlust von Rollenverlust.",
            "Ein Zeichen kann als Bruecke verschwinden und trotzdem als Zentrum, Rand, Rekopplungsfeld oder offene Oberflaeche erhalten bleiben.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese `dio_shift_*` Memory gegen eine weitere Welt gelesen werden.",
            "Dann wird sichtbar, ob Rollenwechsel selbst wiederkehrend sind oder nur eine einmalige Umlagerung der siebten Welt darstellen.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    args = parser.parse_args()

    memory = MCMRoleShiftMemory.from_csv(args.input)
    memory.write_csv(args.out_csv)
    memory.write_json(args.out_json)
    _write_md(args.out_md, memory)
    print(f"records={len(memory.records)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
