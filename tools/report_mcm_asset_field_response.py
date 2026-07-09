from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = befunde_root(ROOT) / "1251_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE.csv"
DEFAULT_OUT = befunde_root(ROOT) / "1253_MCM_ASSET_FELDANTWORT_BEWEGUNGSBRUCH.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _asset_from_world(world: str, data_file: str) -> str:
    text = f"{world} {data_file}".upper()
    for asset in ["BTC", "SOL", "PAXG", "DOGE", "XRP", "KAS"]:
        if asset in text:
            return asset
    if "NEG_STRESS" in text or "POS_EXPANSION" in text or "SIDEWAYS" in text:
        return "SOL_SYNTH_SEGMENT"
    return "UNBEKANNT"


def _avg(rows: list[dict[str, str]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_safe_float(row.get(key)) for row in rows) / len(rows)


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _response_class(row: dict[str, object]) -> str:
    reko_delta = _safe_float(row.get("avg_delta_next_rekopplung"))
    strain_delta = _safe_float(row.get("avg_delta_next_strain"))
    loudness = _safe_float(row.get("avg_loudness"))
    strain = _safe_float(row.get("avg_strain"))
    expansion = _safe_float(row.get("avg_expansion_ratio"))

    if reko_delta >= 0.10 and strain_delta <= -0.12:
        return "stark_entlastender_bruchkontakt"
    if reko_delta >= 0.06 and strain_delta <= -0.08:
        return "entlastender_bruchkontakt"
    if strain >= 0.30 and loudness >= 0.80 and expansion >= 4.0:
        return "lauter_randbruch"
    if reko_delta < 0.03 or strain_delta > -0.04:
        return "unklar_oder_nachlastig"
    return "gemischte_assetantwort"


def _build_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        asset = _asset_from_world(str(row.get("world", "")), str(row.get("data_file", "")))
        grouped[asset].append(row)

    out: list[dict[str, object]] = []
    for asset, items in grouped.items():
        movement_counts = Counter(str(row.get("movement_class", "")) for row in items)
        reading_counts = Counter(str(row.get("window_reading", "")) for row in items)
        world_counts = Counter(str(row.get("world", "")) for row in items)
        phase_counts = Counter(str(row.get("phase_key", "")) for row in items)
        built: dict[str, object] = {
            "asset": asset,
            "event_count": len(items),
            "dominant_world": _dominant(world_counts),
            "dominant_movement": _dominant(movement_counts),
            "dominant_window_reading": _dominant(reading_counts),
            "dominant_phase": _dominant(phase_counts),
            "avg_loudness": round(_avg(items, "current_loudness"), 6),
            "avg_intake": round(_avg(items, "current_intake"), 6),
            "avg_sharpness": round(_avg(items, "current_sharpness"), 6),
            "avg_rekopplung": round(_avg(items, "current_rekopplung"), 6),
            "avg_strain": round(_avg(items, "current_strain"), 6),
            "avg_delta_next_rekopplung": round(_avg(items, "delta_next_rekopplung"), 6),
            "avg_delta_next_strain": round(_avg(items, "delta_next_strain"), 6),
            "avg_raw_return": round(_avg(items, "raw_return"), 6),
            "avg_range_ratio": round(_avg(items, "range_ratio"), 6),
            "avg_expansion_ratio": round(_avg(items, "expansion_ratio"), 6),
            "avg_direction_consistency": round(_avg(items, "direction_consistency"), 6),
            "movement_counts": "; ".join(f"{key}:{value}" for key, value in movement_counts.most_common()),
            "reading_counts": "; ".join(f"{key}:{value}" for key, value in reading_counts.most_common()),
            "world_counts": "; ".join(f"{key}:{value}" for key, value in world_counts.most_common()),
        }
        built["response_class"] = _response_class(built)
        out.append(built)

    return sorted(out, key=lambda row: (-int(row["event_count"]), str(row["asset"])))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]], input_path: Path) -> None:
    class_counts = Counter(str(row["response_class"]) for row in rows)
    lines: list[str] = [
        "# MCM Asset-Feldantwort auf Bewegungsbruch",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Bleibt `bewegungsbruch -> lastkontakt_entlastet` ueber Assets gleich, oder bildet jedes Asset eine eigene MCM-Feldantwort?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose verdichtet die Rohwelt-Fensterlupe assetweise. Sie erzeugt keine Handlung und keine Strategie.",
        "",
        "## Eingabe",
        "",
        f"- `{input_path.relative_to(ROOT)}`",
        "",
        "## Profil",
        "",
        f"- Assetgruppen: `{len(rows)}`",
        f"- Antwortklassen: `{dict(class_counts.most_common())}`",
        "",
        "## Assetantworten",
        "",
        "| Asset | Fenster | Klasse | Bewegung | Lesart | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Dominante Welt |",
        "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["asset"]),
                    str(row["event_count"]),
                    str(row["response_class"]),
                    str(row["dominant_movement"]),
                    str(row["dominant_window_reading"]),
                    _fmt(row["avg_loudness"]),
                    _fmt(row["avg_strain"]),
                    _fmt(row["avg_delta_next_rekopplung"]),
                    _fmt(row["avg_delta_next_strain"]),
                    _fmt(row["avg_expansion_ratio"]),
                    _fmt(row["avg_direction_consistency"]),
                    str(row["dominant_world"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die gekoppelte Rohwelt-Lupe zeigt eine gemeinsame Grundform: `bewegungsbruch` dominiert fast durchgehend.",
            "",
            "Die Assetantwort unterscheidet sich aber in Staerke, Lautheit, Expansion und Entlastungsdelta.",
            "",
            "Damit ist die aktuelle Lesart:",
            "",
            "```text",
            "gleiche Grundklasse, unterschiedliche Feldfaerbung",
            "```",
            "",
            "Das passt zur bisherigen MCM-Lesung: Die Topologie bleibt stabil, aber Welt- und Assetcharakter faerben die Feldantwort.",
            "",
            "## Grenze",
            "",
            "Diese Diagnose nutzt nur eindeutig gekoppelte Fenster aus `1251`. Nicht alle Segmentwelten sind enthalten.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird geprueft, ob die assetweise Feldfaerbung ueber neue Rohweltfenster reproduzierbar bleibt oder ob sie nur aus dieser Auswahl stammt.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verdichtet MCM-Rohweltfenster nach Asset-Feldantwort.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Rohwelt-Fensterlupe CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _build_rows(_load_csv(input_path))
    csv_path = out_path.with_suffix(".csv")
    _write_csv(csv_path, rows)
    _write_markdown(out_path, rows, input_path)

    print(f"wrote {out_path}")
    print(f"wrote {csv_path}")
    print(f"assets={len(rows)}")


if __name__ == "__main__":
    main()
