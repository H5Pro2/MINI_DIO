from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;")
    except Exception:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _short_node(token: str) -> str:
    return token.replace("dio_mcm_episode_", "").strip()


def _hit_row(row: dict[str, str], node: str) -> bool:
    short = _short_node(node)
    joined = " ".join(str(value) for value in row.values())
    return node in joined or short in joined


def _top(counter: Counter[str], limit: int = 5) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _summarize_hits(node: str, files: list[Path]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    source_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    zone_counter: Counter[str] = Counter()
    effect_counter: Counter[str] = Counter()
    tone_counter: Counter[str] = Counter()
    coupling_counter: Counter[str] = Counter()
    world_counter: Counter[str] = Counter()
    rekopplung_values: list[float] = []
    strain_values: list[float] = []
    sensory_values: list[float] = []

    for path in files:
        if not path.exists():
            continue
        rows = _load_rows(path)
        for row in rows:
            if not _hit_row(row, node):
                continue
            hits.append(row)
            source_counter[path.name] += 1
            for key in ("dominant_role", "follow_role", "base_role", "role", "dominant_movement_quality"):
                value = row.get(key)
                if value:
                    role_counter[str(value)] += 1
            for key in ("condensation_zone", "follow_zone", "base_zone", "network_state", "nonbridge_class", "path_class"):
                value = row.get(key)
                if value:
                    zone_counter[str(value)] += 1
            for key in ("inner_effect_state", "dominant_inner_state"):
                value = row.get(key)
                if value:
                    effect_counter[str(value)] += 1
            value = row.get("dominant_tone_role")
            if value:
                tone_counter[str(value)] += 1
            value = row.get("coupling_role")
            if value:
                coupling_counter[str(value)] += 1
            for key in ("world", "world_names", "dominant_world", "source_world"):
                value = row.get(key)
                if value:
                    for part in str(value).replace('"', "").split(","):
                        part = part.strip()
                        if part:
                            world_counter[part] += 1
            for key in ("avg_rekopplung", "avg_mcm_rekopplung_quality"):
                if key in row:
                    rekopplung_values.append(_safe_float(row.get(key)))
            for key in ("avg_strain", "avg_mcm_strain_quality"):
                if key in row:
                    strain_values.append(_safe_float(row.get(key)))
            for key in ("avg_sensory", "avg_mcm_sensory_coupling"):
                if key in row:
                    sensory_values.append(_safe_float(row.get(key)))

    avg_rekopplung = sum(rekopplung_values) / max(1, len(rekopplung_values))
    avg_strain = sum(strain_values) / max(1, len(strain_values))
    avg_sensory = sum(sensory_values) / max(1, len(sensory_values))

    if hits and avg_rekopplung > avg_strain and ("zentrum_stabil" in role_counter or "stabile_bedeutungsinsel" in zone_counter):
        reading = "zentrum_getragen_mit_stabiler_rekopplung"
    elif hits and coupling_counter:
        reading = "zentrum_getragen_ueber_klang_und_sinneskopplung"
    elif hits and role_counter:
        reading = "zentrum_getragen_als_rollenspur"
    else:
        reading = "zentrum_getragen_noch_duenn_belegt"

    return {
        **PASSIVE_FLAGS,
        "node": node,
        "hit_count": len(hits),
        "source_profile": _top(source_counter),
        "role_profile": _top(role_counter),
        "zone_profile": _top(zone_counter),
        "effect_profile": _top(effect_counter),
        "tone_profile": _top(tone_counter),
        "coupling_profile": _top(coupling_counter),
        "world_profile": _top(world_counter),
        "avg_rekopplung": round(avg_rekopplung, 6),
        "avg_strain": round(avg_strain, 6),
        "avg_sensory": round(avg_sensory, 6),
        "reading": reading,
    }


def _target_nodes(network: Path, target_state: str) -> list[str]:
    rows = _load_rows(network)
    nodes = []
    for row in rows:
        if str(row.get("network_state", "") or "") == target_state:
            node = str(row.get("node", "") or "")
            if node:
                nodes.append(node)
    return nodes


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]], target_state: str) -> None:
    total_hits = sum(int(row.get("hit_count", 0) or 0) for row in rows)
    if total_hits > 0:
        finding_lines = [
            "Die gelesene Zentrumsqualitaet ist nicht einfach leer.",
            "Sie zeigt bei den gelesenen Knoten vorhandene Rueckbindung an stabile Zonen, Sinnesachsen oder Klangkopplung.",
        ]
        next_lines = [
            "Als naechstes sollte diese Zentrumsqualitaet gegen eine neue Weltgruppe wiederholt werden.",
            "Bleiben dieselben Knoten zentrumsnah, ist es Reproduktion; entstehen neue Knoten, ist es Feldwachstum.",
        ]
    else:
        finding_lines = [
            "Die gelesenen Zentrumsknoten erscheinen in diesen Folgebelegen nicht wieder.",
            "Damit ist diese Zentrumsqualitaet hier nicht reproduziert, sondern wirkt welt- oder situationsgebunden.",
        ]
        next_lines = [
            "Als naechstes sollte nicht derselbe Knoten gesucht werden, sondern die neu entstehende Zentrumsqualitaet der Folgewelten.",
            "Dann wird sichtbar, ob das Feld seine Mitte verlagert statt dieselbe Mitte zu kopieren.",
        ]

    lines = [
        "# MCM-Rolennetzwerk: Zentrumsqualitaet Ruecklesung",
        "",
        "## Zweck",
        "",
        f"Diese Datei legt `{target_state}` passiv auf vorhandene Zonen-, Sinnes- und Klangbefunde zurueck.",
        "Sie prueft, ob die spaete Zentrumsqualitaet nur aus fehlender Nachbarschaft entsteht oder durch reale Feldspuren getragen wird.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Knoten",
        "",
        "| Knoten | Treffer | Rekopplung | Strain | Sensorik | Rollen | Zonen | Effekte | Klang | Lesung |",
        "|---|---:|---:|---:|---:|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['node']}` | {row['hit_count']} | {row['avg_rekopplung']} | {row['avg_strain']} | {row['avg_sensory']} | "
            f"`{row['role_profile']}` | `{row['zone_profile']}` | `{row['effect_profile']}` | `{row['tone_profile']}` | `{row['reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            *finding_lines,
            "",
            "Wichtig ist die Grenze:",
            "",
            "```text",
            "Getragene Mitte ist hier noch keine Handlung.",
            "Sie ist eine passive Lesung: ein Knoten wirkt zentrumsnah und wird durch bestehende Feldspuren mitgetragen.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            *next_lines,
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--target-state", default="netz_zentrum_getragen")
    parser.add_argument("--evidence", action="append", type=Path, default=[])
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    nodes = _target_nodes(args.network, args.target_state)
    rows = [_summarize_hits(node, args.evidence) for node in nodes]
    if not rows:
        rows = [{**PASSIVE_FLAGS, "node": "-", "hit_count": 0, "source_profile": "-", "role_profile": "-", "zone_profile": "-", "effect_profile": "-", "tone_profile": "-", "coupling_profile": "-", "world_profile": "-", "avg_rekopplung": 0.0, "avg_strain": 0.0, "avg_sensory": 0.0, "reading": "keine_knoten"}]
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows, args.target_state)
    print(f"nodes={len(nodes)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
