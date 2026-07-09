from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1387_UNTERFORMEN_SEMANTISCHE_WIEDERKEHR.csv"
OUT_NODES = befunde_root(ROOT) / "1389_BEDEUTUNGSNETZ_KNOTEN.csv"
OUT_EDGES = befunde_root(ROOT) / "1389_BEDEUTUNGSNETZ_KANTEN.csv"
OUT_MD = befunde_root(ROOT) / "1389_BEDEUTUNGSNETZ_AUS_WIEDERKEHR.md"

PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _safe_float(row: dict[str, str], key: str) -> float:
    try:
        out = float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if out != out else out


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _symbol(prefix: str, *parts: object) -> str:
    raw = "|".join(str(part or "") for part in parts)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:8]
    return f"{prefix}_{digest}"


def _avg(values: list[float]) -> float:
    return mean(values) if values else 0.0


def _binding_quality(binding: str) -> str:
    if binding == "family_and_preview":
        return "stark_semantisch_gekoppelt"
    if binding in {"family", "preview"}:
        return "semantisch_gekoppelt"
    return "oberflaechennaehe"


def _edge_weight(row: dict[str, str]) -> float:
    binding = row.get("semantic_binding", "none")
    base = {
        "family_and_preview": 1.0,
        "family": 0.74,
        "preview": 0.68,
        "none": 0.32,
    }.get(binding, 0.32)
    carry_bonus = 0.12 if int(_safe_float(row, "preview_carry_next")) else 0.0
    rekopplung = _safe_float(row, "rekopplung_delta_next")
    strain = _safe_float(row, "strain_delta_next")
    rekopplung_bonus = max(-0.12, min(0.12, rekopplung * 2.0))
    strain_penalty = max(-0.12, min(0.12, strain * 2.0))
    return max(0.0, min(1.0, base + carry_bonus + rekopplung_bonus - strain_penalty))


def _node_state(avg_weight: float, observations: int, roles: int, worlds: int) -> str:
    if avg_weight >= 0.78 and observations >= 3 and worlds >= 2:
        return "verdichtete_bedeutungsnaehe"
    if avg_weight >= 0.60 and observations >= 2:
        return "tragende_bedeutungsnaehe"
    if roles >= 2 and observations >= 2:
        return "rollenuebergreifend_offen"
    if observations >= 2:
        return "wiederkehrende_oberflaeche"
    return "junge_spur"


def build_report() -> None:
    rows = _read_csv(INPUT)
    if not rows:
        raise RuntimeError("no recurrence rows")

    node_acc: dict[str, dict[str, object]] = {}
    edges: list[dict[str, object]] = []

    def node_for(row: dict[str, str]) -> str:
        signature = row.get("mischlinien_signature", "-")
        node = _symbol("dio_meaning_node", signature)
        if node not in node_acc:
            node_acc[node] = {
                "meaning_node": node,
                "signature": signature,
                "roles": Counter(),
                "worlds": Counter(),
                "families": Counter(),
                "previews": Counter(),
                "bindings": Counter(),
                "weights": [],
                "strain_delta_next": [],
                "rekopplung_delta_next": [],
            }
        acc = node_acc[node]
        acc["roles"].update([row.get("passive_role_near", "-")])  # type: ignore[index, union-attr]
        acc["worlds"].update([row.get("world", "-")])  # type: ignore[index, union-attr]
        acc["families"].update([row.get("family", "-")])  # type: ignore[index, union-attr]
        acc["previews"].update([row.get("preview", "-")])  # type: ignore[index, union-attr]
        acc["bindings"].update([row.get("semantic_binding", "none")])  # type: ignore[index, union-attr]
        weight = _edge_weight(row)
        acc["weights"].append(weight)  # type: ignore[index, union-attr]
        acc["strain_delta_next"].append(_safe_float(row, "strain_delta_next"))  # type: ignore[index, union-attr]
        acc["rekopplung_delta_next"].append(_safe_float(row, "rekopplung_delta_next"))  # type: ignore[index, union-attr]
        return node

    for row in rows:
        source = node_for(row)
        target = _symbol("dio_semantic_core", row.get("semantic_binding"), row.get("family"), row.get("preview"))
        binding = row.get("semantic_binding", "none")
        edge = {
            **PASSIVE_FLAGS,
            "meaning_edge": _symbol("dio_meaning_edge", source, target, row.get("passive_role_near"), binding),
            "source_node": source,
            "target_core": target,
            "edge_kind": f"{_binding_quality(binding)}",
            "semantic_binding": binding,
            "role": row.get("passive_role_near", "-"),
            "world": row.get("world", "-"),
            "family": row.get("family", "-"),
            "preview": row.get("preview", "-"),
            "reference_signature_count": row.get("reference_signature_count", "0"),
            "edge_weight": round(_edge_weight(row), 6),
            "strain_delta_next": round(_safe_float(row, "strain_delta_next"), 6),
            "rekopplung_delta_next": round(_safe_float(row, "rekopplung_delta_next"), 6),
        }
        edges.append(edge)

    node_rows: list[dict[str, object]] = []
    for node, acc in node_acc.items():
        roles: Counter[str] = acc["roles"]  # type: ignore[assignment]
        worlds: Counter[str] = acc["worlds"]  # type: ignore[assignment]
        families: Counter[str] = acc["families"]  # type: ignore[assignment]
        previews: Counter[str] = acc["previews"]  # type: ignore[assignment]
        bindings: Counter[str] = acc["bindings"]  # type: ignore[assignment]
        weights: list[float] = acc["weights"]  # type: ignore[assignment]
        strain_values: list[float] = acc["strain_delta_next"]  # type: ignore[assignment]
        rekopplung_values: list[float] = acc["rekopplung_delta_next"]  # type: ignore[assignment]
        observations = len(weights)
        avg_weight = _avg(weights)
        node_rows.append(
            {
                **PASSIVE_FLAGS,
                "meaning_node": node,
                "signature": acc["signature"],
                "node_state": _node_state(avg_weight, observations, len(roles), len(worlds)),
                "observations": observations,
                "world_count": len(worlds),
                "role_count": len(roles),
                "avg_edge_weight": round(avg_weight, 6),
                "avg_strain_delta_next": round(_avg(strain_values), 6),
                "avg_rekopplung_delta_next": round(_avg(rekopplung_values), 6),
                "binding_profile": " | ".join(f"{k}:{v}" for k, v in bindings.most_common()),
                "top_roles": " | ".join(f"{k}:{v}" for k, v in roles.most_common(5)),
                "top_worlds": " | ".join(f"{k}:{v}" for k, v in worlds.most_common(5)),
                "top_families": " | ".join(f"{k}:{v}" for k, v in families.most_common(5)),
                "top_previews": " | ".join(f"{k}:{v}" for k, v in previews.most_common(5)),
            }
        )

    state_priority = {
        "verdichtete_bedeutungsnaehe": 4,
        "tragende_bedeutungsnaehe": 3,
        "rollenuebergreifend_offen": 2,
        "wiederkehrende_oberflaeche": 1,
        "junge_spur": 0,
    }
    node_rows.sort(
        key=lambda item: (
            state_priority.get(str(item["node_state"]), 0),
            int(item["observations"]),
            int(item["world_count"]),
            float(item["avg_edge_weight"]),
        ),
        reverse=True,
    )
    edges.sort(key=lambda item: float(item["edge_weight"]), reverse=True)

    OUT_NODES.parent.mkdir(parents=True, exist_ok=True)
    with OUT_NODES.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(node_rows[0].keys()))
        writer.writeheader()
        writer.writerows(node_rows)
    with OUT_EDGES.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(edges[0].keys()))
        writer.writeheader()
        writer.writerows(edges)

    node_states = Counter(str(row["node_state"]) for row in node_rows)
    edge_kinds = Counter(str(row["edge_kind"]) for row in edges)
    sem_edges = [edge for edge in edges if edge["semantic_binding"] != "none"]
    surface_edges = [edge for edge in edges if edge["semantic_binding"] == "none"]
    sem_weight = _avg([float(edge["edge_weight"]) for edge in sem_edges])
    surface_weight = _avg([float(edge["edge_weight"]) for edge in surface_edges])
    sem_strain = _avg([float(edge["strain_delta_next"]) for edge in sem_edges])
    surface_strain = _avg([float(edge["strain_delta_next"]) for edge in surface_edges])
    sem_rekopplung = _avg([float(edge["rekopplung_delta_next"]) for edge in sem_edges])
    surface_rekopplung = _avg([float(edge["rekopplung_delta_next"]) for edge in surface_edges])

    top_node_lines = [
        (
            f"- `{row['meaning_node']}`: `{row['node_state']}`, "
            f"obs `{row['observations']}`, worlds `{row['world_count']}`, "
            f"weight `{row['avg_edge_weight']}`, bindings `{row['binding_profile']}`"
        )
        for row in node_rows[:10]
    ]

    lines = [
        "# 1389 - Passives MCM-Bedeutungsnetz aus Wiederkehr",
        "",
        "## Zweck",
        "",
        "Diese Diagnose baut aus `1387` ein erstes passives Bedeutungsnetz.",
        "",
        "Knoten sind wiederkehrende Unterform-/Feldspuren.",
        "Kanten sind Kopplungen zu Familien- oder Preview-Kernen.",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Befund",
        "",
        f"- Knoten: `{len(node_rows)}`",
        f"- Kanten: `{len(edges)}`",
        f"- semantisch gebundene Kanten: `{len(sem_edges)}`",
        f"- reine Oberflaechenkanten: `{len(surface_edges)}`",
        f"- Knotenzustaende: `{', '.join(f'{k}:{v}' for k, v in node_states.most_common())}`",
        f"- Kantenarten: `{', '.join(f'{k}:{v}' for k, v in edge_kinds.most_common())}`",
        "",
        "## Semantisch vs. Oberflaeche",
        "",
        f"- mittleres Gewicht semantischer Kanten: `{sem_weight:.6f}`",
        f"- mittleres Gewicht reiner Oberflaechenkanten: `{surface_weight:.6f}`",
        f"- Folge-Strain semantischer Kanten: `{sem_strain:.6f}`",
        f"- Folge-Strain reiner Oberflaechenkanten: `{surface_strain:.6f}`",
        f"- Folge-Rekopplung semantischer Kanten: `{sem_rekopplung:.6f}`",
        f"- Folge-Rekopplung reiner Oberflaechenkanten: `{surface_rekopplung:.6f}`",
        "",
        "## Staerkste Knoten",
        "",
        *top_node_lines,
        "",
        "## Lesung",
        "",
        "Das Bedeutungsnetz speichert keine externe Bedeutung.",
        "Es liest nur, welche Feldspuren wiederholt nahe beieinander liegen und ob diese Naehe semantisch gebunden ist.",
        "",
        "Wenn semantische Kanten hoeher gewichtet sind als reine Oberflaechenkanten, wird Feldbewusstsein technisch greifbarer:",
        "",
        "```text",
        "Das Feld traegt nicht nur Aehnlichkeit.",
        "Es traegt wiederkehrende innere Naehe.",
        "```",
        "",
        "## Grenze",
        "",
        "Diese Netzschicht ist eine passive Diagnose.",
        "Sie darf nicht als Motorik, Gate, Handlung oder Strategie gelesen werden.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
