from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "206_ORGANISCHE_REIZADAPTATION_DIAGNOSE.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


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


def _read_candles(path_text: str) -> list[dict[str, float]]:
    path = _resolve(path_text)
    if not path.exists():
        return []
    rows: list[dict[str, float]] = []
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
    return rows


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _stimulus_series(candles: list[dict[str, float]]) -> list[float]:
    if len(candles) < 2:
        return []
    volumes = [row["volume"] for row in candles]
    volume_changes = [0.0]
    for index in range(1, len(volumes)):
        previous = volumes[index - 1]
        volume_changes.append(abs((volumes[index] - previous) / previous) if previous else 0.0)

    values: list[float] = []
    for index in range(1, len(candles)):
        current = candles[index]
        previous = candles[index - 1]
        close = current["close"]
        previous_close = previous["close"]
        if not close or not previous_close:
            values.append(0.0)
            continue
        abs_return = abs((close - previous_close) / previous_close)
        candle_range = (current["high"] - current["low"]) / close
        volume_change = min(volume_changes[index], 5.0)
        # Reizstaerke bleibt asset-relativ: Bewegung, Range und Volumenrhythmus
        # werden zu einer neutralen sensorischen Last verdichtet.
        values.append((abs_return * 0.42) + (candle_range * 0.42) + (volume_change * 0.0016))
    return values


def _adaptation_metrics(candles: list[dict[str, float]]) -> dict[str, float]:
    stimuli = _stimulus_series(candles)
    if not stimuli:
        return {
            "ticks": 0.0,
            "avg_stimulus": 0.0,
            "p95_stimulus": 0.0,
            "avg_relative_stimulus": 0.0,
            "p95_relative_stimulus": 0.0,
            "adapted_load": 0.0,
            "avg_habituation": 0.0,
            "avg_sensitization": 0.0,
            "end_habituation": 0.0,
            "end_sensitization": 0.0,
            "attention_salience": 0.0,
            "thalamic_pass_ratio": 0.0,
            "homeostatic_balance": 0.0,
        }

    baseline = stimuli[0] or 1e-9
    relative_values: list[float] = []
    adapted_values: list[float] = []
    salience_values: list[float] = []
    habituation_values: list[float] = []
    sensitization_values: list[float] = []
    thalamic_passes = 0
    habituation = 0.0
    sensitization = 0.0

    for index, stimulus in enumerate(stimuli):
        baseline = (baseline * 0.94) + (stimulus * 0.06)
        relative = stimulus / max(1e-9, baseline)
        previous = stimuli[index - 1] if index else stimulus
        novelty = abs(stimulus - previous) / max(1e-9, baseline)

        mild_repetition = relative < 1.18 and novelty < 0.28
        relevant_pressure = relative > 1.72 or novelty > 1.12

        if mild_repetition:
            habituation = min(1.0, (habituation * 0.985) + 0.030)
        else:
            habituation *= 0.955

        if relevant_pressure:
            sensitization = min(1.0, (sensitization * 0.970) + 0.080)
        else:
            sensitization *= 0.940

        adapted = relative * (1.0 - (habituation * 0.42)) * (1.0 + (sensitization * 0.35))
        salience = _clamp((novelty * 0.36) + (relative * 0.18) + (sensitization * 0.34) - (habituation * 0.22), 0.0, 3.0)
        if salience >= 0.72:
            thalamic_passes += 1

        relative_values.append(relative)
        adapted_values.append(adapted)
        salience_values.append(salience)
        habituation_values.append(habituation)
        sensitization_values.append(sensitization)

    avg_relative = sum(relative_values) / len(relative_values)
    avg_adapted = sum(adapted_values) / len(adapted_values)
    avg_salience = sum(salience_values) / len(salience_values)
    thalamic_ratio = thalamic_passes / max(1, len(stimuli))
    homeostatic_balance = _clamp(1.0 - abs(avg_adapted - 1.0), 0.0, 1.0)

    return {
        "ticks": float(len(stimuli)),
        "avg_stimulus": sum(stimuli) / len(stimuli),
        "p95_stimulus": _percentile(stimuli, 0.95),
        "avg_relative_stimulus": avg_relative,
        "p95_relative_stimulus": _percentile(relative_values, 0.95),
        "adapted_load": avg_adapted,
        "avg_habituation": sum(habituation_values) / len(habituation_values),
        "avg_sensitization": sum(sensitization_values) / len(sensitization_values),
        "end_habituation": habituation,
        "end_sensitization": sensitization,
        "attention_salience": avg_salience,
        "thalamic_pass_ratio": thalamic_ratio,
        "homeostatic_balance": homeostatic_balance,
    }


def _row(name: str, summary: dict) -> dict:
    states = summary.get("episode_memory_states") or {}
    episodes = int((summary.get("episodes") or [0, 0])[1] or 0)
    field_strained = int(states.get("field_strained", 0) or 0)
    field_carried = int(states.get("field_carried", 0) or 0)
    metrics = _adaptation_metrics(_read_candles(str(summary.get("data_path", ""))))
    return {
        "name": name,
        "episodes": episodes,
        "field_strained": field_strained,
        "field_carried": field_carried,
        "field_strained_ratio": field_strained / max(1, episodes),
        "field_carried_ratio": field_carried / max(1, episodes),
        "rekopplung": _second(summary.get("avg_mcm_rekopplung_quality")),
        "carry": _second(summary.get("avg_mcm_carry_quality")),
        "episode_memory": int((summary.get("episode_memory_written") or [0, 0])[1] or 0),
        "metrics": metrics,
    }


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: row["name"])

    lines = [
        "# Organische Reizadaptation - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob MINI_DIO eine organische Reizvorstufe benoetigt:",
        "",
        "- sensorische Adaptation",
        "- Aufmerksamkeitsfilter",
        "- thalamische Filterung als passive Weiterleitungsdiagnose",
        "- Habituation",
        "- Sensitivierung",
        "- Homoestase / Allostase",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-System.",
        "Die Diagnose beschreibt nur, wie eine Welt sensorisch getragen oder ueberreizend gelesen werden kann.",
        "",
        "## Hierarchie der Pruefung",
        "",
        "1. Grundfrage: Wirkt Weltlautstaerke dauerhaft gleich stark, oder passt sich das Innenfeld organisch an?",
        "2. Unterpruefung: Welche Welten erzeugen Habituation, Sensitivierung oder hohe bewusste Weiterleitung?",
        "3. Folgeschritt: Entscheiden, ob diese Vorstufe spaeter in die passive MCM-Feldlesung uebernommen wird.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | rel. Reiz | p95 rel. Reiz | adaptierte Last | Habituation avg/end | Sensitivierung avg/end | Aufmerksamkeit | thalamische Weiterleitung | Homoestase | Strain | Rekopplung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        metrics = row["metrics"]
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(metrics["avg_relative_stimulus"], 3),
                    _fmt(metrics["p95_relative_stimulus"], 3),
                    _fmt(metrics["adapted_load"], 3),
                    f"{_fmt(metrics['avg_habituation'], 3)}/{_fmt(metrics['end_habituation'], 3)}",
                    f"{_fmt(metrics['avg_sensitization'], 3)}/{_fmt(metrics['end_sensitization'], 3)}",
                    _fmt(metrics["attention_salience"], 3),
                    _fmt(metrics["thalamic_pass_ratio"], 3),
                    _fmt(metrics["homeostatic_balance"], 3),
                    str(row["field_strained"]),
                    _fmt(row["rekopplung"], 6),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `rel. Reiz`: Wie stark die aktuelle Welt gegen ihre eigene lokale Basis wirkt.",
            "- `adaptierte Last`: Reiz nach Gewoehnung und Sensitivierung.",
            "- `Habituation avg/end`: durchschnittliche Gewoehnung und Endzustand.",
            "- `Sensitivierung avg/end`: durchschnittliche Empfindlicher-Werdung und Endzustand.",
            "- `Aufmerksamkeit`: passive Salienz aus Neuheit, Reizstaerke, Sensitivierung und Habituation.",
            "- `thalamische Weiterleitung`: Anteil der Ticks, die diagnostisch bewusst genug waeren.",
            "- `Homoestase`: Naehe der adaptierten Last zu einem tragfaehigen Arbeitsbereich.",
            "",
            "## Befund",
            "",
            "MINI_DIO sollte laute Welten nicht nur limitieren.",
            "Organisch sauberer ist eine Vorstufe, die Reize relativ zur eigenen Weltbasis liest.",
            "",
            "Dauerreiz kann dadurch abklingen, ohne blind zu werden.",
            "Wiederkehrende relevante Reize koennen gleichzeitig empfindlicher machen.",
            "Das entspricht eher einem Nervensystem als einem starren Limiter.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird aus dieser Diagnose ein Befund erstellt:",
            "Welche Welten zeigen eher Habituation, welche eher Sensitivierung, und wo bleibt die MCM-Feldlage am tragfaehigsten?",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Diagnose zur organischen Reizadaptation.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        rows.append(_row(name, _load_json(_resolve(path_text))))
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
