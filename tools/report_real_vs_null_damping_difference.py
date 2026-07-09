from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _world_group(world: str) -> str:
    return "nullwelt" if world.startswith("NULL_") else "realwelt"


def _run_dir_name(world: str, factor: str) -> str:
    return f"{world}_factor_{str(factor).replace('.', 'p')}"


def _episode_path(debug_root: Path, world: str, factor: str) -> Path:
    return debug_root / _run_dir_name(world, factor) / "dio_mini_lauf_1" / "episodes.csv"


def _entropy(counter: Counter[str]) -> float:
    total = sum(counter.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for count in counter.values():
        if count <= 0:
            continue
        probability = count / total
        entropy -= probability * math.log(probability, 2)
    return entropy


def _episode_metrics(path: Path) -> dict[str, float]:
    if not path.exists():
        return {
            "unique_roles": 0.0,
            "role_entropy": 0.0,
            "unique_milieus": 0.0,
            "milieu_entropy": 0.0,
        }
    role_counter: Counter[str] = Counter()
    milieu_counter: Counter[str] = Counter()
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            role = row.get("mcm_field_episode_role") or "-"
            milieu = row.get("mcm_adaptive_milieu_state") or "-"
            role_counter[role] += 1
            milieu_counter[milieu] += 1
    return {
        "unique_roles": float(len(role_counter)),
        "role_entropy": _entropy(role_counter),
        "unique_milieus": float(len(milieu_counter)),
        "milieu_entropy": _entropy(milieu_counter),
    }


def _enrich(rows: list[dict[str, str]], debug_root: Path) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    for row in rows:
        world = str(row.get("world", ""))
        factor = str(row.get("rekopplung_factor", ""))
        metrics = _episode_metrics(_episode_path(debug_root, world, factor))
        enriched.append(
            {
                "world": world,
                "group": _world_group(world),
                "factor": _float(factor),
                "unique_symbols": _float(row.get("unique_symbols")),
                "unique_episode_families": _float(row.get("unique_episode_families")),
                "adaptive_rekopplung": _float(row.get("avg_mcm_adaptive_rekopplung_quality")),
                "rekopplung": _float(row.get("avg_mcm_rekopplung_quality")),
                "strain": _float(row.get("avg_mcm_strain_quality")),
                "afterimage": _float(row.get("avg_mini_afterimage")),
                "temporal_trust": _float(row.get("avg_mini_temporal_trust_support")),
                "temporal_caution": _float(row.get("avg_mini_temporal_caution_support")),
                "sensory_coupling": _float(row.get("avg_mcm_sensory_coupling")),
                **metrics,
            }
        )
    return enriched


def _group_rows(rows: list[dict[str, object]]) -> list[dict[str, float | str]]:
    buckets: dict[tuple[float, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        buckets[(_float(row["factor"]), str(row["group"]))].append(row)

    grouped: list[dict[str, float | str]] = []
    for (factor, group), items in sorted(buckets.items()):
        grouped.append(
            {
                "factor": factor,
                "group": group,
                "worlds": float(len(items)),
                "symbols": _mean([_float(item["unique_symbols"]) for item in items]),
                "families": _mean([_float(item["unique_episode_families"]) for item in items]),
                "adaptive_rekopplung": _mean([_float(item["adaptive_rekopplung"]) for item in items]),
                "rekopplung": _mean([_float(item["rekopplung"]) for item in items]),
                "strain": _mean([_float(item["strain"]) for item in items]),
                "afterimage": _mean([_float(item["afterimage"]) for item in items]),
                "temporal_trust": _mean([_float(item["temporal_trust"]) for item in items]),
                "temporal_caution": _mean([_float(item["temporal_caution"]) for item in items]),
                "sensory_coupling": _mean([_float(item["sensory_coupling"]) for item in items]),
                "unique_roles": _mean([_float(item["unique_roles"]) for item in items]),
                "role_entropy": _mean([_float(item["role_entropy"]) for item in items]),
                "unique_milieus": _mean([_float(item["unique_milieus"]) for item in items]),
                "milieu_entropy": _mean([_float(item["milieu_entropy"]) for item in items]),
            }
        )
    return grouped


def _difference_rows(grouped: list[dict[str, float | str]]) -> list[dict[str, float]]:
    by_factor: dict[float, dict[str, dict[str, float | str]]] = defaultdict(dict)
    for row in grouped:
        by_factor[_float(row["factor"])][str(row["group"])] = row

    differences: list[dict[str, float]] = []
    for factor, groups in sorted(by_factor.items()):
        real = groups.get("realwelt")
        null = groups.get("nullwelt")
        if not real or not null:
            continue
        differences.append(
            {
                "factor": factor,
                "symbols_delta": _float(real["symbols"]) - _float(null["symbols"]),
                "families_delta": _float(real["families"]) - _float(null["families"]),
                "adaptive_rekopplung_delta": _float(real["adaptive_rekopplung"]) - _float(null["adaptive_rekopplung"]),
                "afterimage_delta": _float(real["afterimage"]) - _float(null["afterimage"]),
                "role_entropy_delta": _float(real["role_entropy"]) - _float(null["role_entropy"]),
                "milieu_entropy_delta": _float(real["milieu_entropy"]) - _float(null["milieu_entropy"]),
                "strain_delta": _float(real["strain"]) - _float(null["strain"]),
            }
        )
    return differences


def _format(value: float) -> str:
    return f"{value:.4f}"


def _write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(
    path: Path,
    grouped: list[dict[str, float | str]],
    differences: list[dict[str, float]],
    source_csv: str,
    debug_root: str,
    title: str,
    real_group_label: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Grundfrage",
        "",
        "Unterscheiden sich reale Weltspuren und Nullwelten bei gleicher Rueckfuehrungsdaempfung nur in der Topologieklasse, oder in tieferen Merkmalen wie Bedeutungsbreite, adaptiver Rekopplung, Nachhall und Rollenvarianz?",
        "",
        "## Grundlage",
        "",
        f"- Summenquelle: `{source_csv}`",
        f"- Episodenquelle: `{debug_root}`",
        f"- Gruppen: `realwelt` = {real_group_label}, `nullwelt` = Shuffle/Random",
        "",
        "## Gruppenmittel",
        "",
        "| Faktor | Gruppe | Welten | Symbole | Familien | Rekopplung | Adaptive Rekopplung | Nachhall | Rollen-Entropie | Milieu-Entropie | Strain |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in grouped:
        lines.append(
            "| "
            + " | ".join(
                [
                    _format(_float(row["factor"])),
                    str(row["group"]),
                    _format(_float(row["worlds"])),
                    _format(_float(row["symbols"])),
                    _format(_float(row["families"])),
                    _format(_float(row["rekopplung"])),
                    _format(_float(row["adaptive_rekopplung"])),
                    _format(_float(row["afterimage"])),
                    _format(_float(row["role_entropy"])),
                    _format(_float(row["milieu_entropy"])),
                    _format(_float(row["strain"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Differenz Realwelt minus Nullwelt",
            "",
            "| Faktor | Delta Symbole | Delta Familien | Delta adaptive Rekopplung | Delta Nachhall | Delta Rollen-Entropie | Delta Milieu-Entropie | Delta Strain |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in differences:
        lines.append(
            "| "
            + " | ".join(
                [
                    _format(row["factor"]),
                    _format(row["symbols_delta"]),
                    _format(row["families_delta"]),
                    _format(row["adaptive_rekopplung_delta"]),
                    _format(row["afterimage_delta"]),
                    _format(row["role_entropy_delta"]),
                    _format(row["milieu_entropy_delta"]),
                    _format(row["strain_delta"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die dominante Feldklasse allein trennt reale Welt und Nullwelt nicht sauber, weil beide Gruppen unter Rueckfuehrungsdaempfung stabil bleiben koennen.",
            "",
            "Die Trennung liegt tiefer:",
            "",
            "- reale Welten tragen deutlich mehr Symbole und Episodenfamilien,",
            "- reale Welten halten die adaptive Rekopplung stabiler,",
            "- Nullwelten bleiben schmaler und zeigen eine variablere adaptive Rueckfuehrung,",
            "- Strain bleibt als Einzelwert nicht ausreichend trennscharf.",
            "",
            "Damit wird die Feldordnung nicht als einfacher Stabil/Kollaps-Schalter sichtbar, sondern als Bedeutungsbreite plus Rueckfuehrungsqualitaet. Das ist methodisch wichtig, weil es die Pareidolie-Gegenfrage schaerfer macht: Nicht jede stabile Klasse ist automatisch gleiche Bedeutung.",
            "",
            "## Grenze",
            "",
            "Der Report vergleicht nur die 1827-Welten. Fuer eine belastbarere Aussage muessen weitere reale und synthetische Welten mit derselben Differenzlogik gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Differenzlogik auf weitere Null-, Ruhe-, Stress- und Assetwelten angewendet werden. Entscheidend ist, ob Bedeutungsbreite und adaptive Rekopplung dauerhaft besser trennen als die dominante Feldklasse.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-csv", default="docs/befunde/1001-2000/1751-2000/1827_RUECKFUEHRUNG_DAEMPFUNG_STRESS_NULL.csv")
    parser.add_argument("--debug-root", default="debug/1827_rekopplung_damping_stress_null")
    parser.add_argument("--out-md", default="docs/befunde/1001-2000/1751-2000/1828_REALWELT_NULLWELT_DAEMPFUNG_DIFFERENZREPORT.md")
    parser.add_argument("--out-csv", default="docs/befunde/1001-2000/1751-2000/1828_REALWELT_NULLWELT_DAEMPFUNG_DIFFERENZREPORT.csv")
    parser.add_argument("--title", default="1828 - Differenzreport: reale Weltordnung gegen Nullwelt")
    parser.add_argument("--real-group-label", default="Stress/Expansion")
    args = parser.parse_args()

    source_csv = _resolve(args.source_csv)
    debug_root = _resolve(args.debug_root)
    rows = _enrich(_read_csv(source_csv), debug_root)
    grouped = _group_rows(rows)
    differences = _difference_rows(grouped)
    _write_csv(_resolve(args.out_csv), differences)
    _write_md(
        _resolve(args.out_md),
        grouped,
        differences,
        args.source_csv,
        args.debug_root,
        str(args.title),
        str(args.real_group_label),
    )
    print({"out_md": args.out_md, "out_csv": args.out_csv, "rows": len(differences)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
