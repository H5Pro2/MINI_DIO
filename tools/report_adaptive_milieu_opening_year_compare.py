from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _by_family(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("family", "-"): row for row in rows}


def _compare(label_a: str, rows_a: list[dict[str, str]], label_b: str, rows_b: list[dict[str, str]]) -> list[dict[str, object]]:
    a = _by_family(rows_a)
    b = _by_family(rows_b)
    out: list[dict[str, object]] = []
    for family in sorted(set(a) | set(b)):
        row_a = a.get(family, {})
        row_b = b.get(family, {})
        out.append(
            {
                "family": family,
                f"occurrences_{label_a}": row_a.get("occurrences", "0"),
                f"occurrences_{label_b}": row_b.get("occurrences", "0"),
                f"hearing_delta_{label_a}": row_a.get("hearing_delta", "0"),
                f"hearing_delta_{label_b}": row_b.get("hearing_delta", "0"),
                "hearing_delta_diff": _float(row_b.get("hearing_delta")) - _float(row_a.get("hearing_delta")),
                f"tension_delta_{label_a}": row_a.get("tension_delta", "0"),
                f"tension_delta_{label_b}": row_b.get("tension_delta", "0"),
                "tension_delta_diff": _float(row_b.get("tension_delta")) - _float(row_a.get("tension_delta")),
                f"world_hits_{label_a}": row_a.get("world_hits", "0"),
                f"world_hits_{label_b}": row_b.get("world_hits", "0"),
            }
        )
    return out


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(value, 6) if isinstance(value, float) else value for key, value in row.items()})


def _write_md(rows: list[dict[str, object]], out_path: Path, label_a: str, label_b: str) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Jahresvergleich Oeffnungs-Vorform" if title_prefix.isdigit() else "# Jahresvergleich Oeffnungs-Vorform"
    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht die Oeffnungs-Vorform zwischen zwei Jahren.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Traegt die Entlastungsform jahresuebergreifend?",
        "2. Unterpruefung: Delta Hoeren und Delta Spannung fuer `dio_0ly7` und `dio_01hu` vergleichen.",
        "3. Folgeschritt: Gegen 2023 und synthetische Kontrollwelten halten.",
        "",
        "## Vergleich",
        "",
        f"| Familie | Vorkommen {label_a} | Vorkommen {label_b} | Delta Hoeren {label_a} | Delta Hoeren {label_b} | Diff Hoeren | Delta Spannung {label_a} | Delta Spannung {label_b} | Diff Spannung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row.get(f"occurrences_{label_a}", "0")),
                    str(row.get(f"occurrences_{label_b}", "0")),
                    str(row.get(f"hearing_delta_{label_a}", "0")),
                    str(row.get(f"hearing_delta_{label_b}", "0")),
                    _fmt(float(row["hearing_delta_diff"])),
                    str(row.get(f"tension_delta_{label_a}", "0")),
                    str(row.get(f"tension_delta_{label_b}", "0")),
                    _fmt(float(row["tension_delta_diff"])),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn beide Jahre negative Hoer- und Spannungsdeltas halten, ist die Entlastungsform jahresuebergreifend sichtbar.",
            "",
            "Die Differenzen zeigen nicht, ob eine Familie `besser` ist. Sie zeigen nur, ob die Arbeitsform stabil, schwach driftend oder gebrochen wirkt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Vorform gegen 2023 oder synthetische Kontrollwelten gelesen werden.",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleicht Oeffnungs-Vorform ueber zwei Jahre.")
    parser.add_argument("--a-label", required=True)
    parser.add_argument("--a-summary", required=True)
    parser.add_argument("--b-label", required=True)
    parser.add_argument("--b-summary", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()
    rows = _compare(args.a_label, _load_csv(_resolve(args.a_summary)), args.b_label, _load_csv(_resolve(args.b_summary)))
    _write_md(rows, _resolve(args.out_md), args.a_label, args.b_label)
    print({"out_md": str(_resolve(args.out_md)), "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
