from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"

ASSET_INPUTS = {
    "BTC": [
        REPORT_DIR / "460_BTC2024_5M_QUIET_REGULATIONSVORSCHLAG.csv",
        REPORT_DIR / "461_BTC2024_5M_STRESS_REGULATIONSVORSCHLAG.csv",
        REPORT_DIR / "462_BTC2024_1H_QUIET_REGULATIONSVORSCHLAG.csv",
        REPORT_DIR / "463_BTC2024_1H_STRESS_REGULATIONSVORSCHLAG.csv",
    ],
    "SOL": [
        REPORT_DIR / "465_SOL2023_NEGATIVE_STRESS_10K_REGULATIONSVORSCHLAG.csv",
        REPORT_DIR / "466_SOL2026_SIDEWAYS_10K_REGULATIONSVORSCHLAG.csv",
        REPORT_DIR / "467_SOL2023_POSITIVE_EXPANSION_10K_REGULATIONSVORSCHLAG.csv",
    ],
    "KAS": [
        REPORT_DIR / "471_KAS2024_ZEITEBENEN_REGULATIONSVORSCHLAG.csv",
    ],
}

CSV_DEFAULT = REPORT_DIR / "474_ASSET_REGULATIONSVORSCHLAG_FELDTRAGUNG.csv"
MD_DEFAULT = REPORT_DIR / "474_ASSET_REGULATIONSVORSCHLAG_FELDTRAGUNG.md"

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


def _read_asset_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for asset, paths in ASSET_INPUTS.items():
        for path in paths:
            if not path.exists():
                continue
            with path.open("r", encoding="utf-8", newline="") as handle:
                for row in csv.DictReader(handle, delimiter=";"):
                    row["_asset"] = asset
                    row["_source"] = _source_label(path)
                    rows.append(row)
    return rows


def _weighted(rows: list[dict[str, str]], column: str) -> float:
    total = sum(max(1, _int(row.get("total_events"))) for row in rows)
    if total <= 0:
        return 0.0
    return sum(max(1, _int(row.get("total_events"))) * _float(row.get(column)) for row in rows) / total


def _sum_events(rows: list[dict[str, str]]) -> int:
    return sum(_int(row.get("total_events")) for row in rows)


def _score_group(asset: str, suggestion: str, rows: list[dict[str, str]]) -> dict[str, object]:
    recoupling = _weighted(rows, "recoupling_balance")
    strain = _weighted(rows, "strain_quality")
    carry = _weighted(rows, "carry_quality")
    field_input = _weighted(rows, "field_intake_pressure")
    support = _clamp((recoupling * 0.45) + (carry * 0.35) + ((1.0 - strain) * 0.10) + ((1.0 - field_input) * 0.10))
    pressure = _clamp((strain * 0.45) + (field_input * 0.40) + ((1.0 - recoupling) * 0.15))
    return {
        "asset": asset,
        "dominant_suggestion": suggestion,
        "display_name": DISPLAY_NAMES.get(suggestion, suggestion),
        "source_count": len({str(row.get("_source") or "-") for row in rows}),
        "trace_count": len(rows),
        "total_events": _sum_events(rows),
        "avg_recoupling_balance": recoupling,
        "avg_strain_quality": strain,
        "avg_carry_quality": carry,
        "avg_field_intake_pressure": field_input,
        "field_support_score": support,
        "field_pressure_score": pressure,
        "support_minus_pressure": support - pressure,
        "passive_reading": "eher_getragen" if support >= pressure else "eher_drucknah",
    }


def _aggregate_by_asset_suggestion(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row.get("_asset") or "-"), str(row.get("dominant_suggestion") or "-"))].append(row)
    output = [_score_group(asset, suggestion, group) for (asset, suggestion), group in grouped.items()]
    output.sort(key=lambda item: (str(item["asset"]), -float(item["support_minus_pressure"]), str(item["dominant_suggestion"])))
    return output


def _asset_summary(rows: list[dict[str, str]], detail_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("_asset") or "-")].append(row)

    detail_by_asset: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in detail_rows:
        detail_by_asset[str(row["asset"])].append(row)

    output: list[dict[str, object]] = []
    for asset, group in sorted(grouped.items()):
        total_events = _sum_events(group)
        counts = Counter(str(row.get("dominant_suggestion") or "-") for row in group)
        top_count_suggestion, top_count = counts.most_common(1)[0]
        strongest = max(detail_by_asset[asset], key=lambda item: float(item["support_minus_pressure"]))
        scored = _score_group(asset, "asset_total", group)
        scored.update(
            {
                "source_count": len({str(row.get("_source") or "-") for row in group}),
                "trace_count": len(group),
                "total_events": total_events,
                "top_count_suggestion": top_count_suggestion,
                "top_count_display": DISPLAY_NAMES.get(top_count_suggestion, top_count_suggestion),
                "top_count": top_count,
                "strongest_suggestion": strongest["dominant_suggestion"],
                "strongest_display": strongest["display_name"],
                "strongest_net": strongest["support_minus_pressure"],
            }
        )
        output.append(scored)
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "asset",
        "dominant_suggestion",
        "display_name",
        "passive_reading",
        "source_count",
        "trace_count",
        "total_events",
        "avg_recoupling_balance",
        "avg_strain_quality",
        "avg_carry_quality",
        "avg_field_intake_pressure",
        "field_support_score",
        "field_pressure_score",
        "support_minus_pressure",
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


def write_markdown(path: Path, summary_rows: list[dict[str, object]], detail_rows: list[dict[str, object]], total_rows: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 474 - Assetgetrennte Feldtragung der Regulationsvorschlaege",
        "",
        "Stand: 2026-06-21",
        "",
        "## Fragestellung",
        "",
        "Nutzen BTC, SOL und KAS dieselbe passive Wahrnehmungssprache, bilden aber unterschiedliche Trag-, Druck- und Entlastungsprofile aus?",
        "",
        "Diese Pruefung liest nur die vorhandenen Vorschlagsspuren aus den Berichten 460 bis 467 und 471. Die Basis-Memory 459 wird bewusst nicht als eigenes Asset mitgezaehlt.",
        "",
        "Wichtig: Das ist Diagnose. Keine Handlung, kein Gate, keine aktive Regulation und keine Feldsteuerung.",
        "",
        f"- Asset-Spuren: {total_rows}",
        "",
        "## Asset-Gesamtprofil",
        "",
        "| Asset | Quellen | Spuren | Ereignisse | haeufigster Vorschlag | staerkster Netto-Support | Support | Druck | Netto |",
        "|---|---:|---:|---:|---|---|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['asset']} | {row['source_count']} | {row['trace_count']} | {row['total_events']} | "
            f"{row['top_count_display']} ({row['top_count']}) | {row['strongest_display']} ({_fmt(row['strongest_net'])}) | "
            f"{_fmt(row['field_support_score'])} | {_fmt(row['field_pressure_score'])} | {_fmt(row['support_minus_pressure'])} |"
        )

    lines.extend(
        [
            "",
            "## Vorschlagsprofil je Asset",
            "",
            "| Asset | Vorschlag | Lesart | Quellen | Spuren | Ereignisse | Support | Druck | Netto | Rekopplung | Strain | Feldinput |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in detail_rows:
        lines.append(
            f"| {row['asset']} | {row['display_name']} | {row['passive_reading']} | {row['source_count']} | "
            f"{row['trace_count']} | {row['total_events']} | {_fmt(row['field_support_score'])} | "
            f"{_fmt(row['field_pressure_score'])} | {_fmt(row['support_minus_pressure'])} | "
            f"{_fmt(row['avg_recoupling_balance'])} | {_fmt(row['avg_strain_quality'])} | "
            f"{_fmt(row['avg_field_intake_pressure'])} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "BTC, SOL und KAS nutzen in dieser Diagnose dieselbe Vorschlagssprache: Fokus, Abstand, weicher aufnehmen, Sehen schaerfen, Feldkontakt entlasten und ruhig hinhoeren.",
            "",
            "Die Bedeutung liegt nicht in neuen Woertern je Asset, sondern in anderer Gewichtung:",
            "",
            "- BTC wirkt balancierter und verteilt die Vorschlaege gleichmaessiger.",
            "- SOL traegt deutlich mehr Abstand/Entlastungsnaehe, ohne die gemeinsame Sprache zu verlieren.",
            "- KAS zeigt ebenfalls starken Abstandszug, bleibt aber in derselben Vorschlagsfamilie lesbar.",
            "",
            "Uebergreifend bleibt `ruhig hinhoeren` eine stark getragene Aufnahmeart. Abstand und Kontaktentlastung liegen naeher an Entlastungsarbeit: Sie sind nicht schlecht, sondern zeigen, wo der Organismus weniger Rohkontakt oder mehr Distanz zur Weltwirkung brauchen koennte.",
            "",
            "## Schluss",
            "",
            "Die bisherige Lesart wird gestuetzt: MINI_DIO braucht keine asseteigenen Begriffe, um unterschiedliche Welten zu lesen. Die gleiche passive Wahrnehmungssprache kann verschiedene Feldtragungsprofile ausbilden.",
            "",
            "Wie es weitergeht: Als naechstes sollte daraus ein assetbezogenes Organismusprofil gelesen werden: welches Asset ruft mehr Abstand auf, welches mehr Hoeren, welches mehr Schaerfung, und ob diese Profile bei neuen Welten stabil bleiben.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = _read_asset_rows()
    detail_rows = _aggregate_by_asset_suggestion(rows)
    summary_rows = _asset_summary(rows, detail_rows)
    write_csv(CSV_DEFAULT, detail_rows)
    write_markdown(MD_DEFAULT, summary_rows, detail_rows, len(rows))
    print(f"wrote {CSV_DEFAULT}")
    print(f"wrote {MD_DEFAULT}")
    print(f"asset_rows={len(rows)} detail_rows={len(detail_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
