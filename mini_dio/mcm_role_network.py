from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from mini_dio.dio_syntax import make_role_network_symbol


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


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


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = Path(path)
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _short_node(value: object) -> str:
    text = str(value or "").strip()
    if text.startswith("dio_mcm_episode_"):
        return text.replace("dio_mcm_episode_", "", 1)
    return text


def _dominant(counter: Counter[str], fallback: str = "-") -> str:
    if not counter:
        return fallback
    return str(counter.most_common(1)[0][0])


def _role_from_nonbridge(value: str) -> str:
    text = str(value or "")
    if "zentrum" in text:
        return "zentrum"
    if "rand" in text:
        return "rand"
    if "rekopplung" in text:
        return "rekopplung"
    if "offen" in text:
        return "offene_oberflaeche"
    if text and text != "-":
        return "nichtbruecke"
    return "-"


def _network_state(
    *,
    movement: str,
    shift: str,
    stability: str,
    drift: str,
    neighbors: int,
    avg_rekopplung: float,
    avg_strain: float,
) -> str:
    if "fragment" in shift or "drift" in drift:
        if avg_strain > avg_rekopplung:
            return "netz_fragmentiert_belastet"
        return "netz_driftend_getragen"
    if "core" in stability or "zentrum" in shift or "zentrum" in movement:
        if neighbors > 0:
            return "netz_zentrum_mit_anschluss"
        return "netz_zentrum_getragen"
    if "rekopplung" in shift or avg_rekopplung >= avg_strain:
        if neighbors > 0:
            return "netz_rekoppelnd_verbunden"
        return "netz_rekoppelnd_einzeln"
    if neighbors > 0:
        return "netz_offen_verbunden"
    return "netz_offen_einzeln"


def _network_note(state: str) -> str:
    notes = {
        "netz_fragmentiert_belastet": "Knoten bleibt sichtbar, wirkt aber belastet und fragmentiert.",
        "netz_driftend_getragen": "Knoten driftet, bleibt aber als getragene Feldspur lesbar.",
        "netz_zentrum_mit_anschluss": "Knoten wirkt zentrumsnah und besitzt Anschluss an Nachbarn.",
        "netz_zentrum_getragen": "Knoten wirkt zentrumsnah, aber ohne gelesenen Nachbaranschluss.",
        "netz_rekoppelnd_verbunden": "Knoten wirkt rekoppelnd und vernetzt.",
        "netz_rekoppelnd_einzeln": "Knoten wirkt rekoppelnd, aber aktuell eher einzeln.",
        "netz_offen_verbunden": "Knoten bleibt offen, aber mit Feldnachbarschaft.",
        "netz_offen_einzeln": "Knoten bleibt offen und einzeln.",
    }
    return notes.get(state, "Knoten bleibt als passive Feldinformation offen.")


@dataclass
class _NodeAccumulator:
    node: str
    roles: Counter[str] = field(default_factory=Counter)
    movement: Counter[str] = field(default_factory=Counter)
    shift: Counter[str] = field(default_factory=Counter)
    stability: Counter[str] = field(default_factory=Counter)
    drift: Counter[str] = field(default_factory=Counter)
    neighbors: Counter[str] = field(default_factory=Counter)
    edge_kinds: Counter[str] = field(default_factory=Counter)
    observations: int = 0
    worlds: int = 0
    rekopplung_sum: float = 0.0
    strain_sum: float = 0.0
    measure_count: int = 0

    def add_measure(self, *, rekopplung: float = 0.0, strain: float = 0.0) -> None:
        self.rekopplung_sum += float(rekopplung)
        self.strain_sum += float(strain)
        self.measure_count += 1


@dataclass
class RoleNetworkRecord:
    node: str
    network_symbol: str
    dominant_role: str
    dominant_movement_quality: str
    dominant_shift_quality: str
    dominant_stability_quality: str
    dominant_drift_quality: str
    network_state: str
    observations: int
    worlds: int
    neighbor_count: int
    top_neighbors: str
    top_edge_kinds: str
    avg_rekopplung: float
    avg_strain: float
    network_note: str

    @classmethod
    def from_accumulator(cls, acc: _NodeAccumulator) -> "RoleNetworkRecord":
        avg_rekopplung = acc.rekopplung_sum / max(1, acc.measure_count)
        avg_strain = acc.strain_sum / max(1, acc.measure_count)
        dominant_role = _dominant(acc.roles)
        movement = _dominant(acc.movement)
        shift = _dominant(acc.shift)
        stability = _dominant(acc.stability)
        drift = _dominant(acc.drift)
        state = _network_state(
            movement=movement,
            shift=shift,
            stability=stability,
            drift=drift,
            neighbors=len(acc.neighbors),
            avg_rekopplung=avg_rekopplung,
            avg_strain=avg_strain,
        )
        payload = {
            "node": acc.node,
            "dominant_role": dominant_role,
            "network_state": state,
            "dominant_movement_quality": movement,
            "dominant_shift_quality": shift,
            "dominant_stability_quality": stability,
            "dominant_drift_quality": drift,
            "observations": acc.observations,
            "worlds": acc.worlds,
            "neighbor_count": len(acc.neighbors),
            "avg_rekopplung": avg_rekopplung,
            "avg_strain": avg_strain,
        }
        return cls(
            node=acc.node,
            network_symbol=make_role_network_symbol(payload),
            dominant_role=dominant_role,
            dominant_movement_quality=movement,
            dominant_shift_quality=shift,
            dominant_stability_quality=stability,
            dominant_drift_quality=drift,
            network_state=state,
            observations=acc.observations,
            worlds=acc.worlds,
            neighbor_count=len(acc.neighbors),
            top_neighbors=" | ".join(f"{key}:{value}" for key, value in acc.neighbors.most_common(5)),
            top_edge_kinds=" | ".join(f"{key}:{value}" for key, value in acc.edge_kinds.most_common(5)),
            avg_rekopplung=avg_rekopplung,
            avg_strain=avg_strain,
            network_note=_network_note(state),
        )

    def to_row(self) -> dict[str, object]:
        return {
            **PASSIVE_FLAGS,
            "network_symbol": self.network_symbol,
            "node": self.node,
            "dominant_role": self.dominant_role,
            "dominant_movement_quality": self.dominant_movement_quality,
            "dominant_shift_quality": self.dominant_shift_quality,
            "dominant_stability_quality": self.dominant_stability_quality,
            "dominant_drift_quality": self.dominant_drift_quality,
            "network_state": self.network_state,
            "observations": self.observations,
            "worlds": self.worlds,
            "neighbor_count": self.neighbor_count,
            "top_neighbors": self.top_neighbors,
            "top_edge_kinds": self.top_edge_kinds,
            "avg_rekopplung": round(self.avg_rekopplung, 6),
            "avg_strain": round(self.avg_strain, 6),
            "network_note": self.network_note,
        }


class MCMRoleNetwork:
    def __init__(self, records: list[RoleNetworkRecord] | None = None) -> None:
        self.records = list(records or [])

    @classmethod
    def from_sources(
        cls,
        *,
        role_movement_csvs: list[Path] | None = None,
        role_shift_csvs: list[Path] | None = None,
        role_maturation_csvs: list[Path] | None = None,
        bridge_network_csvs: list[Path] | None = None,
    ) -> "MCMRoleNetwork":
        nodes: dict[str, _NodeAccumulator] = defaultdict(lambda: _NodeAccumulator(node=""))

        def node_for(token: str) -> _NodeAccumulator:
            short = _short_node(token)
            acc = nodes[short]
            if not acc.node:
                acc.node = short
            return acc

        for path in list(role_movement_csvs or []):
            for row in _load_csv(Path(path)):
                acc = node_for(row.get("short_token", ""))
                acc.roles.update([str(row.get("trend", "") or "role_open")])
                acc.movement.update([str(row.get("role_movement_quality", "") or "-")])
                acc.stability.update([str(row.get("stability_quality", "") or "-")])
                acc.drift.update([str(row.get("drift_quality", "") or "-")])
                acc.observations += max(1, _safe_int(row.get("weight_delta_total")))
                acc.worlds += _safe_int(row.get("max_rank"))

        for path in list(role_maturation_csvs or []):
            for row in _load_csv(Path(path)):
                acc = node_for(row.get("short_token", ""))
                acc.roles.update([str(row.get("follow_class", "") or "-")])
                acc.movement.update([str(row.get("maturation_quality", "") or "-")])
                acc.stability.update([str(row.get("segment_quality", "") or "-")])
                acc.drift.update([str(row.get("field_quality", "") or "-")])
                acc.observations += _safe_int(row.get("segments"))
                acc.worlds += _safe_int(row.get("worlds"))

        for path in list(role_shift_csvs or []):
            for row in _load_csv(Path(path)):
                acc = node_for(row.get("short_token", ""))
                acc.roles.update([_role_from_nonbridge(str(row.get("to_nonbridge_class", "") or ""))])
                acc.shift.update([str(row.get("shift_quality", "") or "-")])
                acc.stability.update([str(row.get("to_dominant_role", "") or "-")])
                acc.observations += _safe_int(row.get("observations"))
                acc.worlds += _safe_int(row.get("worlds"))
                acc.add_measure(
                    rekopplung=_safe_float(row.get("avg_rekopplung")),
                    strain=_safe_float(row.get("avg_strain")),
                )

        for path in list(bridge_network_csvs or []):
            for row in _load_csv(Path(path)):
                source = _short_node(row.get("source", ""))
                target = _short_node(row.get("target", ""))
                if not source or not target:
                    continue
                for left, right in [(source, target), (target, source)]:
                    acc = node_for(left)
                    acc.neighbors.update([right])
                    acc.edge_kinds.update([str(row.get("edge_kind", "") or "-")])
                    acc.observations += _safe_int(row.get("count"))
                    acc.worlds += _safe_int(row.get("worlds"))
                    acc.add_measure(
                        rekopplung=_safe_float(row.get("exit_rekopplung_delta_avg")),
                        strain=_safe_float(row.get("exit_strain_delta_avg")),
                    )

        records = [RoleNetworkRecord.from_accumulator(acc) for acc in nodes.values() if acc.node]
        records.sort(key=lambda item: (item.observations, item.neighbor_count), reverse=True)
        return cls(records)

    def to_rows(self) -> list[dict[str, object]]:
        return [record.to_row() for record in self.records]

    def quality_profile(self) -> dict[str, object]:
        return {
            "records": len(self.records),
            "network_state": dict(Counter(record.network_state for record in self.records).most_common()),
            "dominant_role": dict(Counter(record.dominant_role for record in self.records).most_common()),
            "dominant_movement_quality": dict(Counter(record.dominant_movement_quality for record in self.records).most_common()),
            **PASSIVE_FLAGS,
        }

    def write_csv(self, path: Path) -> None:
        rows = self.to_rows()
        path.parent.mkdir(parents=True, exist_ok=True)
        if not rows:
            path.write_text("", encoding="utf-8")
            return
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "profile": self.quality_profile(),
            "records": self.to_rows(),
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


__all__ = [
    "MCMRoleNetwork",
    "RoleNetworkRecord",
]
