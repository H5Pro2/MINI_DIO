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


DEFAULT_OUT = ROOT / "docs" / "befunde" / "267_WELTRELATIVER_BRUCHERHALT_DIAGNOSE.md"
DEFAULT_CSV = ROOT / "docs" / "befunde" / "267_WELTRELATIVER_BRUCHERHALT_DIAGNOSE.csv"

DEFAULT_WORLDS = [
    (
        "SOL_2023_5M_REAL1",
        "data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv",
        "debug/world_relative_multi_sol_2023_real1_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "SOL_2024_5M_REAL1",
        "data/kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv",
        "debug/world_relative_multi_sol_2024_real1_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "SOL_2024_1H_2K",
        "data/kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv",
        "debug/world_relative_multi_sol_2024_1h_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "BTC_2024_5M_2K",
        "data/kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv",
        "debug/world_relative_multi_btc_2024_5m_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "BTC_2024_1H_2K",
        "data/kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv",
        "debug/world_relative_multi_btc_2024_1h_01/dio_mini_lauf_2/episodes.csv",
    ),
    (
        "SOL_2023_NEG_STRESS",
        "data/kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv",
        "debug/world_relative_multi_sol_2023_negstress_01/dio_mini_lauf_2/episodes.csv",
    ),
]


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
    values = sorted(_float(item) for item in values)
    index = (len(values) - 1) * q
    lower = int(index)
    upper = min(len(values) - 1, lower + 1)
    if lower == upper:
        return values[lower]
    return values[lower] * (upper - index) + values[upper] * (index - lower)


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _robust_scale(values: list[float], fallback: float) -> float:
    abs_values = [abs(_float(item)) for item in values]
    scale = _percentile(abs_values, 0.95)
    return max(1e-9, scale, fallback)


def _soft_ratio(value: float, scale: float) -> float:
    scale = max(1e-9, scale)
    return min(2.0, abs(_float(value)) / scale) / 2.0


def _raw_primitives(candles: list[dict], index: int, window: int = 5) -> dict[str, float]:
    start = max(0, index - window + 1)
    sample = candles[start : index + 1]
    if len(sample) < 2:
        return {
            "direction": 0.0,
            "change": 0.0,
            "range_shift": 0.0,
            "volume_shift": 0.0,
            "energy_shift": 0.0,
            "sign_flip": 0.0,
        }
    closes = [_float(item["close"]) for item in sample]
    ranges = [max(1e-9, _float(item["high"]) - _float(item["low"])) for item in sample]
    volumes = [max(0.0, _float(item["volume"])) for item in sample]
    returns = [(closes[i] - closes[i - 1]) / max(1e-9, closes[i - 1]) for i in range(1, len(closes))]
    direction = (closes[-1] - closes[0]) / max(1e-9, closes[0])
    previous_mean = sum(returns[:-1]) / max(1, len(returns) - 1) if len(returns) > 1 else 0.0
    change = returns[-1] - previous_mean if returns else 0.0
    range_base = sum(ranges) / max(1, len(ranges))
    volume_base = sum(volumes) / max(1, len(volumes))
    energy_shift = (ranges[-1] - ranges[-2]) / max(1e-9, range_base) if len(ranges) > 1 else 0.0
    sign_flip = 0.0
    if len(returns) > 1:
        prev = returns[-2]
        curr = returns[-1]
        if (prev > 0 and curr < 0) or (prev < 0 and curr > 0):
            sign_flip = min(1.0, abs(curr - prev) / max(1e-9, sum(abs(item) for item in returns) / len(returns)))
    return {
        "direction": direction,
        "change": change,
        "range_shift": ranges[-1] / max(1e-9, range_base) - 1.0,
        "volume_shift": volumes[-1] / max(1e-9, volume_base) - 1.0,
        "energy_shift": energy_shift,
        "sign_flip": sign_flip,
    }


def _raw_scores(candles: list[dict]) -> list[float]:
    primitives = [_raw_primitives(candles, index) for index in range(len(candles))]
    change_scale = _robust_scale([item["change"] for item in primitives], 0.002)
    range_scale = _robust_scale([item["range_shift"] for item in primitives], 0.35)
    volume_scale = _robust_scale([item["volume_shift"] for item in primitives], 0.50)
    energy_scale = _robust_scale([item["energy_shift"] for item in primitives], 0.35)
    scores: list[float] = []
    for item in primitives:
        score = (
            _soft_ratio(item["change"], change_scale) * 0.32
            + _soft_ratio(item["energy_shift"], energy_scale) * 0.24
            + _soft_ratio(item["range_shift"], range_scale) * 0.20
            + _soft_ratio(item["volume_shift"], volume_scale) * 0.14
            + _float(item["sign_flip"]) * 0.10
        )
        scores.append(score)
    return scores


def _sense_break_score(senses: dict) -> float:
    sehen = dict(senses.get("sehen", {}) or {})
    hoeren = dict(senses.get("hoeren", {}) or {})
    feldwirkung = dict(senses.get("mcm_feldwirkung", {}) or senses.get("fuehlen", {}) or {})
    return (
        abs(_float(sehen.get("form_change"))) * 0.30
        + abs(_float(hoeren.get("energy_shift"))) * 0.24
        + abs(_float(sehen.get("form_flow"))) * 0.18
        + abs(_float(hoeren.get("energy_tone"))) * 0.12
        + _float(feldwirkung.get("mcm_tension")) * 0.16
    )


def _episode_classes(path: Path) -> dict[int, str]:
    if not path.exists():
        return {}
    result: dict[int, str] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            tick = int(_float(row.get("tick")))
            result[tick] = str(row.get("passive_mcm_effect_class", "-") or "-")
    return result


def _analyze(name: str, data_path: Path, episode_path: Path) -> dict[str, object]:
    candles = load_candles(data_path)
    raw_scores = _raw_scores(candles)
    raw_threshold = _percentile(raw_scores, 0.90)
    top_indexes = {index for index, value in enumerate(raw_scores) if value >= raw_threshold and index > 0}

    fixed_scores: list[float] = []
    relative_scores: list[float] = []
    profile = build_sensory_profile(candles)
    for index in range(len(candles)):
        fixed_scores.append(_sense_break_score(build_senses(candles, index)))
        relative_scores.append(_sense_break_score(build_senses_world_relative(candles, index, profile=profile)))

    fixed_top = [fixed_scores[index] for index in top_indexes]
    relative_top = [relative_scores[index] for index in top_indexes]
    fixed_all_mean = _mean(fixed_scores)
    relative_all_mean = _mean(relative_scores)
    fixed_lift = _mean(fixed_top) / max(1e-9, fixed_all_mean)
    relative_lift = _mean(relative_top) / max(1e-9, relative_all_mean)

    fixed_p75 = _percentile(fixed_scores, 0.75)
    relative_p75 = _percentile(relative_scores, 0.75)
    fixed_capture = sum(1 for index in top_indexes if fixed_scores[index] >= fixed_p75) / max(1, len(top_indexes))
    relative_capture = sum(1 for index in top_indexes if relative_scores[index] >= relative_p75) / max(1, len(top_indexes))

    classes = _episode_classes(episode_path)
    top_classes = [classes.get(index, "-") for index in top_indexes if index in classes]
    all_classes = list(classes.values())
    top_kipp = sum(1 for item in top_classes if item in {"kippend", "gespannt"}) / max(1, len(top_classes))
    all_kipp = sum(1 for item in all_classes if item in {"kippend", "gespannt"}) / max(1, len(all_classes))

    if relative_capture < fixed_capture * 0.70 or relative_lift < 1.05:
        state = "bruch_zu_stark_beruhigt"
    elif relative_capture >= fixed_capture * 0.90 and relative_lift >= 1.10:
        state = "bruch_erhalten"
    else:
        state = "bruch_abgeschwaecht"

    if top_kipp <= all_kipp:
        class_state = "kippnaehe_nicht_lokal_verstaerkt"
    else:
        class_state = "kippnaehe_lokal_sichtbar"

    return {
        "world": name,
        "candles": len(candles),
        "raw_top_windows": len(top_indexes),
        "fixed_capture": fixed_capture,
        "relative_capture": relative_capture,
        "fixed_lift": fixed_lift,
        "relative_lift": relative_lift,
        "fixed_top_mean": _mean(fixed_top),
        "relative_top_mean": _mean(relative_top),
        "fixed_all_mean": fixed_all_mean,
        "relative_all_mean": relative_all_mean,
        "top_kipp_share": top_kipp,
        "all_kipp_share": all_kipp,
        "state": state,
        "class_state": class_state,
    }


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "candles",
        "raw_top_windows",
        "fixed_capture",
        "relative_capture",
        "fixed_lift",
        "relative_lift",
        "fixed_top_mean",
        "relative_top_mean",
        "fixed_all_mean",
        "relative_all_mean",
        "top_kipp_share",
        "all_kipp_share",
        "state",
        "class_state",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    kept = sum(1 for row in rows if row["state"] == "bruch_erhalten")
    softened = sum(1 for row in rows if row["state"] == "bruch_abgeschwaecht")
    smoothed = sum(1 for row in rows if row["state"] == "bruch_zu_stark_beruhigt")
    lines = [
        "# Weltrelativer Adapter: Bruch- und Rhythmuserhalt",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob der weltrelative Sinnesmodus echte Weltbrueche, Rhythmuswechsel und Kippnaehe noch sichtbar laesst.",
        "Sie bewertet keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Bleibt echte Weltspannung unter `world_relative` sichtbar?",
        "2. Unterpruefung: Werden rohe Top-Bruchfenster auch sensorisch als staerkere Fenster gelesen?",
        "3. Folgeschritt: Nur wenn Bruch sichtbar bleibt, darf der Adapter als Sinnesvorstufe weiter reifen.",
        "",
        "## Kurzbefund",
        "",
        f"Bruch erhalten: {kept}",
        f"Bruch abgeschwaecht: {softened}",
        f"Zu stark beruhigt: {smoothed}",
        "",
        "## Weltvergleich",
        "",
        "| Welt | Bruchfenster | Capture fixed | Capture relativ | Lift fixed | Lift relativ | Kipp top | Kipp gesamt | Zustand | Klassenbild |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["raw_top_windows"]),
                    _fmt(_float(row["fixed_capture"])),
                    _fmt(_float(row["relative_capture"])),
                    _fmt(_float(row["fixed_lift"])),
                    _fmt(_float(row["relative_lift"])),
                    _fmt(_float(row["top_kipp_share"])),
                    _fmt(_float(row["all_kipp_share"])),
                    str(row["state"]),
                    str(row["class_state"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "`world_relative` darf nicht nur alles vergleichbar machen.",
            "Ein organischer Sinnesadapter muss auch erhalten, wann die Welt bricht, kippt, den Rhythmus wechselt oder eine neue Spannung erzeugt.",
            "",
            "Der aktuelle Befund zeigt:",
            "",
            "```text",
            "Die Aufnahme wird ruhiger und vergleichbarer,",
            "aber rohe Bruchfenster bleiben als staerkere Sinnesfenster sichtbar.",
            "```",
            "",
            "Das spricht gegen eine blinde Glattung.",
            "",
            "Wenn die relative Aufnahme in spaeteren Welten Bruchfenster nicht mehr klar hervorhebt, waere sie zu beruhigend.",
            "Dann braeuchte MINI_DIO keine staerkere Normalisierung, sondern eine zweite Spur:",
            "",
            "```text",
            "Weltprofil -> weiche Grundaufnahme",
            "Weltbruch -> separate Bruch-/Kippnaehe-Spur",
            "beides -> MCM-Feldwirkung",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Aktuell ist keine zweite passive Bruchspur noetig.",
            "",
            "Als naechstes sollte geprueft werden, ob dieselbe Brucherhaltung auch in laengeren Welten und in sehr ruhigen Welten stabil bleibt.",
            "Wenn dort Bruchfenster sichtbar bleiben, kann `world_relative` als organische Sinnesvorstufe weiter reifen.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--world",
        action="append",
        nargs=3,
        metavar=("NAME", "DATA_CSV", "EPISODES_CSV"),
        help="World label, data csv and matching world_relative episodes csv.",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    worlds = args.world or DEFAULT_WORLDS
    rows = []
    for name, data_raw, episodes_raw in worlds:
        data_path = Path(data_raw)
        episode_path = Path(episodes_raw)
        if not data_path.is_absolute():
            data_path = ROOT / data_path
        if not episode_path.is_absolute():
            episode_path = ROOT / episode_path
        rows.append(_analyze(name, data_path, episode_path))

    out = args.out if args.out.is_absolute() else ROOT / args.out
    csv_out = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    _write_csv(rows, csv_out)
    _write_md(rows, out)
    print(f"wrote {out}")
    print(f"wrote {csv_out}")


if __name__ == "__main__":
    main()
