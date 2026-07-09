from __future__ import annotations

from collections import Counter


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _profile_counts(value: object) -> dict[str, int]:
    out: dict[str, int] = {}
    for part in str(value or "").split(";"):
        item = part.strip()
        if not item or ":" not in item:
            continue
        symbol, count = item.rsplit(":", 1)
        out[symbol.strip()] = _safe_int(count)
    return out


def _dominant_member(value: object) -> str:
    counts = _profile_counts(value)
    return max(counts, key=counts.get) if counts else "-"


def continuity_score(row: dict[str, object]) -> float:
    if not _safe_int(row.get("has_same_basis_follow_evidence")):
        return 0.0
    return (
        0.35 * _safe_float(row.get("same_basis_world_presence_ratio"))
        + 0.35 * _safe_float(row.get("same_basis_mean_member_coverage"))
        + 0.20 * _safe_float(row.get("same_basis_whole_family_ratio"))
        + 0.10 * _safe_float(row.get("same_basis_family_event_balance"))
    )


def _same_basis_follow_reading(row: dict[str, object]) -> str:
    events = _safe_int(row.get("same_basis_total_follow_events"))
    global_coverage = _safe_float(row.get("same_basis_global_member_coverage"))
    world_presence = _safe_float(row.get("same_basis_world_presence_ratio"))
    mean_coverage = _safe_float(row.get("same_basis_mean_member_coverage"))
    whole_ratio = _safe_float(row.get("same_basis_whole_family_ratio"))
    if events <= 0:
        return "familie_nicht_wiedergefunden"
    if global_coverage < 1.0:
        return "fragmentarischer_folgeweltanschluss"
    if world_presence >= 0.80 and mean_coverage >= 0.80 and whole_ratio >= 0.60:
        return "familienraum_konsistent_anschlussfaehig"
    if world_presence >= 0.70 and mean_coverage >= 0.60:
        return "familienraum_breit_anschlussfaehig"
    if world_presence >= 0.40:
        return "familienraum_offen_anschlussfaehig"
    return "familienraum_lokal_anschlussfaehig"


def _internal_role_reading(row: dict[str, object]) -> tuple[str, str, str]:
    source = _dominant_member(row.get("same_basis_source_member_event_profile"))
    follow = _dominant_member(row.get("same_basis_member_event_profile"))
    drift = _safe_float(row.get("member_distribution_drift"))
    shifted = source != "-" and follow != "-" and source != follow
    if shifted and drift >= 0.30:
        reading = "starker_innerer_dominanzwechsel"
    elif shifted and drift >= 0.15:
        reading = "offener_innerer_dominanzwechsel"
    elif shifted:
        reading = "leichter_dominanzwechsel_bei_naher_verteilung"
    elif drift >= 0.30:
        reading = "rollenverteilung_stark_verschoben"
    elif drift >= 0.15:
        reading = "rollenverteilung_verschoben"
    else:
        reading = "rollenverteilung_nahe_stabil"
    return reading, source, follow


def _legacy_reading(row: dict[str, object]) -> str:
    if not _safe_int(row.get("has_legacy_follow_evidence")):
        return "nicht_rueckgelesen"
    coverage = _safe_float(row.get("legacy_member_coverage"))
    if coverage >= 1.0:
        return "familie_als_ganzes_lesbar"
    if coverage > 0.0:
        return "familie_nur_fragmentarisch_lesbar"
    return "nicht_rueckgelesen"


def read_family(row: dict[str, object]) -> dict[str, object]:
    has_same_basis = bool(_safe_int(row.get("has_same_basis_follow_evidence")))
    legacy_reading = _legacy_reading(row)
    if has_same_basis:
        follow_reading = _same_basis_follow_reading(row)
        internal, source_dominant, follow_dominant = _internal_role_reading(row)
        if follow_reading == "familienraum_konsistent_anschlussfaehig":
            carry = "family_same_basis_consistent"
            connection = (
                "cohesive_same_basis_connection"
                if internal == "rollenverteilung_nahe_stabil"
                else "same_basis_connection_with_role_shift"
            )
        elif follow_reading == "familienraum_breit_anschlussfaehig":
            carry = "family_same_basis_distributed"
            connection = "distributed_same_basis_connection"
        elif follow_reading == "fragmentarischer_folgeweltanschluss":
            carry = "family_same_basis_fragmentary"
            connection = "partial_same_basis_connection"
        else:
            carry = "family_same_basis_open"
            connection = "open_same_basis_connection"

        if internal == "rollenverteilung_nahe_stabil":
            drift_reading = "stable_family_space"
        elif internal == "starker_innerer_dominanzwechsel":
            drift_reading = "internally_reorganizing_family_space"
        elif follow_reading == "familienraum_breit_anschlussfaehig":
            drift_reading = "distributed_role_shifting_family_space"
        elif follow_reading == "fragmentarischer_folgeweltanschluss":
            drift_reading = "fragmenting_family_space"
        else:
            drift_reading = "role_shifting_family_space"

        if drift_reading == "stable_family_space":
            note = "family remains coherent and internally stable across same-basis follow worlds"
        elif drift_reading == "internally_reorganizing_family_space":
            note = "family persists while its internal role dominance reorganizes"
        elif connection == "distributed_same_basis_connection":
            note = "complete family persists across the field but remains locally distributed"
        else:
            note = "same-basis family evidence remains open"
    else:
        follow_reading = legacy_reading
        internal = "nicht_gelesen"
        source_dominant = "-"
        follow_dominant = "-"
        concentration = _safe_float(row.get("cohesion_event_concentration"))
        if legacy_reading == "familie_als_ganzes_lesbar":
            carry = "family_legacy_followworld_confirmed"
            connection = "legacy_whole_family_connection"
            drift_reading = "legacy_drift_unread"
            note = "legacy backread sees the whole family; same-basis drift remains unread"
        elif legacy_reading == "familie_nur_fragmentarisch_lesbar":
            carry = "family_legacy_fragmentary"
            connection = "legacy_partial_family_connection"
            drift_reading = "legacy_fragmentary_drift_unread"
            note = "legacy backread remains partial; same-basis follow worlds are still needed"
        else:
            carry = "family_core_loaded" if concentration >= 0.65 else "family_broadly_carried"
            connection = "same_basis_followworld_missing"
            drift_reading = "drift_unread_without_followworld"
            note = "internally carried family still lacks same-basis followworld evidence"

    return {
        "legacy_follow_reading": legacy_reading,
        "follow_reading": follow_reading,
        "internal_role_reading": internal,
        "source_dominant_member": source_dominant,
        "follow_dominant_member": follow_dominant,
        "continuity_score": continuity_score(row),
        "carry_reading": carry,
        "connection_reading": connection,
        "drift_reading": drift_reading,
        "note": note,
    }


def reading_profile(rows: list[dict[str, object]]) -> dict[str, dict[str, int]]:
    readings = [read_family(row) for row in rows]
    return {
        "follow": dict(Counter(str(item["follow_reading"]) for item in readings).most_common()),
        "internal_role": dict(Counter(str(item["internal_role_reading"]) for item in readings).most_common()),
        "carry": dict(Counter(str(item["carry_reading"]) for item in readings).most_common()),
        "connection": dict(Counter(str(item["connection_reading"]) for item in readings).most_common()),
        "drift": dict(Counter(str(item["drift_reading"]) for item in readings).most_common()),
    }


__all__ = ["continuity_score", "read_family", "reading_profile"]
