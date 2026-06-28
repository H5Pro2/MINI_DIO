from __future__ import annotations

import argparse
import csv
from pathlib import Path


WORLD_FILES = {
    "EXT_EXPANSION_2023": "data/kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv",
    "NEG_STRESS_2023": "data/kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv",
    "NEG_STRESS_2024": "data/kontrolliert_2024_negative_stress_test1_1000_5m_SOLUSDT.csv",
    "POS_EXPANSION_2023": "data/kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv",
    "SIDEWAYS_2024": "data/kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv",
}


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


def _slice(rows: list[dict[str, str]], start: int, end: int) -> list[dict[str, str]]:
    start = max(0, start)
    end = min(len(rows) - 1, end)
    if end < start:
        return []
    return rows[start : end + 1]


def _window_stats(rows: list[dict[str, str]]) -> dict[str, float]:
    if not rows:
        return {
            "open": 0.0,
            "close": 0.0,
            "high": 0.0,
            "low": 0.0,
            "return_pct": 0.0,
            "range_pct": 0.0,
            "body_pct": 0.0,
            "volume_avg": 0.0,
        }
    open_price = _safe_float(rows[0].get("open"))
    close_price = _safe_float(rows[-1].get("close"))
    high = max(_safe_float(row.get("high")) for row in rows)
    low = min(_safe_float(row.get("low")) for row in rows)
    volume = [_safe_float(row.get("volume")) for row in rows]
    base = open_price or 1.0
    return {
        "open": open_price,
        "close": close_price,
        "high": high,
        "low": low,
        "return_pct": ((close_price - open_price) / base) * 100.0,
        "range_pct": ((high - low) / base) * 100.0,
        "body_pct": abs((close_price - open_price) / base) * 100.0,
        "volume_avg": _avg(volume),
    }


def _zone_label(stats: dict[str, float], before: dict[str, float], after: dict[str, float]) -> str:
    ret = stats["return_pct"]
    rng = stats["range_pct"]
    before_ret = before["return_pct"]
    after_ret = after["return_pct"]
    if rng >= 8.0 and abs(ret) < rng * 0.35:
        return "weite_volatilitaetszone"
    if before_ret < -2.0 and ret > 1.0:
        return "rekopplung_nach_abverkauf"
    if before_ret > 2.0 and ret < -1.0:
        return "bruch_nach_anstieg"
    if ret > 2.0 and after_ret >= -0.5:
        return "expansion_getragen"
    if ret < -2.0 and after_ret <= 0.5:
        return "abverkauf_getragen"
    if abs(ret) < 1.0 and rng >= 2.0:
        return "konsolidierung_mit_spannung"
    if abs(ret) < 1.0:
        return "ruhige_konsolidierung"
    return "gerichtete_uebergangsbewegung"


def build_rows(axis_zones: Path, root: Path, pad: int) -> list[dict[str, object]]:
    rows_out: list[dict[str, object]] = []
    for zone in _read(axis_zones):
        world = zone.get("world", "")
        rel = WORLD_FILES.get(world)
        if not rel:
            continue
        data_path = root / rel
        candles = _read(data_path)
        tick_min = _safe_int(zone.get("tick_min"))
        tick_max = _safe_int(zone.get("tick_max"))
        event_mid = _safe_int(zone.get("tick_mid"))
        main = _slice(candles, tick_min, tick_max)
        before = _slice(candles, tick_min - pad, tick_min - 1)
        after = _slice(candles, tick_max + 1, tick_max + pad)
        main_stats = _window_stats(main)
        before_stats = _window_stats(before)
        after_stats = _window_stats(after)
        rows_out.append(
            {
                "world": world,
                "data_file": rel,
                "pair": zone.get("pair", "-"),
                "events": zone.get("events", "0"),
                "tick_min": tick_min,
                "tick_mid": event_mid,
                "tick_max": tick_max,
                "window_candles": len(main),
                "chart_zone": _zone_label(main_stats, before_stats, after_stats),
                "main_return_pct": round(main_stats["return_pct"], 6),
                "main_range_pct": round(main_stats["range_pct"], 6),
                "before_return_pct": round(before_stats["return_pct"], 6),
                "after_return_pct": round(after_stats["return_pct"], 6),
                "main_open": round(main_stats["open"], 8),
                "main_close": round(main_stats["close"], 8),
                "main_high": round(main_stats["high"], 8),
                "main_low": round(main_stats["low"], 8),
                "main_volume_avg": round(main_stats["volume_avg"], 6),
                "dominant_movement": zone.get("dominant_movement", "-"),
                "dominant_tick_zone": zone.get("dominant_tick_zone", "-"),
                "mcm_pressure_abs": zone.get("pressure_delta_abs_avg", "0"),
                "mcm_rekopplung_abs": zone.get("rekopplung_delta_abs_avg", "0"),
                **PASSIVE_FLAGS,
            }
        )
    return rows_out


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


def write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {path.stem.split('_', 1)[0]} - Achsenzonen gegen OHLCV-Chart",
        "",
        "Passive Gegenlesung aktiver MCM-Achsenfenster gegen den echten Kerzenverlauf.",
        "",
        "## Chartzonen",
        "",
        "| Welt | Paar | Ticks | Chartzone | Vorher % | Fenster % | Nachher % | Range % | Bewegung |",
        "|---|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| {world} | `{pair}` | {tick_min}-{tick_max} | `{chart_zone}` | {before_return_pct} | {main_return_pct} | {after_return_pct} | {main_range_pct} | `{dominant_movement}` |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die aktiven MCM-Achsen liegen in realen Chartfenstern mit lokaler Uebergangsqualitaet. Das sind nicht nur abstrakte Feldzeichen, sondern zeitlich lokalisierbare Abschnitte im Kerzenverlauf.",
            "",
            "Wichtig ist die Unterscheidung:",
            "",
            "- Expansionen zeigen haeufig Bewegungsbruch oder Rekopplung im mittleren Verlauf.",
            "- Negative Stresswelten zeigen Achsen eher spaet, in Druck- oder Rekopplungsfenstern.",
            "- Sideways zeigt spaete, kleinere Druck-/Rekopplungsfenster.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte fuer die wichtigsten Fenster eine kleine Chartgrafik erzeugt werden: Kerzenfenster plus markierte Achsenticks. Dann sieht man visuell, ob die Achse an Bruch, Reversal, Konsolidierung oder Fortsetzung sitzt.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis-zones", required=True, type=Path)
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--pad", type=int, default=24)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()
    rows = build_rows(args.axis_zones, args.root, args.pad)
    write_csv(rows, args.out_csv)
    write_md(rows, args.out_md)
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
