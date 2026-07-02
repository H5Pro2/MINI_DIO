from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


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


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _parse_world(value: str) -> tuple[str, Path]:
    parts = value.split("=", 1)
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("world must use LABEL=CSV")
    return parts[0], Path(parts[1])


def _window(raw_rows: list[dict[str, str]], tick: int, radius: int) -> list[dict[str, str]]:
    index = max(0, min(len(raw_rows) - 1, tick - 1))
    return raw_rows[max(0, index - radius) : min(len(raw_rows), index + radius + 1)]


def _raw_profile(raw_rows: list[dict[str, str]], tick: int, radius: int) -> dict[str, float | str | int]:
    rows = _window(raw_rows, tick, radius)
    if not rows:
        return {
            "raw_rows": 0,
            "raw_return": 0.0,
            "range_ratio": 0.0,
            "body_ratio": 0.0,
            "direction_consistency": 0.0,
            "expansion_ratio": 0.0,
            "break_ratio": 0.0,
            "movement_class": "leer",
        }

    first_open = _float(rows[0], "open")
    last_close = _float(rows[-1], "close")
    price_base = max(abs(first_open), 1e-9)
    highs = [_float(row, "high") for row in rows]
    lows = [_float(row, "low") for row in rows]
    closes = [_float(row, "close") for row in rows]
    bodies = [abs(_float(row, "close") - _float(row, "open")) for row in rows]
    ranges = [max(0.0, _float(row, "high") - _float(row, "low")) for row in rows]
    deltas = [closes[idx] - closes[idx - 1] for idx in range(1, len(closes))]
    pos = sum(1 for value in deltas if value > 0)
    neg = sum(1 for value in deltas if value < 0)
    direction_consistency = abs(pos - neg) / max(1, pos + neg)
    avg_range = sum(ranges) / max(1, len(ranges))
    avg_body = sum(bodies) / max(1, len(bodies))
    max_range = max(ranges) if ranges else 0.0
    expansion_ratio = max_range / max(1e-9, avg_range)
    break_ratio = avg_body / max(1e-9, avg_range)
    raw_return = (last_close - first_open) / price_base
    range_ratio = (max(highs) - min(lows)) / price_base
    body_ratio = avg_body / price_base
    movement_class = _movement_class(raw_return, range_ratio, direction_consistency, expansion_ratio, break_ratio)
    return {
        "raw_rows": len(rows),
        "raw_return": raw_return,
        "range_ratio": range_ratio,
        "body_ratio": body_ratio,
        "direction_consistency": direction_consistency,
        "expansion_ratio": expansion_ratio,
        "break_ratio": break_ratio,
        "movement_class": movement_class,
    }


def _movement_class(
    raw_return: float,
    range_ratio: float,
    direction_consistency: float,
    expansion_ratio: float,
    break_ratio: float,
) -> str:
    if expansion_ratio >= 2.5 and direction_consistency >= 0.45:
        return "expansion_impuls"
    if expansion_ratio >= 2.0 and direction_consistency < 0.45:
        return "bewegungsbruch"
    if break_ratio >= 0.55 and range_ratio >= 0.012:
        return "bruch_koerperlast"
    if direction_consistency >= 0.60 and abs(raw_return) >= 0.008:
        return "gerichtete_bewegung"
    if range_ratio <= 0.006 and direction_consistency < 0.40:
        return "rekopplungsversuch"
    return "gemischte_rohwelt"


def _role_sequence_index(rows: list[dict[str, str]]) -> dict[tuple[str, int, int], dict[str, str]]:
    by_world: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_world.setdefault(row.get("world", "-") or "-", []).append(row)
    out: dict[tuple[str, int, int], dict[str, str]] = {}
    for world, world_rows in by_world.items():
        world_rows.sort(key=lambda row: (_int(row, "start_tick"), _int(row, "end_tick")))
        for idx, row in enumerate(world_rows):
            prev_row = world_rows[idx - 1] if idx > 0 else None
            next_row = world_rows[idx + 1] if idx + 1 < len(world_rows) else None
            key = (world, _int(row, "start_tick"), _int(row, "end_tick"))
            out[key] = {
                "previous_role": prev_row.get("role", "-") if prev_row else "-",
                "next_role": next_row.get("role", "-") if next_row else "-",
                "previous_duration": prev_row.get("duration", "0") if prev_row else "0",
                "next_duration": next_row.get("duration", "0") if next_row else "0",
            }
    return out


def _select_segments(rows: list[dict[str, str]], limit: int) -> list[dict[str, str]]:
    candidates = [row for row in rows if row.get("role") == "spannungsrand_kippnaehe"]
    candidates.sort(
        key=lambda row: (
            _float(row, "avg_auditory_loudness"),
            _float(row, "avg_raw_field_intake"),
            _float(row, "avg_strain"),
        ),
        reverse=True,
    )
    return candidates[:limit]


def _build_rows(
    segment_rows: list[dict[str, str]],
    worlds: dict[str, list[dict[str, str]]],
    radius: int,
    sequence_index: dict[tuple[str, int, int], dict[str, str]],
) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in segment_rows:
        world = row.get("world", "-") or "-"
        raw_rows = worlds.get(world)
        if not raw_rows:
            continue
        start_tick = _int(row, "start_tick")
        end_tick = _int(row, "end_tick")
        center_tick = int(round((start_tick + end_tick) / 2))
        sequence = sequence_index.get((world, start_tick, end_tick), {})
        profile = _raw_profile(raw_rows, center_tick, radius)
        out.append(
            {
                "world": world,
                "start_tick": start_tick,
                "end_tick": end_tick,
                "duration": _int(row, "duration"),
                "center_tick": center_tick,
                "previous_role": sequence.get("previous_role", "-"),
                "next_role": sequence.get("next_role", "-"),
                "previous_duration": _int(sequence, "previous_duration"),
                "next_duration": _int(sequence, "next_duration"),
                "avg_raw_field_intake": round(_float(row, "avg_raw_field_intake"), 6),
                "avg_auditory_loudness": round(_float(row, "avg_auditory_loudness"), 6),
                "avg_visual_sharpness": round(_float(row, "avg_visual_sharpness"), 6),
                "avg_rekopplung": round(_float(row, "avg_rekopplung"), 6),
                "avg_strain": round(_float(row, "avg_strain"), 6),
                **{key: round(value, 8) if isinstance(value, float) else value for key, value in profile.items()},
            }
        )
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], out: Path, title: str) -> None:
    counts = Counter(str(row["movement_class"]) for row in rows)
    previous_counts = Counter(str(row["previous_role"]) for row in rows)
    next_counts = Counter(str(row["next_role"]) for row in rows)
    pair_counts = Counter(f"{row['previous_role']} -> spannungsrand_kippnaehe -> {row['next_role']}" for row in rows)
    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Sind reale `gekoppelte_feldlast`-/Rand-Kipp-Fenster eher an Bewegungsbruch, Expansion oder Rekopplungsversuch gebunden?",
        "",
        "Diese Diagnose verbindet reale Rand/Kipp-Segmente mit einem kleinen OHLCV-Fenster um den Segmentmittelpunkt. Sie ist passiv und erzeugt keine Runtime-Regel.",
        "",
        "## Bewegungsarten",
        "",
    ]
    for name, count in counts.most_common():
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(["", "## Rollenfolge um Rand/Kipp", ""])
    lines.append("Vorherige Rolle:")
    for name, count in previous_counts.most_common():
        lines.append(f"- `{name}`: `{count}`")
    lines.append("")
    lines.append("Naechste Rolle:")
    for name, count in next_counts.most_common():
        lines.append(f"- `{name}`: `{count}`")
    lines.append("")
    lines.append("Hauefigste Sequenzen:")
    for name, count in pair_counts.most_common(8):
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste Fenster",
            "",
            "| Welt | Ticks | Lautheit | Rohfeld | Schaerfe | Rekopplung | Strain | Return | Range | Expansion | Richtung | Klasse |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows[:16]:
        lines.append(
            "| {world} | {start_tick}-{end_tick} | {avg_auditory_loudness:.4f} | {avg_raw_field_intake:.4f} | {avg_visual_sharpness:.4f} | {avg_rekopplung:.4f} | {avg_strain:.4f} | {raw_return:+.5f} | {range_ratio:.5f} | {expansion_ratio:.3f} | {direction_consistency:.3f} | {movement_class} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Ableitung",
            "",
            "Wenn `expansion_impuls` dominiert, ist reale Rand/Kipp-Naehe eher an gerichtete starke Weltbewegung gebunden.",
            "",
            "Wenn `bewegungsbruch` dominiert, ist sie eher an Richtungsbruch oder instabile Umordnung gebunden.",
            "",
            "Wenn `rekopplungsversuch` dominiert, waere Rand/Kipp eher ein kurzer Zustand vor Rueckbindung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die dominante Bewegungsart gegen die MCM-Rollenfolge gelesen werden: Welche Rolle kommt vor und nach `gekoppelte_feldlast` am haeufigsten?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--segments", required=True)
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--title", default="Reale gekoppelte Feldlast Rohweltfenster")
    parser.add_argument("--limit", type=int, default=64)
    parser.add_argument("--radius", type=int, default=35)
    args = parser.parse_args()

    worlds = {label: _load(path) for label, path in args.world}
    all_segments = _load(Path(args.segments))
    segment_rows = _select_segments(all_segments, args.limit)
    rows = _build_rows(segment_rows, worlds, args.radius, _role_sequence_index(all_segments))
    _write_csv(rows, Path(args.csv_out))
    _write_md(rows, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
