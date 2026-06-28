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


def _parse_counter_text(value: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for part in str(value or "").split("|"):
        item = part.strip()
        if not item or ":" not in item:
            continue
        key, raw_count = item.rsplit(":", 1)
        try:
            counter[key.strip()] += int(float(raw_count.strip()))
        except ValueError:
            counter[key.strip()] += 1
    return counter


def _counter_text(counter: Counter[str], limit: int = 8) -> str:
    if not counter:
        return "-"
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _overlap_text(left: Counter[str], right: Counter[str]) -> str:
    shared = sorted(set(left) & set(right))
    return " | ".join(shared) if shared else "-"


def _classify(
    library: dict[str, str],
    holdout: dict[str, str] | None,
    typology_overlap: str,
    field_overlap: str,
) -> tuple[str, str]:
    if holdout is None or int(float(holdout.get("recurrence_count", "0") or 0)) <= 0:
        return (
            "nicht_bestaetigt",
            "Die Bedeutung wurde in dieser Holdout-Gruppe nicht wiedergefunden und bleibt fuer diese Weltgruppe offen.",
        )

    form = library.get("visual_form", "")
    holdout_count = int(float(holdout.get("recurrence_count", "0") or 0))
    range_delta = _float(holdout, "avg_range_pct") - _float(library, "avg_range_pct")
    pressure_delta = _float(holdout, "avg_pressure_abs") - _float(library, "avg_pressure_abs")
    rekopplung_delta = _float(holdout, "avg_rekopplung_abs") - _float(library, "avg_rekopplung_abs")

    has_typology_overlap = typology_overlap != "-"
    has_field_overlap = field_overlap != "-"

    if not has_typology_overlap and not has_field_overlap:
        return (
            "wieder_geoeffnet",
            "Die Form kehrt auf Oberflaeche wieder, aber Typologie und Feldqualitaet loesen sich von der Bibliothek.",
        )

    if form == "schmale_offene_transition":
        return (
            "duenn_bestaetigt_offen",
            "Die schmale Transition kehrt zurueck, bleibt aber belegtduenn und offen; sie ist Anwesenheit, keine stabile Tiefe.",
        )

    if abs(range_delta) > 10.0 or abs(pressure_delta) > 0.015 or abs(rekopplung_delta) > 0.004:
        return (
            "bestaetigt_mit_erweiterung",
            "Die Bedeutung kehrt wieder, aber Range, Druck oder Rekopplung verschieben sich sichtbar gegen die Bibliothek.",
        )

    if holdout_count >= 3 and has_typology_overlap and has_field_overlap:
        return (
            "stabil_bestaetigt",
            "Die Bedeutung kehrt mit gemeinsamer Typologie und gemeinsamer Feldqualitaet wieder.",
        )

    return (
        "bestaetigt_offen",
        "Die Bedeutung kehrt wieder, bleibt in dieser Holdout-Gruppe aber noch offen oder schmal belegt.",
    )


def build_rows(
    library_rows: list[dict[str, str]],
    holdout_summary_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    holdout_by_form = {row.get("visual_form", ""): row for row in holdout_summary_rows}
    rows: list[dict[str, object]] = []
    for lib in library_rows:
        form = lib.get("visual_form", "")
        hold = holdout_by_form.get(form)
        lib_typologies = _parse_counter_text(lib.get("typical_typologies", ""))
        lib_fields = _parse_counter_text(lib.get("typical_field_qualities", ""))
        hold_typologies = _parse_counter_text(hold.get("typologies", "") if hold else "")
        hold_fields = _parse_counter_text(hold.get("field_qualities", "") if hold else "")
        typology_overlap = _overlap_text(lib_typologies, hold_typologies)
        field_overlap = _overlap_text(lib_fields, hold_fields)
        status, note = _classify(lib, hold, typology_overlap, field_overlap)
        rows.append(
            {
                "meaning_name": lib.get("meaning_name", ""),
                "visual_form": form,
                "stability_reading": status,
                "library_recurrence": int(float(lib.get("recurrence_count", "0") or 0)),
                "holdout_recurrence": int(float(hold.get("recurrence_count", "0") or 0)) if hold else 0,
                "library_world_variety": int(float(lib.get("world_variety", "0") or 0)),
                "holdout_worlds": hold.get("worlds", "-") if hold else "-",
                "typology_overlap": typology_overlap,
                "field_quality_overlap": field_overlap,
                "library_typologies": _counter_text(lib_typologies),
                "holdout_typologies": _counter_text(hold_typologies),
                "library_field_qualities": _counter_text(lib_fields),
                "holdout_field_qualities": _counter_text(hold_fields),
                "library_avg_return_pct": round(_float(lib, "avg_return_pct"), 6),
                "holdout_avg_return_pct": round(_float(hold, "avg_return_pct"), 6) if hold else 0.0,
                "return_delta": round((_float(hold, "avg_return_pct") if hold else 0.0) - _float(lib, "avg_return_pct"), 6),
                "library_avg_range_pct": round(_float(lib, "avg_range_pct"), 6),
                "holdout_avg_range_pct": round(_float(hold, "avg_range_pct"), 6) if hold else 0.0,
                "range_delta": round((_float(hold, "avg_range_pct") if hold else 0.0) - _float(lib, "avg_range_pct"), 6),
                "library_avg_pressure_abs": round(_float(lib, "avg_pressure_abs"), 6),
                "holdout_avg_pressure_abs": round(_float(hold, "avg_pressure_abs"), 6) if hold else 0.0,
                "pressure_delta": round((_float(hold, "avg_pressure_abs") if hold else 0.0) - _float(lib, "avg_pressure_abs"), 6),
                "library_avg_rekopplung_abs": round(_float(lib, "avg_rekopplung_abs"), 6),
                "holdout_avg_rekopplung_abs": round(_float(hold, "avg_rekopplung_abs"), 6) if hold else 0.0,
                "rekopplung_delta": round((_float(hold, "avg_rekopplung_abs") if hold else 0.0) - _float(lib, "avg_rekopplung_abs"), 6),
                "interpretation": note,
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    return rows


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    status_counts = Counter(str(row["stability_reading"]) for row in rows)
    lines = [
        "# 1030 - Stabilitaet der passiven Bedeutungsbibliothek im Holdout",
        "",
        "Passive Pruefung, welche Bedeutungsformen aus 1027 in der Holdout-Gruppe 1028/1029 stabil bleiben, sich erweitern oder offen werden.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Stabilitaetslesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine Richtungsvorgabe",
        "",
        "## Statusuebersicht",
        "",
    ]
    for key, value in status_counts.most_common():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Bedeutungen",
            "",
            "| Bedeutung | Form | Status | Bibliothek | Holdout | Typologie-Ueberlappung | Feld-Ueberlappung | Return Delta | Range Delta | Druck Delta | Rekopplung Delta |",
            "|---|---|---|---:|---:|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['meaning_name']}` | `{row['visual_form']}` | `{row['stability_reading']}` | "
            f"{row['library_recurrence']} | {row['holdout_recurrence']} | `{row['typology_overlap']}` | "
            f"`{row['field_quality_overlap']}` | {row['return_delta']} | {row['range_delta']} | "
            f"{row['pressure_delta']} | {row['rekopplung_delta']} |"
        )
    lines.extend(["", "## Einzeldeutung", ""])
    for row in rows:
        lines.extend(
            [
                f"### `{row['meaning_name']}`",
                "",
                f"- Form: `{row['visual_form']}`",
                f"- Status: `{row['stability_reading']}`",
                f"- Bibliothek: `{row['library_recurrence']}` Belege, Holdout: `{row['holdout_recurrence']}` Belege",
                f"- Typologie-Ueberlappung: `{row['typology_overlap']}`",
                f"- Feldqualitaet-Ueberlappung: `{row['field_quality_overlap']}`",
                f"- Deutung: {row['interpretation']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Befund",
            "",
            "Die passive Bedeutungsbibliothek wird in der Holdout-Gruppe nicht geschlossen kopiert, sondern unterschiedlich getragen:",
            "",
            "- stabile Bedeutungen bleiben mit Typologie- und Feldqualitaetsueberlappung lesbar,",
            "- erweiterte Bedeutungen zeigen dieselbe Grundform bei veraenderter Range, Druck- oder Rekopplungsqualitaet,",
            "- offene Bedeutungen bleiben schmal oder belegtduenn und duerfen nicht zu festen Bedeutungen erklaert werden.",
            "",
            "## Schluss",
            "",
            "Mini-DIOs passive Bedeutungsbibliothek wirkt damit nicht wie eine starre Liste, sondern wie ein offener Bedeutungsraum: wiedererkennbar, aber weltabhaengig dehnbar.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte eine weitere Holdout-Gruppe mit anderem Asset- oder Zeitprofil gegen dieselbe Bibliothek gelesen werden. Entscheidend ist, ob dieselben Bedeutungen erneut stabil, erweitert oder offen erscheinen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path, required=True)
    parser.add_argument("--holdout-summary", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    rows = build_rows(_read_rows(args.library), _read_rows(args.holdout_summary))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"stability_rows={len(rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
