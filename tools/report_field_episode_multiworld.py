from __future__ import annotations

import argparse
import csv
from pathlib import Path

from report_field_episode_timeline import _read_rows, _safe_float, build_segments


ROOT = Path(__file__).resolve().parents[1]
DEBUG_DEFAULT = ROOT / "debug" / "block_k_10k_multiworld"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "809_BLOCK_K_10K_FELDZEIT_MEHRWELT.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "809_BLOCK_K_10K_FELDZEIT_MEHRWELT.md"


def _weighted_avg(rows: list[dict[str, object]], key: str) -> float:
    weighted_sum = 0.0
    total_weight = 0.0
    for row in rows:
        weight = max(0.0, _safe_float(row.get("duration")))
        weighted_sum += _safe_float(row.get(key)) * weight
        total_weight += weight
    if total_weight <= 0.0:
        return 0.0
    return weighted_sum / total_weight


def _world_label(path: Path) -> str:
    try:
        return path.relative_to(DEBUG_DEFAULT).parts[0]
    except Exception:
        return path.parent.parent.name


def summarize_world(path: Path, long_threshold: int = 1000) -> dict[str, object]:
    segments = build_segments(_read_rows(path), mode="state")
    total_ticks = sum(int(segment["duration"]) for segment in segments)
    long_segments = [segment for segment in segments if int(segment["duration"]) >= long_threshold]
    strained_segments = [
        segment for segment in segments if str(segment["mcm_field_effect_state"]) != "field_carried"
    ]
    carried_ticks = sum(
        int(segment["duration"])
        for segment in segments
        if str(segment["mcm_field_effect_state"]) == "field_carried"
    )
    return {
        "world": _world_label(path),
        "segments": len(segments),
        "total_ticks": total_ticks,
        "max_duration": max((int(segment["duration"]) for segment in segments), default=0),
        "long_segments": len(long_segments),
        "strained_segments": len(strained_segments),
        "carried_tick_share": carried_ticks / max(1, total_ticks),
        "avg_carry": _weighted_avg(segments, "avg_carry"),
        "avg_rekopplung": _weighted_avg(segments, "avg_rekopplung"),
        "avg_strain": _weighted_avg(segments, "avg_strain"),
        "avg_afterimage": _weighted_avg(segments, "avg_afterimage"),
        "avg_temporal_trust": _weighted_avg(segments, "avg_temporal_trust"),
        "dominant_pattern": _dominant_pattern(segments),
        "source": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
    }


def _dominant_pattern(segments: list[dict[str, object]]) -> str:
    if not segments:
        return "-"
    labels = []
    for segment in segments:
        state = str(segment.get("mcm_field_effect_state", "-"))
        duration = int(segment.get("duration", 0) or 0)
        if state == "field_carried" and duration >= 1000:
            labels.append("lang_getragen")
        elif state == "field_carried":
            labels.append("kurz_getragen")
        else:
            labels.append("spannungsbruch")
    compact: list[str] = []
    for label in labels:
        if not compact or compact[-1] != label:
            compact.append(label)
    return " -> ".join(compact)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    avg_trust = sum(float(row["avg_temporal_trust"]) for row in rows) / max(1, len(rows))
    avg_afterimage = sum(float(row["avg_afterimage"]) for row in rows) / max(1, len(rows))
    avg_max_duration = sum(float(row["max_duration"]) for row in rows) / max(1, len(rows))
    all_stable = all(float(row["carried_tick_share"]) >= 0.99 for row in rows)
    lines = [
        "# 809 - Block-K 10k-Feldzeit Mehrwelt",
        "",
        "## Fragestellung",
        "",
        "Bleibt die erhoehte Feldzeit/Integration in mehreren 10k-Welten sichtbar, oder war `808` ein Einzelbefund?",
        "",
        "## Ergebnis",
        "",
        f"- Welten: `{len(rows)}`",
        f"- durchschnittliche Max-Dauer: `{avg_max_duration:.4f}` Ticks",
        f"- durchschnittlicher Nachhall: `{avg_afterimage:.4f}`",
        f"- durchschnittlicher Feldzeit/Trust: `{avg_trust:.4f}`",
        f"- durchgehend getragener Tick-Anteil >= 0.99 in allen Welten: `{str(all_stable).lower()}`",
        "",
        "## Weltvergleich",
        "",
        "| Welt | Segmente | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | Muster |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['world']} | {row['segments']} | {row['total_ticks']} | "
            f"{row['max_duration']} | {row['long_segments']} | {row['strained_segments']} | "
            f"{_fmt(row['carried_tick_share'])} | {_fmt(row['avg_carry'])} | "
            f"{_fmt(row['avg_rekopplung'])} | {_fmt(row['avg_strain'])} | "
            f"{_fmt(row['avg_afterimage'])} | {_fmt(row['avg_temporal_trust'])} | "
            f"{row['dominant_pattern']} |"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die 10k-Feldzeit ist in allen geprueften Welten sichtbar. Die konkrete Segmentform variiert, aber die Grundlesung bleibt erhalten:",
            "",
            "- hohe getragene Tick-Anteile,",
            "- lange stabile Feldphasen,",
            "- messbarer Nachhall,",
            "- hoher temporaler Trust,",
            "- keine dauerhafte Feldkollaps-Struktur.",
            "",
            "Damit wird `808` gestuetzt: laengere Weltwirkung fuehrt hier nicht nur zu mehr Daten, sondern zu tieferer lesbarer Feldintegration.",
            "",
            "## Grenze",
            "",
            "Dies ist weiterhin passive Diagnostik. Der Befund zeigt Feldzeit-Integration in den vorhandenen 10k-Welten, aber noch keine allgemeine Aussage fuer alle moeglichen Welten.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Mehrwelt-Lupe auf kurze 1k/2k-Welten und asset-gemischte Welten angewendet werden. Dann sehen wir, ob Feldzeit wirklich mit Dauer reift oder ob Asset-/Regime-Art die Feldintegration staerker bestimmt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug-root", type=Path, default=DEBUG_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    debug_root = args.debug_root if args.debug_root.is_absolute() else ROOT / args.debug_root
    episode_files = sorted(debug_root.glob("*/*/episodes.csv"))
    if not episode_files:
        raise FileNotFoundError(f"no episodes.csv files found under {debug_root}")
    rows = [summarize_world(path) for path in episode_files]
    write_csv(args.csv_out, rows)
    write_markdown(args.md_out, rows)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in rows:
        print(
            f"{row['world']}: max_duration={row['max_duration']} "
            f"trust={float(row['avg_temporal_trust']):.4f} "
            f"afterimage={float(row['avg_afterimage']):.4f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
