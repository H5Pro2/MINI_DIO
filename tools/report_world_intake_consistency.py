from __future__ import annotations

import argparse
import csv
import statistics
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_senses, build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_OUT = ROOT / "docs" / "befunde" / "262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE.csv"

SENSE_FEATURES = (
    ("sehen.form_flow", "sehen", "form_flow"),
    ("sehen.form_stability", "sehen", "form_stability"),
    ("sehen.form_change", "sehen", "form_change"),
    ("hoeren.energy_tone", "hoeren", "energy_tone"),
    ("hoeren.energy_shift", "hoeren", "energy_shift"),
    ("mcm_feldwirkung.mcm_coherence", "mcm_feldwirkung", "mcm_coherence"),
    ("mcm_feldwirkung.mcm_tension", "mcm_feldwirkung", "mcm_tension"),
    ("mcm_feldwirkung.mcm_asymmetry", "mcm_feldwirkung", "mcm_asymmetry"),
)


def _float(value: object) -> float:
    try:
        value = float(value or 0.0)
    except Exception:
        value = 0.0
    if value != value:
        return 0.0
    return value


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * q
    lower = int(index)
    upper = min(len(values) - 1, lower + 1)
    if lower == upper:
        return values[lower]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _sense_stats(values: list[float]) -> dict[str, float]:
    abs_values = [abs(_float(item)) for item in values]
    if not abs_values:
        return {
            "mean": 0.0,
            "mean_abs": 0.0,
            "p50_abs": 0.0,
            "p95_abs": 0.0,
            "p99_abs": 0.0,
            "saturation_ratio": 0.0,
            "flat_ratio": 0.0,
        }
    return {
        "mean": statistics.fmean(values),
        "mean_abs": statistics.fmean(abs_values),
        "p50_abs": _percentile(abs_values, 0.50),
        "p95_abs": _percentile(abs_values, 0.95),
        "p99_abs": _percentile(abs_values, 0.99),
        "saturation_ratio": sum(1 for item in abs_values if item >= 0.98) / len(abs_values),
        "flat_ratio": sum(1 for item in abs_values if item <= 0.02) / len(abs_values),
    }


def _raw_world_stats(candles: list[dict]) -> dict[str, float]:
    returns: list[float] = []
    range_pct: list[float] = []
    volumes: list[float] = []
    for index, candle in enumerate(candles):
        close = max(1e-9, _float(candle.get("close")))
        range_pct.append((_float(candle.get("high")) - _float(candle.get("low"))) / close)
        volumes.append(max(0.0, _float(candle.get("volume"))))
        if index > 0:
            prev = max(1e-9, _float(candles[index - 1].get("close")))
            returns.append((_float(candle.get("close")) - prev) / prev)
    abs_returns = [abs(item) for item in returns]
    return {
        "candles": float(len(candles)),
        "return_p95_abs": _percentile(abs_returns, 0.95),
        "return_p99_abs": _percentile(abs_returns, 0.99),
        "range_pct_p95": _percentile(range_pct, 0.95),
        "range_pct_p99": _percentile(range_pct, 0.99),
        "volume_p95": _percentile(volumes, 0.95),
        "volume_p99": _percentile(volumes, 0.99),
    }


def _diagnose_feature(stats: dict[str, float]) -> str:
    saturation = stats["saturation_ratio"]
    flat = stats["flat_ratio"]
    p95 = stats["p95_abs"]
    if saturation >= 0.10:
        return "uebersteuert"
    if flat >= 0.60 and p95 <= 0.15:
        return "zu_flach"
    if p95 >= 0.90:
        return "nahe_saettigung"
    if p95 <= 0.10:
        return "schwach"
    return "tragbar"


def _world_state(feature_rows: list[dict[str, object]]) -> str:
    states = [str(row["feature_state"]) for row in feature_rows]
    if any(state == "uebersteuert" for state in states):
        return "reiz_uebersteuert"
    if states.count("zu_flach") + states.count("schwach") >= 4:
        return "reiz_zu_flach"
    if any(state == "nahe_saettigung" for state in states):
        return "reiz_grenznah"
    return "reiz_tragbar"


def _analyze_world(name: str, path: Path, sense_mode: str) -> tuple[dict[str, object], list[dict[str, object]]]:
    candles = load_candles(path)
    raw_stats = _raw_world_stats(candles)
    profile = build_sensory_profile(candles) if sense_mode == "world_relative" else {}
    feature_values = {feature: [] for feature, _, _ in SENSE_FEATURES}
    for index in range(len(candles)):
        if sense_mode == "world_relative":
            senses = build_senses_world_relative(candles, index, profile=profile)
        else:
            senses = build_senses(candles, index)
        for feature, root, key in SENSE_FEATURES:
            source = dict(senses.get(root, {}) or {})
            if root == "mcm_feldwirkung" and key not in source:
                source = dict(senses.get("fuehlen", {}) or {})
            feature_values[feature].append(_float(source.get(key)))

    feature_rows: list[dict[str, object]] = []
    for feature, values in feature_values.items():
        stats = _sense_stats(values)
        feature_rows.append(
            {
                "world": name,
                "feature": feature,
                "mean": stats["mean"],
                "mean_abs": stats["mean_abs"],
                "p50_abs": stats["p50_abs"],
                "p95_abs": stats["p95_abs"],
                "p99_abs": stats["p99_abs"],
                "saturation_ratio": stats["saturation_ratio"],
                "flat_ratio": stats["flat_ratio"],
                "feature_state": _diagnose_feature(stats),
            }
        )
    summary = {
        "world": name,
        "path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        "world_state": _world_state(feature_rows),
        "sense_mode": sense_mode,
        **raw_stats,
    }
    return summary, feature_rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "feature",
        "mean",
        "mean_abs",
        "p50_abs",
        "p95_abs",
        "p99_abs",
        "saturation_ratio",
        "flat_ratio",
        "feature_state",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(summaries: list[dict[str, object]], feature_rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Weltuebergreifende Informationsaufnahme: Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob MINI_DIO Welten ueber Sehen, Hoeren und MCM-Feldwirkung vergleichbar aufnimmt.",
        "Sie liest nicht die MCM-Topologie selbst, sondern den Schritt davor: Rohwelt zu Sinneswerten.",
        f"Sinnesmodus: `{str(summaries[0].get('sense_mode', '-')) if summaries else '-'}`.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Hierarchie",
        "",
        "1. Allgemeine Grundfrage: Ist die Informationsaufnahme ueber Welten einheitlich genug?",
        "2. Konkrete Unterpruefung: Welche Sinnesachsen uebersteuern, flachen ab oder bleiben tragbar?",
        "3. Folgeschritt: Wenn die Aufnahme nicht einheitlich ist, braucht MINI_DIO einen weltrelativen Wahrnehmungsadapter.",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Zustand | Kerzen | Return p95 | Range p95 | Volume p95 |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["world_state"]),
                    str(int(_float(row["candles"]))),
                    _fmt(_float(row["return_p95_abs"])),
                    _fmt(_float(row["range_pct_p95"])),
                    _fmt(_float(row["volume_p95"]), 2),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Sinnesachsen",
            "",
            "| Welt | Achse | Zustand | p95 abs | Saettigung | Flachheit |",
            "|---|---|---|---:|---:|---:|",
        ]
    )
    for row in feature_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["feature"]),
                    str(row["feature_state"]),
                    _fmt(_float(row["p95_abs"])),
                    _fmt(_float(row["saturation_ratio"])),
                    _fmt(_float(row["flat_ratio"])),
                ]
            )
            + " |"
        )

    problem_rows = [row for row in feature_rows if row["feature_state"] != "tragbar"]
    problem_summary = ", ".join(
        f"{row['world']}:{row['feature']}={row['feature_state']}" for row in problem_rows[:12]
    )
    if len(problem_rows) > 12:
        problem_summary += f", ... ({len(problem_rows) - 12} weitere)"
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Auffaellige Sinnesachsen: {problem_summary or '-'}",
            "",
            "Wenn Welten vor allem durch feste Teiler oder lokale Rohverhaeltnisse uebersetzt werden, kann das MCM-Feld nicht sicher unterscheiden, ob es echte Feldwirkung oder falsche Reizskalierung erlebt.",
            "Im weltrelativen Modus wird dagegen geprueft, ob die Aufnahme bereits gegen den eigenen Rhythmus der Welt gelesen wird.",
            "",
            "## Grenze",
            "",
            "Diese Diagnose bewertet nur die Informationsaufnahme.",
            "Sie entscheidet nicht, welche Topologie wahr ist und sie erzeugt keine neue Feldwirkung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte bei weiterhin auffaelligen Achsen geprueft werden, ob sie echte Weltqualitaet tragen oder ob der Adapter eine feinere Aufnahme braucht.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--world",
        action="append",
        nargs=2,
        metavar=("NAME", "PATH"),
        help="World label plus CSV path. Can be passed multiple times.",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument(
        "--sense-mode",
        choices=("fixed", "world_relative"),
        default="world_relative",
        help="Sensory translation mode used for this diagnostic.",
    )
    args = parser.parse_args()

    worlds = args.world or [
        ("SOL_2023_5M_REAL1", "data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv"),
        ("SOL_2024_5M_REAL1", "data/kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv"),
        ("SOL_2024_1H_2K", "data/kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv"),
        ("BTC_2024_5M_2K", "data/kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv"),
        ("BTC_2024_1H_2K", "data/kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv"),
        ("SOL_2023_NEG_STRESS", "data/kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv"),
    ]

    summaries: list[dict[str, object]] = []
    feature_rows: list[dict[str, object]] = []
    for name, raw_path in worlds:
        path = Path(raw_path)
        if not path.is_absolute():
            path = ROOT / path
        summary, rows = _analyze_world(name, path, args.sense_mode)
        summaries.append(summary)
        feature_rows.extend(rows)

    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(feature_rows, csv_path)
    _write_md(summaries, feature_rows, out_path)


if __name__ == "__main__":
    main()
