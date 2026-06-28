from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.strip():
        return []
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _counter_text(values: list[str]) -> str:
    counter = Counter(value for value in values if value)
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common()) if counter else "-"


def _find_candidate_rows(rows: list[dict[str, str]], candidate: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for row in rows:
        if row.get("visual_form") == candidate or row.get("typology") == candidate or row.get("mode") == candidate:
            result.append(row)
    return result


def build_report(
    stability_rows: list[dict[str, str]],
    library_rows: list[dict[str, str]],
    candidate_detail_rows: list[dict[str, str]],
    candidate_summary_rows: list[dict[str, str]],
    candidate: str,
    known_visual_form: str,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    stability_match = next((row for row in stability_rows if row.get("visual_form") == known_visual_form), {})
    library_match = next((row for row in library_rows if row.get("visual_form") == known_visual_form), {})
    candidate_details = _find_candidate_rows(candidate_detail_rows, candidate)
    candidate_summary = next((row for row in candidate_summary_rows if row.get("typology") == candidate), {})

    details: list[dict[str, object]] = []
    for row in candidate_details:
        details.append(
            {
                "candidate": candidate,
                "known_visual_form": known_visual_form,
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "ticks": f"{row.get('tick_min', '-')}-{row.get('tick_max', '-')}",
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "return_pct": round(_float(row, "main_return_pct"), 6),
                "range_pct": round(_float(row, "main_range_pct"), 6),
                "before_return_pct": round(_float(row, "before_return_pct"), 6),
                "after_return_pct": round(_float(row, "after_return_pct"), 6),
                "pressure_abs": round(_float(row, "pressure_delta_abs_avg"), 6),
                "rekopplung_abs": round(_float(row, "rekopplung_delta_abs_avg"), 6),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )

    in_library = bool(library_match)
    stability_class = stability_match.get("stability_class", "nicht_in_1026")
    recurrence = int(float(stability_match.get("recurrence_count", "0") or 0))
    world_variety = int(float(stability_match.get("world_variety", "0") or 0))
    candidate_count = int(float(candidate_summary.get("count", "0") or len(details)))

    if in_library:
        extension_state = "bereits_robuste_bibliotheksform"
        interpretation = "Der Kandidat ist bereits Teil der robusten Bibliothek."
    elif stability_class == "familiengebundene_bedeutungsform" and candidate_count > 0:
        extension_state = "bibliothekserweiterung_kandidat"
        interpretation = (
            "Der Kandidat ist keine robuste Bibliotheksform, aber eine wiederkehrende familiengebundene Form. "
            "KAS aktiviert diese Form erneut und macht sie als Erweiterungskandidat sichtbar."
        )
    elif candidate_count > 0:
        extension_state = "lokaler_erweiterungskandidat"
        interpretation = "Der Kandidat erscheint lokal, hat aber noch keine ausreichende Vorreife in der Bibliothek."
    else:
        extension_state = "nicht_aktiviert"
        interpretation = "Der Kandidat wurde in dieser Gegenprobe nicht aktiviert."

    summary = {
        "candidate": candidate,
        "known_visual_form": known_visual_form,
        "extension_state": extension_state,
        "in_robust_library": int(in_library),
        "known_stability_class": stability_class,
        "known_recurrence_count": recurrence,
        "known_world_variety": world_variety,
        "candidate_holdout_count": candidate_count,
        "candidate_worlds": _counter_text([str(row["world"]) for row in details]),
        "candidate_movements": _counter_text([str(row["dominant_movement"]) for row in details]),
        "avg_return_pct": round(sum(float(row["return_pct"]) for row in details) / len(details), 6) if details else 0.0,
        "avg_range_pct": round(sum(float(row["range_pct"]) for row in details) / len(details), 6) if details else 0.0,
        "avg_pressure_abs": round(sum(float(row["pressure_abs"]) for row in details) / len(details), 6) if details else 0.0,
        "avg_rekopplung_abs": round(sum(float(row["rekopplung_abs"]) for row in details) / len(details), 6) if details else 0.0,
        "interpretation": interpretation,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }
    return details, summary


def _write_md(path: Path, details: list[dict[str, object]], summary: dict[str, object]) -> None:
    lines = [
        "# 1034 - Erweiterungskandidat Rekopplung nach Abverkauf",
        "",
        "Passive Isolation des Kandidaten `rekopplung_nach_abverkauf` nach der KAS-Gegenprobe.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Kandidatenlesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine feste Bedeutungsaufnahme ohne weitere Bestaetigung",
        "",
        "## Kurzbefund",
        "",
        f"- Kandidat: `{summary['candidate']}`",
        f"- zugeordnete visuelle Form: `{summary['known_visual_form']}`",
        f"- Erweiterungsstatus: `{summary['extension_state']}`",
        f"- in robuster Bibliothek 1027: `{summary['in_robust_library']}`",
        f"- bekannter 1026-Status: `{summary['known_stability_class']}`",
        f"- bekannte Wiederkehr: `{summary['known_recurrence_count']}` Belege in `{summary['known_world_variety']}` Welten",
        f"- KAS-Holdout-Belege: `{summary['candidate_holdout_count']}`",
        f"- KAS-Bewegungen: `{summary['candidate_movements']}`",
        f"- Ø Return %: `{summary['avg_return_pct']}`",
        f"- Ø Range %: `{summary['avg_range_pct']}`",
        f"- Ø Druck: `{summary['avg_pressure_abs']}`",
        f"- Ø Rekopplung: `{summary['avg_rekopplung_abs']}`",
        "",
        "## Deutung",
        "",
        str(summary["interpretation"]),
        "",
        "## Detailbelege",
        "",
        "| Welt | Paar | Ticks | Chartzone | Bewegung | Return % | Range % | Druck | Rekopplung |",
        "|---|---|---|---|---|---:|---:|---:|---:|",
    ]
    for row in details:
        lines.append(
            f"| `{row['world']}` | `{row['pair']}` | `{row['ticks']}` | `{row['chart_zone']}` | "
            f"`{row['dominant_movement']}` | {row['return_pct']} | {row['range_pct']} | "
            f"{row['pressure_abs']} | {row['rekopplung_abs']} |"
        )
    lines.extend(
        [
            "",
            "## Schluss",
            "",
            "`rekopplung_nach_abverkauf` sollte noch nicht als robuste Bibliotheksform behandelt werden. "
            "Der Kandidat ist aber mehr als ein Einzelfehler: Er liegt bereits als familiengebundene Form vor "
            "und wird in KAS erneut aktiviert. Fachlich ist das eine offene Erweiterungsform.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte der Kandidat gegen eine weitere unabhaengige Welt gelesen werden. Erst wenn er dort wiederkehrt, kann er als neue passive Bibliothekserweiterung aufgenommen werden.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stability", type=Path, required=True)
    parser.add_argument("--library", type=Path, required=True)
    parser.add_argument("--candidate-detail", type=Path, required=True)
    parser.add_argument("--candidate-summary", type=Path, required=True)
    parser.add_argument("--candidate", default="rekopplung_nach_abverkauf")
    parser.add_argument("--known-visual-form", default="erholung_nach_vorlast")
    parser.add_argument("--out-details", type=Path, required=True)
    parser.add_argument("--out-summary", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    details, summary = build_report(
        stability_rows=_read_rows(args.stability),
        library_rows=_read_rows(args.library),
        candidate_detail_rows=_read_rows(args.candidate_detail),
        candidate_summary_rows=_read_rows(args.candidate_summary),
        candidate=args.candidate,
        known_visual_form=args.known_visual_form,
    )
    _write_csv(args.out_details, details)
    _write_csv(args.out_summary, [summary])
    _write_md(args.out_md, details, summary)
    print(f"candidate_details={len(details)}")
    print(f"extension_state={summary['extension_state']}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
