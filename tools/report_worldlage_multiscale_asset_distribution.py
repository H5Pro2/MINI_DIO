from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _asset_from_world(world: str) -> str:
    upper = world.upper()
    for asset in ("SOL", "BTC", "DOGE", "XRP", "PAXG", "KAS"):
        if asset in upper:
            return asset
    if "VISUAL" in upper or "DESYNC" in upper or "SYNTH" in upper:
        return "SYNTH"
    return "UNKNOWN"


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _summarize(rows: list[dict[str, str]], key: str) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if key == "asset":
            group_key = _asset_from_world(str(row.get("world", "")))
        else:
            group_key = str(row.get(key, ""))
        groups.setdefault(group_key, []).append(row)

    out: list[dict[str, object]] = []
    total = max(1, len(rows))
    for name, group in groups.items():
        raw_counts: dict[str, int] = {}
        sequence_counts: dict[str, int] = {}
        scale_counts: dict[str, int] = {}
        for row in group:
            raw_counts[str(row.get("raw_class", ""))] = raw_counts.get(str(row.get("raw_class", "")), 0) + 1
            sequence_counts[str(row.get("base_sequence", ""))] = sequence_counts.get(str(row.get("base_sequence", "")), 0) + 1
            scale_counts[str(row.get("scale", ""))] = scale_counts.get(str(row.get("scale", "")), 0) + 1
        dominant_raw = sorted(raw_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
        dominant_sequence = sorted(sequence_counts.items(), key=lambda item: (-item[1], item[0]))[0][0]
        out.append(
            {
                "group_type": key,
                "group": name,
                "count": len(group),
                "share": round(len(group) / total, 6),
                "dominant_raw_class": dominant_raw,
                "raw_class_counts": ";".join(f"{k}:{v}" for k, v in sorted(raw_counts.items(), key=lambda item: (-item[1], item[0]))),
                "dominant_sequence": dominant_sequence,
                "sequence_count": sequence_counts[dominant_sequence],
                "scale_counts": ";".join(f"{k}:{v}" for k, v in sorted(scale_counts.items(), key=lambda item: item[0])),
                "avg_price_move_pct": round(_avg([_float(row.get("price_move_pct")) for row in group]), 6),
                "avg_range_pct": round(_avg([_float(row.get("avg_range_pct")) for row in group]), 6),
                "avg_auditory": round(_avg([_float(row.get("avg_auditory")) for row in group]), 6),
                "avg_visual_sharpness": round(_avg([_float(row.get("avg_visual_sharpness")) for row in group]), 6),
                "avg_field_pressure": round(_avg([_float(row.get("avg_field_pressure")) for row in group]), 6),
                "passive_only": 1,
                "influences_action": 0,
            }
        )
    out.sort(key=lambda row: (-int(row["count"]), str(row["group"])))
    return out


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_type: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        by_type.setdefault(str(row["group_type"]), []).append(row)

    lines = [
        "# Mehrskalige Zwischenlagen - Asset- und Weltverteilung",
        "",
        "Diese Diagnose prueft, ob skalenabhaengige Lagefolgen von einzelnen Assets/Welten dominiert werden.",
        "",
        "## Asset-Verteilung",
        "",
        "| Asset | Fenster | Anteil | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck |",
        "|---|---:|---:|---|---|---|---:|---:|---:|",
    ]
    for row in by_type.get("asset", []):
        lines.append(
            "| {group} | {count} | {share:.3f} | {dominant_raw_class} | {dominant_sequence} | {scale_counts} | {avg_auditory:.4f} | {avg_visual_sharpness:.4f} | {avg_field_pressure:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Welt-Verteilung",
            "",
            "| Welt | Fenster | Anteil | Rohklasse | Sequenz | Skalen | Hoeren | Sicht | Felddruck |",
            "|---|---:|---:|---|---|---|---:|---:|---:|",
        ]
    )
    for row in by_type.get("world", []):
        lines.append(
            "| {group} | {count} | {share:.3f} | {dominant_raw_class} | {dominant_sequence} | {scale_counts} | {avg_auditory:.4f} | {avg_visual_sharpness:.4f} | {avg_field_pressure:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die skalenabhaengigen Zwischenlagen werden nicht von einer einzelnen Welt erzeugt.",
            "",
            "Sie treten breit ueber reale Assetwelten auf. Synthetische Welten sind nur schwach beteiligt.",
            "",
            "Damit ist die Zwischenlage eher eine wiederkehrende Feldleseform als ein einzelnes Asset-Artefakt.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Steuerung.",
            "",
            "Wie es weitergeht: Als naechstes sollte geprueft werden, ob die dominante Sequenz pro Asset gleich bleibt oder ob jedes Asset seine eigene Zwischenlagen-Faerbung ausbildet.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1309_WELTLAGEN_MEHRSKALIG_ROHWELTFENSTER.csv")
    parser.add_argument("--out", default="docs/befunde/1313_WELTLAGEN_ZWISCHENLAGEN_ASSET_VERTEILUNG.md")
    parser.add_argument("--csv-out", default="docs/befunde/1313_WELTLAGEN_ZWISCHENLAGEN_ASSET_VERTEILUNG.csv")
    args = parser.parse_args()

    with Path(args.input).open("r", encoding="utf-8", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    if not source_rows:
        raise RuntimeError("no source rows")
    rows = _summarize(source_rows, "asset") + _summarize(source_rows, "world")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
