from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_senses, build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_OUT = ROOT / "docs" / "befunde" / "263_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "263_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.csv"
FEATURES = (
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


def _stats(values: list[float]) -> dict[str, float]:
    abs_values = [abs(_float(item)) for item in values]
    if not abs_values:
        return {
            "mean_abs": 0.0,
            "p95_abs": 0.0,
            "saturation_ratio": 0.0,
            "flat_ratio": 0.0,
            "spread": 0.0,
        }
    return {
        "mean_abs": statistics.fmean(abs_values),
        "p95_abs": _percentile(abs_values, 0.95),
        "saturation_ratio": sum(1 for item in abs_values if item >= 0.98) / len(abs_values),
        "flat_ratio": sum(1 for item in abs_values if item <= 0.02) / len(abs_values),
        "spread": _percentile(abs_values, 0.95) - _percentile(abs_values, 0.50),
    }


def _feature_state(stats: dict[str, float]) -> str:
    if stats["saturation_ratio"] >= 0.10:
        return "uebersteuert"
    if stats["p95_abs"] >= 0.90:
        return "grenznah"
    if stats["flat_ratio"] >= 0.60 and stats["p95_abs"] <= 0.15:
        return "zu_flach"
    if stats["p95_abs"] <= 0.10:
        return "schwach"
    return "tragbar"


def _collect(candles: list[dict], mode: str) -> dict[str, list[float]]:
    profile = build_sensory_profile(candles) if mode == "world_relative" else None
    values: dict[str, list[float]] = defaultdict(list)
    for index in range(len(candles)):
        if mode == "world_relative":
            senses = build_senses_world_relative(candles, index, profile=profile)
        else:
            senses = build_senses(candles, index)
        for feature, root, key in FEATURES:
            source = dict(senses.get(root, {}) or {})
            if root == "mcm_feldwirkung" and key not in source:
                source = dict(senses.get("fuehlen", {}) or {})
            values[feature].append(_float(source.get(key)))
    return values


def _analyze_world(name: str, path: Path) -> list[dict[str, object]]:
    candles = load_candles(path)
    fixed = _collect(candles, "fixed")
    relative = _collect(candles, "world_relative")
    rows: list[dict[str, object]] = []
    for feature, _, _ in FEATURES:
        fixed_stats = _stats(fixed[feature])
        relative_stats = _stats(relative[feature])
        fixed_state = _feature_state(fixed_stats)
        relative_state = _feature_state(relative_stats)
        rows.append(
            {
                "world": name,
                "feature": feature,
                "fixed_state": fixed_state,
                "relative_state": relative_state,
                "fixed_p95_abs": fixed_stats["p95_abs"],
                "relative_p95_abs": relative_stats["p95_abs"],
                "fixed_saturation_ratio": fixed_stats["saturation_ratio"],
                "relative_saturation_ratio": relative_stats["saturation_ratio"],
                "fixed_flat_ratio": fixed_stats["flat_ratio"],
                "relative_flat_ratio": relative_stats["flat_ratio"],
                "fixed_mean_abs": fixed_stats["mean_abs"],
                "relative_mean_abs": relative_stats["mean_abs"],
                "state_change": f"{fixed_state}->{relative_state}",
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "feature",
        "fixed_state",
        "relative_state",
        "state_change",
        "fixed_p95_abs",
        "relative_p95_abs",
        "fixed_saturation_ratio",
        "relative_saturation_ratio",
        "fixed_flat_ratio",
        "relative_flat_ratio",
        "fixed_mean_abs",
        "relative_mean_abs",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    improved = [
        row
        for row in rows
        if row["fixed_state"] in {"uebersteuert", "grenznah", "zu_flach", "schwach"}
        and row["relative_state"] == "tragbar"
    ]
    worsened = [
        row
        for row in rows
        if row["fixed_state"] == "tragbar"
        and row["relative_state"] in {"uebersteuert", "grenznah", "zu_flach", "schwach"}
    ]
    unchanged_bad = [
        row
        for row in rows
        if row["fixed_state"] != "tragbar" and row["relative_state"] != "tragbar"
    ]
    lines = [
        "# Weltrelativer Wahrnehmungsadapter: Vergleich",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht die aktuelle feste Sinnesuebersetzung mit einem weltrelativen Adapter.",
        "Geprueft wird, ob MINI_DIO Welten dadurch einheitlicher sieht, hoert und in MCM-Feldwirkung uebersetzt.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.",
        "",
        "## Kurzbefund",
        "",
        f"Verbesserte Achsen: {len(improved)}",
        f"Verschlechterte Achsen: {len(worsened)}",
        f"Weiter auffaellige Achsen: {len(unchanged_bad)}",
        "",
        "## Vergleich",
        "",
        "| Welt | Achse | Zustand | p95 fest -> relativ | Saettigung fest -> relativ |",
        "|---|---|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["feature"]),
                    str(row["state_change"]),
                    f"{_fmt(_float(row['fixed_p95_abs']))}->{_fmt(_float(row['relative_p95_abs']))}",
                    f"{_fmt(_float(row['fixed_saturation_ratio']))}->{_fmt(_float(row['relative_saturation_ratio']))}",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Wenn der weltrelative Adapter Sättigung reduziert, spricht das dafuer, dass ein Teil der bisherigen Feldspannung aus der Uebersetzung kam.",
            "Wenn Achsen auffaellig bleiben, ist entweder die Welt tatsaechlich stark anders oder die Sinnesmechanik braucht eine organischere Adaptation.",
            "",
            "Der entscheidende Punkt: Das MCM-Feld sollte nicht Rohdatenlast verarbeiten, sondern bereits vorgeformte Sinnesinformation.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte ein kurzer passiver Mini-DIO-Lauf im `world_relative`-Sinnesmodus gegen die feste Uebersetzung verglichen werden. Erst wenn die Rollenkarte stabiler wird, sollte der Adapter als Standardmechanik in Betracht kommen.",
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
    args = parser.parse_args()

    worlds = args.world or [
        ("SOL_2023_5M_REAL1", "data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv"),
        ("SOL_2024_5M_REAL1", "data/kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv"),
        ("SOL_2024_1H_2K", "data/kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv"),
        ("BTC_2024_5M_2K", "data/kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv"),
        ("BTC_2024_1H_2K", "data/kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv"),
        ("SOL_2023_NEG_STRESS", "data/kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv"),
    ]
    rows: list[dict[str, object]] = []
    for name, raw_path in worlds:
        path = Path(raw_path)
        if not path.is_absolute():
            path = ROOT / path
        rows.extend(_analyze_world(name, path))

    out = args.out if args.out.is_absolute() else ROOT / args.out
    csv_out = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(rows, csv_out)
    _write_md(rows, out)


if __name__ == "__main__":
    main()
