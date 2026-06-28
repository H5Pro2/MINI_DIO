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


def _avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _typology(row: dict[str, str]) -> tuple[str, str]:
    chart_zone = row.get("chart_zone", "")
    movement = row.get("dominant_movement", "")
    ret = _safe_float(row.get("main_return_pct"))
    before = _safe_float(row.get("before_return_pct"))
    after = _safe_float(row.get("after_return_pct"))
    rng = _safe_float(row.get("main_range_pct"))

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
    if before > 2.0 and ret > 1.0 and after < 0.0 and rng > 5.0:
        return "expansion_vor_entspannung", "Vorher stark, Fenster weiter steigend, danach erste Entspannung."
    return "offene_chart_achsenlage", "Chartfenster traegt eine Achse, aber ohne klare Typologie."


def build_rows(windows: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows = _read(windows)
    enriched: list[dict[str, object]] = []
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        typology, note = _typology(row)
        enriched_row: dict[str, object] = {
            "typology": typology,
            "note": note,
            "world": row.get("world", "-"),
            "pair": row.get("pair", "-"),
            "events": row.get("events", "0"),
            "ticks": f"{row.get('tick_min', '-')}-{row.get('tick_max', '-')}",
            "chart_zone": row.get("chart_zone", "-"),
            "dominant_movement": row.get("dominant_movement", "-"),
            "main_return_pct": row.get("main_return_pct", "0"),
            "main_range_pct": row.get("main_range_pct", "0"),
            "before_return_pct": row.get("before_return_pct", "0"),
            "after_return_pct": row.get("after_return_pct", "0"),
            "mcm_pressure_abs": row.get("mcm_pressure_abs", "0"),
            "mcm_rekopplung_abs": row.get("mcm_rekopplung_abs", "0"),
            **PASSIVE_FLAGS,
        }
        enriched.append(enriched_row)
        grouped[typology].append(enriched_row)

    summary: list[dict[str, object]] = []
    for typology, subset in sorted(grouped.items()):
        worlds = Counter(str(row["world"]) for row in subset)
        movements = Counter(str(row["dominant_movement"]) for row in subset)
        pairs = Counter(str(row["pair"]) for row in subset)
        summary.append(
            {
                "typology": typology,
                "count": len(subset),
                "worlds": " | ".join(f"{key}:{value}" for key, value in worlds.most_common()),
                "movements": " | ".join(f"{key}:{value}" for key, value in movements.most_common()),
                "top_pairs": " | ".join(f"{key}:{value}" for key, value in pairs.most_common(4)),
                "avg_return_pct": round(_avg([_safe_float(row["main_return_pct"]) for row in subset]), 6),
                "avg_range_pct": round(_avg([_safe_float(row["main_range_pct"]) for row in subset]), 6),
                "avg_pressure_abs": round(_avg([_safe_float(row["mcm_pressure_abs"]) for row in subset]), 6),
                "avg_rekopplung_abs": round(_avg([_safe_float(row["mcm_rekopplung_abs"]) for row in subset]), 6),
                "note": str(subset[0]["note"]),
                **PASSIVE_FLAGS,
            }
        )
    summary.sort(key=lambda row: (-int(row["count"]), str(row["typology"])))
    return enriched, summary


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
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


def _write_md(enriched: list[dict[str, object]], summary: list[dict[str, object]], path: Path) -> None:
    lines = [
        f"# {path.stem.split('_', 1)[0]} - MCM-Achsen Chartzonen-Typologie",
        "",
        "Passive Verdichtung der aktiven Achsenfenster in Chart-/MCM-Typen.",
        "",
        "## Typologie",
        "",
        "| Typ | Anzahl | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |",
        "|---|---:|---|---|---:|---:|---:|---:|---|",
    ]
    for row in summary:
        lines.append(
            "| {typology} | {count} | {worlds} | {movements} | {avg_return_pct} | {avg_range_pct} | {avg_pressure_abs} | {avg_rekopplung_abs} | {note} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Einzelzuordnung",
            "",
            "| Typ | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |",
            "|---|---|---|---|---|---|---:|---:|",
        ]
    )
    for row in enriched:
        lines.append(
            "| {typology} | {world} | `{pair}` | {ticks} | `{chart_zone}` | `{dominant_movement}` | {main_return_pct} | {main_range_pct} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Achsenfenster zerfallen nicht in beliebige Chartstellen. Sie bilden wiederkehrende Typen: gerichtete Bewegung mit Rekopplung, gerichtete Bewegung mit Bruch, Konsolidierung unter Druck, Konsolidierung mit Rekopplung, getragene Expansion und Abverkauf mit Rekopplung oder Bruch.",
            "",
            "Damit wird die bisherige Regimewechsel-Lesung konkreter: Das MCM-Feld reagiert nicht nur auf Richtung, sondern auf Uebergangsqualitaet. Entscheidend ist, ob ein Chartfenster Druck, Bruch, Rekopplung oder tragende Fortsetzung erzeugt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Typen ueber neue Welten wiederkehren oder ob neue Typen entstehen. Besonders wichtig ist die Frage, ob `gerichtete_bewegung_mit_rekopplung` und `abverkauf_mit_rekopplung` stabile MCM-Archetypen werden.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--windows", required=True, type=Path)
    parser.add_argument("--out-detail", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    enriched, summary = build_rows(args.windows)
    _write_csv(enriched, args.out_detail)
    _write_csv(summary, args.out_summary)
    _write_md(enriched, summary, args.out_md)
    print(f"details={len(enriched)}")
    print(f"types={len(summary)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
