from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

from report_harmonic_sol5m_reference import DEFAULT_SUMMARIES
from report_recoupling_quality import _load_json, _resolve
from report_recoupling_quality import _row as recoupling_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "224_AUDITIVE_REGULATION_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


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


def _sound_series(candles: list[dict[str, float]]) -> list[float]:
    if len(candles) < 2:
        return []
    volumes = [row["volume"] for row in candles]
    values: list[float] = []
    for index in range(1, len(candles)):
        current = candles[index]
        previous = candles[index - 1]
        if not previous["close"] or not current["close"]:
            values.append(0.0)
            continue
        abs_return = abs((current["close"] - previous["close"]) / previous["close"])
        candle_range = max(0.0, current["high"] - current["low"]) / current["close"]
        previous_volume = volumes[index - 1]
        volume_change = abs((volumes[index] - previous_volume) / previous_volume) if previous_volume else 0.0
        # Auditive Weltenergie: Bewegung und Range bilden den Hauptton,
        # Volumenveraenderung moduliert die Lautheit nur schwach.
        values.append((abs_return * 0.44) + (candle_range * 0.44) + (min(volume_change, 5.0) * 0.0012))
    return values


def _auditory_metrics(candles: list[dict[str, float]]) -> dict:
    sounds = _sound_series(candles)
    if not sounds:
        return {
            "avg_sound": 0.0,
            "p95_sound": 0.0,
            "avg_focus": 0.0,
            "avg_alarm": 0.0,
            "avg_soothing": 0.0,
            "avg_background": 0.0,
            "avg_aftertone": 0.0,
            "dominant_state": "stille",
            "state_counts": {},
        }

    baseline = sounds[0] or 1e-9
    aftertone = 0.0
    held_focus = 0.0
    focus_values: list[float] = []
    alarm_values: list[float] = []
    soothing_values: list[float] = []
    background_values: list[float] = []
    aftertone_values: list[float] = []
    states: list[str] = []

    for index, sound in enumerate(sounds):
        baseline = (baseline * 0.94) + (sound * 0.06)
        relative = sound / max(1e-9, baseline)
        previous = sounds[index - 1] if index else sound
        tone_shift = abs(sound - previous) / max(1e-9, baseline)

        alarm = _clamp((max(0.0, relative - 1.35) * 0.52) + (tone_shift * 0.34))
        listen = _clamp((relative * 0.24) + (tone_shift * 0.36) + (alarm * 0.24))
        close_listen = _clamp((alarm * 0.38) + (tone_shift * 0.42) + (held_focus * 0.20))
        soothing = _clamp((1.0 - abs(relative - 1.0)) * (1.0 - min(1.0, tone_shift * 2.0)))
        background = _clamp((1.0 - listen) * 0.70 + soothing * 0.30)
        aftertone = (aftertone * 0.90) + (max(0.0, listen - 0.40) * 0.10)
        held_focus = _clamp((held_focus * 0.82) + (close_listen * 0.18))

        if alarm > 0.58:
            state = "alarm_hoeren"
        elif close_listen > 0.50:
            state = "genauer_anhoeren"
        elif listen > 0.46:
            state = "hinhoeren"
        elif soothing > 0.70 and aftertone < 0.35:
            state = "beruhigung_hoeren"
        elif background > 0.64:
            state = "hintergrund_hoeren"
        elif aftertone > 0.18 and listen < 0.42:
            state = "reiz_abklingen_lassen"
        else:
            state = "rauschen_filtern"

        states.append(state)
        focus_values.append(max(listen, close_listen))
        alarm_values.append(alarm)
        soothing_values.append(soothing)
        background_values.append(background)
        aftertone_values.append(aftertone)

    counts = Counter(states)
    dominant_state = counts.most_common(1)[0][0]
    return {
        "avg_sound": sum(sounds) / len(sounds),
        "p95_sound": _percentile(sounds, 0.95),
        "avg_focus": sum(focus_values) / len(focus_values),
        "avg_alarm": sum(alarm_values) / len(alarm_values),
        "avg_soothing": sum(soothing_values) / len(soothing_values),
        "avg_background": sum(background_values) / len(background_values),
        "avg_aftertone": sum(aftertone_values) / len(aftertone_values),
        "dominant_state": dominant_state,
        "state_counts": dict(counts),
    }


def _row(name: str, path_text: str, group: str) -> dict:
    summary = _load_json(_resolve(path_text))
    rec = recoupling_row(name, summary)
    metrics = _auditory_metrics(_read_candles(str(summary.get("data_path", ""))))
    state_counts = metrics["state_counts"]
    total_states = max(1, sum(int(value) for value in state_counts.values()))
    return {
        "name": name,
        "group": group,
        "role": rec["dominant_role"],
        "rekopplung": rec["rekopplung"],
        "field_strain": rec["field_strain"],
        "memory_load": rec["memory_load"],
        **metrics,
        "hinhoeren_ratio": state_counts.get("hinhoeren", 0) / total_states,
        "genauer_ratio": state_counts.get("genauer_anhoeren", 0) / total_states,
        "alarm_ratio": state_counts.get("alarm_hoeren", 0) / total_states,
        "hintergrund_ratio": state_counts.get("hintergrund_hoeren", 0) / total_states,
        "beruhigung_ratio": state_counts.get("beruhigung_hoeren", 0) / total_states,
        "rauschen_ratio": state_counts.get("rauschen_filtern", 0) / total_states,
        "abklingen_ratio": state_counts.get("reiz_abklingen_lassen", 0) / total_states,
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))

    lines = [
        "# Auditive Regulation - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die Marktenergie als passive Hoerachse.",
        "Sie prueft, ob MINI_DIO zwischen Hinhoeren, Rauschenfiltern, Reizabklingen, genauerem Anhoeren, Alarm, Hintergrund und Beruhigung unterscheiden kann.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Wie reguliert ein MCM-Feld auditive Weltenergie, ohne sie direkt ins Handeln zu uebersetzen?",
        "2. Unterpruefung: Tonstaerke, Tonwechsel, Fokus, Alarm, Hintergrund, Beruhigung und Nachton je Welt lesen.",
        "3. Folgeschritt: Pruefen, welche Hoerzustande harmonische Rekopplung beguenstigen oder Feldlast begleiten.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | dominanter Hoerzustand | Ton avg | Ton p95 | Fokus | Alarm | Beruhigung | Hintergrund | Nachton | Rekopplung | Feldlast | Memorylast |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["role"],
                    row["dominant_state"],
                    _fmt(row["avg_sound"], 6),
                    _fmt(row["p95_sound"], 6),
                    _fmt(row["avg_focus"], 4),
                    _fmt(row["avg_alarm"], 4),
                    _fmt(row["avg_soothing"], 4),
                    _fmt(row["avg_background"], 4),
                    _fmt(row["avg_aftertone"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["field_strain"], 4),
                    _fmt(row["memory_load"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Hoerzustandsanteile",
            "",
            "| Welt | Hinhoeren | genauer | Alarm | Hintergrund | Beruhigung | Rauschen filtern | Reiz abklingen |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(row["hinhoeren_ratio"], 4),
                    _fmt(row["genauer_ratio"], 4),
                    _fmt(row["alarm_ratio"], 4),
                    _fmt(row["hintergrund_ratio"], 4),
                    _fmt(row["beruhigung_ratio"], 4),
                    _fmt(row["rauschen_ratio"], 4),
                    _fmt(row["abklingen_ratio"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `hinhoeren`: Ton wirkt relevant genug, um Aufmerksamkeit zu bekommen.",
            "- `genauer_anhoeren`: Tonwechsel oder Fokusspur braucht feinere Betrachtung.",
            "- `alarm_hoeren`: starke relative Tonveraenderung oder Lautheitsdruck.",
            "- `hintergrund_hoeren`: Ton bleibt als Weltgrund vorhanden, ohne Dominanz.",
            "- `beruhigung_hoeren`: gleichmaessiger Ton wirkt potenziell rekoppelnd.",
            "- `rauschen_filtern`: Tonanteil wird als nicht strukturtragend gedaempft.",
            "- `reiz_abklingen_lassen`: gehoerter Reiz darf auslaufen, ohne weiter Feldlast zu werden.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Auditive Regulation sollte als eigene Sinnesregulation gelesen werden.",
            "Tonenergie darf das MCM-Feld stimulieren, aber nicht jede Tonspur darf gleich stark Bedeutung erzeugen.",
            "",
            "Eine organische Hoerachse kann erklaeren, warum eine Welt aktiv bleibt, ohne sofort zu binden:",
            "MINI_DIO kann hinhoeren, genauer hinhoeren, Hintergrund halten, Rauschen filtern oder Reizwirkung abklingen lassen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dort wird geprueft, welche Hoerzustande bei SOL 5m gegen SOL 30m/1h und Stresssegmente dominieren.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Diagnose zur auditiven Regulation.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
