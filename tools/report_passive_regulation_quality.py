from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OVERVIEW = ROOT / "docs" / "befunde" / "341_MILIEU_DRIFTQUALITAET.csv"
DEFAULT_WORLDS = ROOT / "docs" / "befunde" / "341_MILIEU_DRIFTQUALITAET_welten.csv"
DEFAULT_WORLD_METRICS = ROOT / "docs" / "befunde" / "342_MILIEU_DRIFT_WELTMERKMALE.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "344_PASSIVE_REGULATIONSQUALITAET_REPRODUKTION.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def _passive_quality_from_drift(row: dict[str, str]) -> str:
    drift = row.get("drift_quality", "") or ""
    top_quality = row.get("top_quality", "") or ""
    if drift == "eng_getragen":
        return "eng_getragen"
    if drift == "breit_driftend":
        return "breit_driftend"
    if drift == "stark_fragmentiert":
        return "fragmentiert"
    return _passive_quality_from_world_quality(top_quality)


def _passive_quality_from_world_quality(quality: str) -> str:
    if quality == "rekoppelnd_stabil":
        return "eng_getragen"
    if quality == "offen_stabil":
        return "offen_driftend"
    if quality in {"rekoppelnd_offen", "offen_rekoppelnd", "gemischt"}:
        return "breit_driftend"
    if quality in {"druckbruch", "bruchdominant", "druckuebergang", "bruchuebergang"}:
        return "fragmentiert"
    return "unbestimmt"


def _metrics_by_pair_world(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    return {(row.get("pair", "-") or "-", row.get("world", "-") or "-"): row for row in rows}


def _build_rows(
    overview_rows: list[dict[str, str]],
    world_rows: list[dict[str, str]],
    metric_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    overview_out: list[dict[str, object]] = []
    for row in overview_rows:
        overview_out.append(
            {
                "scope": "gesamt",
                "pair": row.get("pair", "-") or "-",
                "world": "-",
                "events": int(_float(row.get("events"))),
                "source_quality": row.get("drift_quality", "-") or "-",
                "top_quality": row.get("top_quality", "-") or "-",
                "share": _float(row.get("top_share")),
                "passive_regulation_quality": _passive_quality_from_drift(row),
                "contact_pressure": "",
                "contact_alignment": "",
                "mcm_rekopplung": "",
            }
        )

    metrics = _metrics_by_pair_world(metric_rows)
    world_out: list[dict[str, object]] = []
    for row in world_rows:
        pair = row.get("pair", "-") or "-"
        world = row.get("world", "-") or "-"
        metric = metrics.get((pair, world), {})
        quality = row.get("quality", "-") or "-"
        world_out.append(
            {
                "scope": "welt",
                "pair": pair,
                "world": world,
                "events": int(_float(row.get("events"))),
                "source_quality": quality,
                "top_quality": quality,
                "share": _float(row.get("share")),
                "passive_regulation_quality": _passive_quality_from_world_quality(quality),
                "contact_pressure": _float(metric.get("contact_pressure")),
                "contact_alignment": _float(metric.get("contact_alignment")),
                "mcm_rekopplung": _float(metric.get("mcm_rekopplung")),
            }
        )

    pair_quality_counts: dict[str, Counter[str]] = defaultdict(Counter)
    pair_world_counts: dict[str, set[str]] = defaultdict(set)
    for row in world_out:
        pair = str(row["pair"])
        pair_quality_counts[pair][str(row["passive_regulation_quality"])] += int(row["events"])
        pair_world_counts[pair].add(str(row["world"]))

    reproduction_out: list[dict[str, object]] = []
    for pair, counts in sorted(pair_quality_counts.items()):
        total = sum(counts.values())
        top_quality, top_events = counts.most_common(1)[0]
        reproduction_out.append(
            {
                "pair": pair,
                "worlds": len(pair_world_counts[pair]),
                "passive_qualities": len(counts),
                "top_passive_quality": top_quality,
                "top_share": top_events / max(1, total),
                "events": total,
                "quality_profile": "; ".join(f"{name}:{count}" for name, count in counts.most_common()),
            }
        )

    return overview_out, world_out, reproduction_out


def _write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6)
                    if isinstance(row.get(key), float)
                    else row.get(key, "")
                    for key in fields
                }
            )


def _write_outputs(
    overview_rows: list[dict[str, object]],
    world_rows: list[dict[str, object]],
    reproduction_rows: list[dict[str, object]],
    out_path: Path,
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    all_rows = overview_rows + world_rows
    fields = [
        "scope",
        "pair",
        "world",
        "events",
        "source_quality",
        "top_quality",
        "share",
        "passive_regulation_quality",
        "contact_pressure",
        "contact_alignment",
        "mcm_rekopplung",
    ]
    _write_csv(out_path.with_suffix(".csv"), all_rows, fields)
    _write_csv(
        out_path.with_name(out_path.stem + "_reproduktion.csv"),
        reproduction_rows,
        ["pair", "worlds", "passive_qualities", "top_passive_quality", "top_share", "events", "quality_profile"],
    )

    lines = [
        "# Passive Regulationsqualitaet Reproduktion",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die in 343 formulierten passiven Regulationsqualitaeten in den vorhandenen Milieu- und Driftbefunden wieder auftauchen.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Strategie und keine harte Runtime-Regel.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Bleiben passive Regulationsqualitaeten ueber Weltgruppen lesbar?",
        "2. Unterpruefung: Milieuqualitaeten aus 341 und Weltkopplung aus 342 in vier Innenfeldqualitaeten uebersetzen.",
        "3. Folgeschritt: pruefen, ob neue Welten dieselben Qualitaeten erweitern, verschieben oder fragmentieren.",
        "",
        "## Reproduktionsmatrix",
        "",
        "| Paar | Welten | Passive Qualitaeten | Top-Qualitaet | Anteil | Events | Profil |",
        "|---|---:|---:|---|---:|---:|---|",
    ]
    for row in reproduction_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["worlds"]),
                    str(row["passive_qualities"]),
                    str(row["top_passive_quality"]),
                    _fmt(float(row["top_share"])),
                    str(row["events"]),
                    str(row["quality_profile"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Gesamtlesung",
            "",
            "| Paar | Events | Driftqualitaet | Top-Milieu | Anteil | Passive Regulationsqualitaet |",
            "|---|---:|---|---|---:|---|",
        ]
    )
    for row in overview_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["events"]),
                    str(row["source_quality"]),
                    str(row["top_quality"]),
                    _fmt(float(row["share"])),
                    str(row["passive_regulation_quality"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Weltlesung",
            "",
            "| Paar | Welt | Events | Milieu | Anteil | Passive Qualitaet | Druck | Alignment | Rekopplung |",
            "|---|---|---:|---|---:|---|---:|---:|---:|",
        ]
    )
    for row in world_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["world"]),
                    str(row["events"]),
                    str(row["source_quality"]),
                    _fmt(float(row["share"])),
                    str(row["passive_regulation_quality"]),
                    _fmt(float(row["contact_pressure"])),
                    _fmt(float(row["contact_alignment"])),
                    _fmt(float(row["mcm_rekopplung"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die vier Qualitaeten sind in den vorhandenen Langweltbefunden lesbar, aber nicht gleich stabil.",
            "`1t5bcxp -> 183drjy` bleibt als Bewegung sichtbar und wird gesamt `breit_driftend` gelesen.",
            "In einzelnen Welten kippt dieselbe Bewegung zwischen `offen_driftend` und `eng_getragen`.",
            "`183drjy -> 1t5bcxp` bleibt deutlich fragmentierter und verteilt sich auf mehr Qualitaeten.",
            "",
            "Fachliche Lesart:",
            "",
            "```text",
            "MINI_DIO liest nicht nur Bewegung, sondern Tragart der Bewegung.",
            "Diese Tragart ist eine passive Innenfeldwahrnehmung.",
            "Sie darf nicht direkt in Handlung uebersetzt werden.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieselbe Qualitaetslesung auf eine neue Weltgruppe angewendet werden.",
            "Ziel ist zu pruefen, ob die Qualitaeten stabil mitwachsen oder ob neue passive Innenfeldqualitaeten entstehen.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build passive regulation quality reproduction report from milieu drift diagnostics.")
    parser.add_argument("--overview", default=str(DEFAULT_OVERVIEW))
    parser.add_argument("--worlds", default=str(DEFAULT_WORLDS))
    parser.add_argument("--world-metrics", default=str(DEFAULT_WORLD_METRICS))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    overview_rows, world_rows, reproduction_rows = _build_rows(
        _load_rows(_resolve(args.overview)),
        _load_rows(_resolve(args.worlds)),
        _load_rows(_resolve(args.world_metrics)),
    )
    _write_outputs(overview_rows, world_rows, reproduction_rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
