from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "326_EPISODENROLLEN_WELTMERKMALE_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    strain = _float(row.get("mcm_strain_quality"))
    rekopplung = _float(row.get("mcm_rekopplung_quality"))
    sensory = _float(row.get("mcm_sensory_coupling"))

    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    if rekopplung >= 0.58 and strain <= 0.26 and sensory >= 0.70:
        return "rekopplungsnaehe"
    if strain >= 0.28:
        return "spannungsrand_kippnaehe"
    return "unbestimmt"


def _world_features(candles: list[dict[str, str]], tick: int) -> dict[str, float]:
    index = max(0, min(len(candles) - 1, tick - 1))
    current = candles[index]
    previous = candles[index - 1] if index > 0 else current
    close = _float(current.get("close"))
    prev_close = _float(previous.get("close"))
    high = _float(current.get("high"))
    low = _float(current.get("low"))
    volume = _float(current.get("volume"))
    prev_volume = _float(previous.get("volume"))

    raw_return = ((close - prev_close) / prev_close) if prev_close else 0.0
    candle_range = ((high - low) / close) if close else 0.0
    volume_change = abs((volume - prev_volume) / prev_volume) if prev_volume else 0.0

    prev_prev = candles[index - 2] if index > 1 else previous
    prev_return = ((prev_close - _float(prev_prev.get("close"))) / _float(prev_prev.get("close"))) if _float(prev_prev.get("close")) else 0.0
    direction_change = 1.0 if raw_return * prev_return < 0 else 0.0

    window_start = max(0, index - 12)
    window = candles[window_start : index + 1]
    first_close = _float(window[0].get("close")) if window else close
    local_drift = ((close - first_close) / first_close) if first_close else 0.0

    return {
        "return": raw_return,
        "abs_return": abs(raw_return),
        "range": candle_range,
        "volume_change": volume_change,
        "direction_change": direction_change,
        "local_drift_12": local_drift,
    }


def _avg(rows: list[dict[str, float]], key: str) -> float:
    values = [float(row.get(key, 0.0) or 0.0) for row in rows]
    return fmean(values) if values else 0.0


def _longest_streak(roles: list[str], role: str) -> int:
    longest = 0
    current = 0
    for item in roles:
        if item == role:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest


def _summarize_world(name: str, episodes_path: Path, data_path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    episodes = _load_csv(episodes_path)
    candles = _load_csv(data_path)
    enriched: list[dict[str, object]] = []
    for row in episodes:
        tick = _int(row.get("tick"))
        features = _world_features(candles, tick)
        role = _role(row)
        enriched.append(
            {
                "world": name,
                "tick": tick,
                "role": role,
                "effect_class": row.get("passive_mcm_effect_class", "-") or "-",
                "symbol_family": row.get("symbol_family", "-") or "-",
                "mcm_preview": row.get("mcm_field_episode_preview_symbol", "-") or "-",
                "rekopplung": _float(row.get("mcm_rekopplung_quality")),
                "carry": _float(row.get("mcm_carry_quality")),
                "strain": _float(row.get("mcm_strain_quality")),
                "sensory": _float(row.get("mcm_sensory_coupling")),
                "visual_gap": _float(row.get("mcm_visual_field_gap")),
                "hearing_gap": _float(row.get("mcm_hearing_field_gap")),
                **features,
            }
        )

    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in enriched:
        grouped[str(row["role"])].append(row)

    summaries: list[dict[str, object]] = []
    total = max(1, len(enriched))
    roles = [str(row["role"]) for row in enriched]
    for role, rows in sorted(grouped.items()):
        summaries.append(
            {
                "world": name,
                "role": role,
                "count": len(rows),
                "share": len(rows) / total,
                "avg_rekopplung": _avg(rows, "rekopplung"),
                "avg_carry": _avg(rows, "carry"),
                "avg_strain": _avg(rows, "strain"),
                "avg_sensory": _avg(rows, "sensory"),
                "avg_abs_return": _avg(rows, "abs_return"),
                "avg_range": _avg(rows, "range"),
                "avg_volume_change": _avg(rows, "volume_change"),
                "direction_change_ratio": _avg(rows, "direction_change"),
                "avg_local_drift_12": _avg(rows, "local_drift_12"),
                "avg_visual_gap": _avg(rows, "visual_gap"),
                "avg_hearing_gap": _avg(rows, "hearing_gap"),
                "longest_streak": _longest_streak(roles, role),
            }
        )

    world_summary = {
        "world": name,
        "episodes": len(enriched),
        "dominant_role": max(grouped.items(), key=lambda item: len(item[1]))[0] if grouped else "-",
        "zentrum_share": len(grouped.get("zentrum_stabil", [])) / total,
        "offen_share": len(grouped.get("offene_variante", [])) / total,
        "rand_share": len(grouped.get("spannungsrand_kippnaehe", [])) / total,
        "avg_abs_return": _avg(enriched, "abs_return"),
        "direction_change_ratio": _avg(enriched, "direction_change"),
        "avg_local_drift_12": _avg(enriched, "local_drift_12"),
        "avg_rekopplung": _avg(enriched, "rekopplung"),
    }
    return summaries, world_summary


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "role",
        "count",
        "share",
        "avg_rekopplung",
        "avg_carry",
        "avg_strain",
        "avg_sensory",
        "avg_abs_return",
        "avg_range",
        "avg_volume_change",
        "direction_change_ratio",
        "avg_local_drift_12",
        "avg_visual_gap",
        "avg_hearing_gap",
        "longest_streak",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key)
                    for key in fields
                }
            )


def _write_md(rows: list[dict[str, object]], worlds: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)
    lines = [
        "# Episodenrollen Gegen Weltmerkmale",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest innerhalb stabiler Topologie, welche lokalen Weltmerkmale mit Zentrum, offener Variante und Rand/Kippnaehe zusammenfallen.",
        "Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Warum rekoppelt eine Stresswelt zentrumsnah, waehrend eine andere offener wird?",
        "2. Unterpruefung: Rollenanteile gegen Return, Range, Volumenwechsel, Richtungswechsel und lokalen Drift legen.",
        "3. Folgeschritt: Lokale Abschnitte mit offener Variante und zentrumsnaher Rekopplung getrennt lesen.",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Richtungswechsel | lokaler Drift | Rekopplung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in worlds:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["episodes"]),
                    _fmt(float(row["zentrum_share"])),
                    _fmt(float(row["offen_share"])),
                    _fmt(float(row["rand_share"])),
                    _fmt(float(row["direction_change_ratio"])),
                    _fmt(float(row["avg_local_drift_12"])),
                    _fmt(float(row["avg_rekopplung"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Rollenwerte",
            "",
            "| Welt | Rolle | Anteil | Rekopplung | Strain | Sinneskopplung | abs Return | Range | Richtungswechsel | lokaler Drift | laengste Serie |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["role"]),
                    _fmt(float(row["share"])),
                    _fmt(float(row["avg_rekopplung"])),
                    _fmt(float(row["avg_strain"])),
                    _fmt(float(row["avg_sensory"])),
                    _fmt(float(row["avg_abs_return"]), 6),
                    _fmt(float(row["avg_range"]), 6),
                    _fmt(float(row["direction_change_ratio"])),
                    _fmt(float(row["avg_local_drift_12"])),
                    str(row["longest_streak"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Diese Datei ist eine Messmatrix. Die fachliche Deutung muss aus den Rollenwerten abgeleitet werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes werden die auffaelligen Unterschiede zwischen `NEG_STRESS_2023` und `NEG_STRESS_2024` verdichtet.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=3, metavar=("NAME", "EPISODES_CSV", "DATA_CSV"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    world_rows: list[dict[str, object]] = []
    for name, episodes_text, data_text in args.world:
        rows, summary = _summarize_world(name, _resolve(episodes_text), _resolve(data_text))
        all_rows.extend(rows)
        world_rows.append(summary)

    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(all_rows, world_rows, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")


if __name__ == "__main__":
    main()
