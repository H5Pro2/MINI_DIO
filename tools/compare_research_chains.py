from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "MEHRWELT_VERGLEICH.md"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _as_float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _effect_profile(summary: dict) -> dict[str, int]:
    return {str(k): int(v or 0) for k, v in (summary.get("passive_mcm_effect_classes") or {}).items()}


def _profile_similarity(left: dict[str, int], right: dict[str, int]) -> float:
    keys = set(left) | set(right)
    if not keys:
        return 0.0
    left_total = max(1, sum(left.values()))
    right_total = max(1, sum(right.values()))
    distance = 0.0
    for key in keys:
        distance += abs((left.get(key, 0) / left_total) - (right.get(key, 0) / right_total))
    return round(max(0.0, 1.0 - (distance / 2.0)), 4)


def _set_from(summary: dict, key: str) -> set[str]:
    value = summary.get(key, {})
    if isinstance(value, dict):
        return {str(item) for item in value.get("shared", []) or []}
    return set()


def _set_similarity(left: set[str], right: set[str]) -> float:
    base = len(left | right)
    if base <= 0:
        return 0.0
    return round(len(left & right) / base, 4)


def compare(summaries: list[tuple[str, dict]]) -> dict:
    rows: list[dict[str, object]] = []
    for name, summary in summaries:
        profile = _effect_profile(summary)
        total = max(1, sum(profile.values()))
        dominant = max(profile.items(), key=lambda item: item[1])[0] if profile else "-"
        rows.append(
            {
                "name": name,
                "data_path": summary.get("data_path", ""),
                "candles": summary.get("candles", 0),
                "unique_symbols_run_1": (summary.get("unique_symbols") or [0, 0])[0],
                "unique_symbols_run_2": (summary.get("unique_symbols") or [0, 0])[1],
                "episodes_run_1": (summary.get("episodes") or [0, 0])[0],
                "episodes_run_2": (summary.get("episodes") or [0, 0])[1],
                "episode_memory_written_run_2": (summary.get("episode_memory_written") or [0, 0])[1],
                "top_symbol_overlap": (summary.get("top_symbol_overlap") or {}).get("ratio", 0.0),
                "top_family_overlap": (summary.get("top_family_overlap") or {}).get("ratio", 0.0),
                "avg_mcm_rekopplung_run_2": (summary.get("avg_mcm_rekopplung_quality") or [0.0, 0.0])[1],
                "avg_mcm_carry_run_2": (summary.get("avg_mcm_carry_quality") or [0.0, 0.0])[1],
                "avg_mcm_sensory_coupling_run_2": (summary.get("avg_mcm_sensory_coupling") or [0.0, 0.0])[1],
                "dominant_effect": dominant,
                "dominant_effect_ratio": round(profile.get(dominant, 0) / total, 4) if dominant != "-" else 0.0,
                "profile": profile,
                "top_symbols": sorted(_set_from(summary, "top_symbol_overlap")),
                "top_families": sorted(_set_from(summary, "top_family_overlap")),
            }
        )

    pair_rows: list[dict[str, object]] = []
    for index, left in enumerate(rows):
        for right in rows[index + 1 :]:
            pair_rows.append(
                {
                    "left": left["name"],
                    "right": right["name"],
                    "effect_profile_similarity": _profile_similarity(left["profile"], right["profile"]),
                    "top_symbol_similarity": _set_similarity(set(left["top_symbols"]), set(right["top_symbols"])),
                    "top_family_similarity": _set_similarity(set(left["top_families"]), set(right["top_families"])),
                    "dominant_effect_shift": f"{left['dominant_effect']} -> {right['dominant_effect']}",
                    "rekopplung_delta": round(
                        _as_float(right["avg_mcm_rekopplung_run_2"])
                        - _as_float(left["avg_mcm_rekopplung_run_2"]),
                        6,
                    ),
                    "carry_delta": round(
                        _as_float(right["avg_mcm_carry_run_2"]) - _as_float(left["avg_mcm_carry_run_2"]),
                        6,
                    ),
                }
            )

    return {
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "worlds": rows,
        "pairs": pair_rows,
    }


def write_markdown(result: dict, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Mehrwelt-Vergleich",
        "",
        f"Stand: {result['created_at']}",
        "",
        "## Zweck",
        "",
        "Dieser Bericht vergleicht mehrere passive MINI_DIO-Forschungsketten.",
        "Er prüft, ob Reproduktion nur innerhalb einer Welt stabil ist oder ob über verschiedene Welten neue Bedeutungsräume, Drift oder stabile Feldrollen sichtbar werden.",
        "",
        "## Einzelwelten",
        "",
    ]
    for world in result["worlds"]:
        lines.extend(
            [
                f"### {world['name']}",
                "",
                f"- Datenwelt: `{world['data_path']}`",
                f"- Kerzen: `{world['candles']}`",
                f"- Unique Syntax: `{world['unique_symbols_run_1']}` -> `{world['unique_symbols_run_2']}`",
                f"- Episoden: `{world['episodes_run_1']}` -> `{world['episodes_run_2']}`",
                f"- Episodenmemory Lauf 2: `{world['episode_memory_written_run_2']}`",
                f"- Top-Syntax-Reproduktion: `{world['top_symbol_overlap']}`",
                f"- Top-Familien-Reproduktion: `{world['top_family_overlap']}`",
                f"- MCM-Rekopplung Lauf 2: `{world['avg_mcm_rekopplung_run_2']}`",
                f"- MCM-Tragqualität Lauf 2: `{world['avg_mcm_carry_run_2']}`",
                f"- dominante Feldwirkung: `{world['dominant_effect']}` (`{world['dominant_effect_ratio']}`)",
                "",
                "Feldprofil:",
                "",
            ]
        )
        for key, value in sorted(world["profile"].items()):
            lines.append(f"- `{key}`: `{value}`")
        lines.append("")

    lines.extend(["## Weltvergleich", ""])
    for pair in result["pairs"]:
        lines.extend(
            [
                f"### {pair['left']} gegen {pair['right']}",
                "",
                f"- Feldprofil-Ähnlichkeit: `{pair['effect_profile_similarity']}`",
                f"- Top-Syntax-Ähnlichkeit: `{pair['top_symbol_similarity']}`",
                f"- Top-Familien-Ähnlichkeit: `{pair['top_family_similarity']}`",
                f"- dominante Feldwirkung: `{pair['dominant_effect_shift']}`",
                f"- Rekopplungsdelta: `{pair['rekopplung_delta']}`",
                f"- Tragqualitätsdelta: `{pair['carry_delta']}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Eine hohe Reproduktion innerhalb einer Welt bei gleichzeitiger Verschiebung zwischen Welten spricht dafür, dass MINI_DIO nicht wahllos speichert, sondern weltbezogene Innenfeldordnungen bildet.",
            "",
            "Wichtig bleibt: Das ist passive Feldforschung. Der Bericht erzeugt keine Handlung, kein Gate und keine Strategie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten weitere Welten ergänzt werden. Entscheidend ist, ob sich ein stabiler Kern der Feldtopologie zeigt, während Bedeutungsinseln je nach Weltspannung entstehen, driften oder rekoppeln.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Vergleiche passive MINI_DIO-Forschungsketten.")
    parser.add_argument(
        "--summary",
        action="append",
        nargs=2,
        metavar=("NAME", "PATH"),
        help="Name und Pfad zu einer research_chain_summary.json",
    )
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    summary_args = args.summary or [
        ("welt_2023_01", "debug/research_chain/research_chain_summary.json"),
        ("welt_2024_01", "debug/research_chain_2024_01/research_chain_summary.json"),
    ]
    summaries = []
    for name, path_text in summary_args:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        summaries.append((name, _load(path)))

    result = compare(summaries)
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    write_markdown(result, out_path)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
