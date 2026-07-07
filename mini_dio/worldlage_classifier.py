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

    return _dominant_label(
        {
            "ueberstabil_mit_randreiz": _mean(zentrum, rekopplung, rand),
            "ueberstabil_extrem_leise_scharf": _mean(zentrum, rekopplung, 1.0 - raw_field, 1.0 - auditory, visual, 1.0 - strain),
            "ueberstabil_visuell_weicher": _mean(zentrum, rekopplung, 1.0 - visual),
            "ueberstabil_leise_scharf": _mean(zentrum, rekopplung, 1.0 - raw_field, 1.0 - auditory, visual, 1.0 - strain),
            "ueberstabil_gemischt": _mean(zentrum, rekopplung),
            "randlastige_sinneslage": rand,
            "ruhig_zentrumsnah": _mean(zentrum, 1.0 - strain, rekopplung),
            "leise_scharf_duenn": _mean(1.0 - raw_field, 1.0 - auditory, visual),
            "leise_duenn": _mean(1.0 - raw_field, 1.0 - auditory, 1.0 - visual),
            "lauter_feldkontakt": _mean(auditory, raw_field),
            "offen_suchend": _mean(1.0 - zentrum, 1.0 - rekopplung),
            "normale_weltspannung": _mean(1.0 - rand, 1.0 - strain, 1.0 - raw_field, 1.0 - auditory),
        }
    )


def classify_adaptation_delta(base: dict[str, object], adapted: dict[str, object]) -> dict[str, object]:
    delta_zentrum = _to_float(adapted.get("zentrum_ratio")) - _to_float(base.get("zentrum_ratio"))
    delta_rand = _to_float(adapted.get("rand_ratio")) - _to_float(base.get("rand_ratio"))
    delta_rekopplung = _to_float(adapted.get("avg_rekopplung")) - _to_float(base.get("avg_rekopplung"))
    delta_strain = _to_float(adapted.get("avg_strain")) - _to_float(base.get("avg_strain"))
    shift_pressure = _mean(abs(delta_zentrum), abs(delta_rekopplung), max(0.0, delta_rand), max(0.0, delta_strain))
    calming_pressure = _mean(max(0.0, -delta_rand), max(0.0, -delta_strain), max(0.0, delta_zentrum), max(0.0, delta_rekopplung))
    light_stability_pressure = _mean(max(0.0, -delta_rand), max(0.0, -delta_strain), 1.0 - abs(delta_zentrum), 1.0 - abs(delta_rekopplung))
    neutral_pressure = _mean(1.0 - abs(delta_zentrum), 1.0 - abs(delta_rand), 1.0 - abs(delta_rekopplung), 1.0 - abs(delta_strain))
    outcome = _dominant_label(
        {
            "verschiebend": shift_pressure,
            "beruhigend": calming_pressure,
            "stabil_leicht": light_stability_pressure,
            "neutral": neutral_pressure,
        }
    )
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


def _clip01(value: object) -> float:
    return max(0.0, min(1.0, _to_float(value)))


def _mean(*values: object) -> float:
    clean = [_clip01(value) for value in values]
    return sum(clean) / max(1, len(clean))


def _dominant_label(scores: dict[str, float]) -> str:
    clean = {key: _clip01(value) for key, value in scores.items()}
    if not clean:
        return "normale_weltspannung"
    return max(clean, key=clean.get)
