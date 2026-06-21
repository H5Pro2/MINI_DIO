from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from report_btc_2025_section_counterprobe import _axis_summary, _fmt, _profile_for_regulation


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "docs" / "befunde"

OUTPUT_CSV = REPORT_DIR / "518_SOL2024_2025_ABSCHNITTSVERGLEICH.csv"
OUTPUT_MD = REPORT_DIR / "518_SOL2024_2025_ABSCHNITTSVERGLEICH.md"

SOURCES = [
    {
        "source": "SOL2024_5M_QUIET_4K",
        "year": "2024",
        "section": "quiet",
        "regulation": REPORT_DIR / "505_SOL2024_5M_QUIET_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "502_SOL2024_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "SOL2024_5M_STRESS_4K",
        "year": "2024",
        "section": "stress",
        "regulation": REPORT_DIR / "509_SOL2024_5M_STRESS_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "506_SOL2024_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "SOL2025_5M_QUIET_4K",
        "year": "2025",
        "section": "quiet",
        "regulation": REPORT_DIR / "513_SOL2025_5M_QUIET_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "510_SOL2025_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
    {
        "source": "SOL2025_5M_STRESS_4K",
        "year": "2025",
        "section": "stress",
        "regulation": REPORT_DIR / "517_SOL2025_5M_STRESS_4K_REGULATIONSVORSCHLAG.csv",
        "axis": REPORT_DIR / "514_SOL2025_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv",
    },
]


def _build_rows() -> list[dict[str, object]]:
    return [{**source, **_profile_for_regulation(source["regulation"]), **_axis_summary(source["axis"])} for source in SOURCES]


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    columns = [
        "source",
        "year",
        "section",
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
        "top_inner_effect",
        "top_inner_effect_count",
        "hoeren_hin_strain",
        "sehen_fokus_strain",
        "sehen_abstand_strain",
        "fuehlen_abstand_strain",
        "feldinput_strain",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def _year_summary(rows: list[dict[str, object]]) -> list[str]:
    lines = [
        "| Jahr | Quellen | Bedarfsmuster | staerkste Tragung | mittl. Hoer-Netto | mittl. Fokus-Netto | mittl. Abstand-Netto | mittl. Abstand-Fokus |",
        "|---|---:|---|---|---:|---:|---:|---:|",
    ]
    for year in sorted({str(row["year"]) for row in rows}):
        group = [row for row in rows if str(row["year"]) == year]
        needs = Counter(str(row["dominant_need_name"]) for row in group)
        carried = Counter(str(row["strongest_carried_name"]) for row in group)
        avg_hearing = sum(float(row["hearing_net"]) for row in group) / max(1, len(group))
        avg_focus = sum(float(row["focus_net"]) for row in group) / max(1, len(group))
        avg_distance = sum(float(row["distance_net"]) for row in group) / max(1, len(group))
        avg_distance_focus = sum(float(row["selected_distance_minus_focus"]) for row in group) / max(1, len(group))
        lines.append(
            "| "
            + " | ".join(
                [
                    year,
                    str(len(group)),
                    ", ".join(f"{name} ({count})" for name, count in needs.most_common()),
                    ", ".join(f"{name} ({count})" for name, count in carried.most_common()),
                    _fmt(avg_hearing),
                    _fmt(avg_focus),
                    _fmt(avg_distance),
                    _fmt(avg_distance_focus),
                ]
            )
            + " |"
        )
    return lines


def _section_delta(rows: list[dict[str, object]]) -> list[str]:
    lines = [
        "| Abschnitt | Bedarf 2024 | Bedarf 2025 | Hoer-Netto Delta | Fokus-Netto Delta | Abstand-Netto Delta | Drucknaehe Delta |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for section in ["quiet", "stress"]:
        old = next(row for row in rows if row["year"] == "2024" and row["section"] == section)
        new = next(row for row in rows if row["year"] == "2025" and row["section"] == section)
        lines.append(
            "| "
            + " | ".join(
                [
                    section,
                    str(old["dominant_need_name"]),
                    str(new["dominant_need_name"]),
                    _fmt(float(new["hearing_net"]) - float(old["hearing_net"])),
                    _fmt(float(new["focus_net"]) - float(old["focus_net"])),
                    _fmt(float(new["distance_net"]) - float(old["distance_net"])),
                    _fmt(float(new["pressure_nearest_score"]) - float(old["pressure_nearest_score"])),
                ]
            )
            + " |"
        )
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 518 - SOL-2024/2025-Abschnittsvergleich",
        "",
        "Stand: 2026-06-21",
        "",
        "## Grundfrage",
        "",
        "Zeigt SOL dieselbe 2025-Abstandsverschiebung wie BTC, wenn 2024 und 2025 mit derselben 5m-Quiet-/Stress-Abschnittslogik gelesen werden?",
        "",
        "## Einordnung",
        "",
        "Diese Diagnose ist passiv. Sie prueft, ob die BTC-2025-Lesung assetnah oder allgemeiner weltzeit-/regimenaeher wirkt.",
        "",
        "## Einzelquellen",
        "",
        "| Quelle | Bedarf | staerkste Tragung | Drucknaehe | Hoer-Netto | Fokus-Netto | Abstand-Netto | Abstand minus Fokus | Top-Innenlage |",
        "|---|---|---|---|---:|---:|---:|---:|---|",
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
                    f"{row['top_inner_effect']} ({row['top_inner_effect_count']})",
                ]
            )
            + " |"
        )

    lines.extend(["", "## Jahresverdichtung", "", *_year_summary(rows), "", "## Abschnittsdelta", "", *_section_delta(rows)])
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "- SOL bleibt in allen vier Abschnittswelten beim dominanten Bedarf `Abstand bilden`.",
            "- `ruhig hinhoeren` bleibt auch hier die staerkste getragene Richtung.",
            "- Damit reproduziert SOL nicht den BTC-Umschlag von Fokus 2024 zu Abstand 2025. SOL war bereits 2024 abstandsnah.",
            "- Die 2025er Veraenderung ist bei SOL feiner: nicht ein Wechsel der Bedarfsklasse, sondern Veraenderung von Staerke, Drucknaehe und Innenlage.",
            "",
            "## Schlussfolgerung",
            "",
            "Die BTC-2025-Verschiebung wirkt nach dieser Gegenprobe eher BTC-spezifisch oder zumindest assetprofilnah. SOL zeigt eine stabilere abstandsnahe Grundaufnahme ueber beide Jahre.",
            "",
            "## Vorsicht",
            "",
            "Der Befund sagt nicht, dass SOL unveraenderlich ist. Er sagt nur: In diesen vier 5m-Abschnitten kippt SOL nicht wie BTC von Fokus zu Abstand, sondern bleibt abstandsnah.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte KAS oder eine weitere BTC/SOL-Zeitebene mit derselben Abschnittslogik gelesen werden. Ziel: trennen, ob BTC ein eigener Wahrnehmungstyp ist oder ob der Effekt in bestimmten Zeitaufloesungen wiederkehrt.",
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
