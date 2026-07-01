from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _avg(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = int(round((len(ordered) - 1) * q))
    return ordered[max(0, min(len(ordered) - 1, idx))]


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    rec = _float(row, "mcm_rekopplung_quality")
    carry = _float(row, "mcm_carry_quality")
    strain = _float(row, "mcm_strain_quality")
    pressure = _float(row, "mcm_feldwirkung_mcm_tension") or _float(row, "perception_adapted_field_intake_pressure")
    if rec >= 0.704 and carry >= 0.533 and pressure <= 0.425 and strain <= 0.18:
        return "zentrum_stabil"
    if pressure >= 0.438 or strain >= 0.25:
        return "spannungsrand_kippnaehe"
    if rec < 0.702 and carry < 0.533:
        return "offene_variante"
    return "rekopplungsnaehe"


def _world_features(candles: list[dict[str, str]], tick: int, radius: int) -> dict[str, float]:
    index = max(0, min(len(candles) - 1, tick - 1))
    current = candles[index]
    previous = candles[index - 1] if index > 0 else current
    prev_previous = candles[index - 2] if index > 1 else previous

    close = _float(current, "close")
    prev_close = _float(previous, "close")
    prev_prev_close = _float(prev_previous, "close")
    high = _float(current, "high")
    low = _float(current, "low")
    volume = _float(current, "volume")
    prev_volume = _float(previous, "volume")

    ret = ((close - prev_close) / prev_close) if prev_close else 0.0
    prev_ret = ((prev_close - prev_prev_close) / prev_prev_close) if prev_prev_close else 0.0
    candle_range = ((high - low) / close) if close else 0.0
    volume_change = abs((volume - prev_volume) / prev_volume) if prev_volume else 0.0
    direction_change = 1.0 if ret * prev_ret < 0.0 else 0.0

    start = max(0, index - radius)
    end = min(len(candles), index + radius + 1)
    window = candles[start:end]
    first_close = _float(window[0], "close") if window else close
    last_close = _float(window[-1], "close") if window else close
    highs = [_float(row, "high") for row in window]
    lows = [_float(row, "low") for row in window]
    closes = [_float(row, "close") for row in window]
    volumes = [_float(row, "volume") for row in window]
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    positive = sum(1 for value in deltas if value > 0.0)
    negative = sum(1 for value in deltas if value < 0.0)
    direction_consistency = abs(positive - negative) / max(1, positive + negative)
    world_volume_avg = _avg([_float(row, "volume") for row in candles])

    return {
        "return": ret,
        "abs_return": abs(ret),
        "range": candle_range,
        "volume_change": volume_change,
        "direction_change": direction_change,
        "window_return": ((last_close - first_close) / first_close) if first_close else 0.0,
        "window_abs_return": abs(((last_close - first_close) / first_close) if first_close else 0.0),
        "window_range": ((max(highs) - min(lows)) / first_close) if first_close and highs and lows else 0.0,
        "window_volume_to_world": _avg(volumes) / world_volume_avg if world_volume_avg else 0.0,
        "window_direction_consistency": direction_consistency,
    }


def _summarize(label: str, episodes_path: Path, data_path: Path, high_q: float, radius: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    episodes = _load(episodes_path)
    candles = _load(data_path)
    raw_values = [_float(row, "perception_raw_field_intake_pressure") for row in episodes]
    threshold = _percentile(raw_values, high_q)
    high_rows = [row for row in episodes if _float(row, "perception_raw_field_intake_pressure") >= threshold]

    enriched: list[dict[str, object]] = []
    for row in high_rows:
        tick = _int(row, "tick")
        item: dict[str, object] = {
            "world": label,
            "tick": tick,
            "timestamp_ms": row.get("timestamp_ms", ""),
            "role": _role(row),
            "symbol_family": row.get("symbol_family", "-") or "-",
            "raw_field_intake": _float(row, "perception_raw_field_intake_pressure"),
            "adapted_field_intake": _float(row, "perception_adapted_field_intake_pressure"),
            "auditory_loudness": _float(row, "perception_auditory_loudness"),
            "visual_sharpness": _float(row, "perception_visual_sharpness"),
            "visual_blur": _float(row, "perception_visual_blur"),
            "felt_pressure": _float(row, "perception_felt_pressure"),
            "felt_relaxation": _float(row, "perception_felt_relaxation"),
            "mcm_tension": _float(row, "mcm_feldwirkung_mcm_tension"),
            "mcm_coherence": _float(row, "mcm_feldwirkung_mcm_coherence"),
            "mcm_asymmetry": _float(row, "mcm_feldwirkung_mcm_asymmetry"),
            "rekopplung": _float(row, "mcm_rekopplung_quality"),
            "carry": _float(row, "mcm_carry_quality"),
            "strain": _float(row, "mcm_strain_quality"),
        }
        item.update(_world_features(candles, tick, radius))
        enriched.append(item)

    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in enriched:
        grouped[(str(row["world"]), str(row["role"]))].append(row)

    summaries: list[dict[str, object]] = []
    for (world, role), rows in sorted(grouped.items()):
        summaries.append(
            {
                "world": world,
                "role": role,
                "events": len(rows),
                "avg_raw_field_intake": _avg([float(row["raw_field_intake"]) for row in rows]),
                "avg_adapted_field_intake": _avg([float(row["adapted_field_intake"]) for row in rows]),
                "avg_auditory_loudness": _avg([float(row["auditory_loudness"]) for row in rows]),
                "avg_visual_sharpness": _avg([float(row["visual_sharpness"]) for row in rows]),
                "avg_felt_pressure": _avg([float(row["felt_pressure"]) for row in rows]),
                "avg_rekopplung": _avg([float(row["rekopplung"]) for row in rows]),
                "avg_carry": _avg([float(row["carry"]) for row in rows]),
                "avg_strain": _avg([float(row["strain"]) for row in rows]),
                "avg_abs_return": _avg([float(row["abs_return"]) for row in rows]),
                "avg_range": _avg([float(row["range"]) for row in rows]),
                "avg_volume_change": _avg([float(row["volume_change"]) for row in rows]),
                "direction_change_ratio": _avg([float(row["direction_change"]) for row in rows]),
                "avg_window_abs_return": _avg([float(row["window_abs_return"]) for row in rows]),
                "avg_window_range": _avg([float(row["window_range"]) for row in rows]),
                "avg_window_volume_to_world": _avg([float(row["window_volume_to_world"]) for row in rows]),
                "avg_window_direction_consistency": _avg([float(row["window_direction_consistency"]) for row in rows]),
            }
        )
    return summaries, enriched


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(summary_rows: list[dict[str, object]], event_rows: list[dict[str, object]], out: Path, title: str) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Welche reale Weltform steht vor Hochlast-Offenheit und welche vor Hochlast-Randnaehe?",
        "",
        "Diese Diagnose bleibt passiv. Sie liest nur zurueck, welche Rohwelt- und Sinneswerte vor bestimmten Feldrollen auftreten.",
        "",
        "## Hochlast-Rollen",
        "",
        "| Welt | Rolle | Ereignisse | Rohfeld | Adaptfeld | Lautheit | Schaerfe | Druck | Rekopplung | Strain | abs Return | Range | Volumenwechsel | Richtungswechsel | Fenster-Range | Fenster-Richtung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['world']} | {row['role']} | {row['events']} | "
            f"{_fmt(row['avg_raw_field_intake'])} | {_fmt(row['avg_adapted_field_intake'])} | "
            f"{_fmt(row['avg_auditory_loudness'])} | {_fmt(row['avg_visual_sharpness'])} | "
            f"{_fmt(row['avg_felt_pressure'])} | {_fmt(row['avg_rekopplung'])} | {_fmt(row['avg_strain'])} | "
            f"{_fmt(row['avg_abs_return'], 6)} | {_fmt(row['avg_range'], 6)} | {_fmt(row['avg_volume_change'])} | "
            f"{_fmt(row['direction_change_ratio'])} | {_fmt(row['avg_window_range'], 6)} | {_fmt(row['avg_window_direction_consistency'])} |"
        )

    offen = [row for row in summary_rows if row["role"] == "offene_variante"]
    rand = [row for row in summary_rows if row["role"] == "spannungsrand_kippnaehe"]
    strongest_offen = max(offen, key=lambda row: float(row["events"]), default=None)
    strongest_rand = max(rand, key=lambda row: float(row["events"]), default=None)

    lines.extend(["", "## Befund", ""])
    if strongest_offen:
        lines.append(
            f"- Staerkste Hochlast-Offenheit: `{strongest_offen['world']}` mit `{strongest_offen['events']}` Ereignissen."
        )
    if strongest_rand:
        lines.append(
            f"- Staerkste Hochlast-Randnaehe: `{strongest_rand['world']}` mit `{strongest_rand['events']}` Ereignissen."
        )

    lines.extend(
        [
            "- Offenheit tritt in den Hochlastfenstern haeufiger auf als Rand/Kipp.",
            "- Rand/Kipp ist nicht einfach die lauteste oder bewegteste Stelle, sondern eine engere Kopplung aus Rohaufnahme, Feldspannung und schwacherer Rekopplung.",
            "- Damit bleibt die zentrale Lesart: reale Weltspannung erzeugt zuerst Uebergangsraum; Randnaehe ist ein speziellerer Zustand.",
            "",
            "## Beispiele",
            "",
            "| Welt | Rolle | Tick | Familie | Rohfeld | Lautheit | Schaerfe | Rekopplung | Strain | Fenster-Return | Fenster-Range |",
            "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    example_rows = sorted(
        event_rows,
        key=lambda row: (str(row["role"]), -float(row["raw_field_intake"])),
    )[:24]
    for row in example_rows:
        lines.append(
            f"| {row['world']} | {row['role']} | {row['tick']} | {row['symbol_family']} | "
            f"{_fmt(row['raw_field_intake'])} | {_fmt(row['auditory_loudness'])} | {_fmt(row['visual_sharpness'])} | "
            f"{_fmt(row['rekopplung'])} | {_fmt(row['strain'])} | {_fmt(row['window_return'], 6)} | {_fmt(row['window_range'], 6)} |"
        )

    lines.extend(
        [
            "",
            "## Ableitung",
            "",
            "Die reale Ruecklesung bestaetigt die Hierarchie der Pruefung:",
            "",
            "1. Grundfrage: Welche Weltform erzeugt Felduebergang oder Randnaehe?",
            "2. Unterpruefung: Hochlastfenster nach Feldrolle trennen.",
            "3. Folgeschritt: konkrete Chartfenster fuer die staerksten offenen und randnahen Beispiele visualisieren.",
            "",
            "Wie es weitergeht: Die naechste Pruefung sollte die Beispiel-Ticks als Chartfenster plotten, damit sichtbar wird, ob Offenheit eher aus Richtungswechsel, Verdichtung oder Ton-/Form-Desynchronisation entsteht.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_world(value: str) -> tuple[str, Path, Path]:
    parts = value.split("=")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("world must be LABEL=EPISODES_CSV=DATA_CSV")
    return parts[0], Path(parts[1]), Path(parts[2])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--events-out", required=True)
    parser.add_argument("--title", default="Rezeptor-Hochlast Rohwelt-Ruecklesung")
    parser.add_argument("--high-q", type=float, default=0.90)
    parser.add_argument("--radius", type=int, default=12)
    args = parser.parse_args()

    all_summary: list[dict[str, object]] = []
    all_events: list[dict[str, object]] = []
    for label, episodes_path, data_path in args.world:
        summary, events = _summarize(label, episodes_path, data_path, args.high_q, args.radius)
        all_summary.extend(summary)
        all_events.extend(events)

    _write_csv(all_summary, Path(args.csv_out))
    _write_csv(all_events, Path(args.events_out))
    _write_markdown(all_summary, all_events, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.events_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
