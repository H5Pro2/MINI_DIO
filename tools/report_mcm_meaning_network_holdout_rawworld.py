from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1395_HOLDOUT_FELDROLLEN_STABILITAET.csv"
OUT_CSV = befunde_root(ROOT) / "1396_HOLDOUT_ROHWELT_RUECKLESUNG.csv"
OUT_MD = befunde_root(ROOT) / "1396_HOLDOUT_ROHWELT_RUECKLESUNG.md"

REPORTS = {
    "HOLDOUT_2024_BRIDGE_TEST1": ROOT / "debug" / "1395_holdout_bridge_test1" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_2024_BRIDGE_TEST2": ROOT / "debug" / "1396_holdout_bridge_test2" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_QUIET_SOL2025": ROOT / "debug" / "1397_holdout_quiet_sol2025" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_SMOOTH_CONTROL": ROOT / "debug" / "1398_holdout_smooth_control" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_POSITIVE_EXPANSION": ROOT / "debug" / "1399_holdout_positive_expansion" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_QUIET_DRIFT": ROOT / "debug" / "1400_holdout_quiet_drift" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_MEDIUM_QUIET_DRIFT": ROOT / "debug" / "1401_holdout_medium_quiet_drift" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_NOISY_DRIFT": ROOT / "debug" / "1402_holdout_noisy_drift" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_HIGH_NOISY_DRIFT": ROOT / "debug" / "1403_holdout_high_noisy_drift" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_COMBINED_STRESS": ROOT / "debug" / "1404_holdout_combined_stress" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_HIGH_FREQUENCY_SWITCH": ROOT / "debug" / "1405_holdout_high_frequency_switch" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_FREQ25": ROOT / "debug" / "1406_holdout_freq25" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_FREQ50": ROOT / "debug" / "1407_holdout_freq50" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_FREQ75": ROOT / "debug" / "1408_holdout_freq75" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_FREQ100": ROOT / "debug" / "1409_holdout_freq100" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_RHYTHM_REGULAR": ROOT / "debug" / "1410_holdout_rhythm_regular" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_RHYTHM_BLOCK": ROOT / "debug" / "1411_holdout_rhythm_block" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_RHYTHM_IRREGULAR": ROOT / "debug" / "1412_holdout_rhythm_irregular" / "dio_mini_lauf_2" / "mini_report.json",
    "HOLDOUT_RHYTHM_WAVE": ROOT / "debug" / "1413_holdout_rhythm_wave" / "dio_mini_lauf_2" / "mini_report.json",
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _data_for_world(world: str) -> list[dict[str, str]]:
    report = json.loads(REPORTS[world].read_text(encoding="utf-8"))
    return _read_rows(ROOT / str(report["data_path"]))


def _raw_stats(rows: list[dict[str, str]]) -> dict[str, float | str]:
    if not rows:
        return {
            "raw_net_pct": 0.0,
            "raw_range_pct": 0.0,
            "raw_avg_body_pct": 0.0,
            "raw_direction_changes": 0.0,
            "raw_direction": "leer",
        }
    opens = [_float(row, "open") for row in rows]
    highs = [_float(row, "high") for row in rows]
    lows = [_float(row, "low") for row in rows]
    closes = [_float(row, "close") for row in rows]
    first = opens[0] or closes[0] or 1.0
    net_pct = (closes[-1] - first) / first * 100.0
    range_pct = (max(highs) - min(lows)) / first * 100.0
    body_pct = mean(abs(close - open_) / first * 100.0 for open_, close in zip(opens, closes))
    signs: list[int] = []
    for open_, close in zip(opens, closes):
        diff = close - open_
        if diff > 0:
            signs.append(1)
        elif diff < 0:
            signs.append(-1)
    changes = sum(1 for left, right in zip(signs, signs[1:]) if left != right)
    if net_pct > 0.25:
        direction = "steigend"
    elif net_pct < -0.25:
        direction = "fallend"
    else:
        direction = "seitwaerts"
    return {
        "raw_net_pct": net_pct,
        "raw_range_pct": range_pct,
        "raw_avg_body_pct": body_pct,
        "raw_direction_changes": float(changes),
        "raw_direction": direction,
    }


def _world_tension(stats: dict[str, float | str]) -> str:
    range_pct = float(stats["raw_range_pct"])
    changes = float(stats["raw_direction_changes"])
    if range_pct >= 4.0 and changes >= 45:
        return "weite_unruhige_spannung"
    if range_pct >= 4.0:
        return "weite_gerichtete_spannung"
    if changes >= 45:
        return "enge_unruhige_spannung"
    return "ruhige_bis_mittlere_spannung"


def main() -> None:
    role_rows = [
        row
        for row in _read_rows(IN_CSV)
        if row.get("holdout_state") in {"rolle_exakt_wiedergefunden", "rolle_als_nachbarschaft"}
    ]
    data_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, str]] = []
    for row in role_rows:
        world = row["world"]
        if world not in data_cache:
            data_cache[world] = _data_for_world(world)
        start = int(row["start_tick"])
        end = int(row["end_tick"])
        stats = _raw_stats(data_cache[world][start - 1 : end])
        out_rows.append(
            {
                "world": world,
                "start_tick": row["start_tick"],
                "end_tick": row["end_tick"],
                "nearest_role_family": row["nearest_role_family"],
                "nearest_node": row["nearest_node"],
                "nearest_similarity": row["nearest_similarity"],
                "effect": row["effect"],
                "effect_mix": row.get("effect_mix", row["effect"]),
                "world_tension": _world_tension(stats),
                "raw_direction": str(stats["raw_direction"]),
                "raw_net_pct": f"{float(stats['raw_net_pct']):.6f}",
                "raw_range_pct": f"{float(stats['raw_range_pct']):.6f}",
                "raw_avg_body_pct": f"{float(stats['raw_avg_body_pct']):.6f}",
                "raw_direction_changes": f"{float(stats['raw_direction_changes']):.0f}",
                "tone": row["tone"],
                "shift": row["shift"],
                "tension": row["tension"],
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    role_counts = Counter(row["nearest_role_family"] for row in out_rows)
    tension_counts = Counter(row["world_tension"] for row in out_rows)
    direction_counts = Counter(row["raw_direction"] for row in out_rows)

    lines = [
        "# 1396 - Holdout Rohwelt-Ruecklesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die starken Holdout-Nachbarschaften aus `1395` in die konkrete Rohwelt zurueck.",
        "",
        "## Befund",
        "",
        f"- starke Holdout-Fenster: `{len(out_rows)}`",
        f"- Rollen: `{', '.join(f'{key}:{value}' for key, value in role_counts.most_common())}`",
        f"- Weltspannungen: `{', '.join(f'{key}:{value}' for key, value in tension_counts.most_common())}`",
        f"- Richtungen: `{', '.join(f'{key}:{value}' for key, value in direction_counts.most_common())}`",
        "",
        "## Fenster",
        "",
        *[
            f"- `{row['world']}:{row['start_tick']}-{row['end_tick']}` -> `{row['nearest_role_family']}`, Spannung `{row['world_tension']}`, Richtung `{row['raw_direction']}`, Range `{row['raw_range_pct']}`, Tonshift `{row['shift']}`, Wirkung `{row['effect_mix']}`"
            for row in out_rows
        ],
        "",
        "## Lesung",
        "",
        "Die Holdout-Beruehrungen liegen nicht in chaotischer Kippung, sondern in stabiler Innenwirkung.",
        "Die beruehrten Rollen treten dort auf, wo die Rohwelt als Spannungs- oder Unruhebereich gelesen wird.",
        "Der ruhige SOL-Holdout ist nicht spannungslos: er zeigt kleinere Range, aber hohe Richtungswechsel. Dadurch entsteht `enge_unruhige_spannung` statt reiner Ruhe.",
        "Der synthetisch glatte Kontrolllauf bleibt dagegen bei ruhiger bis mittlerer Spannung und beruehrt `offene_nachbarschaftsrolle`.",
        "Die positive Expansion beruehrt sowohl Spannungsnaehe als auch gerichtete Spannungsrolle, erzwingt aber noch keine neue Mischklasse.",
        "Damit wird `weite_weltspannungsnaehe` als Name fraglich: die Rolle scheint eher unruhige Spannungsnaehe zu tragen, nicht zwingend nur grosse Range.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
