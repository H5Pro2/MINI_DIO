from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _role(row: dict[str, str]) -> str:
    rec = _float(row, "mcm_rekopplung_quality")
    carry = _float(row, "mcm_carry_quality")
    strain = _float(row, "mcm_strain_quality")
    pressure = _float(row, "mcm_feldwirkung_mcm_tension") or _float(row, "perception_adapted_field_intake_pressure")
    if rec >= 0.704 and carry >= 0.533 and pressure <= 0.425 and strain <= 0.18:
        return "zentrum_stabil"
    if pressure >= 0.438 or strain >= 0.25:
        return "spannungsrand_kippnaehe"
    if rec < 0.702 and carry < 0.533:
        return "offene_variante"
    return "rekopplungsnaehe"


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _segments(label: str, rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    current_role = ""
    start_tick = 0
    items: list[dict[str, str]] = []
    for row in rows:
        role = _role(row)
        tick = _int(row, "tick")
        if current_role and role != current_role:
            out.append(_segment_row(label, current_role, start_tick, _int(items[-1], "tick"), items))
            items = []
            start_tick = tick
        if not current_role or role != current_role:
            current_role = role
            start_tick = tick
        items.append(row)
    if items:
        out.append(_segment_row(label, current_role, start_tick, _int(items[-1], "tick"), items))
    return out


def _segment_row(label: str, role: str, start_tick: int, end_tick: int, items: list[dict[str, str]]) -> dict[str, object]:
    return {
        "world": label,
        "role": role,
        "start_tick": start_tick,
        "end_tick": end_tick,
        "duration": max(1, end_tick - start_tick + 1),
        "avg_raw_field_intake": _avg([_float(row, "perception_raw_field_intake_pressure") for row in items]),
        "avg_auditory_loudness": _avg([_float(row, "perception_auditory_loudness") for row in items]),
        "avg_visual_sharpness": _avg([_float(row, "perception_visual_sharpness") for row in items]),
        "avg_rekopplung": _avg([_float(row, "mcm_rekopplung_quality") for row in items]),
        "avg_strain": _avg([_float(row, "mcm_strain_quality") for row in items]),
    }


def _transition_summary(segments: list[dict[str, object]], lookback: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    transitions = Counter()
    role_counts = Counter(str(seg["role"]) for seg in segments)
    role_duration = Counter()
    rand_segments = [seg for seg in segments if seg["role"] == "spannungsrand_kippnaehe"]
    rand_after_open = 0
    rand_after_center = 0
    rand_after_rekopplung = 0
    open_before_rand_durations: list[float] = []

    for seg in segments:
        role_duration[str(seg["role"])] += int(seg["duration"])

    transition_rows: list[dict[str, object]] = []
    for index in range(1, len(segments)):
        previous = str(segments[index - 1]["role"])
        current = str(segments[index]["role"])
        key = f"{previous}->{current}"
        transitions[key] += 1
        transition_rows.append(
            {
                "world": segments[index]["world"],
                "transition": key,
                "from_role": previous,
                "to_role": current,
                "start_tick": segments[index]["start_tick"],
                "previous_duration": segments[index - 1]["duration"],
                "current_duration": segments[index]["duration"],
                "current_raw_field_intake": segments[index]["avg_raw_field_intake"],
                "current_rekopplung": segments[index]["avg_rekopplung"],
                "current_strain": segments[index]["avg_strain"],
            }
        )

    for index, seg in enumerate(segments):
        if seg["role"] != "spannungsrand_kippnaehe":
            continue
        previous = segments[max(0, index - lookback):index]
        previous_roles = [str(item["role"]) for item in previous]
        if "offene_variante" in previous_roles:
            rand_after_open += 1
            open_seg = next(item for item in reversed(previous) if item["role"] == "offene_variante")
            open_before_rand_durations.append(float(open_seg["duration"]))
        if "zentrum_stabil" in previous_roles:
            rand_after_center += 1
        if "rekopplungsnaehe" in previous_roles:
            rand_after_rekopplung += 1

    summary: dict[str, object] = {
        "segments": len(segments),
        "role_counts": dict(role_counts),
        "role_duration": dict(role_duration),
        "transition_counts": dict(transitions.most_common()),
        "rand_segments": len(rand_segments),
        "rand_after_open": rand_after_open,
        "rand_after_center": rand_after_center,
        "rand_after_rekopplung": rand_after_rekopplung,
        "rand_after_open_ratio": rand_after_open / max(1, len(rand_segments)),
        "avg_open_duration_before_rand": _avg(open_before_rand_durations),
    }
    return transition_rows, summary


def _parse_world(value: str) -> tuple[str, Path]:
    parts = value.split("=")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("world must be LABEL=EPISODES_CSV")
    return parts[0], Path(parts[1])


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(world_summaries: list[dict[str, object]], transition_rows: list[dict[str, object]], out: Path, title: str) -> None:
    lines = [
        f"# {title}",
        "",
        "## Grundfrage",
        "",
        "Liegt `offene_variante` zeitlich vor `spannungsrand_kippnaehe`, oder sind beide Rollen unabhaengige Feldantworten?",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Segmente | Randsegmente | Rand nach Offen | Quote | Ø Offen-Dauer vor Rand |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for summary in world_summaries:
        lines.append(
            f"| {summary['world']} | {summary['segments']} | {summary['rand_segments']} | "
            f"{summary['rand_after_open']} | {_fmt(summary['rand_after_open_ratio'])} | "
            f"{_fmt(summary['avg_open_duration_before_rand'])} |"
        )

    lines.extend(["", "## Wichtigste Uebergaenge", ""])
    for summary in world_summaries:
        lines.append(f"### {summary['world']}")
        counts = summary["transition_counts"]
        if isinstance(counts, dict):
            for name, count in list(counts.items())[:8]:
                lines.append(f"- `{name}`: `{count}`")
        lines.append("")

    direct_open_to_rand = [row for row in transition_rows if row["transition"] == "offene_variante->spannungsrand_kippnaehe"]
    rand_to_open = [row for row in transition_rows if row["transition"] == "spannungsrand_kippnaehe->offene_variante"]
    lines.extend(
        [
            "## Befund",
            "",
            f"- Direkte Uebergaenge `offene_variante -> spannungsrand_kippnaehe`: `{len(direct_open_to_rand)}`",
            f"- Direkte Uebergaenge `spannungsrand_kippnaehe -> offene_variante`: `{len(rand_to_open)}`",
            "",
            "Eine hohe Quote `Rand nach Offen` spricht fuer eine Feldphase: Offenheit kann als Vorraum vor Rand/Kipp auftreten.",
            "Viele Rueckuebergaenge Rand/Kipp -> Offen sprechen dagegen fuer eine Pendelbewegung an der Rekopplungsgrenze.",
            "",
            "## Ableitung",
            "",
            "Wenn Rand/Kipp haeufig nach Offenheit kommt, ist Offenheit kein neutraler Zustand. Sie ist dann eine Vorphase, in der das Feld noch Uebergang halten kann.",
            "",
            "Wenn Rand/Kipp ohne vorherige Offenheit kommt, entsteht die Randnaehe direkter aus Rohaufnahme, Lautheit und schwacher Rekopplung.",
            "",
            "Wie es weitergeht: Die naechste Pruefung sollte die direkten `Offen -> Rand` und `Rand -> Offen` Segmente als kleine Zeitfenster plotten.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", required=True, type=_parse_world)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    parser.add_argument("--segments-out", required=True)
    parser.add_argument("--title", default="Rezeptor-Rollen Phasenuebergaenge")
    parser.add_argument("--lookback", type=int, default=3)
    args = parser.parse_args()

    all_segments: list[dict[str, object]] = []
    all_transitions: list[dict[str, object]] = []
    world_summaries: list[dict[str, object]] = []
    for label, path in args.world:
        segments = _segments(label, _load(path))
        transitions, summary = _transition_summary(segments, args.lookback)
        summary["world"] = label
        all_segments.extend(segments)
        all_transitions.extend(transitions)
        world_summaries.append(summary)

    _write_csv(all_segments, Path(args.segments_out))
    _write_csv(all_transitions, Path(args.csv_out))
    _write_markdown(world_summaries, all_transitions, Path(args.out), args.title)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.segments_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
