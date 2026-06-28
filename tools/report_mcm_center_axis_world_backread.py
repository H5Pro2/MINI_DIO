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


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;")
    except Exception:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _short(value: object) -> str:
    return str(value or "").replace("dio_mcm_episode_", "")


def _top(counter: Counter[str], limit: int = 6) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _axis_tokens(axis: str) -> tuple[str, str]:
    parts = [part.strip() for part in axis.replace("<->", ",").split(",") if part.strip()]
    if len(parts) != 2:
        raise ValueError("--axis must contain exactly two tokens, e.g. 183drjy<->1t5bcxp")
    return _short(parts[0]), _short(parts[1])


def _event_hits(token_a: str, token_b: str, files: list[Path]) -> dict[str, object]:
    node_hits = 0
    pair_hits = 0
    worlds: Counter[str] = Counter()
    effects: Counter[str] = Counter()
    post_states: Counter[str] = Counter()
    classes: Counter[str] = Counter()
    sources: Counter[str] = Counter()
    pressure_delta: list[float] = []
    rek_delta: list[float] = []
    strain: list[float] = []
    rek: list[float] = []
    duration: list[int] = []

    for path in files:
        if not path.exists():
            continue
        for row in _load_rows(path):
            joined = " ".join(str(value) for value in row.values())
            has_a = token_a in joined
            has_b = token_b in joined
            if not has_a and not has_b:
                continue
            sources[path.name] += 1
            world = str(row.get("world") or row.get("source_world") or row.get("assets") or "-")
            worlds[world] += 1
            for key in ("dominant_effect", "dominant_movement_effect", "movement_effect_profile"):
                value = row.get(key)
                if value:
                    effects[str(value)] += 1
            for key in ("post_state",):
                value = row.get(key)
                if value:
                    post_states[str(value)] += 1
            for key in ("before_class", "switch_class", "after_class", "field_memory_quality"):
                value = row.get(key)
                if value:
                    classes[str(value)] += 1
            for key in ("pressure_delta", "avg_pressure_delta"):
                if key in row:
                    pressure_delta.append(_safe_float(row.get(key)))
            for key in ("rekopplung_delta", "avg_rekopplung_delta"):
                if key in row:
                    rek_delta.append(_safe_float(row.get(key)))
            for key in ("avg_strain", "avg_strain_delta"):
                if key in row:
                    strain.append(_safe_float(row.get(key)))
            for key in ("avg_rekopplung",):
                if key in row:
                    rek.append(_safe_float(row.get(key)))
            if "duration" in row:
                duration.append(_safe_int(row.get("duration")))
            if has_a and has_b:
                pair_hits += 1
            else:
                node_hits += 1

    total_hits = node_hits + pair_hits
    return {
        "event_hits": total_hits,
        "node_only_hits": node_hits,
        "pair_hits": pair_hits,
        "source_profile": _top(sources),
        "world_profile": _top(worlds),
        "effect_profile": _top(effects),
        "post_state_profile": _top(post_states),
        "class_profile": _top(classes),
        "avg_pressure_delta": round(sum(pressure_delta) / max(1, len(pressure_delta)), 6),
        "avg_rekopplung_delta": round(sum(rek_delta) / max(1, len(rek_delta)), 6),
        "avg_strain": round(sum(strain) / max(1, len(strain)), 6),
        "avg_rekopplung": round(sum(rek) / max(1, len(rek)), 6),
        "avg_duration": round(sum(duration) / max(1, len(duration)), 6),
    }


def _reading(row: dict[str, object]) -> str:
    pair_hits = _safe_int(row.get("pair_hits"))
    event_hits = _safe_int(row.get("event_hits"))
    avg_rek = _safe_float(row.get("avg_rekopplung"))
    avg_strain = _safe_float(row.get("avg_strain"))
    avg_rek_delta = _safe_float(row.get("avg_rekopplung_delta"))
    if pair_hits > 0 and avg_rek > avg_strain:
        return "achse_weltlich_getragen"
    if pair_hits > 0 and avg_rek_delta > 0:
        return "achse_rekoppelt_im_uebergang"
    if event_hits > 0:
        return "achse_episodisch_getragen"
    return "achse_ohne_rohweltbeleg"


def build_row(axis: str, event_files: list[Path]) -> dict[str, object]:
    token_a, token_b = _axis_tokens(axis)
    row = {
        **PASSIVE_FLAGS,
        "axis_a": token_a,
        "axis_b": token_b,
    }
    row.update(_event_hits(token_a, token_b, event_files))
    row["axis_world_reading"] = _reading(row)
    return row


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Zentrumsachse: Rohwelt-Ruecklesung",
        "",
        "## Zweck",
        "",
        "Diese Datei legt eine reziproke Zentrumsachse passiv auf Rohwelt-, Rezeptor- und Uebergangsereignisse zurueck.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Achsen",
        "",
        "| Achse | Events | Paar-Events | Quellen | Welten | Effekte | Klassen | Rekopplung | Strain | Lesung |",
        "|---|---:|---:|---|---|---|---|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['axis_a']} <-> {row['axis_b']}` | {row['event_hits']} | {row['pair_hits']} | `{row['source_profile']}` | "
            f"`{row['world_profile']}` | `{row['effect_profile']}` | `{row['class_profile']}` | "
            f"{row['avg_rekopplung']} | {row['avg_strain']} | `{row['axis_world_reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Eine Achse ist staerker, wenn sie nicht nur als `dio_net_*`-Paar erscheint,",
            "sondern auch in Rezeptorereignissen, Rohwelt-Uebergaengen oder Feldbewegungs-Memory wieder auftaucht.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Die verlegte Mitte kann als weltlich getragene Achse gelesen werden,",
            "wenn ihre beiden Knoten in Ereignissen und Uebergaengen wieder gekoppelt auftreten.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Achse zeitlich lokalisiert werden: in welchen Tickbereichen und Weltphasen tritt sie gehauft auf?",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--axis", action="append", required=True)
    parser.add_argument("--event-file", action="append", type=Path, default=[])
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = [build_row(axis, args.event_file) for axis in args.axis]
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"axes={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
