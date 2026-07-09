from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.episode_memory import build_mcm_field_effect
from mini_dio.mini_world import _build_receptor_senses, build_senses_world_relative, build_sensory_profile, load_candles


DEFAULT_WORLDS = {
    "SOL_2025_5M": "data/kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv",
    "SOL_2025_1H": "data/kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv",
    "BTC_2025_5M": "data/kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv",
    "BTC_2025_1H": "data/kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv",
    "KAS_2024_5M": "data/kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv",
    "PAXG_2025_5M": "data/kontrolliert_paxg_2025_5m_10k_PAXGUSDT.csv",
}


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _clip(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    try:
        value = float(value)
    except Exception:
        value = 0.0
    if value != value:
        value = 0.0
    return max(lo, min(hi, value))


def _signed_clip(value: float) -> float:
    return max(-1.0, min(1.0, float(value or 0.0)))


def _neutral_reflection() -> dict[str, float]:
    return {
        "reflection_context_carry": 0.50,
        "reflection_context_strain": 0.18,
        "reflection_context_alignment": 0.72,
    }


def _neutral_temporal() -> dict[str, float]:
    return {
        "mini_afterimage": 0.0,
        "mini_recurrence_strength": 0.0,
    }


def _neutral_neuro() -> dict[str, float]:
    return {
        "mini_neuro_support": 0.50,
        "mini_neuro_load": 0.20,
    }


def _effect(senses: dict) -> dict[str, float]:
    return build_mcm_field_effect(senses, _neutral_reflection(), _neutral_temporal(), _neutral_neuro())


def _role(senses: dict, effect: dict) -> str:
    rec = float(effect.get("mcm_rekopplung_quality", 0.0) or 0.0)
    carry = float(effect.get("mcm_carry_quality", 0.0) or 0.0)
    strain = float(effect.get("mcm_strain_quality", 0.0) or 0.0)
    feld = dict(senses.get("mcm_feldwirkung", {}) or senses.get("fuehlen", {}) or {})
    pressure = _clip(feld.get("mcm_tension", 0.0), 0.0, 1.0)
    if rec >= 0.704 and carry >= 0.533 and pressure <= 0.425 and strain <= 0.18:
        return "zentrum_stabil"
    if pressure >= 0.438 or strain >= 0.25:
        return "spannungsrand_kippnaehe"
    if rec < 0.702 and carry < 0.533:
        return "offene_variante"
    return "rekopplungsnaehe"


def _signature(senses: dict, effect: dict) -> str:
    rezeptoren = dict(senses.get("rezeptoren", {}) or {})
    state = dict(senses.get("perception_regulation_state", {}) or {})
    raw = _clip(state.get("raw_field_intake_pressure", rezeptoren.get("raw_field_intake_pressure", 0.0)), 0.0, 1.0)
    auditory = _clip(state.get("auditory_loudness", rezeptoren.get("auditory_stimulation", 0.0)), 0.0, 1.0)
    visual = _clip(state.get("visual_sharpness", 0.0), 0.0, 1.0)
    rec = float(effect.get("mcm_rekopplung_quality", 0.0) or 0.0)
    strain = float(effect.get("mcm_strain_quality", 0.0) or 0.0)

    parts: list[str] = []
    if auditory >= 0.24:
        parts.append("laut")
    elif auditory <= 0.16:
        parts.append("leise")
    else:
        parts.append("mittelton")

    if visual >= 0.67:
        parts.append("scharf")
    elif visual <= 0.62:
        parts.append("unscharf")
    else:
        parts.append("mittelsicht")

    if raw >= 0.18:
        parts.append("feldstark")
    elif raw <= 0.10:
        parts.append("feldduenn")
    else:
        parts.append("feldmittel")

    if rec >= 0.70 and strain <= 0.17:
        parts.append("getragen")
    elif strain >= 0.24:
        parts.append("angespannt")
    else:
        parts.append("offen")
    return "_".join(parts)


def _load_preferences(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        signature = str(row.get("sensory_signature", "") or "")
        if not signature:
            continue
        out[signature] = {
            "hearing": str(row.get("hearing_preference", "hold") or "hold"),
            "vision": str(row.get("vision_preference", "hold") or "hold"),
            "feeling": str(row.get("feeling_preference", "hold") or "hold"),
        }
    return out


def _scale_signed(value: float, factor: float) -> float:
    return _signed_clip(float(value or 0.0) * factor)


def _apply_feeling_preference(senses: dict, preference: str) -> dict:
    if preference == "hold":
        return senses
    factor = 1.0
    if preference == "down":
        factor = 0.88
    elif preference == "up":
        factor = 1.10
    elif preference == "soften":
        factor = 0.94
    out = dict(senses)
    rezeptoren = dict(out.get("rezeptoren", {}) or {})
    regulation = dict(out.get("perception_regulation_state", {}) or {})
    feld = dict(out.get("mcm_feldwirkung", {}) or out.get("fuehlen", {}) or {})
    for key in ("field_intake_pressure", "contact_pressure", "felt_pressure", "raw_field_intake_pressure", "adapted_field_intake_pressure"):
        if key in rezeptoren:
            rezeptoren[key] = _clip(float(rezeptoren.get(key, 0.0) or 0.0) * factor, 0.0, 1.0)
        if key in regulation:
            regulation[key] = _clip(float(regulation.get(key, 0.0) or 0.0) * factor, 0.0, 1.0)
    feld["mcm_tension"] = _clip(float(feld.get("mcm_tension", 0.0) or 0.0) * factor, 0.0, 1.0)
    out["rezeptoren"] = rezeptoren
    out["perception_regulation_state"] = regulation
    out["organism_adaptation_state"] = dict(regulation)
    out["mcm_feldwirkung"] = feld
    out["fuehlen"] = dict(feld)
    return out


def _apply_preference(senses: dict, preference: dict[str, str]) -> dict:
    sehen = dict(senses.get("sehen", {}) or {})
    hoeren = dict(senses.get("hoeren", {}) or {})

    hearing = preference.get("hearing", "hold")
    if hearing == "down":
        hoeren["energy_tone"] = _scale_signed(hoeren.get("energy_tone", 0.0), 0.88)
        hoeren["energy_shift"] = _scale_signed(hoeren.get("energy_shift", 0.0), 0.88)
    elif hearing == "up":
        hoeren["energy_tone"] = _scale_signed(hoeren.get("energy_tone", 0.0), 1.10)
        hoeren["energy_shift"] = _scale_signed(hoeren.get("energy_shift", 0.0), 1.10)

    vision = preference.get("vision", "hold")
    if vision == "up":
        sehen["form_stability"] = _signed_clip(float(sehen.get("form_stability", 0.0) or 0.0) + 0.08)
        sehen["form_change"] = _scale_signed(sehen.get("form_change", 0.0), 0.92)
    elif vision == "soften":
        sehen["form_stability"] = _signed_clip(float(sehen.get("form_stability", 0.0) or 0.0) - 0.04)
        sehen["form_change"] = _scale_signed(sehen.get("form_change", 0.0), 0.90)

    adjusted = _build_receptor_senses(sehen, hoeren)
    adjusted["receptor_preference_applied"] = {
        "hearing": hearing,
        "vision": vision,
        "feeling": preference.get("feeling", "hold"),
        "passive_only": True,
        "influences_action": False,
    }
    return _apply_feeling_preference(adjusted, preference.get("feeling", "hold"))


def _summarize(label: str, path: Path, preferences: dict[str, dict[str, str]], limit: int, window: int) -> tuple[dict[str, object], dict[str, object]]:
    candles = load_candles(path)
    if limit > 0:
        candles = candles[:limit]
    profile = build_sensory_profile(candles, window=window)

    summaries = {
        "A_BASE": _empty_summary(label, "A_BASE"),
        "B_PREF": _empty_summary(label, "B_PREF"),
    }
    applied = 0
    known = 0
    for index in range(len(candles)):
        base = build_senses_world_relative(candles, index, window=window, profile=profile)
        base_effect = _effect(base)
        signature = _signature(base, base_effect)
        pref = preferences.get(signature)
        if pref:
            known += 1
            adjusted = _apply_preference(base, pref)
            applied += 1
        else:
            adjusted = base
        _add_tick(summaries["A_BASE"], base, base_effect)
        _add_tick(summaries["B_PREF"], adjusted, _effect(adjusted))
    summaries["A_BASE"]["known_signature_ticks"] = known
    summaries["A_BASE"]["preference_applied_ticks"] = 0
    summaries["B_PREF"]["known_signature_ticks"] = known
    summaries["B_PREF"]["preference_applied_ticks"] = applied
    return _finish_summary(summaries["A_BASE"]), _finish_summary(summaries["B_PREF"])


def _empty_summary(world: str, mode: str) -> dict[str, object]:
    return {
        "world": world,
        "mode": mode,
        "ticks": 0,
        "roles": Counter(),
        "rekopplung_sum": 0.0,
        "strain_sum": 0.0,
        "carry_sum": 0.0,
        "raw_sum": 0.0,
        "tension_sum": 0.0,
        "auditory_sum": 0.0,
        "visual_sum": 0.0,
    }


def _add_tick(summary: dict[str, object], senses: dict, effect: dict) -> None:
    role = _role(senses, effect)
    state = dict(senses.get("perception_regulation_state", {}) or {})
    feld = dict(senses.get("mcm_feldwirkung", {}) or senses.get("fuehlen", {}) or {})
    summary["ticks"] = int(summary.get("ticks", 0) or 0) + 1
    roles = summary["roles"]
    assert isinstance(roles, Counter)
    roles[role] += 1
    summary["rekopplung_sum"] = float(summary["rekopplung_sum"]) + float(effect.get("mcm_rekopplung_quality", 0.0) or 0.0)
    summary["strain_sum"] = float(summary["strain_sum"]) + float(effect.get("mcm_strain_quality", 0.0) or 0.0)
    summary["carry_sum"] = float(summary["carry_sum"]) + float(effect.get("mcm_carry_quality", 0.0) or 0.0)
    summary["raw_sum"] = float(summary["raw_sum"]) + _clip(state.get("raw_field_intake_pressure", 0.0), 0.0, 1.0)
    summary["tension_sum"] = float(summary["tension_sum"]) + _clip(feld.get("mcm_tension", 0.0), 0.0, 1.0)
    summary["auditory_sum"] = float(summary["auditory_sum"]) + _clip(state.get("auditory_loudness", 0.0), 0.0, 1.0)
    summary["visual_sum"] = float(summary["visual_sum"]) + _clip(state.get("visual_sharpness", 0.0), 0.0, 1.0)


def _finish_summary(summary: dict[str, object]) -> dict[str, object]:
    ticks = max(1, int(summary.get("ticks", 0) or 0))
    roles = summary["roles"]
    assert isinstance(roles, Counter)
    return {
        "world": summary["world"],
        "mode": summary["mode"],
        "ticks": int(summary["ticks"]),
        "known_signature_ticks": int(summary.get("known_signature_ticks", 0) or 0),
        "preference_applied_ticks": int(summary.get("preference_applied_ticks", 0) or 0),
        "zentrum_ratio": round(roles["zentrum_stabil"] / ticks, 6),
        "rekopplung_ratio": round(roles["rekopplungsnaehe"] / ticks, 6),
        "offen_ratio": round(roles["offene_variante"] / ticks, 6),
        "rand_ratio": round(roles["spannungsrand_kippnaehe"] / ticks, 6),
        "avg_rekopplung": round(float(summary["rekopplung_sum"]) / ticks, 6),
        "avg_strain": round(float(summary["strain_sum"]) / ticks, 6),
        "avg_carry": round(float(summary["carry_sum"]) / ticks, 6),
        "avg_raw_field": round(float(summary["raw_sum"]) / ticks, 6),
        "avg_tension": round(float(summary["tension_sum"]) / ticks, 6),
        "avg_auditory": round(float(summary["auditory_sum"]) / ticks, 6),
        "avg_visual": round(float(summary["visual_sum"]) / ticks, 6),
    }


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pairs: dict[str, dict[str, dict[str, object]]] = defaultdict(dict)
    for row in rows:
        pairs[str(row["world"])][str(row["mode"])] = row
    lines = [
        "# Rezeptorhaltung A/B-Test",
        "",
        "Isolierter passiver Test: A ohne Rezeptorhaltung, B mit sanfter achsenspezifischer Rezeptorhaltung aus der Sinnes-Topologie-Memory.",
        "",
        "Der Test veraendert keinen Runtime-Code, schreibt keine Handlung und erzeugt kein Gate.",
        "",
        "## Vergleich",
        "",
        "| Welt | bekannte Signaturen | angewendet | Delta Zentrum | Delta Rand | Delta Rekopplung | Delta Strain | Delta Rohfeld | Delta Ton | Delta Sicht |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for world, modes in sorted(pairs.items()):
        base = modes.get("A_BASE", {})
        pref = modes.get("B_PREF", {})
        lines.append(
            "| {world} | {known} | {applied} | {dz:.4f} | {dr:.4f} | {drec:.4f} | {ds:.4f} | {draw:.4f} | {daud:.4f} | {dvis:.4f} |".format(
                world=world,
                known=int(pref.get("known_signature_ticks", 0) or 0),
                applied=int(pref.get("preference_applied_ticks", 0) or 0),
                dz=float(pref.get("zentrum_ratio", 0.0) or 0.0) - float(base.get("zentrum_ratio", 0.0) or 0.0),
                dr=float(pref.get("rand_ratio", 0.0) or 0.0) - float(base.get("rand_ratio", 0.0) or 0.0),
                drec=float(pref.get("avg_rekopplung", 0.0) or 0.0) - float(base.get("avg_rekopplung", 0.0) or 0.0),
                ds=float(pref.get("avg_strain", 0.0) or 0.0) - float(base.get("avg_strain", 0.0) or 0.0),
                draw=float(pref.get("avg_raw_field", 0.0) or 0.0) - float(base.get("avg_raw_field", 0.0) or 0.0),
                daud=float(pref.get("avg_auditory", 0.0) or 0.0) - float(base.get("avg_auditory", 0.0) or 0.0),
                dvis=float(pref.get("avg_visual", 0.0) or 0.0) - float(base.get("avg_visual", 0.0) or 0.0),
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Ein sinnvoller Effekt waere: weniger Rand/Kipp oder weniger Strain ohne starken Verlust von Zentrum/Rekopplung.",
            "",
            "Ein problematischer Effekt waere: starke Veraenderung der Rollenverteilung oder kuenstlich geglaettete Wahrnehmung.",
            "",
            "Wie es weitergeht: Wenn B die Feldordnung nur leicht beruhigt, kann die Rezeptorhaltung als passive Option weitergefuehrt werden. Wenn B die Topologie stark verschiebt, bleibt sie vorerst nur Diagnose.",
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
    parser.add_argument("--preference-memory", default="docs/befunde/1001-2000/1001-1500/1279_SINNESAUFNAHME_TOPOLOGIE_REPRO_MEMORY.csv")
    parser.add_argument("--limit", type=int, default=2000)
    parser.add_argument("--window", type=int, default=5)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1281_REZEPTORHALTUNG_AB_TEST.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1281_REZEPTORHALTUNG_AB_TEST.csv")
    args = parser.parse_args()

    preferences = _load_preferences(Path(args.preference_memory))
    worlds = dict(args.world or DEFAULT_WORLDS.items())
    rows: list[dict[str, object]] = []
    for label, path in worlds.items():
        base, pref = _summarize(label, Path(path), preferences, limit=args.limit, window=args.window)
        rows.extend([base, pref])
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
