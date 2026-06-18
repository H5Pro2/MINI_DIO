from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.config import Config

DEFAULT_OUT = ROOT / "docs" / "befunde" / "AKTUELLER_FORSCHUNGSLAUF.md"


def _load_report(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _top_names(items: list[dict], key: str, limit: int = 8) -> list[str]:
    names: list[str] = []
    for item in items[:limit]:
        value = item.get(key)
        if value:
            names.append(str(value))
    return names


def _overlap(left: list[str], right: list[str]) -> dict[str, object]:
    left_set = set(left)
    right_set = set(right)
    shared = sorted(left_set & right_set)
    base = max(1, len(left_set | right_set))
    return {
        "shared": shared,
        "ratio": round(len(shared) / base, 4),
    }


def _summarize_reports(first: dict, second: dict) -> dict[str, object]:
    first_symbols = _top_names(first.get("top_symbols", []) or [], "symbol")
    second_symbols = _top_names(second.get("top_symbols", []) or [], "symbol")
    first_families = _top_names(first.get("family_top", []) or [], "family")
    second_families = _top_names(second.get("family_top", []) or [], "family")

    return {
        "data_path": second.get("data_path", first.get("data_path", "")),
        "runs": [first.get("run"), second.get("run")],
        "candles": second.get("candles", first.get("candles", 0)),
        "trades": [first.get("trades", 0), second.get("trades", 0)],
        "unique_symbols": [first.get("unique_symbols", 0), second.get("unique_symbols", 0)],
        "episodes": [first.get("episodes", 0), second.get("episodes", 0)],
        "episode_memory_written": [
            first.get("episode_memory_written", 0),
            second.get("episode_memory_written", 0),
        ],
        "avg_mcm_rekopplung_quality": [
            round(float(first.get("avg_mcm_rekopplung_quality", 0.0) or 0.0), 6),
            round(float(second.get("avg_mcm_rekopplung_quality", 0.0) or 0.0), 6),
        ],
        "avg_mcm_carry_quality": [
            round(float(first.get("avg_mcm_carry_quality", 0.0) or 0.0), 6),
            round(float(second.get("avg_mcm_carry_quality", 0.0) or 0.0), 6),
        ],
        "avg_mcm_sensory_coupling": [
            round(float(first.get("avg_mcm_sensory_coupling", 0.0) or 0.0), 6),
            round(float(second.get("avg_mcm_sensory_coupling", 0.0) or 0.0), 6),
        ],
        "passive_mcm_effect_classes": second.get("passive_mcm_effect_classes", {}),
        "episode_memory_states": second.get("episode_memory_states", {}),
        "top_symbol_overlap": _overlap(first_symbols, second_symbols),
        "top_family_overlap": _overlap(first_families, second_families),
    }


def _write_markdown(summary: dict[str, object], out_path: Path, debug_root: Path, memory_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    debug_display = debug_root.resolve().relative_to(ROOT)
    memory_display = memory_path.resolve().relative_to(ROOT)
    lines = [
        "# Aktueller Forschungslauf",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:",
        "",
        "- gleicher Datensatz,",
        "- gleiche Memory zwischen Lauf 1 und Lauf 2,",
        "- passive Beobachtung ohne Entry, Gate oder Motorik,",
        "- Vergleich von Innenfeld, Syntax und Episodenbildung.",
        "",
        "## Ergebnis",
        "",
        f"- Datenwelt: `{summary['data_path']}`",
        f"- Kerzen: `{summary['candles']}`",
        f"- Trades: `{summary['trades'][0]}` -> `{summary['trades'][1]}`",
        f"- Unique Syntaxsymbole: `{summary['unique_symbols'][0]}` -> `{summary['unique_symbols'][1]}`",
        f"- Episoden: `{summary['episodes'][0]}` -> `{summary['episodes'][1]}`",
        f"- geschriebene Episodenmemory: `{summary['episode_memory_written'][0]}` -> `{summary['episode_memory_written'][1]}`",
        f"- MCM-Rekopplung: `{summary['avg_mcm_rekopplung_quality'][0]}` -> `{summary['avg_mcm_rekopplung_quality'][1]}`",
        f"- MCM-Tragqualitaet: `{summary['avg_mcm_carry_quality'][0]}` -> `{summary['avg_mcm_carry_quality'][1]}`",
        f"- Sinnes-MCM-Kopplung: `{summary['avg_mcm_sensory_coupling'][0]}` -> `{summary['avg_mcm_sensory_coupling'][1]}`",
        "",
        "## Reproduktionsnaehe",
        "",
        f"- Top-Syntax-Ueberlappung: `{summary['top_symbol_overlap']['ratio']}`",
        f"- gemeinsame Top-Syntax: `{', '.join(summary['top_symbol_overlap']['shared']) or '-'}`",
        f"- Top-Familien-Ueberlappung: `{summary['top_family_overlap']['ratio']}`",
        f"- gemeinsame Top-Familien: `{', '.join(summary['top_family_overlap']['shared']) or '-'}`",
        "",
        "## Innenfeld",
        "",
        "Passive MCM-Wirkungsklassen:",
        "",
    ]
    for key, value in sorted((summary.get("passive_mcm_effect_classes") or {}).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "Episodenzustaende:", ""])
    for key, value in sorted((summary.get("episode_memory_states") or {}).items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Artefakte",
            "",
            f"- Debug: `{debug_display}`",
            f"- Memory: `{memory_display}`",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. "
            "Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen "
            "oder ob vorhandene Bedeutungen driften.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def run_chain(data_path: Path, debug_root: Path, memory_path: Path, out_path: Path) -> dict[str, object]:
    data_path = data_path if data_path.is_absolute() else ROOT / data_path
    debug_root = debug_root if debug_root.is_absolute() else ROOT / debug_root
    memory_path = memory_path if memory_path.is_absolute() else ROOT / memory_path
    out_path = out_path if out_path.is_absolute() else ROOT / out_path
    debug_root.mkdir(parents=True, exist_ok=True)
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    if memory_path.exists():
        memory_path.unlink()

    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(data_path.relative_to(ROOT) if data_path.is_relative_to(ROOT) else data_path),
        "--runs",
        "2",
        "--memory",
        str(memory_path.relative_to(ROOT) if memory_path.is_relative_to(ROOT) else memory_path),
        "--debug-root",
        str(debug_root.relative_to(ROOT) if debug_root.is_relative_to(ROOT) else debug_root),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()

    first = _load_report(debug_root / "dio_mini_lauf_1" / "mini_report.json")
    second = _load_report(debug_root / "dio_mini_lauf_2" / "mini_report.json")
    summary = _summarize_reports(first, second)
    _write_markdown(summary, out_path, debug_root, memory_path)
    (debug_root / "research_chain_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the passive MINI_DIO research chain.")
    parser.add_argument("--data", default=getattr(Config, "DIO_MINI_CONTROLLED_WORLD_PATH"))
    parser.add_argument("--debug-root", default="debug/research_chain")
    parser.add_argument("--memory", default="memory/research_chain_memory.json")
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    summary = run_chain(
        data_path=Path(args.data),
        debug_root=Path(args.debug_root),
        memory_path=Path(args.memory),
        out_path=Path(args.out),
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
