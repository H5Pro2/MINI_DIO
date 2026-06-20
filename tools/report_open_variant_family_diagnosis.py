from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "327_OFFENE_VARIANTE_FAMILIEN_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _role(row: dict[str, str]) -> str:
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _avg(rows: list[dict[str, object]], key: str) -> float:
    values = [float(row.get(key, 0.0) or 0.0) for row in rows]
    return fmean(values) if values else 0.0


def _dominant(rows: list[dict[str, object]], key: str) -> str:
    values = [str(row.get(key, "-") or "-") for row in rows]
    if not values:
        return "-"
    value, count = Counter(values).most_common(1)[0]
    return f"{value} ({count}/{len(values)})"


def _streaks(rows: list[dict[str, object]]) -> list[int]:
    ordered = sorted(rows, key=lambda row: int(row["tick"]))
    if not ordered:
        return []
    streaks: list[int] = []
    current = 1
    last_tick = int(ordered[0]["tick"])
    for row in ordered[1:]:
        tick = int(row["tick"])
        if tick == last_tick + 1:
            current += 1
        else:
            streaks.append(current)
            current = 1
        last_tick = tick
    streaks.append(current)
    return streaks


def _summarize_world(name: str, episodes_path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    raw_rows = _load_rows(episodes_path)
    rows: list[dict[str, object]] = []
    for raw in raw_rows:
        role = _role(raw)
        rows.append(
            {
                "world": name,
                "tick": int(_float(raw.get("tick"))),
                "role": role,
                "symbol_family": raw.get("symbol_family", "-") or "-",
                "mcm_preview": raw.get("mcm_field_episode_preview_symbol", "-") or "-",
                "effect_class": raw.get("passive_mcm_effect_class", "-") or "-",
                "meaning_state": raw.get("passive_inner_effect_meaning_state", "-") or "-",
                "rekopplung": _float(raw.get("mcm_rekopplung_quality")),
                "carry": _float(raw.get("mcm_carry_quality")),
                "strain": _float(raw.get("mcm_strain_quality")),
                "sensory": _float(raw.get("mcm_sensory_coupling")),
                "visual_gap": _float(raw.get("mcm_visual_field_gap")),
                "hearing_gap": _float(raw.get("mcm_hearing_field_gap")),
            }
        )

    open_rows = [row for row in rows if row["role"] == "offene_variante"]
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in open_rows:
        grouped[(str(row["mcm_preview"]), str(row["symbol_family"]))].append(row)

    family_rows: list[dict[str, object]] = []
    for (preview, symbol_family), items in sorted(grouped.items(), key=lambda item: len(item[1]), reverse=True):
        streaks = _streaks(items)
        family_rows.append(
            {
                "world": name,
                "mcm_preview": preview,
                "symbol_family": symbol_family,
                "count": len(items),
                "share_of_open": len(items) / max(1, len(open_rows)),
                "avg_rekopplung": _avg(items, "rekopplung"),
                "avg_carry": _avg(items, "carry"),
                "avg_strain": _avg(items, "strain"),
                "avg_sensory": _avg(items, "sensory"),
                "avg_visual_gap": _avg(items, "visual_gap"),
                "avg_hearing_gap": _avg(items, "hearing_gap"),
                "longest_streak": max(streaks) if streaks else 0,
                "streak_count": len(streaks),
            }
        )

    summary = {
        "world": name,
        "episodes": len(rows),
        "open_count": len(open_rows),
        "open_share": len(open_rows) / max(1, len(rows)),
        "open_family_count": len(grouped),
        "top_open_preview": _dominant(open_rows, "mcm_preview"),
        "top_open_symbol_family": _dominant(open_rows, "symbol_family"),
        "avg_open_rekopplung": _avg(open_rows, "rekopplung"),
        "avg_open_strain": _avg(open_rows, "strain"),
        "avg_open_sensory": _avg(open_rows, "sensory"),
        "longest_open_streak": max(_streaks(open_rows)) if open_rows else 0,
    }
    return family_rows, summary


def _preview_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["world"]), str(row["mcm_preview"]))].append(row)

    preview_rows: list[dict[str, object]] = []
    for (world, preview), items in sorted(grouped.items(), key=lambda item: (item[0][0], -len(item[1]))):
        preview_rows.append(
            {
                "world": world,
                "mcm_preview": preview,
                "count": sum(int(item["count"]) for item in items),
                "family_variants": len(items),
                "avg_rekopplung": _avg(items, "avg_rekopplung"),
                "avg_carry": _avg(items, "avg_carry"),
                "avg_strain": _avg(items, "avg_strain"),
                "avg_sensory": _avg(items, "avg_sensory"),
                "avg_visual_gap": _avg(items, "avg_visual_gap"),
                "avg_hearing_gap": _avg(items, "avg_hearing_gap"),
                "longest_streak": max(int(item["longest_streak"]) for item in items),
            }
        )
    return preview_rows


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "mcm_preview",
        "symbol_family",
        "count",
        "share_of_open",
        "avg_rekopplung",
        "avg_carry",
        "avg_strain",
        "avg_sensory",
        "avg_visual_gap",
        "avg_hearing_gap",
        "longest_streak",
        "streak_count",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key)
                    for key in fields
                }
            )


def _write_md(rows: list[dict[str, object]], summaries: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(rows, out_path)
    preview_rows = _preview_rows(rows)
    lines = [
        "# Offene Variante - Familien Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die offene Variante nur diffuse Uebergangszone ist oder eigene wiederkehrende Familien traegt.",
        "Sie bleibt passiv: keine Handlung, kein Gate, kein Entry-Signal.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Ist die offene Variante unreife Zwischenlage, normale Variationszone oder beginnende Bedeutungsinsel?",
        "2. Unterpruefung: offene Episoden nach MCM-Preview-Familie und `symbol_family` verdichten.",
        "3. Folgeschritt: wiederkehrende Familien gegen weitere Welten pruefen.",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Episoden | Offen | Familien | Top MCM-Preview | Top Symbolfamilie | Rekopplung | Strain | Sinneskopplung | laengste offene Serie |",
        "|---|---:|---:|---:|---|---|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["episodes"]),
                    _fmt(float(row["open_share"])),
                    str(row["open_family_count"]),
                    str(row["top_open_preview"]),
                    str(row["top_open_symbol_family"]),
                    _fmt(float(row["avg_open_rekopplung"])),
                    _fmt(float(row["avg_open_strain"])),
                    _fmt(float(row["avg_open_sensory"])),
                    str(row["longest_open_streak"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## MCM-Preview-Verdichtung",
            "",
            "| Welt | MCM-Preview | Anzahl | Symbolvarianten | Rekopplung | Strain | Sinneskopplung | laengste Serie |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in preview_rows[:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["mcm_preview"]),
                    str(row["count"]),
                    str(row["family_variants"]),
                    _fmt(float(row["avg_rekopplung"])),
                    _fmt(float(row["avg_strain"])),
                    _fmt(float(row["avg_sensory"])),
                    str(row["longest_streak"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Staerkste offene Familien",
            "",
            "| Welt | MCM-Preview | Symbolfamilie | Anzahl | Anteil an Offen | Rekopplung | Strain | Sinneskopplung | laengste Serie |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(rows, key=lambda item: (str(item["world"]), -int(item["count"])))[:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["mcm_preview"]),
                    str(row["symbol_family"]),
                    str(row["count"]),
                    _fmt(float(row["share_of_open"])),
                    _fmt(float(row["avg_rekopplung"])),
                    _fmt(float(row["avg_strain"])),
                    _fmt(float(row["avg_sensory"])),
                    str(row["longest_streak"]),
                ]
            )
            + " |"
        )

    shared_previews = Counter(str(row["mcm_preview"]) for row in preview_rows)
    shared = [item for item, count in shared_previews.items() if item != "-" and count > 1]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Weltuebergreifend wiederkehrende offene MCM-Preview-Familien: {', '.join(f'`{item}`' for item in sorted(shared)) or '-'}",
            "",
            "Diese Datei ist eine Messmatrix. Die fachliche Deutung wird nach der Pruefung ergänzt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird bewertet, ob die offene Variante eine eigene stabile Bedeutungsnaehe zeigt oder nur Rand/Übergang zwischen Zentrum und Kippnaehe ist.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for name, episodes_text in args.world:
        rows, summary = _summarize_world(name, _resolve(episodes_text))
        all_rows.extend(rows)
        summaries.append(summary)

    out = args.out if args.out.is_absolute() else ROOT / args.out
    _write_md(all_rows, summaries, out)
    print(f"wrote {out}")
    print(f"wrote {out.with_suffix('.csv')}")


if __name__ == "__main__":
    main()
