from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

VECTOR_KEYS = [
    "sehen_form_salience",
    "sehen_memory_recall",
    "hoeren_stimulation",
    "kontakt_druck",
    "feldaufnahme_druck",
    "mcm_kohaerenz",
    "mcm_spannung",
    "mcm_asymmetrie",
    "feldsignatur",
]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _vector(record: dict) -> list[float]:
    values = [_float(value) for value in list(record.get("vector", []) or [])[: len(VECTOR_KEYS)]]
    while len(values) < len(VECTOR_KEYS):
        values.append(0.0)
    return values


def _cosine(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm <= 0.0 or right_norm <= 0.0:
        return 0.0
    return dot / (left_norm * right_norm)


def _distance(left: list[float], right: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _source_hint(name: str) -> str:
    lower = name.lower()
    for key in ["btc", "paxg", "doge", "xrp", "kas", "sol", "synth", "stress", "expansion", "sideways"]:
        if key in lower:
            return key
    return "sonstige"


def _role_from_delta(delta_by_key: dict[str, float], avg_distance: float, avg_cosine: float) -> str:
    major_key, major_delta = max(delta_by_key.items(), key=lambda item: abs(item[1]))
    if avg_distance <= 0.10 and avg_cosine >= 0.99:
        return "zielnahe_mitrolle"
    if major_key == "mcm_kohaerenz":
        return "kohaerenz_hoeher" if major_delta > 0 else "kohaerenz_niedriger"
    if major_key == "hoeren_stimulation":
        return "hoeren_staerker" if major_delta > 0 else "hoeren_leiser"
    if major_key == "sehen_form_salience":
        return "sehen_schaerfer" if major_delta > 0 else "sehen_weicher"
    if major_key in {"feldaufnahme_druck", "mcm_spannung", "kontakt_druck"}:
        return "feldkontakt_drucknah" if major_delta > 0 else "feldkontakt_entlastet"
    if major_key == "mcm_asymmetrie":
        return "asymmetrie_plus" if major_delta > 0 else "asymmetrie_minus"
    if major_key == "sehen_memory_recall":
        return "erinnerung_naeher" if major_delta > 0 else "erinnerung_ferner"
    return "gemischte_variante"


def _fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, target_family: str, rows: list[dict[str, object]]) -> None:
    role_counts = Counter(str(row["role_reading"]) for row in rows)
    lines = [
        f"# 1795 - `{target_family}` Nachbarn: Rollen-Differenzierung",
        "",
        "## Grundfrage",
        "",
        f"Die Prüfung liest, ob die stärksten Nachbarn von `{target_family}` eigene Rollen tragen oder nur dieselbe Feldphase wiederholen.",
        "",
        "Verglichen wird jeweils nur dort, wo Zielknoten und Nachbar in derselben Achsen-Memory aktiv sind.",
        "",
        "## Kurzbefund",
        "",
        f"- gelesene Nachbarn: `{len(rows)}`",
        f"- Rollenprofil: `{'; '.join(f'{key}:{value}' for key, value in role_counts.most_common()) or '-'}`",
        "",
        "## Stärkste Nachbarn nach gemeinsamer Präsenz",
        "",
        "| Nachbar | Memories | Cosinus | Abstand | Rollenlesung | stärkste Abweichung | Quellenprofil |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    for row in rows[:40]:
        lines.append(
            f"| `{row['neighbor_family']}` | {row['co_memory_count']} | {_fmt(row['avg_cosine'])} | "
            f"{_fmt(row['avg_distance'])} | `{row['role_reading']}` | `{row['major_delta_axis']}:{_fmt(row['major_delta'])}` | "
            f"`{row['source_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"Die Nachbarschaft von `{target_family}` ist kein homogener Block.",
            "Ein Teil liegt sehr nah am Zielknoten, ein anderer Teil trägt klare Abweichungen über Kohärenz, Hören, Sehen, Asymmetrie oder Feldkontakt.",
            "",
            "Fachliche Lesung:",
            "",
            "```text",
            "Mitläufer = ähnliche Achsenlage im selben Bedeutungsraum.",
            "Eigenrolle = wiederkehrende Nachbarschaft mit stabiler Achsenabweichung.",
            "```",
            "",
            "Damit wirkt der Bedeutungsraum wie ein differenziertes Feldnetz, nicht wie eine einzige breite Sammelfamilie.",
            "",
            "## Wie es weitergeht",
            "",
            f"Als nächstes sollte eine Teilnetz-Prüfung die Rollen `{', '.join(key for key, _ in role_counts.most_common(4))}` getrennt lesen: Welche Rolle bindet Zentrum, Brücke, Rand oder Nachhall?",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_104t")
    parser.add_argument("--memory-root", default="memory/multiworld_axis_map")
    parser.add_argument("--limit", type=int, default=80)
    parser.add_argument("--out-csv", default=None)
    parser.add_argument("--out-md", default=None)
    args = parser.parse_args()

    memory_root = ROOT / args.memory_root
    rows_by_neighbor: dict[str, list[dict[str, object]]] = defaultdict(list)

    for memory_file in sorted(memory_root.glob("*/memory_B_real_run_after_sleep.json")):
        data = _read(memory_file)
        families = dict(data.get("families", {}) or {})
        target_record = dict(families.get(args.family, {}) or {})
        if not target_record:
            continue
        target_vector = _vector(target_record)
        source_hint = _source_hint(memory_file.parent.name)

        for family, payload in families.items():
            if family == args.family:
                continue
            record = dict(payload or {})
            count = int(record.get("count", 0) or 0)
            if count <= 0:
                continue
            vector = _vector(record)
            rows_by_neighbor[family].append(
                {
                    "source_hint": source_hint,
                    "count": count,
                    "target_vector": target_vector,
                    "neighbor_vector": vector,
                    "cosine": _cosine(target_vector, vector),
                    "distance": _distance(target_vector, vector),
                }
            )

    rows: list[dict[str, object]] = []
    for neighbor, items in rows_by_neighbor.items():
        co_memory_count = len(items)
        source_counts = Counter(str(item["source_hint"]) for item in items)
        target_avg = [
            _mean([list(item["target_vector"])[index] for item in items])
            for index in range(len(VECTOR_KEYS))
        ]
        neighbor_avg = [
            _mean([list(item["neighbor_vector"])[index] for item in items])
            for index in range(len(VECTOR_KEYS))
        ]
        delta_by_key = {
            key: neighbor_avg[index] - target_avg[index]
            for index, key in enumerate(VECTOR_KEYS)
        }
        major_axis, major_delta = max(delta_by_key.items(), key=lambda item: abs(item[1]))
        avg_cosine = _mean([float(item["cosine"]) for item in items])
        avg_distance = _mean([float(item["distance"]) for item in items])
        row = {
            "target_family": args.family,
            "neighbor_family": neighbor,
            "co_memory_count": co_memory_count,
            "neighbor_count_sum": sum(int(item["count"]) for item in items),
            "avg_cosine": round(avg_cosine, 6),
            "avg_distance": round(avg_distance, 6),
            "role_reading": _role_from_delta(delta_by_key, avg_distance, avg_cosine),
            "major_delta_axis": major_axis,
            "major_delta": round(major_delta, 6),
            "source_profile": ";".join(f"{key}:{value}" for key, value in source_counts.most_common()),
        }
        for index, key in enumerate(VECTOR_KEYS):
            row[f"target_avg_{key}"] = round(target_avg[index], 6)
            row[f"neighbor_avg_{key}"] = round(neighbor_avg[index], 6)
            row[f"delta_{key}"] = round(delta_by_key[key], 6)
        rows.append(row)

    rows.sort(
        key=lambda row: (
            int(row["co_memory_count"]),
            float(row["avg_distance"]),
            int(row["neighbor_count_sum"]),
        ),
        reverse=True,
    )
    if args.limit > 0:
        rows = rows[: args.limit]

    out_csv = ROOT / (args.out_csv or f"reports/{args.family}_neighbor_role_differentiation.csv")
    out_md = ROOT / (args.out_md or f"docs/befunde/1795_{args.family.upper()}_NACHBAR_ROLLEN_DIFFERENZIERUNG.md")
    _write_csv(out_csv, rows)
    _write_md(out_md, args.family, rows)
    print({"family": args.family, "neighbors": len(rows), "out": str(out_md.relative_to(ROOT))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
