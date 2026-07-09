from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def _load(path: Path) -> dict:
    if not path.exists() or path.stat().st_size <= 0:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _counter_text(value: object, limit: int = 5) -> str:
    if not isinstance(value, dict) or not value:
        return "-"
    counter = Counter({str(key): int(raw or 0) for key, raw in value.items()})
    return ";".join(f"{key}:{count}" for key, count in counter.most_common(limit))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    data = _load(Path(args.memory))
    memory = data.get("passive_mcm_field_phase_signature_memory", {}) or {}
    if not isinstance(memory, dict):
        memory = {}

    rows = []
    for symbol, item in memory.items():
        if not isinstance(item, dict):
            continue
        avg_vector = item.get("avg_vector", {}) if isinstance(item.get("avg_vector"), dict) else {}
        rows.append(
            {
                "preview_symbol": symbol,
                "count": int(item.get("count", 0) or 0),
                "world_count": int(item.get("world_count", 0) or 0),
                "phase_quality_state": item.get("phase_quality_state", "-"),
                "phase_quality_depth": _float(item.get("phase_quality_depth")),
                "positive_phase_affinity": _float(item.get("positive_phase_affinity")),
                "avg_phase_drift": _float(item.get("avg_phase_drift")),
                "max_phase_drift": _float(item.get("max_phase_drift")),
                "dominant_field_function": item.get("dominant_field_function", "-"),
                "dominant_field_variant": item.get("dominant_field_variant", "-"),
                "dominant_world_binding": item.get("dominant_world_binding", "-"),
                "worlds": _counter_text(item.get("worlds")),
                "field_functions": _counter_text(item.get("field_functions")),
                "field_variants": _counter_text(item.get("field_variants")),
                "world_bindings": _counter_text(item.get("world_bindings")),
                "avg_carry": _float(avg_vector.get("carry")),
                "avg_strain": _float(avg_vector.get("strain")),
                "avg_rekopplung": _float(avg_vector.get("rekopplung")),
                "avg_sensory": _float(avg_vector.get("sensory")),
                "avg_visual_gap": _float(avg_vector.get("visual_gap")),
                "avg_hearing_gap": _float(avg_vector.get("hearing_gap")),
                "avg_coherence": _float(avg_vector.get("coherence")),
                "avg_tension": _float(avg_vector.get("tension")),
                "avg_asymmetry": _float(avg_vector.get("asymmetry")),
            }
        )

    rows.sort(
        key=lambda row: (
            row["phase_quality_depth"],
            row["world_count"],
            row["count"],
        ),
        reverse=True,
    )
    rows = rows[: max(1, int(args.limit))]

    out_dir = Path("docs") / "befunde"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    if rows:
        with out_csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    else:
        out_csv.write_text("", encoding="utf-8")

    state_counts = Counter(str(item.get("phase_quality_state", "-")) for item in memory.values() if isinstance(item, dict))
    binding_counts = Counter(str(item.get("dominant_world_binding", "-")) for item in memory.values() if isinstance(item, dict))
    function_counts = Counter(str(item.get("dominant_field_function", "-")) for item in memory.values() if isinstance(item, dict))

    lines = [
        f"# {args.out_prefix} - Passive Feldphasen-Signatur-Memory",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die passive Feldphasen-Signatur-Memory.",
        "",
        "Sie prüft nicht Handlung, sondern wiederkehrende Feldqualität, Drift, Trägerrolle und Weltbindung.",
        "",
        "## Übersicht",
        "",
        f"- gespeicherte Feldphasen-Signaturen: `{len(memory)}`",
        "",
        "### Zustände",
        "",
    ]
    for key, count in state_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "### Weltbindung", ""])
    for key, count in binding_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "### Feldfunktionen", ""])
    for key, count in function_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "## Top-Signaturen", ""])
    for row in rows[:12]:
        lines.extend(
            [
                f"### `{row['preview_symbol']}`",
                "",
                f"- Zustand: `{row['phase_quality_state']}`",
                f"- Tiefe: `{row['phase_quality_depth']:.6f}`",
                f"- Count/Welten: `{row['count']}` / `{row['world_count']}`",
                f"- positive Affinität: `{row['positive_phase_affinity']:.6f}`",
                f"- Drift avg/max: `{row['avg_phase_drift']:.6f}` / `{row['max_phase_drift']:.6f}`",
                f"- Feldfunktion: `{row['dominant_field_function']}` / `{row['dominant_field_variant']}`",
                f"- Weltbindung: `{row['dominant_world_binding']}`",
                f"- Welten: {row['worlds']}",
                "",
            ]
        )

    lines.extend(
        [
        ]
    )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
