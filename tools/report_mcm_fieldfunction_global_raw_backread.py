from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1381_FELDFUNKTIONSKARTE_GLOBALE_PROBE.csv"
OUT_CSV = befunde_root(ROOT) / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.csv"
OUT_MD = befunde_root(ROOT) / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.md"

REPORTS = {
    "BTC_2024_5M": ROOT / "debug" / "adapted_field_btc_2024_5m_2k" / "dio_mini_lauf_2" / "mini_report.json",
    "SOL_2024_5M": ROOT / "debug" / "adapted_field_sol_2024_5m_2k" / "dio_mini_lauf_2" / "mini_report.json",
    "PAXG_2024_5M": ROOT / "debug" / "adapted_field_paxg_2024_5m_10k" / "dio_mini_lauf_2" / "mini_report.json",
    "XRP_2024_5M": ROOT / "debug" / "adapted_field_xrp_2024_5m_10k" / "dio_mini_lauf_2" / "mini_report.json",
    "DOGE_2024_5M": ROOT / "debug" / "adapted_field_doge_2024_5m_10k" / "dio_mini_lauf_2" / "mini_report.json",
}


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _data_path_for_world(world: str) -> Path | None:
    report = REPORTS.get(world)
    if not report or not report.exists():
        return None
    data = json.loads(report.read_text(encoding="utf-8")).get("data_path")
    if not data:
        return None
    path = Path(str(data))
    return path if path.is_absolute() else ROOT / path


def _world_features(candles: list[dict[str, str]]) -> dict[str, float | str]:
    if len(candles) < 2:
        return {
            "raw_form": "zu_kurz",
            "drift_pct": 0.0,
            "abs_drift_pct": 0.0,
            "avg_abs_return_pct": 0.0,
            "avg_range_pct": 0.0,
            "max_range_pct": 0.0,
            "volume_change_pct": 0.0,
            "direction_change_ratio": 0.0,
            "direction_persistence": 0.0,
        }
    closes = [_float(row.get("close")) for row in candles]
    highs = [_float(row.get("high")) for row in candles]
    lows = [_float(row.get("low")) for row in candles]
    volumes = [_float(row.get("volume")) for row in candles]
    returns = [
        ((closes[index] - closes[index - 1]) / closes[index - 1]) * 100.0
        for index in range(1, len(closes))
        if closes[index - 1]
    ]
    ranges = [
        ((highs[index] - lows[index]) / closes[index]) * 100.0
        for index in range(len(closes))
        if closes[index]
    ]
    direction_changes = sum(
        1
        for index in range(1, len(returns))
        if returns[index] * returns[index - 1] < 0
    )
    direction_change_ratio = direction_changes / max(1, len(returns) - 1)
    direction_persistence = max(0.0, 1.0 - direction_change_ratio)
    drift_pct = ((closes[-1] - closes[0]) / closes[0]) * 100.0 if closes[0] else 0.0
    volume_change_pct = ((volumes[-1] - volumes[0]) / volumes[0]) * 100.0 if volumes[0] else 0.0
    avg_abs_return = sum(abs(value) for value in returns) / max(1, len(returns))
    avg_range = sum(ranges) / max(1, len(ranges))
    max_range = max(ranges) if ranges else 0.0

    if abs(drift_pct) >= 1.4 and direction_persistence >= 0.62:
        raw_form = "gerichtete_weltbewegung"
    elif avg_range >= 0.22 or avg_abs_return >= 0.11:
        raw_form = "laute_oder_druckvolle_rohwelt"
    elif direction_change_ratio >= 0.52:
        raw_form = "wechselhafte_rohwelt"
    elif avg_range <= 0.075 and avg_abs_return <= 0.035:
        raw_form = "ruhige_enge_rohwelt"
    else:
        raw_form = "gemischte_rohwelt"

    return {
        "raw_form": raw_form,
        "drift_pct": drift_pct,
        "abs_drift_pct": abs(drift_pct),
        "avg_abs_return_pct": avg_abs_return,
        "avg_range_pct": avg_range,
        "max_range_pct": max_range,
        "volume_change_pct": volume_change_pct,
        "direction_change_ratio": direction_change_ratio,
        "direction_persistence": direction_persistence,
    }


def _slice_candles(candles: list[dict[str, str]], start_tick: int, end_tick: int) -> list[dict[str, str]]:
    start = max(0, start_tick - 1)
    end = min(len(candles), end_tick)
    return candles[start:end]


def build_report() -> None:
    probe_rows = _read_csv(INPUT)
    data_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, object]] = []
    for row in probe_rows:
        role = row.get("passive_role_near", "")
        if role == "keine_naehe":
            continue
        world = row.get("world", "")
        if world not in data_cache:
            path = _data_path_for_world(world)
            data_cache[world] = _read_csv(path) if path and path.exists() else []
        candles = data_cache[world]
        start_tick = int(_float(row.get("start_tick")))
        end_tick = int(_float(row.get("end_tick")))
        features = _world_features(_slice_candles(candles, start_tick, end_tick))
        out = dict(row)
        out.update({key: round(value, 6) if isinstance(value, float) else value for key, value in features.items()})
        out_rows.append(out)

    if not out_rows:
        raise RuntimeError("no raw backread rows")
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    role_counts = Counter(str(row["passive_role_near"]) for row in out_rows)
    role_forms: dict[str, Counter[str]] = defaultdict(Counter)
    role_worlds: dict[str, Counter[str]] = defaultdict(Counter)
    for row in out_rows:
        role = str(row["passive_role_near"])
        role_forms[role][str(row["raw_form"])] += 1
        role_worlds[role][str(row["world"])] += 1

    lines = [
        "# 1382 - Feldfunktionskarte: Rohwelt-Ruecklesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die in `1381` markierten Feldfunktionsnaehen gegen konkrete Candle-Fenster zurueck.",
        "",
        "Geprueft wird:",
        "",
        "```text",
        "Koppeln Brueckennaehe, Zentrumsnaehe, Randdrucknaehe und Mischrollen an reale Aussenweltformen,",
        "oder entstehen sie nur aus internen Metriknaehen?",
        "```",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Datengrundlage",
        "",
        f"- gelesene Naehefenster: `{len(out_rows)}`",
        "",
        "## Rollennaehe und Rohweltformen",
        "",
    ]
    for role, count in role_counts.most_common():
        forms = " | ".join(f"{key}:{value}" for key, value in role_forms[role].most_common())
        worlds = " | ".join(f"{key}:{value}" for key, value in role_worlds[role].most_common())
        lines.extend(
            [
                f"### `{role}`",
                "",
                f"- Fenster: `{count}`",
                f"- Rohweltformen: {forms}",
                f"- Welten: {worlds}",
                "",
            ]
        )

    lines.extend(
        [
            "## Lesung",
            "",
            "Wenn eine Rollennaehe ueberwiegend mit konkreten Rohweltformen koppelt, spricht das fuer reale Aussenweltbindung.",
            "Wenn sie breit ueber alle Rohweltformen verteilt ist, muss sie vorsichtig als interne Feldnaehe gelesen werden.",
            "",
            "## Grenze",
            "",
            "Die Rohweltform ist eine einfache Ruecklesung aus Candle-Fenstern. Sie ist keine endgueltige visuelle Formanalyse.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste Kopplung aus dieser Ruecklesung isoliert werden. Dann kann geprueft werden, ob sie in weiteren Welten stabil bleibt oder nur in einem Asset/Regime auftritt.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
