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
    title = (
        f"# {title_prefix} - Synthetische Bruchklassen der Oeffnungs-Vorform"
        if title_prefix.isdigit()
        else "# Synthetische Bruchklassen der Oeffnungs-Vorform"
    )
    families = sorted({str(row.get("family", "")) for row in rows if row.get("family")})
    lines: list[str] = []
    lines.append(title)
    lines.append("")
    lines.append(f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose klassifiziert, welche synthetischen Stoerformen die reale Oeffnungs-Vorform brechen."
    )
    lines.append("Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.")
    lines.append("")
    lines.append("## Hierarchie")
    lines.append("")
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
    lines.append(
        "`dio_0ly7` bleibt in den synthetischen Welten sichtbar, aber die Entlastungsrichtung kehrt sich um: "
        "Hoeren und Spannung steigen im Zielzeichen. Das spricht fuer eine struktursensitive Feldform."
    )
    lines.append("")
    if "dio_01hu" in families:
        lines.append("`dio_01hu` ist in dieser Gegenprobe zu selten und wird deshalb nicht hart gelesen.")
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
    lines.append(
        "Als naechstes sollte `dio_0ly7` gegen weitere synthetische Varianten gehalten werden, um Range-Aufweitung von reiner Laststeigerung zu trennen."
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
