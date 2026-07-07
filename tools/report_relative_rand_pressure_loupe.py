from __future__ import annotations

import argparse
import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path


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


def _rank_map(values: list[float]) -> dict[int, float]:
    if not values:
        return {}
    ordered = sorted((value, index) for index, value in enumerate(values))
    if len(ordered) == 1:
        return {ordered[0][1]: 0.5}
    ranks: dict[int, float] = {}
    max_rank = len(ordered) - 1
    for rank, (_, index) in enumerate(ordered):
        ranks[index] = rank / max_rank
    return ranks


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _world_loupe(label: str, path: Path) -> dict[str, object]:
    rows = _read_rows(path)
    metrics = {
        "strain": [(_float(row.get("mcm_strain_quality"))) for row in rows],
        "rekopplung": [(_float(row.get("mcm_rekopplung_quality"))) for row in rows],
        "carry": [(_float(row.get("mcm_carry_quality"))) for row in rows],
        "sensory": [(_float(row.get("mcm_sensory_coupling"))) for row in rows],
        "visual_gap": [(_float(row.get("mcm_visual_field_gap"))) for row in rows],
        "hearing_gap": [(_float(row.get("mcm_hearing_field_gap"))) for row in rows],
        "intake_pressure": [(_float(row.get("rezeptor_field_intake_pressure"))) for row in rows],
        "feld_tension": [(_float(row.get("mcm_feldwirkung_mcm_tension"))) for row in rows],
        "afterimage": [(_float(row.get("mini_afterimage"))) for row in rows],
    }
    ranks = {name: _rank_map(values) for name, values in metrics.items()}

    pressure_rows: list[dict[str, object]] = []
    dominant_counter: Counter[str] = Counter()
    role_effects: dict[str, Counter[str]] = defaultdict(Counter)
    role_symbols: dict[str, Counter[str]] = defaultdict(Counter)

    for index, row in enumerate(rows):
        strain = ranks["strain"].get(index, 0.0)
        rekopplung = ranks["rekopplung"].get(index, 0.0)
        carry = ranks["carry"].get(index, 0.0)
        sensory = ranks["sensory"].get(index, 0.0)
        visual_gap = ranks["visual_gap"].get(index, 0.0)
        hearing_gap = ranks["hearing_gap"].get(index, 0.0)
        intake_pressure = ranks["intake_pressure"].get(index, 0.0)
        feld_tension = ranks["feld_tension"].get(index, 0.0)
        afterimage = ranks["afterimage"].get(index, 0.0)
        gap_pressure = max(visual_gap, hearing_gap)

        scores = {
            "randdruck": (
                strain * 0.28
                + intake_pressure * 0.20
                + gap_pressure * 0.20
                + feld_tension * 0.17
                + (1.0 - rekopplung) * 0.15
            ),
            "offene_variante": (
                strain * 0.20
                + gap_pressure * 0.22
                + intake_pressure * 0.13
                + carry * 0.15
                + rekopplung * 0.15
                + afterimage * 0.15
            ),
            "rekopplung": (
                rekopplung * 0.30
                + sensory * 0.20
                + carry * 0.20
                + (1.0 - strain) * 0.17
                + (1.0 - intake_pressure) * 0.13
            ),
            "daempfung": (
                (1.0 - intake_pressure) * 0.25
                + (1.0 - gap_pressure) * 0.20
                + sensory * 0.20
                + rekopplung * 0.20
                + (1.0 - feld_tension) * 0.15
            ),
        }
        ordered = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        dominant = ordered[0][0]
        margin = ordered[0][1] - ordered[1][1]
        dominant_counter[dominant] += 1
        effect = row.get("passive_mcm_effect_class") or "-"
        symbol_family = row.get("symbol_family") or "-"
        role_effects[dominant][effect] += 1
        role_symbols[dominant][symbol_family] += 1

        pressure_rows.append(
            {
                "world": label,
                "tick": row.get("tick") or "",
                "timestamp_ms": row.get("timestamp_ms") or "",
                "dominant_pressure": dominant,
                "dominant_margin": margin,
                "randdruck": scores["randdruck"],
                "offene_variante": scores["offene_variante"],
                "rekopplung": scores["rekopplung"],
                "daempfung": scores["daempfung"],
                "effect_class": effect,
                "symbol_family": symbol_family,
                "mcm_episode_preview": row.get("mcm_field_episode_preview_symbol") or "",
                "raw_strain": metrics["strain"][index],
                "raw_rekopplung": metrics["rekopplung"][index],
                "raw_carry": metrics["carry"][index],
                "raw_sensory": metrics["sensory"][index],
                "raw_visual_gap": metrics["visual_gap"][index],
                "raw_hearing_gap": metrics["hearing_gap"][index],
                "raw_intake_pressure": metrics["intake_pressure"][index],
                "raw_feld_tension": metrics["feld_tension"][index],
                "raw_afterimage": metrics["afterimage"][index],
            }
        )

    total = len(rows) or 1
    return {
        "label": label,
        "path": str(path),
        "rows": len(rows),
        "counts": dict(dominant_counter),
        "shares": {key: value / total for key, value in dominant_counter.items()},
        "metric_means": {key: _mean(values) for key, values in metrics.items()},
        "role_effects": {key: dict(counter) for key, counter in role_effects.items()},
        "role_symbols": {
            key: counter.most_common(5) for key, counter in role_symbols.items()
        },
        "top_randdruck": sorted(
            pressure_rows, key=lambda item: float(item["randdruck"]), reverse=True
        )[:10],
        "top_open": sorted(
            pressure_rows, key=lambda item: float(item["offene_variante"]), reverse=True
        )[:10],
        "pressure_rows": pressure_rows,
    }


def _write_csv(path: Path, worlds: list[dict[str, object]]) -> None:
    rows: list[dict[str, object]] = []
    for world in worlds:
        rows.extend(world["pressure_rows"])  # type: ignore[arg-type]
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_report(path: Path, worlds: list[dict[str, object]]) -> None:
    lines: list[str] = [
        "# Relative Randdruck-Lupe",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest innerhalb jeder Welt konkurrierende Druckprofile.",
        "Sie ersetzt keine Runtime-Mechanik und erzeugt kein Gate.",
        "",
        "Gelesene Profile:",
        "",
        "```text",
        "randdruck        = Strain, Intake-Druck, Gap und schwache Rekopplung",
        "offene_variante  = Spannung, Gap, Carry, Rekopplung und Nachhall",
        "rekopplung       = Rekopplung, Sinneskopplung, Carry und geringe Last",
        "daempfung        = geringe Aufnahme, geringe Gap-Spannung und stabile Kopplung",
        "```",
        "",
        "Die Werte sind relative Druckprofile innerhalb der jeweiligen Welt.",
        "Sie sind keine universellen MCM-Grenzen.",
        "",
        "## Kurzbefund",
        "",
        "| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung | Strain | Intake | Visual Gap | Hearing Gap |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for world in worlds:
        shares = world["shares"]  # type: ignore[assignment]
        means = world["metric_means"]  # type: ignore[assignment]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(world["label"]),
                    str(world["rows"]),
                    _fmt(float(shares.get("randdruck", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(shares.get("offene_variante", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(shares.get("rekopplung", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(shares.get("daempfung", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(means.get("strain", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(means.get("intake_pressure", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(means.get("visual_gap", 0.0))),  # type: ignore[union-attr]
                    _fmt(float(means.get("hearing_gap", 0.0))),  # type: ignore[union-attr]
                ]
            )
            + " |"
        )

    lines.extend(["", "## Randdruck-Spitzen", ""])
    for world in worlds:
        lines.extend(["", f"### {world['label']}", ""])
        lines.append("| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |")
        lines.append("|---:|---:|---|---|---|---:|---:|---:|---:|")
        for item in world["top_randdruck"]:  # type: ignore[index]
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(item["tick"]),
                        _fmt(float(item["randdruck"])),
                        str(item["effect_class"]),
                        str(item["symbol_family"]),
                        str(item["mcm_episode_preview"]),
                        _fmt(float(item["raw_strain"])),
                        _fmt(float(item["raw_intake_pressure"])),
                        _fmt(float(item["raw_visual_gap"])),
                        _fmt(float(item["raw_hearing_gap"])),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Diese Lupe trennt zwei Ebenen:",
            "",
            "```text",
            "Topologie-Matrix: Welche Rolle dominiert im Gesamtbild?",
            "Randdruck-Lupe: Wo entstehen lokale Rand-/Oeffnungsdruecke innerhalb der Welt?",
            "```",
            "",
            "Damit kann eine Welt insgesamt zentrumsnah bleiben und trotzdem lokale Randdruckzonen enthalten.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Lupe gegen echte Stressfenster und synthetische Randfenster verglichen werden.",
            "Entscheidend ist, ob Randdruck nur kurz aufflackert, ob er rekoppelt oder ob er zu stabilen offenen Bedeutungsinseln reift.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--world",
        nargs=2,
        action="append",
        metavar=("NAME", "EPISODES_CSV"),
        required=True,
        help="World label and matching episodes csv.",
    )
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--csv-out", type=Path, required=True)
    args = parser.parse_args()

    worlds = [_world_loupe(name, Path(path)) for name, path in args.world]
    _write_report(args.out, worlds)
    _write_csv(args.csv_out, worlds)
    print(f"wrote {args.out.resolve()}")
    print(f"wrote {args.csv_out.resolve()}")


if __name__ == "__main__":
    main()
