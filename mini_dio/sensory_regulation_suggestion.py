from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _clean(value: object, fallback: str = "-") -> str:
    text = str(value or "").strip()
    return text or fallback


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _quality_support(quality: str) -> float:
    if quality == "reproduced_quiet_intake":
        return 1.0
    if quality == "recurrently_carried_intake":
        return 0.82
    if quality == "open_recurrent_intake":
        return 0.64
    if quality == "young_intake_trace":
        return 0.45
    if quality == "contact_loaded_intake":
        return 0.34
    if quality == "drifting_intake":
        return 0.26
    if quality == "strained_intake":
        return 0.18
    return 0.35


@dataclass(frozen=True)
class RegulationSuggestion:
    intake_key: str
    axis: str
    inner_effect_state: str
    mcm_preview_symbol: str
    intake_memory_quality: str
    total_events: int
    max_world_count: int
    recoupling_balance: float
    strain_quality: float
    carry_quality: float
    field_intake_pressure: float
    focus_pull: float
    distance_pull: float
    softening_pull: float
    sharpening_pull: float
    contact_relief_pull: float
    stable_listening_pull: float
    dominant_suggestion: str
    suggestion_family: str
    passive_note: str

    def to_row(self) -> dict[str, object]:
        return {
            "intake_key": self.intake_key,
            "axis": self.axis,
            "inner_effect_state": self.inner_effect_state,
            "mcm_preview_symbol": self.mcm_preview_symbol,
            "intake_memory_quality": self.intake_memory_quality,
            "total_events": self.total_events,
            "max_world_count": self.max_world_count,
            "recoupling_balance": round(self.recoupling_balance, 6),
            "strain_quality": round(self.strain_quality, 6),
            "carry_quality": round(self.carry_quality, 6),
            "field_intake_pressure": round(self.field_intake_pressure, 6),
            "focus_pull": round(self.focus_pull, 6),
            "distance_pull": round(self.distance_pull, 6),
            "softening_pull": round(self.softening_pull, 6),
            "sharpening_pull": round(self.sharpening_pull, 6),
            "contact_relief_pull": round(self.contact_relief_pull, 6),
            "stable_listening_pull": round(self.stable_listening_pull, 6),
            "dominant_suggestion": self.dominant_suggestion,
            "suggestion_family": self.suggestion_family,
            "passive_note": self.passive_note,
        }


def _dominant_suggestion(scores: dict[str, float]) -> str:
    if not scores:
        return "observe_only"
    return max(scores.items(), key=lambda item: (item[1], item[0]))[0]


def _suggestion_family(suggestion: str) -> str:
    if suggestion in {"stable_listening_pull", "sharpening_pull", "focus_pull"}:
        return "aufnahme_vertiefen"
    if suggestion in {"distance_pull", "softening_pull", "contact_relief_pull"}:
        return "aufnahme_entlasten"
    return "aufnahme_beobachten"


def build_suggestion(row: dict[str, str]) -> RegulationSuggestion:
    axis = _clean(row.get("axis"))
    quality = _clean(row.get("intake_memory_quality"))
    recoupling = _float(row.get("avg_recoupling_balance"))
    strain = _float(row.get("avg_strain_quality"))
    carry = _float(row.get("avg_carry_quality"))
    field_input = _float(row.get("avg_field_intake_pressure"))
    events = _int(row.get("total_events"))
    world_count = _int(row.get("max_world_count"))

    support = _quality_support(quality)
    event_weight = _clamp(events / 1000.0)
    recurrence_weight = _clamp(world_count / 4.0)
    load = _clamp((strain * 0.55) + (field_input * 0.65) + ((1.0 - recoupling) * 0.35))
    stability = _clamp((recoupling * 0.55) + (carry * 0.30) + (support * 0.15))
    axis_is_hearing = axis.startswith("hoeren")
    axis_is_visual = axis.startswith("sehen")
    axis_is_contact = axis in {"feldinput", "fuehlen_abstand"}

    focus_pull = _clamp(
        (stability * 0.34)
        + (event_weight * 0.12)
        + (recurrence_weight * 0.16)
        + (0.20 if axis_is_visual else 0.0)
        - (0.12 if axis_is_hearing else 0.0)
        - (0.08 if axis_is_contact else 0.0)
    )
    distance_pull = _clamp((load * 0.58) + (field_input * 0.20) + (0.22 if "abstand" in axis else 0.0))
    softening_pull = _clamp((load * 0.46) + (strain * 0.23) + (0.24 if axis == "hoeren_leise" else 0.0))
    sharpening_pull = _clamp(
        (stability * 0.40)
        + (0.28 if axis == "sehen_fokus" else 0.0)
        + (0.10 if axis_is_visual else 0.0)
        + (0.08 if quality in {"reproduced_quiet_intake", "recurrently_carried_intake"} else 0.0)
    )
    contact_relief_pull = _clamp((field_input * 0.55) + (strain * 0.25) + (0.20 if axis_is_contact else 0.0))
    stable_listening_pull = _clamp(
        (stability * 0.44)
        + (0.34 if axis == "hoeren_hin" else 0.0)
        + (0.14 if axis_is_hearing else 0.0)
        - (0.10 if axis_is_visual else 0.0)
        - (0.12 if axis_is_contact else 0.0)
    )

    scores = {
        "focus_pull": focus_pull,
        "distance_pull": distance_pull,
        "softening_pull": softening_pull,
        "sharpening_pull": sharpening_pull,
        "contact_relief_pull": contact_relief_pull,
        "stable_listening_pull": stable_listening_pull,
    }
    dominant = _dominant_suggestion(scores)
    return RegulationSuggestion(
        intake_key=_clean(row.get("intake_key")),
        axis=axis,
        inner_effect_state=_clean(row.get("inner_effect_state")),
        mcm_preview_symbol=_clean(row.get("mcm_preview_symbol")),
        intake_memory_quality=quality,
        total_events=events,
        max_world_count=world_count,
        recoupling_balance=recoupling,
        strain_quality=strain,
        carry_quality=carry,
        field_intake_pressure=field_input,
        focus_pull=focus_pull,
        distance_pull=distance_pull,
        softening_pull=softening_pull,
        sharpening_pull=sharpening_pull,
        contact_relief_pull=contact_relief_pull,
        stable_listening_pull=stable_listening_pull,
        dominant_suggestion=dominant,
        suggestion_family=_suggestion_family(dominant),
        passive_note="passive_suggestion_not_action",
    )


def read_intake_memory(path: Path) -> list[dict[str, str]]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def build_suggestions(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    suggestions = [build_suggestion(row).to_row() for row in rows if row.get("intake_key")]
    suggestions.sort(
        key=lambda row: (
            str(row["suggestion_family"]),
            str(row["dominant_suggestion"]),
            -int(row["total_events"]),
            str(row["intake_key"]),
        )
    )
    return suggestions


def suggestion_counts(rows: list[dict[str, object]]) -> tuple[Counter[str], Counter[str]]:
    return (
        Counter(str(row.get("dominant_suggestion") or "-") for row in rows),
        Counter(str(row.get("suggestion_family") or "-") for row in rows),
    )


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)
