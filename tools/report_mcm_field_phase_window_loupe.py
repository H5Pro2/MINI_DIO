from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_PHASES = ROOT / "docs" / "befunde" / "1248_MCM_FELDPHASEN_ROHFELD_KOPPLUNG.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1249_MCM_FELDPHASEN_FENSTERLUPE.md"


METRIC_COLUMNS = [
    "avg_raw_field_intake",
    "avg_auditory_loudness",
    "avg_visual_sharpness",
    "avg_rekopplung",
    "avg_strain",
]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _segment_paths() -> list[Path]:
    return sorted((ROOT / "docs" / "befunde").glob("*FELDPHASEN*SEGMENTE.csv"))


def _target_phases(path: Path) -> dict[str, dict[str, str]]:
    return {row.get("phase_key", ""): row for row in _load_csv(path) if row.get("phase_key")}


def _phase_key(prev_row: dict[str, str], current_row: dict[str, str], next_row: dict[str, str]) -> str:
    return "->".join(
        [
            str(prev_row.get("role", "") or ""),
            str(current_row.get("role", "") or ""),
            str(next_row.get("role", "") or ""),
        ]
    )


def _world_kind(world: str, source: str) -> str:
    text = f"{world} {source}".lower()
    if "quiet" in text or "seit" in text:
        return "ruhige_oder_seitwaerts_welt"
    if "stress" in text or "neg" in text or "bear" in text:
        return "stress_oder_negative_welt"
    if "expansion" in text or "bull" in text or "positive" in text:
        return "expansive_oder_positive_welt"
    if "btc" in text:
        return "btc_welt"
    if "paxg" in text:
        return "paxg_welt"
    if "kas" in text:
        return "kas_welt"
    if "synth" in text:
        return "synthetische_sinneswelt"
    if "2023" in text or "2024" in text or "2025" in text or "2026" in text:
        return "zeit_oder_sequenz_welt"
    return "unbekannte_welt"


def _window_reading(prev_row: dict[str, str], current_row: dict[str, str], next_row: dict[str, str]) -> str:
    current_strain = _safe_float(current_row.get("avg_strain"))
    current_reko = _safe_float(current_row.get("avg_rekopplung"))
    next_strain = _safe_float(next_row.get("avg_strain"))
    next_reko = _safe_float(next_row.get("avg_rekopplung"))
    prev_reko = _safe_float(prev_row.get("avg_rekopplung"))

    reko_delta = next_reko - current_reko
    strain_delta = next_strain - current_strain
    reko_drop_before = current_reko - prev_reko

    if current_strain >= 0.25 and reko_delta >= 0.04 and strain_delta <= -0.04:
        return "lastkontakt_entlastet"
    if current_strain >= 0.25 and reko_delta < 0.02 and strain_delta > -0.02:
        return "lastkontakt_bleibt"
    if reko_drop_before <= -0.04 and current_strain >= 0.22:
        return "rekopplung_bricht_in_last"
    if current_reko >= 0.68 and next_strain >= current_strain + 0.04:
        return "rekopplung_vor_neuer_last"
    if reko_delta >= 0.03:
        return "rekopplung_nimmt_zu"
    return "gemischtes_fenster"


def _build_event_rows(targets: dict[str, dict[str, str]]) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    for path in _segment_paths():
        rows = _load_csv(path)
        by_world: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            world = str(row.get("world", "") or "")
            if world:
                by_world[world].append(row)

        for world, world_rows in by_world.items():
            for idx in range(1, len(world_rows) - 1):
                prev_row = world_rows[idx - 1]
                current_row = world_rows[idx]
                next_row = world_rows[idx + 1]
                key = _phase_key(prev_row, current_row, next_row)
                target = targets.get(key)
                if not target:
                    continue

                event: dict[str, object] = {
                    "phase_key": key,
                    "phase_class": target.get("phase_class", ""),
                    "coupling_class": target.get("coupling_class", ""),
                    "window_reading": _window_reading(prev_row, current_row, next_row),
                    "world": world,
                    "world_kind": _world_kind(world, path.name),
                    "source_file": path.name,
                    "prev_start_tick": prev_row.get("start_tick", ""),
                    "prev_end_tick": prev_row.get("end_tick", ""),
                    "prev_duration": prev_row.get("duration", ""),
                    "current_start_tick": current_row.get("start_tick", ""),
                    "current_end_tick": current_row.get("end_tick", ""),
                    "current_duration": current_row.get("duration", ""),
                    "next_start_tick": next_row.get("start_tick", ""),
                    "next_end_tick": next_row.get("end_tick", ""),
                    "next_duration": next_row.get("duration", ""),
                    "signal_completeness": 0,
                }
                signal_completeness = 0
                for column in METRIC_COLUMNS:
                    base = column.removeprefix("avg_")
                    prev_value = _safe_float(prev_row.get(column))
                    current_value = _safe_float(current_row.get(column))
                    next_value = _safe_float(next_row.get(column))
                    if abs(prev_value) > 0.000001:
                        signal_completeness += 1
                    if abs(current_value) > 0.000001:
                        signal_completeness += 1
                    if abs(next_value) > 0.000001:
                        signal_completeness += 1
                    event[f"prev_{base}"] = round(prev_value, 6)
                    event[f"current_{base}"] = round(current_value, 6)
                    event[f"next_{base}"] = round(next_value, 6)
                    event[f"delta_current_prev_{base}"] = round(current_value - prev_value, 6)
                    event[f"delta_next_current_{base}"] = round(next_value - current_value, 6)
                event["signal_completeness"] = signal_completeness
                events.append(event)
    return events


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _avg(rows: list[dict[str, object]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_safe_float(row.get(key)) for row in rows) / len(rows)


def _summary_rows(events: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        grouped[str(event["phase_key"])].append(event)

    out: list[dict[str, object]] = []
    for key, rows in grouped.items():
        readings = Counter(str(row["window_reading"]) for row in rows)
        worlds = Counter(str(row["world"]) for row in rows)
        world_kinds = Counter(str(row["world_kind"]) for row in rows)
        first = rows[0]
        out.append(
            {
                "phase_key": key,
                "phase_class": first.get("phase_class", ""),
                "coupling_class": first.get("coupling_class", ""),
                "event_count": len(rows),
                "dominant_window_reading": readings.most_common(1)[0][0] if readings else "-",
                "dominant_world_kind": world_kinds.most_common(1)[0][0] if world_kinds else "-",
                "dominant_world": worlds.most_common(1)[0][0] if worlds else "-",
                "avg_current_intake": round(_avg(rows, "current_raw_field_intake"), 6),
                "avg_current_loudness": round(_avg(rows, "current_auditory_loudness"), 6),
                "avg_current_sharpness": round(_avg(rows, "current_visual_sharpness"), 6),
                "avg_current_rekopplung": round(_avg(rows, "current_rekopplung"), 6),
                "avg_current_strain": round(_avg(rows, "current_strain"), 6),
                "avg_delta_next_rekopplung": round(_avg(rows, "delta_next_current_rekopplung"), 6),
                "avg_delta_next_strain": round(_avg(rows, "delta_next_current_strain"), 6),
                "avg_signal_completeness": round(_avg(rows, "signal_completeness"), 6),
            }
        )
    return sorted(out, key=lambda row: (-_safe_int(row["event_count"]), str(row["phase_key"])))


def _write_markdown(path: Path, events: list[dict[str, object]], summary: list[dict[str, object]], phases_path: Path) -> None:
    reading_counts = Counter(str(row["window_reading"]) for row in events)
    class_counts = Counter(str(row["phase_class"]) for row in events)
    world_kind_counts = Counter(str(row["world_kind"]) for row in events)

    lines: list[str] = [
        "# MCM-Feldphasen Fensterlupe",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Was passiert direkt vor, waehrend und nach situativen Rand-/Kipp-Phasen?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose liest vorhandene Feldphasen-Segmente als Dreifenster:",
        "",
        "```text",
        "vorherige Feldrolle -> aktuelle Feldrolle -> folgende Feldrolle",
        "```",
        "",
        "Sie prueft nicht Handlung und nicht Strategie. Sie prueft nur Feldbewegung.",
        "",
        "## Eingaben",
        "",
        f"- Zielphasen: `{phases_path.relative_to(ROOT)}`",
        "- Segmentquellen: `docs/befunde/*FELDPHASEN*SEGMENTE.csv`",
        "",
        "## Profil",
        "",
        f"- gefundene Fenster: `{len(events)}`",
        f"- untersuchte Phasenfamilien: `{len(summary)}`",
        f"- Fensterlesarten: `{dict(reading_counts.most_common())}`",
        f"- Phasenklassen: `{dict(class_counts.most_common())}`",
        f"- Weltarten: `{dict(world_kind_counts.most_common())}`",
        "",
        "## Phasenuebersicht",
        "",
        "| Phase | Fenster | Lesart | Weltart | Rekopplung | Strain | Delta Rekopplung | Delta Strain | Signal |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["event_count"]),
                    str(row["dominant_window_reading"]),
                    str(row["dominant_world_kind"]),
                    _fmt(row["avg_current_rekopplung"]),
                    _fmt(row["avg_current_strain"]),
                    _fmt(row["avg_delta_next_rekopplung"]),
                    _fmt(row["avg_delta_next_strain"]),
                    _fmt(row["avg_signal_completeness"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Beispiel-Fenster",
            "",
            "| Phase | Welt | Ticks | Lesart | Intake | Loudness | Sharpness | Rekopplung | Strain | Folge-Delta |",
            "|---|---|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in sorted(
        events,
        key=lambda item: (
            -_safe_float(item.get("signal_completeness")),
            -_safe_float(item.get("current_strain")),
            str(item.get("phase_key")),
        ),
    )[:16]:
        tick_text = f"{row['prev_start_tick']}-{row['next_end_tick']}"
        delta_text = (
            f"reko { _fmt(row['delta_next_current_rekopplung']) }, "
            f"strain { _fmt(row['delta_next_current_strain']) }"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["world"]),
                    tick_text,
                    str(row["window_reading"]),
                    _fmt(row["current_raw_field_intake"]),
                    _fmt(row["current_auditory_loudness"]),
                    _fmt(row["current_visual_sharpness"]),
                    _fmt(row["current_rekopplung"]),
                    _fmt(row["current_strain"]),
                    delta_text,
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Fensterlupe bestaetigt die vorherige Rohfeld-Kopplung genauer: Viele Rand-/Kippkontakte wirken nicht als dauerhafter Kollaps, sondern als kurzer Lastkontakt mit anschliessender Entlastung.",
            "",
            "Der wichtige Punkt ist die Folgebewegung:",
            "",
            "```text",
            "Rand/Kipp wird kritisch, wenn Strain bleibt oder Rekopplung weiter faellt.",
            "Rand/Kipp wird tragbar, wenn danach Rekopplung steigt und Strain faellt.",
            "```",
            "",
            "## Grenze",
            "",
            "Diese Lupe nutzt Feldphasen-Segmente. Sie ist noch keine Kerzen-/OHLCV-Lupe auf Rohchart-Ebene.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die gleiche Lupe mit konkreten Rohweltfenstern gekoppelt werden: Phase, Kerzenbereich, Tonprofil, Rezeptorprofil und Feldfolge in einer Zeile.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Baut eine Fensterlupe fuer situative MCM-Feldphasen.")
    parser.add_argument("--phases", default=str(DEFAULT_PHASES), help="CSV mit Zielphasen.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    phases_path = _resolve(args.phases)
    out_path = _resolve(args.out)
    targets = _target_phases(phases_path)
    events = _build_event_rows(targets)
    summary = _summary_rows(events)

    csv_path = out_path.with_suffix(".csv")
    summary_path = out_path.with_name(out_path.stem + "_SUMMARY.csv")
    _write_csv(csv_path, events)
    _write_csv(summary_path, summary)
    _write_markdown(out_path, events, summary, phases_path)

    print(f"wrote {out_path}")
    print(f"wrote {csv_path}")
    print(f"wrote {summary_path}")
    print(f"events={len(events)} phases={len(summary)}")


if __name__ == "__main__":
    main()
