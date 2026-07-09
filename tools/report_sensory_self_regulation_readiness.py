from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.mini_world import build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_WORLDS = {
    "SOL_2025_5M": "data/kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv",
    "SOL_2025_1H": "data/kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv",
    "BTC_2025_5M": "data/kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv",
    "BTC_2025_1H": "data/kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv",
    "KAS_2024_5M": "data/kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
    "KAS_2024_1H": "data/kontrolliert_kas_2024_1h_test1_2000_KASUSDT.csv",
    "PAXG_2025_5M": "data/kontrolliert_paxg_2025_5m_10k_PAXGUSDT.csv",
    "PAXG_2025_1H": "data/kontrolliert_paxg_2025_1h_10k_PAXGUSDT.csv",
}


def _float(state: dict, key: str) -> float:
    try:
        return float(state.get(key, 0.0) or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _avg(values: list[float]) -> float:
    return mean(values) if values else 0.0


def _asset_from_label(label: str) -> str:
    return label.split("_", 1)[0]


def _timeframe_from_label(label: str) -> str:
    parts = label.split("_")
    return parts[-1] if parts else "-"


def _read_world(label: str, path: Path, limit: int, window: int) -> dict[str, object]:
    candles = load_candles(path)
    if limit > 0:
        candles = candles[:limit]
    profile = build_sensory_profile(candles, window=window)

    auditory_loudness: list[float] = []
    auditory_softening: list[float] = []
    auditory_listen: list[float] = []
    visual_sharpness: list[float] = []
    visual_blur: list[float] = []
    focus_strength: list[float] = []
    distance_need: list[float] = []
    felt_pressure: list[float] = []
    felt_relaxation: list[float] = []
    raw_intake: list[float] = []
    adapted_intake: list[float] = []
    adaptation: list[float] = []

    for index in range(len(candles)):
        senses = build_senses_world_relative(candles, index, window=window, profile=profile)
        state = dict(senses.get("perception_regulation_state", {}) or {})
        auditory_loudness.append(_float(state, "auditory_loudness"))
        auditory_softening.append(_float(state, "auditory_softening"))
        auditory_listen.append(_float(state, "auditory_listen_tendency"))
        visual_sharpness.append(_float(state, "visual_sharpness"))
        visual_blur.append(_float(state, "visual_blur"))
        focus_strength.append(_float(state, "focus_strength"))
        distance_need.append(_float(state, "distance_need"))
        felt_pressure.append(_float(state, "felt_pressure"))
        felt_relaxation.append(_float(state, "felt_relaxation"))
        raw_intake.append(_float(state, "raw_field_intake_pressure"))
        adapted_intake.append(_float(state, "adapted_field_intake_pressure"))
        adaptation.append(_float(state, "adaptation_potential"))

    avg_raw = _avg(raw_intake)
    avg_adapted = _avg(adapted_intake)
    avg_adaptation = _avg(adaptation)
    reduction = max(0.0, avg_raw - avg_adapted)
    reduction_ratio = reduction / avg_raw if avg_raw > 1e-9 else 0.0

    return {
        "world": label,
        "asset": _asset_from_label(label),
        "timeframe": _timeframe_from_label(label),
        "rows": len(candles),
        "avg_auditory_loudness": round(_avg(auditory_loudness), 6),
        "avg_auditory_softening": round(_avg(auditory_softening), 6),
        "avg_auditory_listen": round(_avg(auditory_listen), 6),
        "avg_visual_sharpness": round(_avg(visual_sharpness), 6),
        "avg_visual_blur": round(_avg(visual_blur), 6),
        "avg_focus_strength": round(_avg(focus_strength), 6),
        "avg_distance_need": round(_avg(distance_need), 6),
        "avg_felt_pressure": round(_avg(felt_pressure), 6),
        "avg_felt_relaxation": round(_avg(felt_relaxation), 6),
        "avg_raw_field_intake": round(avg_raw, 6),
        "avg_adapted_field_intake": round(avg_adapted, 6),
        "avg_adaptation_potential": round(avg_adaptation, 6),
        "avg_intake_reduction": round(reduction, 6),
        "avg_intake_reduction_ratio": round(reduction_ratio, 6),
    }


def _rank_label(value: float, low: float, high: float, low_label: str, mid_label: str, high_label: str) -> str:
    if value <= low:
        return low_label
    if value >= high:
        return high_label
    return mid_label


def _add_relative_labels(rows: list[dict[str, object]]) -> None:
    loud = sorted(float(row["avg_auditory_loudness"]) for row in rows)
    sharp = sorted(float(row["avg_visual_sharpness"]) for row in rows)
    pressure = sorted(float(row["avg_felt_pressure"]) for row in rows)
    adaptation = sorted(float(row["avg_adaptation_potential"]) for row in rows)
    n = max(1, len(rows) - 1)
    loud_low, loud_high = loud[int(n * 0.25)], loud[int(n * 0.75)]
    sharp_low, sharp_high = sharp[int(n * 0.25)], sharp[int(n * 0.75)]
    pressure_low, pressure_high = pressure[int(n * 0.25)], pressure[int(n * 0.75)]
    adaptation_low, adaptation_high = adaptation[int(n * 0.25)], adaptation[int(n * 0.75)]

    for row in rows:
        row["hearing_state"] = _rank_label(
            float(row["avg_auditory_loudness"]),
            loud_low,
            loud_high,
            "leise_feinhoeren",
            "mittlere_lautheit",
            "laut_daempfung_noetig",
        )
        row["visual_state"] = _rank_label(
            float(row["avg_visual_sharpness"]),
            sharp_low,
            sharp_high,
            "unscharf_genauer_sehen",
            "mittlere_sicht",
            "scharf_formtragend",
        )
        row["felt_state"] = _rank_label(
            float(row["avg_felt_pressure"]),
            pressure_low,
            pressure_high,
            "duenner_feldkontakt",
            "mittlerer_feldkontakt",
            "starker_feldkontakt",
        )
        row["adaptation_state"] = _rank_label(
            float(row["avg_adaptation_potential"]),
            adaptation_low,
            adaptation_high,
            "geringe_anpassung",
            "mittlere_anpassung",
            "hohe_anpassung",
        )


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    strongest_hearing = max(rows, key=lambda row: float(row["avg_auditory_loudness"]))
    weakest_hearing = min(rows, key=lambda row: float(row["avg_auditory_loudness"]))
    strongest_visual = max(rows, key=lambda row: float(row["avg_visual_sharpness"]))
    strongest_felt = max(rows, key=lambda row: float(row["avg_felt_pressure"]))
    strongest_adaptation = max(rows, key=lambda row: float(row["avg_adaptation_potential"]))

    lines = [
        "# Sinnesaufnahme Selbstregulation Bestand",
        "",
        "Passive Bestandspruefung der drei Sinnesachsen vor dem MCM-Feld.",
        "",
        "Geprueft wird nicht, ob Mini-DIO handelt, sondern ob die Rezeptorschicht bereits verschiedenartige Welten unterschiedlich aufnimmt:",
        "",
        "- Hoeren: Lautheit, Daempfung, Hinhorchen.",
        "- Sehen: Schaerfe, Unschaerfe, Fokus.",
        "- Fuehlen: Feldkontakt, Feldaufnahme, Druck/Entlastung.",
        "",
        "## Weltvergleich",
        "",
        "| Welt | Zeilen | Hoeren | Sehen | Fuehlen | Anpassung | Lautheit | Schaerfe | Druck | Rohfeld | Adaptfeld | Reduktion |",
        "|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {world} | {rows} | {hearing_state} | {visual_state} | {felt_state} | {adaptation_state} | {avg_auditory_loudness:.4f} | {avg_visual_sharpness:.4f} | {avg_felt_pressure:.4f} | {avg_raw_field_intake:.4f} | {avg_adapted_field_intake:.4f} | {avg_intake_reduction:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste auditive Lautheit: `{strongest_hearing['world']}` mit `{float(strongest_hearing['avg_auditory_loudness']):.4f}`.",
            f"- Schwaechste auditive Lautheit: `{weakest_hearing['world']}` mit `{float(weakest_hearing['avg_auditory_loudness']):.4f}`.",
            f"- Staerkste visuelle Schaerfe: `{strongest_visual['world']}` mit `{float(strongest_visual['avg_visual_sharpness']):.4f}`.",
            f"- Staerkster Feldkontakt: `{strongest_felt['world']}` mit `{float(strongest_felt['avg_felt_pressure']):.4f}`.",
            f"- Staerkste passive Anpassung: `{strongest_adaptation['world']}` mit `{float(strongest_adaptation['avg_adaptation_potential']):.4f}`.",
            "",
            "## Bewertung",
            "",
            "Mini-DIO besitzt bereits eine rezeptorische Vorregulation: Rohfeldaufnahme wird nicht eins zu eins in das MCM-Feld gegeben, sondern ueber Anpassung reduziert.",
            "",
            "Das ist noch keine gelernte Selbststeuerung. Es ist eine passive organismische Faehigkeit: Welten kommen unterschiedlich laut, scharf und druckvoll an, und die Rezeptorschicht bildet daraus unterschiedliche Aufnahmequalitaeten.",
            "",
            "Fachlich wichtig: Sehen, Hoeren und Fuehlen bleiben getrennte Achsen. Fuehlen ist hier MCM-Feldwirkung ueber Rezeptorkontakt; direkte Beruehrung ist fuer Chartwelten noch nicht aktiv.",
            "",
            "## Schluss",
            "",
            "Die regulatorische Seite der Sinneswahrnehmung ist begonnen, aber noch nicht voll selbstlernend. Aktuell kann Mini-DIO passiv daempfen, unterscheiden und Aufnahmequalitaet bilden. Der naechste Schritt waere, diese Aufnahmequalitaet episodisch zu speichern: welche Sinneshaltung war fuer welche Welt tragend, ueberreizend oder zu duenn?",
            "",
            "Wie es weitergeht: Als naechstes sollte die Sinnesaufnahme gegen die Topologie gelesen werden: Welche Hoer-/Seh-/Fuehl-Konstellation erzeugt Zentrum, Bruecke, Rand oder Drift?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_world(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("world must be LABEL=PATH")
    label, path = value.split("=", 1)
    return label, path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", type=_parse_world)
    parser.add_argument("--limit", type=int, default=2000)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1272_SINNESAUFNAHME_SELBSTREGULATION_BESTAND.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1272_SINNESAUFNAHME_SELBSTREGULATION_BESTAND.csv")
    args = parser.parse_args()

    worlds = dict(args.world or DEFAULT_WORLDS.items())
    rows = [_read_world(label, Path(path), limit=args.limit, window=args.window) for label, path in worlds.items()]
    _add_relative_labels(rows)
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
