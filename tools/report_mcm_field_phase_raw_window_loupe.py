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


DEFAULT_EVENTS = ROOT / "docs" / "befunde" / "1249_MCM_FELDPHASEN_FENSTERLUPE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1251_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE.md"


WORLD_DATA_MAP = {
    "BTC_5M_2K": "kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv",
    "BTC_1H_2K": "kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv",
    "SOL_5M_2K": "kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv",
    "SOL_1H_2K": "kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv",
    "KAS_5M_2K": "kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
    "DOGE_5M_10K": "kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv",
    "XRP_5M_10K": "kontrolliert_xrp_2024_5m_10k_XRPUSDT.csv",
    "PAXG_5M_10K": "kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv",
    "NEG_STRESS_10K": "kontrolliert_2023_negative_stress_10k_5m_SOLUSDT.csv",
    "POS_EXPANSION_10K": "kontrolliert_2023_positive_expansion_10k_5m_SOLUSDT.csv",
    "SIDEWAYS_10K": "kontrolliert_2026_sideways_10k_5m_SOLUSDT.csv",
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


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _raw_window(raw_rows: list[dict[str, str]], tick: int, radius: int) -> list[dict[str, str]]:
    if not raw_rows:
        return []
    index = tick - 1
    if index < 0 or index >= len(raw_rows):
        return []
    return raw_rows[max(0, index - radius) : min(len(raw_rows), index + radius + 1)]


def _movement_class(
    raw_return: float,
    range_ratio: float,
    direction_consistency: float,
    expansion_ratio: float,
    break_ratio: float,
) -> str:
    if expansion_ratio >= 2.5 and direction_consistency >= 0.45:
        return "expansion_impuls"
    if expansion_ratio >= 2.0 and direction_consistency < 0.45:
        return "bewegungsbruch"
    if break_ratio >= 0.55 and range_ratio >= 0.012:
        return "bruch_koerperlast"
    if direction_consistency >= 0.60 and abs(raw_return) >= 0.008:
        return "gerichtete_bewegung"
    if range_ratio <= 0.006 and direction_consistency < 0.40:
        return "rekopplungsversuch"
    return "gemischte_rohwelt"


def _raw_profile(raw_rows: list[dict[str, str]], tick: int, radius: int) -> dict[str, object]:
    rows = _raw_window(raw_rows, tick, radius)
    if not rows:
        return {
            "raw_rows": 0,
            "raw_return": 0.0,
            "range_ratio": 0.0,
            "body_ratio": 0.0,
            "direction_consistency": 0.0,
            "expansion_ratio": 0.0,
            "break_ratio": 0.0,
            "movement_class": "nicht_gekoppelt",
        }

    first_open = _safe_float(rows[0].get("open"))
    last_close = _safe_float(rows[-1].get("close"))
    price_base = max(abs(first_open), 1e-9)
    highs = [_safe_float(row.get("high")) for row in rows]
    lows = [_safe_float(row.get("low")) for row in rows]
    closes = [_safe_float(row.get("close")) for row in rows]
    bodies = [abs(_safe_float(row.get("close")) - _safe_float(row.get("open"))) for row in rows]
    ranges = [max(0.0, _safe_float(row.get("high")) - _safe_float(row.get("low"))) for row in rows]
    deltas = [closes[idx] - closes[idx - 1] for idx in range(1, len(closes))]
    pos = sum(1 for value in deltas if value > 0)
    neg = sum(1 for value in deltas if value < 0)

    direction_consistency = abs(pos - neg) / max(1, pos + neg)
    avg_range = sum(ranges) / max(1, len(ranges))
    avg_body = sum(bodies) / max(1, len(bodies))
    max_range = max(ranges) if ranges else 0.0
    expansion_ratio = max_range / max(1e-9, avg_range)
    break_ratio = avg_body / max(1e-9, avg_range)
    raw_return = (last_close - first_open) / price_base
    range_ratio = (max(highs) - min(lows)) / price_base
    body_ratio = avg_body / price_base

    return {
        "raw_rows": len(rows),
        "raw_return": raw_return,
        "range_ratio": range_ratio,
        "body_ratio": body_ratio,
        "direction_consistency": direction_consistency,
        "expansion_ratio": expansion_ratio,
        "break_ratio": break_ratio,
        "movement_class": _movement_class(
            raw_return,
            range_ratio,
            direction_consistency,
            expansion_ratio,
            break_ratio,
        ),
    }


def _build_rows(events: list[dict[str, str]], radius: int, limit: int) -> tuple[list[dict[str, object]], Counter[str]]:
    raw_cache: dict[str, list[dict[str, str]]] = {}
    skipped: Counter[str] = Counter()
    rows: list[dict[str, object]] = []

    ranked_events = sorted(
        events,
        key=lambda row: (
            -_safe_float(row.get("signal_completeness")),
            -_safe_float(row.get("current_strain")),
            str(row.get("phase_key", "")),
        ),
    )

    for event in ranked_events:
        world = str(event.get("world", "") or "")
        data_name = WORLD_DATA_MAP.get(world)
        if not data_name:
            skipped["keine_eindeutige_rohwelt"] += 1
            continue

        data_path = ROOT / "data" / data_name
        if not data_path.exists():
            skipped["csv_fehlt"] += 1
            continue

        if data_name not in raw_cache:
            raw_cache[data_name] = _load_csv(data_path)

        center_tick = int(round((_safe_int(event.get("current_start_tick")) + _safe_int(event.get("current_end_tick"))) / 2))
        profile = _raw_profile(raw_cache[data_name], center_tick, radius)
        if profile["raw_rows"] == 0:
            skipped["tick_ausserhalb_rohdatei"] += 1
            continue

        rows.append(
            {
                "phase_key": event.get("phase_key", ""),
                "phase_class": event.get("phase_class", ""),
                "window_reading": event.get("window_reading", ""),
                "world": world,
                "data_file": data_name,
                "current_start_tick": event.get("current_start_tick", ""),
                "current_end_tick": event.get("current_end_tick", ""),
                "center_tick": center_tick,
                "current_intake": event.get("current_raw_field_intake", ""),
                "current_loudness": event.get("current_auditory_loudness", ""),
                "current_sharpness": event.get("current_visual_sharpness", ""),
                "current_rekopplung": event.get("current_rekopplung", ""),
                "current_strain": event.get("current_strain", ""),
                "delta_next_rekopplung": event.get("delta_next_current_rekopplung", ""),
                "delta_next_strain": event.get("delta_next_current_strain", ""),
                **{key: round(value, 8) if isinstance(value, float) else value for key, value in profile.items()},
            }
        )
        if len(rows) >= limit:
            break
    return rows, skipped


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


def _write_markdown(path: Path, rows: list[dict[str, object]], skipped: Counter[str], events_path: Path) -> None:
    movement_counts = Counter(str(row["movement_class"]) for row in rows)
    reading_counts = Counter(str(row["window_reading"]) for row in rows)
    phase_counts = Counter(str(row["phase_key"]) for row in rows)
    world_counts = Counter(str(row["world"]) for row in rows)

    lines: list[str] = [
        "# MCM-Feldphasen Rohwelt-Fensterlupe",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Welche konkrete Rohweltbewegung steht unter den zuvor gefundenen MCM-Feldphasen-Fenstern?",
        "",
        "## Hierarchie",
        "",
        "```text",
        "Grundfrage: Feldfolge um Rand/Kipp",
        "Unterpruefung: konkrete Rohweltbewegung im gleichen Tickbereich",
        "Folgeschritt: Ton-/Rezeptorprofil mit Rohchartfenster zusammenlegen",
        "```",
        "",
        "## Eingabe",
        "",
        f"- Feldfenster: `{events_path.relative_to(ROOT)}`",
        "- Rohwelt-Zuordnung: nur eindeutig gemappte CSV-Dateien aus `data/`",
        "",
        "## Profil",
        "",
        f"- gekoppelte Rohfenster: `{len(rows)}`",
        f"- nicht gekoppelte Events: `{dict(skipped.most_common())}`",
        f"- Bewegungsarten: `{dict(movement_counts.most_common())}`",
        f"- Feldfenster-Lesarten: `{dict(reading_counts.most_common())}`",
        f"- Welten: `{dict(world_counts.most_common())}`",
        "",
        "## Phasenbezug",
        "",
    ]
    for phase, count in phase_counts.most_common(8):
        lines.append(f"- `{phase}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste gekoppelte Fenster",
            "",
            "| Phase | Welt | Tick | Feldlesart | Bewegung | Return | Range | Expansion | Richtung | Loudness | Strain | Folge |",
            "|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows[:24]:
        follow = f"reko {row['delta_next_rekopplung']}, strain {row['delta_next_strain']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["phase_key"]),
                    str(row["world"]),
                    str(row["center_tick"]),
                    str(row["window_reading"]),
                    str(row["movement_class"]),
                    _fmt(row["raw_return"]),
                    _fmt(row["range_ratio"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["current_loudness"]),
                    _fmt(row["current_strain"]),
                    follow,
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Diese Diagnose koppelt Feldfolge und Rohwelt nur dort, wo eine eindeutige Rohdatei vorhanden ist.",
            "",
            "Damit wird sichtbar, ob `lastkontakt_entlastet` eher mit gerichteter Bewegung, Bewegungsbruch, Expansion oder gemischter Rohwelt zusammenfaellt.",
            "",
            "## Grenze",
            "",
            "Viele Feldfenster stammen aus synthetischen oder historisch zusammengesetzten Welten. Diese werden hier bewusst nicht zwangsweise auf Rohdaten gemappt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird die Rohwelt-Fensterlupe bewertet: Welche Bewegungsarten tragen entlastenden Randkontakt, und welche fuehren zu neuer Randlast?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Koppelt MCM-Feldphasen-Fenster mit eindeutigen Rohweltfenstern.")
    parser.add_argument("--events", default=str(DEFAULT_EVENTS), help="Feldfenster CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    parser.add_argument("--radius", type=int, default=35, help="Rohwelt-Fensterradius um den Segmentmittelpunkt.")
    parser.add_argument("--limit", type=int, default=256, help="Maximale gekoppelte Fenster.")
    args = parser.parse_args()

    events_path = _resolve(args.events)
    out_path = _resolve(args.out)
    events = _load_csv(events_path)
    rows, skipped = _build_rows(events, args.radius, args.limit)
    csv_path = out_path.with_suffix(".csv")
    _write_csv(csv_path, rows)
    _write_markdown(out_path, rows, skipped, events_path)

    print(f"wrote {out_path}")
    print(f"wrote {csv_path}")
    print(f"coupled={len(rows)} skipped={dict(skipped)}")


if __name__ == "__main__":
    main()
