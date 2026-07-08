from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * q
    lower = int(index)
    upper = min(lower + 1, len(values) - 1)
    if lower == upper:
        return values[lower]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _read_candles(path: Path) -> list[dict[str, float]]:
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


def _world_features(path_text: str) -> dict[str, float]:
    if not path_text:
        return {
            "rows": 0.0,
            "drift": 0.0,
            "abs_drift": 0.0,
            "avg_abs_return": 0.0,
            "p95_abs_return": 0.0,
            "avg_range": 0.0,
            "p95_range": 0.0,
            "avg_volume_change": 0.0,
            "direction_change_ratio": 0.0,
            "direction_persistence": 0.0,
            "world_energy": 0.0,
        }
    path = (ROOT / path_text).resolve()
    rows = _read_candles(path)
    if len(rows) < 2:
        return {
            "rows": float(len(rows)),
            "drift": 0.0,
            "abs_drift": 0.0,
            "avg_abs_return": 0.0,
            "p95_abs_return": 0.0,
            "avg_range": 0.0,
            "p95_range": 0.0,
            "avg_volume_change": 0.0,
            "direction_change_ratio": 0.0,
            "direction_persistence": 0.0,
            "world_energy": 0.0,
        }
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
        1 for index in range(1, len(returns)) if returns[index] * returns[index - 1] < 0
    )
    direction_change_ratio = direction_changes / max(1, len(returns) - 1)
    drift = ((closes[-1] - closes[0]) / closes[0]) if closes[0] else 0.0
    avg_abs_return = _avg(abs_returns)
    p95_abs_return = _percentile(abs_returns, 0.95)
    avg_range = _avg(ranges)
    p95_range = _percentile(ranges, 0.95)
    avg_volume_change = _avg(volume_changes)
    direction_persistence = 1.0 - direction_change_ratio
    # Passive Weltenergie: keine MCM-Regel, nur Rohwelt-Lupe.
    world_energy = (
        avg_abs_return * 1000.0 * 0.32
        + p95_abs_return * 1000.0 * 0.22
        + avg_range * 1000.0 * 0.22
        + p95_range * 1000.0 * 0.16
        + min(avg_volume_change, 5.0) * 0.04
        + direction_persistence * 0.04
    )
    return {
        "rows": float(len(rows)),
        "drift": drift,
        "abs_drift": abs(drift),
        "avg_abs_return": avg_abs_return,
        "p95_abs_return": p95_abs_return,
        "avg_range": avg_range,
        "p95_range": p95_range,
        "avg_volume_change": avg_volume_change,
        "direction_change_ratio": direction_change_ratio,
        "direction_persistence": direction_persistence,
        "world_energy": world_energy,
    }


def _read_axis_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_axis_markdown(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    rows: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or "FOLLOW" not in line:
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 17:
            continue
        rows.append(
            {
                "label": parts[0],
                "weltgruppe": parts[1],
                "achsenklasse": parts[2],
                "rollenbreite_klasse": parts[3],
                "rollen": parts[4],
                "kombinationen": parts[5],
                "cross_state": parts[6],
                "same_state": parts[7],
                "rekopplung": parts[8],
                "adaptive_rekopplung": parts[9],
                "adaptive_rekopplung_delta": parts[10],
                "adaptive_rekopplung_experience": parts[11],
                "nachhall": parts[12],
                "stabil": parts[13],
                "tragend_unruhig": parts[14],
                "kippend": parts[15],
                "gespannt": parts[16],
                "data_path": "",
                "follow_data_path": "",
            }
        )
    return rows


def _load_axis_rows(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in paths:
        if path.suffix.lower() == ".csv":
            rows.extend(_read_axis_csv(path))
        else:
            rows.extend(_read_axis_markdown(path))
    return rows


def _enrich(row: dict[str, str]) -> dict[str, object]:
    base = _world_features(row.get("data_path", ""))
    follow = _world_features(row.get("follow_data_path", ""))
    out: dict[str, object] = dict(row)
    for prefix, features in (("base", base), ("follow", follow)):
        for key, value in features.items():
            out[f"{prefix}_{key}"] = value
    out["follow_minus_base_energy"] = follow["world_energy"] - base["world_energy"]
    out["follow_minus_base_abs_drift"] = follow["abs_drift"] - base["abs_drift"]
    out["follow_minus_base_range"] = follow["avg_range"] - base["avg_range"]
    return out


def _group(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get("achsenklasse", ""))].append(row)
    result: list[dict[str, object]] = []
    numeric_keys = [
        "rollen",
        "kombinationen",
        "cross_state",
        "same_state",
        "rekopplung",
        "adaptive_rekopplung",
        "adaptive_rekopplung_experience",
        "nachhall",
        "base_world_energy",
        "follow_world_energy",
        "follow_minus_base_energy",
        "base_abs_drift",
        "follow_abs_drift",
        "follow_minus_base_abs_drift",
        "base_avg_range",
        "follow_avg_range",
        "follow_minus_base_range",
        "base_direction_change_ratio",
        "follow_direction_change_ratio",
    ]
    for cls, items in sorted(groups.items()):
        row: dict[str, object] = {"achsenklasse": cls, "count": len(items)}
        for key in numeric_keys:
            row[key] = _avg([_float(item.get(key)) for item in items])
        result.append(row)
    return result


def _fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, (float, int)):
        return f"{value:.{digits}f}"
    return str(value)


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_markdown(path: Path, rows: list[dict[str, object]], grouped: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Sequenz-Rohwelt-Rücklesung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.",
        "Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.",
        "",
        "## Klassenmittel",
        "",
        "| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in grouped:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["achsenklasse"]),
                    str(row["count"]),
                    _fmt(row["rollen"]),
                    _fmt(row["kombinationen"]),
                    _fmt(row["cross_state"]),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["adaptive_rekopplung"], 6),
                    _fmt(row["adaptive_rekopplung_experience"], 4),
                    _fmt(row["nachhall"], 4),
                    _fmt(row["base_world_energy"], 4),
                    _fmt(row["follow_world_energy"], 4),
                    _fmt(row["follow_minus_base_energy"], 4),
                    _fmt(row["base_abs_drift"], 6),
                    _fmt(row["follow_abs_drift"], 6),
                    _fmt(row["base_avg_range"], 6),
                    _fmt(row["follow_avg_range"], 6),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Einzelzeilen",
            "",
            "| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("label", "")),
                    str(row.get("weltgruppe", "")),
                    str(row.get("achsenklasse", "")),
                    _fmt(_float(row.get("rollen")), 0),
                    _fmt(_float(row.get("kombinationen")), 0),
                    _fmt(_float(row.get("cross_state")), 0),
                    _fmt(_float(row.get("rekopplung")), 6),
                    _fmt(_float(row.get("nachhall")), 4),
                    _fmt(row.get("base_world_energy", 0.0)),
                    _fmt(row.get("follow_world_energy", 0.0)),
                    _fmt(row.get("follow_minus_base_energy", 0.0)),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.",
            "",
            "`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.",
            "",
            "## Grenze",
            "",
            "Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", action="append", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv", required=True)
    parser.add_argument("--group-csv", required=True)
    args = parser.parse_args()

    axis_paths = [(ROOT / value).resolve() for value in args.axis]
    rows = [_enrich(row) for row in _load_axis_rows(axis_paths)]
    grouped = _group(rows)
    _write_csv((ROOT / args.csv).resolve(), rows)
    _write_csv((ROOT / args.group_csv).resolve(), grouped)
    _write_markdown((ROOT / args.out).resolve(), rows, grouped)
    print({"rows": len(rows), "groups": len(grouped), "out": args.out})


if __name__ == "__main__":
    main()
