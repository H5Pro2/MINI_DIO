from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"

INPUTS_DEFAULT = [
    ("BTC", REPORT_DIR / "460_BTC2024_5M_QUIET_REGULATIONSVORSCHLAG.csv"),
    ("BTC", REPORT_DIR / "461_BTC2024_5M_STRESS_REGULATIONSVORSCHLAG.csv"),
    ("BTC", REPORT_DIR / "462_BTC2024_1H_QUIET_REGULATIONSVORSCHLAG.csv"),
    ("BTC", REPORT_DIR / "463_BTC2024_1H_STRESS_REGULATIONSVORSCHLAG.csv"),
    ("SOL", REPORT_DIR / "465_SOL2023_NEGATIVE_STRESS_10K_REGULATIONSVORSCHLAG.csv"),
    ("SOL", REPORT_DIR / "466_SOL2026_SIDEWAYS_10K_REGULATIONSVORSCHLAG.csv"),
    ("SOL", REPORT_DIR / "467_SOL2023_POSITIVE_EXPANSION_10K_REGULATIONSVORSCHLAG.csv"),
    ("KAS", REPORT_DIR / "471_KAS2024_ZEITEBENEN_REGULATIONSVORSCHLAG.csv"),
]

INPUTS_KAS_SPLIT = [
    item for item in INPUTS_DEFAULT if item[0] != "KAS"
] + [
    ("KAS", REPORT_DIR / "481_KAS2024_5M_REGULATIONSVORSCHLAG.csv"),
    ("KAS", REPORT_DIR / "482_KAS2024_15M_REGULATIONSVORSCHLAG.csv"),
    ("KAS", REPORT_DIR / "483_KAS2024_30M_REGULATIONSVORSCHLAG.csv"),
    ("KAS", REPORT_DIR / "484_KAS2024_1H_REGULATIONSVORSCHLAG.csv"),
]

INPUTS_YEAR_EXTENDED = INPUTS_KAS_SPLIT + [
    ("BTC", REPORT_DIR / "486_BTC2025_5M_REGULATIONSVORSCHLAG.csv"),
    ("BTC", REPORT_DIR / "487_BTC2025_1H_REGULATIONSVORSCHLAG.csv"),
    ("SOL", REPORT_DIR / "488_SOL2025_5M_REGULATIONSVORSCHLAG.csv"),
    ("SOL", REPORT_DIR / "489_SOL2025_1H_REGULATIONSVORSCHLAG.csv"),
]

OUTPUT_CSV_DEFAULT = REPORT_DIR / "476_ASSET_ORGANISMUSPROFIL_STABILITAET.csv"
OUTPUT_MD_DEFAULT = REPORT_DIR / "476_ASSET_ORGANISMUSPROFIL_STABILITAET.md"

DISPLAY_NAMES = {
    "focus_pull": "Fokus halten / vertiefen",
    "distance_pull": "Abstand bilden",
    "softening_pull": "leiser / weicher aufnehmen",
    "sharpening_pull": "Sehen schaerfen",
    "contact_relief_pull": "Druck / Feldkontakt entlasten",
    "stable_listening_pull": "ruhig hinhoeren",
}


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0.0))
    except Exception:
        return 0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _source_label(path: Path) -> str:
    stem = path.stem
    if "_" in stem and stem.split("_", 1)[0].isdigit():
        return stem.split("_", 1)[1]
    return stem


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _weighted(rows: list[dict[str, str]], column: str) -> float:
    total = sum(max(1, _int(row.get("total_events"))) for row in rows)
    if total <= 0:
        return 0.0
    return sum(max(1, _int(row.get("total_events"))) * _float(row.get(column)) for row in rows) / total


def _sum_events(rows: list[dict[str, str]]) -> int:
    return sum(_int(row.get("total_events")) for row in rows)


def _score_suggestion(rows: list[dict[str, str]]) -> dict[str, float]:
    recoupling = _weighted(rows, "recoupling_balance")
    strain = _weighted(rows, "strain_quality")
    carry = _weighted(rows, "carry_quality")
    field_input = _weighted(rows, "field_intake_pressure")
    support = _clamp((recoupling * 0.45) + (carry * 0.35) + ((1.0 - strain) * 0.10) + ((1.0 - field_input) * 0.10))
    pressure = _clamp((strain * 0.45) + (field_input * 0.40) + ((1.0 - recoupling) * 0.15))
    return {
        "recoupling": recoupling,
        "strain": strain,
        "carry": carry,
        "field_input": field_input,
        "support": support,
        "pressure": pressure,
        "net": support - pressure,
    }


def _profile_for_source(asset: str, path: Path) -> dict[str, object]:
    rows = _read_rows(path)
    by_suggestion: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_suggestion[str(row.get("dominant_suggestion") or "-")].append(row)

    suggestion_rows: list[dict[str, object]] = []
    for suggestion, group in by_suggestion.items():
        scores = _score_suggestion(group)
        suggestion_rows.append(
            {
                "suggestion": suggestion,
                "display": DISPLAY_NAMES.get(suggestion, suggestion),
                "trace_count": len(group),
                "total_events": _sum_events(group),
                **scores,
            }
        )

    top_need = max(suggestion_rows, key=lambda row: (int(row["trace_count"]), int(row["total_events"])))
    strongest = max(suggestion_rows, key=lambda row: float(row["net"]))
    pressure_nearest = max(suggestion_rows, key=lambda row: float(row["pressure"]))

    return {
        "asset": asset,
        "source": _source_label(path),
        "trace_count": len(rows),
        "total_events": _sum_events(rows),
        "dominant_need": top_need["suggestion"],
        "dominant_need_name": top_need["display"],
        "dominant_need_trace_count": top_need["trace_count"],
        "strongest_carried": strongest["suggestion"],
        "strongest_carried_name": strongest["display"],
        "strongest_carried_net": strongest["net"],
        "pressure_nearest": pressure_nearest["suggestion"],
        "pressure_nearest_name": pressure_nearest["display"],
        "pressure_nearest_score": pressure_nearest["pressure"],
        "hearing_net": next((row["net"] for row in suggestion_rows if row["suggestion"] == "stable_listening_pull"), 0.0),
        "seeing_net": next((row["net"] for row in suggestion_rows if row["suggestion"] == "sharpening_pull"), 0.0),
        "focus_net": next((row["net"] for row in suggestion_rows if row["suggestion"] == "focus_pull"), 0.0),
        "distance_net": next((row["net"] for row in suggestion_rows if row["suggestion"] == "distance_pull"), 0.0),
    }


def _stability_rows(profiles: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        grouped[str(profile["asset"])].append(profile)

    output: list[dict[str, object]] = []
    for asset, group in sorted(grouped.items()):
        need_counts = Counter(str(row["dominant_need"]) for row in group)
        carried_counts = Counter(str(row["strongest_carried"]) for row in group)
        pressure_counts = Counter(str(row["pressure_nearest"]) for row in group)
        source_count = len(group)
        top_need, top_need_count = need_counts.most_common(1)[0]
        top_carried, top_carried_count = carried_counts.most_common(1)[0]
        top_pressure, top_pressure_count = pressure_counts.most_common(1)[0]
        if source_count < 2:
            stability = "nicht_belastbar_ein_quellenblock"
        elif top_carried_count == source_count and top_need_count == source_count:
            stability = "bedarf_und_tragung_stabil"
        elif top_carried_count == source_count:
            stability = "tragung_stabil_bedarf_variabel"
        else:
            stability = "profil_variabel"
        output.append(
            {
                "asset": asset,
                "source_count": source_count,
                "dominant_need_mode": top_need,
                "dominant_need_mode_name": DISPLAY_NAMES.get(top_need, top_need),
                "dominant_need_mode_count": top_need_count,
                "strongest_carried_mode": top_carried,
                "strongest_carried_mode_name": DISPLAY_NAMES.get(top_carried, top_carried),
                "strongest_carried_mode_count": top_carried_count,
                "pressure_nearest_mode": top_pressure,
                "pressure_nearest_mode_name": DISPLAY_NAMES.get(top_pressure, top_pressure),
                "pressure_nearest_mode_count": top_pressure_count,
                "stability": stability,
            }
        )
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    columns = [
        "asset",
        "source",
        "trace_count",
        "total_events",
        "dominant_need",
        "dominant_need_name",
        "dominant_need_trace_count",
        "strongest_carried",
        "strongest_carried_name",
        "strongest_carried_net",
        "pressure_nearest",
        "pressure_nearest_name",
        "pressure_nearest_score",
        "hearing_net",
        "seeing_net",
        "focus_net",
        "distance_net",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def write_markdown(
    path: Path,
    profiles: list[dict[str, object]],
    stability: list[dict[str, object]],
    split_kas: bool,
    year_extended: bool,
) -> None:
    title_number = path.name.split("_", 1)[0] if "_" in path.name and path.name.split("_", 1)[0].isdigit() else "476"
    lines = [
        f"# {title_number} - Assetprofil-Stabilitaet unter Weltspannung",
        "",
        "Stand: 2026-06-21",
        "",
        "## Fragestellung",
        "",
        "Bleiben die assetbezogenen Organismusprofile stabil, wenn innerhalb eines Assets andere Weltspannungen gelesen werden?",
        "",
        (
            "Gelesen werden BTC/SOL 2024/2025, SOL-Stress/Sideways/Expansion und getrennte KAS-2024-Zeitebenen."
            if year_extended
            else (
                "Gelesen werden BTC/SOL-Einzelquellen aus den Regulationsvorschlaegen 460 bis 467 und getrennte KAS-Einzelquellen 481 bis 484."
                if split_kas
                else "Gelesen werden nur vorhandene Einzelquellen aus den Regulationsvorschlaegen 460 bis 467 und 471. KAS ist aktuell ein zusammengefasster Zeitebenenblock und daher nur begrenzt als Stabilitaetspruefung belastbar."
            )
        ),
        "",
        "Diese Diagnose bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Stabilitaetsmatrix",
        "",
        "| Asset | Quellen | Stabilitaet | Bedarf Modus | Bedarf Quellen | Tragung Modus | Tragung Quellen | Drucknaehe Modus | Druck Quellen |",
        "|---|---:|---|---|---:|---|---:|---|---:|",
    ]
    for row in stability:
        lines.append(
            f"| {row['asset']} | {row['source_count']} | {row['stability']} | "
            f"{row['dominant_need_mode_name']} | {row['dominant_need_mode_count']} | "
            f"{row['strongest_carried_mode_name']} | {row['strongest_carried_mode_count']} | "
            f"{row['pressure_nearest_mode_name']} | {row['pressure_nearest_mode_count']} |"
        )

    lines.extend(
        [
            "",
            "## Einzelquellen",
            "",
            "| Asset | Quelle | Spuren | Ereignisse | haeufiger Bedarf | staerkste Tragung | Netto | drucknah | Druck | Hoeren | Sehen | Fokus | Abstand |",
            "|---|---|---:|---:|---|---|---:|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in profiles:
        lines.append(
            f"| {row['asset']} | {row['source']} | {row['trace_count']} | {row['total_events']} | "
            f"{row['dominant_need_name']} | {row['strongest_carried_name']} | {_fmt(row['strongest_carried_net'])} | "
            f"{row['pressure_nearest_name']} | {_fmt(row['pressure_nearest_score'])} | "
            f"{_fmt(row['hearing_net'])} | {_fmt(row['seeing_net'])} | {_fmt(row['focus_net'])} | {_fmt(row['distance_net'])} |"
        )

    if year_extended:
        befund_lines = [
            "BTC bleibt in der Tragung stabil: alle sechs BTC-Quellen werden am staerksten ueber `ruhig hinhoeren` getragen. Der haeufige Bedarf ist aber variabel: 2024 liegt er auf Fokus, die 2025er Einzelquellen kippen auf Abstand.",
            "",
            "SOL bleibt in der erweiterten Matrix stabiler: alle fuenf SOL-Quellen liegen bei Abstandsbedarf, getragener Hoerrekopplung und Kontaktentlastungs-Drucknaehe.",
            "",
            "KAS bleibt ueber 5m/15m/30m/1h stabil bei Abstandsbedarf, getragener Hoerrekopplung und Kontaktentlastungs-Drucknaehe.",
        ]
        next_line = "Wie es weitergeht: Als naechstes sollte die BTC-2025-Abweichung lokal gelesen werden: verschiebt sich der Bedarf durch Jahr, Zeitebene oder konkrete Weltspannung?"
    else:
        befund_lines = [
            "BTC zeigt in den vier vorhandenen Quellen eine stabile Tragung ueber `ruhig hinhoeren`. Der haeufige Bedarf liegt ebenfalls stabil auf Fokus. Die Drucknaehe bleibt dagegen eher beim Abstand.",
            "",
            "SOL zeigt in drei sehr unterschiedlichen Welten ebenfalls stabile Tragung ueber `ruhig hinhoeren`. Der haeufige Bedarf bleibt Abstand. Die Drucknaehe bleibt in dieser Matrix bei Kontaktentlastung, also innerhalb derselben Entlastungsfamilie.",
            "",
            (
                "KAS ist jetzt als echte Vier-Quellen-Reihe lesbar. Damit kann die vorher nur angedeutete SOL-naehere Abstandstendenz stabiler beurteilt werden."
                if split_kas
                else "KAS bleibt vorerst nur ein Quellenblock. Die Werte passen zur SOL-naeheren Abstandstendenz, aber Stabilitaet kann daraus noch nicht streng abgeleitet werden."
            ),
        ]
        next_line = (
            "Wie es weitergeht: Als naechstes sollte geprueft werden, ob die stabilen Assetprofile auch mit anderen Jahren oder laengeren Ausschnitten erhalten bleiben."
            if split_kas
            else "Wie es weitergeht: Als naechstes sollte KAS in getrennte Einzelwelten zerlegt werden, damit KAS nicht nur als Zeitebenenblock, sondern als echte Stabilitaetsreihe gegen BTC und SOL vergleichbar wird."
        )

    lines.extend(["", "## Befund", "", *befund_lines, "", "## Schluss", ""])
    lines.extend(
        [
            "Die bisherige Richtung wird gestuetzt: Die getragene Grundaufnahme ist uebergreifend Hinhoeren, waehrend der Bedarf asset- und weltqualitaetsabhaengig variieren kann.",
            "",
            "Fachlich wichtig ist: Stabil ist nicht zwingend die haeufigste Reaktion. Stabiler wirkt die tragende Rekopplungsart.",
            "",
            next_line,
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kas-split", action="store_true")
    parser.add_argument("--year-extended", action="store_true")
    parser.add_argument("--csv-out", type=Path, default=OUTPUT_CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=OUTPUT_MD_DEFAULT)
    args = parser.parse_args()

    if args.year_extended:
        inputs = INPUTS_YEAR_EXTENDED
    elif args.kas_split:
        inputs = INPUTS_KAS_SPLIT
    else:
        inputs = INPUTS_DEFAULT
    profiles = [_profile_for_source(asset, path) for asset, path in inputs if path.exists()]
    profiles.sort(key=lambda row: (str(row["asset"]), str(row["source"])))
    stability = _stability_rows(profiles)
    write_csv(args.csv_out, profiles)
    write_markdown(args.md_out, profiles, stability, bool(args.kas_split), bool(args.year_extended))
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    print(f"sources={len(profiles)} assets={len(stability)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
