from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _quantile(values: list[float], fraction: float) -> float:
    clean = sorted(value for value in values if value == value)
    if not clean:
        return 0.0
    idx = min(len(clean) - 1, max(0, int(round((len(clean) - 1) * fraction))))
    return clean[idx]


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _label_visual(row: dict[str, str]) -> str:
    stability = _safe_float(row.get("sehen_form_stability"))
    change = _safe_float(row.get("sehen_form_change"))
    flow = _safe_float(row.get("sehen_form_flow"))
    sharpness = _safe_float(row.get("perception_visual_sharpness"))
    blur = _safe_float(row.get("perception_visual_blur"))
    if stability >= max(change, 0.34) and sharpness >= blur:
        return "sichtbar_stabile_form"
    if change > stability and change >= 0.30:
        return "sichtbarer_formwechsel"
    if abs(flow) >= 0.24:
        return "gerichteter_formfluss"
    if blur > sharpness:
        return "unscharfe_formaufnahme"
    return "offene_formaufnahme"


def _label_tone(row: dict[str, str]) -> str:
    tone = _safe_float(row.get("hoeren_energy_tone"))
    shift = _safe_float(row.get("hoeren_energy_shift"))
    loudness = _safe_float(row.get("perception_auditory_loudness"))
    softening = _safe_float(row.get("perception_auditory_softening"))
    if loudness >= 0.62 and abs(shift) >= 0.16:
        return "laute_wechselnde_energie"
    if loudness >= 0.62:
        return "laute_energie"
    if softening > loudness and tone < 0.35:
        return "gedaempfte_energie"
    if abs(shift) >= 0.16:
        return "tonaler_wechsel"
    return "ruhige_energie"


def _label_tension(row: dict[str, str]) -> str:
    intake = _safe_float(row.get("perception_adapted_field_intake_pressure"))
    raw_intake = _safe_float(row.get("perception_raw_field_intake_pressure"))
    felt = _safe_float(row.get("perception_felt_pressure"))
    tension = _safe_float(row.get("mcm_feldwirkung_mcm_tension"))
    relaxation = _safe_float(row.get("perception_felt_relaxation"))
    pressure = max(intake, raw_intake, felt, tension)
    if pressure >= 0.62 and relaxation < pressure:
        return "hohe_weltspannung"
    if pressure >= 0.38:
        return "mittlere_weltspannung"
    if relaxation > pressure:
        return "entlastete_weltspannung"
    return "niedrige_weltspannung"


def _is_recoupling_binding(row: dict[str, str], *, rekopplung_floor: float, strain_ceiling: float) -> bool:
    rekopplung = max(
        _safe_float(row.get("mcm_rekopplung_quality")),
        _safe_float(row.get("passive_inner_effect_rekopplung")),
    )
    strain = max(
        _safe_float(row.get("mcm_strain_quality")),
        _safe_float(row.get("passive_inner_effect_strain")),
    )
    effect = str(row.get("passive_mcm_effect_class", "") or "")
    state = str(row.get("passive_inner_effect_awareness_state", "") or "")
    return (
        rekopplung >= rekopplung_floor
        and strain <= strain_ceiling
        and ("stabil" in effect or "stable" in state or rekopplung > 0.0)
    )


def _is_fragmentation_load(row: dict[str, str], *, strain_floor: float, rekopplung_ceiling: float) -> bool:
    rekopplung = max(
        _safe_float(row.get("mcm_rekopplung_quality")),
        _safe_float(row.get("passive_inner_effect_rekopplung")),
    )
    strain = max(
        _safe_float(row.get("mcm_strain_quality")),
        _safe_float(row.get("passive_inner_effect_strain")),
    )
    carry = max(
        _safe_float(row.get("mcm_carry_quality")),
        _safe_float(row.get("passive_inner_effect_carry")),
    )
    return strain >= strain_floor and rekopplung <= rekopplung_ceiling and strain >= carry


def _source_name(path: Path) -> str:
    parts = path.parts
    if "debug" in parts:
        idx = parts.index("debug")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return path.parent.name


def _profile_episode(path: Path, lookback: int, target: str) -> dict[str, object] | None:
    rows = _load_rows(path)
    if len(rows) < lookback + 2:
        return None

    recoupling_values = [
        max(_safe_float(row.get("mcm_rekopplung_quality")), _safe_float(row.get("passive_inner_effect_rekopplung")))
        for row in rows
    ]
    strain_values = [
        max(_safe_float(row.get("mcm_strain_quality")), _safe_float(row.get("passive_inner_effect_strain")))
        for row in rows
    ]
    recoupling_floor = _quantile(recoupling_values, 0.80)
    strain_ceiling = _quantile(strain_values, 0.55)
    strain_floor = _quantile(strain_values, 0.80)
    recoupling_ceiling = _quantile(recoupling_values, 0.55)
    baselines = {
        "sehen_form_stability": _avg([_safe_float(row.get("sehen_form_stability")) for row in rows]),
        "sehen_form_change": _avg([_safe_float(row.get("sehen_form_change")) for row in rows]),
        "hoeren_energy_tone": _avg([_safe_float(row.get("hoeren_energy_tone")) for row in rows]),
        "hoeren_energy_shift_abs": _avg([abs(_safe_float(row.get("hoeren_energy_shift"))) for row in rows]),
        "perception_auditory_loudness": _avg([_safe_float(row.get("perception_auditory_loudness")) for row in rows]),
        "perception_visual_sharpness": _avg([_safe_float(row.get("perception_visual_sharpness")) for row in rows]),
        "perception_felt_pressure": _avg([_safe_float(row.get("perception_felt_pressure")) for row in rows]),
        "perception_adapted_field_intake_pressure": _avg(
            [_safe_float(row.get("perception_adapted_field_intake_pressure")) for row in rows]
        ),
        "mcm_feldwirkung_mcm_tension": _avg([_safe_float(row.get("mcm_feldwirkung_mcm_tension")) for row in rows]),
    }

    events: list[int] = []
    for idx, row in enumerate(rows):
        if idx < lookback:
            continue
        if target == "fragmentation":
            is_target = _is_fragmentation_load(row, strain_floor=strain_floor, rekopplung_ceiling=recoupling_ceiling)
        else:
            is_target = _is_recoupling_binding(row, rekopplung_floor=recoupling_floor, strain_ceiling=strain_ceiling)
        if is_target:
            events.append(idx)

    if not events:
        return None

    values: dict[str, list[float]] = defaultdict(list)
    visuals: Counter[str] = Counter()
    tones: Counter[str] = Counter()
    tensions: Counter[str] = Counter()
    source = _source_name(path)

    for idx in events:
        window = rows[max(0, idx - lookback) : idx]
        target = rows[idx]
        for row in window:
            visuals.update([_label_visual(row)])
            tones.update([_label_tone(row)])
            tensions.update([_label_tension(row)])
            for key in (
                "sehen_form_flow",
                "sehen_form_stability",
                "sehen_form_change",
                "hoeren_energy_tone",
                "hoeren_energy_shift",
                "perception_auditory_loudness",
                "perception_visual_sharpness",
                "perception_felt_pressure",
                "perception_adapted_field_intake_pressure",
                "mcm_feldwirkung_mcm_coherence",
                "mcm_feldwirkung_mcm_tension",
                "mcm_feldwirkung_mcm_asymmetry",
            ):
                values[key].append(_safe_float(row.get(key)))
        values["target_rekopplung"].append(
            max(
                _safe_float(target.get("mcm_rekopplung_quality")),
                _safe_float(target.get("passive_inner_effect_rekopplung")),
            )
        )
        values["target_strain"].append(
            max(
                _safe_float(target.get("mcm_strain_quality")),
                _safe_float(target.get("passive_inner_effect_strain")),
            )
        )

    return {
        **PASSIVE_FLAGS,
        "source": source,
        "episode_file": str(path),
        "rows": len(rows),
        "lookback_ticks": lookback,
        "target": target,
        "target_events": len(events),
        "recoupling_events": len(events),
        "recoupling_floor_used": round(recoupling_floor, 6),
        "strain_ceiling_used": round(strain_ceiling, 6),
        "strain_floor_used": round(strain_floor, 6),
        "recoupling_ceiling_used": round(recoupling_ceiling, 6),
        "dominant_visual_form_before": visuals.most_common(1)[0][0],
        "dominant_tone_before": tones.most_common(1)[0][0],
        "dominant_world_tension_before": tensions.most_common(1)[0][0],
        "visual_mix": " | ".join(f"{key}:{value}" for key, value in visuals.most_common(4)),
        "tone_mix": " | ".join(f"{key}:{value}" for key, value in tones.most_common(4)),
        "tension_mix": " | ".join(f"{key}:{value}" for key, value in tensions.most_common(4)),
        "avg_seen_stability_before": round(_avg(values["sehen_form_stability"]), 6),
        "avg_seen_change_before": round(_avg(values["sehen_form_change"]), 6),
        "avg_heard_energy_tone_before": round(_avg(values["hoeren_energy_tone"]), 6),
        "avg_heard_energy_shift_before": round(_avg(values["hoeren_energy_shift"]), 6),
        "avg_auditory_loudness_before": round(_avg(values["perception_auditory_loudness"]), 6),
        "avg_visual_sharpness_before": round(_avg(values["perception_visual_sharpness"]), 6),
        "avg_felt_pressure_before": round(_avg(values["perception_felt_pressure"]), 6),
        "avg_adapted_field_intake_before": round(_avg(values["perception_adapted_field_intake_pressure"]), 6),
        "avg_mcm_coherence_before": round(_avg(values["mcm_feldwirkung_mcm_coherence"]), 6),
        "avg_mcm_tension_before": round(_avg(values["mcm_feldwirkung_mcm_tension"]), 6),
        "avg_mcm_asymmetry_before": round(_avg(values["mcm_feldwirkung_mcm_asymmetry"]), 6),
        "avg_target_rekopplung": round(_avg(values["target_rekopplung"]), 6),
        "avg_target_strain": round(_avg(values["target_strain"]), 6),
        "delta_seen_stability_vs_world": round(_avg(values["sehen_form_stability"]) - baselines["sehen_form_stability"], 6),
        "delta_seen_change_vs_world": round(_avg(values["sehen_form_change"]) - baselines["sehen_form_change"], 6),
        "delta_energy_tone_vs_world": round(_avg(values["hoeren_energy_tone"]) - baselines["hoeren_energy_tone"], 6),
        "delta_energy_shift_abs_vs_world": round(
            _avg([abs(value) for value in values["hoeren_energy_shift"]]) - baselines["hoeren_energy_shift_abs"], 6
        ),
        "delta_loudness_vs_world": round(_avg(values["perception_auditory_loudness"]) - baselines["perception_auditory_loudness"], 6),
        "delta_visual_sharpness_vs_world": round(
            _avg(values["perception_visual_sharpness"]) - baselines["perception_visual_sharpness"], 6
        ),
        "delta_felt_pressure_vs_world": round(_avg(values["perception_felt_pressure"]) - baselines["perception_felt_pressure"], 6),
        "delta_adapted_field_intake_vs_world": round(
            _avg(values["perception_adapted_field_intake_pressure"])
            - baselines["perception_adapted_field_intake_pressure"],
            6,
        ),
        "delta_mcm_tension_vs_world": round(_avg(values["mcm_feldwirkung_mcm_tension"]) - baselines["mcm_feldwirkung_mcm_tension"], 6),
    }


def _collect(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(path.rglob("episodes.csv"))
        else:
            files.extend(Path().glob(str(path)))
    return sorted(set(files))


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _target_title(target: str) -> str:
    if target == "fragmentation":
        return "belastete Fragmentierung"
    return "Rekopplungsbindung"


def _target_prepositional(target: str) -> str:
    if target == "fragmentation":
        return "belasteter Fragmentierung"
    return "Rekopplungsbindung"


def _target_explanation(target: str) -> str:
    if target == "fragmentation":
        return "belasteten Fragmentierungszustandsmomenten"
    return "rekoppelnden Zustandsmomenten"


def _write_md(path: Path, rows: list[dict[str, object]], target: str) -> None:
    total_events = sum(int(row["target_events"]) for row in rows)
    visual = Counter()
    tone = Counter()
    tension = Counter()
    for row in rows:
        visual.update([str(row["dominant_visual_form_before"])])
        tone.update([str(row["dominant_tone_before"])])
        tension.update([str(row["dominant_world_tension_before"])])

    lines = [
        f"# Rohwelt-Ruecklesung vor {_target_prepositional(target)}",
        "",
        "## Zweck",
        "",
        f"Diese Diagnose liest passiv zurueck, welche Weltspannung, Ton-/Energieform und sichtbare Form vor spaeterer {_target_prepositional(target)} lag.",
        f"Sie nutzt Episode-Dateien und betrachtet das Vorfenster vor {_target_explanation(target)}.",
        "",
        "## Methodische Grenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "- Der Zielzustand wird pro Lauf aus der jeweiligen Verteilung gelesen, nicht als feste globale Schwelle",
        "",
        "## Befund",
        "",
        f"- Ausgewertete Laeufe: `{len(rows)}`",
        f"- Zielereignisse: `{total_events}`",
        f"- Dominante sichtbare Vorformen: `{ ' | '.join(f'{k}:{v}' for k, v in visual.most_common(4)) }`",
        f"- Dominante Ton-/Energie-Vorformen: `{ ' | '.join(f'{k}:{v}' for k, v in tone.most_common(4)) }`",
        f"- Dominante Weltspannungs-Vorformen: `{ ' | '.join(f'{k}:{v}' for k, v in tension.most_common(4)) }`",
        "",
        "## Laufprofile",
        "",
        "| Quelle | Events | Sicht davor | Ton davor | Spannung davor | Formstabilitaet | dForm | Energie-Ton | dTon | Feldaufnahme | dFeld | Ziel-Rekopplung | Ziel-Strain |",
        "|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in sorted(rows, key=lambda item: int(item["target_events"]), reverse=True)[:40]:
        lines.append(
            f"| `{row['source']}` | {row['target_events']} | `{row['dominant_visual_form_before']}` | "
            f"`{row['dominant_tone_before']}` | `{row['dominant_world_tension_before']}` | "
            f"{row['avg_seen_stability_before']} | {row['delta_seen_stability_vs_world']} | "
            f"{row['avg_heard_energy_tone_before']} | {row['delta_energy_tone_vs_world']} | "
            f"{row['avg_adapted_field_intake_before']} | {row['delta_adapted_field_intake_vs_world']} | "
            f"{row['avg_target_rekopplung']} | {row['avg_target_strain']} |"
        )

    lines.extend(
        [
            "",
            "## Arbeitsableitung",
            "",
            "```text",
            f"Spaetere Zielbindung ({_target_title(target)}) entsteht nicht aus einem einzelnen Rohwert.",
            "Ruecklesbar ist ein Vorfeld aus sichtbarer Formlage, tonaler Energieform und regulierter Feldaufnahme.",
            "Die relativen Delta-Spalten zeigen, ob dieses Vorfeld gegen die jeweilige Weltbasis abweicht.",
            "Damit liegt die Ursache nicht direkt in der Rohwelt, sondern in der Art, wie die Rohwelt vorher sinnlich aufgenommen wurde.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten Rekopplungs- und Fragmentierungsruecklesung direkt nebeneinander gelegt werden.",
            "Dann wird sichtbar, welche Vorwelt eher Bindung vorbereitet und welche eher Last/Fragmentierung vorbereitet.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, type=Path)
    parser.add_argument("--lookback", type=int, default=6)
    parser.add_argument("--target", choices=["recoupling", "fragmentation"], default="recoupling")
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    files = _collect(args.input)
    rows = [row for path in files if (row := _profile_episode(path, args.lookback, args.target))]
    if not rows:
        raise SystemExit(f"no {args.target} profiles found")
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows, args.target)
    print(f"files={len(files)}")
    print(f"profiles={len(rows)}")
    print(f"events={sum(int(row['target_events']) for row in rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
