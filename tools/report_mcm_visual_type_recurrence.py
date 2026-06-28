from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
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


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _counter_text(counter: Counter[str], limit: int = 10) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _visual_form(row: dict[str, str]) -> str:
    typology = row.get("typology", "") or row.get("mode", "")
    chart_zone = row.get("chart_zone", "")
    movement = row.get("dominant_movement", "")
    ret = _float(row, "main_return_pct")
    rng = _float(row, "main_range_pct")
    before = _float(row, "before_return_pct")

    if typology == "getragene_expansion":
        return "weite_aufwaerts_expansion"
    if typology == "rekopplung_nach_abverkauf":
        return "erholung_nach_vorlast"
    if typology == "abverkauf_mit_rekopplung":
        return "fallende_rueckbindung"
    if typology == "abverkauf_mit_bruch":
        return "fallender_strukturbruch"
    if typology == "gerichtete_bewegung_mit_rekopplung":
        return "ruhige_gerichtete_rekopplung"
    if typology == "gerichtete_bewegung_mit_bruch" and ret < 0:
        return "offenes_bullfenster_mit_bruch"
    if typology == "gerichtete_bewegung_mit_bruch" and rng <= 8:
        return "schmale_offene_transition"
    if typology == "gerichtete_bewegung_mit_bruch":
        return "gemischte_achsenbewegung"
    if "rekopplung" in movement and ret < 0:
        return "fallende_rueckbindung"
    if "rekopplung" in movement:
        return "ruhige_gerichtete_rekopplung"
    if ret > 0 and rng >= 30:
        return "weite_aufwaerts_expansion" if before >= 0 else "erholung_nach_vorlast"
    if ret < 0 and "bruch" in movement:
        return "fallender_strukturbruch"
    if "offen" in chart_zone or rng <= 8:
        return "schmale_offene_transition"
    return "nicht_eindeutig"


def _field_quality(row: dict[str, str]) -> str:
    pressure = _float(row, "pressure_delta_abs_avg")
    rekopplung = _float(row, "rekopplung_delta_abs_avg")
    rng = _float(row, "main_range_pct")
    movement = row.get("dominant_movement", "")

    if pressure >= 0.09 and rng >= 80:
        return "hochlastige_weite_rekopplung"
    if pressure >= 0.07 and rng >= 35:
        return "druckgetragene_weite"
    if rekopplung >= 0.023:
        return "starke_rekopplungsbindung"
    if pressure <= 0.055 and "rekopplung" in movement:
        return "ruhige_rekopplung"
    if rng <= 8:
        return "schmale_offene_lage"
    return "mittlere_feldspannung"


def _load_probe_rows(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in paths:
        for row in _read_rows(path):
            enriched = dict(row)
            enriched["source_file"] = path.name
            rows.append(enriched)
    return rows


def _build_recurrence(
    reference_rows: list[dict[str, str]],
    probe_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    reference_forms = {row.get("visual_form", "") for row in reference_rows}
    details: list[dict[str, object]] = []
    for row in probe_rows:
        form = _visual_form(row)
        if form not in reference_forms:
            continue
        details.append(
            {
                "visual_form": form,
                "field_quality": _field_quality(row),
                "source_file": row.get("source_file", "-"),
                "world": row.get("world", "-"),
                "pair": row.get("pair", "-"),
                "typology": row.get("typology", "-"),
                "chart_zone": row.get("chart_zone", "-"),
                "dominant_movement": row.get("dominant_movement", "-"),
                "return_pct": _float(row, "main_return_pct"),
                "range_pct": _float(row, "main_range_pct"),
                "before_return_pct": _float(row, "before_return_pct"),
                "after_return_pct": _float(row, "after_return_pct"),
                "pressure_abs": _float(row, "pressure_delta_abs_avg"),
                "rekopplung_abs": _float(row, "rekopplung_delta_abs_avg"),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )

    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in details:
        groups[str(row["visual_form"])].append(row)

    summary: list[dict[str, object]] = []
    for form in sorted(reference_forms):
        items = groups.get(form, [])
        summary.append(
            {
                "visual_form": form,
                "recurrence_count": len(items),
                "worlds": _counter_text(Counter(str(item["world"]) for item in items)),
                "typologies": _counter_text(Counter(str(item["typology"]) for item in items)),
                "field_qualities": _counter_text(Counter(str(item["field_quality"]) for item in items)),
                "avg_return_pct": round(_mean([float(item["return_pct"]) for item in items]), 6),
                "avg_range_pct": round(_mean([float(item["range_pct"]) for item in items]), 6),
                "avg_pressure_abs": round(_mean([float(item["pressure_abs"]) for item in items]), 6),
                "avg_rekopplung_abs": round(_mean([float(item["rekopplung_abs"]) for item in items]), 6),
            }
        )
    return details, summary


def _write_md(path: Path, details: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    lines = [
        "# 1025 - Wiederkehr visueller Bedeutungsformen",
        "",
        "Passive Pruefung, ob die visuellen Typen aus 1024 in weiteren Detailwelten wiederkehren.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Wiederkehrpruefung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine Bedeutungsfixierung",
        "",
        "## Zusammenfassung",
        "",
        "| Visuelle Form | Wiederkehr | Welten | Typologien | Feldqualitaeten | Return % | Range % | Druck | Rekopplung |",
        "|---|---:|---|---|---|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| `{row['visual_form']}` | {row['recurrence_count']} | `{row['worlds']}` | "
            f"`{row['typologies']}` | `{row['field_qualities']}` | {row['avg_return_pct']} | "
            f"{row['avg_range_pct']} | {row['avg_pressure_abs']} | {row['avg_rekopplung_abs']} |"
        )

    lines.extend(["", "## Detailbelege", ""])
    lines.append(
        "| Visuelle Form | Welt | Paar | Typologie | Chartzone | Bewegung | Return % | Range % | Druck | Rekopplung |"
    )
    lines.append("|---|---|---|---|---|---|---:|---:|---:|---:|")
    for row in details:
        lines.append(
            f"| `{row['visual_form']}` | `{row['world']}` | `{row['pair']}` | `{row['typology']}` | "
            f"`{row['chart_zone']}` | `{row['dominant_movement']}` | {row['return_pct']} | "
            f"{row['range_pct']} | {row['pressure_abs']} | {row['rekopplung_abs']} |"
        )

    recurrent = [row for row in summary if int(row["recurrence_count"]) > 0]
    absent = [row for row in summary if int(row["recurrence_count"]) == 0]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Wiederkehrende visuelle Formen: {len(recurrent)}",
            f"- In dieser Gegenlesung nicht wiedergefunden: {len(absent)}",
            "",
            "Wiederkehr bedeutet hier nicht starre Kopie, sondern erneute Lesbarkeit einer Bild-/Feldform",
            "in anderen Weltfenstern oder Quellen.",
            "",
            "## Schluss",
            "",
            "Wenn eine visuelle Form ueber mehrere Quellen wiederkehrt, wird sie als passive Bedeutungsgrundlage staerker.",
            "Wenn sie nicht wiederkehrt, bleibt sie eine lokale oder situationsgebundene Form.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die wiederkehrende Gruppe nach Stabilitaet sortiert werden: welche Formen sind robust, welche nur situationsbedingt?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True, type=Path)
    parser.add_argument("--probe-detail", action="append", required=True, type=Path)
    parser.add_argument("--out-details", required=True, type=Path)
    parser.add_argument("--out-summary", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    details, summary = _build_recurrence(
        _read_rows(args.reference),
        _load_probe_rows(args.probe_detail),
    )
    _write_csv(args.out_details, details)
    _write_csv(args.out_summary, summary)
    _write_md(args.out_md, details, summary)
    print(f"details={len(details)}")
    print(f"summary={len(summary)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
