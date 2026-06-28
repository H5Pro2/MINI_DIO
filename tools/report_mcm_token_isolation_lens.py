from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


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


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _segments(rows: list[dict[str, str]], token: str) -> list[dict[str, object]]:
    by_world: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_world[row.get("world", "-")].append(row)

    segments: list[dict[str, object]] = []
    for world, items in by_world.items():
        sorted_items = sorted(items, key=lambda row: _int(row, "tick"))
        current: list[dict[str, str]] = []
        last_tick: int | None = None
        for row in sorted_items:
            tick = _int(row, "tick")
            if last_tick is None or tick == last_tick + 1:
                current.append(row)
            else:
                if current:
                    segments.append(_segment_summary(world, current, token))
                current = [row]
            last_tick = tick
        if current:
            segments.append(_segment_summary(world, current, token))
    return segments


def _segment_summary(world: str, items: list[dict[str, str]], token: str) -> dict[str, object]:
    start = _int(items[0], "tick")
    end = _int(items[-1], "tick")
    prev_token = items[0].get("prev_token", "-")
    next_token = items[-1].get("next_token", "-")
    role_counter = Counter(row.get("current_role", "-") for row in items)
    return {
        "token": token,
        "world": world,
        "start_tick": start,
        "end_tick": end,
        "duration": end - start + 1,
        "entry_token": prev_token,
        "exit_token": next_token,
        "role_profile": "; ".join(f"{k}:{v}" for k, v in role_counter.most_common()),
        "avg_rekopplung": _avg([_float(row, "current_rekopplung") for row in items]),
        "avg_strain": _avg([_float(row, "current_strain") for row in items]),
        "avg_loudness": _avg([_float(row, "current_loudness") for row in items]),
        "avg_blur": _avg([_float(row, "current_blur") for row in items]),
        "avg_tension": _avg([_float(row, "current_tension") for row in items]),
    }


def _world_summary(rows: list[dict[str, str]], segments: list[dict[str, object]]) -> list[dict[str, object]]:
    by_world: dict[str, list[dict[str, str]]] = defaultdict(list)
    seg_by_world: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_world[row.get("world", "-")].append(row)
    for segment in segments:
        seg_by_world[str(segment["world"])].append(segment)

    out: list[dict[str, object]] = []
    for world, items in sorted(by_world.items()):
        world_segments = seg_by_world.get(world, [])
        role_counter = Counter(row.get("current_role", "-") for row in items)
        out.append(
            {
                "world": world,
                "contacts": len(items),
                "segments": len(world_segments),
                "max_segment_duration": max([int(seg["duration"]) for seg in world_segments], default=0),
                "avg_segment_duration": _avg([float(seg["duration"]) for seg in world_segments]),
                "self_prev_share": _avg([1.0 if row.get("prev_token") == row.get("token") else 0.0 for row in items]),
                "self_next_share": _avg([1.0 if row.get("next_token") == row.get("token") else 0.0 for row in items]),
                "role_profile": "; ".join(f"{k}:{v}" for k, v in role_counter.most_common()),
                "avg_rekopplung": _avg([_float(row, "current_rekopplung") for row in items]),
                "avg_strain": _avg([_float(row, "current_strain") for row in items]),
                "avg_loudness": _avg([_float(row, "current_loudness") for row in items]),
                "avg_blur": _avg([_float(row, "current_blur") for row in items]),
                "avg_tension": _avg([_float(row, "current_tension") for row in items]),
            }
        )
    return out


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(
    path: Path,
    token: str,
    rows: list[dict[str, str]],
    worlds: list[dict[str, object]],
    segments: list[dict[str, object]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    role_counter = Counter(row.get("current_role", "-") for row in rows)
    entry_counter = Counter(row.get("prev_token", "-") for row in rows if row.get("prev_token") != token)
    exit_counter = Counter(row.get("next_token", "-") for row in rows if row.get("next_token") != token)
    self_prev = _avg([1.0 if row.get("prev_token") == token else 0.0 for row in rows])
    self_next = _avg([1.0 if row.get("next_token") == token else 0.0 for row in rows])
    max_duration = max([int(seg["duration"]) for seg in segments], default=0)
    avg_duration = _avg([float(seg["duration"]) for seg in segments])

    lines: list[str] = []
    lines.append(f"# MCM-Token Isolation: {_short(token)}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose isoliert einen einzelnen MCM-Token und prueft, ob seine Verdichtung weltuebergreifend, selbstbindend und phasenstabil ist.")
    lines.append("")
    lines.append("## Gesamtbefund")
    lines.append("")
    lines.append(f"- Token: `{token}`")
    lines.append(f"- Kontakte: `{len(rows)}`")
    lines.append(f"- Welten: `{len(worlds)}`")
    lines.append(f"- Segmente: `{len(segments)}`")
    lines.append(f"- Maximale Segmentdauer: `{max_duration}`")
    lines.append(f"- Mittlere Segmentdauer: `{avg_duration:.2f}`")
    lines.append(f"- Selbstbindung vorher/nachher: `{self_prev:.4f}` / `{self_next:.4f}`")
    lines.append(f"- Rollenprofil: `{'; '.join(f'{k}:{v}' for k, v in role_counter.most_common())}`")
    lines.append("")
    lines.append("## Weltprofil")
    lines.append("")
    lines.append("| Welt | Kontakte | Segmente | Max Dauer | Mittlere Dauer | Selbstbindung | Rolle | Rekopplung | Strain | Lautheit |")
    lines.append("|---|---:|---:|---:|---:|---:|---|---:|---:|---:|")
    for world in worlds:
        self_share = min(float(world["self_prev_share"]), float(world["self_next_share"]))
        lines.append(
            f"| {world['world']} | {world['contacts']} | {world['segments']} | {world['max_segment_duration']} | {float(world['avg_segment_duration']):.2f} | {self_share:.4f} | {world['role_profile']} | {float(world['avg_rekopplung']):.4f} | {float(world['avg_strain']):.4f} | {float(world['avg_loudness']):.4f} |"
        )
    lines.append("")
    lines.append("## Ein- Und Austrittskontakte")
    lines.append("")
    lines.append(f"- Dominante Fremdeintritte: `{'; '.join(f'{_short(k)}:{v}' for k, v in entry_counter.most_common(5)) or '-'}`")
    lines.append(f"- Dominante Fremdaustritte: `{'; '.join(f'{_short(k)}:{v}' for k, v in exit_counter.most_common(5)) or '-'}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    if len(worlds) >= 3 and self_prev >= 0.90 and self_next >= 0.90 and max_duration >= 100:
        lines.append("Der Token wirkt als starke Eigenphase.")
        lines.append("Er ist nicht nur ein Einzelkontakt und nicht nur eine einzelne laute Weltsequenz.")
        lines.append("Die hohe Selbstbindung zeigt, dass hier eine innere Feldlage ueber Zeit gehalten wird.")
    else:
        lines.append("Der Token ist sichtbar, aber die Kriterien fuer eine starke Eigenphase sind nur teilweise erfuellt.")
    lines.append("")
    lines.append("Wichtig:")
    lines.append("")
    lines.append("Diese Eigenphase ist nicht automatisch ein Rand-Gegenkern.")
    lines.append("Sie kann als Driftkern gelesen werden, wenn sie in Drift-/Oeffnungszonen liegt und dennoch stark selbstbindet.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte dieser Token gegen die zentrale Brueckenstruktur gelegt werden: ist er ein Gegenbereich, ein paralleler Driftpol oder eine lange Seitenphase im selben Topologieraum?")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--details", type=Path, required=True)
    parser.add_argument("--token", required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--out-world-csv", type=Path, required=True)
    parser.add_argument("--out-segment-csv", type=Path, required=True)
    args = parser.parse_args()

    rows = [row for row in _read(args.details) if row.get("token") == args.token]
    segments = _segments(rows, args.token)
    worlds = _world_summary(rows, segments)
    _write_csv(args.out_world_csv, worlds)
    _write_csv(args.out_segment_csv, segments)
    _write_md(args.out_md, args.token, rows, worlds, segments)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_world_csv}")
    print(f"wrote {args.out_segment_csv}")


if __name__ == "__main__":
    main()
