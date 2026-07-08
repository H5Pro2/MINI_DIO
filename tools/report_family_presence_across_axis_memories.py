from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
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


def _dominant_axes(vector: list[float]) -> str:
    ranked = sorted(
        ((VECTOR_KEYS[index], abs(value), value) for index, value in enumerate(vector)),
        key=lambda item: item[1],
        reverse=True,
    )
    return ";".join(f"{key}:{value:.4f}" for key, _, value in ranked[:4])


def _field_profile(data: dict) -> str:
    maps = list(data.get("passive_inner_field_maps", []) or [])
    counts: Counter[str] = Counter()
    total = 0
    for field_map in maps:
        for state, payload in dict(field_map.get("profile", {}) or {}).items():
            count = int(dict(payload or {}).get("count", 0) or 0)
            counts[state] += count
            total += count
    if not total:
        return "-"
    return ";".join(f"{state}:{count / total:.4f}" for state, count in counts.most_common())


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, family: str, rows: list[dict[str, object]]) -> None:
    active = [row for row in rows if int(row["present"]) == 1]
    total = len(rows)
    top = sorted(active, key=lambda row: int(row["count"]), reverse=True)[:30]
    source_counts = Counter(str(row["source_hint"]) for row in active)
    lines = [
        f"# 1792 - `{family}` über Achsen-Memories",
        "",
        "## Grundfrage",
        "",
        f"Die Prüfung liest, ob `{family}` nur in den rekoppelnden BTC/PAXG-Fenstern stark ist oder breiter in vorhandenen Achsen-Memories auftritt.",
        "",
        "Die Diagnose bleibt passiv und verändert keine Laufmechanik.",
        "",
        "## Kurzbefund",
        "",
        f"- geprüfte Memories: `{total}`",
        f"- aktive Memories mit `{family}`: `{len(active)}`",
        f"- Quellenprofil: `{'; '.join(f'{key}:{value}' for key, value in source_counts.most_common()) or '-'}`",
        "",
        "## Stärkste Vorkommen",
        "",
        "| Memory | Quelle | Count | Symbolcount | Dominante Achsen | Feldprofil |",
        "|---|---|---:|---:|---|---|",
    ]
    for row in top:
        lines.append(
            f"| `{row['memory']}` | {row['source_hint']} | {row['count']} | {row['symbol_count']} | "
            f"`{row['dominant_axes']}` | `{row['field_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            f"`{family}` ist dann fachlich interessant, wenn es nicht nur häufig erscheint, sondern in verschiedenen Weltmilieus eine ähnliche Achsenmischung hält.",
            "",
            "Wichtig bleibt:",
            "",
            "```text",
            "Familie allein ist kein Bedeutungsbeweis.",
            "Erst Wiederkehr + Achsenprofil + Feldprofil + Nachbarschaft machen sie lesbar.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            f"Als nächstes sollte `{family}` gegen seine Nachbarfamilien gelesen werden: Welche Familien treten in denselben Memories mit auf und bilden einen stabilen Bedeutungsraum?",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _source_hint(name: str) -> str:
    lower = name.lower()
    for key in ["btc", "paxg", "doge", "xrp", "kas", "sol", "synth", "stress", "expansion", "sideways"]:
        if key in lower:
            return key
    return "sonstige"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_104t")
    parser.add_argument("--memory-root", default="memory/multiworld_axis_map")
    parser.add_argument("--out-csv", default=None)
    parser.add_argument("--out-md", default=None)
    args = parser.parse_args()

    memory_root = ROOT / args.memory_root
    rows: list[dict[str, object]] = []
    for memory_file in sorted(memory_root.glob("*/memory_B_real_run_after_sleep.json")):
        data = _read(memory_file)
        families = dict(data.get("families", {}) or {})
        symbols = dict(data.get("symbols", {}) or {})
        record = dict(families.get(args.family, {}) or {})
        vector = _vector(record)
        symbol_count = sum(
            1 for payload in symbols.values()
            if dict(payload or {}).get("syntax_family") == args.family
        )
        rows.append(
            {
                "memory": memory_file.parent.name,
                "source_hint": _source_hint(memory_file.parent.name),
                "family": args.family,
                "present": 1 if record else 0,
                "count": int(record.get("count", 0) or 0),
                "symbol_count": symbol_count,
                "dominant_axes": _dominant_axes(vector) if record else "-",
                "field_profile": _field_profile(data),
                **{key: round(vector[index], 6) for index, key in enumerate(VECTOR_KEYS)},
            }
        )
    rows.sort(key=lambda row: (int(row["present"]), int(row["count"])), reverse=True)

    out_csv = ROOT / (args.out_csv or f"reports/{args.family}_axis_memory_presence.csv")
    out_md = ROOT / (args.out_md or f"docs/befunde/1792_{args.family.upper()}_ACHSEN_MEMORY_PRESENCE.md")
    _write_csv(out_csv, rows)
    _write_md(out_md, args.family, rows)
    print({"family": args.family, "rows": len(rows), "active": sum(int(row["present"]) for row in rows), "out": str(out_md.relative_to(ROOT))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
