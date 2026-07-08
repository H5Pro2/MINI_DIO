from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_dio.config import Config
from mini_dio.semantic_memory import SemanticMemory

SOURCE_CSV = ROOT / "docs/befunde/1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN.csv"
MEMORY_PATH = ROOT / Config.DIO_MINI_EPISODIC_MEMORY_PATH

PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read_rows() -> list[dict[str, str]]:
    with SOURCE_CSV.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _quality(row: dict[str, str]) -> float:
    return max(
        0.0,
        (_float(row.get("afterimage_delta_spaet_frueh")) * 0.42)
        + (_float(row.get("temporal_delta_spaet_frueh")) * 0.36)
        + (min(1.0, _float(row.get("phase_presence")) / 3.0) * 0.22)
        - (max(0.0, _float(row.get("strain_delta_spaet_frueh"))) * 0.10),
    )


def _state(row: dict[str, str]) -> str:
    reading = str(row.get("family_reading") or "")
    quality = _quality(row)
    if reading == "kernfamilie_mit_feldzeitverdichtung" and quality >= 0.28:
        return "feldrolle_reift_verdichtend"
    if reading == "kernfamilie_mit_feldzeitverdichtung":
        return "feldrolle_reift_leise"
    if reading.startswith("brueckenfamilie"):
        return "feldrolle_bruecke_wachsend"
    if reading.startswith("fruehe_familie"):
        return "feldrolle_nachhallrest"
    if reading.startswith("randnahe"):
        return "feldrolle_randspannung"
    return "feldrolle_anschlussfaehig"


def build_field_role_memory(rows: list[dict[str, str]]) -> dict:
    items = []
    for row in rows:
        items.append(
            {
                **PASSIVE_FLAGS,
                "asset": str(row.get("asset") or ""),
                "family": str(row.get("family") or ""),
                "field_role_state": _state(row),
                "source_reading": str(row.get("family_reading") or ""),
                "dominant_role": str(row.get("dominant_role") or ""),
                "phase_presence": int(_float(row.get("phase_presence"))),
                "total_count": int(_float(row.get("total_count"))),
                "share_frueh": round(_float(row.get("share_frueh")), 6),
                "share_mitte": round(_float(row.get("share_mitte")), 6),
                "share_spaet": round(_float(row.get("share_spaet")), 6),
                "afterimage_delta_spaet_frueh": round(_float(row.get("afterimage_delta_spaet_frueh")), 6),
                "temporal_delta_spaet_frueh": round(_float(row.get("temporal_delta_spaet_frueh")), 6),
                "strain_delta_spaet_frueh": round(_float(row.get("strain_delta_spaet_frueh")), 6),
                "field_role_quality": round(_quality(row), 6),
            }
        )

    items.sort(
        key=lambda item: (
            float(item["field_role_quality"]),
            int(item["phase_presence"]),
            int(item["total_count"]),
        ),
        reverse=True,
    )
    state_counts = Counter(str(item["field_role_state"]) for item in items)
    asset_counts = Counter(str(item["asset"]) for item in items)
    return {
        **PASSIVE_FLAGS,
        "kind": "passive_mcm_field_role_memory",
        "source": str(SOURCE_CSV.relative_to(ROOT)),
        "memory_state": "field_roles_from_phase_maturation",
        "description": (
            "Passive Feldrollen-Memory aus 17k-Phasenprofilen. "
            "Speichert Reifungsbewegung von Familien, nicht Handlung."
        ),
        "state_counts": dict(state_counts.most_common()),
        "asset_counts": dict(asset_counts.most_common()),
        "top_roles": items[:48],
    }


def main() -> int:
    rows = _read_rows()
    role_memory = build_field_role_memory(rows)
    memory = SemanticMemory(MEMORY_PATH)
    memory.load()
    memory.store_passive_mcm_field_role_memory(role_memory)
    memory.save()
    print(f"updated {MEMORY_PATH.relative_to(ROOT)}")
    print(f"top_roles={len(role_memory['top_roles'])}")
    print(f"states={role_memory['state_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
