from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_worldlage_multiscale_asset_distribution import _asset_from_world, _summarize, _write_csv


def _write_markdown(rows: list[dict[str, object]], *, sample_size: int, scale_quota: dict[str, int], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Balancierte Zwischenlagen - Assetvergleich",
        "",
        "Diese Diagnose liest skalenabhaengige Zwischenlagen mit gleicher Fensterzahl pro realem Asset.",
        "",
        f"Sample pro Asset: `{sample_size}` Fenster.",
        "",
        "Skalenquote:",
        "",
        *[f"- Block `{scale}`: `{count}` Fenster pro Asset" for scale, count in sorted(scale_quota.items())],
        "",
        "Synthetische Welten werden hier nicht in die Balance einbezogen.",
        "",
        "## Assetvergleich",
        "",
        "| Asset | Fenster | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck | Range |",
        "|---|---:|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        if str(row["group_type"]) != "asset":
            continue
        lines.append(
            "| {group} | {count} | {dominant_raw_class} | {dominant_sequence} | {scale_counts} | {avg_auditory:.4f} | {avg_visual_sharpness:.4f} | {avg_field_pressure:.4f} | {avg_range_pct:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die balancierte Lesung nimmt SOL die Mengen-Dominanz.",
            "",
            "Wenn die Zwischenlagen danach weiter aehnliche Rohklassen und Sinneswerte tragen, spricht das fuer eine gemeinsame MCM-Feldform mit Assetfaerbung.",
            "",
            "Wenn einzelne Assets stark abweichen, ist die Zwischenlage eher weltgebunden.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _balanced_rows(source_rows: list[dict[str, str]], sample_size: int | None) -> tuple[list[dict[str, str]], int, dict[str, int]]:
    groups: dict[str, list[dict[str, str]]] = {}
    for row in source_rows:
        asset = _asset_from_world(str(row.get("world", "")))
        if asset in {"SYNTH", "UNKNOWN"}:
            continue
        groups.setdefault(asset, []).append(row)
    if not groups:
        raise RuntimeError("no real asset groups found")
    scale_quota: dict[str, int] = {}
    scales = sorted({str(row.get("scale", "")) for group in groups.values() for row in group})
    for scale in scales:
        scale_quota[scale] = min(sum(1 for row in group if str(row.get("scale", "")) == scale) for group in groups.values())
    if sample_size:
        # Keep deterministic ordering while shrinking the natural per-scale quota.
        remaining = int(sample_size)
        reduced: dict[str, int] = {}
        for scale in scales:
            if remaining <= 0:
                reduced[scale] = 0
                continue
            take = min(scale_quota[scale], remaining)
            reduced[scale] = take
            remaining -= take
        scale_quota = reduced
    size = sum(scale_quota.values())
    out: list[dict[str, str]] = []
    for asset in sorted(groups):
        for scale in scales:
            quota = scale_quota.get(scale, 0)
            if quota <= 0:
                continue
            group = sorted(
                [row for row in groups[asset] if str(row.get("scale", "")) == scale],
                key=lambda row: (
                    str(row.get("world", "")),
                    int(float(row.get("block_index", 0) or 0)),
                    str(row.get("base_sequence", "")),
                ),
            )
            out.extend(group[:quota])
    return out, size, scale_quota


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1001-2000/1001-1500/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER.csv")
    parser.add_argument("--sample-size", type=int, default=0)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    args = parser.parse_args()

    with Path(args.input).open("r", encoding="utf-8", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    balanced, size, scale_quota = _balanced_rows(source_rows, args.sample_size if args.sample_size > 0 else None)
    rows = _summarize(balanced, "asset")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, sample_size=size, scale_quota=scale_quota, path=Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
