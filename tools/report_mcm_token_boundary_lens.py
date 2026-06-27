from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from report_mcm_token_neighborhood_lens import DEFAULT_INPUTS, DEFAULT_TOKENS, _float, _int, _load, _parse_inputs, _role, _token


def _segments(rows: list[dict[str, str]], token: str) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    start: int | None = None
    for index, row in enumerate(rows):
        if _token(row) == token:
            if start is None:
                start = index
        elif start is not None:
            result.append((start, index - 1))
            start = None
    if start is not None:
        result.append((start, len(rows) - 1))
    return result


def _collect(inputs: list[tuple[str, Path]], tokens: list[str]) -> list[dict[str, object]]:
    rows_out: list[dict[str, object]] = []
    for world, path in inputs:
        if not path.exists():
            continue
        rows = sorted(_load(path), key=lambda row: _int(row, "tick"))
        for token in tokens:
            for seg_index, (start, end) in enumerate(_segments(rows, token), start=1):
                first = rows[start]
                last = rows[end]
                before = rows[start - 1] if start > 0 else None
                after = rows[end + 1] if end + 1 < len(rows) else None
                rows_out.append(
                    {
                        "token": token,
                        "world": world,
                        "segment": seg_index,
                        "start_tick": _int(first, "tick"),
                        "end_tick": _int(last, "tick"),
                        "duration": end - start + 1,
                        "enter_from": _token(before),
                        "exit_to": _token(after),
                        "enter_role": _role(before),
                        "current_start_role": _role(first),
                        "current_end_role": _role(last),
                        "exit_role": _role(after),
                        "start_rekopplung": _float(first, "mcm_rekopplung_quality"),
                        "end_rekopplung": _float(last, "mcm_rekopplung_quality"),
                        "after_rekopplung": _float(after, "mcm_rekopplung_quality"),
                        "start_strain": _float(first, "mcm_strain_quality"),
                        "end_strain": _float(last, "mcm_strain_quality"),
                        "after_strain": _float(after, "mcm_strain_quality"),
                        "start_loudness": _float(first, "perception_auditory_loudness"),
                        "end_loudness": _float(last, "perception_auditory_loudness"),
                        "after_loudness": _float(after, "perception_auditory_loudness"),
                        "start_blur": _float(first, "perception_visual_blur"),
                        "end_blur": _float(last, "perception_visual_blur"),
                        "after_blur": _float(after, "perception_visual_blur"),
                        "start_tension": _float(first, "mcm_feldwirkung_mcm_tension"),
                        "end_tension": _float(last, "mcm_feldwirkung_mcm_tension"),
                        "after_tension": _float(after, "mcm_feldwirkung_mcm_tension"),
                    }
                )
    rows_out.sort(key=lambda row: (str(row["token"]), str(row["world"]), int(row["start_tick"])))
    return rows_out


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _summaries(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["token"])].append(row)

    out: list[dict[str, object]] = []
    for token, items in sorted(grouped.items()):
        enter = Counter(str(row["enter_from"]) for row in items if str(row["enter_from"]) != "-")
        exit_to = Counter(str(row["exit_to"]) for row in items if str(row["exit_to"]) != "-")
        worlds = Counter(str(row["world"]) for row in items)
        current_end_roles = Counter(str(row["current_end_role"]) for row in items)
        exit_roles = Counter(str(row["exit_role"]) for row in items if str(row["exit_role"]) != "-")
        out.append(
            {
                "token": token,
                "segments": len(items),
                "worlds": len(worlds),
                "world_profile": "; ".join(f"{name}:{count}" for name, count in worlds.most_common(8)),
                "dominant_enter": enter.most_common(1)[0][0] if enter else "-",
                "dominant_enter_count": enter.most_common(1)[0][1] if enter else 0,
                "dominant_exit": exit_to.most_common(1)[0][0] if exit_to else "-",
                "dominant_exit_count": exit_to.most_common(1)[0][1] if exit_to else 0,
                "end_role_profile": "; ".join(f"{name}:{count}" for name, count in current_end_roles.most_common(4)),
                "exit_role_profile": "; ".join(f"{name}:{count}" for name, count in exit_roles.most_common(4)),
                "duration_avg": _avg([float(row["duration"]) for row in items]),
                "within_rekopplung_delta": _avg([float(row["end_rekopplung"]) - float(row["start_rekopplung"]) for row in items]),
                "exit_rekopplung_delta": _avg([float(row["after_rekopplung"]) - float(row["end_rekopplung"]) for row in items if str(row["exit_to"]) != "-"]),
                "within_strain_delta": _avg([float(row["end_strain"]) - float(row["start_strain"]) for row in items]),
                "exit_strain_delta": _avg([float(row["after_strain"]) - float(row["end_strain"]) for row in items if str(row["exit_to"]) != "-"]),
                "within_loudness_delta": _avg([float(row["end_loudness"]) - float(row["start_loudness"]) for row in items]),
                "exit_loudness_delta": _avg([float(row["after_loudness"]) - float(row["end_loudness"]) for row in items if str(row["exit_to"]) != "-"]),
                "within_blur_delta": _avg([float(row["end_blur"]) - float(row["start_blur"]) for row in items]),
                "exit_blur_delta": _avg([float(row["after_blur"]) - float(row["end_blur"]) for row in items if str(row["exit_to"]) != "-"]),
                "within_tension_delta": _avg([float(row["end_tension"]) - float(row["start_tension"]) for row in items]),
                "exit_tension_delta": _avg([float(row["after_tension"]) - float(row["end_tension"]) for row in items if str(row["exit_to"]) != "-"]),
            }
        )
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(summary_rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# MCM-Token Grenzlupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.",
        "Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.",
        "",
        "## Uebersicht",
        "",
        "| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |",
        "|---|---:|---:|---:|---|---|---|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['token']} | {row['segments']} | {row['worlds']} | {_fmt(row['duration_avg'])} | "
            f"{row['dominant_enter']} ({row['dominant_enter_count']}) | "
            f"{row['dominant_exit']} ({row['dominant_exit_count']}) | "
            f"{row['end_role_profile']} | {row['exit_role_profile']} |"
        )

    lines.extend(
        [
            "",
            "## Achsbewegung Innerhalb Des Segments Und Beim Austritt",
            "",
            "| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in summary_rows:
        lines.append(
            f"| {row['token']} | {_fmt(row['within_rekopplung_delta'])} | {_fmt(row['exit_rekopplung_delta'])} | "
            f"{_fmt(row['within_strain_delta'])} | {_fmt(row['exit_strain_delta'])} | "
            f"{_fmt(row['within_loudness_delta'])} | {_fmt(row['exit_loudness_delta'])} | "
            f"{_fmt(row['within_blur_delta'])} | {_fmt(row['exit_blur_delta'])} |"
        )

    lines.extend(["", "## Befund", ""])
    for row in summary_rows:
        token = str(row["token"])
        exit_rek = float(row["exit_rekopplung_delta"])
        exit_strain = float(row["exit_strain_delta"])
        if exit_rek > 0 and exit_strain <= 0:
            verdict = "Austritt wirkt rekoppelnd"
        elif exit_rek < 0 and exit_strain > 0:
            verdict = "Austritt wirkt oeffnend/belastend"
        else:
            verdict = "Austritt wirkt gemischt"
        lines.append(f"- `{token}`: {verdict}; dominanter Austritt `{row['dominant_exit']}`.")

    lines.extend(
        [
            "",
            "## Gesamtlesart",
            "",
            "Die Grenzlupe ist die saubere Nachbarschaftspruefung.",
            "Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", action="append", default=[])
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--detail-csv", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    detail_rows = _collect(_parse_inputs(args.input, root), args.token or DEFAULT_TOKENS)
    summary_rows = _summaries(detail_rows)
    _write_csv(summary_rows, Path(args.out_csv))
    _write_csv(detail_rows, Path(args.detail_csv))
    _write_markdown(summary_rows, Path(args.out_md))
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.detail_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
