from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.config import Config
from mini_dio.sleep_memory_reorganization import apply_sleep_reorganization_to_memory_file
from tools.report_sleep_field_environment import run_environment as run_sleep_environment


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


def _top_names(items: list[dict], key: str, limit: int = 8) -> list[str]:
    result: list[str] = []
    for item in (items or [])[:limit]:
        value = item.get(key)
        if value:
            result.append(str(value))
    return result


def _overlap(left: list[str], right: list[str]) -> dict:
    left_set = set(left)
    right_set = set(right)
    shared = sorted(left_set & right_set)
    union = left_set | right_set
    return {
        "shared": shared,
        "ratio": round(len(shared) / max(1, len(union)), 6),
    }


def _memory_key_count(memory: dict, key: str) -> int:
    value = memory.get(key, {})
    if isinstance(value, dict):
        return len(value)
    if isinstance(value, list):
        return len(value)
    return 0


def _summarize_memory(memory_path: Path) -> dict:
    memory = _load_json(memory_path)
    field_memory = memory.get("mcm_field_episode_memory", {})
    role_counter: dict[str, int] = {}
    if isinstance(field_memory, dict):
        for entry in field_memory.values():
            if not isinstance(entry, dict):
                continue
            role = str(entry.get("episode_state", entry.get("role", entry.get("effect_class", "-"))) or "-")
            role_counter[role] = role_counter.get(role, 0) + 1
    return {
        "path": _rel(memory_path),
        "runs": int(memory.get("runs", 0) or 0),
        "symbols": _memory_key_count(memory, "symbols"),
        "families": _memory_key_count(memory, "families"),
        "episode_memory": _memory_key_count(memory, "episode_memory"),
        "mcm_field_episode_memory": _memory_key_count(memory, "mcm_field_episode_memory"),
        "passive_inner_field_maps": _memory_key_count(memory, "passive_inner_field_maps"),
        "passive_mcm_role_network": _memory_key_count(memory, "passive_mcm_role_network"),
        "passive_sleep_reorganization_history": _memory_key_count(memory, "passive_sleep_reorganization_history"),
        "passive_sleep_reorganization_state": str(
            dict(memory.get("passive_sleep_reorganization_memory", {}) or {}).get("reorganization_state", "")
            or ""
        ),
        "field_roles": dict(sorted(role_counter.items())),
    }


def _run_mini(data_path: Path, memory_path: Path, debug_root: Path, runs: int, reset_memory: bool, sense_mode: str) -> None:
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        _rel(data_path),
        "--runs",
        str(max(1, int(runs))),
        "--memory",
        _rel(memory_path),
        "--debug-root",
        _rel(debug_root),
        "--sense-mode",
        str(sense_mode),
    ]
    if reset_memory:
        command.append("--reset-memory")
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()


def _report_path(debug_root: Path, run_index: int) -> Path:
    return debug_root / f"dio_mini_lauf_{run_index}" / "mini_report.json"


def _compare_reports(real_a: dict, real_b: dict) -> dict:
    a_symbols = _top_names(real_a.get("top_symbols", []) or [], "symbol")
    b_symbols = _top_names(real_b.get("top_symbols", []) or [], "symbol")
    a_families = _top_names(real_a.get("family_top", []) or [], "family")
    b_families = _top_names(real_b.get("family_top", []) or [], "family")
    metrics = [
        "candles",
        "episodes",
        "unique_symbols",
        "episode_memory_written",
        "mcm_field_episode_written",
        "avg_mcm_carry_quality",
        "avg_mcm_rekopplung_quality",
        "avg_mcm_strain_quality",
        "avg_mcm_sensory_coupling",
        "avg_mini_afterimage",
        "avg_mini_neuro_load",
        "avg_mini_neuro_balance",
    ]
    values = {}
    for metric in metrics:
        a_value = real_a.get(metric, 0)
        b_value = real_b.get(metric, 0)
        if isinstance(a_value, (int, float)) and isinstance(b_value, (int, float)):
            values[metric] = {
                "real_a": round(float(a_value), 6),
                "real_b_after_sleep": round(float(b_value), 6),
                "delta": round(float(b_value) - float(a_value), 6),
            }
        else:
            values[metric] = {"real_a": a_value, "real_b_after_sleep": b_value, "delta": ""}
    return {
        "metrics": values,
        "top_symbol_overlap": _overlap(a_symbols, b_symbols),
        "top_family_overlap": _overlap(a_families, b_families),
        "real_a_effect_classes": real_a.get("passive_mcm_effect_classes", {}),
        "real_b_effect_classes": real_b.get("passive_mcm_effect_classes", {}),
        "real_a_episode_states": real_a.get("episode_memory_states", {}),
        "real_b_episode_states": real_b.get("episode_memory_states", {}),
    }


def _write_compare_csv(path: Path, comparison: dict) -> None:
    rows = []
    for metric, values in comparison.get("metrics", {}).items():
        rows.append(
            {
                "metric": metric,
                "real_a": values.get("real_a", ""),
                "real_b_after_sleep": values.get("real_b_after_sleep", ""),
                "delta": values.get("delta", ""),
            }
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "real_a", "real_b_after_sleep", "delta"])
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, summary: dict) -> None:
    comparison = summary["comparison"]
    metrics = comparison["metrics"]
    sleep = summary["sleep_summary"]
    title = (
        "Real-Sleep-Real Passive Reorganisation"
        if bool(summary.get("sleep_memory_reorganization_written", False))
        else "Real-Sleep-Real Baseline"
    )
    lines = [
        f"# {title}",
        "",
        f"Stand: {summary['created_at']}",
        "",
        "## Zweck",
        "",
        "Diese Kette prueft, was sich zwischen zwei Real-Welt-Beruehrungen veraendert,",
        "wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt. Real-B kann dieselbe oder eine andere Welt sein.",
        "",
        (
            "Wichtig: In der Baseline schreibt die Schlafphase noch keine Memory um."
            if not bool(summary.get("sleep_memory_reorganization_written", False))
            else "Wichtig: In diesem Lauf schreibt die Schlafphase eine passive Reorganisationsspur."
        ),
        (
            "Sie erzeugt nur Diagnoseartefakte. Dadurch bleibt sichtbar, was Wiederholung mit gleicher Memory leistet,"
            if not bool(summary.get("sleep_memory_reorganization_written", False))
            else "Diese Spur markiert nur beruehrte bestehende Rollen; sie erzeugt keine neue Weltbedeutung,"
        ),
        (
            "bevor spaeter echte Schlaf-Reorganisation erlaubt wird."
            if not bool(summary.get("sleep_memory_reorganization_written", False))
            else "keine Richtung, kein Gate und keine Handlung."
        ),
        "",
        "## Kette",
        "",
        f"- Real A Welt: `{summary['data_path']}`",
        f"- Real B Welt: `{summary['follow_data_path']}`",
        f"- gleiche Welt: `{bool(summary.get('same_world_followup', False))}`",
        f"- Real A Memory: `{summary['memory_a_real']}`",
        f"- Sleep Diagnose: `{summary['sleep_debug_root']}`",
        f"- Memory nach Sleep: `{summary['memory_after_sleep']}`",
        f"- Real B Memory: `{summary['memory_b_real']}`",
        "",
        "## Real A -> Real B",
        "",
        f"- Episoden: `{metrics['episodes']['real_a']}` -> `{metrics['episodes']['real_b_after_sleep']}`",
        f"- Unique Syntax: `{metrics['unique_symbols']['real_a']}` -> `{metrics['unique_symbols']['real_b_after_sleep']}`",
        f"- geschriebene Feldepisoden: `{metrics['mcm_field_episode_written']['real_a']}` -> `{metrics['mcm_field_episode_written']['real_b_after_sleep']}`",
        f"- MCM-Tragqualitaet: `{metrics['avg_mcm_carry_quality']['real_a']}` -> `{metrics['avg_mcm_carry_quality']['real_b_after_sleep']}`",
        f"- MCM-Rekopplung: `{metrics['avg_mcm_rekopplung_quality']['real_a']}` -> `{metrics['avg_mcm_rekopplung_quality']['real_b_after_sleep']}`",
        f"- MCM-Sinneskopplung: `{metrics['avg_mcm_sensory_coupling']['real_a']}` -> `{metrics['avg_mcm_sensory_coupling']['real_b_after_sleep']}`",
        f"- Top-Syntax-Ueberlappung: `{comparison['top_symbol_overlap']['ratio']}`",
        f"- Top-Familien-Ueberlappung: `{comparison['top_family_overlap']['ratio']}`",
        "",
        "## Sleep Diagnose",
        "",
        f"- Sleep Ticks: `{sleep.get('ticks', 0)}`",
        f"- Rollen im Sleep-Pool: `{sleep.get('role_count', 0)}`",
        f"- aktive Rollensets: `{sleep.get('active_role_set_count', 0)}`",
        f"- Sleep Unique Syntax: `{sleep.get('sleep_unique_symbols', 0)}`",
        f"- mittlerer Nachhall: `{round(float(sleep.get('avg_afterimage_abs', 0.0) or 0.0), 6)}`",
        f"- passive Sleep-Memory geschrieben: `{bool(summary.get('sleep_memory_reorganization_written', False))}`",
        "",
        "Sleep-Zustaende:",
        "",
    ]
    for key, value in sorted((sleep.get("state_counts", {}) or {}).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            (
                "Diese Baseline ist noch kein Nachweis fuer schlafbedingtes Lernen."
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "Diese Stufe ist noch kein Nachweis fuer veraendertes Weltverhalten durch Schlaf."
            ),
            (
                "Sie trennt aber die drei Ebenen: erste Weltberuehrung, entkoppelte Feldaktivitaet, zweite Weltberuehrung."
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "Sie zeigt aber, dass Sleep bestehende Rollen passiv markieren kann, ohne Welt-Symbole neu zu erfinden."
            ),
            (
                "Damit ist der naechste Schritt sauber messbar: Schlaf darf spaeter begrenzt Memory-Reorganisation schreiben,"
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "Damit ist der naechste Schritt sauber messbar: eine spaetere Leseschicht darf pruefen,"
            ),
            (
                "und die zweite Weltberuehrung kann gegen diese Baseline verglichen werden."
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "ob diese passive Reorganisationsspur bei erneutem Weltkontakt wieder auftaucht oder neutral bleibt."
            ),
            "",
            "## Wie es weitergeht",
            "",
            (
                "Als naechstes wird dieselbe Kette mit aktiver, aber klar begrenzter Sleep-Memory-Reorganisation vorbereitet."
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "Als naechstes wird die passive Sleep-Reorganisationsspur gegen weitere Welten geprueft."
            ),
            (
                "Dann pruefen wir, ob im Schlaf beruehrte Rollen im zweiten Real-Lauf stabiler, klarer oder driftender wieder auftauchen."
                if not bool(summary.get("sleep_memory_reorganization_written", False))
                else "Dann wird sichtbar, ob sie nur eine lokale Markierung bleibt oder als wiederkehrende Innenfeldspur tragfaehig ist."
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def run_chain(
    data_path: Path,
    follow_data_path: Path | None,
    label: str,
    debug_root: Path,
    memory_root: Path,
    out_path: Path,
    ticks: int,
    intensity: float,
    role_limit: int,
    max_active_roles: int,
    activation_floor: float,
    sense_mode: str,
    write_sleep_memory: bool,
) -> dict:
    data_path = data_path if data_path.is_absolute() else ROOT / data_path
    if follow_data_path is None:
        follow_data_path = data_path
    follow_data_path = follow_data_path if follow_data_path.is_absolute() else ROOT / follow_data_path
    debug_root = debug_root if debug_root.is_absolute() else ROOT / debug_root
    memory_root = memory_root if memory_root.is_absolute() else ROOT / memory_root
    out_path = out_path if out_path.is_absolute() else ROOT / out_path

    run_debug_root = debug_root / label
    run_memory_root = memory_root / label
    real_a_debug = run_debug_root / "real_a"
    sleep_debug = run_debug_root / "sleep"
    real_b_debug = run_debug_root / "real_b"
    memory_a = run_memory_root / "memory_A_real_run.json"
    memory_after_sleep = run_memory_root / "memory_A_after_sleep.json"
    memory_b = run_memory_root / "memory_B_real_run_after_sleep.json"

    if run_debug_root.exists():
        shutil.rmtree(run_debug_root)
    run_debug_root.mkdir(parents=True, exist_ok=True)
    run_memory_root.mkdir(parents=True, exist_ok=True)
    for memory_file in (memory_a, memory_after_sleep, memory_b):
        if memory_file.exists():
            memory_file.unlink()

    _run_mini(data_path, memory_a, real_a_debug, runs=1, reset_memory=True, sense_mode=sense_mode)
    real_a_report = _load_json(_report_path(real_a_debug, 1))
    shutil.copy2(memory_a, memory_after_sleep)

    sleep_summary, sleep_rows = run_sleep_environment(
        memory_path=memory_after_sleep,
        ticks=ticks,
        intensity=intensity,
        role_limit=role_limit,
        max_active_roles=max_active_roles,
        activation_floor=activation_floor,
    )
    sleep_debug.mkdir(parents=True, exist_ok=True)
    _write_json(sleep_debug / "sleep_field_environment_summary.json", sleep_summary)
    if sleep_rows:
        with (sleep_debug / "sleep_field_environment_ticks.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(sleep_rows[0].keys()))
            writer.writeheader()
            writer.writerows(sleep_rows)
    sleep_reorganization_memory = {}
    if write_sleep_memory:
        sleep_reorganization_memory = apply_sleep_reorganization_to_memory_file(
            memory_after_sleep,
            sleep_summary=sleep_summary,
            sleep_rows=sleep_rows,
        )
        _write_json(sleep_debug / "sleep_reorganization_memory.json", sleep_reorganization_memory)

    shutil.copy2(memory_after_sleep, memory_b)
    _run_mini(follow_data_path, memory_b, real_b_debug, runs=1, reset_memory=False, sense_mode=sense_mode)
    real_b_report = _load_json(_report_path(real_b_debug, 2))

    comparison = _compare_reports(real_a_report, real_b_report)
    summary = {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_path": _rel(data_path),
        "follow_data_path": _rel(follow_data_path),
        "same_world_followup": _rel(data_path) == _rel(follow_data_path),
        "label": label,
        "sense_mode": sense_mode,
        "sleep_is_diagnostic_only": not bool(write_sleep_memory),
        "sleep_memory_reorganization_written": bool(write_sleep_memory),
        "memory_a_real": _rel(memory_a),
        "memory_after_sleep": _rel(memory_after_sleep),
        "memory_b_real": _rel(memory_b),
        "real_a_debug_root": _rel(real_a_debug),
        "sleep_debug_root": _rel(sleep_debug),
        "real_b_debug_root": _rel(real_b_debug),
        "memory_a_summary": _summarize_memory(memory_a),
        "memory_after_sleep_summary": _summarize_memory(memory_after_sleep),
        "memory_b_summary": _summarize_memory(memory_b),
        "sleep_summary": sleep_summary,
        "sleep_reorganization_memory": sleep_reorganization_memory,
        "comparison": comparison,
    }
    _write_json(run_debug_root / "real_sleep_real_summary.json", summary)
    _write_compare_csv(run_debug_root / "real_sleep_real_compare.csv", comparison)
    _write_compare_csv(out_path.with_suffix(".csv"), comparison)
    _write_markdown(out_path, summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Real-Sleep-Real baseline for MINI_DIO.")
    parser.add_argument("--data", default=getattr(Config, "DIO_MINI_CONTROLLED_WORLD_PATH"))
    parser.add_argument("--follow-data", default="")
    parser.add_argument("--label", default="real_sleep_real_baseline")
    parser.add_argument("--debug-root", default="debug/real_sleep_real")
    parser.add_argument("--memory-root", default="memory/real_sleep_real")
    parser.add_argument("--out", default="docs/befunde/1541_REAL_SLEEP_REAL_BASELINE.md")
    parser.add_argument("--ticks", type=int, default=300)
    parser.add_argument("--intensity", type=float, default=0.42)
    parser.add_argument("--role-limit", type=int, default=24)
    parser.add_argument("--max-active-roles", type=int, default=5)
    parser.add_argument("--activation-floor", type=float, default=0.65)
    parser.add_argument("--write-sleep-memory", action="store_true")
    parser.add_argument(
        "--sense-mode",
        choices=("fixed", "world_relative"),
        default=getattr(Config, "DIO_MINI_SENSE_MODE", "world_relative"),
    )
    args = parser.parse_args()
    summary = run_chain(
        data_path=Path(args.data),
        follow_data_path=Path(args.follow_data) if args.follow_data else None,
        label=str(args.label),
        debug_root=Path(args.debug_root),
        memory_root=Path(args.memory_root),
        out_path=Path(args.out),
        ticks=args.ticks,
        intensity=args.intensity,
        role_limit=args.role_limit,
        max_active_roles=args.max_active_roles,
        activation_floor=args.activation_floor,
        sense_mode=args.sense_mode,
        write_sleep_memory=bool(args.write_sleep_memory),
    )
    print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
