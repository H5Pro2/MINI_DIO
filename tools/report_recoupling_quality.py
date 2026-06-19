from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "210_REKOPPLUNGSQUALITAET_DIAGNOSE.md"


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


def _sensor_state(candles: list[dict[str, float]]) -> dict[str, float]:
    stimuli = _stimulus_series(candles)
    if not stimuli:
        return {
            "attention_load": 0.0,
            "afterimage_load": 0.0,
            "sensor_load": 0.0,
            "adaptation_capacity": 0.0,
        }

    baseline = stimuli[0] or 1e-9
    attention_values: list[float] = []
    afterimage_values: list[float] = []
    relative_values: list[float] = []
    adaptation_values: list[float] = []
    afterimage = 0.0
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
        afterimage = (afterimage * 0.92) + (max(0.0, adapted - 1.0) * 0.08)
        attention = _clamp((novelty * 0.36) + (relative * 0.18) + (sensitization * 0.34) - (habituation * 0.22), 0.0, 3.0)

        attention_values.append(attention)
        afterimage_values.append(afterimage)
        relative_values.append(max(0.0, relative - 1.0))
        adaptation_values.append(max(0.0, habituation - sensitization))

    return {
        "attention_load": sum(attention_values) / len(attention_values),
        "afterimage_load": sum(afterimage_values) / len(afterimage_values),
        "sensor_load": sum(relative_values) / len(relative_values),
        "adaptation_capacity": _clamp((sum(adaptation_values) / len(adaptation_values)) + 0.5, 0.0, 1.0),
    }


def _row(name: str, summary: dict) -> dict:
    states = summary.get("episode_memory_states") or {}
    episodes = int((summary.get("episodes") or [0, 0])[1] or 0)
    field_strained = int(states.get("field_strained", 0) or 0)
    field_carried = int(states.get("field_carried", 0) or 0)
    episode_memory = int((summary.get("episode_memory_written") or [0, 0])[1] or 0)
    rekopplung = _second(summary.get("avg_mcm_rekopplung_quality"))
    carry = _second(summary.get("avg_mcm_carry_quality"))
    sensory = _second(summary.get("avg_mcm_sensory_coupling"))
    sensor = _sensor_state(_read_candles(str(summary.get("data_path", ""))))

    field_strain = field_strained / max(1, episodes)
    field_carry = field_carried / max(1, episodes)
    memory_load = episode_memory / max(1, episodes)
    recoupling_loss = _clamp(0.64 - rekopplung, 0.0, 1.0)
    carry_loss = _clamp(0.37 - carry, 0.0, 1.0)
    recoupling_strength = _clamp((rekopplung - 0.56) / 0.10, 0.0, 1.0)

    role_scores = {
        "reiz_aktiv_rekoppelnd": _clamp(
            (sensor["attention_load"] * 0.42)
            + (recoupling_strength * 0.34)
            + ((1.0 - field_strain) * 0.16)
            + (field_carry * 0.08)
        ),
        "last_bindend": _clamp(
            (field_strain * 0.42)
            + (recoupling_loss * 2.0 * 0.26)
            + (carry_loss * 2.0 * 0.14)
            + (sensor["afterimage_load"] * 0.18)
        ),
        "memory_bindend": _clamp(
            (memory_load * 0.52)
            + (recoupling_loss * 2.0 * 0.24)
            + (field_strain * 0.16)
            + (sensor["afterimage_load"] * 0.08)
        ),
        "nachhall_rekoppelnd": _clamp(
            (sensor["afterimage_load"] * 0.36)
            + (recoupling_strength * 0.30)
            + (sensor["adaptation_capacity"] * 0.20)
            + ((1.0 - memory_load) * 0.14)
        ),
        "feld_entrueckt": _clamp(
            (recoupling_loss * 2.2 * 0.36)
            + (carry_loss * 2.0 * 0.22)
            + ((1.0 - sensory) * 0.18)
            + (memory_load * 0.14)
            + (field_strain * 0.10)
        ),
    }
    active_score = role_scores["reiz_aktiv_rekoppelnd"]
    binding_sum = role_scores["last_bindend"] + role_scores["memory_bindend"] + role_scores["feld_entrueckt"]
    if binding_sum >= active_score * 1.15:
        dominant_role = "last_memory_bindend"
    elif binding_sum >= active_score * 0.70:
        dominant_role = "uebergang_bindend"
    elif role_scores["nachhall_rekoppelnd"] >= active_score * 0.85:
        dominant_role = "nachhall_rekoppelnd"
    else:
        dominant_role = "reiz_aktiv_rekoppelnd"

    return {
        "name": name,
        "episodes": episodes,
        "rekopplung": rekopplung,
        "carry": carry,
        "sensory": sensory,
        "field_strain": field_strain,
        "field_carry": field_carry,
        "memory_load": memory_load,
        "recoupling_loss": recoupling_loss,
        "carry_loss": carry_loss,
        "recoupling_strength": recoupling_strength,
        "binding_sum": binding_sum,
        "dominant_role": dominant_role,
        **sensor,
        **role_scores,
    }


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: row["name"])
    weak = sorted(rows, key=lambda row: row["recoupling_loss"], reverse=True)[:5]
    active = sorted(rows, key=lambda row: row["reiz_aktiv_rekoppelnd"], reverse=True)[:5]
    binding = sorted(rows, key=lambda row: row["last_bindend"] + row["memory_bindend"], reverse=True)[:5]

    lines = [
        "# Rekopplungsqualitaet - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft passiv, warum manche Welten trotz Aufmerksamkeit gut rekoppeln und andere in Feld-/Memorylast binden.",
        "Sie ist keine Handlung, kein Gate und keine Strategie.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Warum rekoppeln manche Welten besser als andere?",
        "2. Unterpruefung: Reizaktivitaet, Feldlast, Memorylast, Nachhall und Entrueckung getrennt lesen.",
        "3. Folgeschritt: Entscheiden, ob `last_bindend` und `reiz_aktiv_rekoppelnd` stabile passive Rollen sind.",
        "",
        "## Rollenkarte",
        "",
        "| Welt | Rolle | Rekopplung | Rek-Verlust | Feldlast | Memorylast | Aufmerksamkeit | Nachhall | aktiv-rekoppelnd | Bindungssumme | lastbindend | memorybindend | nachhall-rekoppelnd | feld-entrueckt |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["dominant_role"],
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["recoupling_loss"], 4),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["memory_load"], 4),
                    _fmt(row["attention_load"], 4),
                    _fmt(row["afterimage_load"], 4),
                    _fmt(row["reiz_aktiv_rekoppelnd"], 4),
                    _fmt(row["binding_sum"], 4),
                    _fmt(row["last_bindend"], 4),
                    _fmt(row["memory_bindend"], 4),
                    _fmt(row["nachhall_rekoppelnd"], 4),
                    _fmt(row["feld_entrueckt"], 4),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Schwaechste Rekopplung", ""])
    for row in weak:
        lines.append(
            f"- `{row['name']}`: Rekopplungsverlust `{_fmt(row['recoupling_loss'], 4)}`, "
            f"Feldlast `{_fmt(row['field_strain'], 4)}`, Memorylast `{_fmt(row['memory_load'], 4)}`, Rolle `{row['dominant_role']}`"
        )

    lines.extend(["", "## Reizaktiv aber rekoppelnd", ""])
    for row in active:
        lines.append(
            f"- `{row['name']}`: aktiv-rekoppelnd `{_fmt(row['reiz_aktiv_rekoppelnd'], 4)}`, "
            f"Aufmerksamkeit `{_fmt(row['attention_load'], 4)}`, Rekopplung `{_fmt(row['rekopplung'], 6)}`"
        )

    lines.extend(["", "## Last- und memorybindend", ""])
    for row in binding:
        lines.append(
            f"- `{row['name']}`: lastbindend `{_fmt(row['last_bindend'], 4)}`, "
            f"memorybindend `{_fmt(row['memory_bindend'], 4)}`, feld-entrueckt `{_fmt(row['feld_entrueckt'], 4)}`"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `reiz_aktiv_rekoppelnd`: Welt ist aufmerksamkeitsnah, aber das Feld kommt gut zurueck.",
            "- `last_bindend`: Feldlast und Rekopplungsverlust binden die Weltwirkung.",
            "- `memory_bindend`: Episodenspuren halten die Weltwirkung staerker im Feld.",
            "- `nachhall_rekoppelnd`: Nachhall ist da, bleibt aber mit Rekopplung verbunden.",
            "- `feld_entrueckt`: Rekopplung und Tragqualitaet sinken zusammen.",
            "",
            "## Befund",
            "",
            "Die Rollen sind passive Auswertungsnamen.",
            "Sie beschreiben keine festen Mechaniken im Kern.",
            "",
            "Wenn die Rollen ueber weitere Welten stabil bleiben, entsteht daraus eine Rekopplungslandkarte:",
            "Welche Welt wirkt aktiv und bleibt loesbar, welche bindet das Feld, welche schreibt Memorylast?",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird ein Befund geschrieben.",
            "Dabei steht die Unterscheidung zwischen `reiz_aktiv_rekoppelnd` und `last_bindend` im Mittelpunkt.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Rekopplungsqualitaets-Diagnose.")
    parser.add_argument("--summary", nargs=2, action="append", metavar=("NAME", "PATH"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for name, path_text in args.summary:
        rows.append(_row(name, _load_json(_resolve(path_text))))
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
