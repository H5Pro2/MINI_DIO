from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "204_VERDICHTUNGS_SENSITIVITAET.md"
TIMEFRAME_MINUTES = {"5m": 5, "15m": 15, "30m": 30, "1h": 60}


def _resolve(path_text: str) -> Path:
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


def _world_loudness(data_path_text: str) -> float:
    path = _resolve(data_path_text)
    if not path.exists():
        return 0.0
    closes: list[float] = []
    highs: list[float] = []
    lows: list[float] = []
    volumes: list[float] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            closes.append(_float(row.get("close")))
            highs.append(_float(row.get("high")))
            lows.append(_float(row.get("low")))
            volumes.append(_float(row.get("volume")))

    returns = [
        abs((closes[index] - closes[index - 1]) / closes[index - 1])
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
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
    avg_abs_return = sum(returns) / max(1, len(returns))
    avg_range = sum(ranges) / max(1, len(ranges))
    p95_return = _percentile(returns, 0.95)
    p95_range = _percentile(ranges, 0.95)
    avg_volume_change = sum(volume_changes) / max(1, len(volume_changes))
    return (
        (avg_abs_return * 1000.0 * 0.30)
        + (p95_return * 1000.0 * 0.25)
        + (avg_range * 1000.0 * 0.25)
        + (p95_range * 1000.0 * 0.15)
        + (min(avg_volume_change, 5.0) * 0.05)
    )


def _row(asset: str, year: str, timeframe: str, summary: dict) -> dict:
    states = summary.get("episode_memory_states") or {}
    episodes = int((summary.get("episodes") or [0, 0])[1] or 0)
    field_strained = int(states.get("field_strained", 0) or 0)
    field_carried = int(states.get("field_carried", 0) or 0)
    data_path = str(summary.get("data_path", ""))
    loudness = _world_loudness(data_path)
    return {
        "asset": asset,
        "year": year,
        "timeframe": timeframe,
        "minutes": TIMEFRAME_MINUTES.get(timeframe, 0),
        "name": f"{asset}_{year}_{timeframe}",
        "loudness": loudness,
        "rekopplung": _second(summary.get("avg_mcm_rekopplung_quality")),
        "carry": _second(summary.get("avg_mcm_carry_quality")),
        "sensory": _second(summary.get("avg_mcm_sensory_coupling")),
        "episode_memory": int((summary.get("episode_memory_written") or [0, 0])[1] or 0),
        "episodes": episodes,
        "field_strained": field_strained,
        "field_carried": field_carried,
        "field_strained_ratio": field_strained / max(1, episodes),
        "field_carried_ratio": field_carried / max(1, episodes),
    }


def _delta(a: dict, b: dict) -> dict:
    minute_delta = max(1.0, float(b["minutes"] - a["minutes"]))
    loudness_delta = b["loudness"] - a["loudness"]
    strain_delta = b["field_strained"] - a["field_strained"]
    memory_delta = b["episode_memory"] - a["episode_memory"]
    rek_delta = b["rekopplung"] - a["rekopplung"]
    carry_delta = b["carry"] - a["carry"]
    return {
        "from": a["timeframe"],
        "to": b["timeframe"],
        "minute_delta": minute_delta,
        "loudness_delta": loudness_delta,
        "strain_delta": strain_delta,
        "memory_delta": memory_delta,
        "rek_delta": rek_delta,
        "carry_delta": carry_delta,
        "strain_per_loudness_delta": strain_delta / max(0.000001, loudness_delta),
        "memory_per_loudness_delta": memory_delta / max(0.000001, loudness_delta),
        "rek_loss_per_loudness_delta": (-rek_delta) / max(0.000001, loudness_delta),
        "carry_loss_per_loudness_delta": (-carry_delta) / max(0.000001, loudness_delta),
    }


def _fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def _group_rows(rows: list[dict]) -> dict[tuple[str, str], list[dict]]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        groups.setdefault((row["asset"], row["year"]), []).append(row)
    for key in groups:
        groups[key] = sorted(groups[key], key=lambda item: item["minutes"])
    return groups


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    groups = _group_rows(rows)

    lines = [
        "# Verdichtungs-Sensitivitaet",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose misst passiv, wie empfindlich eine Welt auf zeitliche Verdichtung reagiert.",
        "Sie ist keine Regel, kein Gate und keine Handlungsempfehlung.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Wie stark veraendert Zeitverdichtung die MCM-Feldwirkung?",
        "2. Unterpruefung: Steigen Lautstaerke, Strain und Memory proportional oder ueberproportional?",
        "3. Folgeschritt: Unterscheiden, ob eine Welt nur lauter wird oder ob das Innenfeld ueberempfindlich reagiert.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Minuten | Lautstaerke | Strain | Memory | Rekopplung | Tragqualitaet | field_carried_ratio |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: (item["asset"], item["year"], item["minutes"])):
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    str(row["minutes"]),
                    _fmt(row["loudness"], 3),
                    str(row["field_strained"]),
                    str(row["episode_memory"]),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["carry"], 6),
                    _fmt(row["field_carried_ratio"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Verdichtungs-Schritte",
            "",
            "| Gruppe | Schritt | Lautstaerke-Delta | Strain-Delta | Memory-Delta | Rekopplungs-Delta | Strain/Lautstaerke-Delta | Memory/Lautstaerke-Delta |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    deltas: list[tuple[str, dict]] = []
    for (asset, year), items in sorted(groups.items()):
        for index in range(1, len(items)):
            step = _delta(items[index - 1], items[index])
            group_name = f"{asset}_{year}"
            deltas.append((group_name, step))
            lines.append(
                "| "
                + " | ".join(
                    [
                        group_name,
                        f"{step['from']}->{step['to']}",
                        _fmt(step["loudness_delta"], 3),
                        str(step["strain_delta"]),
                        str(step["memory_delta"]),
                        _fmt(step["rek_delta"], 6),
                        _fmt(step["strain_per_loudness_delta"], 3),
                        _fmt(step["memory_per_loudness_delta"], 3),
                    ]
                )
                + " |"
            )

    lines.extend(["", "## Jahresprofile", ""])
    for (asset, year), items in sorted(groups.items()):
        first = items[0]
        last = items[-1]
        full = _delta(first, last)
        lines.extend(
            [
                f"### {asset} {year}",
                "",
                f"- Lautstaerke {first['timeframe']}->{last['timeframe']}: `{_fmt(full['loudness_delta'], 3)}`",
                f"- Strain {first['timeframe']}->{last['timeframe']}: `{full['strain_delta']}`",
                f"- Memory {first['timeframe']}->{last['timeframe']}: `{full['memory_delta']}`",
                f"- Rekopplung {first['timeframe']}->{last['timeframe']}: `{_fmt(full['rek_delta'], 6)}`",
                f"- Strain pro Lautstaerke-Delta: `{_fmt(full['strain_per_loudness_delta'], 3)}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Verdichtungs-Sensitivitaet beschreibt, wie stark das Innenfeld auf groessere Weltpakete reagiert.",
            "Eine Welt kann absolut laut sein, aber proportional gut getragen werden. Eine andere Welt kann bei aehnlicher Lautstaerke schneller in Strain und Memorylast kippen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Diagnose in die Forschungsuebersicht aufgenommen werden.",
            "Danach koennen weitere Assets geprueft werden, um zu sehen, ob BTC und SOL zwei Extreme oder nur zwei Punkte auf einer groesseren MCM-Weltkarte sind.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Verdichtungs-Sensitivitaetsdiagnose.")
    parser.add_argument(
        "--summary",
        nargs=4,
        action="append",
        metavar=("ASSET", "YEAR", "TIMEFRAME", "PATH"),
        required=True,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    rows = []
    for asset, year, timeframe, path_text in args.summary:
        rows.append(_row(asset, year, timeframe, _load_json(_resolve(path_text))))
    _write_markdown(rows, _resolve(str(args.out)))


if __name__ == "__main__":
    main()
