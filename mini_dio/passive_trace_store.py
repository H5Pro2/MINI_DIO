"""Passive relation and trace persistence helpers for MINI_DIO.

This module stores passive relations, contact-lage traces, sentence traces and
reflection traces. It does not provide action diagnostics and it does not feed
motoric behavior.
"""

from __future__ import annotations

from mini_dio.dio_syntax import (
    make_contact_lage_symbol,
)


def sensor_relation_rank(item: dict) -> tuple:
    kind = str(item.get("relation_kind", "") or "")
    return (
        kind == "same_family_cross_phase",
        kind == "bearing_sensor_neighbor",
        float(item.get("sensor_relation_trace", 0.0) or 0.0),
        int(item.get("left_executed", 0) or 0) + int(item.get("right_executed", 0) or 0),
        float(item.get("left_reward", 0.0) or 0.0) + float(item.get("right_reward", 0.0) or 0.0),
    )


def neighbor_consequence_rank(item: dict) -> tuple:
    state = str(item.get("neighbor_consequence_state", "") or "")
    return (
        state == "reifende_verwandtschaft",
        state == "vorsichtige_verwandtschaft",
        state == "beobachtete_verwandtschaft",
        float(item.get("sensor_similarity", 0.0) or 0.0),
        float(item.get("target_reward_sum", 0.0) or 0.0),
        float(item.get("reference_reward_sum", 0.0) or 0.0),
    )


def contact_lage_rank(item: dict) -> tuple:
    state = str(item.get("contact_lage_state", "") or "")
    return (
        state == "exakte_wiederbegegnung",
        state == "nahe_aehnlichkeit",
        state == "ferne_aehnlichkeit",
        float(item.get("contact_reward_sum", 0.0) or 0.0),
        int(item.get("direct_positive_action", 0) or 0),
        int(item.get("observation_to_positive_action", 0) or 0),
        int(item.get("held_observation", 0) or 0),
    )


def reflection_seed_rank(item: dict) -> tuple:
    state = str(item.get("reflection_state", "") or "")
    return (
        state == "reflection_seed_reconfirmed",
        state == "reflection_seed_overheld",
        float(item.get("followup_executed_reward", 0.0) or 0.0),
        int(item.get("followup_executed_aligned_count", 0) or 0),
        float(item.get("prior_execution_reward_sum", 0.0) or 0.0),
        int(item.get("prior_execution_count", 0) or 0),
    )


def reflection_map_rank(item: dict) -> tuple:
    state = str(item.get("reflection_map_state", "") or "")
    return (
        state == "reflection_memory_reconfirmed",
        state == "reflection_memory_conflict",
        state == "reflection_memory_observed",
        float(item.get("reward_sum", 0.0) or 0.0),
        int(item.get("seen_count", 0) or 0),
        int(item.get("executed_count", 0) or 0),
    )


def sentence_trace_rank(item: dict) -> tuple:
    return (
        float(item.get("reward_sum", 0.0) or 0.0),
        int(item.get("count", 0) or 0),
        str(item.get("episode_contact_state", "") or "") == "kontakt_handlung_bestaetigt",
    )


def _compact_mapping(data: dict, key: str, limit: int, ranker) -> dict:
    limit = max(1, int(limit))
    mapping = data.setdefault(key, {})
    if not isinstance(mapping, dict):
        data[key] = {}
        return {"before": 0, "after": 0, "removed": 0}
    before = len(mapping)
    if before <= limit:
        return {"before": before, "after": before, "removed": 0}
    sorted_items = sorted(mapping.items(), key=lambda item: ranker(dict(item[1] or {})), reverse=True)
    kept = dict(sorted_items[:limit])
    data[key] = kept
    after = len(kept)
    return {"before": before, "after": after, "removed": before - after}


def set_relation_summary(data: dict, support_pair: str, summary: dict) -> None:
    support_pair = str(support_pair or "-") or "-"
    if support_pair == "-":
        return
    relations = data.setdefault("relations", {})
    relations[support_pair] = {
        "support_pair": support_pair,
        "families": list(summary.get("families", []) or []),
        "phases": list(summary.get("phases", []) or []),
        "phase_count": int(summary.get("phase_count", 0) or 0),
        "rows": int(summary.get("rows", 0) or 0),
        "executed_local_confirmation": int(summary.get("executed_local_confirmation", 0) or 0),
        "observed_related_potential": int(summary.get("observed_related_potential", 0) or 0),
        "long_local": int(summary.get("long_local", 0) or 0),
        "short_local": int(summary.get("short_local", 0) or 0),
        "avg_local_confirmation": float(summary.get("avg_local_confirmation", 0.0) or 0.0),
        "max_local_confirmation": float(summary.get("max_local_confirmation", 0.0) or 0.0),
        "reward_sum": float(summary.get("reward_sum", 0.0) or 0.0),
        "passive_only": True,
    }


def set_sensor_relation_summary(data: dict, relation_key: str, summary: dict, max_items: int) -> None:
    relation_key = str(relation_key or "-") or "-"
    if relation_key == "-":
        return
    relations = data.setdefault("sensor_relations", {})
    relations[relation_key] = {
        "relation_key": relation_key,
        "left_family": str(summary.get("left_family", "-") or "-"),
        "right_family": str(summary.get("right_family", "-") or "-"),
        "left_phase": str(summary.get("left_phase", "-") or "-"),
        "right_phase": str(summary.get("right_phase", "-") or "-"),
        "relation_kind": str(summary.get("relation_kind", "-") or "-"),
        "sensor_relation_trace": float(summary.get("sensor_relation_trace", 0.0) or 0.0),
        "sensor_distance": float(summary.get("sensor_distance", 0.0) or 0.0),
        "visual_mcm_gap": float(summary.get("visual_mcm_gap", 0.0) or 0.0),
        "tone_tension_gap": float(summary.get("tone_tension_gap", 0.0) or 0.0),
        "left_reward": float(summary.get("left_reward", 0.0) or 0.0),
        "right_reward": float(summary.get("right_reward", 0.0) or 0.0),
        "left_executed": int(summary.get("left_executed", 0) or 0),
        "right_executed": int(summary.get("right_executed", 0) or 0),
        "passive_only": True,
    }
    compact_sensor_relations(data, max_items)


def set_neighbor_consequence_summary(data: dict, relation_key: str, summary: dict, max_items: int) -> None:
    relation_key = str(relation_key or "-") or "-"
    if relation_key == "-":
        return
    relations = data.setdefault("neighbor_consequences", {})
    relations[relation_key] = {
        "relation_key": relation_key,
        "target_family": str(summary.get("target_family", "-") or "-"),
        "reference_family": str(summary.get("reference_family", "-") or "-"),
        "neighbor_consequence_state": str(summary.get("neighbor_consequence_state", "-") or "-"),
        "sensor_distance": float(summary.get("sensor_distance", 0.0) or 0.0),
        "sensor_similarity": float(summary.get("sensor_similarity", 0.0) or 0.0),
        "target_reward_sum": float(summary.get("target_reward_sum", 0.0) or 0.0),
        "reference_reward_sum": float(summary.get("reference_reward_sum", 0.0) or 0.0),
        "target_executed_rows": int(summary.get("target_executed_rows", 0) or 0),
        "target_observed_rows": int(summary.get("target_observed_rows", 0) or 0),
        "reference_executed_rows": int(summary.get("reference_executed_rows", 0) or 0),
        "reference_observed_rows": int(summary.get("reference_observed_rows", 0) or 0),
        "target_class": str(summary.get("target_class", "-") or "-"),
        "reference_class": str(summary.get("reference_class", "-") or "-"),
        "target_phases": str(summary.get("target_phases", "-") or "-"),
        "reference_phases": str(summary.get("reference_phases", "-") or "-"),
        "passive_only": True,
    }
    compact_neighbor_consequences(data, max_items)


def compact_neighbor_consequences(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "neighbor_consequences", max_items, neighbor_consequence_rank)


def compact_sensor_relations(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "sensor_relations", max_items, sensor_relation_rank)


def compact_contact_lagen(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "contact_lagen", max_items, contact_lage_rank)


def compact_sentence_traces(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "sentence_traces", max_items, sentence_trace_rank)


def compact_reflection_seeds(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "reflection_seeds", max_items, reflection_seed_rank)


def compact_reflection_maps(data: dict, max_items: int) -> dict:
    return _compact_mapping(data, "reflection_maps", max_items, reflection_map_rank)


def store_contact_lage(data: dict, contact_id: str, payload: dict) -> None:
    contact_id = str(contact_id or "").strip()
    if not contact_id:
        return
    state = str(payload.get("contact_lage_state", "") or "")
    contact_lagen = data.setdefault("contact_lagen", {})
    current = dict(contact_lagen.get(contact_id, {}) or {})
    current.update(
        {
            "contact_id": contact_id,
            "contact_symbol": make_contact_lage_symbol(payload),
            "contact_lage_state": state,
            "debug_root": str(payload.get("debug_root", "") or ""),
            "passive_only": 1,
            "runs": int(payload.get("runs", current.get("runs", 0)) or 0),
            "trades_total": int(payload.get("trades_total", current.get("trades_total", 0)) or 0),
            "reward_total": float(payload.get("reward_total", current.get("reward_total", 0.0)) or 0.0),
            "contact_reward_sum": float(
                payload.get("contact_reward_sum", current.get("contact_reward_sum", 0.0)) or 0.0
            ),
            "direct_positive_action": int(
                payload.get("direct_positive_action", current.get("direct_positive_action", 0)) or 0
            ),
            "observation_to_positive_action": int(
                payload.get(
                    "observation_to_positive_action",
                    current.get("observation_to_positive_action", 0),
                )
                or 0
            ),
            "held_observation": int(payload.get("held_observation", current.get("held_observation", 0)) or 0),
            "quiet_family": int(payload.get("quiet_family", current.get("quiet_family", 0)) or 0),
            "top_direct_action": list(payload.get("top_direct_action", current.get("top_direct_action", [])) or []),
            "top_observation_to_action": list(
                payload.get("top_observation_to_action", current.get("top_observation_to_action", [])) or []
            ),
        }
    )
    contact_lagen[contact_id] = current


def store_sentence_trace(data: dict, sentence_symbol: str, payload: dict) -> None:
    sentence_symbol = str(sentence_symbol or "").strip()
    if not sentence_symbol:
        return
    traces = data.setdefault("sentence_traces", {})
    current = dict(traces.get(sentence_symbol, {}) or {})
    current.update(
        {
            "sentence_symbol": sentence_symbol,
            "contact_symbol": str(payload.get("contact_symbol", "") or ""),
            "contact_lage_state": str(payload.get("contact_lage_state", "") or ""),
            "symbol_family": str(payload.get("symbol_family", "") or ""),
            "episode_contact_state": str(payload.get("episode_contact_state", "") or ""),
            "count": int(payload.get("count", current.get("count", 0)) or 0),
            "reward_sum": float(payload.get("reward_sum", current.get("reward_sum", 0.0)) or 0.0),
            "actions": str(payload.get("actions", current.get("actions", "")) or ""),
            "passive_only": 1,
        }
    )
    traces[sentence_symbol] = current


def store_reflection_seed(data: dict, reflection_symbol: str, payload: dict) -> None:
    reflection_symbol = str(reflection_symbol or "").strip()
    if not reflection_symbol:
        return
    seeds = data.setdefault("reflection_seeds", {})
    current = dict(seeds.get(reflection_symbol, {}) or {})
    current.update(
        {
            "reflection_symbol": reflection_symbol,
            "symbol_family": str(payload.get("symbol_family", current.get("symbol_family", "")) or ""),
            "reflection_state": str(payload.get("reflection_state", current.get("reflection_state", "")) or ""),
            "prior_observation_count": int(
                payload.get("prior_observation_count", current.get("prior_observation_count", 0)) or 0
            ),
            "prior_execution_count": int(
                payload.get("prior_execution_count", current.get("prior_execution_count", 0)) or 0
            ),
            "prior_observation_reward_potential_sum": float(
                payload.get(
                    "prior_observation_reward_potential_sum",
                    current.get("prior_observation_reward_potential_sum", 0.0),
                )
                or 0.0
            ),
            "prior_execution_reward_sum": float(
                payload.get("prior_execution_reward_sum", current.get("prior_execution_reward_sum", 0.0)) or 0.0
            ),
            "followup_seen_count": int(
                payload.get("followup_seen_count", current.get("followup_seen_count", 0)) or 0
            ),
            "followup_executed_aligned_count": int(
                payload.get(
                    "followup_executed_aligned_count",
                    current.get("followup_executed_aligned_count", 0),
                )
                or 0
            ),
            "followup_executed_reward": float(
                payload.get("followup_executed_reward", current.get("followup_executed_reward", 0.0)) or 0.0
            ),
            "followup_observed_count": int(
                payload.get("followup_observed_count", current.get("followup_observed_count", 0)) or 0
            ),
            "followup_observed_potential": float(
                payload.get("followup_observed_potential", current.get("followup_observed_potential", 0.0)) or 0.0
            ),
            "followup_overheld_count": int(
                payload.get("followup_overheld_count", current.get("followup_overheld_count", 0)) or 0
            ),
            "followup_overheld_potential": float(
                payload.get("followup_overheld_potential", current.get("followup_overheld_potential", 0.0)) or 0.0
            ),
            "followup_actions": str(payload.get("followup_actions", current.get("followup_actions", "")) or ""),
            "passive_only": 1,
        }
    )
    seeds[reflection_symbol] = current


def store_reflection_map(data: dict, reflection_map_symbol: str, payload: dict) -> None:
    reflection_map_symbol = str(reflection_map_symbol or "").strip()
    if not reflection_map_symbol:
        return
    maps = data.setdefault("reflection_maps", {})
    current = dict(maps.get(reflection_map_symbol, {}) or {})
    current.update(
        {
            "reflection_map_symbol": reflection_map_symbol,
            "reflection_symbol": str(payload.get("reflection_symbol", current.get("reflection_symbol", "")) or ""),
            "symbol_family": str(payload.get("symbol_family", current.get("symbol_family", "")) or ""),
            "reflection_state": str(payload.get("reflection_state", current.get("reflection_state", "")) or ""),
            "reflection_map_state": str(
                payload.get("reflection_map_state", current.get("reflection_map_state", "")) or ""
            ),
            "reflection_map_reason": str(
                payload.get("reflection_map_reason", current.get("reflection_map_reason", "")) or ""
            ),
            "dio_sentence": str(payload.get("dio_sentence", current.get("dio_sentence", "")) or ""),
            "seen_count": int(payload.get("seen_count", current.get("seen_count", 0)) or 0),
            "executed_count": int(payload.get("executed_count", current.get("executed_count", 0)) or 0),
            "observed_count": int(payload.get("observed_count", current.get("observed_count", 0)) or 0),
            "reward_sum": float(payload.get("reward_sum", current.get("reward_sum", 0.0)) or 0.0),
            "best_reward_sum": float(payload.get("best_reward_sum", current.get("best_reward_sum", 0.0)) or 0.0),
            "actions": str(payload.get("actions", current.get("actions", "")) or ""),
            "runs": str(payload.get("runs", current.get("runs", "")) or ""),
            "source_probe": str(payload.get("source_probe", current.get("source_probe", "")) or ""),
            "passive_only": 1,
        }
    )
    maps[reflection_map_symbol] = current


__all__ = [
    "compact_contact_lagen",
    "compact_neighbor_consequences",
    "compact_reflection_maps",
    "compact_reflection_seeds",
    "compact_sensor_relations",
    "compact_sentence_traces",
    "set_neighbor_consequence_summary",
    "set_relation_summary",
    "set_sensor_relation_summary",
    "store_contact_lage",
    "store_reflection_map",
    "store_reflection_seed",
    "store_sentence_trace",
]
