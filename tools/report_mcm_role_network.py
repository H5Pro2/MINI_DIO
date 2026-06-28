from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mcm_role_network import MCMRoleNetwork


def _paths(values: list[str] | None) -> list[Path]:
    return [Path(value) for value in list(values or []) if str(value).strip()]


def _write_md(path: Path, network: MCMRoleNetwork) -> None:
    rows = network.to_rows()
    profile = network.quality_profile()
    lines: list[str] = [
        "# MCM-Rolennetzwerk: passive Feldkarte",
        "",
        "## Zweck",
        "",
        "Diese Datei haelt eine passive Netzwerkkarte aus Rollenbewegung, Rollenwechsel, Rollenreifung und gelesenen Nachbarschaften fest.",
        "Sie ist keine Handlungsschicht, kein Gate und keine Strategie.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Lesung",
        "- keine Entry-Wirkung",
        "- keine Richtungsvorgabe",
        "- keine Motorik",
        "- keine harte Regel",
        "",
        "## Profil",
        "",
        f"- Knoten: `{profile['records']}`",
        "",
        "### Netzwerkzustaende",
        "",
    ]
    for key, count in dict(profile.get("network_state", {})).items():
        lines.append(f"- `{key}`: {count}")

    lines.extend(
        [
            "",
            "## Staerkste Knoten",
            "",
            "| Symbol | Knoten | Zustand | Rolle | Bewegung | Shift | Stabilitaet | Drift | Nachbarn | Rekopplung | Strain |",
            "|---|---|---|---|---|---|---|---|---:|---:|---:|",
        ]
    )
    for row in rows[:32]:
        lines.append(
            f"| `{row['network_symbol']}` | `{row['node']}` | `{row['network_state']}` | `{row['dominant_role']}` | `{row['dominant_movement_quality']}` | `{row['dominant_shift_quality']}` | `{row['dominant_stability_quality']}` | `{row['dominant_drift_quality']}` | {row['neighbor_count']} | {row['avg_rekopplung']} | {row['avg_strain']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Das Rolennetzwerk liest nicht nur, ob ein Zeichen vorkommt.",
            "Es liest, welche Feldrolle ein Zeichen traegt, wie diese Rolle wandert, ob Nachbarschaft entsteht und ob der Knoten rekoppelt, driftet oder fragmentiert.",
            "",
            "Damit wird die aktuelle Arbeitsannahme technisch greifbar:",
            "",
            "```text",
            "Daten liegen nicht nur im Raum.",
            "Das MCM-Feld bildet ein dynamisches Bedeutungsnetz.",
            "```",
            "",
            "## Grenze",
            "",
            "Diese Netzwerkkarte darf nicht direkt handeln.",
            "Sie darf spaeter nur als gereifte passive Feldkarte fuer weitere Forschung gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, welche Bedingungen dazu fuehren, dass ein Knoten stabil bleibt, seine Rolle wechselt, driftet oder rekoppelt.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role-movement", action="append", default=[])
    parser.add_argument("--role-shift", action="append", default=[])
    parser.add_argument("--role-maturation", action="append", default=[])
    parser.add_argument("--bridge-network", action="append", default=[])
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    args = parser.parse_args()

    network = MCMRoleNetwork.from_sources(
        role_movement_csvs=_paths(args.role_movement),
        role_shift_csvs=_paths(args.role_shift),
        role_maturation_csvs=_paths(args.role_maturation),
        bridge_network_csvs=_paths(args.bridge_network),
    )
    network.write_csv(args.out_csv)
    network.write_json(args.out_json)
    _write_md(args.out_md, network)
    print(f"records={len(network.records)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_json}")


if __name__ == "__main__":
    main()
