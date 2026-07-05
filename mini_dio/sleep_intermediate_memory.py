"""Passive memory for sleep intermediate-role candidates.

This layer is diagnostic only. It records whether offline sleep combinations
remain origin-bound, partly reconnect in related worlds, or disappear.
It does not feed action, gates, direction, or motoric behavior.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


PASSIVE_INTERMEDIATE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
    "writes_runtime_memory": 0,
}


def _candidate_id(pair_key: str) -> str:
    digest = hashlib.sha1(str(pair_key or "").encode("utf-8")).hexdigest()[:10]
    return f"dio_sleep_mid_{digest}"


def _safe_float(value: object) -> float:
    try:
        result = float(value)
    except Exception:
        result = 0.0
    if result != result:
        return 0.0
    return result


def _safe_int(value: object) -> int:
    try:
        return int(float(value))
    except Exception:
        return 0


def build_sleep_intermediate_memory(analysis_summary: dict) -> dict:
    """Build a passive intermediate-role memory snapshot from analysis rows."""

    rows = list(analysis_summary.get("rows", []) or [])
    candidates = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        pair_key = str(row.get("pair_key", "") or "")
        if not pair_key:
            continue
        candidate_state = str(row.get("candidate_state", "") or "")
        if candidate_state not in {"quiet_intermediate_candidate", "broad_intermediate_candidate"}:
            continue
        candidate = {
            "candidate_id": _candidate_id(pair_key),
            "pair_key": pair_key,
            "roles": [part for part in pair_key.split("|") if part],
            "candidate_state": candidate_state,
            "same_state": str(row.get("same_state", "") or ""),
            "quiet_state": str(row.get("quiet_state", "") or ""),
            "stress_state": str(row.get("stress_state", "") or ""),
            "mosaic_state": str(row.get("mosaic_state", "") or ""),
            "same_delta": str(row.get("same_delta", "") or ""),
            "quiet_delta": str(row.get("quiet_delta", "") or ""),
            "stress_delta": str(row.get("stress_delta", "") or ""),
            "mosaic_delta": str(row.get("mosaic_delta", "") or ""),
            "avg_pair_sleep_resonance": round(_safe_float(row.get("avg_pair_sleep_resonance", 0.0)), 6),
            "co_touch_ratio": round(_safe_float(row.get("co_touch_ratio", 0.0)), 6),
            "combination_state": str(row.get("combination_state", "") or ""),
            **PASSIVE_INTERMEDIATE_FLAGS,
        }
        candidates.append(candidate)
    state_counts: dict[str, int] = {}
    for row in rows:
        if isinstance(row, dict):
            state = str(row.get("candidate_state", "") or "unknown")
            state_counts[state] = state_counts.get(state, 0) + 1
    if candidates:
        memory_state = "sleep_intermediate_candidates_present"
    elif rows:
        memory_state = "sleep_intermediate_candidates_absent"
    else:
        memory_state = "sleep_intermediate_unavailable"
    return {
        "version": 1,
        "kind": "passive_sleep_intermediate_candidate_memory",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "memory_state": memory_state,
        "candidate_count": len(candidates),
        "observed_combination_count": len(rows),
        "candidate_state_counts": dict(sorted(state_counts.items())),
        "labels": dict(analysis_summary.get("labels", {}) or {}),
        "candidates": candidates,
        "interpretation_boundary": (
            "Zwischenrollen-Kandidaten sind passive Messspuren aus Sleep-Kombinationen. "
            "Sie erzeugen keine Handlung, keine Richtung, kein Gate und keine Motorik."
        ),
        **PASSIVE_INTERMEDIATE_FLAGS,
    }


def update_sleep_intermediate_memory_file(memory_path: Path, analysis_summary: dict) -> dict:
    """Update a standalone passive intermediate candidate memory file."""

    memory_path = Path(memory_path)
    if memory_path.exists():
        try:
            memory = json.loads(memory_path.read_text(encoding="utf-8"))
        except Exception:
            memory = {}
    else:
        memory = {}
    snapshot = build_sleep_intermediate_memory(analysis_summary)
    existing = dict(memory.get("candidates", {}) or {})
    for candidate in snapshot.get("candidates", []) or []:
        candidate_id = str(candidate.get("candidate_id", "") or "")
        if not candidate_id:
            continue
        record = dict(existing.get(candidate_id, {}) or {})
        record.update(candidate)
        record["seen_count"] = _safe_int(record.get("seen_count", 0)) + 1
        record["last_seen_at"] = snapshot["created_at"]
        existing[candidate_id] = record
    history = list(memory.get("history", []) or [])
    history.append(
        {
            "created_at": snapshot["created_at"],
            "memory_state": snapshot["memory_state"],
            "candidate_count": snapshot["candidate_count"],
            "observed_combination_count": snapshot["observed_combination_count"],
            "candidate_state_counts": snapshot["candidate_state_counts"],
            "labels": snapshot["labels"],
            **PASSIVE_INTERMEDIATE_FLAGS,
        }
    )
    memory = {
        "version": 1,
        "kind": "passive_sleep_intermediate_candidate_store",
        "updated_at": snapshot["created_at"],
        "candidate_count": len(existing),
        "history": history[-32:],
        "candidates": dict(sorted(existing.items())),
        "latest_snapshot": snapshot,
        **PASSIVE_INTERMEDIATE_FLAGS,
    }
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = memory_path.with_suffix(memory_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(memory, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    temp_path.replace(memory_path)
    return memory


__all__ = [
    "build_sleep_intermediate_memory",
    "update_sleep_intermediate_memory_file",
]
