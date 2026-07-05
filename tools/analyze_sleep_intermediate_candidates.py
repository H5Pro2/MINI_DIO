from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _rel(path: Path) -> str:
    path = path.resolve()
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _load_summary(label: str) -> dict:
    path = ROOT / "debug" / "real_sleep_real" / label / "real_sleep_real_summary.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _combination_state_by_pair(summary: dict) -> dict[str, dict]:
    result: dict[str, dict] = {}
    followup = dict(summary.get("sleep_reorganization_followup", {}) or {})
    for item in followup.get("combination_traces", []) or []:
        if not isinstance(item, dict):
            continue
        pair = str(item.get("pair_key", "") or "")
        if pair:
            result[pair] = dict(item)
    return result


def _state_rank(state: str) -> int:
    if state == "sleep_combination_fully_reactivated":
        return 2
    if state == "sleep_combination_partly_reactivated":
        return 1
    return 0


def _candidate_state(same: str, quiet: str, stress: str, mosaic: str) -> str:
    if _state_rank(same) <= 0:
        return "not_recalled_in_origin"
    if _state_rank(quiet) > 0 and _state_rank(stress) <= 0 and _state_rank(mosaic) <= 0:
        return "quiet_intermediate_candidate"
    if _state_rank(quiet) > 0 and (_state_rank(stress) > 0 or _state_rank(mosaic) > 0):
        return "broad_intermediate_candidate"
    if _state_rank(quiet) <= 0 and _state_rank(stress) <= 0 and _state_rank(mosaic) <= 0:
        return "origin_bound_combination"
    return "mixed_candidate"


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "pair_key",
        "candidate_state",
        "same_state",
        "quiet_state",
        "stress_state",
        "mosaic_state",
        "same_delta",
        "quiet_delta",
        "stress_delta",
        "mosaic_delta",
        "avg_pair_sleep_resonance",
        "co_touch_ratio",
        "combination_state",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: dict) -> None:
    rows = summary["rows"]
    counts = summary["candidate_counts"]
    lines = [
        "# Sleep-Zwischenrollen Kandidaten",
        "",
        f"Stand: {summary['created_at']}",
        "",
        "## Zweck",
        "",
        "Diese Auswertung prueft, ob weiche Sleep-Kombinationen als Zwischenrollen-Kandidaten lesbar sind.",
        "",
        "Eine Zwischenrolle ist hier noch keine neue autonome Bedeutung. Gemeint ist nur:",
        "",
        "```text",
        "Eine Offline-Kombination kommt bei gleicher Welt voll zurueck",
        "und findet in einer verwandten Folgewelt zumindest teilweise Anschluss.",
        "```",
        "",
        "Die Auswertung bleibt passiv: keine Handlung, keine Richtung, kein Gate.",
        "",
        "## Zaehler",
        "",
    ]
    for key, value in sorted(counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Kandidaten",
            "",
            "| Kombination | Zustand | gleiche Welt | Ruhewelt | Stress | Mosaik |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['pair_key']}` | `{row['candidate_state']}` | `{row['same_state']}` | "
            f"`{row['quiet_state']}` | `{row['stress_state']}` | `{row['mosaic_state']}` |"
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            summary["interpretation"],
            "",
            "## Grenze",
            "",
            "Diese Kandidaten sind keine Handlung und keine sichere neue Semantik. Sie sind eine passive Messspur fuer Offline-Kombinationen, die spaeter teilweise wieder Weltnaehe finden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte ein eigener passiver Speicher fuer solche Zwischenrollen-Kandidaten vorbereitet werden. Dieser Speicher darf nur dokumentieren, ob Kandidaten ueber mehrere Ketten stabil bleiben, driftend werden oder verschwinden.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def analyze(
    same_label: str,
    quiet_label: str,
    stress_label: str,
    mosaic_label: str,
    out_path: Path,
) -> dict:
    same = _combination_state_by_pair(_load_summary(same_label))
    quiet = _combination_state_by_pair(_load_summary(quiet_label))
    stress = _combination_state_by_pair(_load_summary(stress_label))
    mosaic = _combination_state_by_pair(_load_summary(mosaic_label))
    all_pairs = sorted(set(same) | set(quiet) | set(stress) | set(mosaic))
    rows = []
    for pair in all_pairs:
        same_item = same.get(pair, {})
        quiet_item = quiet.get(pair, {})
        stress_item = stress.get(pair, {})
        mosaic_item = mosaic.get(pair, {})
        same_state = str(same_item.get("followup_state", "missing") or "missing")
        quiet_state = str(quiet_item.get("followup_state", "missing") or "missing")
        stress_state = str(stress_item.get("followup_state", "missing") or "missing")
        mosaic_state = str(mosaic_item.get("followup_state", "missing") or "missing")
        rows.append(
            {
                "pair_key": pair,
                "candidate_state": _candidate_state(same_state, quiet_state, stress_state, mosaic_state),
                "same_state": same_state,
                "quiet_state": quiet_state,
                "stress_state": stress_state,
                "mosaic_state": mosaic_state,
                "same_delta": "|".join(str(item) for item in same_item.get("role_seen_deltas", []) or []),
                "quiet_delta": "|".join(str(item) for item in quiet_item.get("role_seen_deltas", []) or []),
                "stress_delta": "|".join(str(item) for item in stress_item.get("role_seen_deltas", []) or []),
                "mosaic_delta": "|".join(str(item) for item in mosaic_item.get("role_seen_deltas", []) or []),
                "avg_pair_sleep_resonance": quiet_item.get(
                    "avg_pair_sleep_resonance",
                    same_item.get("avg_pair_sleep_resonance", 0.0),
                ),
                "co_touch_ratio": quiet_item.get("co_touch_ratio", same_item.get("co_touch_ratio", 0.0)),
                "combination_state": quiet_item.get("combination_state", same_item.get("combination_state", "")),
            }
        )
    counts = dict(sorted({row["candidate_state"]: 0 for row in rows}.items()))
    for row in rows:
        counts[row["candidate_state"]] = counts.get(row["candidate_state"], 0) + 1
    candidate_count = counts.get("quiet_intermediate_candidate", 0) + counts.get("broad_intermediate_candidate", 0)
    if candidate_count:
        interpretation = (
            "Die weiche Sleep-Ausbreitung enthaelt Kandidaten fuer Zwischenrollen: Kombinationen, "
            "die in der Ursprungswelt voll ruecklesbar sind und in der ruhigen Folgewelt mindestens teilweise anschliessen. "
            "Stress und Mosaik nehmen diese Kandidaten aktuell nicht auf."
        )
    else:
        interpretation = (
            "In dieser Auswertung wurden keine Zwischenrollen-Kandidaten gefunden. "
            "Die weiche Sleep-Ausbreitung blieb entweder nur lokal oder zerfiel in den Folgewelten."
        )
    summary = {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "labels": {
            "same": same_label,
            "quiet": quiet_label,
            "stress": stress_label,
            "mosaic": mosaic_label,
        },
        "rows": rows,
        "candidate_counts": counts,
        "interpretation": interpretation,
        "passive_only": 1,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
    }
    out_path = out_path if out_path.is_absolute() else ROOT / out_path
    _write_csv(out_path.with_suffix(".csv"), rows)
    _write_markdown(out_path, summary)
    debug_path = ROOT / "debug" / "sleep_intermediate_candidates" / "sleep_intermediate_candidates.json"
    debug_path.parent.mkdir(parents=True, exist_ok=True)
    debug_path.write_text(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze passive sleep intermediate candidates.")
    parser.add_argument("--same-label", default="sol2024_soft_sleep_combo_same")
    parser.add_argument("--quiet-label", default="sol2024_soft_sleep_combo_quiet2025")
    parser.add_argument("--stress-label", default="sol2024_soft_sleep_combo_stress2024")
    parser.add_argument("--mosaic-label", default="sol2024_soft_sleep_combo_mosaic1525")
    parser.add_argument("--out", default="docs/befunde/1562_SLEEP_ZWISCHENROLLEN_KANDIDATEN.md")
    args = parser.parse_args()
    summary = analyze(
        same_label=str(args.same_label),
        quiet_label=str(args.quiet_label),
        stress_label=str(args.stress_label),
        mosaic_label=str(args.mosaic_label),
        out_path=Path(args.out),
    )
    print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
