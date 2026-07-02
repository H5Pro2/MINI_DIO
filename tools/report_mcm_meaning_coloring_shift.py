from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _read_assets(path: Path) -> dict[str, dict[str, str]]:
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


def _shift_label(base: dict[str, str], holdout: dict[str, str]) -> str:
    auditory_delta = _float(holdout.get("avg_auditory")) - _float(base.get("avg_auditory"))
    visual_delta = _float(holdout.get("avg_visual_sharpness")) - _float(base.get("avg_visual_sharpness"))
    pressure_delta = _float(holdout.get("avg_field_pressure")) - _float(base.get("avg_field_pressure"))
    range_delta = _float(holdout.get("avg_range_pct")) - _float(base.get("avg_range_pct"))
    sequence_changed = base.get("dominant_sequence") != holdout.get("dominant_sequence")
    if sequence_changed and auditory_delta > 0.03 and range_delta < -0.03:
        return "hoerbarer_schmaler_folgeschift"
    if sequence_changed and pressure_delta < -0.004 and range_delta >= 0.0:
        return "druck_entlasteter_normalisierungsshift"
    if sequence_changed:
        return "folgefaerbung_veraendert"
    if abs(range_delta) > 0.08:
        return "oberflaeche_veraendert"
    return "stabil"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, *, base_path: Path, holdout_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Bedeutungsfaerbung - Basis gegen Holdout",
        "",
        "Diese Diagnose untersucht, warum einzelne Assetfaerbungen ihre dominante Folge veraendern.",
        "",
        f"Verglichen werden Basis `{base_path.name}` und Holdout `{holdout_path.name}`.",
        "",
        "## Verschiebungen",
        "",
        "| Asset | Shift | Basis-Folge | Holdout-Folge | dHoeren | dSicht | dDruck | dRange |",
        "|---|---|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {asset} | `{shift_label}` | `{base_sequence}` | `{holdout_sequence}` | {delta_auditory:.4f} | {delta_visual:.4f} | {delta_pressure:.4f} | {delta_range:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die Feldform bleibt gleich, aber die Faerbung verschiebt sich je nach Rohweltprofil.",
            "",
            "Die konkrete Faerbung wird ueber Folge, Hoeren, Sicht, Felddruck und Range beschrieben.",
            "",
            "Wichtig ist nicht ein einzelnes Asset, sondern ob ein Shift-Typ in weiteren Welten wiederkehrt oder ausklingt.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.",
            "",
            "Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese Shift-Typen bei weiteren Holdout-Fenstern erneut auftreten oder ob sie lokale Oberflaechenvarianten bleiben.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="docs/befunde/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument("--holdout", default="docs/befunde/1322_HOLDOUT_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument("--out", default="docs/befunde/1325_MCM_BEDEUTUNGSFAERBUNG_SHIFT.md")
    parser.add_argument("--csv-out", default="docs/befunde/1325_MCM_BEDEUTUNGSFAERBUNG_SHIFT.csv")
    args = parser.parse_args()

    base_rows = _read_assets(Path(args.base))
    holdout_rows = _read_assets(Path(args.holdout))
    rows: list[dict[str, object]] = []
    for asset in sorted(set(base_rows) & set(holdout_rows)):
        base = base_rows[asset]
        holdout = holdout_rows[asset]
        rows.append(
            {
                "asset": asset,
                "shift_label": _shift_label(base, holdout),
                "base_sequence": base.get("dominant_sequence", "-"),
                "holdout_sequence": holdout.get("dominant_sequence", "-"),
                "delta_auditory": round(_float(holdout.get("avg_auditory")) - _float(base.get("avg_auditory")), 6),
                "delta_visual": round(_float(holdout.get("avg_visual_sharpness")) - _float(base.get("avg_visual_sharpness")), 6),
                "delta_pressure": round(_float(holdout.get("avg_field_pressure")) - _float(base.get("avg_field_pressure")), 6),
                "delta_range": round(_float(holdout.get("avg_range_pct")) - _float(base.get("avg_range_pct")), 6),
                "passive_only": 1,
                "influences_action": 0,
            }
        )
    if not rows:
        raise RuntimeError("no overlapping assets")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), base_path=Path(args.base), holdout_path=Path(args.holdout))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
