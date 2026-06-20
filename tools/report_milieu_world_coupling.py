from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVENTS = ROOT / "docs" / "befunde" / "339_LANGWELT_STABILES_MILIEU_SEGMENTE_events.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "342_MILIEU_DRIFT_WELTMERKMALE.md"


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


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _has_value(row: dict[str, str], name: str) -> bool:
    value = row.get(name)
    return value is not None and str(value).strip() != ""


def _contact_pressure(row: dict[str, str]) -> float:
    if _has_value(row, "rezeptor_contact_pressure"):
        return _float(row.get("rezeptor_contact_pressure"))
    if _has_value(row, "mcm_feldwirkung_mcm_tension"):
        return abs(_float(row.get("mcm_feldwirkung_mcm_tension")))
    if _has_value(row, "fuehlen_mcm_tension"):
        return abs(_float(row.get("fuehlen_mcm_tension")))
    return _float(row.get("mcm_strain_quality"))


def _contact_alignment(row: dict[str, str]) -> float:
    if _has_value(row, "rezeptor_contact_alignment"):
        return _float(row.get("rezeptor_contact_alignment"))
    if _has_value(row, "mcm_feldwirkung_mcm_coherence"):
        return max(0.0, min(1.0, (_float(row.get("mcm_feldwirkung_mcm_coherence")) + 3.0) / 6.0))
    if _has_value(row, "fuehlen_mcm_coherence"):
        return max(0.0, min(1.0, (_float(row.get("fuehlen_mcm_coherence")) + 3.0) / 6.0))
    return _float(row.get("mcm_rekopplung_quality"))


def _load_csv(path: Path) -> list[dict[str, str]]:
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


def _world_metrics(path: Path) -> dict[str, float]:
    rows = _load_csv(path)
    return {
        "ticks": float(len(rows)),
        "form_change": _mean([abs(_float(row.get("sehen_form_change"))) for row in rows]),
        "form_stability": _mean([_float(row.get("sehen_form_stability")) for row in rows]),
        "energy_shift": _mean([abs(_float(row.get("hoeren_energy_shift"))) for row in rows]),
        "energy_tone": _mean([abs(_float(row.get("hoeren_energy_tone"))) for row in rows]),
        "contact_pressure": _mean([_contact_pressure(row) for row in rows]),
        "contact_alignment": _mean([_contact_alignment(row) for row in rows]),
        "mcm_strain": _mean([_float(row.get("mcm_strain_quality")) for row in rows]),
        "mcm_rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in rows]),
    }


def _summarize(events: list[dict[str, str]], world_paths: dict[str, Path]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for event in events:
        grouped[(event.get("pair", "-") or "-", event.get("world", "-") or "-")].append(event)

    rows: list[dict[str, object]] = []
    for (pair, world), items in sorted(grouped.items()):
        if world not in world_paths:
            continue
        qualities = Counter(_quality(_signature(item)) for item in items)
        top_quality, top_events = qualities.most_common(1)[0]
        metrics = _world_metrics(world_paths[world])
        rows.append(
            {
                "pair": pair,
                "world": world,
                "events": len(items),
                "top_quality": top_quality,
                "top_share": top_events / max(1, len(items)),
                "quality_count": len(qualities),
                **metrics,
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "pair",
        "world",
        "events",
        "top_quality",
        "top_share",
        "quality_count",
        "ticks",
        "form_change",
        "form_stability",
        "energy_shift",
        "energy_tone",
        "contact_pressure",
        "contact_alignment",
        "mcm_strain",
        "mcm_rekopplung",
    ]
    with out_path.with_suffix(".csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in fields})


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    lines = [
        "# Milieu-Drift Und Weltmerkmale",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt Milieu-Driftqualitaeten auf Weltmerkmale zurueck.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Weltspannung haelt eine Feldbewegung eng oder fuehrt sie in Drift?",
        "2. Unterpruefung: Top-Milieuqualitaet je Welt mit Formbruch, Energiebruch, Druck, Alignment, Strain und Rekopplung vergleichen.",
        "3. Folgeschritt: daraus passive Regulationswahrnehmung ableiten, nicht Regeln.",
        "",
        "## Weltmatrix",
        "",
        "| Paar | Welt | Events | Top-Qualitaet | Anteil | Qualitaeten | Formbruch | Energiebruch | Druck | Alignment | Strain | Rekopplung |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["world"]),
                    str(row["events"]),
                    str(row["top_quality"]),
                    _fmt(float(row["top_share"])),
                    str(row["quality_count"]),
                    _fmt(float(row["form_change"])),
                    _fmt(float(row["energy_shift"])),
                    _fmt(float(row["contact_pressure"])),
                    _fmt(float(row["contact_alignment"])),
                    _fmt(float(row["mcm_strain"])),
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
            "Die Tabelle trennt Weltspannung von Feldbewegung.",
            "Eine gleiche Feldbewegung kann je nach Weltmilieu rekoppelnd, offen oder fragmentiert erscheinen.",
            "",
            "Wichtig ist die vorsichtige Lesart:",
            "",
            "```text",
            "Weltmerkmale erklaeren Milieu-Neigung, aber erzwingen keine Feldbewegung.",
            "```",
            "",
            "Damit bleibt MINI_DIO passiv und organisch: Weltkontakt wird als Milieu gelesen, nicht als Regel.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte aus diesen Befunden eine kleine passive Regulationswahrnehmung formuliert werden.",
            "Sie beschreibt nur Innenfeldqualitaeten wie eng getragen, offen driftend und fragmentiert, ohne Handlung auszufuehren.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Join passive milieu drift qualities with world-level sensory/MCM metrics.")
    parser.add_argument("--events", default=str(DEFAULT_EVENTS))
    parser.add_argument("--world", nargs=2, action="append", metavar=("NAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    world_paths = {name: _resolve(path_text) for name, path_text in args.world}
    for path in world_paths.values():
        if not path.exists():
            raise FileNotFoundError(path)
    rows = _summarize(_load_csv(_resolve(args.events)), world_paths)
    _write_md(rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
