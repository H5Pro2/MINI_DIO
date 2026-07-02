from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from tools.report_mcm_field_phase_raw_window_loupe import WORLD_DATA_MAP, _raw_profile


DEFAULT_INPUT = ROOT / "docs" / "befunde" / "1264_MCM_FOLGEHALT_NACH_RANDKONTAKT.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "1266_MCM_FOLGEHALT_ROHWELT_KOPPLUNG.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _raw_shape_bucket(profile: dict[str, object]) -> str:
    movement = str(profile.get("movement_class", "") or "")
    expansion = _safe_float(profile.get("expansion_ratio"))
    direction = _safe_float(profile.get("direction_consistency"))
    body = _safe_float(profile.get("body_ratio"))
    raw_return = _safe_float(profile.get("raw_return"))

    if movement == "bewegungsbruch" and expansion >= 4.0:
        return "starker_bruchimpuls"
    if movement == "bewegungsbruch":
        return "bewegungsbruch"
    if movement == "expansion_impuls" and raw_return > 0.0:
        return "positive_expansion"
    if movement == "expansion_impuls" and raw_return < 0.0:
        return "negative_expansion"
    if movement == "gerichtete_bewegung" and direction >= 0.6:
        return "gerichtete_bewegung"
    if body >= 0.006:
        return "koerperlast"
    return "gemischte_rohwelt"


def _build_rows(input_rows: list[dict[str, str]], radius: int) -> tuple[list[dict[str, object]], Counter[str]]:
    raw_cache: dict[str, list[dict[str, str]]] = {}
    skipped: Counter[str] = Counter()
    rows: list[dict[str, object]] = []

    for row in input_rows:
        world = str(row.get("world", "") or "")
        data_name = WORLD_DATA_MAP.get(world)
        if not data_name:
            skipped["keine_eindeutige_rohwelt"] += 1
            continue

        data_path = ROOT / "data" / data_name
        if not data_path.exists():
            skipped["csv_fehlt"] += 1
            continue

        if data_name not in raw_cache:
            raw_cache[data_name] = _load_csv(data_path)

        tick = _safe_int(row.get("rand_start_tick"))
        profile = _raw_profile(raw_cache[data_name], tick, radius)
        if _safe_int(profile.get("raw_rows")) <= 0:
            skipped["tick_ausserhalb_rohdatei"] += 1
            continue

        rows.append(
            {
                "followhold_kind": row.get("followhold_kind", ""),
                "world": world,
                "data_file": data_name,
                "rand_start_tick": row.get("rand_start_tick", ""),
                "follow_role": row.get("follow_role", ""),
                "follow_duration": row.get("follow_duration", ""),
                "after_role": row.get("after_role", ""),
                "delta_follow_rekopplung": row.get("delta_follow_rekopplung", ""),
                "delta_follow_strain": row.get("delta_follow_strain", ""),
                "rand_loudness": row.get("rand_loudness", ""),
                "rand_intake": row.get("rand_intake", ""),
                "rand_sharpness": row.get("rand_sharpness", ""),
                "rand_rekopplung": row.get("rand_rekopplung", ""),
                "rand_strain": row.get("rand_strain", ""),
                **{key: round(value, 8) if isinstance(value, float) else value for key, value in profile.items()},
                "raw_shape_bucket": _raw_shape_bucket(profile),
            }
        )

    return rows, skipped


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _group_stats(rows: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key, "") or "")].append(row)

    out: list[dict[str, object]] = []
    for name, group in grouped.items():
        movements = Counter(str(row.get("movement_class", "")) for row in group)
        buckets = Counter(str(row.get("raw_shape_bucket", "")) for row in group)
        followholds = Counter(str(row.get("followhold_kind", "")) for row in group)
        out.append(
            {
                key: name,
                "count": len(group),
                "movement_top": dict(movements.most_common(3)),
                "bucket_top": dict(buckets.most_common(3)),
                "followhold_top": dict(followholds.most_common(4)),
                "raw_return": _mean([_safe_float(row.get("raw_return")) for row in group]),
                "range_ratio": _mean([_safe_float(row.get("range_ratio")) for row in group]),
                "expansion_ratio": _mean([_safe_float(row.get("expansion_ratio")) for row in group]),
                "direction_consistency": _mean([_safe_float(row.get("direction_consistency")) for row in group]),
                "delta_follow_rekopplung": _mean([_safe_float(row.get("delta_follow_rekopplung")) for row in group]),
                "delta_follow_strain": _mean([_safe_float(row.get("delta_follow_strain")) for row in group]),
            }
        )
    out.sort(key=lambda item: (-int(item["count"]), str(item[key])))
    return out


def _write_markdown(path: Path, rows: list[dict[str, object]], skipped: Counter[str], input_path: Path) -> None:
    kind_counts = Counter(str(row["followhold_kind"]) for row in rows)
    movement_counts = Counter(str(row["movement_class"]) for row in rows)
    bucket_counts = Counter(str(row["raw_shape_bucket"]) for row in rows)
    world_counts = Counter(str(row["world"]) for row in rows)
    by_kind = _group_stats(rows, "followhold_kind")
    by_bucket = _group_stats(rows, "raw_shape_bucket")

    lines: list[str] = [
        "# MCM Folgehalt Rohwelt-Kopplung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Welche Rohweltspannung steht vor Folgehalt oder Rueckfall nach Randkontakt?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose koppelt `1264_MCM_FOLGEHALT_NACH_RANDKONTAKT.csv` mit eindeutig zuordenbaren Rohweltfenstern.",
        "",
        "## Eingabe",
        "",
        f"- Folgehalt: `{input_path.relative_to(ROOT)}`",
        "- Rohwelt: gemappte CSV-Dateien aus `data/`",
        "",
        "## Profil",
        "",
        f"- gekoppelte Fenster: `{len(rows)}`",
        f"- ausgelassen: `{dict(skipped.most_common())}`",
        f"- Folgehalt-Arten: `{dict(kind_counts.most_common())}`",
        f"- Rohbewegungen: `{dict(movement_counts.most_common())}`",
        f"- Rohform-Buckets: `{dict(bucket_counts.most_common())}`",
        f"- Welten: `{dict(world_counts.most_common(12))}`",
        "",
        "## Folgehalt nach Rohweltprofil",
        "",
        "| Folgehalt | Anzahl | Rohbewegung | Rohform | Return | Range | Expansion | Richtung | Delta Rekopplung | Delta Strain |",
        "|---|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in by_kind:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["followhold_kind"]),
                    str(row["count"]),
                    str(row["movement_top"]),
                    str(row["bucket_top"]),
                    _fmt(row["raw_return"]),
                    _fmt(row["range_ratio"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["delta_follow_rekopplung"]),
                    _fmt(row["delta_follow_strain"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Rohform nach Folgequalitaet",
            "",
            "| Rohform | Anzahl | Folgehalt | Return | Range | Expansion | Richtung | Delta Rekopplung | Delta Strain |",
            "|---|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in by_bucket:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["raw_shape_bucket"]),
                    str(row["count"]),
                    str(row["followhold_top"]),
                    _fmt(row["raw_return"]),
                    _fmt(row["range_ratio"]),
                    _fmt(row["expansion_ratio"]),
                    _fmt(row["direction_consistency"]),
                    _fmt(row["delta_follow_rekopplung"]),
                    _fmt(row["delta_follow_strain"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Rohwelt liefert nicht allein die Bedeutung. Der gleiche Bewegungsbruch kann unterschiedliche Feldfolgen tragen.",
            "",
            "Entscheidend ist die Kopplung:",
            "",
            "```text",
            "Rohweltspannung -> Randkontakt -> Folgehalt oder Rueckfall",
            "```",
            "",
            "Damit wird Folgehalt als Feldantwort auf Weltspannung lesbar, nicht als isolierte Rolle.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Kopplung nach Asset/Weltart getrennt werden: Bleibt die Feldantwort gleich, wenn sich die Weltmelodie stark unterscheidet?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_assessment(path: Path, rows: list[dict[str, object]], skipped: Counter[str]) -> None:
    by_kind = _group_stats(rows, "followhold_kind")
    lines = [
        "# Bewertung: MCM Folgehalt Rohwelt-Kopplung",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Kernaussage",
        "",
        "Folgehalt entsteht nicht aus einer einzelnen Rohbewegung, sondern aus der Feldantwort auf eine Rohweltspannung.",
        "",
        "## Messbild",
        "",
        f"- gekoppelte Fenster: `{len(rows)}`",
        f"- ausgelassen: `{dict(skipped.most_common())}`",
        "",
        "## Differenzierung",
        "",
    ]
    for row in by_kind[:8]:
        lines.append(
            f"- `{row['followhold_kind']}`: count `{row['count']}`, "
            f"Expansion `{_fmt(row['expansion_ratio'])}`, Richtung `{_fmt(row['direction_consistency'])}`, "
            f"Delta Rekopplung `{_fmt(row['delta_follow_rekopplung'])}`, Delta Strain `{_fmt(row['delta_follow_strain'])}`."
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Aussenweltform ist ein Ausloeser, aber nicht die fertige Bedeutung.",
            "",
            "MINI_DIO zeigt hier eine feldbezogene Zwischenebene: Weltspannung wird aufgenommen, als Randkontakt verarbeitet und danach entweder entlastend, rueckfallend oder gemischt weitergetragen.",
            "",
            "## Naechste Pruefung",
            "",
            "Nach Asset/Weltart trennen und pruefen, ob BTC, SOL, KAS, PAXG und synthetische Welten dieselbe Folgehalt-Mechanik mit unterschiedlicher Faerbung zeigen.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Koppelt Folgehalt nach Randkontakt mit Rohweltfenstern.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Folgehalt CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    parser.add_argument("--radius", type=int, default=35, help="Rohwelt-Radius um Randkontakt.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows, skipped = _build_rows(_load_csv(input_path), args.radius)
    csv_path = out_path.with_suffix(".csv")
    assessment_path = out_path.with_name("1267_MCM_FOLGEHALT_ROHWELT_KOPPLUNG_BEWERTUNG.md")

    _write_csv(csv_path, rows)
    _write_markdown(out_path, rows, skipped, input_path)
    _write_assessment(assessment_path, rows, skipped)

    print(f"rows={len(rows)} skipped={dict(skipped)}")
    print(f"wrote={out_path.relative_to(ROOT)}")
    print(f"wrote={csv_path.relative_to(ROOT)}")
    print(f"wrote={assessment_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
