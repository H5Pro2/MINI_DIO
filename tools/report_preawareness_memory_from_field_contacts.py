from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.preawareness_memory import build_preawareness_memory, update_preawareness_memory_file


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "preawareness_id",
        "preawareness_key",
        "lookback",
        "target_group",
        "chain",
        "assets",
        "asset_count",
        "dominant_field_contact_class",
        "dominant_sensory_class",
        "dominant_motion_class",
        "field_asset_share",
        "sensory_asset_share",
        "motion_asset_share",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "preawareness_quality",
        "boundary",
        "passive_only",
        "influences_action",
        "is_gate",
        "is_motoric",
        "is_entry_signal",
        "is_direction_signal",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            item = dict(row)
            item["assets"] = ";".join(item.get("assets", []) or [])
            writer.writerow({key: item.get(key, "") for key in fieldnames})


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_markdown(path: Path, snapshot: dict, memory_path: Path) -> None:
    roles = list(snapshot.get("roles", []) or [])
    lines = [
        "# 2040 - Passive Vorwahrnehmungs-Memory aus Feldkontaktrollen",
        "",
        "## Zweck",
        "",
        "Diese Auswertung überführt die assetbezogenen Vorphasen aus `2039` in eine passive Vorwahrnehmungs-Memory.",
        "",
        "Wichtig: Diese Memory speichert keine Handlung, keine Richtung, kein Gate und keine Entry-Mechanik. Sie speichert nur, welche MCM-Feldkontaktrollen vor Öffnung oder Rekopplung wiederkehrend lesbar wurden.",
        "",
        "## Übersicht",
        "",
        f"- Memory-Zustand: `{snapshot.get('memory_state', '-')}`",
        f"- Rollen: `{snapshot.get('role_count', 0)}`",
        f"- Detail-Zeilen aus 2039: `{snapshot.get('detail_row_count', 0)}`",
        f"- lokaler Speicher: `{memory_path}`",
        f"- Qualitätsverteilung: `{snapshot.get('quality_counts', {})}`",
        f"- Feldkontaktverteilung: `{snapshot.get('field_contact_counts', {})}`",
        "",
        "## Rollen",
        "",
        "| Rolle | Gruppe | Kette | Assets | Feldkontakt | Sinnesphase | Rohphase | Qualität | MCM |",
        "|---|---|---|---|---|---|---|---|---:|",
    ]
    for role in roles:
        lines.append(
            "| "
            f"`{role.get('preawareness_id', '-')}` | "
            f"`{role.get('target_group', '-')}` | "
            f"`{role.get('chain', '-')}` | "
            f"`{';'.join(role.get('assets', []) or [])}` | "
            f"`{role.get('dominant_field_contact_class', '-')}` ({float(role.get('field_asset_share', 0.0)):.2f}) | "
            f"`{role.get('dominant_sensory_class', '-')}` ({float(role.get('sensory_asset_share', 0.0)):.2f}) | "
            f"`{role.get('dominant_motion_class', '-')}` ({float(role.get('motion_asset_share', 0.0)):.2f}) | "
            f"`{role.get('preawareness_quality', '-')}` | "
            f"{float(role.get('avg_carry', 0.0)):.3f}/{float(role.get('avg_strain', 0.0)):.3f}/{float(role.get('avg_rekopplung', 0.0)):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "MINI_DIO erhält damit eine passive Vorwahrnehmungs-Spur: Feldkontaktrollen können wiedererkannt werden, ohne dass daraus sofort Verhalten entsteht.",
            "",
            "Die Memory trennt drei Ebenen:",
            "",
            "- Rohphase: wie die Außenwelt oberflächlich lief.",
            "- Sinnesphase: wie Sehen/Hören in dieser Vorphase ankoppelte.",
            "- Feldkontaktrolle: welche MCM-Wirkung als wiederkehrender Kontakt lesbar wurde.",
            "",
            "Der Mehrwert liegt nicht in einer neuen Regel, sondern in einer stabileren inneren Kartierung: Wenn ähnliche Feldkontaktrollen später wieder auftauchen, kann MINI_DIO sie als bekannte Feldnähe lesen, ohne sie als Entscheidung zu behandeln.",
            "",
            "## Grenze",
            "",
            "Diese Schicht bleibt passiv. Sie ist keine Vorhersage, kein Signal und keine Handlungsvorbereitung. Sie dokumentiert nur wiederkehrende Feldnähe.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Vorwahrnehmungs-Memory gegen neue reale Weltfenster geprüft werden. Entscheidend ist, ob dieselben Feldkontaktrollen wieder auftauchen, driften oder neue Rollen daneben entstehen.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stability",
        default="docs/befunde/2001-3000/2039_FELDFUNKTIONSWECHSEL_VORPHASEN_ASSET_STABILITAET.stability.csv",
    )
    parser.add_argument(
        "--summary",
        default="docs/befunde/2001-3000/2039_FELDFUNKTIONSWECHSEL_VORPHASEN_ASSET_STABILITAET.summary.csv",
    )
    parser.add_argument(
        "--memory",
        default="memory/preawareness/passive_field_contact_preawareness_memory.json",
    )
    parser.add_argument("--out-prefix", default="2040_FELDKONTAKT_VORWAHRNEHMUNG_MEMORY")
    args = parser.parse_args()

    stability_rows = _load_csv(Path(args.stability))
    detail_rows = _load_csv(Path(args.summary))
    snapshot = build_preawareness_memory(stability_rows, detail_rows)
    memory_path = Path(args.memory)
    memory_abs = memory_path if memory_path.is_absolute() else ROOT / memory_path
    memory = update_preawareness_memory_file(memory_abs, stability_rows, detail_rows)

    out_dir = befunde_root(ROOT)
    _write_csv(out_dir / f"{args.out_prefix}.roles.csv", snapshot.get("roles", []))
    _write_json(out_dir / f"{args.out_prefix}.snapshot.json", snapshot)
    _write_markdown(out_dir / f"{args.out_prefix}.md", snapshot, memory_path)

    print(f"roles={snapshot.get('role_count', 0)}")
    print(f"memory_roles={memory.get('role_count', 0)}")
    print(f"memory={memory_path}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
