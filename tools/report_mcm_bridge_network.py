from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _bridge_tokens(summary_rows: list[dict[str, str]]) -> set[str]:
    return {row.get("token", "-") or "-" for row in summary_rows}


def _edge_kind(source: str, target: str, bridges: set[str]) -> str:
    if source in bridges and target in bridges:
        return "bruecke_zu_bruecke"
    if source in bridges and target not in bridges:
        return "bruecke_zu_aussen"
    if source not in bridges and target in bridges:
        return "aussen_zu_bruecke"
    return "aussen_zu_aussen"


def _phase(exit_rekopplung_delta: float, exit_strain_delta: float) -> str:
    if exit_rekopplung_delta > 0.0 and exit_strain_delta <= 0.0:
        return "rekoppelnder_austritt"
    if exit_rekopplung_delta < 0.0 and exit_strain_delta > 0.0:
        return "oeffnend_belastender_austritt"
    return "gemischter_austritt"


def _build_edges(summary_rows: list[dict[str, str]], detail_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    bridges = _bridge_tokens(summary_rows)
    edge_counts: Counter[tuple[str, str, str]] = Counter()
    edge_worlds: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    edge_durations: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    edge_exit_rek: dict[tuple[str, str, str], list[float]] = defaultdict(list)
    edge_exit_strain: dict[tuple[str, str, str], list[float]] = defaultdict(list)

    for row in detail_rows:
        token = row.get("token", "-") or "-"
        world = row.get("world", "-") or "-"
        duration = _float(row, "duration")
        exit_rekopplung = _float(row, "after_rekopplung") - _float(row, "end_rekopplung")
        exit_strain = _float(row, "after_strain") - _float(row, "end_strain")
        for relation, source, target in (
            ("eintritt", row.get("enter_from", "-") or "-", token),
            ("austritt", token, row.get("exit_to", "-") or "-"),
        ):
            if source == "-" or target == "-":
                continue
            key = (source, target, relation)
            edge_counts[key] += 1
            edge_worlds[key].add(world)
            edge_durations[key].append(duration)
            edge_exit_rek[key].append(exit_rekopplung)
            edge_exit_strain[key].append(exit_strain)

    rows: list[dict[str, object]] = []
    for (source, target, relation), count in edge_counts.items():
        rek_avg = sum(edge_exit_rek[(source, target, relation)]) / max(1, len(edge_exit_rek[(source, target, relation)]))
        strain_avg = sum(edge_exit_strain[(source, target, relation)]) / max(1, len(edge_exit_strain[(source, target, relation)]))
        duration_avg = sum(edge_durations[(source, target, relation)]) / max(1, len(edge_durations[(source, target, relation)]))
        rows.append(
            {
                "source": source,
                "target": target,
                "relation": relation,
                "edge_kind": _edge_kind(source, target, bridges),
                "count": count,
                "worlds": len(edge_worlds[(source, target, relation)]),
                "duration_avg": round(duration_avg, 6),
                "exit_rekopplung_delta_avg": round(rek_avg, 6),
                "exit_strain_delta_avg": round(strain_avg, 6),
                "exit_phase": _phase(rek_avg, strain_avg),
            }
        )

    rows.sort(key=lambda row: (-int(row["count"]), str(row["edge_kind"]), str(row["source"]), str(row["target"])))
    return rows


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _dominant_summary(summary_rows: list[dict[str, str]], bridges: set[str]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in summary_rows:
        token = row.get("token", "-") or "-"
        enter = row.get("dominant_enter", "-") or "-"
        exit_to = row.get("dominant_exit", "-") or "-"
        enter_internal = enter in bridges
        exit_internal = exit_to in bridges
        rows.append(
            {
                "token": token,
                "dominant_enter": enter,
                "dominant_enter_internal": int(enter_internal),
                "dominant_exit": exit_to,
                "dominant_exit_internal": int(exit_internal),
                "segments": _int(row, "segments"),
                "worlds": _int(row, "worlds"),
                "duration_avg": _float(row, "duration_avg"),
                "exit_phase": _phase(_float(row, "exit_rekopplung_delta"), _float(row, "exit_strain_delta")),
            }
        )
    rows.sort(key=lambda item: (-_int({k: str(v) for k, v in item.items()}, "segments"), str(item["token"])))
    return rows


def _reciprocal_pairs(nodes: list[dict[str, object]], edges: list[dict[str, object]], bridges: set[str]) -> list[tuple[str, str, int]]:
    edge_weight: Counter[tuple[str, str]] = Counter()
    for row in edges:
        if row["edge_kind"] != "bruecke_zu_bruecke":
            continue
        edge_weight[(str(row["source"]), str(row["target"]))] += int(row["count"])

    pairs: list[tuple[str, str, int]] = []
    seen: set[tuple[str, str]] = set()
    for a in bridges:
        for b in bridges:
            if a >= b:
                continue
            weight = edge_weight[(a, b)] + edge_weight[(b, a)]
            if weight <= 0:
                continue
            key = (a, b)
            if key in seen:
                continue
            seen.add(key)
            pairs.append((a, b, weight))
    pairs.sort(key=lambda item: (-item[2], item[0], item[1]))
    return pairs


def _write_markdown(summary_rows: list[dict[str, str]], edges: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    bridges = _bridge_tokens(summary_rows)
    node_rows = _dominant_summary(summary_rows, bridges)
    edge_counts = Counter(str(row["edge_kind"]) for row in edges)
    phase_counts = Counter(str(row["exit_phase"]) for row in edges)
    reciprocal = _reciprocal_pairs(node_rows, edges, bridges)
    internal_edges = [row for row in edges if row["edge_kind"] == "bruecke_zu_bruecke"]
    external_exit_edges = [row for row in edges if row["edge_kind"] == "bruecke_zu_aussen"]

    lines = [
        "# MCM-Bruecken Netzwerk",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die stabilen Bruecken nicht mehr als Einzelzeichen, sondern als Netzwerk aus Eintritts- und Austrittskanten.",
        "Knoten sind MCM-Episodentokens. Kanten sind beobachtete Eintritte in eine Bruecke oder Austritte aus einer Bruecke.",
        "",
        "## Netzwerkbestand",
        "",
        f"- Brueckenknoten: `{len(bridges)}`",
        f"- Kanten gesamt: `{len(edges)}`",
        f"- Interne Bruecke-zu-Bruecke-Kanten: `{edge_counts.get('bruecke_zu_bruecke', 0)}`",
        f"- Bruecke-zu-Aussen-Kanten: `{edge_counts.get('bruecke_zu_aussen', 0)}`",
        f"- Aussen-zu-Bruecke-Kanten: `{edge_counts.get('aussen_zu_bruecke', 0)}`",
        "",
        "## Austrittsphasen Der Kanten",
        "",
        "| Austrittsphase | Kanten |",
        "|---|---:|",
    ]
    for phase, count in sorted(phase_counts.items()):
        lines.append(f"| {phase} | {count} |")

    lines.extend(
        [
            "",
            "## Brueckenknoten",
            "",
            "| Token | Segmente | Welten | Dauer | Dominanter Eintritt | intern | Dominanter Austritt | intern | Austrittsphase |",
            "|---|---:|---:|---:|---|---:|---|---:|---|",
        ]
    )
    for row in node_rows:
        lines.append(
            f"| {row['token']} | {row['segments']} | {row['worlds']} | {float(row['duration_avg']):.2f} | "
            f"{row['dominant_enter']} | {row['dominant_enter_internal']} | {row['dominant_exit']} | {row['dominant_exit_internal']} | {row['exit_phase']} |"
        )

    lines.extend(["", "## Staerkste Interne Brueckenkanten", "", "| Quelle | Ziel | Relation | Anzahl | Welten | Austrittsphase |", "|---|---|---|---:|---:|---|"])
    for row in internal_edges[:20]:
        lines.append(
            f"| {row['source']} | {row['target']} | {row['relation']} | {row['count']} | {row['worlds']} | {row['exit_phase']} |"
        )

    lines.extend(["", "## Staerkste Externe Austritte", "", "| Quelle | Ziel | Anzahl | Welten | Austrittsphase |", "|---|---|---:|---:|---|"])
    for row in external_exit_edges[:20]:
        lines.append(f"| {row['source']} | {row['target']} | {row['count']} | {row['worlds']} | {row['exit_phase']} |")

    lines.extend(["", "## Gegenseitige Brueckenpaare", "", "| Bruecke A | Bruecke B | Kantengewicht |", "|---|---|---:|"])
    if reciprocal:
        for a, b, weight in reciprocal[:20]:
            lines.append(f"| {a} | {b} | {weight} |")
    else:
        lines.append("| - | - | 0 |")

    lines.extend(["", "## Befund", ""])
    if reciprocal:
        a, b, weight = reciprocal[0]
        lines.append(
            f"Das staerkste interne Brueckenpaar ist `{a}` <-> `{b}` mit Kantengewicht `{weight}`. Das spricht fuer eine echte Rueckbezugsstruktur im Brueckennetz."
        )
    if edge_counts.get("bruecke_zu_bruecke", 0) > 0:
        lines.append(
            "Es gibt interne Bruecke-zu-Bruecke-Kanten. Bruecken sind damit nicht nur Ausgaenge aus dem Feld, sondern koennen andere Bruecken aktivieren oder rahmen."
        )
    if edge_counts.get("bruecke_zu_aussen", 0) > edge_counts.get("bruecke_zu_bruecke", 0):
        lines.append(
            "Die meisten Austritte fuehren dennoch in Aussen- oder Nicht-Bruecken-Tokens. Das passt zur Uebergangslesart: Bruecken halten eine Innenphase und fuehren danach in andere Feldlagen."
        )

    lines.extend(
        [
            "",
            "## Bedeutung",
            "",
            "Die Netzwerklesung verschiebt die Brueckenhypothese weiter:",
            "",
            "```text",
            "Bruecke = gehaltene Innenphase + gerichtete Kanten + Rueckbezuege",
            "```",
            "",
            "Damit wird Bedeutung nicht nur als Insel oder Punkt lesbar, sondern als topologische Verbindung zwischen Feldzustaenden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte das staerkste Brueckenpaar gezielt gelesen werden: Welche Weltphasen erzeugen `0e7qvj1` und `18l3thm`, und warum halten sie sich gegenseitig so stabil?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--details", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    summary_rows = _load(Path(args.summary))
    detail_rows = _load(Path(args.details))
    edges = _build_edges(summary_rows, detail_rows)
    _write_csv(edges, Path(args.out_csv))
    _write_markdown(summary_rows, edges, Path(args.out_md))
    print(f"edges={len(edges)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
