from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _load_base(path: Path, asset: str) -> dict[str, float]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            if str(row.get("group_type")) == "asset" and str(row.get("group")) == asset:
                return {
                    "avg_auditory": _float(row.get("avg_auditory")),
                    "avg_visual_sharpness": _float(row.get("avg_visual_sharpness")),
                    "avg_field_pressure": _float(row.get("avg_field_pressure")),
                    "avg_range_pct": _float(row.get("avg_range_pct")),
                }
    raise RuntimeError(f"asset base not found: {asset}")


def _read_candidates(path: Path, base: dict[str, float]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
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
                    "world": row.get("world", "-"),
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
    rows.sort(key=lambda item: (-float(item["score"]), str(item["world"]), str(item["scale"]), str(item["block_index"])))
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, *, base: dict[str, float], top: int) -> None:
    sequence_counts: dict[str, int] = {}
    world_counts: dict[str, int] = {}
    raw_counts: dict[str, int] = {}
    for row in rows:
        sequence_counts[str(row["base_sequence"])] = sequence_counts.get(str(row["base_sequence"]), 0) + 1
        world_counts[str(row["world"])] = world_counts.get(str(row["world"]), 0) + 1
        raw_counts[str(row["raw_class"])] = raw_counts.get(str(row["raw_class"]), 0) + 1

    lines = [
        "# Hoerbarer schmaler Folgeschift - Kandidatenfenster",
        "",
        "Diese Diagnose sucht Fenster, die das Rohprofil des bisher einzelnen `hoerbarer_schmaler_folgeschift` tragen.",
        "",
        "Gesucht wurde passiv nach:",
        "",
        "- Hoeren steigt gegenueber BTC-Basis deutlich",
        "- Sicht steigt gegenueber BTC-Basis",
        "- Felddruck steigt gegenueber BTC-Basis",
        "- Range sinkt gegenueber BTC-Basis",
        "",
        "Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.",
        "",
        "## BTC-Basis",
        "",
        f"- Hoeren: `{base['avg_auditory']:.6f}`",
        f"- Sicht: `{base['avg_visual_sharpness']:.6f}`",
        f"- Felddruck: `{base['avg_field_pressure']:.6f}`",
        f"- Range: `{base['avg_range_pct']:.6f}`",
        "",
        "## Verdichtung",
        "",
        f"- Kandidatenfenster: `{len(rows)}`",
        "",
        "Sequenzen:",
        "",
    ]
    for name, count in sorted(sequence_counts.items(), key=lambda item: (-item[1], item[0]))[:12]:
        lines.append(f"- `{name}`: `{count}`")
    lines.extend(["", "Welten:", ""])
    for name, count in sorted(world_counts.items(), key=lambda item: (-item[1], item[0]))[:12]:
        lines.append(f"- `{name}`: `{count}`")
    lines.extend(["", "Rohklassen:", ""])
    for name, count in sorted(raw_counts.items(), key=lambda item: (-item[1], item[0]))[:8]:
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste Fenster",
            "",
            "| Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |",
            "|---|---:|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows[:top]:
        lines.append(
            "| {world} | {scale} | {block_index} | `{base_sequence}` | `{raw_class}` | {score:.4f} | {delta_auditory:.4f} | {delta_visual:.4f} | {delta_pressure:.4f} | {delta_range:.4f} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Der starke hoerbare-schmale Shift ist als Mikrofenster mehrfach vorhanden.",
            "",
            "Er wird aber in breiten Weltgruppen nicht automatisch zur dominanten Assetfaerbung. Das spricht dafuer, dass diese Sonderrolle lokal und phasenabhaengig ist.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "- als Mikrofenster: klar vorhanden",
            "- als ganze Weltfaerbung: bisher nicht stabil reproduziert",
            "",
            "Wie es weitergeht: Als naechstes sollte ein passiver Mikrofenster-Holdout gebaut werden: nicht ganze Welten mitteln, sondern nur passende Kandidatenfenster in neuen BTC/SOL-Welten suchen und gegen diese Kandidatenfamilie vergleichen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-windows", default="docs/befunde/1001-2000/1001-1500/1345_BTC_CANDIDATE_WELTLAGEN_ROHWELTFENSTER.csv")
    parser.add_argument("--base", default="docs/befunde/1001-2000/1001-1500/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument("--asset", default="BTC")
    parser.add_argument("--top", type=int, default=25)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1347_HOERBARER_SCHMALER_SHIFT_KANDIDATEN.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1347_HOERBARER_SCHMALER_SHIFT_KANDIDATEN.csv")
    args = parser.parse_args()

    base = _load_base(Path(args.base), args.asset)
    rows = _read_candidates(Path(args.raw_windows), base)
    if not rows:
        raise RuntimeError("no hoerbarer schmaler candidates found")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), base=base, top=args.top)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
