from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def _load_json(path: Path) -> dict:
    if not path.exists() or path.stat().st_size <= 0:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _int(value: object) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def _counter_text(value: object, limit: int = 8) -> str:
    if not isinstance(value, dict) or not value:
        return "-"
    counter = Counter({str(key): _int(raw) for key, raw in value.items()})
    return ";".join(f"{key}:{count}" for key, count in counter.most_common(limit))


def _world_origin_counts(worlds: dict) -> tuple[int, int, int, int]:
    real_count = 0
    null_count = 0
    synthetic_count = 0
    unknown_count = 0
    for raw_name, raw_count in worlds.items():
        name = str(raw_name).upper()
        count = _int(raw_count)
        if "NULL" in name or "RANDSIGN" in name or "SHUFFLE" in name:
            null_count += count
        elif "SYNTHETIC" in name:
            synthetic_count += count
        elif name:
            real_count += count
        else:
            unknown_count += count
    return real_count, null_count, synthetic_count, unknown_count


def _origin_quality(real_share: float, null_share: float, synthetic_share: float, mixed_share: float) -> str:
    if null_share >= 0.70:
        return "feldinterne_nullordnung"
    if synthetic_share >= 0.70:
        return "synthetisch_getragen"
    if real_share >= 0.70:
        return "realwelt_getragen"
    if mixed_share >= 0.30 or (real_share >= 0.20 and null_share >= 0.20):
        return "gemischte_bindung"
    return "offene_herkunft"


def _row_for(symbol: str, item: dict) -> dict:
    worlds = item.get("worlds", {}) if isinstance(item.get("worlds"), dict) else {}
    world_bindings = item.get("world_bindings", {}) if isinstance(item.get("world_bindings"), dict) else {}
    avg_vector = item.get("avg_vector", {}) if isinstance(item.get("avg_vector"), dict) else {}

    real_count, null_count, synthetic_count, unknown_count = _world_origin_counts(worlds)
    total_origin_count = real_count + null_count + synthetic_count + unknown_count
    if total_origin_count <= 0:
        total_origin_count = max(1, _int(item.get("count")))

    mixed_count = _int(world_bindings.get("mixed_binding"))
    real_share = real_count / total_origin_count
    null_share = null_count / total_origin_count
    synthetic_share = synthetic_count / total_origin_count
    unknown_share = unknown_count / total_origin_count
    mixed_share = mixed_count / max(1, _int(item.get("count")))

    return {
        "preview_symbol": str(item.get("preview_symbol") or symbol),
        "count": _int(item.get("count")),
        "world_count": _int(item.get("world_count")),
        "phase_quality_state": str(item.get("phase_quality_state", "-")),
        "origin_quality": _origin_quality(real_share, null_share, synthetic_share, mixed_share),
        "dominant_world_binding": str(item.get("dominant_world_binding", "-")),
        "dominant_field_function": str(item.get("dominant_field_function", "-")),
        "dominant_field_variant": str(item.get("dominant_field_variant", "-")),
        "phase_quality_depth": _float(item.get("phase_quality_depth")),
        "positive_phase_affinity": _float(item.get("positive_phase_affinity")),
        "avg_phase_drift": _float(item.get("avg_phase_drift")),
        "max_phase_drift": _float(item.get("max_phase_drift")),
        "real_count": real_count,
        "null_count": null_count,
        "synthetic_count": synthetic_count,
        "unknown_count": unknown_count,
        "mixed_binding_count": mixed_count,
        "real_share": real_share,
        "null_share": null_share,
        "synthetic_share": synthetic_share,
        "unknown_share": unknown_share,
        "mixed_binding_share": mixed_share,
        "avg_carry": _float(avg_vector.get("carry")),
        "avg_strain": _float(avg_vector.get("strain")),
        "avg_rekopplung": _float(avg_vector.get("rekopplung")),
        "avg_sensory": _float(avg_vector.get("sensory")),
        "avg_visual_gap": _float(avg_vector.get("visual_gap")),
        "avg_hearing_gap": _float(avg_vector.get("hearing_gap")),
        "worlds": _counter_text(worlds),
        "world_bindings": _counter_text(world_bindings),
    }


def _write_markdown(path: Path, rows: list[dict], all_rows: list[dict], title: str) -> None:
    state_counts = Counter(row["phase_quality_state"] for row in all_rows)
    origin_counts = Counter(row["origin_quality"] for row in all_rows)
    binding_counts = Counter(row["dominant_world_binding"] for row in all_rows)
    function_counts = Counter(row["dominant_field_function"] for row in all_rows)

    lines = [
        f"# {title}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die passive Feldphasen-Signatur-Memory und trennt Herkunftsqualität von reiner Wiederkehr.",
        "",
        "Sie prüft nicht Handlung, Richtung oder Entry, sondern:",
        "",
        "- Realwelt-Anteil",
        "- Null-/Störwelt-Anteil",
        "- Mixed-Binding-Anteil",
        "- Feldfunktion",
        "- Reifetiefe",
        "- Drift",
        "",
        "## Übersicht",
        "",
        f"- Signaturen gesamt: `{len(all_rows)}`",
        "",
        "### Herkunftsqualität",
        "",
    ]
    for key, count in origin_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Phasenzustand", ""])
    for key, count in state_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Dominante Weltbindung", ""])
    for key, count in binding_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Feldfunktion", ""])
    for key, count in function_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "## Top-Herkunftssignaturen", ""])
    header = (
        "| Signatur | Herkunft | Zustand | Funktion | Tiefe | Drift | Real | Null | Mixed | Count/Welten |\n"
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|"
    )
    lines.append(header)
    for row in rows[:30]:
        lines.append(
            "| "
            f"`{row['preview_symbol']}` | "
            f"`{row['origin_quality']}` | "
            f"`{row['phase_quality_state']}` | "
            f"`{row['dominant_field_function']}` | "
            f"{row['phase_quality_depth']:.3f} | "
            f"{row['avg_phase_drift']:.3f} | "
            f"{row['real_share']:.3f} | "
            f"{row['null_share']:.3f} | "
            f"{row['mixed_binding_share']:.3f} | "
            f"{row['count']}/{row['world_count']} |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Eine stabile Feldphase ist erst dann fachlich stark, wenn ihre Herkunft mitgelesen wird.",
            "",
            "Eine Signatur kann tief und wiederkehrend sein, aber trotzdem anders zu lesen sein, wenn sie unter Null- oder Random-Sign-Welten stark mitgetragen wird.",
            "",
            "Damit wird die Feldmemory genauer: Sie speichert nicht nur, dass eine Phase wiederkehrt, sondern in welcher Herkunftsqualität sie wiederkehrt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte diese Herkunftsdiagnose auf weitere reale und gestörte Weltketten angewendet werden. Entscheidend ist, welche Signaturen realweltgetragen bleiben und welche zu feldinternen Ordnungen oder gemischten Bindungen werden.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--limit", type=int, default=120)
    args = parser.parse_args()

    data = _load_json(Path(args.memory))
    memory = data.get("passive_mcm_field_phase_signature_memory", {}) or {}
    if not isinstance(memory, dict):
        memory = {}

    all_rows = []
    for symbol, item in memory.items():
        if isinstance(item, dict):
            all_rows.append(_row_for(str(symbol), item))

    all_rows.sort(
        key=lambda row: (
            row["phase_quality_depth"],
            row["world_count"],
            row["count"],
        ),
        reverse=True,
    )
    rows = all_rows[: max(1, int(args.limit))]

    out_dir = Path("docs") / "befunde"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    fieldnames = list(rows[0].keys()) if rows else [
        "preview_symbol",
        "origin_quality",
        "phase_quality_state",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _write_markdown(out_md, rows, all_rows, f"{args.out_prefix} - Feldphasen-Herkunftsdiagnose")
    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
