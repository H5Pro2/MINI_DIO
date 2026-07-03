from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_worldlage_multiscale_asset_distribution import _asset_from_world


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _load_asset_bases(path: Path) -> dict[str, dict[str, float]]:
    bases: dict[str, dict[str, float]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if str(row.get("group_type")) != "asset":
                continue
            asset = str(row.get("group") or "")
            if not asset:
                continue
            bases[asset] = {
                "avg_auditory": _float(row.get("avg_auditory")),
                "avg_visual_sharpness": _float(row.get("avg_visual_sharpness")),
                "avg_field_pressure": _float(row.get("avg_field_pressure")),
                "avg_range_pct": _float(row.get("avg_range_pct")),
            }
    if not bases:
        raise RuntimeError("no asset bases found")
    return bases


def _read_candidates(path: Path, bases: dict[str, dict[str, float]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            world = str(row.get("world") or "")
            asset = _asset_from_world(world)
            if asset in {"SYNTH", "UNKNOWN"} or asset not in bases:
                continue
            base = bases[asset]
            auditory = _float(row.get("avg_auditory"))
            visual = _float(row.get("avg_visual_sharpness"))
            pressure = _float(row.get("avg_field_pressure"))
            range_pct = _float(row.get("avg_range_pct"))
            delta_auditory = auditory - base["avg_auditory"]
            delta_visual = visual - base["avg_visual_sharpness"]
            delta_pressure = pressure - base["avg_field_pressure"]
            delta_range = range_pct - base["avg_range_pct"]
            if delta_auditory <= 0.03 or delta_visual <= 0.0 or delta_pressure <= 0.0 or delta_range >= -0.03:
                continue
            score = delta_auditory + delta_visual + delta_pressure + abs(delta_range)
            rows.append(
                {
                    "asset": asset,
                    "world": world,
                    "scale": row.get("scale", "-"),
                    "block_index": row.get("block_index", "-"),
                    "base_sequence": row.get("base_sequence", "-"),
                    "raw_class": row.get("raw_class", "-"),
                    "score": round(score, 6),
                    "delta_auditory": round(delta_auditory, 6),
                    "delta_visual": round(delta_visual, 6),
                    "delta_pressure": round(delta_pressure, 6),
                    "delta_range": round(delta_range, 6),
                    "avg_auditory": round(auditory, 6),
                    "avg_visual_sharpness": round(visual, 6),
                    "avg_field_pressure": round(pressure, 6),
                    "avg_range_pct": round(range_pct, 6),
                    "price_move_pct": round(_float(row.get("price_move_pct")), 6),
                    "passive_only": 1,
                    "influences_action": 0,
                }
            )
    rows.sort(
        key=lambda item: (
            str(item["asset"]),
            -float(item["score"]),
            str(item["world"]),
            str(item["scale"]),
            str(item["block_index"]),
        )
    )
    return rows


def _counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        name = str(row.get(key) or "-")
        out[name] = out.get(name, 0) + 1
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, *, top: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    asset_counts = _counter(rows, "asset")
    sequence_counts = _counter(rows, "base_sequence")
    raw_counts = _counter(rows, "raw_class")

    lines = [
        "# Hoerbarer schmaler Shift - assetrelativer Holdout",
        "",
        "Diese Diagnose prueft, ob das Mikrofensterprofil des `hoerbarer_schmaler_folgeschift` auch ausserhalb der BTC-Kandidaten assetrelativ auftaucht.",
        "",
        "Jedes Fenster wird gegen die eigene Asset-Basis gelesen. Dadurch wird nicht Preisgroesse oder Lautstaerke eines Assets gemessen, sondern relative Veraenderung der Sinneslage.",
        "",
        "Gesucht wurde passiv nach:",
        "",
        "- Hoeren steigt gegenueber eigener Asset-Basis deutlich",
        "- Sicht steigt gegenueber eigener Asset-Basis",
        "- Felddruck steigt gegenueber eigener Asset-Basis",
        "- Range sinkt gegenueber eigener Asset-Basis",
        "",
        "Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.",
        "",
        "## Verdichtung",
        "",
        f"- Kandidatenfenster: `{len(rows)}`",
        "",
        "Assets:",
        "",
    ]
    for name, count in sorted(asset_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{name}`: `{count}`")
    lines.extend(["", "Sequenzen:", ""])
    for name, count in sorted(sequence_counts.items(), key=lambda item: (-item[1], item[0]))[:12]:
        lines.append(f"- `{name}`: `{count}`")
    lines.extend(["", "Rohklassen:", ""])
    for name, count in sorted(raw_counts.items(), key=lambda item: (-item[1], item[0]))[:8]:
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste Fenster pro Asset",
            "",
            "| Asset | Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |",
            "|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    shown = 0
    for asset in sorted(asset_counts):
        asset_rows = [row for row in rows if str(row.get("asset")) == asset]
        for row in asset_rows[:top]:
            lines.append(
                "| {asset} | {world} | {scale} | {block_index} | `{base_sequence}` | `{raw_class}` | {score:.4f} | {delta_auditory:.4f} | {delta_visual:.4f} | {delta_pressure:.4f} | {delta_range:.4f} |".format(
                    **row
                )
            )
            shown += 1

    if shown == 0:
        lines.append("| - | - | 0 | 0 | `-` | `-` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |")

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Der hoerbare-schmale Shift wird hier nicht als feste Rolle gesetzt.",
            "",
            "Wenn er assetrelativ in mehreren Assets erscheint, ist er eher eine wiederkehrende Mikrophase des Feldes. Wenn er nur bei BTC stabil bleibt, ist er eher BTC-spezifische Faerbung.",
            "",
            "Wie es weitergeht: Als naechstes sollte die Kandidatenfamilie gegen neue, noch nicht verwendete Weltfenster gelesen werden. Erst dann ist entscheidbar, ob daraus eine reproduzierbare Mikrorolle oder nur lokale Oberflaechenvarianz entsteht.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-windows", default="docs/befunde/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER.csv")
    parser.add_argument("--base", default="docs/befunde/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--out", default="docs/befunde/1348_HOERBARER_SCHMALER_SHIFT_ASSETRELATIVER_HOLDOUT.md")
    parser.add_argument("--csv-out", default="docs/befunde/1348_HOERBARER_SCHMALER_SHIFT_ASSETRELATIVER_HOLDOUT.csv")
    args = parser.parse_args()

    bases = _load_asset_bases(Path(args.base))
    rows = _read_candidates(Path(args.raw_windows), bases)
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), top=args.top)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
