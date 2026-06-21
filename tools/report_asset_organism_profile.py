from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"
INPUT_CSV = REPORT_DIR / "474_ASSET_REGULATIONSVORSCHLAG_FELDTRAGUNG.csv"
OUTPUT_CSV = REPORT_DIR / "475_ASSET_ORGANISMUSPROFIL.csv"
OUTPUT_MD = REPORT_DIR / "475_ASSET_ORGANISMUSPROFIL.md"


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


def _read_rows() -> list[dict[str, str]]:
    with INPUT_CSV.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _asset_rows(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(str(row.get("asset") or "-"), []).append(row)
    return grouped


def _profile_label(top_need: str, strongest: str) -> str:
    if strongest == "stable_listening_pull" and top_need == "distance_pull":
        return "abstandsnahe_aufnahme_mit_getragenem_hinhoeren"
    if strongest == "stable_listening_pull" and top_need == "focus_pull":
        return "balancierte_aufnahme_mit_fokusoberflaeche"
    if strongest == "stable_listening_pull":
        return "hoernahe_aufnahme_mit_getragener_rekopplung"
    return "gemischtes_aufnahmeprofil"


def build_profiles(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    profiles: list[dict[str, object]] = []
    for asset, group in sorted(_asset_rows(rows).items()):
        total_traces = sum(_int(row.get("trace_count")) for row in group)
        total_events = sum(_int(row.get("total_events")) for row in group)
        top_need = max(group, key=lambda row: (_int(row.get("trace_count")), _int(row.get("total_events"))))
        strongest = max(group, key=lambda row: _float(row.get("support_minus_pressure")))
        pressure_near = max(group, key=lambda row: _float(row.get("field_pressure_score")))

        by_suggestion = {str(row.get("dominant_suggestion") or "-"): row for row in group}
        hearing = by_suggestion.get("stable_listening_pull", {})
        seeing = by_suggestion.get("sharpening_pull", {})
        focus = by_suggestion.get("focus_pull", {})
        distance = by_suggestion.get("distance_pull", {})
        relief = by_suggestion.get("contact_relief_pull", {})
        softening = by_suggestion.get("softening_pull", {})

        profiles.append(
            {
                "asset": asset,
                "total_traces": total_traces,
                "total_events": total_events,
                "dominant_need": top_need.get("dominant_suggestion", "-"),
                "dominant_need_name": top_need.get("display_name", "-"),
                "dominant_need_trace_share": _int(top_need.get("trace_count")) / total_traces if total_traces else 0.0,
                "dominant_need_event_share": _int(top_need.get("total_events")) / total_events if total_events else 0.0,
                "strongest_carried": strongest.get("dominant_suggestion", "-"),
                "strongest_carried_name": strongest.get("display_name", "-"),
                "strongest_carried_net": _float(strongest.get("support_minus_pressure")),
                "pressure_nearest": pressure_near.get("dominant_suggestion", "-"),
                "pressure_nearest_name": pressure_near.get("display_name", "-"),
                "pressure_nearest_score": _float(pressure_near.get("field_pressure_score")),
                "hearing_net": _float(hearing.get("support_minus_pressure")),
                "seeing_net": _float(seeing.get("support_minus_pressure")),
                "focus_net": _float(focus.get("support_minus_pressure")),
                "distance_net": _float(distance.get("support_minus_pressure")),
                "relief_net": _float(relief.get("support_minus_pressure")),
                "softening_net": _float(softening.get("support_minus_pressure")),
                "distance_trace_share": _int(distance.get("trace_count")) / total_traces if total_traces else 0.0,
                "relief_trace_share": _int(relief.get("trace_count")) / total_traces if total_traces else 0.0,
                "softening_trace_share": _int(softening.get("trace_count")) / total_traces if total_traces else 0.0,
                "organism_profile": _profile_label(
                    str(top_need.get("dominant_suggestion") or "-"),
                    str(strongest.get("dominant_suggestion") or "-"),
                ),
            }
        )
    return profiles


def write_csv(rows: list[dict[str, object]]) -> None:
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "asset",
        "organism_profile",
        "total_traces",
        "total_events",
        "dominant_need",
        "dominant_need_name",
        "dominant_need_trace_share",
        "dominant_need_event_share",
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
        "relief_net",
        "softening_net",
        "distance_trace_share",
        "relief_trace_share",
        "softening_trace_share",
    ]
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def write_markdown(rows: list[dict[str, object]]) -> None:
    lines = [
        "# 475 - Assetbezogenes Organismusprofil",
        "",
        "Stand: 2026-06-21",
        "",
        "## Fragestellung",
        "",
        "Welche passive Aufnahmefaehigkeit wird je Asset haeufig aufgerufen, und welche Aufnahmefaehigkeit wird vom Feld am staerksten getragen?",
        "",
        "Diese Diagnose trennt bewusst:",
        "",
        "- haeufiger Bedarf: welche Faehigkeit taucht oft auf?",
        "- getragene Faehigkeit: welche Faehigkeit hat den staerksten Netto-Support?",
        "- Drucknaehe: welche Faehigkeit liegt am naechsten an Feld-/Kontaktlast?",
        "",
        "Das ist ein Organismusprofil, keine Handlungsvorgabe.",
        "",
        "## Profilmatrix",
        "",
        "| Asset | Profil | Spuren | Ereignisse | haeufiger Bedarf | Bedarf Anteil | staerkste Tragung | Netto | drucknah | Druck |",
        "|---|---|---:|---:|---|---:|---|---:|---|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['asset']} | {row['organism_profile']} | {row['total_traces']} | {row['total_events']} | "
            f"{row['dominant_need_name']} | {_fmt(row['dominant_need_trace_share'])} | "
            f"{row['strongest_carried_name']} | {_fmt(row['strongest_carried_net'])} | "
            f"{row['pressure_nearest_name']} | {_fmt(row['pressure_nearest_score'])} |"
        )

    lines.extend(
        [
            "",
            "## Sinnesprofil",
            "",
            "| Asset | Hoeren Netto | Sehen Netto | Fokus Netto | Abstand Netto | Kontaktentlastung Netto | Weicher aufnehmen Netto |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['asset']} | {_fmt(row['hearing_net'])} | {_fmt(row['seeing_net'])} | "
            f"{_fmt(row['focus_net'])} | {_fmt(row['distance_net'])} | {_fmt(row['relief_net'])} | "
            f"{_fmt(row['softening_net'])} |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "BTC wirkt in dieser Schicht als balancierteres Aufnahmeprofil: Fokus taucht haeufig auf, aber getragen wird vor allem ruhiges Hinhoeren.",
            "",
            "SOL und KAS wirken abstandsnaeher: Abstand wird haeufiger aufgerufen, aber auch dort traegt ruhiges Hinhoeren am staerksten. Das ist fachlich wichtig, weil Bedarf und Tragung nicht identisch sind.",
            "",
            "Damit entsteht eine saubere Trennung:",
            "",
            "```text",
            "Was der Organismus oft braucht",
            "ist nicht automatisch das,",
            "was ihn am besten traegt.",
            "```",
            "",
            "Genau diese Trennung ist fuer spaetere rezeptorisch-regulatorische Wahrnehmung relevant. MINI_DIO sollte nicht einfach das Haeufigste verstaerken, sondern lernen, welche Aufnahmeart in welcher Weltlage tragend rekoppelt.",
            "",
            "## Grenze",
            "",
            "- kein Gate",
            "- keine Strategie",
            "- keine aktive Regulation",
            "- keine automatische Veraenderung der Sinnesaufnahme",
            "- nur passive Diagnose vorhandener Feldtragungsprofile",
            "",
            "Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese Assetprofile bei neuen Welten stabil bleiben oder ob SOL, BTC und KAS ihre Aufnahmeprofile unter anderer Weltspannung verschieben.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = _read_rows()
    profiles = build_profiles(rows)
    write_csv(profiles)
    write_markdown(profiles)
    print(f"wrote {OUTPUT_CSV}")
    print(f"wrote {OUTPUT_MD}")
    print(f"assets={len(profiles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
