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

from mini_dio.preawareness_memory import (
    build_preawareness_state_memory,
    update_preawareness_state_memory_file,
)


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[dict]) -> None:
    fieldnames = [
        "preawareness_state_id",
        "preawareness_state_key",
        "target_group",
        "chain",
        "holdout_label",
        "holdout_asset",
        "events",
        "expected_field_contact_class",
        "observed_field_contact_class",
        "field_relation",
        "preawareness_state_quality",
        "field_recall_share",
        "sensory_recall_share",
        "motion_recall_share",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "boundary",
        "passive_only",
        "read_by_mini_dio",
        "influences_action",
        "is_gate",
        "is_motoric",
        "is_entry_signal",
        "is_direction_signal",
        "writes_runtime_memory",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _write_markdown(path: Path, snapshot: dict, memory_path: Path) -> None:
    states = list(snapshot.get("states", []) or [])
    lines = [
        "# 2043 - Passive Zustandsqualität der Vorwahrnehmung",
        "",
        "## Zweck",
        "",
        "Diese Auswertung führt die 2042-Landkarte passiv in eine Vorwahrnehmungs-Zustandsmemory zurück.",
        "",
        "Gespeichert wird nicht, was MINI_DIO tun soll. Gespeichert wird nur, wie eine bekannte Feldnähe in Holdout-Welten wieder auftaucht: stabil, teilstabil, umorganisiert oder driftend.",
        "",
        "## Übersicht",
        "",
        f"- Memory-Zustand: `{snapshot.get('memory_state', '-')}`",
        f"- Zustände: `{snapshot.get('state_count', 0)}`",
        f"- Detail-Zeilen aus 2042: `{snapshot.get('detail_row_count', 0)}`",
        f"- lokaler Speicher: `{memory_path}`",
        f"- Zustandsverteilung: `{snapshot.get('state_quality_counts', {})}`",
        f"- Feldrelationsverteilung: `{snapshot.get('field_relation_counts', {})}`",
        f"- Holdout-Assets: `{snapshot.get('holdout_asset_counts', {})}`",
        "",
        "## Zustände",
        "",
        "| Zustand | Gruppe | Kette | Holdout | Erwartet | Beobachtet | Relation | Rücklesung | MCM |",
        "|---|---|---|---|---|---|---|---:|---:|",
    ]
    for state in states:
        lines.append(
            "| "
            f"`{state.get('preawareness_state_quality', '-')}` | "
            f"`{state.get('target_group', '-')}` | "
            f"`{state.get('chain', '-')}` | "
            f"`{state.get('holdout_label', '-')}/{state.get('holdout_asset', '-')}` | "
            f"`{state.get('expected_field_contact_class', '-')}` | "
            f"`{state.get('observed_field_contact_class', '-')}` | "
            f"`{state.get('field_relation', '-')}` | "
            f"{float(state.get('field_recall_share', 0.0)):.3f}/"
            f"{float(state.get('sensory_recall_share', 0.0)):.3f}/"
            f"{float(state.get('motion_recall_share', 0.0)):.3f} | "
            f"{float(state.get('avg_carry', 0.0)):.3f}/"
            f"{float(state.get('avg_strain', 0.0)):.3f}/"
            f"{float(state.get('avg_rekopplung', 0.0)):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "MINI_DIO bekommt damit keine neue Entscheidungslogik, sondern eine passive Erinnerung an Zustandsqualität. Eine Rolle kann also später nicht nur als bekannt gelesen werden, sondern als bekannt-stabil, bekannt-teilstabil, bekannt-umorganisiert oder bekannt-driftend.",
            "",
            "Der wichtige Punkt ist die Trennung: Die Feldrolle bleibt Wahrnehmung und Gedächtnis. Sie wird nicht automatisch zu Handlung.",
            "",
            "## Grenze",
            "",
            "Diese Zustandsmemory ist keine Vorhersage, kein Signal, kein Gate, keine Richtung und kein Entry. Sie beschreibt ausschließlich die wiederholte oder veränderte Qualität einer Feldnähe.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte ein weiterer Holdout mit anderer Weltspannung gegen diese Zustandsmemory geprüft werden. Entscheidend ist, ob `umorganisierte_rekopplung` stabil als Umorganisation wiederkehrt oder ob daraus eine neue teilstabile Feldrolle entsteht.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--landscape",
        default="docs/befunde/2001-3000/2042_VORWAHRNEHMUNG_STABIL_DRIFT_LANDKARTE.detail.csv",
    )
    parser.add_argument(
        "--memory",
        default="memory/preawareness/passive_preawareness_state_quality_memory.json",
    )
    parser.add_argument("--out-prefix", default="2043_VORWAHRNEHMUNG_ZUSTANDSQUALITAET_MEMORY")
    args = parser.parse_args()

    landscape_rows = _load_csv(Path(args.landscape))
    snapshot = build_preawareness_state_memory(landscape_rows, landscape_rows)
    memory_path = Path(args.memory)
    memory_abs = memory_path if memory_path.is_absolute() else ROOT / memory_path
    memory = update_preawareness_state_memory_file(memory_abs, landscape_rows, landscape_rows)

    out_dir = befunde_root(ROOT)
    _write_csv(out_dir / f"{args.out_prefix}.states.csv", snapshot.get("states", []))
    _write_json(out_dir / f"{args.out_prefix}.snapshot.json", snapshot)
    _write_markdown(out_dir / f"{args.out_prefix}.md", snapshot, memory_path)

    print(f"states={snapshot.get('state_count', 0)}")
    print(f"memory_states={memory.get('state_count', 0)}")
    print(f"memory={memory_path}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
