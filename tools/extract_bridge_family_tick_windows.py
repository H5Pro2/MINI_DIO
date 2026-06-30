from __future__ import annotations

import argparse
import csv
from pathlib import Path

from report_bridge_family_event_examples import _matches
from report_bridge_family_rawworld_windows import (
    PATTERNS,
    _band,
    _field_label,
    _float,
    _iter_episode_files,
    _quantile,
    _role,
    _tone_label,
    _visual_label,
    _world_group,
)


WINDOW_COLUMNS = [
    "tick",
    "timestamp_ms",
    "symbol_family",
    "pattern_marker",
    "relative_pos",
    "visual_label",
    "tone_label",
    "field_label",
    "sehen_form_stability",
    "sehen_form_change",
    "hoeren_energy_tone",
    "hoeren_energy_shift",
    "perception_auditory_loudness",
    "perception_auditory_listen_tendency",
    "perception_visual_sharpness",
    "perception_visual_distance_tendency",
    "perception_raw_field_intake_pressure",
    "perception_adapted_field_intake_pressure",
    "mcm_feldwirkung_mcm_tension",
    "mcm_rekopplung_quality",
    "mcm_strain_quality",
]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _qs(rows: list[dict[str, str]]) -> dict[str, float]:
    tone_values = [_float(row, "hoeren_energy_tone") for row in rows]
    return {
        "tone_q33": _quantile(tone_values, 0.33),
        "tone_q66": _quantile(tone_values, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }


def _event_score(row: dict[str, str], pattern: str) -> float:
    tension = _float(row, "mcm_feldwirkung_mcm_tension")
    rekopplung = _float(row, "mcm_rekopplung_quality")
    strain = _float(row, "mcm_strain_quality")
    if pattern == "kippnaehe":
        return tension + strain - rekopplung
    return rekopplung - strain - tension


def _select_events(
    episode_files: list[Path],
    *,
    family: str,
    per_pattern: int,
) -> list[tuple[Path, int, str, float]]:
    candidates: list[tuple[Path, int, str, float]] = []
    for episode_file in episode_files:
        rows = _load(episode_file)
        if not rows:
            continue
        qs = _qs(rows)
        for idx, row in enumerate(rows):
            if (row.get("symbol_family") or "").strip() != family:
                continue
            for pattern in PATTERNS:
                if _matches(row, pattern, qs):
                    candidates.append((episode_file, idx, pattern, _event_score(row, pattern)))

    selected: list[tuple[Path, int, str, float]] = []
    for pattern in PATTERNS:
        pattern_candidates = [item for item in candidates if item[2] == pattern]
        selected.extend(sorted(pattern_candidates, key=lambda item: item[3], reverse=True)[:per_pattern])
    return selected


def _window_rows(
    event: tuple[Path, int, str, float],
    *,
    family: str,
    before: int,
    after: int,
    event_id: int,
) -> list[dict[str, object]]:
    episode_file, idx, pattern, score = event
    rows = _load(episode_file)
    start = max(0, idx - before)
    end = min(len(rows), idx + after + 1)
    out: list[dict[str, object]] = []
    for pos in range(start, end):
        row = rows[pos]
        marker = pattern if pos == idx else "-"
        item: dict[str, object] = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "event_id": event_id,
            "world_group": _world_group(episode_file),
            "world": episode_file.parent.parent.name,
            "run": episode_file.parent.name,
            "family": family,
            "event_pattern": pattern,
            "event_score": score,
            "pattern_marker": marker,
            "relative_pos": pos - idx,
            "visual_label": _visual_label(row),
            "tone_label": _tone_label(row),
            "field_label": _field_label(row),
        }
        for column in WINDOW_COLUMNS:
            if column in {"pattern_marker", "relative_pos", "visual_label", "tone_label", "field_label"}:
                continue
            if column in {"tick"}:
                item[column] = int(_float(row, column))
            else:
                item[column] = row.get(column, "")
        out.append(item)
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _report_title(path: Path, fallback: str) -> str:
    stem = path.stem
    if "_" not in stem:
        return fallback
    prefix, rest = stem.split("_", 1)
    if not prefix.isdigit():
        return fallback
    return f"{prefix} - {rest.replace('_', ' ').title()}"


def _write_md(rows: list[dict[str, object]], path: Path, family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    events: dict[int, list[dict[str, object]]] = {}
    for row in rows:
        events.setdefault(int(row["event_id"]), []).append(row)

    lines = [
        f"# {_report_title(path, f'Tickfenster Brueckenfamilie {family}')}",
        "",
        "Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Wie sieht der Vorlauf, Ereignispunkt und Nachlauf einer realen Brueckenfamilie aus?",
        "",
        "## Extrahierte Fenster",
        "",
    ]
    for event_id, event_rows in sorted(events.items()):
        event_row = next(row for row in event_rows if row["relative_pos"] == 0)
        lines.extend(
            [
                f"### Fenster {event_id}: {event_row['event_pattern']} / {event_row['world']} / Tick {event_row['tick']}",
                "",
                "| Rel | Tick | Marker | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake |",
                "|---:|---:|---|---|---|---|---:|---:|---:|---:|---:|",
            ]
        )
        for row in event_rows:
            lines.append(
                "| {relative_pos} | {tick} | {pattern_marker} | {visual_label} | {tone_label} | {field_label} | {mcm_feldwirkung_mcm_tension:.4f} | {mcm_rekopplung_quality:.4f} | {mcm_strain_quality:.4f} | {perception_raw_field_intake_pressure:.4f} | {perception_adapted_field_intake_pressure:.4f} |".format(
                    **{
                        **row,
                        "mcm_feldwirkung_mcm_tension": _float(row, "mcm_feldwirkung_mcm_tension"),
                        "mcm_rekopplung_quality": _float(row, "mcm_rekopplung_quality"),
                        "mcm_strain_quality": _float(row, "mcm_strain_quality"),
                        "perception_raw_field_intake_pressure": _float(row, "perception_raw_field_intake_pressure"),
                        "perception_adapted_field_intake_pressure": _float(
                            row, "perception_adapted_field_intake_pressure"
                        ),
                    }
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Lesart",
            "",
            "Die Fenster zeigen, ob eine Brueckenfamilie aus dem Vorlauf heraus in Rekopplung oder in Kippnaehe laeuft.",
            "",
            "Damit wird die Realitaetsrueckkopplung konkret: Nicht der Name der Familie entscheidet, sondern die Feldfolge um den Kontaktpunkt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Fenstern eine kompakte Feldfolgen-Signatur abgeleitet werden: welche Vorlauf-Merkmale gehen rekoppelnden gegen kippnahen Lesarten voraus?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--family", required=True)
    parser.add_argument("--before", type=int, default=6)
    parser.add_argument("--after", type=int, default=6)
    parser.add_argument("--per-pattern", type=int, default=3)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    episode_files = _iter_episode_files([Path(item) for item in args.world_dir])
    events = _select_events(episode_files, family=args.family, per_pattern=args.per_pattern)
    rows: list[dict[str, object]] = []
    for event_id, event in enumerate(events, start=1):
        rows.extend(
            _window_rows(event, family=args.family, before=args.before, after=args.after, event_id=event_id)
        )
    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md), args.family)
    print(f"events={len(events)}")
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
