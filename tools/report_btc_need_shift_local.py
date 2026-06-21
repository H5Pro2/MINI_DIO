from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"

OUTPUT_CSV = REPORT_DIR / "491_BTC2025_BEDARFSVERSCHIEBUNG_LOKAL.csv"
OUTPUT_MD = REPORT_DIR / "491_BTC2025_BEDARFSVERSCHIEBUNG_LOKAL.md"

DISPLAY_NAMES = {
    "focus_pull": "Fokus halten / vertiefen",
    "distance_pull": "Abstand bilden",
    "softening_pull": "leiser / weicher aufnehmen",
    "sharpening_pull": "Sehen schaerfen",
    "contact_relief_pull": "Druck / Feldkontakt entlasten",
    "stable_listening_pull": "ruhig hinhoeren",
}

SOURCES = [
    {
        "source": "BTC2024_5M_QUIET",
        "year": "2024",
        "timeframe": "5m",
        "world": "quiet",
        "regulation": REPORT_DIR / "460_BTC2024_5M_QUIET_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "435_BTC2024_5M_QUIET_4K_LONG_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2024_5M_STRESS",
        "year": "2024",
        "timeframe": "5m",
        "world": "stress",
        "regulation": REPORT_DIR / "461_BTC2024_5M_STRESS_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "440_BTC2024_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2024_1H_QUIET",
        "year": "2024",
        "timeframe": "1h",
        "world": "quiet",
        "regulation": REPORT_DIR / "462_BTC2024_1H_QUIET_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "451_BTC2024_1H_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2024_1H_STRESS",
        "year": "2024",
        "timeframe": "1h",
        "world": "stress",
        "regulation": REPORT_DIR / "463_BTC2024_1H_STRESS_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "445_BTC2024_1H_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2025_5M",
        "year": "2025",
        "timeframe": "5m",
        "world": "test1",
        "regulation": REPORT_DIR / "486_BTC2025_5M_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "486_BTC2025_5M_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2025_1H",
        "year": "2025",
        "timeframe": "1h",
        "world": "test1",
        "regulation": REPORT_DIR / "487_BTC2025_1H_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "487_BTC2025_1H_SINNESACHSEN_EPISODENKARTE.csv",
    },
]


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


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _weighted(rows: list[dict[str, str]], column: str, count_column: str = "count") -> float:
    total = sum(max(1, _int(row.get(count_column))) for row in rows)
    if total <= 0:
        return 0.0
    return sum(max(1, _int(row.get(count_column))) * _float(row.get(column)) for row in rows) / total


def _weighted_regulation(rows: list[dict[str, str]], column: str) -> float:
    total = sum(max(1, _int(row.get("total_events"))) for row in rows)
    if total <= 0:
        return 0.0
    return sum(max(1, _int(row.get("total_events"))) * _float(row.get(column)) for row in rows) / total


def _score_suggestion(rows: list[dict[str, str]]) -> dict[str, float]:
    recoupling = _weighted_regulation(rows, "recoupling_balance")
    strain = _weighted_regulation(rows, "strain_quality")
    carry = _weighted_regulation(rows, "carry_quality")
    field_input = _weighted_regulation(rows, "field_intake_pressure")
    support = _clamp((recoupling * 0.45) + (carry * 0.35) + ((1.0 - strain) * 0.10) + ((1.0 - field_input) * 0.10))
    pressure = _clamp((strain * 0.45) + (field_input * 0.40) + ((1.0 - recoupling) * 0.15))
    return {
        "support": support,
        "pressure": pressure,
        "net": support - pressure,
        "recoupling": recoupling,
        "strain": strain,
        "carry": carry,
        "field_input": field_input,
    }


def _sum_events(rows: list[dict[str, str]]) -> int:
    return sum(_int(row.get("total_events")) for row in rows)


def _profile_for_regulation(path: Path) -> dict[str, object]:
    rows = _read_rows(path)
    by_suggestion: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_suggestion[str(row.get("dominant_suggestion") or "-")].append(row)

    suggestions: list[dict[str, object]] = []
    for suggestion, group in by_suggestion.items():
        scores = _score_suggestion(group)
        suggestions.append(
            {
                "suggestion": suggestion,
                "trace_count": len(group),
                "total_events": _sum_events(group),
                **scores,
            }
        )

    top_need = max(suggestions, key=lambda row: (int(row["trace_count"]), int(row["total_events"])))
    strongest = max(suggestions, key=lambda row: float(row["net"]))
    pressure = max(suggestions, key=lambda row: float(row["pressure"]))

    def net_for(name: str) -> float:
        for row in suggestions:
            if row["suggestion"] == name:
                return float(row["net"])
        return 0.0

    return {
        "regulation_rows": len(rows),
        "regulation_events": _sum_events(rows),
        "dominant_need": top_need["suggestion"],
        "dominant_need_name": DISPLAY_NAMES.get(str(top_need["suggestion"]), str(top_need["suggestion"])),
        "dominant_need_trace_count": top_need["trace_count"],
        "strongest_carried": strongest["suggestion"],
        "strongest_carried_name": DISPLAY_NAMES.get(str(strongest["suggestion"]), str(strongest["suggestion"])),
        "strongest_carried_net": strongest["net"],
        "pressure_nearest": pressure["suggestion"],
        "pressure_nearest_name": DISPLAY_NAMES.get(str(pressure["suggestion"]), str(pressure["suggestion"])),
        "pressure_nearest_score": pressure["pressure"],
        "hearing_net": net_for("stable_listening_pull"),
        "focus_net": net_for("focus_pull"),
        "distance_net": net_for("distance_pull"),
        "contact_relief_net": net_for("contact_relief_pull"),
        "sharpening_net": net_for("sharpening_pull"),
        "softening_net": net_for("softening_pull"),
    }


def _axis_summary(path: Path) -> dict[str, object]:
    rows = _read_rows(path)
    by_axis: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_axis[str(row.get("axis") or "-")].append(row)

    result: dict[str, object] = {
        "axis_rows": len(rows),
        "axis_total_count": sum(_int(row.get("count")) for row in rows),
    }

    for axis in ["hoeren_hin", "sehen_fokus", "sehen_abstand", "fuehlen_abstand", "feldinput"]:
        group = by_axis.get(axis, [])
        result[f"{axis}_count"] = sum(_int(row.get("count")) for row in group)
        result[f"{axis}_ratio"] = sum(_float(row.get("ratio")) for row in group)
        result[f"{axis}_recoupling"] = _weighted(group, "avg_mcm_rekopplung_quality") if group else 0.0
        result[f"{axis}_strain"] = _weighted(group, "avg_mcm_strain_quality") if group else 0.0
        result[f"{axis}_carry"] = _weighted(group, "avg_mcm_carry_quality") if group else 0.0
        result[f"{axis}_field_input"] = _weighted(group, "avg_rezeptor_field_intake_pressure") if group else 0.0
        result[f"{axis}_visual_focus_tendency"] = _weighted(group, "avg_perception_visual_focus_tendency") if group else 0.0
        result[f"{axis}_visual_distance_tendency"] = _weighted(group, "avg_perception_visual_distance_tendency") if group else 0.0
        result[f"{axis}_felt_distance_tendency"] = _weighted(group, "avg_perception_felt_distance_tendency") if group else 0.0
        result[f"{axis}_auditory_listen_tendency"] = _weighted(group, "avg_perception_auditory_listen_tendency") if group else 0.0

    result["selected_distance_ratio"] = (
        float(result["sehen_abstand_ratio"])
        + float(result["fuehlen_abstand_ratio"])
        + float(result["feldinput_ratio"])
    )
    result["selected_focus_ratio"] = float(result["sehen_fokus_ratio"])
    result["selected_hearing_ratio"] = float(result["hoeren_hin_ratio"])
    result["selected_distance_minus_focus"] = float(result["selected_distance_ratio"]) - float(result["selected_focus_ratio"])
    return result


def _build_rows() -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    missing = []
    for source in SOURCES:
        if not Path(source["regulation"]).exists():
            missing.append(str(source["regulation"]))
        if not Path(source["axis"]).exists():
            missing.append(str(source["axis"]))
    if missing:
        raise FileNotFoundError("Missing source files:\n" + "\n".join(missing))

    for source in SOURCES:
        row: dict[str, object] = {
            "source": source["source"],
            "year": source["year"],
            "timeframe": source["timeframe"],
            "world": source["world"],
        }
        row.update(_profile_for_regulation(Path(source["regulation"])))
        row.update(_axis_summary(Path(source["axis"])))
        output.append(row)
    return output


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    columns = [
        "source",
        "year",
        "timeframe",
        "world",
        "regulation_rows",
        "regulation_events",
        "axis_rows",
        "axis_total_count",
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
        "focus_net",
        "distance_net",
        "contact_relief_net",
        "selected_hearing_ratio",
        "selected_focus_ratio",
        "selected_distance_ratio",
        "selected_distance_minus_focus",
        "hoeren_hin_count",
        "hoeren_hin_ratio",
        "hoeren_hin_recoupling",
        "hoeren_hin_strain",
        "hoeren_hin_field_input",
        "sehen_fokus_count",
        "sehen_fokus_ratio",
        "sehen_fokus_recoupling",
        "sehen_fokus_strain",
        "sehen_fokus_field_input",
        "sehen_abstand_count",
        "sehen_abstand_ratio",
        "sehen_abstand_recoupling",
        "sehen_abstand_strain",
        "sehen_abstand_field_input",
        "fuehlen_abstand_count",
        "fuehlen_abstand_ratio",
        "fuehlen_abstand_recoupling",
        "fuehlen_abstand_strain",
        "fuehlen_abstand_field_input",
        "feldinput_count",
        "feldinput_ratio",
        "feldinput_recoupling",
        "feldinput_strain",
        "feldinput_field_input",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["year"])].append(row)

    lines = [
        "# 491 - BTC-2025-Bedarfsverschiebung lokal gelesen",
        "",
        "Stand: 2026-06-21",
        "",
        "## Grundfrage",
        "",
        "Warum verschiebt BTC in den 2025er Quellen den dominanten Wahrnehmungsbedarf von Fokus zu Abstand, obwohl der Hoertrag stabil bleibt?",
        "",
        "## Einordnung",
        "",
        "Diese Diagnose ist eine Unterpruefung der Assetprofil-Stabilitaet. Sie ist passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "Gelesen werden zwei Ebenen:",
        "",
        "- Regulationsvorschlag: Welche Wahrnehmungsfaehigkeit wird dominant angefragt?",
        "- Lokale Sinnesachsen: Welche Achsenanteile und MCM-Feldqualitaeten liegen darunter?",
        "",
        "## Quellenuebersicht",
        "",
        "| Quelle | Bedarf | Getragen | Drucknaehe | Hoer-Netto | Fokus-Netto | Abstand-Netto | Abstand minus Fokus |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["source"]),
                    str(row["dominant_need_name"]),
                    str(row["strongest_carried_name"]),
                    str(row["pressure_nearest_name"]),
                    _fmt(row["hearing_net"]),
                    _fmt(row["focus_net"]),
                    _fmt(row["distance_net"]),
                    _fmt(row["selected_distance_minus_focus"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lokale Achsenlesung",
            "",
            "| Quelle | Hoeren-Anteil | Fokus-Anteil | Abstand/Feldkontakt-Anteil | hoeren Strain | sehen Fokus Strain | sehen Abstand Strain | fuehlen Abstand Strain | Feldinput Strain |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["source"]),
                    _fmt(row["selected_hearing_ratio"]),
                    _fmt(row["selected_focus_ratio"]),
                    _fmt(row["selected_distance_ratio"]),
                    _fmt(row["hoeren_hin_strain"]),
                    _fmt(row["sehen_fokus_strain"]),
                    _fmt(row["sehen_abstand_strain"]),
                    _fmt(row["fuehlen_abstand_strain"]),
                    _fmt(row["feldinput_strain"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Jahreslesung",
            "",
            "| Jahr | Quellen | Bedarfsmuster | Hoertrag | Achsenhinweis |",
            "|---|---:|---|---|---|",
        ]
    )
    for year in sorted(grouped):
        group = grouped[year]
        need_names = sorted(set(str(row["dominant_need_name"]) for row in group))
        carried_names = sorted(set(str(row["strongest_carried_name"]) for row in group))
        avg_distance_minus_focus = sum(float(row["selected_distance_minus_focus"]) for row in group) / max(1, len(group))
        lines.append(
            f"| {year} | {len(group)} | {', '.join(need_names)} | {', '.join(carried_names)} | Abstand-Fokus {avg_distance_minus_focus:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "- BTC-2024 bleibt in den vier gelesenen Quellen beim dominanten Fokusbedarf. Der staerkste tragende Anteil bleibt trotzdem `ruhig hinhoeren`.",
            "- BTC-2025 verschiebt beide Quellen, 5m und 1h, zum dominanten Abstandbedarf. Damit ist die Verschiebung nicht sauber als reine Zeitebene erklaerbar.",
            "- Der Hoertrag bricht nicht weg. `ruhig hinhoeren` bleibt auch 2025 die staerkste getragene Richtung.",
            "- Die lokalen Achsenanteile bleiben relativ nah beieinander. Die Verschiebung liegt daher nicht grob in mehr Roh-Abstandsaufnahme, sondern eher in der Bedeutungs-/Regulationsgewichtung nach der Aufnahme.",
            "- Die lokale Lesung spricht fuer eine andere konkrete Weltspannung oder Segmentoberflaeche: BTC-2025 will weiter hoeren, aber die aufgenommene Lage wird staerker als Abstand/Kontaktentlastung verarbeitet.",
            "- Die Diagnose zeigt keine neue Handlungsschicht. Sie zeigt nur, dass der Organismus dieselbe Assetnaehe in einer anderen Weltlage anders aufnehmen will.",
            "",
            "## Vorsicht",
            "",
            "Der Befund belegt keine allgemeine BTC-2025-Regel. Er sagt nur: In diesen zwei 2025er Quellen tritt die Abstandsanforderung konsistent auf, waehrend 2024 in den vorhandenen Gegenwelten fokussierter bleibt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine BTC-2025-Gegenwelt aus einem anderen Abschnitt gelesen werden. Wenn Abstand erneut dominiert, wird es jahres-/assetnaher. Wenn Fokus zurueckkommt, war es eher eine lokale Weltspannungszone.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = _build_rows()
    _write_csv(OUTPUT_CSV, rows)
    _write_markdown(OUTPUT_MD, rows)
    print(f"wrote {OUTPUT_CSV}")
    print(f"wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
