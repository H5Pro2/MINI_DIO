from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, 0.0) or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _asset(world: str) -> str:
    value = world.lower()
    for asset in ("btc", "sol", "paxg", "doge", "kas", "xrp"):
        if asset in value:
            return asset.upper()
    return "UNBEKANNT"


def _timeframe(world: str, group: str) -> str:
    value = world.lower()
    if "_1h" in value or group == "zeit_1h":
        return "1h"
    if "_5m" in value or group == "feld_5m":
        return "5m"
    if "_15m" in value:
        return "15m"
    if "_30m" in value:
        return "30m"
    return "unbekannt"


def _top(counter: Counter[str], limit: int = 4) -> str:
    if not counter:
        return "-"
    return ";".join(f"{key}:{value}" for key, value in counter.most_common(limit))


def _summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    buckets: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (
            row.get("family", "-"),
            row.get("pattern", "-"),
            _asset(row.get("world", "")),
            _timeframe(row.get("world", ""), row.get("world_group", "")),
        )
        buckets[key].append(row)

    out: list[dict[str, object]] = []
    for (family, pattern, asset, timeframe), items in sorted(buckets.items()):
        worlds = sorted({item.get("world", "-") for item in items})
        out.append(
            {
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
                "family": family,
                "pattern": pattern,
                "asset": asset,
                "timeframe": timeframe,
                "events": len(items),
                "worlds": len(worlds),
                "world_names": ";".join(worlds),
                "visual": _top(Counter(item.get("visual", "-") for item in items)),
                "tone": _top(Counter(item.get("tone", "-") for item in items)),
                "field": _top(Counter(item.get("field", "-") for item in items)),
                "target_tension": _mean([_float(item, "target_tension") for item in items]),
                "target_rekopplung": _mean([_float(item, "target_rekopplung") for item in items]),
                "target_strain": _mean([_float(item, "target_strain") for item in items]),
                "delta_tension": _mean([_float(item, "delta_tension") for item in items]),
                "delta_rekopplung": _mean([_float(item, "delta_rekopplung") for item in items]),
                "delta_strain": _mean([_float(item, "delta_strain") for item in items]),
                "visual_sharpness": _mean([_float(item, "visual_sharpness") for item in items]),
                "visual_distance": _mean([_float(item, "visual_distance") for item in items]),
                "auditory_loudness": _mean([_float(item, "auditory_loudness") for item in items]),
                "auditory_listen": _mean([_float(item, "auditory_listen") for item in items]),
                "raw_field_intake": _mean([_float(item, "raw_field_intake") for item in items]),
                "adapted_field_intake": _mean([_float(item, "adapted_field_intake") for item in items]),
            }
        )
    return sorted(out, key=lambda item: (str(item["family"]), str(item["pattern"]), -int(item["events"])))


def _read_rows(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in paths:
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows.extend(csv.DictReader(handle))
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _report_title(path: Path, fallback: str) -> str:
    stem = path.stem
    if "_" not in stem:
        return fallback
    prefix, rest = stem.split("_", 1)
    if not prefix.isdigit():
        return fallback
    return f"{prefix} - {rest.replace('_', ' ').title()}"


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {_report_title(path, 'Bindung Neuer Brueckenkandidaten')}",
        "",
        "Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Woran sind die neuen Brueckenkandidaten gebunden: Asset, Zeitrahmen, Rezeptorhaltung, Tonband oder Feldfolge?",
        "",
        "## Bindungsmatrix",
        "",
        "| Familie | Lesart | Asset | TF | Events | Welten | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Hoeren | Schaerfe | Intake |",
        "|---|---|---|---|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {family} | {pattern} | {asset} | {timeframe} | {events} | {worlds} | {visual} | {tone} | {field} | {target_tension} | {target_rekopplung} | {target_strain} | {auditory_listen} | {visual_sharpness} | {adapted_field_intake} |".format(
                **{key: _fmt(value) for key, value in row.items()}
            )
        )

    by_family = defaultdict(list)
    for row in rows:
        by_family[row["family"]].append(row)

    lines.extend(["", "## Technische Lesart", ""])
    for family, items in sorted(by_family.items()):
        events = sum(int(item["events"]) for item in items)
        assets = sorted({str(item["asset"]) for item in items})
        timeframes = sorted({str(item["timeframe"]) for item in items})
        patterns = sorted({str(item["pattern"]) for item in items})
        lines.extend(
            [
                f"- `{family}`: `{events}` Ereignisse, Assets `{', '.join(assets)}`, Zeitrahmen `{', '.join(timeframes)}`, Lesarten `{', '.join(patterns)}`.",
            ]
        )

    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Die Matrix beschreibt Bindung, nicht Bedeutung. Eine Familie wird erst belastbarer, wenn sie in weiteren Weltgruppen aehnlich gebunden bleibt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob die Bindung aus Asset, Zeitrahmen und Rezeptorhaltung bei frisch erzeugten Folgewelten wieder auftaucht.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events-csv", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _summarize(_read_rows([Path(item) for item in args.events_csv]))
    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md))
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
