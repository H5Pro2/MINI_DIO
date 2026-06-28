from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _anchor_class(
    *,
    token: str,
    core_tokens: set[str],
    total_weight: int,
    outside_bridge_edges: int,
    bridge_to_bridge_edges: int,
    max_world_span: int,
    bidirectional_neighbors: int,
) -> str:
    if token in core_tokens:
        return "brueckenkern"
    if total_weight >= 30 and outside_bridge_edges >= 2 and bidirectional_neighbors >= 1 and max_world_span >= 3:
        return "starker_anschlussanker"
    if total_weight >= 30 and outside_bridge_edges >= 2 and bidirectional_neighbors >= 1 and bridge_to_bridge_edges == 0:
        return "starker_anschlussanker"
    if total_weight >= 12 and outside_bridge_edges >= 1 and max_world_span >= 2:
        return "lokaler_anschlussanker"
    if bridge_to_bridge_edges > 0:
        return "schwacher_brueckenpfad"
    return "schwacher_anschluss"


def _token_profiles(
    network_rows: list[dict[str, str]],
    core_rows: list[dict[str, str]],
    paths: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    edges_by_token: dict[str, list[dict[str, str]]] = defaultdict(list)
    directed_neighbors: dict[str, dict[str, set[str]]] = defaultdict(lambda: {"in": set(), "out": set()})

    for row in network_rows:
        source = row.get("source", "")
        target = row.get("target", "")
        if source:
            edges_by_token[source].append(row)
            directed_neighbors[source]["out"].add(target)
        if target:
            edges_by_token[target].append(row)
            directed_neighbors[target]["in"].add(source)

    core_tokens: set[str] = set()
    core_pairs: set[tuple[str, str]] = set()
    for row in core_rows:
        token_a = row.get("token_a", "")
        token_b = row.get("token_b", "")
        if token_a:
            core_tokens.add(token_a)
        if token_b:
            core_tokens.add(token_b)
        if token_a and token_b:
            core_pairs.add(tuple(sorted((token_a, token_b))))

    rows: list[dict[str, str]] = []
    for token, token_edges in edges_by_token.items():
        total_weight = sum(_int(row.get("count", "0")) for row in token_edges)
        max_world_span = max((_int(row.get("worlds", "0")) for row in token_edges), default=0)
        weighted_duration = (
            sum(_float(row.get("duration_avg", "0")) * _int(row.get("count", "0")) for row in token_edges) / total_weight
            if total_weight
            else 0.0
        )
        edge_kinds = Counter(row.get("edge_kind", "-") for row in token_edges)
        phases = Counter(row.get("exit_phase", "-") for row in token_edges)
        relations = Counter(row.get("relation", "-") for row in token_edges)
        outside_bridge_edges = edge_kinds.get("aussen_zu_bruecke", 0) + edge_kinds.get("bruecke_zu_aussen", 0)
        bridge_to_bridge_edges = edge_kinds.get("bruecke_zu_bruecke", 0)
        neighbor_in = directed_neighbors[token]["in"]
        neighbor_out = directed_neighbors[token]["out"]
        bidirectional_neighbors = len(neighbor_in & neighbor_out)
        path = paths.get(token, {})
        anchor_class = _anchor_class(
            token=token,
            core_tokens=core_tokens,
            total_weight=total_weight,
            outside_bridge_edges=outside_bridge_edges,
            bridge_to_bridge_edges=bridge_to_bridge_edges,
            max_world_span=max_world_span,
            bidirectional_neighbors=bidirectional_neighbors,
        )
        rows.append(
            {
                "token": token,
                "short_token": _short(token),
                "anchor_class": anchor_class,
                "total_weight": str(total_weight),
                "max_world_span": str(max_world_span),
                "weighted_duration": f"{weighted_duration:.6f}",
                "edge_count": str(len(token_edges)),
                "outside_bridge_edges": str(outside_bridge_edges),
                "bridge_to_bridge_edges": str(bridge_to_bridge_edges),
                "bidirectional_neighbors": str(bidirectional_neighbors),
                "incoming_neighbors": str(len(neighbor_in)),
                "outgoing_neighbors": str(len(neighbor_out)),
                "path_class": path.get("path_class", "-"),
                "movement": path.get("movement", "-"),
                "base_zone": path.get("base_zone", "-"),
                "follow_zone": path.get("follow_zone", "-"),
                "base_role": path.get("base_role", "-"),
                "follow_role": path.get("follow_role", "-"),
                "dominant_edge_kind": edge_kinds.most_common(1)[0][0] if edge_kinds else "-",
                "edge_kind_profile": "; ".join(f"{k}:{v}" for k, v in edge_kinds.most_common()),
                "dominant_exit_phase": phases.most_common(1)[0][0] if phases else "-",
                "phase_profile": "; ".join(f"{k}:{v}" for k, v in phases.most_common()),
                "relation_profile": "; ".join(f"{k}:{v}" for k, v in relations.most_common()),
                "in_known_core_pair": "1" if token in core_tokens else "0",
                "known_core_pairs": str(sum(1 for pair in core_pairs if token in pair)),
            }
        )

    return sorted(
        rows,
        key=lambda row: (
            {
                "brueckenkern": 5,
                "starker_anschlussanker": 4,
                "lokaler_anschlussanker": 3,
                "schwacher_brueckenpfad": 2,
                "schwacher_anschluss": 1,
            }.get(row["anchor_class"], 0),
            _int(row["total_weight"]),
            _float(row["weighted_duration"]),
        ),
        reverse=True,
    )


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    class_counts = Counter(row["anchor_class"] for row in rows)
    strong = [row for row in rows if row["anchor_class"] == "starker_anschlussanker"]
    local = [row for row in rows if row["anchor_class"] == "lokaler_anschlussanker"]

    lines: list[str] = []
    lines.append("# MCM-Brueckenanker Landschaft")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese passive Diagnose prueft, ob `0b7nep9` als Anschlussanker singulaer ist oder ob das Feld mehrere vergleichbare Anschlussanker ausbildet.")
    lines.append("Sie nutzt vorhandene Bruecken-, Kern- und Pfadbefunde. Es wird keine neue Feldmechanik eingefuehrt.")
    lines.append("")
    lines.append("## Gesamtbefund")
    lines.append("")
    lines.append(f"- Untersuchte Bruecken-Tokens: `{len(rows)}`")
    lines.append(f"- Klassenprofil: `{'; '.join(f'{k}:{v}' for k, v in class_counts.most_common())}`")
    lines.append(f"- Starke Anschlussanker: `{len(strong)}`")
    lines.append(f"- Lokale Anschlussanker: `{len(local)}`")
    lines.append("")
    if strong:
        lines.append("## Starke Anschlussanker")
        lines.append("")
        lines.append("| Token | Gewicht | Welten | Dauer | Bidirektional | Pfadklasse | Bewegung | Kantenprofil |")
        lines.append("|---|---:|---:|---:|---:|---|---|---|")
        for row in strong:
            lines.append(
                f"| `{row['short_token']}` | {row['total_weight']} | {row['max_world_span']} | {float(row['weighted_duration']):.2f} | {row['bidirectional_neighbors']} | {row['path_class']} | {row['movement']} | {row['edge_kind_profile']} |"
            )
        lines.append("")
    lines.append("## Staerkste Brueckenrollen")
    lines.append("")
    lines.append("| Klasse | Token | Gewicht | Welten | Dauer | Rolle | Kantenprofil | Phasenprofil |")
    lines.append("|---|---|---:|---:|---:|---|---|---|")
    for row in rows[:16]:
        lines.append(
            f"| {row['anchor_class']} | `{row['short_token']}` | {row['total_weight']} | {row['max_world_span']} | {float(row['weighted_duration']):.2f} | {row['base_role']} -> {row['follow_role']} | {row['edge_kind_profile']} | {row['phase_profile']} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    strong_tokens = {row["short_token"] for row in strong}
    if len(strong) == 1 and "0b7nep9" in strong_tokens:
        lines.append("`0b7nep9` bleibt in dieser Pruefung als starker Anschlussanker singulaer.")
        lines.append("Das stuetzt die Lesung: Es gibt einen zentralen Brueckenkern und daneben eine ausgepraegte Anschlussphase, die Drift-/Seitenarmbereiche anbindet.")
    elif len(strong) > 1:
        lines.append("Das Feld bildet mehrere starke Anschlussanker.")
        lines.append("Damit waere die Anschlussanker-Rolle keine Singularitaet, sondern eine wiederkehrende Zwischenebene der Topologie.")
        if "0b7nep9" in strong_tokens:
            lines.append("`0b7nep9` bleibt dabei ein starker Anschlussanker, ist aber nicht die einzige Auspraegung dieser Rolle.")
    else:
        lines.append("Es wurde kein starker Anschlussanker gefunden.")
        lines.append("Dann waere die zuvor beobachtete Rolle entweder zu eng klassifiziert oder in der Gesamtlandschaft nicht stabil.")
    lines.append("")
    lines.append("Wichtig: Ein Anschlussanker ist nicht gleich Brueckenkern.")
    lines.append("Der Brueckenkern verbindet stabile zentrale Bedeutungsraeume. Ein Anschlussanker koppelt solche Raeume an offene Drift-, Rand- oder Seitenphasen.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte die staerkste Anschlussanker-Landschaft gegen weitere Weltgruppen geprueft werden, um zu sehen, ob die Rolle unter anderer Weltspannung stabil bleibt oder neue Anschlussanker entstehen.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--cores", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    paths = {row.get("token", ""): row for row in _read(args.paths)}
    rows = _token_profiles(_read(args.network), _read(args.cores), paths)
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
