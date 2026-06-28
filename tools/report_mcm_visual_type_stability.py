from __future__ import annotations

import argparse
import csv
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


def _safe_int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _safe_float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _count_parts(value: str) -> int:
    value = str(value or "").strip()
    if not value or value == "-":
        return 0
    return len([part for part in value.split("|") if part.strip()])


def _classify(row: dict[str, str]) -> tuple[str, str]:
    count = _safe_int(row.get("recurrence_count", "0"))
    world_variety = _count_parts(row.get("worlds", ""))
    typology_variety = _count_parts(row.get("typologies", ""))
    field_variety = _count_parts(row.get("field_qualities", ""))
    avg_range = _safe_float(row.get("avg_range_pct", "0"))

    if count >= 9 and world_variety >= 6:
        return (
            "robuste_bedeutungsform",
            "breite Wiederkehr ueber mehrere Welten; als passive Bedeutungsgrundlage stark.",
        )
    if count >= 4 and world_variety >= 2 and typology_variety <= 2:
        return (
            "familiengebundene_bedeutungsform",
            "wiederkehrend, aber staerker an eine bestimmte Typfamilie gebunden.",
        )
    if count >= 4 and field_variety >= 3:
        return (
            "variable_bedeutungsform",
            "wiederkehrend, aber mit wechselnder Feldqualitaet; eher offen als stabil fixiert.",
        )
    if count <= 2 and avg_range >= 30:
        return (
            "situativer_hochspannungszustand",
            "wenige Belege, aber grosse Weltbewegung; derzeit situationsgebunden.",
        )
    if count <= 2:
        return (
            "lokale_situationsform",
            "wenige Belege; noch keine robuste Bedeutungsgrundlage.",
        )
    return (
        "mittlere_stabilitaet",
        "mehrfach sichtbar, aber noch nicht breit genug fuer robuste Einordnung.",
    )


def _build(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for row in rows:
        stability, note = _classify(row)
        result.append(
            {
                "visual_form": row.get("visual_form", "-"),
                "stability_class": stability,
                "recurrence_count": _safe_int(row.get("recurrence_count", "0")),
                "world_variety": _count_parts(row.get("worlds", "")),
                "typology_variety": _count_parts(row.get("typologies", "")),
                "field_quality_variety": _count_parts(row.get("field_qualities", "")),
                "worlds": row.get("worlds", "-"),
                "typologies": row.get("typologies", "-"),
                "field_qualities": row.get("field_qualities", "-"),
                "avg_return_pct": _safe_float(row.get("avg_return_pct", "0")),
                "avg_range_pct": _safe_float(row.get("avg_range_pct", "0")),
                "avg_pressure_abs": _safe_float(row.get("avg_pressure_abs", "0")),
                "avg_rekopplung_abs": _safe_float(row.get("avg_rekopplung_abs", "0")),
                "stability_note": note,
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )
    result.sort(
        key=lambda row: (
            str(row["stability_class"]) != "robuste_bedeutungsform",
            -int(row["recurrence_count"]),
            str(row["visual_form"]),
        )
    )
    return result


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# 1026 - Stabilitaet visueller Bedeutungsformen",
        "",
        "Passive Stabilitaetssortierung der in 1025 wiedergefundenen visuellen Bedeutungsformen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Stabilitaetsdiagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- keine starre Bedeutungsfixierung",
        "",
        "## Stabilitaetsmatrix",
        "",
        "| Visuelle Form | Klasse | Wiederkehr | Weltstreuung | Typstreuung | Feldstreuung | Return % | Range % | Druck | Rekopplung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['visual_form']}` | `{row['stability_class']}` | {row['recurrence_count']} | "
            f"{row['world_variety']} | {row['typology_variety']} | {row['field_quality_variety']} | "
            f"{row['avg_return_pct']} | {row['avg_range_pct']} | {row['avg_pressure_abs']} | {row['avg_rekopplung_abs']} |"
        )

    lines.extend(["", "## Lesung", ""])
    for row in rows:
        lines.extend(
            [
                f"### `{row['visual_form']}`",
                "",
                f"- Klasse: `{row['stability_class']}`",
                f"- Wiederkehr: `{row['recurrence_count']}`",
                f"- Welten: `{row['worlds']}`",
                f"- Typologien: `{row['typologies']}`",
                f"- Feldqualitaeten: `{row['field_qualities']}`",
                f"- Einordnung: {row['stability_note']}",
                "",
            ]
        )

    robust = [row for row in rows if row["stability_class"] == "robuste_bedeutungsform"]
    family = [row for row in rows if row["stability_class"] == "familiengebundene_bedeutungsform"]
    local = [row for row in rows if str(row["stability_class"]).startswith("lokale") or "situativer" in str(row["stability_class"])]
    lines.extend(
        [
            "## Befund",
            "",
            f"- Robuste Bedeutungsformen: {len(robust)}",
            f"- Familiengebundene Bedeutungsformen: {len(family)}",
            f"- Lokale oder situationsgebundene Formen: {len(local)}",
            "",
            "Robust heisst hier nicht endgueltig oder handlungsleitend.",
            "Es bedeutet: Die Form wiederholt sich breit genug, um als passive Bedeutungsgrundlage weiter untersucht zu werden.",
            "",
            "## Schluss",
            "",
            "Mini-DIO bildet innerhalb der MCM-Achse keine beliebige Sammlung einzelner Fenster,",
            "sondern eine gestufte Bedeutungsordnung: robuste Formen, familiengebundene Formen und lokale Zustandsformen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus den robusten Formen eine passive Bedeutungsbibliothek entstehen: Name, Weltform, Feldqualitaet, typische Streuung und offene Grenzen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read_rows(args.summary))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"stability_rows={len(rows)}")
    print(f"wrote {args.out_md}")


if __name__ == "__main__":
    main()
