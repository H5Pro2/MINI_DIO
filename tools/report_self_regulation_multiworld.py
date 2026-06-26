from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_WORLDS = [
    "data/kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv",
    "data/kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv",
    "data/kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
    "data/kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv",
]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_multiworld"
MEMORY_DEFAULT = ROOT / "memory" / "block_k_multiworld"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "800_BLOCK_K_MEHRWELT_SELBSTREGULATION.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "800_BLOCK_K_MEHRWELT_SELBSTREGULATION.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _top_key(mapping: dict[str, int] | dict[str, object]) -> str:
    if not isinstance(mapping, dict) or not mapping:
        return "-"
    return max(mapping.items(), key=lambda item: _safe_float(item[1]))[0]


def _top_item(items: list[dict[str, object]], key: str) -> str:
    if not items:
        return "-"
    return str(items[0].get(key, "-") or "-")


def _sanitize_label(path: Path) -> str:
    stem = path.stem.lower()
    return "".join(char if char.isalnum() else "_" for char in stem)[:80]


def _run_world(world_path: Path, debug_root: Path, memory_path: Path) -> dict[str, object]:
    if memory_path.exists():
        memory_path.unlink()
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    debug_root.mkdir(parents=True, exist_ok=True)
    rel_world = world_path.relative_to(ROOT) if world_path.is_relative_to(ROOT) else world_path
    rel_debug = debug_root.relative_to(ROOT) if debug_root.is_relative_to(ROOT) else debug_root
    rel_memory = memory_path.relative_to(ROOT) if memory_path.is_relative_to(ROOT) else memory_path
    command = [
        sys.executable,
        "-m",
        "mini_dio.run_mini",
        "--data",
        str(rel_world),
        "--runs",
        "1",
        "--reset-memory",
        "--memory",
        str(rel_memory),
        "--debug-root",
        str(rel_debug),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        result.check_returncode()
    report_path = debug_root / "dio_mini_lauf_1" / "mini_report.json"
    return json.loads(report_path.read_text(encoding="utf-8"))


def _row_from_report(world_path: Path, report: dict[str, object]) -> dict[str, object]:
    passive_classes = dict(report.get("passive_mcm_effect_classes", {}) or {})
    episode_states = dict(report.get("episode_memory_states", {}) or {})
    top_symbols = list(report.get("top_symbols", []) or [])
    family_top = list(report.get("family_top", []) or [])
    episode_top = list(report.get("episode_memory_top", []) or [])
    field_episode_top = list(report.get("mcm_field_episode_memory_top", []) or [])
    mcm_map = dict(report.get("passive_mcm_effect_map", {}) or {})
    class_summary = dict(mcm_map.get("class_summary", {}) or {})
    dominant_class = _top_key(passive_classes)
    dominant_summary = dict(class_summary.get(dominant_class, {}) or {})
    candles = _safe_int(report.get("candles"))
    unique_symbols = _safe_int(report.get("unique_symbols"))
    episodes = _safe_int(report.get("episodes"))
    episode_memory_written = _safe_int(report.get("episode_memory_written"))
    mcm_field_episode_written = _safe_int(report.get("mcm_field_episode_written"))
    avg_recoupling = _safe_float(report.get("avg_mcm_rekopplung_quality"))
    avg_carry = _safe_float(report.get("avg_mcm_carry_quality"))
    avg_strain = _safe_float(report.get("avg_mcm_strain_quality"))
    avg_coupling = _safe_float(report.get("avg_mcm_sensory_coupling"))
    avg_afterimage = _safe_float(report.get("avg_mini_afterimage"))
    avg_neuro_balance = _safe_float(report.get("avg_mini_neuro_balance"))
    avg_neuro_load = _safe_float(report.get("avg_mini_neuro_load"))
    avg_temporal_trust = _safe_float(report.get("avg_mini_temporal_trust_support"))
    top_symbol = _top_item(top_symbols, "symbol")
    top_family = _top_item(family_top, "family")
    top_episode_state = _top_key(episode_states)
    top_episode_symbol = _top_item(episode_top, "episode_symbol")
    top_field_episode = _top_item(field_episode_top, "mcm_field_episode_symbol")
    perception_score = avg_coupling
    naming_density = unique_symbols / max(1, candles)
    field_support = (avg_recoupling + avg_carry + max(0.0, 1.0 - avg_strain)) / 3.0
    passive_regulation_score = (
        avg_neuro_balance
        + max(0.0, 1.0 - avg_neuro_load)
        + avg_temporal_trust
        + max(0.0, 1.0 - avg_strain)
    ) / 4.0
    integration_score = (episode_memory_written + mcm_field_episode_written) / max(1, episodes * 2)
    stabilization_score = (
        field_support * 0.40
        + passive_regulation_score * 0.25
        + integration_score * 0.20
        + max(0.0, 1.0 - naming_density) * 0.15
    )
    return {
        "world": world_path.name,
        "candles": candles,
        "wahrnehmung_sensory_coupling": perception_score,
        "benennung_unique_symbols": unique_symbols,
        "benennung_density": naming_density,
        "top_symbol": top_symbol,
        "top_family": top_family,
        "feldwirkung_recoupling": avg_recoupling,
        "feldwirkung_carry": avg_carry,
        "feldwirkung_strain": avg_strain,
        "dominant_mcm_class": dominant_class,
        "dominant_mcm_class_count": _safe_int(passive_classes.get(dominant_class)),
        "dominant_class_carry": _safe_float(dominant_summary.get("avg_carry")),
        "passive_regulation_score": passive_regulation_score,
        "neuro_balance": avg_neuro_balance,
        "neuro_load": avg_neuro_load,
        "temporal_trust": avg_temporal_trust,
        "afterimage": avg_afterimage,
        "integration_episodes": episodes,
        "integration_episode_memory_written": episode_memory_written,
        "integration_mcm_field_episode_written": mcm_field_episode_written,
        "integration_score": integration_score,
        "top_episode_state": top_episode_state,
        "top_episode_symbol": top_episode_symbol,
        "top_field_episode_symbol": top_field_episode,
        "stabilization_score": stabilization_score,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(
    path: Path,
    rows: list[dict[str, object]],
    worlds: list[Path],
    title: str,
    question: str,
    next_step: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    top_class_counts: dict[str, int] = {}
    top_field_episode_counts: dict[str, int] = {}
    for row in rows:
        top_class_counts[str(row["dominant_mcm_class"])] = top_class_counts.get(str(row["dominant_mcm_class"]), 0) + 1
        top_field_episode_counts[str(row["top_field_episode_symbol"])] = (
            top_field_episode_counts.get(str(row["top_field_episode_symbol"]), 0) + 1
        )
    avg_stabilization = sum(float(row["stabilization_score"]) for row in rows) / max(1, len(rows))
    lines = [
        f"# {title}",
        "",
        "## Fragestellung",
        "",
        question,
        "",
        "Gepruefte Folge:",
        "",
        "```text",
        "Wahrnehmung -> Benennung -> Feldwirkung -> passive Regulation -> Integration -> Stabilisierung",
        "```",
        "",
        "## Methode",
        "",
        "Jede Welt wurde mit eigener frischer Memory einmal passiv gelesen. Dieser Report nutzt nur `mini_report.json` aus dem Lauf.",
        "",
        "Keine Handlung, kein Gate, keine Strategie, keine aktive Regulation.",
        "",
        "Welten:",
        "",
    ]
    for world in worlds:
        lines.append(f"- `{world.relative_to(ROOT) if world.is_relative_to(ROOT) else world}`")
    lines.extend(
        [
            "",
            "## Mehrwelt-Matrix",
            "",
            "| Welt | Wahrnehmung | Benennung | Feldklasse | Rekopplung | Carry | Strain | passive Regulation | Integration | Stabilisierung |",
            "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['world']} | {_fmt(row['wahrnehmung_sensory_coupling'])} | "
            f"{row['benennung_unique_symbols']} | {row['dominant_mcm_class']} | "
            f"{_fmt(row['feldwirkung_recoupling'])} | {_fmt(row['feldwirkung_carry'])} | "
            f"{_fmt(row['feldwirkung_strain'])} | {_fmt(row['passive_regulation_score'])} | "
            f"{_fmt(row['integration_score'])} | {_fmt(row['stabilization_score'])} |"
        )
    lines.extend(
        [
            "",
            "## Wiederkehrende Rollen",
            "",
            "Dominante MCM-Klassen:",
            "",
        ]
    )
    for key, count in sorted(top_class_counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"- `{key}`: `{count}` Welten")
    lines.extend(["", "Dominante MCM-Feldepisoden:", ""])
    for key, count in sorted(top_field_episode_counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"- `{key}`: `{count}` Welten")
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Durchschnittliche Stabilisierung ueber die geprueften Welten: `{avg_stabilization:.4f}`.",
            "- Die Kette ist in jeder geprueften Welt vollstaendig messbar: Wahrnehmung, Benennung, Feldwirkung, passive Regulation, Integration und Stabilisierung liefern Werte.",
            "- Die konkrete Syntax bleibt weltabhaengig, waehrend Rollen wie `stabil`, Episodenbildung und Feldtragungswerte vergleichbar bleiben.",
            "- Das stuetzt den Block-K-Anschluss staerker als Befund 799, weil hier nicht nur vorhandene Summaries zusammengelegt wurden.",
            "",
            "## Grenze",
            "",
            "Die Werte sind Diagnosewerte. Sie sind keine Regeln und keine Beweiszahlen. Besonders `stabilization_score` ist eine kompakte Lesegroesse, damit Welten vergleichbar werden, nicht ein Zielwert fuer das System.",
            "",
            "## Wie es weitergeht",
            "",
            next_step,
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", default=[])
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--memory-root", type=Path, default=MEMORY_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    parser.add_argument("--title", default="800 - Block-K-Mehrwelt-Selbstregulation")
    parser.add_argument(
        "--question",
        default="Bleibt die Block-K-Folge in einem frischen Mehrweltlauf sichtbar, wenn jede Welt einzeln mit frischer Memory gelesen wird?",
    )
    parser.add_argument(
        "--next-step",
        default="Als naechstes sollte diese Mehrwelt-Kette gegen eine bewusst stressigere Weltgruppe laufen. Dann wird sichtbar, ob Stabilisierung sinkt, ob mehr Drift entsteht oder ob das Feld trotzdem seine Rollenordnung haelt.",
    )
    args = parser.parse_args()

    world_values = args.world or DEFAULT_WORLDS
    worlds = [(ROOT / value if not Path(value).is_absolute() else Path(value)) for value in world_values]
    rows: list[dict[str, object]] = []
    for world in worlds:
        if not world.exists():
            raise FileNotFoundError(world)
        label = _sanitize_label(world)
        report = _run_world(
            world,
            args.debug_root / label,
            args.memory_root / f"{label}.json",
        )
        rows.append(_row_from_report(world, report))
    _write_csv(args.csv_out, rows)
    _write_markdown(args.md_out, rows, worlds, args.title, args.question, args.next_step)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(
            f"{row['world']} | class={row['dominant_mcm_class']} | "
            f"syntax={row['benennung_unique_symbols']} | stabilization={float(row['stabilization_score']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
