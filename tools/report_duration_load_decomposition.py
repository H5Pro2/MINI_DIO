from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "208_DAUERLAST_ZERLEGUNG_DIAGNOSE.md"


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


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


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
        candle_range = max(0.0, current["high"] - current["low"]) / close
        volume_change = min(volume_changes[index], 5.0)
        values.append((abs_return * 0.42) + (candle_range * 0.42) + (volume_change * 0.0016))
    return values


def _sensor_decomposition(candles: list[dict[str, float]]) -> dict[str, float]:
    stimuli = _stimulus_series(candles)
    if not stimuli:
        return {
            "sensor_load": 0.0,
            "persistent_load": 0.0,
            "afterimage_load": 0.0,
            "attention_load": 0.0,
            "distance_need": 0.0,
            "adaptation_capacity": 0.0,
        }

    baseline = stimuli[0] or 1e-9
    relative_values: list[float] = []
    afterimage_values: list[float] = []
    attention_values: list[float] = []
    adaptation_values: list[float] = []
    afterimage = 0.0
    habituation = 0.0
    sensitization = 0.0
    persistent_ticks = 0

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
        excess = max(0.0, adapted - 1.0)
        afterimage = (afterimage * 0.92) + (excess * 0.08)
        attention = _clamp((novelty * 0.36) + (relative * 0.18) + (sensitization * 0.34) - (habituation * 0.22), 0.0, 3.0)
        if adapted > 1.0:
            persistent_ticks += 1

        relative_values.append(relative)
        afterimage_values.append(afterimage)
        attention_values.append(attention)
        adaptation_values.append(max(0.0, habituation - sensitization))

    sensor_load = sum(max(0.0, value - 1.0) for value in relative_values) / len(relative_values)
    persistent_load = persistent_ticks / max(1, len(stimuli))
    afterimage_load = sum(afterimage_values) / len(afterimage_values)
    attention_load = sum(attention_values) / len(attention_values)
    adaptation_capacity = _clamp((sum(adaptation_values) / len(adaptation_values)) + 0.5, 0.0, 1.0)
    distance_need = _clamp((afterimage_load * 1.8) + (persistent_load * 0.55) + (attention_load * 0.35), 0.0, 1.0)

    return {
        "sensor_load": sensor_load,
        "persistent_load": persistent_load,
        "afterimage_load": afterimage_load,
        "attention_load": attention_load,
        "distance_need": distance_need,
        "adaptation_capacity": adaptation_capacity,
    }


def _row(name: str, summary: dict) -> dict:
    states = summary.get("episode_memory_states") or {}
    episodes = int((summary.get("episodes") or [0, 0])[1] or 0)
    field_strained = int(states.get("field_strained", 0) or 0)
    field_carried = int(states.get("field_carried", 0) or 0)
    episode_memory = int((summary.get("episode_memory_written") or [0, 0])[1] or 0)
    rekopplung = _second(summary.get("avg_mcm_rekopplung_quality"))
    carry = _second(summary.get("avg_mcm_carry_quality"))
    sensor = _sensor_decomposition(_read_candles(str(summary.get("data_path", ""))))

    field_strain_load = field_strained / max(1, episodes)
    field_carry_ratio = field_carried / max(1, episodes)
    memory_load = episode_memory / max(1, episodes)
    recoupling_loss = _clamp(0.64 - rekopplung, 0.0, 1.0)
    carry_loss = _clamp(0.37 - carry, 0.0, 1.0)
    mcm_duration_load = _clamp(
        (field_strain_load * 0.34)
        + (memory_load * 0.24)
        + (recoupling_loss * 0.22)
        + (sensor["afterimage_load"] * 0.14)
        + (carry_loss * 0.06),
        0.0,
        1.0,
    )
    distance_gap = _clamp(sensor["distance_need"] - sensor["adaptation_capacity"], 0.0, 1.0)

    return {
        "name": name,
        "episodes": episodes,
        "field_strain_load": field_strain_load,
        "field_carry_ratio": field_carry_ratio,
        "memory_load": memory_load,
        "recoupling_loss": recoupling_loss,
        "carry_loss": carry_loss,
        "mcm_duration_load": mcm_duration_load,
        "distance_gap": distance_gap,
        "rekopplung": rekopplung,
        "carry": carry,
        **sensor,
    }


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: row["name"])
    top_duration = sorted(rows, key=lambda row: row["mcm_duration_load"], reverse=True)[:4]
    top_distance = sorted(rows, key=lambda row: row["distance_gap"], reverse=True)[:4]

    lines = [
        "# Dauerlast-Zerlegung - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose zerlegt Dauerlast in mehrere passive Quellen.",
        "Sie prueft nicht, ob gehandelt werden soll.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Woher kommt Dauerlast im MCM-Feld?",
        "2. Unterpruefung: Sensorik, Nachhall, Memory, Rekopplung und Distanzierung getrennt lesen.",
        "3. Folgeschritt: Entscheiden, ob eine Distanzierungs-Vorstufe notwendig ist.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | sensorische Last | Persistenz | Nachhall | Aufmerksamkeit | Adaptionskapazitaet | Distanzbedarf | Distanzluecke | Feldlast | Memorylast | Rekopplungsverlust | Dauerlast gesamt |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(row["sensor_load"], 4),
                    _fmt(row["persistent_load"], 4),
                    _fmt(row["afterimage_load"], 4),
                    _fmt(row["attention_load"], 4),
                    _fmt(row["adaptation_capacity"], 4),
                    _fmt(row["distance_need"], 4),
                    _fmt(row["distance_gap"], 4),
                    _fmt(row["field_strain_load"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["recoupling_loss"], 4),
                    _fmt(row["mcm_duration_load"], 4),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Staerkste Dauerlast", ""])
    for row in top_duration:
        lines.append(
            f"- `{row['name']}`: Dauerlast `{_fmt(row['mcm_duration_load'], 4)}`, "
            f"Feldlast `{_fmt(row['field_strain_load'], 4)}`, Memorylast `{_fmt(row['memory_load'], 4)}`, "
            f"Rekopplungsverlust `{_fmt(row['recoupling_loss'], 4)}`"
        )

    lines.extend(["", "## Staerkste Distanzluecke", ""])
    for row in top_distance:
        lines.append(
            f"- `{row['name']}`: Distanzluecke `{_fmt(row['distance_gap'], 4)}`, "
            f"Distanzbedarf `{_fmt(row['distance_need'], 4)}`, Adaptionskapazitaet `{_fmt(row['adaptation_capacity'], 4)}`"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `sensorische Last`: akute Reizueberschreitung gegen lokale Basis.",
            "- `Persistenz`: Anteil der Ticks, in denen die adaptierte Last ueber dem Arbeitsbereich bleibt.",
            "- `Nachhall`: Restspur wiederholter Last nach Adaptation.",
            "- `Adaptionskapazitaet`: Gewoehnung minus Sensitivierung, auf einen tragbaren Bereich bezogen.",
            "- `Distanzluecke`: wenn Distanzbedarf groesser ist als Adaptionskapazitaet.",
            "- `Dauerlast gesamt`: passive Zusammenfassung aus Feldlast, Memorylast, Rekopplungsverlust und Nachhall.",
            "",
            "## Befund",
            "",
            "Dauerlast ist nicht identisch mit akuter Lautstaerke.",
            "Sie entsteht, wenn Last ueber Zeit im Feld bleibt, Memoryspuren erzeugt und die Rekopplung sinkt.",
            "",
            "Die Distanzierungsfrage ist damit fachlich berechtigt:",
            "Wenn Distanzbedarf und Nachhall steigen, aber Adaptionskapazitaet nicht mitkommt, wird Weltspannung zu Innenfeldlast.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus dieser Diagnose ein Befund geschrieben werden.",
            "Darin wird festgehalten, ob SOL 1h eher durch Sensorik, durch Nachhall oder durch Rekopplungsverlust zur Dauerlast wird.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Zerlegt passive Dauerlast in Sensorik, Nachhall, Memory und Rekopplung.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        rows.append(_row(name, _load_json(_resolve(path_text))))
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
