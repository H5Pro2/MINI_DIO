from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUTS = [
    ("SOL", befunde_root(ROOT) / "1868_SOL_HARTKERN_WELTLAGENREAKTION.csv"),
    ("BTC", befunde_root(ROOT) / "1872B_BTC_HARTKERN_WELTLAGENREAKTION.csv"),
    ("DOGE", befunde_root(ROOT) / "1872D_DOGE_HARTKERN_WELTLAGENREAKTION.csv"),
    ("PAXG", befunde_root(ROOT) / "1876_PAXG_HARTKERN_FENSTER_TIMEFRAME_VERGLEICH.csv"),
    ("XRP", befunde_root(ROOT) / "1872X_XRP_HARTKERN_WELTLAGENREAKTION.csv"),
]

DEFAULT_OUT_CSV = befunde_root(ROOT) / "1878_WELTPASSUNG_METRIK.csv"
DEFAULT_OUT_MD = befunde_root(ROOT) / "1878_WELTPASSUNG_METRIK.md"


SHIFT_STATES = {
    "lokale_qualitaet_wird_kernnah",
    "lokale_qualitaet_wird_nachhallnah",
    "lokale_qualitaet_wird_nullnah",
    "lokale_qualitaet_driftet",
    "qualitaet_reproduziert",
}


def _resolve(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def _parse_input(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("input must be LABEL=path.csv")
    label, path = value.split("=", 1)
    return label.strip(), _resolve(path.strip())


def _read_detail_rows(label: str, path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("row_type") != "worldstate_core_detail":
                continue
            rows.append({**row, "source_label": label, "source_file": str(path.relative_to(ROOT))})
    return rows


def _dominant_fit(counts: Counter[str]) -> str:
    if not counts:
        return "weltpassung_unbestimmt"
    dominant, _ = counts.most_common(1)[0]
    return {
        "getragen": "kern_getragen",
        "geoeffnet": "kern_geoeffnet",
        "verschoben": "kern_verschoben",
        "ausgeblendet": "kern_ausgeblendet",
    }.get(dominant, "weltpassung_gemischt")


def _state_bucket(state: str) -> str:
    if state == "lokale_qualitaet_reproduziert":
        return "getragen"
    if state == "lokale_qualitaet_wird_offen":
        return "geoeffnet"
    if state == "fehlt_im_folgefenster":
        return "ausgeblendet"
    if state in SHIFT_STATES:
        return "verschoben"
    return "verschoben"


def build_metric_rows(inputs: list[tuple[str, Path]]) -> list[dict[str, object]]:
    detail_rows: list[dict[str, str]] = []
    for label, path in inputs:
        if path.exists():
            detail_rows.extend(_read_detail_rows(label, path))

    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in detail_rows:
        key = (row.get("asset", ""), row.get("condition", ""), row.get("source_label", ""))
        grouped.setdefault(key, []).append(row)

    metric_rows: list[dict[str, object]] = []
    for (asset, condition, source_label), rows in sorted(grouped.items()):
        buckets = Counter(_state_bucket(row.get("followup_state", "")) for row in rows)
        total = len(rows)
        carried = buckets["getragen"] / total if total else 0.0
        opened = buckets["geoeffnet"] / total if total else 0.0
        shifted = buckets["verschoben"] / total if total else 0.0
        hidden = buckets["ausgeblendet"] / total if total else 0.0
        # Passive diagnostic score: positive values mean the world keeps the hard core close;
        # negative values mean the world hides or dissolves the core.
        world_fit_score = carried + (shifted * 0.35) + (opened * 0.15) - (hidden * 0.65)
        metric_rows.append(
            {
                "row_type": "world_fit_metric",
                "asset": asset,
                "condition": condition,
                "source_label": source_label,
                "core_pairs": total,
                "carried_count": buckets["getragen"],
                "opened_count": buckets["geoeffnet"],
                "shifted_count": buckets["verschoben"],
                "hidden_count": buckets["ausgeblendet"],
                "carried_share": carried,
                "opened_share": opened,
                "shifted_share": shifted,
                "hidden_share": hidden,
                "world_fit_score": world_fit_score,
                "world_fit_reading": _dominant_fit(buckets),
            }
        )
    return metric_rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "row_type",
        "asset",
        "condition",
        "source_label",
        "core_pairs",
        "carried_count",
        "opened_count",
        "shifted_count",
        "hidden_count",
        "carried_share",
        "opened_share",
        "shifted_share",
        "hidden_share",
        "world_fit_score",
        "world_fit_reading",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.3f}"
    except (TypeError, ValueError):
        return str(value)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(rows, key=lambda row: float(row["world_fit_score"]), reverse=True)
    lines = [
        "# 1878 - Weltpassungs-Metrik",
        "",
        "Diese Diagnose liest, wie gut eine Weltlage den harten Kern der lokalen Reifegruppe trägt.",
        "Die Metrik ist passiv: Sie erzeugt keine Handlung, kein Gate und keine Richtung.",
        "",
        "## Zustände",
        "",
        "- `getragen`: dieselbe lokale Qualität wird reproduziert.",
        "- `geöffnet`: der Kern bleibt sichtbar, verliert aber Schärfe.",
        "- `verschoben`: der Kern bleibt anschlussfähig, wechselt aber in Kernnähe, Nachhall, Nullnähe oder Drift.",
        "- `ausgeblendet`: das Kernpaar fehlt im Folgefenster.",
        "",
        "## Ergebnis",
        "",
        "| Asset | Weltlage | Kernpaare | getragen | geöffnet | verschoben | ausgeblendet | Score | Lesung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in ordered:
        lines.append(
            "| {asset} | {condition} | {core_pairs} | {carried_share} | {opened_share} | {shifted_share} | {hidden_share} | {score} | `{reading}` |".format(
                asset=row["asset"],
                condition=row["condition"],
                core_pairs=row["core_pairs"],
                carried_share=_fmt(row["carried_share"]),
                opened_share=_fmt(row["opened_share"]),
                shifted_share=_fmt(row["shifted_share"]),
                hidden_share=_fmt(row["hidden_share"]),
                score=_fmt(row["world_fit_score"]),
                reading=row["world_fit_reading"],
            )
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.",
            "Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.",
            "",
            "Damit wird Reife als Beziehung lesbar:",
            "",
            "```text",
            "Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Weltpassung in die passive Feldrollen-Memory übernommen werden. Nicht als Steuerung, sondern als Erfahrungsqualität: welche Weltlagen tragen welchen Kern, und welche lösen Randdrift aus?",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build passive world-fit metrics for hard-core local maturity reports.")
    parser.add_argument("--input", action="append", type=_parse_input, default=None)
    parser.add_argument("--out-csv", default=str(DEFAULT_OUT_CSV.relative_to(ROOT)))
    parser.add_argument("--out-md", default=str(DEFAULT_OUT_MD.relative_to(ROOT)))
    args = parser.parse_args()

    inputs = args.input or DEFAULT_INPUTS
    rows = build_metric_rows(inputs)
    _write_csv(_resolve(args.out_csv), rows)
    _write_md(_resolve(args.out_md), rows)
    print({"rows": len(rows), "out_csv": args.out_csv, "out_md": args.out_md})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
