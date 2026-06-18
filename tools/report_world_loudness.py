from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "202_WELTLAUTSTAERKE_DIAGNOSE.md"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _second(values: object) -> float:
    if isinstance(values, list) and len(values) >= 2:
        return _float(values[1])
    return 0.0


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * q
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return values[int(index)]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _std(values: list[float]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def _resolve(path_text: str) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _read_world_metrics(path_text: str) -> dict[str, float]:
    path = _resolve(path_text)
    rows: list[dict[str, float]] = []
    if not path.exists():
        return {}

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(
                {
                    "open": _float(row.get("open")),
                    "high": _float(row.get("high")),
                    "low": _float(row.get("low")),
                    "close": _float(row.get("close")),
                    "volume": _float(row.get("volume")),
                }
            )

    closes = [row["close"] for row in rows]
    highs = [row["high"] for row in rows]
    lows = [row["low"] for row in rows]
    volumes = [row["volume"] for row in rows]

    returns = [
        (closes[index] - closes[index - 1]) / closes[index - 1]
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    abs_returns = [abs(value) for value in returns]
    ranges = [
        (high - low) / close
        for high, low, close in zip(highs, lows, closes)
        if close
    ]
    volume_changes = [
        abs((volumes[index] - volumes[index - 1]) / volumes[index - 1])
        for index in range(1, len(volumes))
        if volumes[index - 1]
    ]
    direction_changes = sum(
        1
        for index in range(2, len(closes))
        if (closes[index] - closes[index - 1]) * (closes[index - 1] - closes[index - 2]) < 0
    )

    drift = ((closes[-1] - closes[0]) / closes[0]) if closes else 0.0
    median_return = median(abs_returns) if abs_returns else 0.0
    median_range = median(ranges) if ranges else 0.0
    p95_return = _percentile(abs_returns, 0.95)
    p95_range = _percentile(ranges, 0.95)
    p99_return = _percentile(abs_returns, 0.99)
    p99_range = _percentile(ranges, 0.99)
    avg_abs_return = sum(abs_returns) / max(1, len(abs_returns))
    avg_range = sum(ranges) / max(1, len(ranges))
    avg_volume_change = sum(volume_changes) / max(1, len(volume_changes))

    # Passive Lautstaerke: robust gegen einzelne Extremkerzen, aber empfindlich fuer
    # wiederkehrende Bewegung, Kerzenkoerper und Volumenrhythmus.
    loudness = (
        (avg_abs_return * 1000.0 * 0.30)
        + (p95_return * 1000.0 * 0.25)
        + (avg_range * 1000.0 * 0.25)
        + (p95_range * 1000.0 * 0.15)
        + (min(avg_volume_change, 5.0) * 0.05)
    )

    return {
        "candles": float(len(rows)),
        "avg_abs_return": avg_abs_return,
        "median_abs_return": median_return,
        "p95_abs_return": p95_return,
        "p99_abs_return": p99_return,
        "std_return": _std(returns),
        "avg_range": avg_range,
        "median_range": median_range,
        "p95_range": p95_range,
        "p99_range": p99_range,
        "avg_volume_change": avg_volume_change,
        "direction_changes": float(direction_changes),
        "direction_change_ratio": direction_changes / max(1, len(closes) - 2),
        "drift": drift,
        "world_loudness": loudness,
    }


def _summary_row(name: str, summary: dict) -> dict:
    states = summary.get("episode_memory_states") or {}
    episodes = int((summary.get("episodes") or [0, 0])[1] or 0)
    field_strained = int(states.get("field_strained", 0) or 0)
    field_carried = int(states.get("field_carried", 0) or 0)
    profile = summary.get("passive_mcm_effect_classes") or {}
    tension = int(profile.get("gespannt", 0) or 0) + int(profile.get("kippend", 0) or 0)
    data_path = str(summary.get("data_path", ""))
    metrics = _read_world_metrics(data_path)
    row = {
        "name": name,
        "data_path": data_path,
        "rekopplung": _second(summary.get("avg_mcm_rekopplung_quality")),
        "carry": _second(summary.get("avg_mcm_carry_quality")),
        "sensory": _second(summary.get("avg_mcm_sensory_coupling")),
        "episode_memory": int((summary.get("episode_memory_written") or [0, 0])[1] or 0),
        "episodes": episodes,
        "field_strained": field_strained,
        "field_carried": field_carried,
        "field_strained_ratio": field_strained / max(1, episodes),
        "field_carried_ratio": field_carried / max(1, episodes),
        "tension": tension,
        "metrics": metrics,
    }
    loudness = metrics.get("world_loudness", 0.0)
    row["strain_per_loudness"] = row["field_strained_ratio"] / max(0.000001, loudness)
    row["memory_per_loudness"] = row["episode_memory"] / max(0.000001, loudness)
    return row


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: row["name"])

    lines = [
        "# Weltlautstaerke-Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob unterschiedliche Welten unterschiedlich laut oder intensiv in MINI_DIO ankommen.",
        "Sie trennt Rohwelt-Lautstaerke von MCM-Feldwirkung.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Ist die staerkere Feldlast eine reale Weltwirkung oder eine Sensorik-/Normierungsfrage?",
        "2. Unterpruefung: Wie verhalten sich Rohwelt-Lautstaerke, Rekopplung, Strain und Episodenmemory zueinander?",
        "3. Folgeschritt: Entscheiden, ob eine bessere Welt-Normierung oder eine separate Verdichtungs-Sensitivitaet notwendig ist.",
        "",
        "## Uebersicht",
        "",
        "| Welt | Lautstaerke | avg_ret | p95_ret | avg_range | p95_range | Strain | Memory | Rekopplung | Tragqualitaet |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in rows:
        metrics = row["metrics"]
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(metrics.get("world_loudness", 0.0), 3),
                    _fmt(metrics.get("avg_abs_return", 0.0), 6),
                    _fmt(metrics.get("p95_abs_return", 0.0), 6),
                    _fmt(metrics.get("avg_range", 0.0), 6),
                    _fmt(metrics.get("p95_range", 0.0), 6),
                    str(row["field_strained"]),
                    str(row["episode_memory"]),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["carry"], 6),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Sensitivitaet",
            "",
            "| Welt | Strain/Lautstaerke | Memory/Lautstaerke | field_strained_ratio | field_carried_ratio | Richtungswechsel | Drift |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        metrics = row["metrics"]
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(row["strain_per_loudness"], 6),
                    _fmt(row["memory_per_loudness"], 3),
                    _fmt(row["field_strained_ratio"], 4),
                    _fmt(row["field_carried_ratio"], 4),
                    str(int(metrics.get("direction_changes", 0.0))),
                    _fmt(metrics.get("drift", 0.0), 6),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Lautstaerke ist keine Feldklasse. Sie beschreibt nur, wie stark die Rohwelt durch Bewegung, Range und Volumenrhythmus auftritt.",
            "",
            "Wenn eine Welt bei vergleichbarer Lautstaerke deutlich mehr `field_strained` oder Episodenmemory erzeugt, spricht das fuer andere Verdichtungs-Sensitivitaet.",
            "Wenn eine Welt zugleich lauter ist und staerker kippt, muss geprueft werden, ob die Sensorik sauber asset-relativ normiert ist.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus dieser Diagnose eine Verdichtungs-Sensitivitaetskarte entstehen.",
            "Sie soll nicht regulieren und keine Handlung ausloesen, sondern nur zeigen, welche Welten bei welcher Zeitaufloesung ueberproportional viel Innenfeldlast erzeugen.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Weltlautstaerke-Diagnose.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        rows.append(_summary_row(name, _load_json(_resolve(path_text))))
    _write_markdown(rows, _resolve(str(args.out)))


if __name__ == "__main__":
    main()
