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


def _dominant_axes(vector: list[float]) -> str:
    ranked = sorted(
        ((VECTOR_KEYS[index], abs(value), value) for index, value in enumerate(vector)),
        key=lambda item: item[1],
        reverse=True,
    )
    return ";".join(f"{key}:{value:.4f}" for key, _, value in ranked[:4])


def _source_hint(name: str) -> str:
    lower = name.lower()
    for key in ["btc", "paxg", "doge", "xrp", "kas", "sol", "synth", "stress", "expansion", "sideways"]:
        if key in lower:
            return key
    return "sonstige"


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


def _write_md(path: Path, target_family: str, rows: list[dict[str, object]], target_memory_count: int) -> None:
    top = rows[:30]
    lines = [
        f"# 1794 - `{target_family}` Nachbarschaft über Achsen-Memories",
        "",
        "## Grundfrage",
        "",
        f"Die Prüfung liest, welche Familien gemeinsam mit `{target_family}` in denselben Achsen-Memories auftreten.",
        "",
        "Die Diagnose bleibt passiv. Sie verändert keine Laufmechanik und setzt keine neue Regel.",
        "",
        "## Kurzbefund",
        "",
        f"- aktive Memories mit `{target_family}`: `{target_memory_count}`",
        f"- gelesene Nachbarfamilien: `{len(rows)}`",
        "",
        "## Stärkste Nachbarn",
        "",
        "| Familie | gemeinsame Memories | Anteil | Count-Summe | Cosinus | Abstand | Quellenprofil | Dominante Achsen |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in top:
        lines.append(
            f"| `{row['neighbor_family']}` | {row['co_memory_count']} | {_fmt(row['co_memory_share'])} | "
            f"{row['neighbor_count_sum']} | {_fmt(row['avg_cosine'])} | {_fmt(row['avg_distance'])} | "
            f"`{row['source_profile']}` | `{row['dominant_axes']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"`{target_family}` wird damit nicht als einzelnes Wort gelesen, sondern als Knoten in einem Bedeutungsraum.",
            "Wichtig ist die Kombination aus gemeinsamer Wiederkehr, Achsenähnlichkeit, Quellenbreite und Abstand.",
            "",
            "Fachliche Lesung:",
            "",
            "```text",
            "Eine Familie wird tragfähiger, wenn sie nicht isoliert steht, sondern wiederkehrend mit ähnlichen Nachbarn koppelt.",
            "Bedeutung entsteht hier als Nachbarschaft im Feld, nicht als einzelner Name.",
            "```",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_104t")
    parser.add_argument("--memory-root", default="memory/multiworld_axis_map")
    parser.add_argument("--out-csv", default=None)
    parser.add_argument("--out-md", default=None)
    args = parser.parse_args()

    memory_root = ROOT / args.memory_root
    target_memory_count = 0
    neighbor_memory_counts: Counter[str] = Counter()
    neighbor_count_sums: Counter[str] = Counter()
    source_counts: dict[str, Counter[str]] = defaultdict(Counter)
    cosine_sums: Counter[str] = Counter()
    distance_sums: Counter[str] = Counter()
    vector_sums: dict[str, list[float]] = defaultdict(lambda: [0.0] * len(VECTOR_KEYS))

    for memory_file in sorted(memory_root.glob("*/memory_B_real_run_after_sleep.json")):
        data = _read(memory_file)
        families = dict(data.get("families", {}) or {})
        target_record = dict(families.get(args.family, {}) or {})
        if not target_record:
            continue
        target_memory_count += 1
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
            neighbor_memory_counts[family] += 1
            neighbor_count_sums[family] += count
            source_counts[family][source_hint] += 1
            cosine_sums[family] += _cosine(target_vector, vector)
            distance_sums[family] += _distance(target_vector, vector)
            for index, value in enumerate(vector):
                vector_sums[family][index] += value

    rows: list[dict[str, object]] = []
    for family, co_count in neighbor_memory_counts.items():
        avg_vector = [value / max(1, co_count) for value in vector_sums[family]]
        rows.append(
            {
                "target_family": args.family,
                "neighbor_family": family,
                "co_memory_count": co_count,
                "co_memory_share": round(co_count / max(1, target_memory_count), 6),
                "neighbor_count_sum": neighbor_count_sums[family],
                "avg_cosine": round(cosine_sums[family] / max(1, co_count), 6),
                "avg_distance": round(distance_sums[family] / max(1, co_count), 6),
                "source_profile": ";".join(f"{key}:{value}" for key, value in source_counts[family].most_common()),
                "dominant_axes": _dominant_axes(avg_vector),
                **{key: round(avg_vector[index], 6) for index, key in enumerate(VECTOR_KEYS)},
            }
        )
    rows.sort(
        key=lambda row: (
            int(row["co_memory_count"]),
            float(row["avg_cosine"]),
            int(row["neighbor_count_sum"]),
        ),
        reverse=True,
    )

    out_csv = ROOT / (args.out_csv or f"reports/{args.family}_axis_neighbor_space.csv")
    out_md = ROOT / (args.out_md or f"docs/befunde/1001-2000/1751-2000/1794_{args.family.upper()}_ACHSEN_NACHBARSCHAFT.md")
    _write_csv(out_csv, rows)
    _write_md(out_md, args.family, rows, target_memory_count)
    print(
        {
            "family": args.family,
            "target_memories": target_memory_count,
            "neighbors": len(rows),
            "out": str(out_md.relative_to(ROOT)),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
