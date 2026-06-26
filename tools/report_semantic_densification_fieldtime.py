from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_fieldtime_controlled"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "812_BLOCK_K_SEMANTISCHE_VERDICHTUNG_FELDZEIT.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "812_BLOCK_K_SEMANTISCHE_VERDICHTUNG_FELDZEIT.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p, 2)
    return entropy


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _read_report(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _top_share(counter: Counter[str], n: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return sum(count for _, count in counter.most_common(n)) / total


def _repeat_share(counter: Counter[str], min_count: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return sum(count for count in counter.values() if count >= min_count) / total


def _group_from_path(path: Path) -> str:
    try:
        return path.relative_to(DEBUG_DEFAULT).parts[0]
    except Exception:
        return path.parts[-4]


def summarize_run(report_path: Path) -> dict[str, object]:
    episodes_path = report_path.parent / "episodes.csv"
    rows = _read_csv(episodes_path)
    report = _read_report(report_path)
    symbols = Counter(str(row.get("symbol", "-") or "-") for row in rows)
    families = Counter(str(row.get("symbol_family", "-") or "-") for row in rows)
    field_episodes = Counter(
        str(row.get("mcm_field_episode_symbol", "-") or row.get("mcm_field_episode_preview_symbol", "-") or "-")
        for row in rows
    )
    total = len(rows)
    unique_symbols = len(symbols)
    unique_families = len(families)
    unique_field_episodes = len(field_episodes)
    semantic_reuse = 1.0 - (unique_symbols / max(1, total))
    family_reuse = 1.0 - (unique_families / max(1, total))
    field_episode_reuse = 1.0 - (unique_field_episodes / max(1, total))
    top_family_share = _top_share(families, 1, total)
    top5_family_share = _top_share(families, 5, total)
    repeated_symbol_share = _repeat_share(symbols, 10, total)
    repeated_family_share = _repeat_share(families, 10, total)
    top_family = families.most_common(1)[0][0] if families else "-"
    top_symbol = symbols.most_common(1)[0][0] if symbols else "-"
    group = _group_from_path(report_path)
    world = report_path.parent.parent.name
    # Diagnostic composite only: not a gate, not a target value.
    verdichtung_score = (
        semantic_reuse * 0.30
        + family_reuse * 0.20
        + top5_family_share * 0.20
        + repeated_family_share * 0.15
        + _safe_float(report.get("avg_mini_temporal_trust_support")) * 0.15
    )
    return {
        "type": "detail",
        "group": group,
        "world": world,
        "ticks": total,
        "unique_symbols": unique_symbols,
        "symbol_density": unique_symbols / max(1, total),
        "semantic_reuse": semantic_reuse,
        "unique_families": unique_families,
        "family_density": unique_families / max(1, total),
        "family_reuse": family_reuse,
        "unique_field_episodes": unique_field_episodes,
        "field_episode_reuse": field_episode_reuse,
        "top_symbol": top_symbol,
        "top_family": top_family,
        "top_family_share": top_family_share,
        "top5_family_share": top5_family_share,
        "repeated_symbol_share_10": repeated_symbol_share,
        "repeated_family_share_10": repeated_family_share,
        "symbol_entropy": _entropy(symbols),
        "family_entropy": _entropy(families),
        "fieldtime_trust": _safe_float(report.get("avg_mini_temporal_trust_support")),
        "afterimage": _safe_float(report.get("avg_mini_afterimage")),
        "avg_rekopplung": _safe_float(report.get("avg_mcm_rekopplung_quality")),
        "avg_carry": _safe_float(report.get("avg_mcm_carry_quality")),
        "avg_strain": _safe_float(report.get("avg_mcm_strain_quality")),
        "verdichtung_score": verdichtung_score,
        "source": str(report_path.relative_to(ROOT) if report_path.is_relative_to(ROOT) else report_path),
    }


def summarize_groups(details: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in details:
        grouped[str(row["group"])].append(row)
    summaries = []
    for group, rows in grouped.items():
        top_families = Counter(str(row["top_family"]) for row in rows)
        summaries.append(
            {
                "type": "summary",
                "group": group,
                "world": "GROUP",
                "ticks": _mean([_safe_float(row["ticks"]) for row in rows]),
                "unique_symbols": _mean([_safe_float(row["unique_symbols"]) for row in rows]),
                "symbol_density": _mean([_safe_float(row["symbol_density"]) for row in rows]),
                "semantic_reuse": _mean([_safe_float(row["semantic_reuse"]) for row in rows]),
                "unique_families": _mean([_safe_float(row["unique_families"]) for row in rows]),
                "family_density": _mean([_safe_float(row["family_density"]) for row in rows]),
                "family_reuse": _mean([_safe_float(row["family_reuse"]) for row in rows]),
                "unique_field_episodes": _mean([_safe_float(row["unique_field_episodes"]) for row in rows]),
                "field_episode_reuse": _mean([_safe_float(row["field_episode_reuse"]) for row in rows]),
                "top_symbol": "-",
                "top_family": top_families.most_common(1)[0][0] if top_families else "-",
                "top_family_share": _mean([_safe_float(row["top_family_share"]) for row in rows]),
                "top5_family_share": _mean([_safe_float(row["top5_family_share"]) for row in rows]),
                "repeated_symbol_share_10": _mean(
                    [_safe_float(row["repeated_symbol_share_10"]) for row in rows]
                ),
                "repeated_family_share_10": _mean(
                    [_safe_float(row["repeated_family_share_10"]) for row in rows]
                ),
                "symbol_entropy": _mean([_safe_float(row["symbol_entropy"]) for row in rows]),
                "family_entropy": _mean([_safe_float(row["family_entropy"]) for row in rows]),
                "fieldtime_trust": _mean([_safe_float(row["fieldtime_trust"]) for row in rows]),
                "afterimage": _mean([_safe_float(row["afterimage"]) for row in rows]),
                "avg_rekopplung": _mean([_safe_float(row["avg_rekopplung"]) for row in rows]),
                "avg_carry": _mean([_safe_float(row["avg_carry"]) for row in rows]),
                "avg_strain": _mean([_safe_float(row["avg_strain"]) for row in rows]),
                "verdichtung_score": _mean([_safe_float(row["verdichtung_score"]) for row in rows]),
                "source": "-",
            }
        )
    return summaries


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


def _write_markdown(path: Path, summaries: list[dict[str, object]], details: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_group = {str(row["group"]): row for row in summaries}
    lines = [
        "# 812 - Block-K semantische Verdichtung und Feldzeit",
        "",
        "## Fragestellung",
        "",
        "Vertieft laengere Feldzeit auch die semantische Bedeutungsverdichtung, oder werden `dio_*`-Inseln nur laenger getragen?",
        "",
        "## Gruppensynthese",
        "",
        "| Gruppe | Ticks | Symbol-Dichte | Semantik-Reuse | Familien-Dichte | Familien-Reuse | Top5-Familien | Wiederholte Familien | Feldzeit/Trust | Nachhall | Verdichtung | Top-Familie |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for group in ["kurz_2k", "asset_mixed_2k", "lang_10k"]:
        row = by_group.get(group)
        if not row:
            continue
        lines.append(
            f"| {row['group']} | {_fmt(row['ticks'])} | {_fmt(row['symbol_density'])} | "
            f"{_fmt(row['semantic_reuse'])} | {_fmt(row['family_density'])} | "
            f"{_fmt(row['family_reuse'])} | {_fmt(row['top5_family_share'])} | "
            f"{_fmt(row['repeated_family_share_10'])} | {_fmt(row['fieldtime_trust'])} | "
            f"{_fmt(row['afterimage'])} | {_fmt(row['verdichtung_score'])} | {row['top_family']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die 10k-Gruppe bildet nicht einfach eine groessere dominante Einzelinsel. Der Top-Familien-Anteil bleibt in einer aehnlichen Groessenordnung wie bei kurzen Welten. Der entscheidende Unterschied liegt in der Dichte:",
            "",
            "- deutlich niedrigere Symbol- und Familien-Dichte,",
            "- deutlich hoehere Wiederverwendung der eigenen Syntax,",
            "- hoehere Feldzeit/Trust- und Nachhallwerte,",
            "- stabile Top-Familie ueber alle Gruppen hinweg.",
            "",
            "Damit wirkt 10k nicht wie `mehr neue Worte`, sondern wie tiefere Wiederverwendung vorhandener Bedeutungsfamilien. Die Bedeutungsinseln werden also nicht nur laenger getragen; sie werden effizienter in der laufenden Welt wiederverwendet.",
            "",
            "## Detailauszug",
            "",
            "| Gruppe | Welt | Symbol-Dichte | Semantik-Reuse | Top5-Familien | Feldzeit/Trust | Nachhall | Top-Familie |",
            "|---|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in details:
        lines.append(
            f"| {row['group']} | {row['world']} | {_fmt(row['symbol_density'])} | "
            f"{_fmt(row['semantic_reuse'])} | {_fmt(row['top5_family_share'])} | "
            f"{_fmt(row['fieldtime_trust'])} | {_fmt(row['afterimage'])} | {row['top_family']} |"
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "`Verdichtung` ist hier eine diagnostische Zusammenschau aus Reuse, Familienbindung, Wiederkehr und Feldzeit. Sie ist kein Gate, kein Zielwert und keine Handlungsvorschrift.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die stabile Top-Familie `dio_104t` selbst mit der Lupe gelesen werden: welche Feldlage, Sinnesachsen und Weltkontakte tragen diese Familie in 2k und 10k jeweils mit?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    report_paths = sorted(debug_root.glob("*/*/dio_mini_lauf_1/mini_report.json"))
    if not report_paths:
        raise FileNotFoundError(f"no mini_report.json files found under {debug_root}")
    details = [summarize_run(path) for path in report_paths]
    summaries = summarize_groups(details)
    _write_csv(args.csv_out, summaries + details)
    _write_markdown(args.md_out, summaries, details)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summaries:
        print(
            f"{row['group']}: density={float(row['symbol_density']):.4f} "
            f"reuse={float(row['semantic_reuse']):.4f} "
            f"verdichtung={float(row['verdichtung_score']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
