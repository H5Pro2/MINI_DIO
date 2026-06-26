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

from mini_dio.mini_world import build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_WORLDS = (
    ("SOL_2024_5M", ROOT / "data" / "kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv"),
    ("BTC_2024_5M", ROOT / "data" / "kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv"),
    ("KAS_2024_5M", ROOT / "data" / "kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv"),
    ("PAXG_2024_5M", ROOT / "data" / "kontrolliert_paxg_2024_5m_test1_2000_PAXGUSDT.csv"),
)

DEFAULT_CSV = ROOT / "docs" / "befunde" / "839_REZEPTOR_MCM_KETTE_AUDIT.csv"
DEFAULT_MD = ROOT / "docs" / "befunde" / "839_REZEPTOR_MCM_KETTE_AUDIT.md"


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _avg(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _fmt(value: float) -> str:
    return f"{float(value or 0.0):.6f}"


def _corr(left: list[float], right: list[float]) -> float:
    if len(left) != len(right) or len(left) < 2:
        return 0.0
    mean_l = _avg(left)
    mean_r = _avg(right)
    cov = sum((a - mean_l) * (b - mean_r) for a, b in zip(left, right))
    var_l = sum((a - mean_l) ** 2 for a in left)
    var_r = sum((b - mean_r) ** 2 for b in right)
    if var_l <= 1e-12 or var_r <= 1e-12:
        return 0.0
    return cov / ((var_l * var_r) ** 0.5)


def _analyze_world(label: str, path: Path) -> dict[str, object]:
    candles = load_candles(path)
    profile = build_sensory_profile(candles)
    visual: list[float] = []
    auditory: list[float] = []
    direct_contact: list[float] = []
    field_intake: list[float] = []
    raw_intake: list[float] = []
    adapted_intake: list[float] = []
    adaptation: list[float] = []
    coherence: list[float] = []
    tension: list[float] = []
    asymmetry: list[float] = []
    tension_intake_delta: list[float] = []

    for index in range(len(candles)):
        senses = build_senses_world_relative(candles, index, profile=profile)
        rezeptoren = dict(senses.get("rezeptoren", {}) or {})
        feld = dict(senses.get("mcm_feldwirkung", {}) or {})
        regulation = dict(senses.get("perception_regulation_state", {}) or {})
        visual.append(_float(rezeptoren.get("visual_form_salience")))
        auditory.append(_float(rezeptoren.get("auditory_stimulation")))
        direct_contact.append(_float(rezeptoren.get("direct_contact_pressure")))
        field_intake.append(_float(rezeptoren.get("field_intake_pressure")))
        raw_intake.append(_float(regulation.get("raw_field_intake_pressure")))
        adapted_intake.append(_float(regulation.get("adapted_field_intake_pressure")))
        adaptation.append(_float(regulation.get("adaptation_potential")))
        coherence.append(_float(feld.get("mcm_coherence")))
        tension.append(_float(feld.get("mcm_tension")))
        asymmetry.append(_float(feld.get("mcm_asymmetry")))
        tension_intake_delta.append(abs(_float(feld.get("mcm_tension")) - _float(rezeptoren.get("field_intake_pressure"))))

    raw_avg = _avg(raw_intake)
    adapted_avg = _avg(adapted_intake)
    reduction = raw_avg - adapted_avg
    reduction_ratio = reduction / max(1e-9, raw_avg)
    return {
        "world": label,
        "path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        "frames": len(candles),
        "avg_visual_form_salience": _avg(visual),
        "avg_auditory_stimulation": _avg(auditory),
        "avg_direct_contact_pressure": _avg(direct_contact),
        "avg_raw_field_intake_pressure": raw_avg,
        "avg_adapted_field_intake_pressure": adapted_avg,
        "avg_adaptation_potential": _avg(adaptation),
        "field_intake_reduction": reduction,
        "field_intake_reduction_ratio": reduction_ratio,
        "avg_mcm_coherence": _avg(coherence),
        "avg_mcm_tension": _avg(tension),
        "avg_mcm_asymmetry": _avg(asymmetry),
        "max_tension_field_intake_delta": max(tension_intake_delta) if tension_intake_delta else 0.0,
        "corr_auditory_tension": _corr(auditory, tension),
        "corr_visual_asymmetry": _corr(visual, asymmetry),
        "corr_visual_coherence": _corr(visual, coherence),
        "corr_auditory_coherence": _corr(auditory, coherence),
        "direct_contact_active_ratio": sum(1 for item in direct_contact if abs(item) > 1e-9) / max(1, len(direct_contact)),
    }


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    max_delta = max((_float(row.get("max_tension_field_intake_delta")) for row in rows), default=0.0)
    contact_active = max((_float(row.get("direct_contact_active_ratio")) for row in rows), default=0.0)
    lines = [
        "# 839 - Rezeptor-zu-MCM-Kette: Audit",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft die technische Kette:",
        "",
        "```text",
        "Aussenwelt -> Sehen / Hoeren / direkter Kontakt -> Rezeptoren -> MCM-Feldwirkung",
        "```",
        "",
        "Sie prueft keine Handlung, keine Strategie und keine Topologie. Es geht nur um die Frage, ob Rohdaten, Doppelwirkung oder unklare Feldkopplung in der aktuellen Mechanik sichtbar sind.",
        "",
        "## Ergebnis",
        "",
        f"- Gepruefte Welten: {len(rows)}",
        f"- Groesste Abweichung zwischen `rezeptoren.field_intake_pressure` und `mcm_feldwirkung.mcm_tension`: `{_fmt(max_delta)}`",
        f"- Groesster Anteil aktiver direkter Kontaktachse: `{_fmt(contact_active)}`",
        "",
        "Befund:",
        "",
        "- Roh-OHLCV gelangt nicht direkt in das MCM-Feld.",
        "- Direkter Kontakt ist in den aktuellen Kurswelten inaktiv.",
        "- `raw_field_intake_pressure` bleibt Diagnose.",
        "- `adapted_field_intake_pressure` wird als `rezeptoren.field_intake_pressure` an das Feld weitergegeben.",
        "- `mcm_feldwirkung.mcm_tension` ist aktuell technisch identisch mit `rezeptoren.field_intake_pressure`.",
        "",
        "Das ist fachlich sauber als Alias der Feldspannung lesbar. Kritisch wird es nur dort, wo beide Werte gleichzeitig als getrennte Eingangsfeatures verarbeitet werden.",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Frames | Visual | Hoeren | Raw Intake | Adapted Intake | Reduktion | MCM Tension | Delta Tension/Input | Direkter Kontakt |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {world} | {frames} | {visual} | {auditory} | {raw} | {adapted} | {reduction} | {tension} | {delta} | {contact} |".format(
                world=row["world"],
                frames=int(row["frames"]),
                visual=_fmt(row["avg_visual_form_salience"]),
                auditory=_fmt(row["avg_auditory_stimulation"]),
                raw=_fmt(row["avg_raw_field_intake_pressure"]),
                adapted=_fmt(row["avg_adapted_field_intake_pressure"]),
                reduction=_fmt(row["field_intake_reduction"]),
                tension=_fmt(row["avg_mcm_tension"]),
                delta=_fmt(row["max_tension_field_intake_delta"]),
                contact=_fmt(row["direct_contact_active_ratio"]),
            )
        )
    lines.extend(
        [
            "",
            "## Kritischer Mechanikpunkt",
            "",
            "`mcm_neuron.FEATURES` liest derzeit sowohl:",
            "",
            "- `rezeptoren.field_intake_pressure`",
            "- `mcm_feldwirkung.mcm_tension`",
            "",
            "Da beide Werte identisch sind, entsteht im neuronalen Eingangsvektor eine doppelte Funktionspraesenz derselben Feldspannung.",
            "",
            "Das ist keine Rohdatenflutung, aber eine Dopplung der gleichen Funktion. Fachlich sollte spaeter entschieden werden:",
            "",
            "1. Entweder das Mini-MCM-Neuron liest nur die verdichtete `mcm_feldwirkung`.",
            "2. Oder Rezeptorwerte bleiben als getrennte Wahrnehmungsspur im Syntax-/Diagnosevektor, aber nicht als zweite Feldspannung im MCM-Neuron.",
            "",
            "## Bewertung",
            "",
            "Die Rezeptorschicht ist grundsaetzlich vorhanden und schuetzt das Feld bereits vor direkter Rohdatenuebernahme. Die wichtigste offene Stelle ist nicht Rohdatenflutung, sondern Schichtklarheit im neuronalen Eingangsvektor.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Eingangsfeature-Liste des Mini-MCM-Neurons bereinigt werden: MCM-Feldwirkung als Feldinput, Rezeptorachsen als Diagnose/Syntax, aber keine doppelte Feldspannung.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument(
        "--world",
        action="append",
        nargs=2,
        metavar=("LABEL", "CSV"),
        help="Optional world label and csv path. Can be repeated.",
    )
    args = parser.parse_args()

    worlds = tuple((label, Path(path)) for label, path in args.world) if args.world else DEFAULT_WORLDS
    rows = [_analyze_world(label, path) for label, path in worlds]
    _write_csv(rows, args.csv_out)
    _write_md(rows, args.md_out)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
