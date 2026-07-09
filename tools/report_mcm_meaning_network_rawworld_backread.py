from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1390_BEDEUTUNGSNETZ_FOLGEWELTEN.csv"
BASE_NODES = befunde_root(ROOT) / "1389_BEDEUTUNGSNETZ_KNOTEN.csv"
OUT_CSV = befunde_root(ROOT) / "1393_BEDEUTUNGSNETZ_ROHWELT_RUECKLESUNG.csv"
OUT_MD = befunde_root(ROOT) / "1393_BEDEUTUNGSNETZ_ROHWELT_RUECKLESUNG.md"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _data_path_from_episode_source(source: str) -> Path:
    episode_path = ROOT / source
    report_path = episode_path.parent / "mini_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    return ROOT / str(report["data_path"])


def _strong_nodes() -> set[str]:
    rows = _read_csv(BASE_NODES)
    return {
        row.get("meaning_node", "")
        for row in rows
        if row.get("node_state", "") in {"tragende_bedeutungsnaehe", "verdichtete_bedeutungsnaehe"}
    }


def _raw_stats(raw_rows: list[dict[str, str]]) -> dict[str, float | str]:
    if not raw_rows:
        return {
            "raw_net_pct": 0.0,
            "raw_range_pct": 0.0,
            "raw_avg_body_pct": 0.0,
            "raw_avg_volume": 0.0,
            "raw_direction_changes": 0.0,
            "raw_direction": "flach",
        }
    opens = [_float(row, "open") for row in raw_rows]
    highs = [_float(row, "high") for row in raw_rows]
    lows = [_float(row, "low") for row in raw_rows]
    closes = [_float(row, "close") for row in raw_rows]
    volumes = [_float(row, "volume") for row in raw_rows]
    first_open = opens[0] or closes[0] or 1.0
    net_pct = ((closes[-1] - first_open) / first_open) * 100.0 if first_open else 0.0
    range_pct = ((max(highs) - min(lows)) / first_open) * 100.0 if first_open else 0.0
    body_pct = mean(abs(close - open_) / first_open * 100.0 for open_, close in zip(opens, closes)) if first_open else 0.0
    signs: list[int] = []
    for open_, close in zip(opens, closes):
        diff = close - open_
        if diff > 0:
            signs.append(1)
        elif diff < 0:
            signs.append(-1)
        else:
            signs.append(0)
    compact = [sign for sign in signs if sign != 0]
    direction_changes = sum(1 for left, right in zip(compact, compact[1:]) if left != right)
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
        "raw_avg_volume": mean(volumes) if volumes else 0.0,
        "raw_direction_changes": float(direction_changes),
        "raw_direction": direction,
    }


def _classify_world_tension(stats: dict[str, float | str]) -> str:
    range_pct = float(stats["raw_range_pct"])
    changes = float(stats["raw_direction_changes"])
    body_pct = float(stats["raw_avg_body_pct"])
    if range_pct >= 2.0 and changes >= 35:
        return "weite_unruhige_weltspannung"
    if range_pct >= 2.0:
        return "weite_gerichtete_weltspannung"
    if changes >= 35:
        return "enge_unruhige_weltspannung"
    if body_pct <= 0.035:
        return "ruhige_feinspannung"
    return "mittlere_weltspannung"


def main() -> None:
    rows = _read_csv(IN_CSV)
    target_nodes = _strong_nodes()
    data_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, str]] = []

    for row in rows:
        node = row.get("exact_old_node") or row.get("nearest_old_node")
        if node not in target_nodes:
            continue
        source = row.get("source", "")
        if not source:
            continue
        if source not in data_cache:
            data_cache[source] = _read_csv(_data_path_from_episode_source(source))
        data_rows = data_cache[source]
        start = max(1, int(row.get("start_tick", "1") or 1))
        end = max(start, int(row.get("end_tick", str(start)) or start))
        raw_slice = data_rows[start - 1 : end]
        stats = _raw_stats(raw_slice)
        out_rows.append(
            {
                "world": row.get("world", ""),
                "old_node": node,
                "old_state": row.get("exact_old_state") or row.get("nearest_old_state") or "",
                "follow_state": row.get("follow_state", ""),
                "start_tick": str(start),
                "end_tick": str(end),
                "mischlinien_signature": row.get("mischlinien_signature", ""),
                "world_tension_class": _classify_world_tension(stats),
                "raw_direction": str(stats["raw_direction"]),
                "raw_net_pct": f"{float(stats['raw_net_pct']):.6f}",
                "raw_range_pct": f"{float(stats['raw_range_pct']):.6f}",
                "raw_avg_body_pct": f"{float(stats['raw_avg_body_pct']):.6f}",
                "raw_avg_volume": f"{float(stats['raw_avg_volume']):.6f}",
                "raw_direction_changes": f"{float(stats['raw_direction_changes']):.0f}",
                "hoeren_energy_tone": row.get("hoeren_energy_tone", ""),
                "hoeren_energy_shift": row.get("hoeren_energy_shift", ""),
                "sehen_form_stability": row.get("sehen_form_stability", ""),
                "mcm_feldwirkung_mcm_tension": row.get("mcm_feldwirkung_mcm_tension", ""),
                "perception_adapted_field_intake_pressure": row.get("perception_adapted_field_intake_pressure", ""),
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    by_node: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in out_rows:
        by_node[row["old_node"]].append(row)

    node_lines: list[str] = []
    for node, node_rows in sorted(by_node.items(), key=lambda item: len(item[1]), reverse=True):
        tensions = Counter(row["world_tension_class"] for row in node_rows)
        directions = Counter(row["raw_direction"] for row in node_rows)
        states = Counter(row["follow_state"] for row in node_rows)
        avg_range = mean(float(row["raw_range_pct"]) for row in node_rows)
        avg_changes = mean(float(row["raw_direction_changes"]) for row in node_rows)
        node_lines.append(
            f"- `{node}`: Fenster `{len(node_rows)}`, Weltspannung `{', '.join(f'{key}:{value}' for key, value in tensions.most_common())}`, Richtung `{', '.join(f'{key}:{value}' for key, value in directions.most_common())}`, Folgezustand `{', '.join(f'{key}:{value}' for key, value in states.most_common())}`, avg_range `{avg_range:.4f}`, avg_wechsel `{avg_changes:.2f}`"
        )

    tension_counts = Counter(row["world_tension_class"] for row in out_rows)
    world_counts = Counter(row["world"] for row in out_rows)

    lines = [
        "# 1393 - Bedeutungsnetz Rohwelt-Ruecklesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest dominante Bedeutungsnetz-Knoten aus `1390` in die konkrete Rohwelt zurueck.",
        "Damit wird sichtbar, welche Weltspannung hinter stabiler Wiederkehr oder Nachbarschaftsdrift liegt.",
        "",
        "Die Diagnose bleibt passiv. Sie beschreibt Weltkontakt und Feldnaehe, keine Handlung.",
        "",
        "## Befund",
        "",
        f"- untersuchte Fenster: `{len(out_rows)}`",
        f"- Welten: `{', '.join(f'{key}:{value}' for key, value in world_counts.most_common())}`",
        f"- Weltspannungen: `{', '.join(f'{key}:{value}' for key, value in tension_counts.most_common())}`",
        "",
        "## Knoten Ruecklesung",
        "",
        *node_lines,
        "",
        "## Lesung",
        "",
        "`5495a55c` wird nicht durch eine einzelne starre Rohform getragen.",
        "Der Knoten bleibt als Feldnaehe erhalten, waehrend die Folgewelten vor allem Ton-/Aufnahmevarianten erzeugen.",
        "Das spricht fuer eine Bedeutungsnaehe, die ueber Weltkontakt erhalten bleibt, aber in der konkreten Sinnesaufnahme variiert.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollten aus den starken Knoten Feldrollen-Familien gebildet werden: ruhige Naehe, gerichtete Spannung, weite Spannung und offene Nachbarschaft.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
