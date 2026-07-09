from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.config import Config
from mini_dio.sleep_memory_reorganization import build_sleep_reorganization_memory
from tools.report_sleep_field_environment import run_environment


def _rel(path: Path) -> str:
    path = path.resolve()
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")


def _run_mini(data_path: Path, memory_path: Path, debug_root: Path, sense_mode: str) -> None:
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        _rel(data_path),
        "--runs",
        "1",
        "--memory",
        _rel(memory_path),
        "--debug-root",
        _rel(debug_root),
        "--sense-mode",
        str(sense_mode),
        "--reset-memory",
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()


def _pair_keys(sleep_memory: dict) -> list[str]:
    return [str(item.get("pair_key", "") or "") for item in sleep_memory.get("combination_traces", []) or [] if item]


def _write_phase_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "phase",
        "activation_floor",
        "active_role_set_count",
        "touched_role_count",
        "combination_trace_count",
        "shared_with_phase_1",
        "new_vs_phase_1",
        "missing_vs_phase_1",
        "jaccard_vs_phase_1",
        "sleep_top_symbol",
        "sleep_state",
        "phase_reading",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: dict) -> None:
    lines = [
        "# Sleep-Kombinationsphasen Scan",
        "",
        f"Stand: {summary['created_at']}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob Sleep-Kombinationen bei veraenderter Sleep-Naehe stabil bleiben,",
        "sich teilen oder neue Kombinationsinseln bilden.",
        "",
        "Wichtig: Die Pruefung ist passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine Motorik.",
        "",
        "## Welt",
        "",
        f"- Daten: `{summary['data_path']}`",
        f"- Basis-Memory: `{summary['base_memory']}`",
        "",
        "## Phasen",
        "",
        "| Phase | activation_floor | Rollen | Kombinationen | geteilt mit Phase 1 | neu gegen Phase 1 | fehlt gegen Phase 1 | Jaccard | Lesung |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in summary["phase_rows"]:
        lines.append(
            "| {phase} | {activation_floor} | {touched_role_count} | {combination_trace_count} | "
            "{shared_with_phase_1} | {new_vs_phase_1} | {missing_vs_phase_1} | {jaccard_vs_phase_1} | {phase_reading} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            summary["interpretation"],
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run_scan(
    data_path: Path,
    label: str,
    floors: list[float],
    ticks: int,
    intensity: float,
    role_limit: int,
    max_active_roles: int,
    debug_root: Path,
    memory_root: Path,
    out_path: Path,
    sense_mode: str,
) -> dict:
    data_path = data_path if data_path.is_absolute() else ROOT / data_path
    debug_root = debug_root if debug_root.is_absolute() else ROOT / debug_root
    memory_root = memory_root if memory_root.is_absolute() else ROOT / memory_root
    out_path = out_path if out_path.is_absolute() else ROOT / out_path
    run_debug = debug_root / label
    run_memory = memory_root / label
    if run_debug.exists():
        shutil.rmtree(run_debug)
    if run_memory.exists():
        shutil.rmtree(run_memory)
    run_debug.mkdir(parents=True, exist_ok=True)
    run_memory.mkdir(parents=True, exist_ok=True)
    base_memory = run_memory / "base_memory.json"
    _run_mini(data_path, base_memory, run_debug / "real_a", sense_mode=sense_mode)
    base = _load_json(base_memory)
    phase_rows: list[dict] = []
    phase_payloads: list[dict] = []
    phase_1_pairs: set[str] | None = None
    for index, floor in enumerate(floors, start=1):
        phase_dir = run_debug / f"sleep_phase_{index}"
        phase_dir.mkdir(parents=True, exist_ok=True)
        sleep_summary, sleep_rows = run_environment(
            memory_path=base_memory,
            ticks=ticks,
            intensity=intensity,
            role_limit=role_limit,
            max_active_roles=max_active_roles,
            activation_floor=float(floor),
        )
        sleep_memory = build_sleep_reorganization_memory(base, sleep_summary, sleep_rows)
        pairs = set(_pair_keys(sleep_memory))
        if phase_1_pairs is None:
            phase_1_pairs = set(pairs)
        shared = pairs & phase_1_pairs
        new_pairs = pairs - phase_1_pairs
        missing_pairs = phase_1_pairs - pairs
        union = pairs | phase_1_pairs
        jaccard = 1.0 if not union else round(len(shared) / len(union), 6)
        states = Counter(str(row.get("sleep_state", "") or "-") for row in sleep_rows)
        if index == 1:
            phase_reading = "referenz_phase"
        elif new_pairs and missing_pairs:
            phase_reading = "sleep_combination_reorganized"
        elif new_pairs:
            phase_reading = "sleep_combination_expanded"
        elif missing_pairs:
            phase_reading = "sleep_combination_narrowed"
        else:
            phase_reading = "sleep_combination_stable"
        row = {
            "phase": index,
            "activation_floor": float(floor),
            "active_role_set_count": int(sleep_summary.get("active_role_set_count", 0) or 0),
            "touched_role_count": int(sleep_memory.get("touched_role_count", 0) or 0),
            "combination_trace_count": int(sleep_memory.get("combination_trace_count", 0) or 0),
            "shared_with_phase_1": len(shared),
            "new_vs_phase_1": len(new_pairs),
            "missing_vs_phase_1": len(missing_pairs),
            "jaccard_vs_phase_1": jaccard,
            "sleep_top_symbol": str(sleep_summary.get("sleep_top_symbol", "") or ""),
            "sleep_state": ",".join(f"{key}:{value}" for key, value in sorted(states.items())),
            "phase_reading": phase_reading,
        }
        phase_rows.append(row)
        payload = {
            "phase": index,
            "activation_floor": float(floor),
            "sleep_summary": sleep_summary,
            "sleep_reorganization_memory": sleep_memory,
            "pairs": sorted(pairs),
            "new_vs_phase_1": sorted(new_pairs),
            "missing_vs_phase_1": sorted(missing_pairs),
            "phase_reading": phase_reading,
        }
        phase_payloads.append(payload)
        _write_json(phase_dir / "sleep_phase_summary.json", payload)
    expansion_phases = [row for row in phase_rows if row["new_vs_phase_1"] > 0]
    if expansion_phases:
        interpretation = (
            "Die Sleep-Kombinationsnaehe ist nicht starr. Weichere oder veraenderte Naehe kann neue "
            "Kombinationsinseln sichtbar machen, ohne dass daraus Handlung entsteht."
        )
    else:
        interpretation = (
            "Die Sleep-Kombinationsnaehe blieb in dieser Phasenpruefung stabil. Es wurden keine neuen "
            "Kombinationsinseln gegen die Referenzphase sichtbar."
        )
    summary = {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_path": _rel(data_path),
        "base_memory": _rel(base_memory),
        "label": label,
        "ticks": int(ticks),
        "intensity": float(intensity),
        "floors": [float(item) for item in floors],
        "phase_rows": phase_rows,
        "phase_payloads": phase_payloads,
        "interpretation": interpretation,
        "passive_only": 1,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
    }
    _write_json(run_debug / "sleep_combination_phase_scan.json", summary)
    _write_phase_csv(out_path.with_suffix(".csv"), phase_rows)
    _write_markdown(out_path, summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan passive sleep combination phases.")
    parser.add_argument("--data", default=getattr(Config, "DIO_MINI_CONTROLLED_WORLD_PATH"))
    parser.add_argument("--label", default="sleep_combination_phase_scan")
    parser.add_argument("--floors", default="0.75,0.65,0.45")
    parser.add_argument("--ticks", type=int, default=300)
    parser.add_argument("--intensity", type=float, default=0.42)
    parser.add_argument("--role-limit", type=int, default=24)
    parser.add_argument("--max-active-roles", type=int, default=5)
    parser.add_argument("--debug-root", default="debug/sleep_combination_phase_scan")
    parser.add_argument("--memory-root", default="memory/sleep_combination_phase_scan")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1501-1750/1554_SLEEP_KOMBINATIONS_PHASEN_SCAN.md")
    parser.add_argument(
        "--sense-mode",
        choices=("fixed", "world_relative"),
        default=getattr(Config, "DIO_MINI_SENSE_MODE", "world_relative"),
    )
    args = parser.parse_args()
    floors = [float(item.strip()) for item in str(args.floors).split(",") if item.strip()]
    summary = run_scan(
        data_path=Path(args.data),
        label=str(args.label),
        floors=floors,
        ticks=args.ticks,
        intensity=args.intensity,
        role_limit=args.role_limit,
        max_active_roles=args.max_active_roles,
        debug_root=Path(args.debug_root),
        memory_root=Path(args.memory_root),
        out_path=Path(args.out),
        sense_mode=args.sense_mode,
    )
    print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
