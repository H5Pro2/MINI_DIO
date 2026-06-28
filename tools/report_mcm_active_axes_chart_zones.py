from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


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


def _avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _short(token: str) -> str:
    return str(token or "").replace("dio_mcm_episode_", "")


def _quantile(values: list[int], q: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[index]


def _tick_zone(tick: int) -> str:
    if tick < 250:
        return "frueh"
    if tick < 500:
        return "frueh_mitte"
    if tick < 750:
        return "spaet_mitte"
    return "spaet"


def _movement_reading(before: str, switch: str, after: str) -> str:
    text = f"{before}|{switch}|{after}"
    if "bewegungsbruch" in text:
        return "bewegungsbruch_zone"
    if "druck_lage" in text:
        return "druck_uebergang"
    if text.count("rekoppelnde_lage") >= 2:
        return "rekopplungs_uebergang"
    if "offene_lage" in text:
        return "offene_uebergangszone"
    if "gehaltene_form" in text:
        return "gehaltene_formzone"
    return "unbestimmte_uebergangszone"


def build_rows(events_path: Path, min_events: int, top_pairs: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    events = _read(events_path)
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in events:
        grouped[(row.get("world", "-"), row.get("pair", "-"))].append(row)

    zone_rows: list[dict[str, object]] = []
    pair_rows: list[dict[str, object]] = []
    pair_counter: Counter[str] = Counter()

    for (world, pair), rows in grouped.items():
        if len(rows) < min_events:
            continue
        ticks = [_safe_int(row.get("event_tick")) for row in rows]
        pressure = [_safe_float(row.get("pressure_delta")) for row in rows]
        rekopplung = [_safe_float(row.get("rekopplung_delta")) for row in rows]
        movement_counter = Counter(
            _movement_reading(row.get("before_class", ""), row.get("switch_class", ""), row.get("after_class", ""))
            for row in rows
        )
        tick_zone_counter = Counter(_tick_zone(tick) for tick in ticks)
        class_counter = Counter()
        for row in rows:
            class_counter.update([row.get("before_class", "-"), row.get("switch_class", "-"), row.get("after_class", "-")])
        pair_counter[pair] += len(rows)
        pair_rows.append(
            {
                "world": world,
                "pair": f"{_short(pair.split('->')[0])}->{_short(pair.split('->')[1])}" if "->" in pair else pair,
                "events": len(rows),
                "tick_min": min(ticks),
                "tick_q25": _quantile(ticks, 0.25),
                "tick_mid": _quantile(ticks, 0.50),
                "tick_q75": _quantile(ticks, 0.75),
                "tick_max": max(ticks),
                "dominant_tick_zone": tick_zone_counter.most_common(1)[0][0],
                "dominant_movement": movement_counter.most_common(1)[0][0],
                "movement_profile": " | ".join(f"{key}:{value}" for key, value in movement_counter.most_common()),
                "class_profile": " | ".join(f"{key}:{value}" for key, value in class_counter.most_common(5)),
                "pressure_delta_avg": round(_avg(pressure), 6),
                "pressure_delta_abs_avg": round(_avg([abs(value) for value in pressure]), 6),
                "rekopplung_delta_avg": round(_avg(rekopplung), 6),
                "rekopplung_delta_abs_avg": round(_avg([abs(value) for value in rekopplung]), 6),
                **PASSIVE_FLAGS,
            }
        )

    top_pair_names = {pair for pair, _count in pair_counter.most_common(top_pairs)}
    for row in pair_rows:
        raw_pair = row["pair"]
        if raw_pair not in {_short(pair.split("->")[0]) + "->" + _short(pair.split("->")[1]) for pair in top_pair_names if "->" in pair}:
            continue
        zone_rows.append(row)

    zone_rows.sort(key=lambda row: (str(row["world"]), -int(row["events"]), str(row["pair"])))
    pair_rows.sort(key=lambda row: (-int(row["events"]), str(row["world"]), str(row["pair"])))
    return zone_rows, pair_rows


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_md(zone_rows: list[dict[str, object]], pair_rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    world_counter = Counter(str(row["world"]) for row in zone_rows)
    movement_counter = Counter(str(row["dominant_movement"]) for row in zone_rows)
    lines = [
        f"# {path.stem.split('_', 1)[0]} - Aktive Achsen und Chartzonen",
        "",
        "Passive Diagnose, wo aktive MCM-Uebergangsachsen im Verlauf auftreten.",
        "",
        "Diese Lesung nutzt vorhandene Ereignisse mit Weltname und Tickposition. Sie ist keine Handlungsschicht und kein Signal.",
        "",
        "## Kurzbefund",
        "",
        f"- Ausgewertete aktive Achsenzonen: {len(zone_rows)}",
        f"- Welten mit aktiven Zonen: {len(world_counter)}",
        f"- Dominante Bewegungsarten: {' | '.join(f'{k}:{v}' for k, v in movement_counter.most_common()) or '-'}",
        "",
        "## Staerkste Achsenzonen",
        "",
        "| Welt | Paar | Events | Tickbereich | Schwerpunkt | Bewegungsart | Druck | Rekopplung |",
        "|---|---|---:|---|---|---|---:|---:|",
    ]
    for row in zone_rows[:40]:
        lines.append(
            "| {world} | `{pair}` | {events} | {tick_min}-{tick_max} | {dominant_tick_zone} | {dominant_movement} | {pressure_delta_abs_avg} | {rekopplung_delta_abs_avg} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Aktive Achsen liegen nicht gleichmaessig im gesamten Verlauf. Sie konzentrieren sich in bestimmten Tickfenstern und tragen dort meistens rekoppelnde Uebergaenge, Druckuebergaenge oder Bewegungsbruchzonen.",
            "",
            "Fachlich bedeutet das: Die MCM-Achse ist wahrscheinlich keine reine Symbolbeziehung. Sie entsteht dort, wo der Chartverlauf eine lokale Uebergangsqualitaet liefert: Bruch, Druckwechsel, Rekopplung oder erneute Stabilisierung.",
            "",
            "## Naechster konkreter Schritt",
            "",
            "Die naechste Diagnose sollte die Tickfenster dieser Achsenzonen gegen die echten OHLCV-Kerzen lesen. Dann sehen wir direkt: laeuft der Chart dort in Expansion, Abverkauf, Seitwaertsphase, Reversal oder Konsolidierung.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--min-events", type=int, default=2)
    parser.add_argument("--top-pairs", type=int, default=8)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-all-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    zone_rows, pair_rows = build_rows(args.events, args.min_events, args.top_pairs)
    write_csv(zone_rows, args.out_csv)
    write_csv(pair_rows, args.out_all_csv)
    write_md(zone_rows, pair_rows, args.out_md)
    print(f"zone_rows={len(zone_rows)}")
    print(f"pair_rows={len(pair_rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
