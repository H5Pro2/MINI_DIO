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


BUILTIN_WORLD_FILES = {
    "EXT_EXPANSION_2023": "data/kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv",
    "NEG_STRESS_2023": "data/kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv",
    "NEG_STRESS_2024": "data/kontrolliert_2024_negative_stress_test1_1000_5m_SOLUSDT.csv",
    "POS_EXPANSION_2023": "data/kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv",
    "SIDEWAYS_2024": "data/kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv",
    "SOL_2024_5M": "data/kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv",
    "SOL_2024_15M": "data/kontrolliert_sol_2024_15m_test1_2000_SOLUSDT.csv",
    "SOL_2024_30M": "data/kontrolliert_sol_2024_30m_test1_2000_SOLUSDT.csv",
    "SOL_2024_1H": "data/kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv",
    "BTC_2024_5M": "data/kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv",
    "BTC_2024_15M": "data/kontrolliert_btc_2024_15m_test1_2000_BTCUSDT.csv",
    "BTC_2024_30M": "data/kontrolliert_btc_2024_30m_test1_2000_BTCUSDT.csv",
    "BTC_2024_1H": "data/kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv",
    "KAS_2024_5M": "data/kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
    "KAS_2024_15M": "data/kontrolliert_kas_2024_15m_test1_2000_KASUSDT.csv",
    "KAS_2024_30M": "data/kontrolliert_kas_2024_30m_test1_2000_KASUSDT.csv",
    "KAS_2024_1H": "data/kontrolliert_kas_2024_1h_test1_2000_KASUSDT.csv",
    "PAXG_2024_5M": "data/kontrolliert_paxg_2024_5m_test1_2000_PAXGUSDT.csv",
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


def _pair_short(pair: str) -> str:
    if "->" not in pair:
        return _short(pair)
    left, right = pair.split("->", 1)
    return f"{_short(left)}->{_short(right)}"


def _quantile(values: list[int], q: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[index]


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


def _typology(chart_zone: str, movement: str, ret: float, before: float, after: float, rng: float) -> tuple[str, str]:
    if chart_zone == "abverkauf_getragen":
        if movement == "rekopplungs_uebergang":
            return "abverkauf_mit_rekopplung", "Abverkauf wird nicht nur als Fall gelesen, sondern mit Rekopplungsanteil getragen."
        return "abverkauf_mit_bruch", "Abverkauf wird als Bewegungsbruch oder Druckbruch gelesen."
    if "konsolidierung" in chart_zone:
        if movement == "druck_uebergang":
            return "konsolidierung_unter_druck", "Seitwaerts-/Ruhefenster traegt innere Druckspannung."
        if movement == "rekopplungs_uebergang":
            return "konsolidierung_mit_rekopplung", "Seitwaerts-/Ruhefenster traegt Rekopplung statt reiner Ruhe."
        return "konsolidierung_mit_bruchnaehe", "Konsolidierung zeigt Bruchnaehe oder gespannte Struktur."
    if chart_zone == "expansion_getragen":
        return "getragene_expansion", "Expansion bleibt ueber das Fenster getragen."
    if chart_zone == "gerichtete_uebergangsbewegung":
        if movement == "bewegungsbruch_zone":
            return "gerichtete_bewegung_mit_bruch", "Richtung laeuft, aber das MCM-Feld liest Bruch oder Umordnung."
        if movement == "rekopplungs_uebergang":
            return "gerichtete_bewegung_mit_rekopplung", "Richtung laeuft und koppelt im Feld wieder an."
        return "gerichtete_uebergangsbewegung", "Gerichtete Bewegung mit unspezifischer Uebergangsqualitaet."
    if chart_zone == "rekopplung_nach_abverkauf":
        return "rekopplung_nach_abverkauf", "Nach einem Abverkauf entsteht ein lokales Rekopplungsfenster."
    if chart_zone == "bruch_nach_anstieg":
        return "bruch_nach_anstieg", "Nach einem Anstieg entsteht ein lokaler Bruch oder Entlastungswechsel."
    if chart_zone == "weite_volatilitaetszone":
        return "weite_volatilitaetszone", "Das Fenster traegt breite Bewegung ohne eindeutige Richtung."
    if before > 2.0 and ret > 1.0 and after < 0.0 and rng > 5.0:
        return "expansion_vor_entspannung", "Vorher stark, Fenster weiter steigend, danach erste Entspannung."
    return "offene_chart_achsenlage", "Chartfenster traegt eine Achse, aber ohne klare Typologie."


def _load_reference_types(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {row.get("typology", "") for row in _read(path) if row.get("typology")}


def _world_file_map(root: Path, overrides: list[list[str]] | None) -> dict[str, Path]:
    mapping = {name: root / rel for name, rel in BUILTIN_WORLD_FILES.items()}
    for item in overrides or []:
        if len(item) != 2:
            continue
        mapping[item[0]] = root / item[1]
    return mapping


def build_rows(
    root: Path,
    sources: list[list[str]],
    world_files: dict[str, Path],
    reference_types: set[str],
    min_events: int,
    pad: int,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    detail: list[dict[str, object]] = []
    grouped_summary: dict[str, list[dict[str, object]]] = defaultdict(list)
    for source_name, events_path_text in sources:
        events_path = root / events_path_text
        grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
        for row in _read(events_path):
            grouped[(row.get("world", "-"), row.get("pair", "-"))].append(row)
        for (world, pair), events in sorted(grouped.items()):
            if len(events) < min_events:
                continue
            data_path = world_files.get(world)
            if data_path is None or not data_path.exists():
                continue
            candles = _read(data_path)
            ticks = [_safe_int(row.get("event_tick")) for row in events]
            tick_min = min(ticks)
            tick_mid = _quantile(ticks, 0.50)
            tick_max = max(ticks)
            movement_counter = Counter(
                _movement_reading(row.get("before_class", ""), row.get("switch_class", ""), row.get("after_class", ""))
                for row in events
            )
            pressure = [_safe_float(row.get("pressure_delta")) for row in events]
            rekopplung = [_safe_float(row.get("rekopplung_delta")) for row in events]
            main = _slice(candles, tick_min, tick_max)
            before = _slice(candles, tick_min - pad, tick_min - 1)
            after = _slice(candles, tick_max + 1, tick_max + pad)
            main_stats = _window_stats(main)
            before_stats = _window_stats(before)
            after_stats = _window_stats(after)
            chart_zone = _zone_label(main_stats, before_stats, after_stats)
            movement = movement_counter.most_common(1)[0][0]
            typology, note = _typology(
                chart_zone,
                movement,
                main_stats["return_pct"],
                before_stats["return_pct"],
                after_stats["return_pct"],
                main_stats["range_pct"],
            )
            row_out: dict[str, object] = {
                "source": source_name,
                "world": world,
                "data_file": str(data_path.relative_to(root)) if data_path.is_relative_to(root) else str(data_path),
                "pair": _pair_short(pair),
                "events": len(events),
                "tick_min": tick_min,
                "tick_mid": tick_mid,
                "tick_max": tick_max,
                "chart_zone": chart_zone,
                "dominant_movement": movement,
                "typology": typology,
                "reference_state": "known_reference_type" if typology in reference_types else "new_or_extended_type",
                "main_return_pct": round(main_stats["return_pct"], 6),
                "main_range_pct": round(main_stats["range_pct"], 6),
                "before_return_pct": round(before_stats["return_pct"], 6),
                "after_return_pct": round(after_stats["return_pct"], 6),
                "pressure_delta_abs_avg": round(_avg([abs(value) for value in pressure]), 6),
                "rekopplung_delta_abs_avg": round(_avg([abs(value) for value in rekopplung]), 6),
                "note": note,
                **PASSIVE_FLAGS,
            }
            detail.append(row_out)
            grouped_summary[typology].append(row_out)
    summary: list[dict[str, object]] = []
    for typology, rows in grouped_summary.items():
        worlds = Counter(str(row["world"]) for row in rows)
        sources_count = Counter(str(row["source"]) for row in rows)
        movements = Counter(str(row["dominant_movement"]) for row in rows)
        summary.append(
            {
                "typology": typology,
                "count": len(rows),
                "reference_state": "known_reference_type" if typology in reference_types else "new_or_extended_type",
                "sources": " | ".join(f"{key}:{value}" for key, value in sources_count.most_common()),
                "worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common(8)),
                "movements": " | ".join(f"{key}:{value}" for key, value in movements.most_common()),
                "avg_return_pct": round(_avg([_safe_float(row["main_return_pct"]) for row in rows]), 6),
                "avg_range_pct": round(_avg([_safe_float(row["main_range_pct"]) for row in rows]), 6),
                "avg_pressure_abs": round(_avg([_safe_float(row["pressure_delta_abs_avg"]) for row in rows]), 6),
                "avg_rekopplung_abs": round(_avg([_safe_float(row["rekopplung_delta_abs_avg"]) for row in rows]), 6),
                "note": str(rows[0]["note"]),
                **PASSIVE_FLAGS,
            }
        )
    detail.sort(key=lambda row: (str(row["reference_state"]), str(row["typology"]), str(row["world"]), str(row["pair"])))
    summary.sort(key=lambda row: (str(row["reference_state"]), -int(row["count"]), str(row["typology"])))
    return detail, summary


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
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


def _write_md(path: Path, summary: list[dict[str, object]], detail: list[dict[str, object]], reference_types: set[str]) -> None:
    known = sum(1 for row in detail if row["reference_state"] == "known_reference_type")
    new = sum(1 for row in detail if row["reference_state"] == "new_or_extended_type")
    lines = [
        f"# {path.stem.split('_', 1)[0]} - MCM-Achsentypen Wiederkehrpruefung",
        "",
        "Passive Gegenprobe, ob die in 1012 gelesenen Chart-/MCM-Typen in weiteren Welten wiederkehren.",
        "",
        "## Kurzbefund",
        "",
        f"- Referenztypen aus 1012: {len(reference_types)}",
        f"- Gepruefte Achsenfenster: {len(detail)}",
        f"- Bekannte Referenztypen: {known}",
        f"- Neue oder erweiterte Typen: {new}",
        "",
        "## Typen",
        "",
        "| Typ | Status | Anzahl | Quellen | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |",
        "|---|---|---:|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in summary:
        clean_row = {key: str(value).replace("|", "<br>") for key, value in row.items()}
        lines.append(
            "| {typology} | {reference_state} | {count} | {sources} | {worlds} | {movements} | {avg_return_pct} | {avg_range_pct} | {avg_pressure_abs} | {avg_rekopplung_abs} | {note} |".format(
                **clean_row
            )
        )
    lines.extend(
        [
            "",
            "## Einzelzuordnung",
            "",
            "| Status | Typ | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |",
            "|---|---|---|---|---|---|---|---|---:|---:|",
        ]
    )
    for row in detail[:80]:
        lines.append(
            "| {reference_state} | {typology} | {source} | {world} | `{pair}` | {tick_min}-{tick_max} | `{chart_zone}` | `{dominant_movement}` | {main_return_pct} | {main_range_pct} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Pruefung trennt bekannte Referenztypen von neu entstehenden oder erweiterten Typen. Bekannte Typen sprechen fuer Wiederkehr der Feld-/Chart-Lesung. Neue Typen sind nicht automatisch Fehler; sie koennen echte Erweiterungen durch andere Weltspannung, Assetklasse oder Zeitebene sein.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die neuen oder erweiterten Typen getrennt gelesen werden: Welche entstehen durch andere Assetspannung, welche durch Zeitebene, und welche durch echte neue MCM-Uebergangsqualitaet.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", nargs=2, metavar=("NAME", "EVENTS_CSV"), required=True)
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "DATA_CSV"))
    parser.add_argument("--reference", type=Path, default=Path("docs/befunde/1012_MCM_ACHSE_CHARTZONEN_TYPOLOGIE_SUMMARY.csv"))
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--min-events", type=int, default=2)
    parser.add_argument("--pad", type=int, default=24)
    parser.add_argument("--out-detail", type=Path, required=True)
    parser.add_argument("--out-summary", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    root = args.root
    reference_types = _load_reference_types(root / args.reference)
    world_files = _world_file_map(root, args.world)
    detail, summary = build_rows(root, args.source, world_files, reference_types, args.min_events, args.pad)
    _write_csv(args.out_detail, detail)
    _write_csv(args.out_summary, summary)
    _write_md(args.out_md, summary, detail, reference_types)
    print(f"details={len(detail)}")
    print(f"types={len(summary)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
