"""Passive MCM field-effect map for Mini-DIO.

This module classifies stored field episodes for reporting only. It does not
drive action, gates, entries, direction, or motoric behavior.
"""

from __future__ import annotations


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def classify_mcm_field_episode(episode: dict) -> str:
    """Classify a passive MCM field episode into a coarse Wirkung class."""

    transition = str(episode.get("transition", "") or "")
    state = str(episode.get("episode_state", "") or "")
    rekopplung = _safe_float(episode.get("avg_mcm_rekopplung_quality"))
    carry = _safe_float(episode.get("avg_mcm_carry_quality"))
    strain = _safe_float(episode.get("avg_mcm_strain_quality"))
    sensory = _safe_float(episode.get("avg_sensory_coupling"))
    gap = (
        _safe_float(episode.get("avg_visual_field_gap"))
        + _safe_float(episode.get("avg_hearing_field_gap"))
    ) * 0.5

    if "field_strained->field_carried" in transition:
        return "rekoppelnd"
    if "field_carried->field_strained" in transition:
        return "kippend"
    if state == "field_strained":
        return "gespannt"
    if rekopplung >= 0.62 and carry >= 0.32 and strain <= 0.22 and sensory >= 0.80 and gap <= 0.18:
        return "stabil"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "tragend_unruhig"
    return "diffus"


def classify_current_mcm_effect(effect: dict) -> str:
    """Classify the current passive MCM effect for debug display only."""

    state = str(effect.get("field_effect_state", "") or "")
    rekopplung = _safe_float(effect.get("mcm_rekopplung_quality"))
    carry = _safe_float(effect.get("mcm_carry_quality"))
    strain = _safe_float(effect.get("mcm_strain_quality"))
    sensory = _safe_float(effect.get("sensory_coupling"))
    gap = (_safe_float(effect.get("visual_field_gap")) + _safe_float(effect.get("hearing_field_gap"))) * 0.5

    if state == "field_strained":
        if rekopplung >= 0.58 and strain <= 0.32:
            return "rekoppelnd"
        return "gespannt"
    if rekopplung >= 0.62 and carry >= 0.32 and strain <= 0.22 and sensory >= 0.80 and gap <= 0.18:
        return "stabil"
    if rekopplung >= 0.58 and strain <= 0.28:
        return "tragend_unruhig"
    if strain >= 0.28 or gap >= 0.22:
        return "kippend"
    return "diffus"


def build_passive_inner_effect_awareness(effect: dict, effect_class: str | None = None) -> dict:
    """Build a read-only inner awareness payload for the current MCM effect."""

    effect_class = str(effect_class or classify_current_mcm_effect(effect))
    rekopplung = _safe_float(effect.get("mcm_rekopplung_quality"))
    carry = _safe_float(effect.get("mcm_carry_quality"))
    strain = _safe_float(effect.get("mcm_strain_quality"))
    sensory = _safe_float(effect.get("sensory_coupling"))
    visual_gap = _safe_float(effect.get("visual_field_gap"))
    hearing_gap = _safe_float(effect.get("hearing_field_gap"))
    if effect_class == "stabil":
        awareness_state = "inner_effect_stable"
    elif effect_class == "tragend_unruhig":
        awareness_state = "inner_effect_carried_unrest"
    elif effect_class == "kippend":
        awareness_state = "inner_effect_tipping"
    elif effect_class == "gespannt":
        awareness_state = "inner_effect_strained"
    elif effect_class == "rekoppelnd":
        awareness_state = "inner_effect_recoupling"
    else:
        awareness_state = "inner_effect_diffuse"
    return {
        "passive_inner_effect_awareness_state": awareness_state,
        "passive_inner_effect_class": effect_class,
        "passive_inner_effect_rekopplung": rekopplung,
        "passive_inner_effect_carry": carry,
        "passive_inner_effect_strain": strain,
        "passive_inner_effect_sensory_coupling": sensory,
        "passive_inner_effect_visual_gap": visual_gap,
        "passive_inner_effect_hearing_gap": hearing_gap,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_mcm_effect_map(memory_data: dict, limit: int = 12) -> dict:
    """Build a compact passive Wirkung map from mcm_field_episode_memory."""

    episodes = list(dict(memory_data.get("mcm_field_episode_memory", {}) or {}).values())
    class_counts: dict[str, int] = {}
    class_seen: dict[str, int] = {}
    class_rekopplung: dict[str, float] = {}
    class_strain: dict[str, float] = {}
    top = []
    for episode in episodes:
        item = dict(episode or {})
        effect_class = classify_mcm_field_episode(item)
        seen = int(item.get("seen_count", 0) or 0)
        class_counts[effect_class] = int(class_counts.get(effect_class, 0) or 0) + 1
        class_seen[effect_class] = int(class_seen.get(effect_class, 0) or 0) + seen
        class_rekopplung[effect_class] = float(class_rekopplung.get(effect_class, 0.0) or 0.0) + (
            _safe_float(item.get("avg_mcm_rekopplung_quality")) * max(1, seen)
        )
        class_strain[effect_class] = float(class_strain.get(effect_class, 0.0) or 0.0) + (
            _safe_float(item.get("avg_mcm_strain_quality")) * max(1, seen)
        )
        item["mcm_effect_class"] = effect_class
        top.append(item)

    top.sort(
        key=lambda item: (
            int(item.get("seen_count", 0) or 0),
            _safe_float(item.get("avg_mcm_rekopplung_quality")),
            -_safe_float(item.get("avg_mcm_strain_quality")),
        ),
        reverse=True,
    )

    class_summary = {}
    for effect_class, count in sorted(class_counts.items()):
        seen_sum = max(1, int(class_seen.get(effect_class, 0) or 0))
        class_summary[effect_class] = {
            "episode_count": count,
            "seen_count": int(class_seen.get(effect_class, 0) or 0),
            "avg_rekopplung": class_rekopplung.get(effect_class, 0.0) / seen_sum,
            "avg_strain": class_strain.get(effect_class, 0.0) / seen_sum,
        }

    return {
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
        "class_summary": class_summary,
        "top": top[: max(1, int(limit))],
    }


def build_passive_inner_effect_reflection_note(report: dict) -> dict:
    """Build a passive per-run reflection note from inner effect awareness."""

    states = dict(report.get("passive_inner_effect_awareness_states", {}) or {})
    total = max(1, sum(int(value or 0) for value in states.values()))
    sorted_states = sorted(states.items(), key=lambda item: int(item[1] or 0), reverse=True)
    dominant_state, dominant_count = sorted_states[0] if sorted_states else ("inner_effect_unknown", 0)
    rare_states = [state for state, count in sorted_states if int(count or 0) > 0 and (int(count or 0) / total) <= 0.07]
    return {
        "run": int(report.get("run", 0) or 0),
        "data_path": str(report.get("data_path", "") or ""),
        "dominant_inner_effect_state": str(dominant_state),
        "dominant_inner_effect_ratio": int(dominant_count or 0) / total,
        "rare_inner_effect_states": rare_states,
        "avg_mcm_rekopplung_quality": _safe_float(report.get("avg_mcm_rekopplung_quality")),
        "avg_mcm_strain_quality": _safe_float(report.get("avg_mcm_strain_quality")),
        "avg_mcm_carry_quality": _safe_float(report.get("avg_mcm_carry_quality")),
        "states": states,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_effect_reflection_history(notes: list[dict]) -> dict:
    """Build a passive summary over stored inner effect reflection notes."""

    clean_notes = [dict(note or {}) for note in list(notes or []) if isinstance(note, dict)]
    note_count = len(clean_notes)
    dominant_counts: dict[str, int] = {}
    rare_counts: dict[str, int] = {}
    rekopplung_sum = 0.0
    strain_sum = 0.0
    carry_sum = 0.0
    transitions: dict[str, int] = {}
    previous_state = ""

    for note in clean_notes:
        state = str(note.get("dominant_inner_effect_state", "") or "inner_effect_unknown")
        dominant_counts[state] = int(dominant_counts.get(state, 0) or 0) + 1
        for rare_state in list(note.get("rare_inner_effect_states", []) or []):
            rare_key = str(rare_state or "inner_effect_unknown")
            rare_counts[rare_key] = int(rare_counts.get(rare_key, 0) or 0) + 1
        rekopplung_sum += _safe_float(note.get("avg_mcm_rekopplung_quality"))
        strain_sum += _safe_float(note.get("avg_mcm_strain_quality"))
        carry_sum += _safe_float(note.get("avg_mcm_carry_quality"))
        if previous_state:
            transition = f"{previous_state}->{state}"
            transitions[transition] = int(transitions.get(transition, 0) or 0) + 1
        previous_state = state

    avg_rekopplung = rekopplung_sum / max(1, note_count)
    avg_strain = strain_sum / max(1, note_count)
    avg_carry = carry_sum / max(1, note_count)
    dominant_sorted = sorted(dominant_counts.items(), key=lambda item: int(item[1] or 0), reverse=True)
    top_state, top_count = dominant_sorted[0] if dominant_sorted else ("inner_effect_unknown", 0)
    top_ratio = int(top_count or 0) / max(1, note_count)

    if note_count <= 0:
        history_state = "inner_effect_history_empty"
    elif len(dominant_counts) <= 1:
        history_state = "inner_effect_history_single_mode"
    elif top_ratio >= 0.70:
        history_state = "inner_effect_history_dominant_mode"
    else:
        history_state = "inner_effect_history_mixed_mode"

    return {
        "history_state": history_state,
        "note_count": note_count,
        "dominant_inner_effect_counts": dict(sorted(dominant_counts.items())),
        "rare_inner_effect_counts": dict(sorted(rare_counts.items())),
        "dominant_transition_counts": dict(sorted(transitions.items())),
        "top_inner_effect_state": str(top_state),
        "top_inner_effect_ratio": top_ratio,
        "avg_mcm_rekopplung_quality": avg_rekopplung,
        "avg_mcm_strain_quality": avg_strain,
        "avg_mcm_carry_quality": avg_carry,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_effect_meaning_notes(history: dict) -> list[dict]:
    """Build passive meaning notes from an inner effect history.

    The notes are explanatory only. They do not drive action, entries, gates,
    direction, or motoric behavior.
    """

    history = dict(history or {})
    counts = dict(history.get("dominant_inner_effect_counts", {}) or {})
    total = max(1, int(history.get("note_count", 0) or 0))
    notes: list[dict] = []

    definitions = {
        "inner_effect_stable": {
            "meaning_state": "meaning_stable_inner_field",
            "short_meaning": "tragend und gut rekoppelt",
            "field_reading": "Das Feld bleibt tragend, mit relativ sauberer Rekopplung.",
        },
        "inner_effect_carried_unrest": {
            "meaning_state": "meaning_carried_unrest_inner_field",
            "short_meaning": "tragbar, aber spannungsreicher gekoppelt",
            "field_reading": (
                "Die Welt traegt noch, aber das Feld haelt mehr Spannung "
                "und koppelt weniger sauber zurueck."
            ),
        },
        "inner_effect_tipping": {
            "meaning_state": "meaning_tipping_inner_field",
            "short_meaning": "tragend nahe am Kippen",
            "field_reading": (
                "Das Feld traegt noch Anteile, aber Spannung und Feldabstand "
                "nehmen zu."
            ),
        },
        "inner_effect_strained": {
            "meaning_state": "meaning_strained_inner_field",
            "short_meaning": "angespannt und schwerer rekoppelt",
            "field_reading": (
                "Das Feld steht unter hoeherer Spannung und koppelt deutlich "
                "schwaecher zurueck."
            ),
        },
        "inner_effect_diffuse": {
            "meaning_state": "meaning_diffuse_inner_field",
            "short_meaning": "schwach gebunden und unscharf",
            "field_reading": (
                "Die Innenwirkung ist vorhanden, aber noch nicht sauber genug "
                "gebunden."
            ),
        },
    }
    rare_candidates = {"inner_effect_tipping", "inner_effect_strained", "inner_effect_diffuse"}

    def append_note(effect_state: str, count: int, source: str) -> None:
        effect_state = str(effect_state or "inner_effect_unknown")
        count = int(count or 0)
        if count <= 0:
            return
        if effect_state in {str(note.get("inner_effect_state", "") or "") for note in notes}:
            return
        definition = definitions.get(
            effect_state,
            {
                "meaning_state": "meaning_unknown_inner_field",
                "short_meaning": "unbekannte Innenwirkung",
                "field_reading": "Die Innenwirkung ist noch nicht zugeordnet.",
            },
        )
        notes.append(
            {
                "inner_effect_state": effect_state,
                "meaning_state": definition["meaning_state"],
                "short_meaning": definition["short_meaning"],
                "field_reading": definition["field_reading"],
                "meaning_source": source,
                "seen_count": count,
                "seen_ratio": count / total,
                "history_state": str(history.get("history_state", "") or ""),
                "avg_mcm_rekopplung_quality": _safe_float(history.get("avg_mcm_rekopplung_quality")),
                "avg_mcm_strain_quality": _safe_float(history.get("avg_mcm_strain_quality")),
                "avg_mcm_carry_quality": _safe_float(history.get("avg_mcm_carry_quality")),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )

    for effect_state, count in sorted(counts.items()):
        append_note(effect_state, int(count or 0), "dominant_history")
    rare_counts = dict(history.get("rare_inner_effect_counts", {}) or {})
    for effect_state, count in sorted(rare_counts.items()):
        if str(effect_state or "") in rare_candidates:
            append_note(str(effect_state), int(count or 0), "rare_recurrence")
    return notes


def build_passive_inner_effect_meaning_display(
    awareness: dict,
    meaning_notes: list[dict],
) -> dict:
    """Build a read-only display for the current inner-effect meaning."""

    awareness = dict(awareness or {})
    state = str(awareness.get("passive_inner_effect_awareness_state", "") or "")
    meaning = {}
    for note in list(meaning_notes or []):
        if not isinstance(note, dict):
            continue
        if str(note.get("inner_effect_state", "") or "") == state:
            meaning = dict(note)
            break

    if meaning:
        display_state = "meaning_display_found"
        meaning_state = str(meaning.get("meaning_state", "") or "")
        short_meaning = str(meaning.get("short_meaning", "") or "")
        field_reading = str(meaning.get("field_reading", "") or "")
        seen_ratio = _safe_float(meaning.get("seen_ratio"))
    else:
        display_state = "meaning_display_unavailable"
        meaning_state = ""
        short_meaning = ""
        field_reading = ""
        seen_ratio = 0.0

    return {
        "display_state": display_state,
        "inner_effect_state": state,
        "meaning_state": meaning_state,
        "short_meaning": short_meaning,
        "field_reading": field_reading,
        "seen_ratio": seen_ratio,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_field_map(report: dict, meaning_notes: list[dict]) -> dict:
    """Build a read-only profile of current inner-field meaning distribution."""

    report = dict(report or {})
    states = dict(report.get("passive_inner_effect_awareness_states", {}) or {})
    display_states = dict(report.get("passive_inner_effect_meaning_display_states", {}) or {})
    total = max(1, sum(int(value or 0) for value in states.values()))
    meanings_by_state = {}
    for note in list(meaning_notes or []):
        if not isinstance(note, dict):
            continue
        state = str(note.get("inner_effect_state", "") or "")
        if state:
            meanings_by_state[state] = dict(note)

    profile = {}
    named_count = 0
    unnamed_count = 0
    for state, count_value in sorted(states.items()):
        count = int(count_value or 0)
        note = meanings_by_state.get(str(state), {})
        meaning_state = str(note.get("meaning_state", "") or "")
        short_meaning = str(note.get("short_meaning", "") or "")
        if meaning_state:
            named_count += count
        else:
            unnamed_count += count
        profile[str(state)] = {
            "count": count,
            "ratio": count / total,
            "meaning_state": meaning_state,
            "short_meaning": short_meaning,
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
        }

    sorted_profile = sorted(profile.items(), key=lambda item: int(item[1].get("count", 0) or 0), reverse=True)
    dominant_state = sorted_profile[0][0] if sorted_profile else "inner_effect_unknown"
    dominant = profile.get(dominant_state, {})
    if named_count >= total and len(profile) >= 2:
        map_state = "inner_field_map_fully_named"
    elif named_count > 0 and len(profile) >= 2:
        map_state = "inner_field_map_partly_named"
    elif len(profile) >= 2:
        map_state = "inner_field_map_unlabeled_distribution"
    else:
        map_state = "inner_field_map_single_surface"

    return {
        "run": int(report.get("run", 0) or 0),
        "data_path": str(report.get("data_path", "") or ""),
        "passive_world_label": str(report.get("passive_world_label", "") or ""),
        "map_state": map_state,
        "total_observations": total,
        "named_count": named_count,
        "unnamed_count": unnamed_count,
        "named_ratio": named_count / total,
        "dominant_inner_effect_state": dominant_state,
        "dominant_ratio": _safe_float(dominant.get("ratio")),
        "display_states": dict(sorted(display_states.items())),
        "profile": profile,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def _profile_ratios(field_map: dict) -> dict[str, float]:
    profile = dict((field_map or {}).get("profile", {}) or {})
    ratios = {}
    for state, payload in profile.items():
        ratios[str(state)] = _safe_float(dict(payload or {}).get("ratio"))
    return ratios


def _profile_similarity(left: dict, right: dict) -> float:
    left_ratios = _profile_ratios(left)
    right_ratios = _profile_ratios(right)
    states = sorted(set(left_ratios) | set(right_ratios))
    if not states:
        return 0.0
    distance = sum(abs(left_ratios.get(state, 0.0) - right_ratios.get(state, 0.0)) for state in states) * 0.5
    return max(0.0, min(1.0, 1.0 - distance))


def build_passive_inner_field_map_comparison(field_maps: list[dict], limit: int = 8) -> dict:
    """Compare stored passive inner-field maps by profile distribution only."""

    clean_maps = [dict(item or {}) for item in list(field_maps or []) if isinstance(item, dict)]
    if not clean_maps:
        return {
            "comparison_state": "inner_field_map_comparison_empty",
            "map_count": 0,
            "pairs": [],
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
        }

    pairs = []
    for left_index in range(len(clean_maps)):
        for right_index in range(left_index + 1, len(clean_maps)):
            left = clean_maps[left_index]
            right = clean_maps[right_index]
            similarity = _profile_similarity(left, right)
            pairs.append(
                {
                    "left_index": left_index,
                    "right_index": right_index,
                    "left_run": int(left.get("run", 0) or 0),
                    "right_run": int(right.get("run", 0) or 0),
                    "left_data_path": str(left.get("data_path", "") or ""),
                    "right_data_path": str(right.get("data_path", "") or ""),
                    "left_world_label": str(left.get("passive_world_label", "") or ""),
                    "right_world_label": str(right.get("passive_world_label", "") or ""),
                    "similarity": similarity,
                    "left_dominant": str(left.get("dominant_inner_effect_state", "") or ""),
                    "right_dominant": str(right.get("dominant_inner_effect_state", "") or ""),
                    "left_map_state": str(left.get("map_state", "") or ""),
                    "right_map_state": str(right.get("map_state", "") or ""),
                    "passive_only": 1,
                    "read_by_mini_dio": 0,
                    "influences_action": 0,
                    "is_gate": 0,
                    "is_motoric": 0,
                    "is_entry_signal": 0,
                    "is_direction_signal": 0,
                }
            )
    pairs.sort(key=lambda item: float(item.get("similarity", 0.0) or 0.0), reverse=True)
    similarities = [float(pair.get("similarity", 0.0) or 0.0) for pair in pairs]
    avg_similarity = sum(similarities) / max(1, len(similarities))
    min_similarity = min(similarities) if similarities else 0.0
    max_similarity = max(similarities) if similarities else 0.0
    if len(clean_maps) < 2:
        comparison_state = "inner_field_map_comparison_single"
    elif min_similarity >= 0.86:
        comparison_state = "inner_field_map_cluster_tight"
    elif avg_similarity >= 0.78:
        comparison_state = "inner_field_map_cluster_related"
    else:
        comparison_state = "inner_field_map_cluster_drifting"

    return {
        "comparison_state": comparison_state,
        "map_count": len(clean_maps),
        "pair_count": len(pairs),
        "avg_similarity": avg_similarity,
        "min_similarity": min_similarity,
        "max_similarity": max_similarity,
        "pairs": pairs[: max(1, int(limit))],
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_field_bridge_stable_contrast(field_maps: list[dict]) -> dict:
    """Contrast carried-unrest dominated maps with stable dominated maps."""

    clean_maps = [dict(item or {}) for item in list(field_maps or []) if isinstance(item, dict)]
    bridge_maps = [
        item for item in clean_maps
        if str(item.get("dominant_inner_effect_state", "") or "") == "inner_effect_carried_unrest"
    ]
    stable_maps = [
        item for item in clean_maps
        if str(item.get("dominant_inner_effect_state", "") or "") == "inner_effect_stable"
    ]
    states = sorted({state for item in clean_maps for state in _profile_ratios(item)})

    def average_profile(items: list[dict]) -> dict[str, float]:
        if not items:
            return {state: 0.0 for state in states}
        return {
            state: sum(_profile_ratios(item).get(state, 0.0) for item in items) / len(items)
            for state in states
        }

    bridge_profile = average_profile(bridge_maps)
    stable_profile = average_profile(stable_maps)
    contrast = {
        state: stable_profile.get(state, 0.0) - bridge_profile.get(state, 0.0)
        for state in states
    }
    strongest = sorted(contrast.items(), key=lambda item: abs(float(item[1] or 0.0)), reverse=True)
    if not bridge_maps or not stable_maps:
        contrast_state = "bridge_stable_contrast_incomplete"
    elif abs(contrast.get("inner_effect_stable", 0.0)) >= abs(contrast.get("inner_effect_carried_unrest", 0.0)):
        contrast_state = "bridge_stable_contrast_stable_axis"
    else:
        contrast_state = "bridge_stable_contrast_unrest_axis"

    return {
        "contrast_state": contrast_state,
        "map_count": len(clean_maps),
        "bridge_map_count": len(bridge_maps),
        "stable_map_count": len(stable_maps),
        "bridge_avg_profile": bridge_profile,
        "stable_avg_profile": stable_profile,
        "stable_minus_bridge": contrast,
        "strongest_differences": [
            {"state": state, "stable_minus_bridge": value}
            for state, value in strongest[:6]
        ],
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_field_archetypes(field_maps: list[dict]) -> dict:
    """Build a passive ontology view for known inner-field archetypes."""

    clean_maps = [dict(item or {}) for item in list(field_maps or []) if isinstance(item, dict)]
    definitions = {
        "inner_effect_stable": {
            "archetype_state": "archetype_stable_rekopplung",
            "name": "stable",
            "short_reading": "tragend und gut rekoppelt",
            "field_quality": "ruhiger tragender Innenfeldbereich",
        },
        "inner_effect_carried_unrest": {
            "archetype_state": "archetype_carried_unrest_tension",
            "name": "carried_unrest",
            "short_reading": "tragend, aber spannungsreicher",
            "field_quality": "tragende Spannungsnaehe ohne Kollaps",
        },
        "inner_effect_tipping": {
            "archetype_state": "archetype_tipping_edge",
            "name": "tipping",
            "short_reading": "tragend nahe am Kippen",
            "field_quality": "randnaher Uebergang mit steigender Kippnaehe",
        },
        "inner_effect_strained": {
            "archetype_state": "archetype_strained_load",
            "name": "strained",
            "short_reading": "angespannt und schwerer rekoppelt",
            "field_quality": "belastete Innenfeldlage mit hoeherer Spannung",
        },
        "inner_effect_diffuse": {
            "archetype_state": "archetype_diffuse_unbound",
            "name": "diffuse",
            "short_reading": "schwach gebunden und unscharf",
            "field_quality": "vorhandene Wirkung ohne saubere Bindung",
        },
    }
    observed_counts = {state: 0 for state in definitions}
    dominant_counts = {state: 0 for state in definitions}
    ratio_sums = {state: 0.0 for state in definitions}
    for field_map in clean_maps:
        dominant = str(field_map.get("dominant_inner_effect_state", "") or "")
        if dominant in dominant_counts:
            dominant_counts[dominant] += 1
        ratios = _profile_ratios(field_map)
        for state in definitions:
            ratio = ratios.get(state, 0.0)
            if ratio > 0.0:
                observed_counts[state] += 1
                ratio_sums[state] += ratio

    archetypes = {}
    for state, definition in definitions.items():
        seen_maps = observed_counts.get(state, 0)
        dominant_maps = dominant_counts.get(state, 0)
        avg_ratio = ratio_sums.get(state, 0.0) / max(1, seen_maps)
        if dominant_maps > 0:
            maturity_state = "archetype_dominant_observed"
        elif seen_maps >= max(2, len(clean_maps) // 2):
            maturity_state = "archetype_recurring_background"
        elif seen_maps > 0:
            maturity_state = "archetype_sparse_trace"
        else:
            maturity_state = "archetype_unseen"
        archetypes[state] = {
            **definition,
            "inner_effect_state": state,
            "seen_map_count": seen_maps,
            "dominant_map_count": dominant_maps,
            "avg_ratio_when_seen": avg_ratio,
            "maturity_state": maturity_state,
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
        }

    if not clean_maps:
        ontology_state = "inner_field_archetypes_empty"
    elif any(item["dominant_map_count"] > 0 for item in archetypes.values()):
        ontology_state = "inner_field_archetypes_observed"
    else:
        ontology_state = "inner_field_archetypes_background_only"

    return {
        "ontology_state": ontology_state,
        "map_count": len(clean_maps),
        "archetypes": archetypes,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }


def build_passive_inner_field_archetype_matrix(field_maps: list[dict], archetypes: dict) -> dict:
    """Build a passive matrix from world maps to archetype readings."""

    clean_maps = [dict(item or {}) for item in list(field_maps or []) if isinstance(item, dict)]
    archetype_items = dict((archetypes or {}).get("archetypes", {}) or {})
    rows = []
    cluster_counts: dict[str, int] = {}
    for index, field_map in enumerate(clean_maps):
        dominant = str(field_map.get("dominant_inner_effect_state", "") or "inner_effect_unknown")
        archetype = dict(archetype_items.get(dominant, {}) or {})
        archetype_state = str(archetype.get("archetype_state", "") or "archetype_unknown")
        cluster_counts[archetype_state] = int(cluster_counts.get(archetype_state, 0) or 0) + 1
        rows.append(
            {
                "index": index,
                "run": int(field_map.get("run", 0) or 0),
                "data_path": str(field_map.get("data_path", "") or ""),
                "passive_world_label": str(field_map.get("passive_world_label", "") or ""),
                "dominant_inner_effect_state": dominant,
                "dominant_ratio": _safe_float(field_map.get("dominant_ratio")),
                "map_state": str(field_map.get("map_state", "") or ""),
                "archetype_state": archetype_state,
                "archetype_name": str(archetype.get("name", "") or ""),
                "short_reading": str(archetype.get("short_reading", "") or ""),
                "field_quality": str(archetype.get("field_quality", "") or ""),
                "passive_only": 1,
                "read_by_mini_dio": 0,
                "influences_action": 0,
                "is_gate": 0,
                "is_motoric": 0,
                "is_entry_signal": 0,
                "is_direction_signal": 0,
            }
        )

    if not rows:
        matrix_state = "inner_field_archetype_matrix_empty"
    elif len(cluster_counts) == 1:
        matrix_state = "inner_field_archetype_matrix_single_island"
    else:
        matrix_state = "inner_field_archetype_matrix_multi_island"

    return {
        "matrix_state": matrix_state,
        "map_count": len(clean_maps),
        "archetype_cluster_counts": dict(sorted(cluster_counts.items())),
        "rows": rows,
        "passive_only": 1,
        "read_by_mini_dio": 0,
        "influences_action": 0,
        "is_gate": 0,
        "is_motoric": 0,
        "is_entry_signal": 0,
        "is_direction_signal": 0,
    }
