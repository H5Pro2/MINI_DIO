from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = ROOT / "docs" / "befunde" / "1257_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE_ERWEITERT.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1260_MCM_BEWEGUNGSBRUCH_FOLGEFORMEN.md"


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


def _avg(rows: list[dict[str, str]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(_safe_float(row.get(key)) for row in rows) / len(rows)


def _dominant(counter: Counter[str]) -> str:
    return counter.most_common(1)[0][0] if counter else "-"


def _followup_quality(row: dict[str, object]) -> str:
    reko_delta = _safe_float(row.get("avg_delta_next_rekopplung"))
    strain_delta = _safe_float(row.get("avg_delta_next_strain"))
    if reko_delta >= 0.08 and strain_delta <= -0.10:
        return "klare_entlastung"
    if reko_delta >= 0.04 and strain_delta <= -0.06:
        return "moderate_entlastung"
    if reko_delta >= 0.0 and strain_delta <= -0.02:
        return "schwache_entlastung"
    if reko_delta < 0.0 or strain_delta > 0.0:
        return "nachlast_oder_bruch"
    return "unklar"


def _build_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("window_reading", "") or "-")].append(row)

    out: list[dict[str, object]] = []
    for reading, items in grouped.items():
        world_counts = Counter(str(row.get("world", "")) for row in items)
        movement_counts = Counter(str(row.get("movement_class", "")) for row in items)
        phase_counts = Counter(str(row.get("phase_key", "")) for row in items)
        built: dict[str, object] = {
            "window_reading": reading,
            "event_count": len(items),
            "dominant_world": _dominant(world_counts),
            "dominant_movement": _dominant(movement_counts),
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
            "avg_break_ratio": round(_avg(items, "break_ratio"), 6),
            "avg_direction_consistency": round(_avg(items, "direction_consistency"), 6),
            "world_counts": "; ".join(f"{key}:{value}" for key, value in world_counts.most_common(8)),
            "phase_counts": "; ".join(f"{key}:{value}" for key, value in phase_counts.most_common(8)),
        }
        built["followup_quality"] = _followup_quality(built)
        out.append(built)

    return sorted(out, key=lambda row: (-int(row["event_count"]), str(row["window_reading"])))


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
    lines: list[str] = [
        "# MCM Bewegungsbruch Folgeformen",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Wann wird aus `bewegungsbruch` Entlastung, und wann entsteht Nachlast, gebrochene Rekopplung oder ein gemischtes Fenster?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose vergleicht die Fensterlesarten aus der erweiterten Rohwelt-Fensterlupe.",
        "",
        "## Eingabe",
        "",
        f"- `{input_path.relative_to(ROOT)}`",
        "",
        "## Folgeformen",
        "",
        "| Fensterlesart | Anzahl | Folgequalitaet | Bewegung | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Dominante Welt |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["window_reading"]),
                    str(row["event_count"]),
                    str(row["followup_quality"]),
                    str(row["dominant_movement"]),
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
            "Die Hauptform `lastkontakt_entlastet` unterscheidet sich nicht dadurch, dass sie keinen Bewegungsbruch hat.",
            "",
            "Der Unterschied liegt vor allem in der Folgequalitaet:",
            "",
            "```text",
            "Entlastung = Rekopplung steigt deutlich und Strain faellt deutlich.",
            "Gegenform = dieselbe Rohweltklasse, aber schwacheres oder gebrochenes Folgeprofil.",
            "```",
            "",
            "Damit ist Bewegungsbruch die Rohweltbedingung, aber nicht die ganze Erklaerung.",
            "",
            "## Bedeutung",
            "",
            "Das MCM-Feld liest nicht nur die Aussenbewegung. Es liest, ob das Feld nach der Aussenbewegung wieder Anschluss findet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die Gegenformen mit konkreten Tickfenstern markiert werden: Wo beginnt die Nachlast, und welche Feldrolle liegt direkt davor?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Vergleicht Folgeformen nach Bewegungsbruch.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Erweiterte Rohwelt-Fensterlupe CSV.")
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
    print(f"forms={len(rows)}")


if __name__ == "__main__":
    main()
