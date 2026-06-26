from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EPISODES_DEFAULT = (
    ROOT
    / "debug"
    / "block_k_10k_multiworld"
    / "kontrolliert_2023_negative_stress_10k_5m_solusdt"
    / "dio_mini_lauf_1"
    / "episodes.csv"
)
CSV_DEFAULT = ROOT / "docs" / "befunde" / "806_BLOCK_K_FELDEPISODEN_ZEITREIHE.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "806_BLOCK_K_FELDEPISODEN_ZEITREIHE.md"


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    if result != result:
        return default
    return result


def _safe_int(value: object, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return default


def _avg(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _segment_key(row: dict[str, str], mode: str) -> tuple[str, ...]:
    field_state = str(row.get("mcm_field_effect_state", "") or "-")
    effect_class = str(row.get("passive_mcm_effect_class", "") or "-")
    if mode == "symbol":
        return (
            str(row.get("mcm_field_episode_symbol", "") or "-"),
            field_state,
            effect_class,
        )
    if mode == "state":
        return (field_state,)
    return (field_state, effect_class)


def _summarize_segment(rows: list[dict[str, str]], segment_index: int) -> dict[str, object]:
    first = rows[0]
    last = rows[-1]
    states = Counter(str(row.get("mcm_field_effect_state", "-") or "-") for row in rows)
    classes = Counter(str(row.get("passive_mcm_effect_class", "-") or "-") for row in rows)
    symbols = Counter()
    for row in rows:
        symbol = str(row.get("mcm_field_episode_symbol", "") or "")
        preview = str(row.get("mcm_field_episode_preview_symbol", "") or "")
        if symbol and symbol != "-":
            symbols[symbol] += 1
        elif preview and preview != "-":
            symbols[preview] += 1
        else:
            symbols["-"] += 1
    families = Counter(str(row.get("symbol_family", "-") or "-") for row in rows)
    dominant_symbol = symbols.most_common(1)[0][0] if symbols else "-"
    dominant_state = states.most_common(1)[0][0]
    dominant_class = classes.most_common(1)[0][0]
    return {
        "segment": segment_index,
        "start_tick": _safe_int(first.get("tick")),
        "end_tick": _safe_int(last.get("tick")),
        "duration": len(rows),
        "mcm_field_episode_symbol": dominant_symbol,
        "mcm_field_effect_state": dominant_state,
        "passive_mcm_effect_class": dominant_class,
        "dominant_symbol_family": families.most_common(1)[0][0] if families else "-",
        "avg_carry": _avg([_safe_float(row.get("mcm_carry_quality")) for row in rows]),
        "avg_rekopplung": _avg([_safe_float(row.get("mcm_rekopplung_quality")) for row in rows]),
        "avg_strain": _avg([_safe_float(row.get("mcm_strain_quality")) for row in rows]),
        "avg_sensory_coupling": _avg([_safe_float(row.get("mcm_sensory_coupling")) for row in rows]),
        "avg_afterimage": _avg([_safe_float(row.get("mini_afterimage")) for row in rows]),
        "avg_temporal_trust": _avg([_safe_float(row.get("mini_temporal_trust_support")) for row in rows]),
        "avg_temporal_caution": _avg([_safe_float(row.get("mini_temporal_caution_support")) for row in rows]),
        "avg_reflection_carry": _avg([_safe_float(row.get("reflection_context_carry")) for row in rows]),
        "avg_reflection_strain": _avg([_safe_float(row.get("reflection_context_strain")) for row in rows]),
        "avg_field_tension": _avg([_safe_float(row.get("mcm_feldwirkung_mcm_tension")) for row in rows]),
        "avg_field_coherence": _avg([_safe_float(row.get("mcm_feldwirkung_mcm_coherence")) for row in rows]),
    }


def build_segments(rows: list[dict[str, str]], mode: str = "phase") -> list[dict[str, object]]:
    if not rows:
        return []
    segments: list[dict[str, object]] = []
    current: list[dict[str, str]] = [rows[0]]
    current_key = _segment_key(rows[0], mode)
    for row in rows[1:]:
        key = _segment_key(row, mode)
        if key != current_key:
            segments.append(_summarize_segment(current, len(segments) + 1))
            current = [row]
            current_key = key
        else:
            current.append(row)
    segments.append(_summarize_segment(current, len(segments) + 1))
    for index, segment in enumerate(segments):
        previous_symbol = str(segments[index - 1]["mcm_field_episode_symbol"]) if index > 0 else "start"
        next_symbol = str(segments[index + 1]["mcm_field_episode_symbol"]) if index < len(segments) - 1 else "end"
        segment["previous_mcm_field_episode_symbol"] = previous_symbol
        segment["next_mcm_field_episode_symbol"] = next_symbol
        segment["transition"] = f"{previous_symbol}->{segment['mcm_field_episode_symbol']}->{next_symbol}"
    return segments


def _write_csv(path: Path, segments: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(segments[0].keys()) if segments else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(segments)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(
    path: Path,
    segments: list[dict[str, object]],
    source: Path,
    mode: str,
    title: str,
    question: str,
    next_step: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    long_segments = [segment for segment in segments if int(segment["duration"]) >= 1000]
    strained_segments = [segment for segment in segments if str(segment["mcm_field_effect_state"]) != "field_carried"]
    repeated_symbols = Counter(str(segment["mcm_field_episode_symbol"]) for segment in segments)
    repeated_symbols = Counter({key: value for key, value in repeated_symbols.items() if value > 1})
    avg_duration = _avg([float(segment["duration"]) for segment in segments])
    avg_long_carry = _avg([float(segment["avg_carry"]) for segment in long_segments])
    avg_long_rekopplung = _avg([float(segment["avg_rekopplung"]) for segment in long_segments])
    avg_long_strain = _avg([float(segment["avg_strain"]) for segment in long_segments])
    lines = [
        f"# {title}",
        "",
        "## Fragestellung",
        "",
        question,
        "",
        "Quelle:",
        "",
        f"- `{source.relative_to(ROOT) if source.is_relative_to(ROOT) else source}`",
        f"- Segmentierung: `{mode}`",
        "",
        "## Segmentuebersicht",
        "",
        f"- Segmente: `{len(segments)}`",
        f"- durchschnittliche Segmentdauer: `{avg_duration:.2f}` Ticks",
        f"- lange Segmente ab 1000 Ticks: `{len(long_segments)}`",
        f"- nicht getragene/gespannte Segmente: `{len(strained_segments)}`",
        f"- wiederkehrende Feldepisoden-Symbole: `{len(repeated_symbols)}`",
        "",
        "Lange Segmente:",
        "",
        f"- Carry: `{avg_long_carry:.4f}`",
        f"- Rekopplung: `{avg_long_rekopplung:.4f}`",
        f"- Strain: `{avg_long_strain:.4f}`",
        "",
        "## Zeitreihe",
        "",
        "| Segment | Ticks | Dauer | Feldepisode | Zustand | Klasse | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | Transition |",
        "|---:|---|---:|---|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for segment in segments:
        lines.append(
            f"| {segment['segment']} | {segment['start_tick']}-{segment['end_tick']} | {segment['duration']} | "
            f"{segment['mcm_field_episode_symbol']} | {segment['mcm_field_effect_state']} | "
            f"{segment['passive_mcm_effect_class']} | {_fmt(segment['avg_carry'])} | "
            f"{_fmt(segment['avg_rekopplung'])} | {_fmt(segment['avg_strain'])} | "
            f"{_fmt(segment['avg_afterimage'])} | {_fmt(segment['avg_temporal_trust'])} | "
            f"{segment['transition']} |"
        )
    lines.extend(["", "## Befund", ""])
    if long_segments:
        lines.extend(
            [
                "Die Welt zeigt Feldintegration als Phasenstruktur, nicht nur als Durchschnittswert.",
                "",
                "Lesart:",
                "",
                "- Lange getragene Feldepisoden bilden den Hauptanteil der Weltzeit.",
                "- Kurze gespannte oder kippende Segmente treten als Bruch- oder Uebergangspunkte auf.",
                "- Feldepisoden-Symbole markieren die jeweilige Feldphase; Wiederkehr zeigt sich hier primaer als wiederholter Wechsel zwischen getragenen Langphasen und kurzen Spannungsbruechen.",
                "- Nachhall und temporales Trust-Signal bleiben in langen Segmenten lesbar und begleiten die Integration.",
                "",
                "Damit wird der Befund aus `805` konkretisiert: die hoehere 10k-Stabilisierung ist in einer zeitlichen Segmentordnung sichtbar.",
            ]
        )
    else:
        lines.extend(
            [
                "Die Welt zeigt eine kurze, durchgehend getragene Feldphase ohne langen Integrationsabschnitt nach der 1000-Tick-Leseschwelle.",
                "",
                "Lesart:",
                "",
                "- Der Feldzustand bleibt stabil getragen.",
                "- Es entstehen keine langen Integrationssegmente.",
                "- Nachhall und temporales Trust-Signal bleiben niedriger als in der 10k-Langphase.",
                "- Es gibt hier keinen sichtbaren Bruch, aber auch keine lange Feldzeit zur Reifung.",
                "",
                "Damit eignet sich diese Welt als Gegenpol zur 10k-Zeitreihe: stabiler Zustand ja, laengere Feldintegration nein.",
            ]
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            "Diese Zeitreihe ist eine Segmentierung nach Feldphase. Sie ist keine Handlungsauswertung und keine kausale Beweisfuehrung.",
            "",
            "## Wie es weitergeht",
            "",
            next_step,
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=Path, default=EPISODES_DEFAULT)
    parser.add_argument("--mode", choices=["state", "phase", "symbol"], default="state")
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    parser.add_argument("--title", default="806 - Block-K Feldepisoden-Zeitreihe")
    parser.add_argument(
        "--question",
        default="Wann entsteht Feldintegration, wann bricht sie, und tragen Nachhall/Feldzeit diese Phasen sichtbar mit?",
    )
    parser.add_argument(
        "--next-step",
        default="Als naechstes sollte dieselbe Zeitreihen-Lupe fuer eine stressige 1000/2000er Welt laufen. Dann sehen wir, ob kuerzere Stresswelten weniger lange Integrationssegmente und mehr Bruchpunkte bilden.",
    )
    args = parser.parse_args()

    source = args.episodes if args.episodes.is_absolute() else ROOT / args.episodes
    rows = _read_rows(source)
    segments = build_segments(rows, mode=args.mode)
    _write_csv(args.csv_out, segments)
    _write_markdown(args.md_out, segments, source, args.mode, args.title, args.question, args.next_step)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    print(f"segments={len(segments)} long_segments={sum(1 for segment in segments if int(segment['duration']) >= 1000)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
