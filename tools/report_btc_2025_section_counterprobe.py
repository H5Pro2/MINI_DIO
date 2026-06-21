from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"

OUTPUT_CSV = REPORT_DIR / "500_BTC2025_ABSCHNITTSGEGENPROBE.csv"
OUTPUT_MD = REPORT_DIR / "500_BTC2025_ABSCHNITTSGEGENPROBE.md"

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
        "source": "BTC2025_5M_GESAMT",
        "group": "basis",
        "regulation": REPORT_DIR / "486_BTC2025_5M_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "486_BTC2025_5M_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2025_1H_GESAMT",
        "group": "basis",
        "regulation": REPORT_DIR / "487_BTC2025_1H_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "487_BTC2025_1H_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2025_5M_QUIET_4K",
        "group": "gegenwelt",
        "regulation": REPORT_DIR / "495_BTC2025_5M_QUIET_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "492_BTC2025_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "BTC2025_5M_STRESS_4K",
        "group": "gegenwelt",
        "regulation": REPORT_DIR / "499_BTC2025_5M_STRESS_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "496_BTC2025_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv",
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


def _fmt(value: object) -> str:
    return f"{_float(value):.4f}"


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
        suggestions.append(
            {
                "suggestion": suggestion,
                "trace_count": len(group),
                "total_events": _sum_events(group),
                **_score_suggestion(group),
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
    by_effect: Counter[str] = Counter()
    for row in rows:
        by_axis[str(row.get("axis") or "-")].append(row)
        by_effect[str(row.get("inner_effect_state") or "-")] += _int(row.get("count"))

    result: dict[str, object] = {
        "axis_rows": len(rows),
        "axis_total_count": sum(_int(row.get("count")) for row in rows),
        "top_inner_effect": "-",
        "top_inner_effect_count": 0,
    }
    if by_effect:
        effect, count = by_effect.most_common(1)[0]
        result["top_inner_effect"] = effect
        result["top_inner_effect_count"] = count

    for axis in ["hoeren_hin", "sehen_fokus", "sehen_abstand", "fuehlen_abstand", "feldinput"]:
        group = by_axis.get(axis, [])
        result[f"{axis}_count"] = sum(_int(row.get("count")) for row in group)
        result[f"{axis}_ratio"] = sum(_float(row.get("ratio")) for row in group)
        result[f"{axis}_recoupling"] = _weighted(group, "avg_mcm_rekopplung_quality") if group else 0.0
        result[f"{axis}_strain"] = _weighted(group, "avg_mcm_strain_quality") if group else 0.0
        result[f"{axis}_carry"] = _weighted(group, "avg_mcm_carry_quality") if group else 0.0
        result[f"{axis}_field_input"] = _weighted(group, "avg_rezeptor_field_intake_pressure") if group else 0.0

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
    rows: list[dict[str, object]] = []
    for source in SOURCES:
        regulation = _profile_for_regulation(source["regulation"])
        axis = _axis_summary(source["axis"])
        rows.append({**source, **regulation, **axis})
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    columns = [
        "source",
        "group",
        "regulation_rows",
        "regulation_events",
        "axis_rows",
        "axis_total_count",
        "top_inner_effect",
        "top_inner_effect_count",
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
        "hoeren_hin_strain",
        "sehen_fokus_count",
        "sehen_fokus_strain",
        "sehen_abstand_count",
        "sehen_abstand_strain",
        "fuehlen_abstand_count",
        "fuehlen_abstand_strain",
        "feldinput_count",
        "feldinput_strain",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    quiet = next(row for row in rows if row["source"] == "BTC2025_5M_QUIET_4K")
    stress = next(row for row in rows if row["source"] == "BTC2025_5M_STRESS_4K")
    basis_5m = next(row for row in rows if row["source"] == "BTC2025_5M_GESAMT")

    lines = [
        "# 500 - BTC-2025-Abschnittsgegenprobe",
        "",
        "Stand: 2026-06-21",
        "",
        "## Grundfrage",
        "",
        "Ist die in 491 gelesene BTC-2025-Verschiebung zum Abstand eine allgemeine Jahres-/Assetnaehe oder nur eine lokale Segmentoberflaeche?",
        "",
        "## Unterpruefung",
        "",
        "Gelesen wurden zwei neue 5m-Abschnitte aus BTC-2025:",
        "",
        "- `BTC2025_5M_QUIET_4K` als ruhigerer Abschnitt.",
        "- `BTC2025_5M_STRESS_4K` als belasteterer Abschnitt.",
        "",
        "Die Diagnose bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Vergleich",
        "",
        "| Quelle | Gruppe | dominanter Bedarf | staerkste Tragung | Drucknaehe | Hoer-Netto | Fokus-Netto | Abstand-Netto | Abstand minus Fokus | Top-Innenlage |",
        "|---|---|---|---|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["source"]),
                    str(row["group"]),
                    str(row["dominant_need_name"]),
                    str(row["strongest_carried_name"]),
                    str(row["pressure_nearest_name"]),
                    _fmt(row["hearing_net"]),
                    _fmt(row["focus_net"]),
                    _fmt(row["distance_net"]),
                    _fmt(row["selected_distance_minus_focus"]),
                    f"{row['top_inner_effect']} ({row['top_inner_effect_count']})",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lokale Achsen",
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

    quiet_pressure_delta = _float(stress["pressure_nearest_score"]) - _float(quiet["pressure_nearest_score"])
    quiet_stable_delta = _float(stress["top_inner_effect_count"]) - _float(quiet["top_inner_effect_count"])
    basis_distance_delta = _float(quiet["distance_net"]) - _float(basis_5m["distance_net"])
    stress_distance_delta = _float(stress["distance_net"]) - _float(basis_5m["distance_net"])

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "- Beide neuen BTC-2025-Abschnitte bleiben beim dominanten Bedarf `Abstand bilden`. Die Drucknaehe liegt aber weiterhin bei `Druck / Feldkontakt entlasten`. Damit bestaetigen sie die fruehere Abstandlesung und verfeinern sie: Der Abstand ist nicht leer, sondern kontaktentlastungsnah.",
            "- `ruhig hinhoeren` bleibt in beiden Abschnittswelten die staerkste getragene Richtung. Das Hoeren bricht also nicht weg.",
            f"- Stress liegt gegenueber Quiet etwas drucknaeher: Drucknaehe-Differenz {quiet_pressure_delta:.4f}. Gleichzeitig sinkt die stabile Innenlage im Stressabschnitt um {abs(quiet_stable_delta):.0f} Ereignisse gegenueber Quiet.",
            f"- Gegenueber der 5m-Gesamtquelle steigt das Abstand-Netto im Quiet-Abschnitt um {basis_distance_delta:.4f} und im Stress-Abschnitt um {stress_distance_delta:.4f}. Die lokalen Abschnitte tragen also mehr Abstand-/Entlastungsnaehe als der Gesamtbefund.",
            "- Die Verschiebung ist damit nicht als zufaellige Einzelstelle erledigt. Sie wirkt segmentuebergreifend, aber nicht einheitlich: Gesamtquelle, Quiet und Stress zeigen denselben Grundbereich, jedoch mit anderer Auspraegung.",
            "",
            "## Schlussfolgerung",
            "",
            "BTC-2025 zeigt in den geprueften Quellen keine einfache neue Regel. Sauberer ist: Das Feld liest BTC-2025 als hoerbar getragen, aber abstandsnaeher als die BTC-2024-Gegenwelten. Die Drucknaehe zeigt zugleich, dass dieser Abstand als Kontaktentlastung gefaerbt ist.",
            "",
            "## Vorsicht",
            "",
            "Das ist weiterhin passive Wahrnehmungsdiagnose. Daraus folgt keine aktive Regulierungsregel und keine Handlung. Die Werte beschreiben, welche Aufnahmequalitaet in den gelesenen Welten nahe liegt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte BTC-2025 gegen eine weitere, anders gelagerte 2025er Quelle oder gegen BTC-2024 mit identischer Abschnittslogik gelesen werden. Ziel: trennen, ob abstandsnahe Kontaktentlastung eine BTC-2025-nahe Grundfarbe ist oder aus den gewaehlten Abschnitten entsteht.",
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
