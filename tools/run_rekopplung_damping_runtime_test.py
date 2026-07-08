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

DEFAULT_WORLDS = {
    "smooth_control": "data/kontrolliert_1398_smooth_sol2025_1000_5m.csv",
    "noisy_drift": "data/synthetic_1402_noisy_drift_1000_5m.csv",
    "null_shuffle": "data/synthetic_1526_null_shuffle_order_2400_5m.csv",
    "null_random": "data/synthetic_1527_null_random_sign_2400_5m.csv",
}


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: object, digits: int = 4) -> str:
    return f"{_float(value):.{digits}f}"


def _mean(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _source_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def _parse_factors(text: str) -> list[float]:
    factors: list[float] = []
    for part in str(text or "").split(","):
        part = part.strip()
        if not part:
            continue
        factors.append(max(0.0, min(2.0, float(part))))
    if 1.0 not in factors:
        factors.append(1.0)
    return sorted(set(factors), reverse=True)


def _parse_worlds(items: list[str] | None) -> dict[str, str]:
    if not items:
        return dict(DEFAULT_WORLDS)
    worlds: dict[str, str] = {}
    for item in items:
        if "=" in item:
            label, path = item.split("=", 1)
        else:
            path = item
            label = Path(item).stem
        worlds[label.strip()] = path.strip()
    return worlds


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0]


def _run_one(label: str, world_path: Path, factor: float, debug_root: Path, memory_root: Path) -> tuple[dict, Path]:
    run_label = f"{label}_factor_{str(factor).replace('.', 'p')}"
    run_debug = debug_root / run_label
    run_memory = memory_root / f"{run_label}.json"
    report_path = run_debug / "dio_mini_lauf_1" / "mini_report.json"
    episodes_path = run_debug / "dio_mini_lauf_1" / "episodes.csv"
    if report_path.exists() and episodes_path.exists():
        report = json.loads(report_path.read_text(encoding="utf-8"))
        return report, episodes_path
    if run_debug.exists():
        shutil.rmtree(run_debug)
    if run_memory.exists():
        run_memory.unlink()
    run_debug.mkdir(parents=True, exist_ok=True)
    run_memory.parent.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        _source_label(world_path),
        "--runs",
        "1",
        "--reset-memory",
        "--memory",
        _source_label(run_memory),
        "--debug-root",
        _source_label(run_debug),
        "--sense-mode",
        "world_relative",
        "--mcm-rekopplung-factor",
        str(factor),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()
    report = json.loads(report_path.read_text(encoding="utf-8"))
    return report, episodes_path


def _summarize_episode_rows(episode_path: Path) -> dict[str, object]:
    rows = _read_csv(episode_path)
    role_counts = Counter(str(row.get("passive_mcm_effect_class", "") or "-") for row in rows)
    state_counts = Counter(str(row.get("episode_state", "") or "-") for row in rows)
    families = Counter(str(row.get("symbol_family", "") or "-") for row in rows if str(row.get("symbol_family", "") or "-") != "-")
    return {
        "episodes": len(rows),
        "dominant_effect_class": _dominant(role_counts),
        "dominant_episode_state": _dominant(state_counts),
        "top_family_count": families.most_common(1)[0][1] if families else 0,
        "unique_families": len(families),
    }


def _row(label: str, world_path: Path, factor: float, report: dict, episode_summary: dict) -> dict[str, object]:
    return {
        "world": label,
        "source": _source_label(world_path),
        "rekopplung_factor": round(factor, 4),
        "candles": int(report.get("candles", 0) or 0),
        "unique_symbols": int(report.get("unique_symbols", 0) or 0),
        "episodes": int(episode_summary.get("episodes", 0) or 0),
        "dominant_effect_class": episode_summary.get("dominant_effect_class", "-"),
        "dominant_episode_state": episode_summary.get("dominant_episode_state", "-"),
        "unique_episode_families": int(episode_summary.get("unique_families", 0) or 0),
        "top_family_count": int(episode_summary.get("top_family_count", 0) or 0),
        "avg_mcm_carry_quality": round(_float(report.get("avg_mcm_carry_quality")), 6),
        "avg_mcm_strain_quality": round(_float(report.get("avg_mcm_strain_quality")), 6),
        "avg_mcm_rekopplung_quality": round(_float(report.get("avg_mcm_rekopplung_quality")), 6),
        "avg_mcm_adaptive_rekopplung_quality": round(_float(report.get("avg_mcm_adaptive_rekopplung_quality")), 6),
        "avg_mcm_sensory_coupling": round(_float(report.get("avg_mcm_sensory_coupling")), 6),
        "avg_mini_afterimage": round(_float(report.get("avg_mini_afterimage")), 6),
        "avg_mini_temporal_trust_support": round(_float(report.get("avg_mini_temporal_trust_support")), 6),
        "avg_mini_temporal_caution_support": round(_float(report.get("avg_mini_temporal_caution_support")), 6),
    }


def _baseline(rows: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(row["world"]): row for row in rows if _float(row["rekopplung_factor"]) == 1.0}


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], factors: list[float], title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    base = _baseline(rows)
    lowest = min(factors)
    low_rows = [row for row in rows if _float(row["rekopplung_factor"]) == lowest]
    avg_low_rekopplung = _mean([_float(row["avg_mcm_rekopplung_quality"]) for row in low_rows])
    avg_low_symbols = _mean([_float(row["unique_symbols"]) for row in low_rows])
    avg_low_families = _mean([_float(row["unique_episode_families"]) for row in low_rows])

    lines = [
        f"# {title}",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?",
        "",
        "## Aufbau",
        "",
        "- jeder Faktor laeuft mit frischer Memory",
        "- Standardfaktor `1.0` bleibt Referenz",
        "- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt",
        "- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut",
        "",
        "## Gesamtbefund",
        "",
        f"- Faktoren: `{', '.join(_fmt(item, 2) for item in factors)}`",
        f"- mittlere Rekopplung bei staerkster Daempfung: `{_fmt(avg_low_rekopplung, 6)}`",
        f"- mittlere Unique-Syntax bei staerkster Daempfung: `{_fmt(avg_low_symbols, 2)}`",
        f"- mittlere Episodenfamilien bei staerkster Daempfung: `{_fmt(avg_low_families, 2)}`",
        "",
        "## Vergleich",
        "",
        "| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    for row in rows:
        base_row = base.get(str(row["world"]), {})
        delta_rec = _float(row["avg_mcm_rekopplung_quality"]) - _float(base_row.get("avg_mcm_rekopplung_quality"))
        lines.append(
            "| {world} | {rekopplung_factor:.2f} | {avg_mcm_rekopplung_quality:.4f} | {avg_mcm_carry_quality:.4f} | {avg_mcm_strain_quality:.4f} | {avg_mcm_adaptive_rekopplung_quality:.4f} | {avg_mcm_sensory_coupling:.4f} | {unique_symbols} | {unique_episode_families} | `{dominant_effect_class}` | ".format(**row)
            + f"{delta_rec:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.",
            "",
            "Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?",
            "",
            "## Grenze",
            "",
            "Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte derselbe direkte Eingriff mit mehr Faktoren und gegen laengere reale Assetfenster laufen. Entscheidend ist, ob die Reaktion graduell bleibt oder ob es einen echten Kipppunkt gibt.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Direkter MINI_DIO-Lauf-Stresstest fuer Rekopplungsdaempfung.")
    parser.add_argument("--world", action="append", help="label=pfad.csv; kann mehrfach angegeben werden.")
    parser.add_argument("--factors", default="1.0,0.75,0.5")
    parser.add_argument("--debug-root", default="debug/1823_rekopplung_damping_runtime")
    parser.add_argument("--memory-root", default="memory/1823_rekopplung_damping_runtime")
    parser.add_argument("--out-md", default="docs/befunde/1823_RUECKFUEHRUNG_DAEMPFUNG_DIREKTER_LAUFTEST.md")
    parser.add_argument("--out-csv", default="docs/befunde/1823_RUECKFUEHRUNG_DAEMPFUNG_DIREKTER_LAUFTEST.csv")
    parser.add_argument("--title", default="1823 - Direkter Lauf-Stresstest: Rueckfuehrungsdaempfung")
    args = parser.parse_args()

    factors = _parse_factors(args.factors)
    debug_root = _resolve(args.debug_root)
    memory_root = _resolve(args.memory_root)
    worlds = _parse_worlds(args.world)

    rows: list[dict[str, object]] = []
    for label, world in worlds.items():
        world_path = _resolve(world)
        if not world_path.exists():
            raise FileNotFoundError(world_path)
        for factor in factors:
            report, episodes_path = _run_one(label, world_path, factor, debug_root, memory_root)
            rows.append(_row(label, world_path, factor, report, _summarize_episode_rows(episodes_path)))

    rows.sort(key=lambda row: (str(row["world"]), -_float(row["rekopplung_factor"])))
    _write_csv(_resolve(args.out_csv), rows)
    _write_md(_resolve(args.out_md), rows, factors, str(args.title))
    print({"out_md": args.out_md, "out_csv": args.out_csv, "rows": len(rows)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
