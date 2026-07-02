from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = ROOT / "docs" / "befunde" / "1257_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE_ERWEITERT.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1262_MCM_GEGENFORMEN_TICKFENSTER.md"


COUNTERFORMS = {
    "rekopplung_bricht_in_last",
    "gemischtes_fenster",
    "rekopplung_vor_neuer_last",
    "lastkontakt_bleibt",
}


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


def _severity(row: dict[str, str]) -> float:
    reko_loss = max(0.0, -_safe_float(row.get("delta_next_rekopplung")))
    strain_gain = max(0.0, _safe_float(row.get("delta_next_strain")))
    weak_reko = max(0.0, 0.05 - _safe_float(row.get("delta_next_rekopplung")))
    weak_strain_release = max(0.0, _safe_float(row.get("delta_next_strain")) + 0.05)
    return reko_loss + strain_gain + (weak_reko * 0.5) + (weak_strain_release * 0.5)


def _counterform_kind(row: dict[str, str]) -> str:
    reading = str(row.get("window_reading", "") or "")
    reko_delta = _safe_float(row.get("delta_next_rekopplung"))
    strain_delta = _safe_float(row.get("delta_next_strain"))
    if reading == "rekopplung_vor_neuer_last":
        return "rueckfall_nach_kurzer_rekopplung"
    if reading == "rekopplung_bricht_in_last":
        return "schwache_entlastung_gebrochene_rekopplung"
    if reading == "gemischtes_fenster" and reko_delta < 0.0 and strain_delta > 0.0:
        return "aktive_nachlast"
    if reading == "lastkontakt_bleibt":
        return "last_bleibt"
    return "gemischte_gegenform"


def _build_rows(rows: list[dict[str, str]], limit: int) -> list[dict[str, object]]:
    selected = [row for row in rows if str(row.get("window_reading", "")) in COUNTERFORMS]
    selected.sort(key=lambda row: (-_severity(row), str(row.get("world", "")), str(row.get("center_tick", ""))))
    out: list[dict[str, object]] = []
    for row in selected[:limit]:
        out.append(
            {
                "counterform_kind": _counterform_kind(row),
                "window_reading": row.get("window_reading", ""),
                "phase_key": row.get("phase_key", ""),
                "world": row.get("world", ""),
                "data_file": row.get("data_file", ""),
                "current_start_tick": row.get("current_start_tick", ""),
                "current_end_tick": row.get("current_end_tick", ""),
                "center_tick": row.get("center_tick", ""),
                "current_loudness": row.get("current_loudness", ""),
                "current_intake": row.get("current_intake", ""),
                "current_sharpness": row.get("current_sharpness", ""),
                "current_rekopplung": row.get("current_rekopplung", ""),
                "current_strain": row.get("current_strain", ""),
                "delta_next_rekopplung": row.get("delta_next_rekopplung", ""),
                "delta_next_strain": row.get("delta_next_strain", ""),
                "raw_return": row.get("raw_return", ""),
                "range_ratio": row.get("range_ratio", ""),
                "expansion_ratio": row.get("expansion_ratio", ""),
                "direction_consistency": row.get("direction_consistency", ""),
                "movement_class": row.get("movement_class", ""),
                "severity": round(_severity(row), 6),
            }
        )
    return out


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
    kind_counts = Counter(str(row["counterform_kind"]) for row in rows)
    reading_counts = Counter(str(row["window_reading"]) for row in rows)
    world_counts = Counter(str(row["world"]) for row in rows)
    phase_counts = Counter(str(row["phase_key"]) for row in rows)

    lines: list[str] = [
        "# MCM Gegenformen Tickfenster",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Welche konkreten Tickfenster zeigen, dass Bewegungsbruch nicht in Entlastung, sondern in Nachlast oder gebrochene Rekopplung geht?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose isoliert Gegenformen aus der erweiterten Rohwelt-Fensterlupe.",
        "",
        "## Eingabe",
        "",
        f"- `{input_path.relative_to(ROOT)}`",
        "",
        "## Profil",
        "",
        f"- markierte Gegenform-Fenster: `{len(rows)}`",
        f"- Gegenformarten: `{dict(kind_counts.most_common())}`",
        f"- Fensterlesarten: `{dict(reading_counts.most_common())}`",
        f"- Welten: `{dict(world_counts.most_common())}`",
        "",
        "## Dominante Phasen",
        "",
    ]
    for phase, count in phase_counts.most_common(8):
        lines.append(f"- `{phase}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste Gegenfenster",
            "",
            "| Art | Lesart | Welt | Tick | Phase | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Severity |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows[:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["counterform_kind"]),
                    str(row["window_reading"]),
                    str(row["world"]),
                    str(row["center_tick"]),
                    str(row["phase_key"]),
                    _fmt(row["current_loudness"]),
                    _fmt(row["current_strain"]),
                    _fmt(row["delta_next_rekopplung"]),
                    _fmt(row["delta_next_strain"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["severity"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Gegenformen entstehen nicht aus einer anderen Rohweltklasse. Sie bleiben ueberwiegend `bewegungsbruch`.",
            "",
            "Der Unterschied liegt in der Folge:",
            "",
            "```text",
            "Entlastung: Rekopplung steigt, Strain faellt.",
            "Gegenform: Rekopplung steigt zu schwach, faellt, oder Strain steigt erneut.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Gegenform-Liste mit den direkten vorherigen Rollen gekoppelt werden, um zu sehen, ob bestimmte Vorrollen Nachlast beguenstigen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Markiert konkrete Gegenform-Tickfenster.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Erweiterte Rohwelt-Fensterlupe CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    parser.add_argument("--limit", type=int, default=96, help="Maximale Gegenfenster.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _build_rows(_load_csv(input_path), args.limit)
    csv_path = out_path.with_suffix(".csv")
    _write_csv(csv_path, rows)
    _write_markdown(out_path, rows, input_path)

    print(f"wrote {out_path}")
    print(f"wrote {csv_path}")
    print(f"counter_windows={len(rows)}")


if __name__ == "__main__":
    main()
