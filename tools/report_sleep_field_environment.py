"""Run passive sleep-field environment diagnostics from stored MCM episodes."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from mini_dio.config import Config
from mini_dio.dio_syntax import make_syntax_symbol
from mini_dio.mcm_neuron import MiniMCMField
from mini_dio.sleep_field_environment import build_sleep_environment_senses, load_mcm_episode_roles


def _mean(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _mean_abs(values: list[float]) -> float:
    return _mean([abs(float(item or 0.0)) for item in values])


def _afterimage_abs(field: MiniMCMField) -> float:
    return _mean_abs([float(neuron.afterimage) for neuron in field.neurons])


def _sleep_state(afterimage_abs: float, signature_abs: float, active_count: int) -> str:
    if active_count <= 0 and afterimage_abs < 0.012:
        return "sleep_quiet"
    if signature_abs < 0.035 and afterimage_abs < 0.060:
        return "sleep_rekopplung"
    if afterimage_abs >= 0.110:
        return "sleep_loaded"
    return "sleep_resonance"


def run_environment(memory_path: Path, ticks: int, intensity: float, role_limit: int, max_active_roles: int) -> tuple[dict, list[dict]]:
    roles = load_mcm_episode_roles(memory_path, limit=role_limit)
    field = MiniMCMField(neuron_count=getattr(Config, "DIO_MINI_MCM_NEURON_COUNT", 12))
    rows: list[dict] = []
    symbol_counter: Counter[str] = Counter()
    state_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    previous_signature = 0.0
    for tick in range(1, max(1, int(ticks)) + 1):
        senses, active_roles = build_sleep_environment_senses(
            roles,
            current_signature=previous_signature,
            tick=tick,
            intensity=intensity,
            max_active_roles=max_active_roles,
        )
        field_state = field.step(senses)
        signature = float(field_state["signature"])
        afterimage = _afterimage_abs(field)
        symbol = make_syntax_symbol(senses, signature)
        symbol_counter[symbol] += 1
        for role in active_roles:
            role_counter[str(role["symbol"])] += 1
        state = _sleep_state(afterimage_abs=afterimage, signature_abs=abs(signature), active_count=len(active_roles))
        state_counter[state] += 1
        rows.append(
            {
                "tick": tick,
                "signature": f"{signature:.9f}",
                "afterimage_abs": f"{afterimage:.9f}",
                "sleep_state": state,
                "sleep_symbol": symbol,
                "active_role_count": len(active_roles),
                "active_roles": "|".join(str(role["symbol"]) for role in active_roles[:5]),
                "active_role_resonance": "|".join(f"{float(role['resonance']):.6f}" for role in active_roles[:5]),
                "mcm_coherence": f"{float(senses['mcm_feldwirkung']['mcm_coherence']):.9f}",
                "mcm_tension": f"{float(senses['mcm_feldwirkung']['mcm_tension']):.9f}",
                "mcm_asymmetry": f"{float(senses['mcm_feldwirkung']['mcm_asymmetry']):.9f}",
            }
        )
        previous_signature = signature
    summary = {
        "memory_path": str(memory_path),
        "ticks": len(rows),
        "role_count": len(roles),
        "intensity": float(intensity),
        "role_limit": int(role_limit),
        "max_active_roles": int(max_active_roles),
        "sleep_unique_symbols": len(symbol_counter),
        "sleep_top_symbol": symbol_counter.most_common(1)[0][0] if symbol_counter else "-",
        "sleep_top_symbol_count": symbol_counter.most_common(1)[0][1] if symbol_counter else 0,
        "state_counts": dict(state_counter),
        "top_active_roles": dict(role_counter.most_common(8)),
        "avg_afterimage_abs": _mean([float(row["afterimage_abs"]) for row in rows]),
        "final_afterimage_abs": float(rows[-1]["afterimage_abs"]) if rows else 0.0,
        "avg_signature_abs": _mean([abs(float(row["signature"])) for row in rows]),
        "final_signature_abs": abs(float(rows[-1]["signature"])) if rows else 0.0,
    }
    return summary, rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Passive sleep field environment from MCM episode memory.")
    parser.add_argument("--memory-json", required=True)
    parser.add_argument("--ticks", type=int, default=300)
    parser.add_argument("--intensity", type=float, default=0.42)
    parser.add_argument("--role-limit", type=int, default=24)
    parser.add_argument("--max-active-roles", type=int, default=5)
    parser.add_argument("--out-dir", default="debug/sleep_field_environment")
    args = parser.parse_args()

    root = Path.cwd()
    memory_path = Path(args.memory_json)
    if not memory_path.is_absolute():
        memory_path = root / memory_path
    out_dir = root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    summary, rows = run_environment(
        memory_path=memory_path,
        ticks=args.ticks,
        intensity=args.intensity,
        role_limit=args.role_limit,
        max_active_roles=args.max_active_roles,
    )
    (out_dir / "sleep_field_environment_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    if rows:
        with (out_dir / "sleep_field_environment_ticks.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
