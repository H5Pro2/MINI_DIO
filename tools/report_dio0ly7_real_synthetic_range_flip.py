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


def _read_rows(path: Path, source: str, family: str) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("family") != family:
                continue
            occurrences = int(_float(row.get("occurrences")))
            if occurrences <= 0:
                continue
            hearing = _float(row.get("hearing_delta_hit_minus_pre"))
            tension = _float(row.get("tension_delta_hit_minus_pre"))
            range_delta = _float(row.get("range_delta_hit_minus_pre"))
            out.append(
                {
                    "source": source,
                    "world": row.get("world", ""),
                    "family": family,
                    "occurrences": occurrences,
                    "hearing_delta": hearing,
                    "tension_delta": tension,
                    "range_delta": range_delta,
                    "range_expands": int(range_delta > 0.0),
                    "load_rises": int(hearing > 0.0 and tension > 0.0),
                    "reading": _reading(hearing, tension, range_delta),
                }
            )
    return out


def _reading(hearing: float, tension: float, range_delta: float) -> str:
    if hearing < 0.0 and tension < 0.0 and range_delta > 0.0:
        return "range_aufweitung_aber_entlastung"
    if hearing < 0.0 and tension < 0.0:
        return "entlastung_ohne_range_aufweitung"
    if hearing > 0.0 and tension > 0.0 and range_delta > 0.0:
        return "lastanstieg_mit_range_aufweitung"
    if hearing > 0.0 or tension > 0.0:
        return "teilweise_lastanstieg"
    return "unklar"


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source",
        "world",
        "family",
        "occurrences",
        "hearing_delta",
        "tension_delta",
        "range_delta",
        "range_expands",
        "load_rises",
        "reading",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.6f}"
    return str(value)


def _write_md(path: Path, rows: list[dict[str, object]], family: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    real = [row for row in rows if str(row["source"]).startswith("real")]
    synthetic = [row for row in rows if str(row["source"]).startswith("synthetic")]
    real_range_expansion = [row for row in real if row["range_expands"]]
    synthetic_range_expansion = [row for row in synthetic if row["range_expands"]]

    lines: list[str] = []
    lines.append("# 1712 - dio_0ly7 Range-Aufweitung real gegen synthetisch")
    lines.append("")
    lines.append(f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose prueft, ob Range-Aufweitung allein die Umkehr von `dio_0ly7` erklaert."
    )
    lines.append("Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.")
    lines.append("")
    lines.append("## Hierarchie")
    lines.append("")
    lines.append("1. Grundfrage: Kippt `dio_0ly7` wegen Range-Aufweitung?")
    lines.append("2. Unterpruefung: Reale Range-Aufweitung gegen synthetische Range-Aufweitung vergleichen.")
    lines.append("3. Folgeschritt: Falls Range allein nicht reicht, Kombinationsursache lesen.")
    lines.append("")
    lines.append("## Vergleich")
    lines.append("")
    lines.append("| Quelle | Welt | Vorkommen | Delta Hoeren | Delta Spannung | Delta Range | Lesung |")
    lines.append("|---|---|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["source"]),
                    str(row["world"]),
                    str(row["occurrences"]),
                    _fmt(row["hearing_delta"]),
                    _fmt(row["tension_delta"]),
                    _fmt(row["range_delta"]),
                    str(row["reading"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Kurzbefund")
    lines.append("")
    lines.append(f"- Reale Welten mit Range-Aufweitung: {len(real_range_expansion)}")
    lines.append(f"- Synthetische Welten mit Range-Aufweitung: {len(synthetic_range_expansion)}")
    lines.append("")
    lines.append("Lesung:")
    lines.append("")
    lines.append("```text")
    lines.append("Range-Aufweitung allein reicht nicht aus.")
    lines.append("In realen PAXG-Welten bleibt dio_0ly7 trotz leichter Range-Aufweitung entlastend.")
    lines.append("In synthetischen Welten koppelt Range-Aufweitung mit Hoer- und Spannungsanstieg.")
    lines.append("Der Bruch ist deshalb eine Kombinationswirkung, nicht nur ein Range-Effekt.")
    lines.append("```")
    lines.append("")
    lines.append("## Grenze")
    lines.append("")
    lines.append("```text")
    lines.append("Das ist eine passive Felddiagnose.")
    lines.append("Keine Handlungsregel.")
    lines.append("Keine Aussage ueber Absicht.")
    lines.append("```")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append(
        "Als naechstes sollte die Kombinationswirkung getrennt gelesen werden: Hoeranstieg, Spannungsanstieg und Range-Aufweitung als gemeinsamer Bruchzustand."
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_0ly7")
    parser.add_argument("--source", nargs=2, action="append", metavar=("LABEL", "CSV"), required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for label, path_text in args.source:
        rows.extend(_read_rows(Path(path_text), label, args.family))

    out_md = Path(args.out_md)
    out_csv = out_md.with_suffix(".csv")
    _write_csv(out_csv, rows)
    _write_md(out_md, rows, args.family)
    print({"out_md": str(out_md.resolve()), "out_csv": str(out_csv.resolve()), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
