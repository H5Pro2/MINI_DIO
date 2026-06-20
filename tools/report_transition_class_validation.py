from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "336_BEWEGUNGSARTEN_VALIDIERUNG.md"


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


def _axes(row: dict[str, str] | None) -> dict[str, float]:
    if row is None:
        return {}
    visual_gap = _float(row.get("mcm_visual_field_gap"))
    hearing_gap = _float(row.get("mcm_hearing_field_gap"))
    contact_alignment = _float(row.get("rezeptor_contact_alignment"))
    visual_contact = _float(row.get("rezeptor_visual_contact"))
    auditory_contact = _float(row.get("rezeptor_auditory_contact"))
    hearing_tone = abs(_float(row.get("hoeren_energy_tone")))
    hearing_shift = abs(_float(row.get("hoeren_energy_shift")))
    form_stability = _float(row.get("sehen_form_stability"))
    form_change = abs(_float(row.get("sehen_form_change")))
    contact_pressure = _float(row.get("rezeptor_contact_pressure"))
    strain = _float(row.get("mcm_strain_quality"))
    rekopplung = _float(row.get("mcm_rekopplung_quality"))

    distance = max(0.0, min(1.0, (visual_gap + hearing_gap + max(0.0, 1.0 - contact_alignment)) / 3.0))
    focus = max(0.0, min(1.0, ((visual_contact + auditory_contact + contact_alignment) / 3.0) * (1.0 - distance * 0.35)))
    loudness = max(0.0, min(1.0, (hearing_tone + hearing_shift) / 2.0))
    sharpness = max(0.0, min(1.0, (form_stability + max(0.0, 1.0 - form_change)) / 2.0))
    pressure = max(0.0, min(1.0, (contact_pressure + strain + max(0.0, 1.0 - rekopplung)) / 3.0))
    relaxation = max(0.0, min(1.0, (rekopplung + contact_alignment + max(0.0, 1.0 - strain)) / 3.0))
    return {
        "focus": focus,
        "distance": distance,
        "loudness": loudness,
        "sharpness": sharpness,
        "pressure": pressure,
        "relaxation": relaxation,
        "rekopplung": rekopplung,
        "strain": strain,
    }


def _movement_class(items: list[dict[str, object]]) -> str:
    worlds = len({str(item["world"]) for item in items})
    count = len(items)
    pressure = _mean([float(item["pressure_delta"]) for item in items])
    sharpness = _mean([float(item["sharpness_delta"]) for item in items])
    rekopplung = _mean([float(item["rekopplung_delta"]) for item in items])
    role_shift = Counter(str(item["role_shift"]) for item in items).most_common(1)[0][0]

    if worlds >= 3 and count >= 12 and abs(pressure) <= 0.025 and abs(rekopplung) <= 0.025:
        return "grundinsel_wechsel"
    if rekopplung > 0.008 and pressure <= 0.0:
        return "rekopplungsbogen"
    if pressure > 0.04 and rekopplung < -0.02:
        return "druck_rueckfuehrung"
    if "offene_variante" in role_shift and pressure > 0.0:
        return "offener_uebergang"
    if sharpness > 0.06 and abs(pressure) <= 0.04:
        return "schaerfungsuebergang"
    if worlds <= 2 and count <= 5:
        return "lokale_einzelkante"
    return "gemischte_feldbewegung"


def _dominant(values: list[str]) -> str:
    cleaned = [value for value in values if value and value != "-"]
    if not cleaned:
        return "-"
    value, count = Counter(cleaned).most_common(1)[0]
    return f"{value} ({count}/{len(cleaned)})"


def _collect_world(world: str, episodes_path: Path) -> list[dict[str, object]]:
    rows = _load_rows(episodes_path)
    transitions: list[dict[str, object]] = []
    for idx in range(1, len(rows)):
        prev_row = rows[idx - 1]
        cur_row = rows[idx]
        from_preview = _preview(prev_row)
        to_preview = _preview(cur_row)
        if from_preview == to_preview:
            continue
        prev_axes = _axes(prev_row)
        cur_axes = _axes(cur_row)
        transitions.append(
            {
                "world": world,
                "from_preview": from_preview,
                "to_preview": to_preview,
                "pair": f"{from_preview}->{to_preview}",
                "role_shift": f"{_role(prev_row)}->{_role(cur_row)}",
                "pressure_delta": cur_axes["pressure"] - prev_axes["pressure"],
                "sharpness_delta": cur_axes["sharpness"] - prev_axes["sharpness"],
                "focus_delta": cur_axes["focus"] - prev_axes["focus"],
                "rekopplung_delta": cur_axes["rekopplung"] - prev_axes["rekopplung"],
                "loudness_delta": cur_axes["loudness"] - prev_axes["loudness"],
            }
        )
    return transitions


def _summarize(transitions: list[dict[str, object]], top_n: int) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in transitions:
        grouped[str(item["pair"])].append(item)

    pair_rows: list[dict[str, object]] = []
    for pair, items in sorted(grouped.items(), key=lambda entry: len(entry[1]), reverse=True)[:top_n]:
        pair_rows.append(
            {
                "pair": pair,
                "movement_class": _movement_class(items),
                "count": len(items),
                "worlds": len({str(item["world"]) for item in items}),
                "dominant_world": _dominant([str(item["world"]) for item in items]),
                "dominant_role_shift": _dominant([str(item["role_shift"]) for item in items]),
                "pressure_delta": _mean([float(item["pressure_delta"]) for item in items]),
                "sharpness_delta": _mean([float(item["sharpness_delta"]) for item in items]),
                "focus_delta": _mean([float(item["focus_delta"]) for item in items]),
                "rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in items]),
                "loudness_delta": _mean([float(item["loudness_delta"]) for item in items]),
            }
        )

    class_grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in pair_rows:
        class_grouped[str(row["movement_class"])].append(row)
    class_rows: list[dict[str, object]] = []
    for movement_class, items in sorted(class_grouped.items(), key=lambda entry: sum(int(item["count"]) for item in entry[1]), reverse=True):
        class_rows.append(
            {
                "movement_class": movement_class,
                "pairs": len(items),
                "events": sum(int(item["count"]) for item in items),
                "worlds_sum": sum(int(item["worlds"]) for item in items),
                "top_pair": max(items, key=lambda item: int(item["count"]))["pair"],
                "pressure_delta": _mean([float(item["pressure_delta"]) for item in items]),
                "sharpness_delta": _mean([float(item["sharpness_delta"]) for item in items]),
                "rekopplung_delta": _mean([float(item["rekopplung_delta"]) for item in items]),
            }
        )
    return pair_rows, class_rows


def _write_csv(pair_rows: list[dict[str, object]], class_rows: list[dict[str, object]], out_path: Path) -> None:
    pair_path = out_path.with_suffix(".csv")
    pair_fields = [
        "pair",
        "movement_class",
        "count",
        "worlds",
        "dominant_world",
        "dominant_role_shift",
        "pressure_delta",
        "sharpness_delta",
        "focus_delta",
        "rekopplung_delta",
        "loudness_delta",
    ]
    pair_path.parent.mkdir(parents=True, exist_ok=True)
    with pair_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=pair_fields)
        writer.writeheader()
        for row in pair_rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in pair_fields
                }
            )

    class_path = out_path.with_name(out_path.stem + "_klassen.csv")
    class_fields = ["movement_class", "pairs", "events", "worlds_sum", "top_pair", "pressure_delta", "sharpness_delta", "rekopplung_delta"]
    with class_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=class_fields)
        writer.writeheader()
        for row in class_rows:
            writer.writerow(
                {
                    key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "")
                    for key in class_fields
                }
            )


def _write_md(pair_rows: list[dict[str, object]], class_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(pair_rows, class_rows, out_path)

    lines = [
        "# Bewegungsarten Validierung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die bisher gefundenen Preview-Uebergangsklassen auch in Bedingungswelten auftreten.",
        "Sie ist passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Sind die Bewegungsarten robuste Feldbewegungen oder nur Artefakte einer Weltmatrix?",
        "2. Unterpruefung: Stress-, Seitwaerts- und Expansionswelten gegen die bekannten Preview-Uebergangspaare pruefen.",
        "3. Folgeschritt: stabile Bewegungsarten koennen spaeter als passive Regulationswahrnehmung gelesen werden.",
        "",
        "## Klassenuebersicht",
        "",
        "| Klasse | Paare | Events | Welten-Summe | Top-Paar | dDruck | dSchaerfe | dRekopplung |",
        "|---|---:|---:|---:|---|---:|---:|---:|",
    ]
    for row in class_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["movement_class"]),
                    str(row["pairs"]),
                    str(row["events"]),
                    str(row["worlds_sum"]),
                    str(row["top_pair"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Top-Uebergangspaare",
            "",
            "| Paar | Klasse | Anzahl | Welten | dominante Welt | Rollenwechsel | dDruck | dSchaerfe | dRekopplung |",
            "|---|---|---:|---:|---|---|---:|---:|---:|",
        ]
    )
    for row in pair_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["movement_class"]),
                    str(row["count"]),
                    str(row["worlds"]),
                    str(row["dominant_world"]),
                    str(row["dominant_role_shift"]),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["sharpness_delta"])),
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
            "Die Bewegungsarten bleiben als Arbeitsklassen lesbar, wenn sie in mehreren Bedingungswelten wiederkehren.",
            "Wichtig ist nicht nur die Haeufigkeit, sondern ob Druck, Schaerfe und Rekopplung dieselbe Bewegungsrichtung tragen.",
            "",
            "Wenn ein Paar nur lokal oder nur in einer Welt erscheint, wird es als lokale Kante behandelt.",
            "Wenn ein Paar weltuebergreifend erscheint, ist es ein Kandidat fuer eine passive Feldbewegung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die stabilsten validierten Bewegungsarten gegen ihre Rohwelt-Segmente gelegt werden.",
            "Dann wird sichtbar, welche Weltbewegung eine Feldbewegung ausloest, ohne daraus schon Handlung abzuleiten.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate passive preview transition classes across condition worlds.")
    parser.add_argument("--world", nargs=2, action="append", metavar=("NAME", "EPISODES_CSV"), required=True)
    parser.add_argument("--top-n", type=int, default=30)
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    transitions: list[dict[str, object]] = []
    for world_name, path_text in args.world:
        path = _resolve(path_text)
        if not path.exists():
            raise FileNotFoundError(path)
        transitions.extend(_collect_world(world_name, path))

    pair_rows, class_rows = _summarize(transitions, top_n=args.top_n)
    _write_md(pair_rows, class_rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
