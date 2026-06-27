from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


DEFAULT_TOKENS = [
    "dio_mcm_episode_0v5p8er",
    "dio_mcm_episode_14l8khu",
    "dio_mcm_episode_1xx3u1e",
    "dio_mcm_episode_1q3us3f",
]

DEFAULT_INPUTS = [
    ("KAS_2024_5M", "debug/post_clean_diverse_kas_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG_2025_5M", "debug/post_clean_asset_tf_paxg_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("DOGE_2025_5M", "debug/post_clean_diverse_doge_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("XRP_2025_5M", "debug/post_clean_diverse_xrp_2025_5m/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_HARMONIC", "debug/post_clean_synth_harmonic_a/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_BRUCH_RAND", "debug/post_clean_synth_bruch_rand_a/dio_mini_lauf_2/episodes.csv"),
    ("SYNTH_RAND", "debug/post_clean_diverse_synth_rand_a/dio_mini_lauf_2/episodes.csv"),
    ("BTC_2024_5M", "debug/post_feature_cleanup_btc_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("SOL_2024_5M", "debug/post_feature_cleanup_sol_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("PAXG_2024_5M", "debug/post_feature_cleanup_paxg_2024_5m/dio_mini_lauf_2/episodes.csv"),
    ("DOGE_2024_5M", "debug/adapted_field_doge_2024_5m_10k/dio_mini_lauf_2/episodes.csv"),
    ("XRP_2024_5M", "debug/adapted_field_xrp_2024_5m_10k/dio_mini_lauf_2/episodes.csv"),
]


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


def _token(row: dict[str, str]) -> str:
    for key in ("mcm_field_episode_preview_symbol", "mcm_field_episode_symbol"):
        value = str(row.get(key, "") or "").strip()
        if value and value != "-":
            return value
    return "-"


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _parse_inputs(items: list[str], root: Path) -> list[tuple[str, Path]]:
    if not items:
        return [(name, root / rel) for name, rel in DEFAULT_INPUTS if (root / rel).exists()]
    parsed: list[tuple[str, Path]] = []
    for item in items:
        if "=" in item:
            name, text = item.split("=", 1)
        else:
            path = Path(item)
            name = path.parent.parent.name if path.name == "episodes.csv" else path.stem
            text = item
        path = Path(text)
        if not path.is_absolute():
            path = root / path
        parsed.append((name, path))
    return parsed


def _segment_indices(rows: list[dict[str, str]], token: str) -> list[tuple[int, int]]:
    segments: list[tuple[int, int]] = []
    start: int | None = None
    for index, row in enumerate(rows):
        if _token(row) == token:
            if start is None:
                start = index
        elif start is not None:
            segments.append((start, index - 1))
            start = None
    if start is not None:
        segments.append((start, len(rows) - 1))
    return segments


def _window(rows: list[dict[str, str]], start: int, end: int, before_after: int) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    before = rows[max(0, start - before_after) : start]
    current = rows[start : end + 1]
    after = rows[end + 1 : min(len(rows), end + 1 + before_after)]
    return before, current, after


def _direction(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "-"
    first = _float(rows[0], "close_reward")
    last = _float(rows[-1], "close_reward")
    diff = last - first
    if diff > 0.004:
        return "steigend"
    if diff < -0.004:
        return "fallend"
    return "seitwaerts"


def _summarize_window(rows: list[dict[str, str]]) -> dict[str, object]:
    return {
        "ticks": len(rows),
        "direction": _direction(rows),
        "avg_loudness": _avg([_float(row, "perception_auditory_loudness") for row in rows]),
        "avg_visual_blur": _avg([_float(row, "perception_visual_blur") for row in rows]),
        "avg_rekopplung": _avg([_float(row, "mcm_rekopplung_quality") for row in rows]),
        "avg_strain": _avg([_float(row, "mcm_strain_quality") for row in rows]),
        "avg_tension": _avg([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows]),
        "avg_sensory": _avg([_float(row, "mcm_sensory_coupling") for row in rows]),
        "top_family": Counter(str(row.get("symbol_family", "-") or "-") for row in rows).most_common(1)[0][0] if rows else "-",
        "top_effect": Counter(str(row.get("passive_mcm_effect_class", "-") or "-") for row in rows).most_common(1)[0][0] if rows else "-",
        "top_role": Counter(str(row.get("passive_inner_effect_awareness_state", "-") or "-") for row in rows).most_common(1)[0][0] if rows else "-",
    }


def _rows_for_segments(inputs: list[tuple[str, Path]], tokens: list[str], before_after: int) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for world, path in inputs:
        if not path.exists():
            continue
        rows = sorted(_load(path), key=lambda row: _int(row, "tick"))
        for token in tokens:
            for seg_index, (start, end) in enumerate(_segment_indices(rows, token), start=1):
                before, current, after = _window(rows, start, end, before_after)
                b = _summarize_window(before)
                c = _summarize_window(current)
                a = _summarize_window(after)
                out.append(
                    {
                        "token": token,
                        "world": world,
                        "segment": seg_index,
                        "start_tick": _int(rows[start], "tick"),
                        "end_tick": _int(rows[end], "tick"),
                        "duration": end - start + 1,
                        "before_direction": b["direction"],
                        "current_direction": c["direction"],
                        "after_direction": a["direction"],
                        "current_top_family": c["top_family"],
                        "current_top_effect": c["top_effect"],
                        "current_top_role": c["top_role"],
                        "before_loudness": round(float(b["avg_loudness"]), 6),
                        "current_loudness": round(float(c["avg_loudness"]), 6),
                        "after_loudness": round(float(a["avg_loudness"]), 6),
                        "before_visual_blur": round(float(b["avg_visual_blur"]), 6),
                        "current_visual_blur": round(float(c["avg_visual_blur"]), 6),
                        "after_visual_blur": round(float(a["avg_visual_blur"]), 6),
                        "before_rekopplung": round(float(b["avg_rekopplung"]), 6),
                        "current_rekopplung": round(float(c["avg_rekopplung"]), 6),
                        "after_rekopplung": round(float(a["avg_rekopplung"]), 6),
                        "before_strain": round(float(b["avg_strain"]), 6),
                        "current_strain": round(float(c["avg_strain"]), 6),
                        "after_strain": round(float(a["avg_strain"]), 6),
                        "before_tension": round(float(b["avg_tension"]), 6),
                        "current_tension": round(float(c["avg_tension"]), 6),
                        "after_tension": round(float(a["avg_tension"]), 6),
                        "before_sensory": round(float(b["avg_sensory"]), 6),
                        "current_sensory": round(float(c["avg_sensory"]), 6),
                        "after_sensory": round(float(a["avg_sensory"]), 6),
                    }
                )
    out.sort(key=lambda row: (str(row["token"]), str(row["world"]), int(row["start_tick"])))
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


def _write_markdown(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    by_token: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        by_token.setdefault(str(row["token"]), []).append(row)

    lines = [
        "# MCM-Token Rohwelt-Segmentlupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest konkrete Kontaktsegmente fuer ausgewaehlte MCM-Episodentokens.",
        "Sie betrachtet Vorfenster, Kontaktfenster und Nachfenster direkt aus den `episodes.csv`-Spuren.",
        "",
        "## Uebersicht",
        "",
        "| Token | Segmente | Welten | mittlere Dauer | Richtung im Kontakt | Effekt im Kontakt |",
        "|---|---:|---:|---:|---|---|",
    ]
    for token, token_rows in sorted(by_token.items()):
        directions = Counter(str(row["current_direction"]) for row in token_rows)
        effects = Counter(str(row["current_top_effect"]) for row in token_rows)
        worlds = {str(row["world"]) for row in token_rows}
        avg_duration = sum(int(row["duration"]) for row in token_rows) / max(1, len(token_rows))
        lines.append(
            f"| {token} | {len(token_rows)} | {len(worlds)} | {avg_duration:.2f} | "
            f"{'; '.join(f'{k}:{v}' for k, v in directions.most_common(3))} | "
            f"{'; '.join(f'{k}:{v}' for k, v in effects.most_common(3))} |"
        )

    lines.extend(["", "## Tokenbefunde", ""])
    for token, token_rows in sorted(by_token.items()):
        avg_loud_delta = _avg([float(row["current_loudness"]) - float(row["before_loudness"]) for row in token_rows])
        avg_blur_delta = _avg([float(row["current_visual_blur"]) - float(row["before_visual_blur"]) for row in token_rows])
        avg_rek_delta = _avg([float(row["current_rekopplung"]) - float(row["before_rekopplung"]) for row in token_rows])
        avg_strain_delta = _avg([float(row["current_strain"]) - float(row["before_strain"]) for row in token_rows])
        worlds = Counter(str(row["world"]) for row in token_rows)
        lines.extend(
            [
                f"### `{token}`",
                "",
                f"- Welten: `{'; '.join(f'{k}:{v}' for k, v in worlds.most_common())}`",
                f"- Lautheit Kontakt minus Vorfenster: `{avg_loud_delta:+.4f}`",
                f"- Unschaerfe Kontakt minus Vorfenster: `{avg_blur_delta:+.4f}`",
                f"- Rekopplung Kontakt minus Vorfenster: `{avg_rek_delta:+.4f}`",
                f"- Strain Kontakt minus Vorfenster: `{avg_strain_delta:+.4f}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Befund",
            "",
            "Die Segmentlupe trennt Tokenoberflaeche von Kontaktlage.",
            "Wenn ein Token im Kontakt lauter/unschaerfer und weniger rekoppelnd wird, passt das zur Driftlesung.",
            "Wenn ein Token im Kontakt leiser/schaerfer oder rekoppelnder wird, passt das zur Reifungs- oder Rueckbindungslesung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die Segmentbefunde gegen die Driftlupe verbunden werden: fuer jeden Token ein Kurzurteil, ob der Zonenwechsel eher Weltphase, Rezeptoraufnahme oder MCM-Drift ist.",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", action="append", default=[])
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--before-after", type=int, default=12)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    tokens = args.token or DEFAULT_TOKENS
    rows = _rows_for_segments(_parse_inputs(args.input, root), tokens, args.before_after)
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, Path(args.out_md))
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
