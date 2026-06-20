from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVENTS = ROOT / "docs" / "befunde" / "339_LANGWELT_STABILES_MILIEU_SEGMENTE_events.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "341_MILIEU_DRIFTQUALITAET.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _signature(row: dict[str, str]) -> str:
    return "->".join([row.get("before_class", "-") or "-", row.get("switch_class", "-") or "-", row.get("after_class", "-") or "-"])


def _quality(signature: str) -> str:
    parts = signature.split("->")
    counts = Counter(parts)
    if counts["rekoppelnde_lage"] == 3:
        return "rekoppelnd_stabil"
    if counts["offene_lage"] == 3:
        return "offen_stabil"
    if counts["druck_lage"] >= 1 and counts["bewegungsbruch"] >= 1:
        return "druckbruch"
    if counts["bewegungsbruch"] >= 2:
        return "bruchdominant"
    if counts["rekoppelnde_lage"] >= 2 and counts["bewegungsbruch"] == 0:
        return "rekoppelnd_offen"
    if counts["offene_lage"] >= 2 and counts["bewegungsbruch"] == 0:
        return "offen_rekoppelnd"
    if counts["druck_lage"] >= 1:
        return "druckuebergang"
    if counts["bewegungsbruch"] >= 1:
        return "bruchuebergang"
    return "gemischt"


def _summarize(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    pair_world_quality: dict[tuple[str, str, str], int] = Counter()
    pair_quality: dict[tuple[str, str], int] = Counter()
    pair_totals: Counter[str] = Counter()
    world_totals: Counter[tuple[str, str]] = Counter()

    for row in rows:
        pair = row.get("pair", "-") or "-"
        world = row.get("world", "-") or "-"
        quality = _quality(_signature(row))
        pair_quality[(pair, quality)] += 1
        pair_world_quality[(pair, world, quality)] += 1
        pair_totals[pair] += 1
        world_totals[(pair, world)] += 1

    pair_rows: list[dict[str, object]] = []
    qualities_by_pair: dict[str, set[str]] = defaultdict(set)
    worlds_by_pair: dict[str, set[str]] = defaultdict(set)
    for (pair, quality), count in pair_quality.items():
        qualities_by_pair[pair].add(quality)
        pair_rows.append(
            {
                "pair": pair,
                "quality": quality,
                "events": count,
                "share": count / max(1, pair_totals[pair]),
            }
        )
    for pair, world in world_totals:
        worlds_by_pair[pair].add(world)

    overview_rows: list[dict[str, object]] = []
    for pair, total in pair_totals.items():
        quality_counts = {quality: pair_quality[(pair, quality)] for quality in qualities_by_pair[pair]}
        top_quality, top_count = max(quality_counts.items(), key=lambda item: item[1])
        overview_rows.append(
            {
                "pair": pair,
                "events": total,
                "worlds": len(worlds_by_pair[pair]),
                "quality_count": len(qualities_by_pair[pair]),
                "top_quality": top_quality,
                "top_share": top_count / max(1, total),
                "drift_quality": _drift_quality(len(qualities_by_pair[pair]), top_count / max(1, total)),
            }
        )

    world_rows: list[dict[str, object]] = []
    for (pair, world, quality), count in pair_world_quality.items():
        world_rows.append(
            {
                "pair": pair,
                "world": world,
                "quality": quality,
                "events": count,
                "share": count / max(1, world_totals[(pair, world)]),
            }
        )
    return sorted(overview_rows, key=lambda row: str(row["pair"])), sorted(world_rows, key=lambda row: (str(row["pair"]), str(row["world"]), -int(row["events"])))


def _drift_quality(quality_count: int, top_share: float) -> str:
    if quality_count <= 2 and top_share >= 0.65:
        return "eng_getragen"
    if quality_count <= 4 and top_share >= 0.45:
        return "kontrolliert_variabel"
    if top_share >= 0.30:
        return "breit_driftend"
    return "stark_fragmentiert"


def _write_csv(overview_rows: list[dict[str, object]], world_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    overview_path = out_path.with_suffix(".csv")
    overview_fields = ["pair", "events", "worlds", "quality_count", "top_quality", "top_share", "drift_quality"]
    with overview_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=overview_fields)
        writer.writeheader()
        for row in overview_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in overview_fields})

    world_path = out_path.with_name(out_path.stem + "_welten.csv")
    world_fields = ["pair", "world", "quality", "events", "share"]
    with world_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=world_fields)
        writer.writeheader()
        for row in world_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in world_fields})


def _write_md(overview_rows: list[dict[str, object]], world_rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(overview_rows, world_rows, out_path)
    lines = [
        "# Milieu-Driftqualitaet",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest, ob dieselbe passive Feldbewegung in engen oder driftenden Kontaktmilieus erscheint.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Kann MINI_DIO Milieu-Drift als eigene Qualitaet lesen?",
        "2. Unterpruefung: gleiche Feldbewegung nach Signaturqualitaeten und Weltverteilung vergleichen.",
        "3. Folgeschritt: stabile und driftende Qualitaeten als passive Innenfeldwahrnehmung dokumentieren.",
        "",
        "## Uebersicht",
        "",
        "| Paar | Events | Welten | Qualitaeten | Top-Qualitaet | Anteil | Driftqualitaet |",
        "|---|---:|---:|---:|---|---:|---|",
    ]
    for row in overview_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["events"]),
                    str(row["worlds"]),
                    str(row["quality_count"]),
                    str(row["top_quality"]),
                    _fmt(float(row["top_share"])),
                    str(row["drift_quality"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Weltverteilung",
            "",
            "| Paar | Welt | Qualitaet | Events | Anteil |",
            "|---|---|---|---:|---:|",
        ]
    )
    for row in world_rows[:80]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["world"]),
                    str(row["quality"]),
                    str(row["events"]),
                    _fmt(float(row["share"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Langweltpruefung zeigt: dieselbe Feldbewegung kann in unterschiedlichen Milieus getragen werden.",
            "Das ist kein Widerspruch zur Wiederkehr, sondern eine Driftqualitaet.",
            "",
            "Fachliche Lesart:",
            "",
            "```text",
            "gleiche Feldbewegung + anderes Kontaktmilieu = Milieu-Drift",
            "Milieu-Drift ist eine passive Innenfeldqualitaet, keine Regelabweichung.",
            "```",
            "",
            "Damit kann MINI_DIO spaeter unterscheiden:",
            "",
            "- eng getragene Feldbewegung,",
            "- kontrolliert variable Feldbewegung,",
            "- breit driftende Feldbewegung,",
            "- stark fragmentierte Feldbewegung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Driftqualitaet auf Weltmerkmale zurueckgelegt werden.",
            "Dann wird sichtbar, welche Weltspannung eine Feldbewegung eng haelt oder in breite Drift fuehrt.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify milieu drift quality for passive MCM preview movements.")
    parser.add_argument("--events", default=str(DEFAULT_EVENTS))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()
    rows = _load_rows(_resolve(args.events))
    overview_rows, world_rows = _summarize(rows)
    _write_md(overview_rows, world_rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
