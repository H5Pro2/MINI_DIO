from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _classify(row: dict[str, str]) -> str:
    occurrences = int(_float(row.get("occurrences")))
    hearing_delta = _float(row.get("hearing_delta_hit_minus_pre"))
    tension_delta = _float(row.get("tension_delta_hit_minus_pre"))
    range_delta = _float(row.get("range_delta_hit_minus_pre"))

    if occurrences < 10:
        return "zu_duenn"
    if hearing_delta < 0.0 and tension_delta < 0.0:
        return "oeffnung_getragen"
    if hearing_delta > 0.0 and tension_delta > 0.0:
        if range_delta > 0.0:
            return "bruch_mit_range_aufweitung"
        return "bruch_mit_lastanstieg"
    if hearing_delta > 0.0 or tension_delta > 0.0:
        return "teilbruch"
    return "unklar"


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "family",
        "occurrences",
        "hearing_delta",
        "tension_delta",
        "range_delta",
        "break_class",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def _write_md(path: Path, rows: list[dict[str, object]], source: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    title_prefix = path.stem.split("_", 1)[0]
    is_pair_report = "ZWEIERKOPPLUNG" in path.stem.upper() or "PAIR_" in str(source).upper()
    report_name = (
        "Synthetische Zweierkopplungs-Bruchklassen der Oeffnungs-Vorform"
        if is_pair_report
        else "Synthetische Bruchklassen der Oeffnungs-Vorform"
    )
    title = (
        f"# {title_prefix} - {report_name}"
        if title_prefix.isdigit()
        else f"# {report_name}"
    )
    families = sorted({str(row.get("family", "")) for row in rows if row.get("family")})
    family_label = ", ".join(families) if families else "Ziel-Familie"
    visible_rows = [row for row in rows if int(row.get("occurrences", 0) or 0) >= 10]
    carried = [row for row in visible_rows if row.get("break_class") == "oeffnung_getragen"]
    broken = [
        row
        for row in visible_rows
        if str(row.get("break_class", "")).startswith("bruch") or row.get("break_class") == "teilbruch"
    ]
    lines: list[str] = []
    lines.append(title)
    lines.append("")
    lines.append(f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    if is_pair_report:
        lines.append(
            "Diese Diagnose klassifiziert, welche synthetischen Zweierkopplungen die reale "
            "Oeffnungs-Vorform tragen oder brechen."
        )
    else:
        lines.append(
            "Diese Diagnose klassifiziert, welche synthetischen Stoerformen die reale Oeffnungs-Vorform brechen."
        )
    lines.append("Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.")
    lines.append("")
    lines.append("## Hierarchie")
    lines.append("")
    if is_pair_report:
        lines.append("1. Grundfrage: Welche Zweierkopplung bricht die Oeffnungs-Vorform?")
        lines.append("2. Unterpruefung: Range+Hoeren, Range+Spannung und Hoeren+Spannung getrennt lesen.")
        lines.append("3. Folgeschritt: Gegen Einzelachsen und volle Dreierlast verdichten.")
    else:
        lines.append("1. Grundfrage: Welche Stoerform bricht die Oeffnungs-Vorform?")
        lines.append("2. Unterpruefung: Hoer-, Spannungs- und Range-Delta je Welt/Familie lesen.")
        lines.append("3. Folgeschritt: Bruchklassen gegen weitere synthetische Varianten halten.")
    lines.append("")
    lines.append("## Klassifikation")
    lines.append("")
    lines.append("| Welt | Familie | Vorkommen | Delta Hoeren | Delta Spannung | Delta Range | Klasse |")
    lines.append("|---|---|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["family"]),
                    str(row["occurrences"]),
                    _fmt(row["hearing_delta"]),
                    _fmt(row["tension_delta"]),
                    _fmt(row["range_delta"]),
                    str(row["break_class"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Lesung")
    lines.append("")
    if carried and not broken:
        lines.append(
            f"In dieser Pruefung bleibt `{family_label}` dort sichtbar, wo die Achsenkopplung eine "
            "Entlastungsbewegung traegt: Hoeren und Spannung fallen im Zielzeichen. "
            "Die reine Einzelachsen-Stoerung reicht hier nicht aus, um die Form zu brechen."
        )
    elif broken and not carried:
        lines.append(
            f"`{family_label}` bleibt sichtbar, aber die Entlastungsrichtung kippt: Hoeren oder Spannung "
            "steigen im Zielzeichen. Das spricht fuer eine struktursensitive Bruchform."
        )
    elif carried and broken:
        lines.append(
            f"`{family_label}` zeigt gemischte Reaktion: einige Welten tragen die Entlastung, andere brechen sie. "
            "Damit ist die Form achsensensitiv und muss je Stoerklasse getrennt gelesen werden."
        )
    else:
        lines.append(
            f"`{family_label}` ist in dieser Pruefung zu selten sichtbar. Die Achsenwirkung bleibt deshalb offen."
        )
    lines.append("")
    lines.append("## Grenze")
    lines.append("")
    lines.append("```text")
    lines.append("Bruchklasse = passive Felddiagnose")
    lines.append("keine Handlungsregel")
    lines.append("keine Aussage ueber Absicht")
    lines.append("```")
    lines.append("")
    lines.append("## Quelle")
    lines.append("")
    lines.append(f"- `{source.as_posix()}`")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    if is_pair_report:
        lines.append(
            "Als naechstes sollte die Zweierkopplung direkt gegen Einzelachsen und volle Dreierlast "
            f"verdichtet werden: welche Kopplungsqualitaet bricht `{family_label}` wirklich?"
        )
    else:
        lines.append(
            "Als naechstes sollte die Achsenisolation gegen weitere Weltfenster gehalten werden: "
            "bleibt die Form bei Einzelstoerung getragen, aber kippt bei gekoppelter Last?"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    source = Path(args.source)
    rows = []
    for row in _read(source):
        rows.append(
            {
                "world": row.get("world", ""),
                "family": row.get("family", ""),
                "occurrences": int(_float(row.get("occurrences"))),
                "hearing_delta": _float(row.get("hearing_delta_hit_minus_pre")),
                "tension_delta": _float(row.get("tension_delta_hit_minus_pre")),
                "range_delta": _float(row.get("range_delta_hit_minus_pre")),
                "break_class": _classify(row),
            }
        )

    out_md = Path(args.out_md)
    out_csv = out_md.with_suffix(".csv")
    _write_csv(out_csv, rows)
    _write_md(out_md, rows, source)
    print({"out_md": str(out_md.resolve()), "out_csv": str(out_csv.resolve()), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
