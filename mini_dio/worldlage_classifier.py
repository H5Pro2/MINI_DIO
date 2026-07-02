from __future__ import annotations


def classify_worldlage(row: dict[str, object]) -> str:
    """Classify a passive world-state from measured field/sensory values.

    This classifier does not use file names, asset names, direction labels or
    action outcomes. It only reads the passive A-state of the observed world.
    The classes are diagnostic and intentionally coarse.
    """

    zentrum = _to_float(row.get("zentrum_ratio"))
    rand = _to_float(row.get("rand_ratio"))
    rekopplung = _to_float(row.get("avg_rekopplung"))
    strain = _to_float(row.get("avg_strain"))
    raw_field = _to_float(row.get("avg_raw_field"))
    auditory = _to_float(row.get("avg_auditory"))
    visual = _to_float(row.get("avg_visual"))

    if zentrum >= 0.88 and rekopplung >= 0.727:
        if rand >= 0.015:
            return "ueberstabil_mit_randreiz"
        if raw_field <= 0.03 and auditory <= 0.03 and visual >= 0.82 and strain <= 0.11:
            return "ueberstabil_extrem_leise_scharf"
        if visual < 0.79:
            return "ueberstabil_visuell_weicher"
        if raw_field <= 0.065 and auditory <= 0.10 and visual >= 0.82 and strain <= 0.12:
            return "ueberstabil_leise_scharf"
        return "ueberstabil_gemischt"
    if rand >= 0.015:
        return "randlastige_sinneslage"
    if zentrum >= 0.78 and strain <= 0.145:
        return "ruhig_zentrumsnah"
    if raw_field <= 0.11 and auditory <= 0.19:
        if visual >= 0.66:
            return "leise_scharf_duenn"
        return "leise_duenn"
    if auditory >= 0.23 or raw_field >= 0.15:
        return "lauter_feldkontakt"
    if zentrum < 0.70 or rekopplung < 0.709:
        return "offen_suchend"
    return "normale_weltspannung"


def classify_adaptation_delta(base: dict[str, object], adapted: dict[str, object]) -> dict[str, object]:
    delta_zentrum = _to_float(adapted.get("zentrum_ratio")) - _to_float(base.get("zentrum_ratio"))
    delta_rand = _to_float(adapted.get("rand_ratio")) - _to_float(base.get("rand_ratio"))
    delta_rekopplung = _to_float(adapted.get("avg_rekopplung")) - _to_float(base.get("avg_rekopplung"))
    delta_strain = _to_float(adapted.get("avg_strain")) - _to_float(base.get("avg_strain"))
    if abs(delta_zentrum) > 0.04 or abs(delta_rekopplung) > 0.015:
        outcome = "verschiebend"
    elif delta_rand < -0.001 and delta_strain < -0.0005 and delta_zentrum > -0.01 and delta_rekopplung > -0.002:
        if delta_zentrum >= 0.003 or delta_rekopplung >= 0.0005:
            outcome = "beruhigend"
        else:
            outcome = "stabil_leicht"
    elif delta_rand > 0.002 or delta_strain > 0.001:
        outcome = "verschiebend"
    else:
        outcome = "neutral"
    return {
        "delta_zentrum": round(delta_zentrum, 6),
        "delta_rand": round(delta_rand, 6),
        "delta_rekopplung": round(delta_rekopplung, 6),
        "delta_strain": round(delta_strain, 6),
        "delta_raw_field": round(_to_float(adapted.get("avg_raw_field")) - _to_float(base.get("avg_raw_field")), 6),
        "delta_auditory": round(_to_float(adapted.get("avg_auditory")) - _to_float(base.get("avg_auditory")), 6),
        "delta_visual": round(_to_float(adapted.get("avg_visual")) - _to_float(base.get("avg_visual")), 6),
        "adaptation_outcome": outcome,
    }


def _to_float(value: object) -> float:
    try:
        number = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if number != number else number
