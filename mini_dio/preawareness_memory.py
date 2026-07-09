"""Passive pre-awareness memory for recurring MCM field-contact roles.

This layer stores whether a field-contact role appears before later
re-coupling or opening phases across assets and lookback depths.

It is diagnostic only. It does not create action, direction, entries, gates or
motoric behavior.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


PASSIVE_PREAWARENESS_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
    "writes_runtime_memory": 0,
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        result = 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _clean(value: object, fallback: str = "-") -> str:
    text = str(value or "").strip()
    return text or fallback


def _clip01(value: object) -> float:
    return max(0.0, min(1.0, _safe_float(value)))


def _preawareness_id(key: str) -> str:
    digest = hashlib.sha1(str(key or "").encode("utf-8")).hexdigest()[:10]
    return f"dio_preaware_{digest}"


def _role_quality(field_share: float, rekopplung: float, strain: float, asset_count: int) -> str:
    stability = _clip01(field_share)
    carried = _clip01(rekopplung)
    strain = _clip01(strain)
    asset_breadth = min(1.0, max(0.0, asset_count / 3.0))
    score = (stability * 0.36) + (carried * 0.30) + ((1.0 - strain) * 0.20) + (asset_breadth * 0.14)
    if score >= 0.78:
        return "breit_getragene_vorwahrnehmung"
    if score >= 0.64:
        return "stabile_vorwahrnehmung"
    if score >= 0.50:
        return "offene_vorwahrnehmung"
    return "junge_oder_driftende_vorwahrnehmung"


def build_preawareness_memory(stability_rows: list[dict], detail_rows: list[dict] | None = None) -> dict:
    """Build a passive memory snapshot from field-contact stability rows."""

    detail_rows = list(detail_rows or [])
    items = []
    for row in list(stability_rows or []):
        if not isinstance(row, dict):
            continue
        lookback = _clean(row.get("lookback"))
        target_group = _clean(row.get("target_group"))
        chain = _clean(row.get("chain"))
        field_contact = _clean(row.get("dominant_field_contact_class"))
        sensory = _clean(row.get("dominant_sensory_class"))
        motion = _clean(row.get("dominant_motion_class"))
        assets = [part for part in _clean(row.get("assets"), "").split(";") if part]
        asset_count = _safe_int(row.get("asset_count") or len(assets))
        field_share = _clip01(row.get("field_asset_share"))
        sensory_share = _clip01(row.get("sensory_asset_share"))
        motion_share = _clip01(row.get("motion_asset_share"))
        carry = _clip01(row.get("avg_carry"))
        strain = _clip01(row.get("avg_strain"))
        rekopplung = _clip01(row.get("avg_rekopplung"))
        key = "|".join([lookback, target_group, chain, field_contact])
        item = {
            "preawareness_id": _preawareness_id(key),
            "preawareness_key": key,
            "lookback": lookback,
            "target_group": target_group,
            "chain": chain,
            "assets": assets,
            "asset_count": asset_count,
            "dominant_field_contact_class": field_contact,
            "dominant_sensory_class": sensory,
            "dominant_motion_class": motion,
            "field_asset_share": round(field_share, 6),
            "sensory_asset_share": round(sensory_share, 6),
            "motion_asset_share": round(motion_share, 6),
            "avg_carry": round(carry, 6),
            "avg_strain": round(strain, 6),
            "avg_rekopplung": round(rekopplung, 6),
            "preawareness_quality": _role_quality(field_share, rekopplung, strain, asset_count),
            "boundary": "passive_field_role_only_no_action_no_direction",
            **PASSIVE_PREAWARENESS_FLAGS,
        }
        items.append(item)

    quality_counts: dict[str, int] = {}
    field_counts: dict[str, int] = {}
    for item in items:
        quality = str(item.get("preawareness_quality", "-"))
        field = str(item.get("dominant_field_contact_class", "-"))
        quality_counts[quality] = quality_counts.get(quality, 0) + 1
        field_counts[field] = field_counts.get(field, 0) + 1

    return {
        "version": 1,
        "kind": "passive_preawareness_field_contact_memory",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "memory_state": "preawareness_field_roles_present" if items else "preawareness_field_roles_absent",
        "role_count": len(items),
        "detail_row_count": len(detail_rows),
        "quality_counts": dict(sorted(quality_counts.items())),
        "field_contact_counts": dict(sorted(field_counts.items())),
        "roles": sorted(items, key=lambda item: (str(item["target_group"]), str(item["chain"]), str(item["lookback"]))),
        "interpretation_boundary": (
            "Diese Vorwahrnehmungs-Memory speichert nur wiederkehrende MCM-Feldkontaktrollen. "
            "Sie ist keine Handlung, keine Richtung, kein Gate und keine Entry-Mechanik."
        ),
        **PASSIVE_PREAWARENESS_FLAGS,
    }


def update_preawareness_memory_file(
    memory_path: Path,
    stability_rows: list[dict],
    detail_rows: list[dict] | None = None,
) -> dict:
    """Update a standalone passive pre-awareness memory file."""

    memory_path = Path(memory_path)
    if memory_path.exists():
        try:
            memory = json.loads(memory_path.read_text(encoding="utf-8"))
        except Exception:
            memory = {}
    else:
        memory = {}

    snapshot = build_preawareness_memory(stability_rows, detail_rows)
    existing = dict(memory.get("roles", {}) or {})
    for role in snapshot.get("roles", []) or []:
        role_id = str(role.get("preawareness_id", "") or "")
        if not role_id:
            continue
        record = dict(existing.get(role_id, {}) or {})
        record.update(role)
        record["seen_count"] = _safe_int(record.get("seen_count", 0)) + 1
        record["last_seen_at"] = snapshot["created_at"]
        existing[role_id] = record

    history = list(memory.get("history", []) or [])
    history.append(
        {
            "created_at": snapshot["created_at"],
            "memory_state": snapshot["memory_state"],
            "role_count": snapshot["role_count"],
            "quality_counts": snapshot["quality_counts"],
            "field_contact_counts": snapshot["field_contact_counts"],
            **PASSIVE_PREAWARENESS_FLAGS,
        }
    )
    memory = {
        "version": 1,
        "kind": "passive_preawareness_field_contact_store",
        "updated_at": snapshot["created_at"],
        "role_count": len(existing),
        "history": history[-32:],
        "roles": dict(sorted(existing.items())),
        "latest_snapshot": snapshot,
        **PASSIVE_PREAWARENESS_FLAGS,
    }
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = memory_path.with_suffix(memory_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(memory, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    temp_path.replace(memory_path)
    return memory


__all__ = [
    "PASSIVE_PREAWARENESS_FLAGS",
    "build_preawareness_memory",
    "update_preawareness_memory_file",
]
