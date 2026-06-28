"""Semantic memory facade for the mini DIO core.

The facade owns the JSON memory document and preserves the public API used by
the current runtime. Concrete memory layers live in dedicated store modules so
passive MCM meaning, episode, field and compatibility action memory stay
separated.
"""

from __future__ import annotations

import json
from pathlib import Path

from mini_dio.action_memory_store import (
    action_bias as action_bias_store,
    action_diagnostics as action_diagnostics_store,
    action_readiness as action_readiness_store,
    compact_record,
    episode_record_rank,
    family_record as family_record_store,
    learn as learn_store,
    learn_observation as learn_observation_store,
    symbol_record as symbol_record_store,
)
from mini_dio.dio_syntax import (
    make_reflection_map_symbol,
    make_reflection_seed_symbol,
    make_syntax_symbol,
    make_syntax_vector,
)
from mini_dio.episode_store import (
    compact_episode_memory as compact_episode_memory_store,
    store_episode_memory as store_episode_memory_trace,
    top_episode_memory,
)
from mini_dio.mcm_field_memory_store import (
    compact_mcm_field_episode_memory as compact_mcm_field_episode_memory_store,
    store_mcm_field_episode_memory as store_mcm_field_episode_memory_trace,
    top_mcm_field_episode_memory,
)
from mini_dio.perception_memory_store import (
    compact_temporal_families as compact_temporal_families_store,
    store_temporal_family as store_temporal_family_trace,
)
from mini_dio.passive_trace_store import (
    compact_contact_lagen as compact_contact_lagen_store,
    compact_neighbor_consequences as compact_neighbor_consequences_store,
    compact_reflection_maps as compact_reflection_maps_store,
    compact_reflection_seeds as compact_reflection_seeds_store,
    compact_sensor_relations as compact_sensor_relations_store,
    compact_sentence_traces as compact_sentence_traces_store,
    set_neighbor_consequence_summary as set_neighbor_consequence_summary_trace,
    set_relation_summary as set_relation_summary_trace,
    set_sensor_relation_summary as set_sensor_relation_summary_trace,
    store_contact_lage as store_contact_lage_trace,
    store_reflection_map as store_reflection_map_trace,
    store_reflection_seed as store_reflection_seed_trace,
    store_sentence_trace as store_sentence_trace_trace,
)
from mini_dio.semantic_meaning_store import (
    store_passive_inner_effect_meaning_notes as store_passive_inner_effect_meaning_notes_trace,
    store_passive_inner_effect_reflection_note as store_passive_inner_effect_reflection_note_trace,
    store_passive_inner_field_archetype_matrix as store_passive_inner_field_archetype_matrix_trace,
    store_passive_inner_field_archetypes as store_passive_inner_field_archetypes_trace,
    store_passive_inner_field_bridge_stable_contrast as store_passive_inner_field_bridge_stable_contrast_trace,
    store_passive_inner_field_map as store_passive_inner_field_map_trace,
    store_passive_inner_field_map_comparison as store_passive_inner_field_map_comparison_trace,
    store_passive_mcm_fragmentation_memory as store_passive_mcm_fragmentation_memory_trace,
    store_passive_mcm_role_maturation_memory as store_passive_mcm_role_maturation_memory_trace,
    store_passive_mcm_role_movement_memory as store_passive_mcm_role_movement_memory_trace,
    store_passive_mcm_role_network as store_passive_mcm_role_network_trace,
    store_passive_mcm_role_shift_memory as store_passive_mcm_role_shift_memory_trace,
)


class SemanticMemory:
    def __init__(self, path: str | Path, max_symbols: int = 2048):
        self.path = Path(path)
        self.max_symbols = int(max_symbols)
        self.data = {
            "version": 1,
            "runs": 0,
            "symbols": {},
            "families": {},
            "relations": {},
            "sensor_relations": {},
            "neighbor_consequences": {},
            "contact_lagen": {},
            "sentence_traces": {},
            "reflection_seeds": {},
            "reflection_maps": {},
            "temporal_families": {},
            "episode_memory": {},
            "mcm_field_episode_memory": {},
            "passive_inner_effect_reflection_notes": [],
            "passive_inner_effect_reflection_history": {},
            "passive_inner_effect_meaning_notes": [],
            "passive_inner_field_maps": [],
            "passive_inner_field_map_comparison": {},
            "passive_inner_field_bridge_stable_contrast": {},
            "passive_inner_field_archetypes": {},
            "passive_inner_field_archetype_matrix": {},
            "passive_mcm_fragmentation_memory": {},
            "passive_mcm_role_maturation_memory": {},
            "passive_mcm_role_movement_memory": {},
            "passive_mcm_role_network": {},
            "passive_mcm_role_shift_memory": {},
        }
        self.max_sensor_relations = 128
        self.max_neighbor_consequences = 128
        self.max_contact_lagen = 64
        self.max_sentence_traces = 128
        self.max_reflection_seeds = 64
        self.max_reflection_maps = 96
        self.max_temporal_families = 128
        self.max_episode_memory = 128
        self.max_mcm_field_episode_memory = 96

    def load(self) -> None:
        if not self.path.exists():
            return
        try:
            loaded = json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:
            return
        if isinstance(loaded, dict):
            self.data.update(loaded)
            self.data.setdefault("symbols", {})
            self.data.setdefault("families", {})
            self.data.setdefault("relations", {})
            self.data.setdefault("sensor_relations", {})
            self.data.setdefault("neighbor_consequences", {})
            self.data.setdefault("contact_lagen", {})
            self.data.setdefault("sentence_traces", {})
            self.data.setdefault("reflection_seeds", {})
            self.data.setdefault("reflection_maps", {})
            self.data.setdefault("temporal_families", {})
            self.data.setdefault("episode_memory", {})
            self.data.setdefault("mcm_field_episode_memory", {})
            self.data.setdefault("passive_inner_effect_reflection_notes", [])
            self.data.setdefault("passive_inner_effect_reflection_history", {})
            self.data.setdefault("passive_inner_effect_meaning_notes", [])
            self.data.setdefault("passive_inner_field_maps", [])
            self.data.setdefault("passive_inner_field_map_comparison", {})
            self.data.setdefault("passive_inner_field_bridge_stable_contrast", {})
            self.data.setdefault("passive_inner_field_archetypes", {})
            self.data.setdefault("passive_inner_field_archetype_matrix", {})
            self.data.setdefault("passive_mcm_fragmentation_memory", {})
            self.data.setdefault("passive_mcm_role_maturation_memory", {})
            self.data.setdefault("passive_mcm_role_movement_memory", {})
            self.data.setdefault("passive_mcm_role_network", {})
            self.data.setdefault("passive_mcm_role_shift_memory", {})
            self.compact_symbols()
            self.compact_families()

    def family_record(self, family: str) -> dict:
        return family_record_store(self.data, family)

    def set_relation_summary(self, support_pair: str, summary: dict) -> None:
        """Store passive relation memory.

        Relations are a reflection map only. They are intentionally not read by
        action_diagnostics, action_bias or action_readiness.
        """

        set_relation_summary_trace(self.data, support_pair, summary)

    def set_sensor_relation_summary(self, relation_key: str, summary: dict) -> None:
        """Store passive sensor-neighbor relation memory.

        Sensor relations are not read by action_diagnostics. They only preserve
        which DIO-owned families looked similar across sehen/hoeren/fuehlen.
        """

        set_sensor_relation_summary_trace(self.data, relation_key, summary, self.max_sensor_relations)

    def set_neighbor_consequence_summary(self, relation_key: str, summary: dict) -> None:
        """Store passive consequence-bound sensor-neighbor memory.

        Neighbor consequences are not read by action_diagnostics. They preserve
        whether a sensor-near relation is only observed, reifying, cautious, or
        still open.
        """

        set_neighbor_consequence_summary_trace(self.data, relation_key, summary, self.max_neighbor_consequences)

    def compact_neighbor_consequences(self, max_relations: int | None = None) -> dict:
        """Keep the passive neighbor-consequence map compact."""

        limit = int(max_relations if max_relations is not None else self.max_neighbor_consequences)
        return compact_neighbor_consequences_store(self.data, limit)

    def compact_sensor_relations(self, max_relations: int | None = None) -> dict:
        """Keep the passive sensor relation map compact."""

        limit = int(max_relations if max_relations is not None else self.max_sensor_relations)
        return compact_sensor_relations_store(self.data, limit)

    def compact_contact_lagen(self, max_relations: int | None = None) -> dict:
        """Keep the passive contact-lage map compact."""

        limit = int(max_relations if max_relations is not None else self.max_contact_lagen)
        return compact_contact_lagen_store(self.data, limit)

    def compact_sentence_traces(self, max_relations: int | None = None) -> dict:
        """Keep the passive sentence trace map compact."""

        limit = int(max_relations if max_relations is not None else self.max_sentence_traces)
        return compact_sentence_traces_store(self.data, limit)

    def compact_reflection_seeds(self, max_relations: int | None = None) -> dict:
        """Keep passive reflection seeds compact."""

        limit = int(max_relations if max_relations is not None else self.max_reflection_seeds)
        return compact_reflection_seeds_store(self.data, limit)

    def compact_episode_memory(self, max_items: int | None = None) -> dict:
        """Keep passive episode memory compact."""

        limit = int(max_items if max_items is not None else self.max_episode_memory)
        return compact_episode_memory_store(self.data, limit)

    def compact_mcm_field_episode_memory(self, max_items: int | None = None) -> dict:
        """Keep passive MCM field episode memory compact."""

        limit = int(max_items if max_items is not None else self.max_mcm_field_episode_memory)
        return compact_mcm_field_episode_memory_store(self.data, limit)

    def compact_reflection_maps(self, max_relations: int | None = None) -> dict:
        """Keep passive reflection-map snapshots compact."""

        limit = int(max_relations if max_relations is not None else self.max_reflection_maps)
        return compact_reflection_maps_store(self.data, limit)

    def compact_temporal_families(self, max_relations: int | None = None) -> dict:
        """Keep passive temporal family traces compact."""

        limit = int(max_relations if max_relations is not None else self.max_temporal_families)
        return compact_temporal_families_store(self.data, limit)

    def save(self) -> None:
        self.compact_symbols()
        self.compact_families()
        self.compact_sensor_relations()
        self.compact_neighbor_consequences()
        self.compact_contact_lagen()
        self.compact_sentence_traces()
        self.compact_reflection_seeds()
        self.compact_reflection_maps()
        self.compact_temporal_families()
        self.compact_episode_memory()
        self.compact_mcm_field_episode_memory()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        temp_path.write_text(json.dumps(self.data, indent=2, sort_keys=True), encoding="utf-8")
        temp_path.replace(self.path)

    def compact_symbols(self, max_symbols: int | None = None) -> dict:
        limit = int(max_symbols if max_symbols is not None else self.max_symbols)
        symbols = self.data.setdefault("symbols", {})
        if not isinstance(symbols, dict):
            self.data["symbols"] = {}
            return {"before": 0, "after": 0, "removed": 0}
        before = len(symbols)
        if before <= limit:
            return {"before": before, "after": before, "removed": 0}
        sorted_items = sorted(symbols.items(), key=lambda item: episode_record_rank(dict(item[1] or {})), reverse=True)
        kept = dict(sorted_items[:limit])
        self.data["symbols"] = kept
        return {"before": before, "after": len(kept), "removed": before - len(kept)}

    def compact_families(self, max_families: int | None = None) -> dict:
        limit = int(max_families if max_families is not None else self.max_symbols)
        families = self.data.setdefault("families", {})
        if not isinstance(families, dict):
            self.data["families"] = {}
            return {"before": 0, "after": 0, "removed": 0}
        before = len(families)
        if before <= limit:
            return {"before": before, "after": before, "removed": 0}
        sorted_items = sorted(families.items(), key=lambda item: episode_record_rank(dict(item[1] or {})), reverse=True)
        kept = dict(sorted_items[:limit])
        self.data["families"] = kept
        return {"before": before, "after": len(kept), "removed": before - len(kept)}

    def mark_run(self) -> None:
        self.data["runs"] = int(self.data.get("runs", 0) or 0) + 1

    def symbol_record(self, symbol: str) -> dict:
        return symbol_record_store(self.data, symbol)

    def action_diagnostics(self, symbol: str, action: str, vector: list[float] | None = None) -> dict:
        return action_diagnostics_store(self.data, symbol, action, vector=vector)

    def action_bias(self, symbol: str, action: str, vector: list[float] | None = None) -> float:
        return action_bias_store(self.data, symbol, action, vector=vector)

    def action_readiness(self, symbol: str, action: str, vector: list[float] | None = None) -> float:
        return action_readiness_store(self.data, symbol, action, vector=vector)

    def learn(
        self,
        symbol: str,
        action: str,
        reward: float,
        *,
        shadow: bool = False,
        vector: list[float] | None = None,
        timing_improvement: float = 0.0,
    ) -> None:
        learn_store(
            self.data,
            symbol,
            action,
            reward,
            shadow=shadow,
            vector=vector,
            timing_improvement=timing_improvement,
        )

    def learn_observation(
        self,
        symbol: str,
        action: str,
        reward: float,
        recognition: float,
        *,
        vector: list[float] | None = None,
    ) -> None:
        """Store recognized-but-unacted experience.

        This records observation and possible consequence without increasing
        direct action trust. It separates "I noticed this" from "I acted on
        this".
        """

        learn_observation_store(
            self.data,
            symbol,
            action,
            reward,
            recognition,
            vector=vector,
        )

    def store_contact_lage(self, contact_id: str, payload: dict) -> None:
        """Store passive contact-lage experience.

        This is not consumed by the motor loop. It only preserves whether a
        world contact behaved like exact recurrence, near similarity, or
        distant similarity.
        """

        store_contact_lage_trace(self.data, contact_id, payload)

    def store_sentence_trace(self, sentence_symbol: str, payload: dict) -> None:
        """Store a passive DIO sentence trace."""

        store_sentence_trace_trace(self.data, sentence_symbol, payload)

    def store_reflection_seed(self, reflection_symbol: str, payload: dict) -> None:
        """Store a passive reflection seed.

        Reflection seeds are not consumed by action_diagnostics or choose_action.
        They preserve that a family was observed, later executed, and optionally
        reconfirmed in a follow-up world.
        """

        store_reflection_seed_trace(self.data, reflection_symbol, payload)

    def store_reflection_map(self, reflection_map_symbol: str, payload: dict) -> None:
        """Store a passive reflection-map snapshot.

        Reflection maps are not consumed by action_diagnostics or choose_action.
        They preserve whether a known trace was quiet, reconfirmed, observed,
        conflicted, or unclear in a later world.
        """

        store_reflection_map_trace(self.data, reflection_map_symbol, payload)

    def store_temporal_family(self, family: str, temporal_state: dict) -> None:
        """Store passive time-depth for a DIO-owned family.

        This is not consumed by action_diagnostics. It preserves recurrence,
        time distance and afterimage so Mini-DIO can later be compared across
        controlled runs without mixing thought and reality.
        """

        store_temporal_family_trace(self.data, family, temporal_state, self.max_temporal_families)

    def store_episode_memory(self, payload: dict) -> str:
        """Store a passive episode-memory trace.

        Episode memory preserves state sequences such as carried -> strained ->
        carried. It is not read by action_diagnostics, choose_action, gates, or
        motoric code.
        """

        return store_episode_memory_trace(self.data, payload, self.max_episode_memory)

    def store_mcm_field_episode_memory(self, payload: dict) -> str:
        """Store passive MCM field-effect episode recurrence.

        This is the coarse field layer. It intentionally does not store the
        dominant family as identity, only as an example carrier.
        """

        return store_mcm_field_episode_memory_trace(self.data, payload, self.max_mcm_field_episode_memory)

    def compact_top(self, limit: int = 12) -> list[dict]:
        symbols = list(self.data.get("symbols", {}).values())
        symbols.sort(key=lambda item: int(item.get("count", 0) or 0), reverse=True)
        return [compact_record(item) for item in symbols[:limit]]

    def compact_top_families(self, limit: int = 12) -> list[dict]:
        families = list(self.data.get("families", {}).values())
        families.sort(key=lambda item: int(item.get("count", 0) or 0), reverse=True)
        return [compact_record(item) for item in families[:limit]]

    def compact_top_episode_memory(self, limit: int = 8) -> list[dict]:
        return top_episode_memory(self.data, limit)

    def compact_top_mcm_field_episode_memory(self, limit: int = 8) -> list[dict]:
        return top_mcm_field_episode_memory(self.data, limit)

    def store_passive_inner_effect_reflection_note(self, note: dict, max_notes: int = 64) -> None:
        """Store passive per-run inner effect reflection notes.

        These notes are not consumed by action_diagnostics or choose_action.
        """

        store_passive_inner_effect_reflection_note_trace(self.data, note, max_notes=max_notes)

    def store_passive_inner_effect_meaning_notes(self, meaning_notes: list[dict]) -> None:
        """Store passive inner-effect meaning notes.

        These notes explain stored inner effects. They are intentionally not
        consumed by action_diagnostics or choose_action.
        """

        store_passive_inner_effect_meaning_notes_trace(self.data, meaning_notes)

    def store_passive_inner_field_map(self, field_map: dict, max_maps: int = 32) -> None:
        """Store passive inner-field maps.

        These maps are diagnostics only. They are not consumed by action,
        entries, gates, direction, or motoric behavior.
        """

        store_passive_inner_field_map_trace(self.data, field_map, max_maps=max_maps)

    def store_passive_inner_field_map_comparison(self, comparison: dict) -> None:
        """Store passive inner-field map comparison diagnostics."""

        store_passive_inner_field_map_comparison_trace(self.data, comparison)

    def store_passive_inner_field_bridge_stable_contrast(self, contrast: dict) -> None:
        """Store passive contrast between carried-unrest and stable map groups."""

        store_passive_inner_field_bridge_stable_contrast_trace(self.data, contrast)

    def store_passive_inner_field_archetypes(self, archetypes: dict) -> None:
        """Store passive inner-field archetype ontology diagnostics."""

        store_passive_inner_field_archetypes_trace(self.data, archetypes)

    def store_passive_inner_field_archetype_matrix(self, matrix: dict) -> None:
        """Store passive matrix from world profiles to archetype readings."""

        store_passive_inner_field_archetype_matrix_trace(self.data, matrix)

    def store_passive_mcm_role_movement_memory(self, role_memory: dict) -> None:
        """Store passive MCM role-movement memory.

        This stores role movement, stability and drift quality. It is not
        consumed by action, entries, gates, direction, or motoric behavior.
        """

        store_passive_mcm_role_movement_memory_trace(self.data, role_memory)

    def store_passive_mcm_fragmentation_memory(self, fragmentation_memory: dict) -> None:
        """Store passive MCM fragmentation memory.

        This stores surface fragmentation quality. It is not consumed by action,
        entries, gates, direction, or motoric behavior.
        """

        store_passive_mcm_fragmentation_memory_trace(self.data, fragmentation_memory)

    def store_passive_mcm_role_maturation_memory(self, maturation_memory: dict) -> None:
        """Store passive MCM role-maturation memory.

        This stores maturation quality, segment quality and field quality. It is
        not consumed by action, entries, gates, direction, or motoric behavior.
        """

        store_passive_mcm_role_maturation_memory_trace(self.data, maturation_memory)

    def store_passive_mcm_role_shift_memory(self, shift_memory: dict) -> None:
        """Store passive MCM role-shift memory.

        This stores role changes across world orderings. It is not consumed by
        action, entries, gates, direction, or motoric behavior.
        """

        store_passive_mcm_role_shift_memory_trace(self.data, shift_memory)

    def store_passive_mcm_role_network(self, role_network: dict) -> None:
        """Store passive MCM role-network memory.

        This stores node roles, role movement, neighborhood, drift and
        recoupling as an inner field map. It is not consumed by action,
        entries, gates, direction, or motoric behavior.
        """

        store_passive_mcm_role_network_trace(self.data, role_network)
