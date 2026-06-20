from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE.md"


TARGET_PAIRS = {
    "dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy",
    "dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp",
    "dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp",
    "dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk",
}


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


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=lambda row: int(_float(row.get("tick"))))


def _preview(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    return row.get("mcm_field_episode_preview_symbol", "-") or "-"


def _role(row: dict[str, str] | None) -> str:
    if row is None:
        return "-"
    effect_class = str(row.get("passive_mcm_effect_class", "-") or "-")
    awareness = str(row.get("passive_inner_effect_awareness_state", "-") or "-")
    if effect_class == "stabil" or awareness == "inner_effect_stable":
        return "zentrum_stabil"
    if effect_class in {"kippend", "gespannt"}:
        return "spannungsrand_kippnaehe"
    if effect_class in {"tragend_unruhig", "diffus"}:
        return "offene_variante"
    return "unbestimmt"


def _axis(row: dict[str, str], name: str) -> float:
    return _float(row.get(name))


def _has_value(row: dict[str, str], name: str) -> bool:
    value = row.get(name)
    return value is not None and str(value).strip() != ""


def _contact_pressure(row: dict[str, str]) -> float:
    if _has_value(row, "rezeptor_contact_pressure"):
        return _axis(row, "rezeptor_contact_pressure")
    if _has_value(row, "mcm_feldwirkung_mcm_tension"):
        return abs(_axis(row, "mcm_feldwirkung_mcm_tension"))
    if _has_value(row, "fuehlen_mcm_tension"):
        return abs(_axis(row, "fuehlen_mcm_tension"))
    return _axis(row, "mcm_strain_quality")


def _contact_alignment(row: dict[str, str]) -> float:
    if _has_value(row, "rezeptor_contact_alignment"):
        return _axis(row, "rezeptor_contact_alignment")
    if _has_value(row, "mcm_feldwirkung_mcm_coherence"):
        return max(0.0, min(1.0, (_axis(row, "mcm_feldwirkung_mcm_coherence") + 3.0) / 6.0))
    if _has_value(row, "fuehlen_mcm_coherence"):
        return max(0.0, min(1.0, (_axis(row, "fuehlen_mcm_coherence") + 3.0) / 6.0))
    return _axis(row, "mcm_rekopplung_quality")


def _phase(event_idx: int, idx: int) -> str:
    if idx < event_idx:
        return "vorher"
    if idx == event_idx:
        return "wechsel"
    return "nachher"


def _classify_segment(values: dict[str, float]) -> str:
    pressure = values["rezeptor_contact_pressure"]
    alignment = values["rezeptor_contact_alignment"]
    rekopplung = values["mcm_rekopplung_quality"]
    strain = values["mcm_strain_quality"]
    energy_shift = abs(values["hoeren_energy_shift"])
    form_change = abs(values["sehen_form_change"])
    stability = values["sehen_form_stability"]

    if rekopplung >= 0.62 and pressure <= 0.22 and alignment >= 0.70:
        return "rekoppelnde_lage"
    if pressure >= 0.32 or strain >= 0.28:
        return "druck_lage"
    if form_change >= 0.45 or energy_shift >= 0.45:
        return "bewegungsbruch"
    if stability >= 0.58 and alignment >= 0.62:
        return "gehaltene_form"
    return "offene_lage"


def _event_values(rows: list[dict[str, str]], event_idx: int, radius: int) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    for idx in range(max(0, event_idx - radius), min(len(rows), event_idx + radius + 1)):
        row = rows[idx]
        values = {
            "sehen_form_flow": _axis(row, "sehen_form_flow"),
            "sehen_form_stability": _axis(row, "sehen_form_stability"),
            "sehen_form_change": _axis(row, "sehen_form_change"),
            "hoeren_energy_tone": _axis(row, "hoeren_energy_tone"),
            "hoeren_energy_shift": _axis(row, "hoeren_energy_shift"),
            "rezeptor_contact_pressure": _contact_pressure(row),
            "rezeptor_contact_alignment": _contact_alignment(row),
            "mcm_carry_quality": _axis(row, "mcm_carry_quality"),
            "mcm_strain_quality": _axis(row, "mcm_strain_quality"),
            "mcm_rekopplung_quality": _axis(row, "mcm_rekopplung_quality"),
        }
        items.append(
            {
                "tick": int(_float(row.get("tick"))),
                "phase": _phase(event_idx, idx),
                "role": _role(row),
                "preview": _preview(row),
                "segment_class": _classify_segment(values),
                **values,
            }
        )
    return items


def _collect(world: str, episodes_path: Path, radius: int, target_pairs: set[str]) -> list[dict[str, object]]:
    rows = _load_rows(episodes_path)
    events: list[dict[str, object]] = []
    for idx in range(1, len(rows)):
        pair = f"{_preview(rows[idx - 1])}->{_preview(rows[idx])}"
        if pair not in target_pairs:
            continue
        segment_items = _event_values(rows, idx, radius)
        for item in segment_items:
            events.append({"world": world, "pair": pair, "event_tick": int(_float(rows[idx].get("tick"))), **item})
    return events


def _summaries(events: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for event in events:
        grouped[(str(event["pair"]), str(event["phase"]))].append(event)

    phase_rows: list[dict[str, object]] = []
    for (pair, phase), items in sorted(grouped.items()):
        phase_rows.append(
            {
                "pair": pair,
                "phase": phase,
                "samples": len(items),
                "worlds": len({str(item["world"]) for item in items}),
                "dominant_segment": Counter(str(item["segment_class"]) for item in items).most_common(1)[0][0],
                "dominant_role": Counter(str(item["role"]) for item in items).most_common(1)[0][0],
                "form_stability": _mean([float(item["sehen_form_stability"]) for item in items]),
                "form_change": _mean([abs(float(item["sehen_form_change"])) for item in items]),
                "energy_shift": _mean([abs(float(item["hoeren_energy_shift"])) for item in items]),
                "contact_pressure": _mean([float(item["rezeptor_contact_pressure"]) for item in items]),
                "contact_alignment": _mean([float(item["rezeptor_contact_alignment"]) for item in items]),
                "mcm_strain": _mean([float(item["mcm_strain_quality"]) for item in items]),
                "mcm_rekopplung": _mean([float(item["mcm_rekopplung_quality"]) for item in items]),
            }
        )

    event_grouped: dict[tuple[str, str, int], list[dict[str, object]]] = defaultdict(list)
    for event in events:
        event_grouped[(str(event["world"]), str(event["pair"]), int(event["event_tick"]))].append(event)
    event_rows: list[dict[str, object]] = []
    for (world, pair, event_tick), items in sorted(event_grouped.items())[:200]:
        before = [item for item in items if item["phase"] == "vorher"]
        after = [item for item in items if item["phase"] == "nachher"]
        switch = [item for item in items if item["phase"] == "wechsel"]
        event_rows.append(
            {
                "world": world,
                "pair": pair,
                "event_tick": event_tick,
                "before_class": Counter(str(item["segment_class"]) for item in before).most_common(1)[0][0] if before else "-",
                "switch_class": Counter(str(item["segment_class"]) for item in switch).most_common(1)[0][0] if switch else "-",
                "after_class": Counter(str(item["segment_class"]) for item in after).most_common(1)[0][0] if after else "-",
                "pressure_delta": (_mean([float(item["rezeptor_contact_pressure"]) for item in after]) - _mean([float(item["rezeptor_contact_pressure"]) for item in before])) if before and after else 0.0,
                "rekopplung_delta": (_mean([float(item["mcm_rekopplung_quality"]) for item in after]) - _mean([float(item["mcm_rekopplung_quality"]) for item in before])) if before and after else 0.0,
            }
        )
    return phase_rows, event_rows


def _write_csv(phase_rows: list[dict[str, object]], event_rows: list[dict[str, object]], out_path: Path) -> None:
    phase_path = out_path.with_suffix(".csv")
    phase_fields = [
        "pair",
        "phase",
        "samples",
        "worlds",
        "dominant_segment",
        "dominant_role",
        "form_stability",
        "form_change",
        "energy_shift",
        "contact_pressure",
        "contact_alignment",
        "mcm_strain",
        "mcm_rekopplung",
    ]
    phase_path.parent.mkdir(parents=True, exist_ok=True)
    with phase_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=phase_fields)
        writer.writeheader()
        for row in phase_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in phase_fields})

    event_path = out_path.with_name(out_path.stem + "_events.csv")
    event_fields = ["world", "pair", "event_tick", "before_class", "switch_class", "after_class", "pressure_delta", "rekopplung_delta"]
    with event_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=event_fields)
        writer.writeheader()
        for row in event_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in event_fields})


def _write_md(phase_rows: list[dict[str, object]], event_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(phase_rows, event_rows, out_path)
    lines = [
        "# Bewegungsarten Rohwelt-Segmente",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose legt validierte MCM-Preview-Bewegungen neben ihre lokalen Rohwelt- und Rezeptorsegmente.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Welt-/Rezeptorlage begleitet eine passive Feldbewegung?",
        "2. Unterpruefung: vor, waehrend und nach stabilen Uebergangspaaren vergleichen.",
        "3. Folgeschritt: daraus passive Ausloesemilieus lesen, nicht Handlungsregeln.",
        "",
        "## Phasenmatrix",
        "",
        "| Paar | Phase | Samples | Welten | Segment | Rolle | Formstabilitaet | Formbruch | Energiebruch | Druck | Alignment | Strain | Rekopplung |",
        "|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in phase_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["phase"]),
                    str(row["samples"]),
                    str(row["worlds"]),
                    str(row["dominant_segment"]),
                    str(row["dominant_role"]),
                    _fmt(float(row["form_stability"])),
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
            "## Ereignislupe",
            "",
            "| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |",
            "|---|---|---:|---|---|---|---:|---:|",
        ]
    )
    for row in event_rows[:60]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["pair"]),
                    str(row["event_tick"]),
                    str(row["before_class"]),
                    str(row["switch_class"]),
                    str(row["after_class"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Rohwelt-Segmentlupe beschreibt das Milieu einer Feldbewegung.",
            "Sie sagt nicht: Wenn dieses Segment kommt, dann muss diese Bewegung folgen.",
            "",
            "Fachlich wichtig ist die Trennung:",
            "",
            "```text",
            "Rohwelt/Rezeptorlage = Kontaktmilieu",
            "MCM-Preview-Wechsel = passive Feldbewegung",
            "```",
            "",
            "Damit bleibt die Diagnose organisch: Weltkontakt wird gelesen, aber nicht als Regel gesetzt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die besten Milieus auf Wiederkehr und Drift geprueft werden.",
            "Dann wird sichtbar, ob eine Feldbewegung an eine konkrete Weltlage gebunden ist oder mehrere Milieus tragen kann.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect raw/receptor segments around validated MCM preview transitions.")
    parser.add_argument("--world", nargs=2, action="append", metavar=("NAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--pair", action="append", default=[])
    parser.add_argument("--radius", type=int, default=2)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    target_pairs = set(args.pair) if args.pair else set(TARGET_PAIRS)
    events: list[dict[str, object]] = []
    for world_name, path_text in args.world:
        path = _resolve(path_text)
        if not path.exists():
            raise FileNotFoundError(path)
        events.extend(_collect(world_name, path, args.radius, target_pairs))
    phase_rows, event_rows = _summaries(events)
    _write_md(phase_rows, event_rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
