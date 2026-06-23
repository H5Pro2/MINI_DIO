"""Passive semantic-meaning persistence helpers for MINI_DIO.

The functions here store explanatory inner-field meaning artifacts. They do not
feed action, entries, gates, direction, or motoric behavior.
"""

from __future__ import annotations


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _passive_item(payload: dict) -> dict:
    item = dict(payload)
    item.update(PASSIVE_FLAGS)
    return item


def store_passive_inner_effect_reflection_note(data: dict, note: dict, max_notes: int = 64) -> None:
    if not isinstance(note, dict):
        return
    notes = data.setdefault("passive_inner_effect_reflection_notes", [])
    if not isinstance(notes, list):
        notes = []
    notes.append(_passive_item(note))
    data["passive_inner_effect_reflection_notes"] = notes[-max(1, int(max_notes)) :]


def store_passive_inner_effect_meaning_notes(data: dict, meaning_notes: list[dict]) -> None:
    notes = []
    for note in list(meaning_notes or []):
        if not isinstance(note, dict):
            continue
        notes.append(_passive_item(note))
    data["passive_inner_effect_meaning_notes"] = notes


def store_passive_inner_field_map(data: dict, field_map: dict, max_maps: int = 32) -> None:
    if not isinstance(field_map, dict):
        return
    maps = data.setdefault("passive_inner_field_maps", [])
    if not isinstance(maps, list):
        maps = []
    maps.append(_passive_item(field_map))
    data["passive_inner_field_maps"] = maps[-max(1, int(max_maps)) :]


def store_passive_inner_field_map_comparison(data: dict, comparison: dict) -> None:
    if not isinstance(comparison, dict):
        return
    data["passive_inner_field_map_comparison"] = _passive_item(comparison)


def store_passive_inner_field_bridge_stable_contrast(data: dict, contrast: dict) -> None:
    if not isinstance(contrast, dict):
        return
    data["passive_inner_field_bridge_stable_contrast"] = _passive_item(contrast)


def store_passive_inner_field_archetypes(data: dict, archetypes: dict) -> None:
    if not isinstance(archetypes, dict):
        return
    data["passive_inner_field_archetypes"] = _passive_item(archetypes)


def store_passive_inner_field_archetype_matrix(data: dict, matrix: dict) -> None:
    if not isinstance(matrix, dict):
        return
    data["passive_inner_field_archetype_matrix"] = _passive_item(matrix)


__all__ = [
    "store_passive_inner_effect_meaning_notes",
    "store_passive_inner_effect_reflection_note",
    "store_passive_inner_field_archetype_matrix",
    "store_passive_inner_field_archetypes",
    "store_passive_inner_field_bridge_stable_contrast",
    "store_passive_inner_field_map",
    "store_passive_inner_field_map_comparison",
]
