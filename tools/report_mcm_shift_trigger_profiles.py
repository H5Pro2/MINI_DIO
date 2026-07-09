from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def _parse_shift(value: str) -> tuple[str, Path, Path]:
    parts = value.split("=", 2)
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("shift must be LABEL=SHIFT_CSV=BALANCED_CSV")
    return parts[0], Path(parts[1]), Path(parts[2])


def _read_by_asset(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {str(row.get("asset") or row.get("group")): row for row in csv.DictReader(handle)}


def _read_balanced_by_asset(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {
            str(row.get("group", "")): row
            for row in csv.DictReader(handle)
            if str(row.get("group_type", "")) == "asset"
        }


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["shift_label"])].append(row)

    lines = [
        "# MCM-Shift-Triggerprofile",
        "",
        "Diese Diagnose bindet wiederkehrende Bedeutungsfaerbungen an konkrete Rohwelt- und Sinnesprofile zurueck.",
        "",
        "Sie bleibt passiv: keine Handlung, keine Richtung, kein Gate.",
        "",
        "## Einzelprofile",
        "",
        "| Quelle | Asset | Shift | Folge | Rohklasse | dHoeren | dSicht | dDruck | dRange | Holdout-Hoeren | Holdout-Sicht | Holdout-Druck | Holdout-Range |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {source} | {asset} | `{shift_label}` | `{holdout_sequence}` | `{dominant_raw_class}` | {delta_auditory:.4f} | {delta_visual:.4f} | {delta_pressure:.4f} | {delta_range:.4f} | {holdout_auditory:.4f} | {holdout_visual:.4f} | {holdout_pressure:.4f} | {holdout_range:.4f} |".format(
                **row
            )
        )

    lines.extend(["", "## Verdichtete Shift-Typen", ""])
    lines.append("| Shift | Vorkommen | Assets | dHoeren | dSicht | dDruck | dRange | Holdout-Hoeren | Holdout-Sicht | Holdout-Druck | Holdout-Range |")
    lines.append("|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for shift, shift_rows in sorted(grouped.items()):
        assets = ",".join(sorted({str(row["asset"]) for row in shift_rows}))
        lines.append(
            "| {shift} | {count} | {assets} | {d_h:.4f} | {d_v:.4f} | {d_p:.4f} | {d_r:.4f} | {h_h:.4f} | {h_v:.4f} | {h_p:.4f} | {h_r:.4f} |".format(
                shift=f"`{shift}`",
                count=len(shift_rows),
                assets=assets,
                d_h=_avg([float(row["delta_auditory"]) for row in shift_rows]),
                d_v=_avg([float(row["delta_visual"]) for row in shift_rows]),
                d_p=_avg([float(row["delta_pressure"]) for row in shift_rows]),
                d_r=_avg([float(row["delta_range"]) for row in shift_rows]),
                h_h=_avg([float(row["holdout_auditory"]) for row in shift_rows]),
                h_v=_avg([float(row["holdout_visual"]) for row in shift_rows]),
                h_p=_avg([float(row["holdout_pressure"]) for row in shift_rows]),
                h_r=_avg([float(row["holdout_range"]) for row in shift_rows]),
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "`druck_entlasteter_normalisierungsshift` erscheint bisher als PAXG-nahe Normalisierung: Hoeren und Felddruck sinken gegenueber der Basis, waehrend die Folge auf `normale_weltspannung->normale_weltspannung` rueckbindet.",
            "",
            "`oberflaeche_veraendert` erscheint bisher als Oberflaechen-/Range-Verschiebung: die dominante Folge kann gleich bleiben, aber Range und teilweise Hoeren/Sicht veraendern die Faerbung.",
            "",
            "`hoerbarer_schmaler_folgeschift` bleibt ein einzelner starker BTC-Befund aus `1325`: Hoeren, Sicht und Druck steigen, Range sinkt deutlich. Dieser Typ ist noch nicht reproduziert.",
            "",
            "Wie es weitergeht: Als naechstes sollte gezielt eine Weltgruppe mit hoher Hoer-/Sichtzunahme und sinkender Range gebaut oder ausgewaehlt werden, um zu pruefen, ob `hoerbarer_schmaler_folgeschift` wiederholbar ist.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shift", action="append", type=_parse_shift, required=True)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1342_MCM_SHIFT_TRIGGERPROFILE.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1342_MCM_SHIFT_TRIGGERPROFILE.csv")
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for source, shift_path, balanced_path in args.shift:
        shift_rows = _read_by_asset(shift_path)
        balanced_rows = _read_balanced_by_asset(balanced_path)
        for asset, shift in sorted(shift_rows.items()):
            if str(shift.get("shift_label")) == "stabil":
                continue
            profile = balanced_rows.get(asset, {})
            rows.append(
                {
                    "source": source,
                    "asset": asset,
                    "shift_label": shift.get("shift_label", "-"),
                    "base_sequence": shift.get("base_sequence", "-"),
                    "holdout_sequence": shift.get("holdout_sequence", "-"),
                    "dominant_raw_class": profile.get("dominant_raw_class", "-"),
                    "raw_class_counts": profile.get("raw_class_counts", "-"),
                    "delta_auditory": round(_float(shift.get("delta_auditory")), 6),
                    "delta_visual": round(_float(shift.get("delta_visual")), 6),
                    "delta_pressure": round(_float(shift.get("delta_pressure")), 6),
                    "delta_range": round(_float(shift.get("delta_range")), 6),
                    "holdout_auditory": round(_float(profile.get("avg_auditory")), 6),
                    "holdout_visual": round(_float(profile.get("avg_visual_sharpness")), 6),
                    "holdout_pressure": round(_float(profile.get("avg_field_pressure")), 6),
                    "holdout_range": round(_float(profile.get("avg_range_pct")), 6),
                    "passive_only": 1,
                    "influences_action": 0,
                }
            )
    if not rows:
        raise RuntimeError("no non-stable shift rows found")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
