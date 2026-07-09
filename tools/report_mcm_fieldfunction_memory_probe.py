from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KNOWN = [
    "dio_mcm_episode_0hiolzy",
    "dio_mcm_episode_1yxc2ug",
    "dio_mcm_episode_0hvxln3",
    "dio_mcm_episode_14sn1ov",
]


def _memory_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(item: dict, key: str) -> float:
    try:
        out = float(item.get(key, 0.0) or 0.0)
    except Exception:
        return 0.0
    return 0.0 if out != out else out


def _read_items(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    memory = data.get("passive_mcm_preview_anchor_depth_memory", {}) or {}
    return [dict(item or {}) for item in memory.values()]


def _top_counts(counter: Counter[str], limit: int = 8) -> str:
    return "; ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_report(memory_path: Path, out_prefix: str, known_symbols: list[str]) -> None:
    items = _read_items(memory_path)
    with_function = [item for item in items if item.get("field_function_class")]
    with_function.sort(
        key=lambda item: (
            _float(item, "depth_score"),
            int(item.get("world_count", 0) or 0),
            int(item.get("count", 0) or 0),
        ),
        reverse=True,
    )

    rows: list[dict] = []
    for item in with_function:
        rows.append(
            {
                "preview_symbol": item.get("preview_symbol", "-"),
                "field_function_class": item.get("field_function_class", "-"),
                "field_function_variant": item.get("field_function_variant", "-"),
                "field_function_confidence": item.get("field_function_confidence", 0.0),
                "depth_score": item.get("depth_score", 0.0),
                "depth_state": item.get("depth_state", "-"),
                "world_count": item.get("world_count", 0),
                "count": item.get("count", 0),
                "avg_afterimage": item.get("avg_afterimage", 0.0),
                "avg_recurrence": item.get("avg_recurrence", 0.0),
                "avg_rekopplung": item.get("avg_rekopplung", 0.0),
                "avg_strain": item.get("avg_strain", 0.0),
                "avg_sensory_coupling": item.get("avg_sensory_coupling", 0.0),
                "last_world": item.get("last_world", "-"),
                "world_binding_quality": item.get("world_binding_quality", "-"),
                "world_binding_confidence": item.get("world_binding_confidence", 0.0),
                "real_world_count": item.get("real_world_count", 0),
                "null_world_count": item.get("null_world_count", 0),
                "synthetic_world_count": item.get("synthetic_world_count", 0),
                "real_observation_share": item.get("real_observation_share", 0.0),
                "null_observation_share": item.get("null_observation_share", 0.0),
                "synthetic_observation_share": item.get("synthetic_observation_share", 0.0),
                "worlds": _top_counts(Counter(dict(item.get("worlds", {}) or {}))),
                "effects": _top_counts(Counter(dict(item.get("effects", {}) or {}))),
                "passive_only": item.get("passive_only", 1),
                "influences_action": item.get("influences_action", 0),
                "is_gate": item.get("is_gate", 0),
                "is_motoric": item.get("is_motoric", 0),
            }
        )

    out_csv = befunde_root(ROOT) / f"{out_prefix}.csv"
    out_md = befunde_root(ROOT) / f"{out_prefix}.md"
    _write_csv(out_csv, rows)

    class_counts = Counter(str(item.get("field_function_class", "-")) for item in with_function)
    variant_counts = Counter(str(item.get("field_function_variant", "-")) for item in with_function)
    binding_counts = Counter(str(item.get("world_binding_quality", "-")) for item in with_function)
    known_lines = []
    by_symbol = {str(item.get("preview_symbol", "")): item for item in with_function}
    for symbol in known_symbols:
        item = by_symbol.get(symbol, {})
        known_lines.append(
            {
                "symbol": symbol,
                "class": item.get("field_function_class", "-"),
                "variant": item.get("field_function_variant", "-"),
                "confidence": item.get("field_function_confidence", "-"),
                "depth": item.get("depth_score", "-"),
                "world_count": item.get("world_count", "-"),
                "count": item.get("count", "-"),
                "binding": item.get("world_binding_quality", "-"),
                "binding_confidence": item.get("world_binding_confidence", "-"),
                "last_world": item.get("last_world", "-"),
            }
        )

    lines = [
        f"# {out_prefix} - Passive Feldfunktions-Memory Mehrweltprüfung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.",
        "",
        "Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:",
        "",
        "- `milieu_island`",
        "- `active_recoupling`",
        "- `open_surface`",
        "- `undetermined`",
        "",
        "Die Lesung bleibt passiv.",
        "",
        "## Datengrundlage",
        "",
        f"- Memory: `{memory_path.relative_to(ROOT)}`",
        f"- Preview-Anker gesamt: `{len(items)}`",
        f"- Preview-Anker mit Feldfunktionslesung: `{len(with_function)}`",
        "",
        "## Klassen",
        "",
    ]
    for key, value in class_counts.most_common():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Varianten", ""])
    for key, value in variant_counts.most_common():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Weltbindung", ""])
    for key, value in binding_counts.most_common():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Bekannte Referenzrollen", ""])
    for row in known_lines:
        lines.append(
            f"- `{row['symbol']}`: `{row['class']}` / `{row['variant']}`, "
            f"Konfidenz `{row['confidence']}`, Depth `{row['depth']}`, "
            f"Bindung `{row['binding']}` (`{row['binding_confidence']}`), "
            f"Welten `{row['world_count']}`, Count `{row['count']}`, Last `{row['last_world']}`"
        )

    lines.extend(["", "## Top-Anker", ""])
    for row in rows[:12]:
        lines.append(
            f"- `{row['preview_symbol']}`: `{row['field_function_class']}` / "
            f"`{row['field_function_variant']}`, Depth `{row['depth_score']}`, "
            f"Bindung `{row['world_binding_quality']}`, "
            f"Welten `{row['world_count']}`, Count `{row['count']}`"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die neue Memory-Lesung erzeugt keine reine Symboltabelle.",
            "Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.",
            "",
            "Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.",
            "Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.",
            "",
        ]
    )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True)
    parser.add_argument("--out-prefix", required=True)
    parser.add_argument("--known-symbol", action="append", default=[])
    args = parser.parse_args()
    known = args.known_symbol or DEFAULT_KNOWN
    build_report(_memory_path(args.memory), args.out_prefix, known)


if __name__ == "__main__":
    main()
