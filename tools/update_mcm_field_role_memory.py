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
ATTACHMENT_SOURCES = [
    ROOT / "docs/befunde/1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv",
    ROOT / "docs/befunde/1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv",
]
FAMILY_ATTACHMENT_SOURCE = ROOT / "docs/befunde/1851_FAMILIEN_ANSCHLUSSQUALITAET.csv"
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


def _read_optional_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["source_report"] = str(path.relative_to(ROOT))
    return rows


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


def _attachment_quality(reading: str) -> str:
    if reading in {"realwelt_kernnaehe_staerker", "graduell_realnaeher_kern"}:
        return "kernnah"
    if reading == "graduell_kernnaehe_ohne_feldzeitvorsprung":
        return "kernnah_ohne_feldzeit"
    if reading == "graduell_realer_nachhall_ohne_kern":
        return "nachhallnah_ohne_kern"
    if reading in {"nullwelt_staerker", "graduell_nullnaeher"}:
        return "nullnah"
    if reading == "realwelt_anschluss_staerker":
        return "anschlussnah"
    return "offen_gemischt"


def _read_attachment_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in ATTACHMENT_SOURCES:
        rows.extend(_read_optional_rows(source))
    return rows


def build_attachment_quality_memory(rows: list[dict[str, str]]) -> dict:
    windows = [row for row in rows if row.get("row_type") == "window_summary"]
    items = []
    for row in windows:
        reading = str(row.get("reading") or "")
        quality = _attachment_quality(reading)
        items.append(
            {
                **PASSIVE_FLAGS,
                "source_report": str(row.get("source_report") or ""),
                "asset": str(row.get("asset") or ""),
                "window_start": int(_float(row.get("window_start"))),
                "attachment_quality": quality,
                "source_reading": reading,
                "source_edge": round(_float(row.get("source_edge")), 6),
                "kern_edge": round(_float(row.get("kern_edge")), 6),
                "afterimage_edge": round(_float(row.get("afterimage_edge")), 6),
                "temporal_edge": round(_float(row.get("temporal_edge")), 6),
                "field_edge_score": round(_float(row.get("field_edge_score")), 6),
            }
        )
    quality_counts = Counter(str(item["attachment_quality"]) for item in items)
    asset_counts = Counter(str(item["asset"]) for item in items)
    source_counts = Counter(str(item["source_report"]) for item in items)
    return {
        **PASSIVE_FLAGS,
        "kind": "passive_mcm_field_role_attachment_quality",
        "sources": [str(source.relative_to(ROOT)) for source in ATTACHMENT_SOURCES if source.exists()],
        "memory_state": "field_role_attachment_quality_from_multi_source_real_null_windows",
        "description": (
            "Passive Reifungsqualitaet aus mehreren Realwelt/Nullwelt-Zwischenlagen. "
            "Speichert Kernnaehe, Nachhallnaehe, Feldzeitnaehe, offene Mischung oder Nullnaehe."
        ),
        "quality_counts": dict(quality_counts.most_common()),
        "asset_counts": dict(asset_counts.most_common()),
        "source_counts": dict(source_counts.most_common()),
        "window_readings": items,
    }


def build_family_attachment_quality_memory(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {
            **PASSIVE_FLAGS,
            "kind": "passive_mcm_family_attachment_quality_memory",
            "source": str(FAMILY_ATTACHMENT_SOURCE.relative_to(ROOT)),
            "memory_state": "family_attachment_quality_not_available",
            "description": "Passive Familien-Anschlusskarte ist noch nicht erzeugt.",
            "state_counts": {},
            "quality_counts": {},
            "family_profiles": [],
            "asset_family_profiles": [],
        }

    family_rows = [row for row in rows if row.get("row_type") == "family_attachment_summary"]
    asset_family_rows = [row for row in rows if row.get("row_type") == "asset_family_attachment_summary"]
    state_counts = Counter(str(row.get("attachment_profile_state") or "-") for row in family_rows)
    quality_counts = Counter(str(row.get("dominant_attachment_quality") or "-") for row in family_rows)
    asset_quality_counts = Counter(
        f"{row.get('asset', '-')}::{row.get('dominant_attachment_quality', '-')}"
        for row in asset_family_rows
    )

    def family_profile(row: dict[str, str]) -> dict:
        return {
            **PASSIVE_FLAGS,
            "family": str(row.get("family") or ""),
            "appearances": int(_float(row.get("appearances"))),
            "asset_count": int(_float(row.get("asset_count"))),
            "window_count": int(_float(row.get("window_count"))),
            "attachment_profile_state": str(row.get("attachment_profile_state") or ""),
            "dominant_attachment_quality": str(row.get("dominant_attachment_quality") or ""),
            "attachment_profile": str(row.get("attachment_profile") or ""),
            "dominant_family_reading": str(row.get("dominant_family_reading") or ""),
            "family_reading_profile": str(row.get("family_reading_profile") or ""),
            "mean_afterimage_delta": round(_float(row.get("mean_afterimage_delta")), 6),
            "mean_temporal_delta": round(_float(row.get("mean_temporal_delta")), 6),
            "mean_field_edge_score": round(_float(row.get("mean_field_edge_score")), 6),
        }

    def asset_family_profile(row: dict[str, str]) -> dict:
        return {
            **PASSIVE_FLAGS,
            "asset": str(row.get("asset") or ""),
            "family": str(row.get("family") or ""),
            "appearances": int(_float(row.get("appearances"))),
            "attachment_profile_state": str(row.get("attachment_profile_state") or ""),
            "dominant_attachment_quality": str(row.get("dominant_attachment_quality") or ""),
            "attachment_profile": str(row.get("attachment_profile") or ""),
            "mean_field_edge_score": round(_float(row.get("mean_field_edge_score")), 6),
        }

    return {
        **PASSIVE_FLAGS,
        "kind": "passive_mcm_family_attachment_quality_memory",
        "source": str(FAMILY_ATTACHMENT_SOURCE.relative_to(ROOT)),
        "memory_state": "family_attachment_quality_from_real_world_windows",
        "description": (
            "Passive Familien-Anschlusskarte. Speichert, in welchem Weltkontext "
            "eine Familie eher kernnah, nachhallnah, offen, nullnah oder gemischt wiederkehrt."
        ),
        "state_counts": dict(state_counts.most_common()),
        "quality_counts": dict(quality_counts.most_common()),
        "asset_quality_counts": dict(asset_quality_counts.most_common()),
        "family_profiles": [family_profile(row) for row in family_rows[:48]],
        "asset_family_profiles": [asset_family_profile(row) for row in asset_family_rows[:96]],
    }


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
    attachment_memory = build_attachment_quality_memory(_read_attachment_rows())
    family_attachment_memory = build_family_attachment_quality_memory(_read_optional_rows(FAMILY_ATTACHMENT_SOURCE))
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
        "attachment_quality": attachment_memory,
        "family_attachment_quality": family_attachment_memory,
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
    print(f"attachment_quality={role_memory['attachment_quality']['quality_counts']}")
    print(f"family_attachment_quality={role_memory['family_attachment_quality']['state_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
