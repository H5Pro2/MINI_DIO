from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


TARGET_PATHS = {
    "active_recoupling -> open_surface -> open_surface": "rekopplung_oeffnet",
    "open_surface -> active_recoupling -> active_recoupling": "oberflaeche_rekoppelt",
    "open_surface -> open_surface -> active_recoupling": "oberflaeche_rekoppelt_spaet",
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _raw_window_stats(rows: list[dict[str, str]]) -> dict[str, float | str]:
    if not rows:
        return {
            "raw_net_pct": 0.0,
            "raw_range_pct": 0.0,
            "raw_avg_body_pct": 0.0,
            "raw_direction_changes": 0.0,
            "raw_direction": "offen",
        }
    opens = [_safe_float(row.get("open")) for row in rows]
    highs = [_safe_float(row.get("high")) for row in rows]
    lows = [_safe_float(row.get("low")) for row in rows]
    closes = [_safe_float(row.get("close")) for row in rows]
    base = opens[0] or closes[0] or 1.0
    signs: list[int] = []
    for open_, close in zip(opens, closes):
        diff = close - open_
        if diff > 0:
            signs.append(1)
        elif diff < 0:
            signs.append(-1)
    changes = sum(1 for left, right in zip(signs, signs[1:]) if left != right)
    net_pct = ((closes[-1] - opens[0]) / base) * 100.0 if base else 0.0
    range_pct = ((max(highs) - min(lows)) / base) * 100.0 if base else 0.0
    avg_body_pct = mean(abs(close - open_) / base * 100.0 for open_, close in zip(opens, closes)) if base else 0.0
    if net_pct > 0.18:
        direction = "steigend"
    elif net_pct < -0.18:
        direction = "fallend"
    else:
        direction = "seitwaerts"
    return {
        "raw_net_pct": net_pct,
        "raw_range_pct": range_pct,
        "raw_avg_body_pct": avg_body_pct,
        "raw_direction_changes": float(changes),
        "raw_direction": direction,
    }


def _world_lauf_paths(debug_root: Path) -> list[Path]:
    return sorted(path for path in debug_root.glob("dio_mini_lauf_*/episodes.csv") if path.exists())


def _data_path_for_episode(episodes_path: Path) -> Path:
    report_path = episodes_path.parent / "mini_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    data_path = Path(str(report["data_path"]))
    if not data_path.is_absolute():
        data_path = Path.cwd() / data_path
    return data_path


def _label_window(raw_stats: dict[str, float | str]) -> str:
    range_pct = float(raw_stats["raw_range_pct"])
    changes = float(raw_stats["raw_direction_changes"])
    body = float(raw_stats["raw_avg_body_pct"])
    direction = str(raw_stats["raw_direction"])
    if range_pct >= 0.85 and changes >= 10:
        return f"weite_unruhige_{direction}"
    if range_pct >= 0.85:
        return f"weite_gerichtete_{direction}"
    if changes >= 10:
        return f"enge_unruhige_{direction}"
    if body <= 0.025:
        return f"feine_ruhespur_{direction}"
    return f"mittlere_spur_{direction}"


def _event_row(
    *,
    symbol: str,
    target_group: str,
    chain: str,
    episodes_path: Path,
    episode_row: dict[str, str],
    raw_rows: list[dict[str, str]],
    lookback: int,
) -> dict[str, object]:
    tick = int(_safe_float(episode_row.get("tick")))
    start = max(0, tick - lookback - 1)
    end = max(start, tick - 1)
    raw_stats = _raw_window_stats(raw_rows[start:end])
    run_path = episodes_path.parent.resolve()
    try:
        run_text = str(run_path.relative_to(Path.cwd().resolve()))
    except ValueError:
        run_text = str(run_path)
    return {
        "preview_symbol": symbol,
        "target_group": target_group,
        "chain": chain,
        "world": episode_row.get("passive_world_label", "-"),
        "run": run_text,
        "tick": tick,
        "window_start_tick": start + 1,
        "window_end_tick": end,
        "window_label": _label_window(raw_stats),
        "raw_direction": raw_stats["raw_direction"],
        "raw_net_pct": raw_stats["raw_net_pct"],
        "raw_range_pct": raw_stats["raw_range_pct"],
        "raw_avg_body_pct": raw_stats["raw_avg_body_pct"],
        "raw_direction_changes": raw_stats["raw_direction_changes"],
        "sehen_form_stability": _safe_float(episode_row.get("sehen_form_stability")),
        "sehen_form_change": _safe_float(episode_row.get("sehen_form_change")),
        "sehen_form_flow": _safe_float(episode_row.get("sehen_form_flow")),
        "hoeren_energy_tone": _safe_float(episode_row.get("hoeren_energy_tone")),
        "hoeren_energy_shift": _safe_float(episode_row.get("hoeren_energy_shift")),
        "perception_auditory_loudness": _safe_float(episode_row.get("perception_auditory_loudness")),
        "perception_visual_sharpness": _safe_float(episode_row.get("perception_visual_sharpness")),
        "mcm_carry_quality": _safe_float(episode_row.get("mcm_carry_quality")),
        "mcm_strain_quality": _safe_float(episode_row.get("mcm_strain_quality")),
        "mcm_rekopplung_quality": _safe_float(episode_row.get("mcm_rekopplung_quality")),
        "mcm_field_phase_signature_depth": _safe_float(episode_row.get("mcm_field_phase_signature_depth")),
        "mcm_field_phase_signature_drift": _safe_float(episode_row.get("mcm_field_phase_signature_drift")),
    }


def _collect_events(
    shift_rows: list[dict[str, str]],
    debug_roots: dict[str, Path],
    lookback: int,
    max_events_per_symbol_chain: int,
) -> list[dict[str, object]]:
    wanted: dict[str, str] = {}
    for row in shift_rows:
        path = row.get("function_path", "")
        if path in TARGET_PATHS:
            wanted[row["preview_symbol"]] = TARGET_PATHS[path]

    events: list[dict[str, object]] = []
    for chain, debug_root in debug_roots.items():
        for episodes_path in _world_lauf_paths(debug_root):
            raw_rows = _load_csv(_data_path_for_episode(episodes_path))
            seen: Counter[str] = Counter()
            for episode_row in _load_csv(episodes_path):
                symbol = episode_row.get("mcm_field_episode_preview_symbol", "")
                if symbol not in wanted:
                    continue
                if seen[symbol] >= max_events_per_symbol_chain:
                    continue
                seen[symbol] += 1
                events.append(
                    _event_row(
                        symbol=symbol,
                        target_group=wanted[symbol],
                        chain=chain,
                        episodes_path=episodes_path,
                        episode_row=episode_row,
                        raw_rows=raw_rows,
                        lookback=lookback,
                    )
                )
    return events


def _summarize(events: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for event in events:
        groups[(str(event["target_group"]), str(event["chain"]))].append(event)
    rows: list[dict[str, object]] = []
    for (target_group, chain), items in sorted(groups.items()):
        window_counts = Counter(str(item["window_label"]) for item in items)
        direction_counts = Counter(str(item["raw_direction"]) for item in items)
        symbol_counts = Counter(str(item["preview_symbol"]) for item in items)
        rows.append(
            {
                "target_group": target_group,
                "chain": chain,
                "events": len(items),
                "symbols": ";".join(f"{key}:{value}" for key, value in symbol_counts.most_common()),
                "window_labels": ";".join(f"{key}:{value}" for key, value in window_counts.most_common()),
                "directions": ";".join(f"{key}:{value}" for key, value in direction_counts.most_common()),
                "avg_raw_net_pct": _avg([float(item["raw_net_pct"]) for item in items]),
                "avg_raw_range_pct": _avg([float(item["raw_range_pct"]) for item in items]),
                "avg_raw_body_pct": _avg([float(item["raw_avg_body_pct"]) for item in items]),
                "avg_raw_direction_changes": _avg([float(item["raw_direction_changes"]) for item in items]),
                "avg_visual_stability": _avg([float(item["sehen_form_stability"]) for item in items]),
                "avg_visual_change": _avg([float(item["sehen_form_change"]) for item in items]),
                "avg_hearing_tone": _avg([float(item["hoeren_energy_tone"]) for item in items]),
                "avg_hearing_shift_abs": _avg([abs(float(item["hoeren_energy_shift"])) for item in items]),
                "avg_loudness": _avg([float(item["perception_auditory_loudness"]) for item in items]),
                "avg_mcm_carry": _avg([float(item["mcm_carry_quality"]) for item in items]),
                "avg_mcm_strain": _avg([float(item["mcm_strain_quality"]) for item in items]),
                "avg_mcm_rekopplung": _avg([float(item["mcm_rekopplung_quality"]) for item in items]),
                "avg_phase_depth": _avg([float(item["mcm_field_phase_signature_depth"]) for item in items]),
            }
        )
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["target_group"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: list[dict[str, object]], events: list[dict[str, object]], lookback: int) -> None:
    group_counts = Counter(str(row["target_group"]) for row in events)
    chain_counts = Counter(str(row["chain"]) for row in events)
    lines = [
        "# 2034 - Feldfunktionswechsel Rohweltfenster-Lupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose betrachtet konkrete Rohweltfenster vor Feldfunktionswechseln.",
        "",
        "Fokus:",
        "",
        "- `active_recoupling -> open_surface`: wann rekoppelnde Signaturen öffnen",
        "- `open_surface -> active_recoupling`: wann offene Oberflächen rekoppeln",
        "",
        "Die Diagnose bleibt passiv. Sie beschreibt nur Rohwelt, Sinneswerte und MCM-Feldwerte um die Signaturen herum.",
        "",
        "## Übersicht",
        "",
        f"- Rohfenster-Lookback: `{lookback}` Ticks",
        f"- untersuchte Ereignisse: `{len(events)}`",
        f"- Gruppen: `{', '.join(f'{key}:{value}' for key, value in group_counts.most_common())}`",
        f"- Ketten: `{', '.join(f'{key}:{value}' for key, value in chain_counts.most_common())}`",
        "",
        "## Gruppenzusammenfassung",
        "",
        "| Gruppe | Kette | Ereignisse | Fenster | Richtung | Range | Wechsel | Sehen stabil/change | Hören Ton/Shift | MCM carry/strain/rekopplung |",
        "|---|---|---:|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            "| "
            f"`{row['target_group']}` | "
            f"`{row['chain']}` | "
            f"{row['events']} | "
            f"`{row['window_labels']}` | "
            f"`{row['directions']}` | "
            f"{float(row['avg_raw_range_pct']):.4f} | "
            f"{float(row['avg_raw_direction_changes']):.2f} | "
            f"{float(row['avg_visual_stability']):.3f}/{float(row['avg_visual_change']):.3f} | "
            f"{float(row['avg_hearing_tone']):.3f}/{float(row['avg_hearing_shift_abs']):.3f} | "
            f"{float(row['avg_mcm_carry']):.3f}/{float(row['avg_mcm_strain']):.3f}/{float(row['avg_mcm_rekopplung']):.3f} |"
        )

    lines.extend(["", "## Einzelereignisse", ""])
    lines.append("| Signatur | Gruppe | Kette | Welt | Tick | Fenster | Richtung | Range | MCM |")
    lines.append("|---|---|---|---|---:|---|---|---:|---:|")
    for event in sorted(events, key=lambda item: (str(item["target_group"]), str(item["chain"]), str(item["preview_symbol"]), int(item["tick"])))[:80]:
        lines.append(
            "| "
            f"`{event['preview_symbol']}` | "
            f"`{event['target_group']}` | "
            f"`{event['chain']}` | "
            f"`{event['world']}` | "
            f"{event['tick']} | "
            f"`{event['window_label']}` | "
            f"`{event['raw_direction']}` | "
            f"{float(event['raw_range_pct']):.4f} | "
            f"{float(event['mcm_carry_quality']):.3f}/{float(event['mcm_strain_quality']):.3f}/{float(event['mcm_rekopplung_quality']):.3f} |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Rollenwechsel erscheinen nicht als reiner Symbolwechsel.",
            "",
            "Sie liegen in konkreten Rohweltfenstern mit unterscheidbaren Richtungs-, Wechsel- und Sinnesprofilen.",
            "",
            "`open_surface -> active_recoupling` wird damit als mögliche Rekopplung offener Oberflächen lesbar. `active_recoupling -> open_surface` wirkt dagegen wie ein Öffnen zuvor rekoppelnder Signaturen unter anderer Weltspannung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Lupe mit längeren Lookbacks und einem direkten Vergleich der Rohfensterklassen wiederholt werden. Entscheidend ist, ob Öffnung und Rekopplung schon vor dem Signaturauftreten unterschiedliche Weltprofile zeigen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shift-report", default="docs/befunde/2032_FELDFUNKTION_WECHSEL_REALWELT_KERN.csv")
    parser.add_argument("--long-debug", default="debug/2026_field_phase_signature_long_real_chain")
    parser.add_argument("--multi-debug", default="debug/2029_field_phase_signature_multiasset_real_chain")
    parser.add_argument("--lookback", type=int, default=48)
    parser.add_argument("--max-events-per-symbol-chain", type=int, default=40)
    parser.add_argument("--out-prefix", default="2034_FELDFUNKTIONSWECHSEL_ROHWELTFENSTER_LUPE")
    args = parser.parse_args()

    shift_rows = _load_csv(Path(args.shift_report))
    debug_roots = {
        "long_btc_sol": Path(args.long_debug),
        "multiasset": Path(args.multi_debug),
    }
    events = _collect_events(shift_rows, debug_roots, args.lookback, args.max_events_per_symbol_chain)
    summary = _summarize(events)

    out_dir = Path("docs") / "befunde"
    _write_csv(out_dir / f"{args.out_prefix}.events.csv", events)
    _write_csv(out_dir / f"{args.out_prefix}.summary.csv", summary)
    _write_markdown(out_dir / f"{args.out_prefix}.md", summary, events, args.lookback)

    print(f"events={len(events)}")
    print(f"summary_rows={len(summary)}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
