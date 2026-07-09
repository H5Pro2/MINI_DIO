from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METRIC_KEYS = [
    "avg_tension",
    "avg_rekopplung",
    "avg_strain",
    "avg_raw_intake",
    "avg_adapted_intake",
]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _key(row: dict[str, str]) -> tuple[str, str]:
    return str(row.get("pattern") or "-"), str(row.get("phase") or "-")


def _index(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    return {_key(row): row for row in rows}


def _classify(left: dict[str, str], right: dict[str, str]) -> str:
    pattern = str(left.get("pattern") or right.get("pattern") or "-")
    phase = str(left.get("phase") or right.get("phase") or "-")
    left_field = str(left.get("field") or "-")
    right_field = str(right.get("field") or "-")
    tension_delta = _float(right.get("avg_tension")) - _float(left.get("avg_tension"))
    rekopplung_delta = _float(right.get("avg_rekopplung")) - _float(left.get("avg_rekopplung"))
    strain_delta = _float(right.get("avg_strain")) - _float(left.get("avg_strain"))
    tone_left = str(left.get("tone") or "-")
    tone_right = str(right.get("tone") or "-")

    if pattern == "tragende_verarbeitung" and phase == "nachlauf" and right_field == "rekoppelt" and left_field != "rekoppelt":
        return "rechts_haelt_rekopplung_laenger"
    if pattern == "tragende_verarbeitung" and phase == "ereignis" and tension_delta > 0.015 and rekopplung_delta < 0.0:
        return "links_rekoppelt_spitzer"
    if pattern == "kippnaehe" and strain_delta > 0.0 and rekopplung_delta < 0.0:
        return "rechts_traegt_mehr_offene_last"
    if tone_left != tone_right:
        return "unterschiedliche_hoerbindung"
    if abs(tension_delta) < 0.01 and abs(rekopplung_delta) < 0.01 and abs(strain_delta) < 0.01:
        return "nahe_feldlage"
    return "gemischter_unterschied"


def _write_md(
    path: Path,
    left_family: str,
    right_family: str,
    left_source: str,
    right_source: str,
    rows: list[dict[str, object]],
) -> None:
    lines = [
        f"# 1806 - `{left_family}` gegen `{right_family}`",
        "",
        "## Grundfrage",
        "",
        "Diese Prüfung legt zwei Feldfolgen-Signaturen direkt nebeneinander.",
        "",
        "Ziel ist eine passive Trennung: Brückenträger, Anschlussknoten oder nur gleiche Oberfläche?",
        "",
        "## Quellen",
        "",
        f"- `{left_source}`",
        f"- `{right_source}`",
        "",
        "## Vergleich",
        "",
        "| Muster | Phase | Feld links | Feld rechts | Spannung Δ | Rekopplung Δ | Strain Δ | Lesung |",
        "|---|---|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['pattern']}` | `{row['phase']}` | `{row['left_field']}` | `{row['right_field']}` | "
            f"{row['delta_avg_tension']} | {row['delta_avg_rekopplung']} | {row['delta_avg_strain']} | "
            f"`{row['comparison_reading']}` |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{left_family}` und `{right_family}` teilen die gleiche Grundbewegung: offene Vorphase, tragendes Ereignis und getrennte Kippnähe.",
            "",
            f"Der Unterschied liegt in der Feldfolge. `{left_family}` rekoppelt im Ereignis spitzer und fällt danach wieder offener in Nachprüfung. `{right_family}` hält Rekopplung im Nachlauf stärker und bleibt stärker an Hören mit Wechsel gebunden.",
            "",
            "Damit wirkt die Trennung vorläufig so:",
            "",
            f"- `{left_family}`: stärkerer Brückenträger.",
            f"- `{right_family}`: stärkerer Anschluss-/Kohärenzknoten.",
            "",
            "Das ist kein Beweis für feste Bedeutungen. Die Bedeutung entsteht weiter aus Familie, Weltfenster, Feldfolge und Nachbarschaft.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese Rollen in weiteren Kernfamilien ebenfalls paarweise auftreten: Brückenträger, Anschlussknoten, Randknoten und breite Sammelfamilien.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", default="reports/dio_0l7p_bridge_tick_window_signature.csv")
    parser.add_argument("--right", default="reports/dio_104t_bridge_tick_window_signature.csv")
    parser.add_argument("--left-family", default="dio_0l7p")
    parser.add_argument("--right-family", default="dio_104t")
    parser.add_argument("--out-csv", default="reports/dio_0l7p_vs_dio_104t_signature_compare.csv")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1806_DIO_0L7P_GEGEN_DIO_104T.md")
    args = parser.parse_args()

    left_rows = _index(_read_csv(ROOT / args.left))
    right_rows = _index(_read_csv(ROOT / args.right))
    out_rows: list[dict[str, object]] = []
    for key in sorted(set(left_rows) | set(right_rows)):
        left = left_rows.get(key, {})
        right = right_rows.get(key, {})
        row: dict[str, object] = {
            "left_family": args.left_family,
            "right_family": args.right_family,
            "pattern": key[0],
            "phase": key[1],
            "left_rows": left.get("rows", 0),
            "right_rows": right.get("rows", 0),
            "left_visual": left.get("visual", "-"),
            "right_visual": right.get("visual", "-"),
            "left_tone": left.get("tone", "-"),
            "right_tone": right.get("tone", "-"),
            "left_field": left.get("field", "-"),
            "right_field": right.get("field", "-"),
        }
        for metric in METRIC_KEYS:
            row[f"left_{metric}"] = left.get(metric, 0)
            row[f"right_{metric}"] = right.get(metric, 0)
            row[f"delta_{metric}"] = round(_float(right.get(metric)) - _float(left.get(metric)), 6)
        row["comparison_reading"] = _classify(left, right)
        out_rows.append(row)

    _write_csv(ROOT / args.out_csv, out_rows)
    _write_md(ROOT / args.out_md, args.left_family, args.right_family, args.left, args.right, out_rows)
    print({"rows": len(out_rows), "out": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
