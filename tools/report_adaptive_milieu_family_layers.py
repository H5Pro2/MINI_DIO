from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean


ROOT = Path(__file__).resolve().parents[1]


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
        return list(csv.DictReader(handle))


def _family(row: dict[str, str]) -> str:
    for key in ("symbol_family", "mcm_field_episode_preview_symbol", "mcm_field_episode_symbol"):
        value = (row.get(key) or "").strip()
        if value:
            return value[:12]
    symbol = (row.get("symbol") or row.get("episode_memory_symbol") or "").strip()
    return symbol[:12] if symbol else "-"


def _layer(milieu: str) -> str:
    if milieu == "milieu_offen":
        return "offen"
    if milieu in {"milieu_rollennah", "milieu_pfadnah", "milieu_rolle_und_pfad_getragen"}:
        return "gereift"
    if milieu == "milieu_untrained":
        return "untrainiert"
    return "sonstig"


def _load_world(name: str, path: Path) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    rows = _load_rows(path)
    family_layers: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    layer_counts = Counter()
    milieu_counts = Counter()
    for row in rows:
        milieu = row.get("mcm_adaptive_milieu_state", "") or "-"
        layer = _layer(milieu)
        family = _family(row)
        family_layers[family][layer].append(row)
        layer_counts[layer] += 1
        milieu_counts[milieu] += 1

    family_rows: list[dict[str, object]] = []
    for family, layers in family_layers.items():
        open_rows = layers.get("offen", [])
        mature_rows = layers.get("gereift", [])
        total = sum(len(items) for items in layers.values())
        if total <= 0:
            continue
        open_count = len(open_rows)
        mature_count = len(mature_rows)
        shared = open_count > 0 and mature_count > 0
        if shared:
            relation = "offen_und_gereift"
        elif open_count > 0:
            relation = "nur_offen"
        elif mature_count > 0:
            relation = "nur_gereift"
        else:
            relation = "sonstig"
        all_rows = [row for items in layers.values() for row in items]
        family_rows.append(
            {
                "world": name,
                "family": family,
                "relation": relation,
                "total": total,
                "open_count": open_count,
                "mature_count": mature_count,
                "open_share": open_count / total,
                "mature_share": mature_count / total,
                "avg_rekopplung": _mean([_float(row.get("mcm_rekopplung_quality")) for row in all_rows]),
                "avg_adaptive_rekopplung": _mean([_float(row.get("mcm_adaptive_rekopplung_quality")) for row in all_rows]),
                "avg_strain": _mean([_float(row.get("mcm_strain_quality")) for row in all_rows]),
                "avg_role_experience": _mean([_float(row.get("mcm_adaptive_role_experience")) for row in all_rows]),
                "avg_path_experience": _mean([_float(row.get("mcm_adaptive_path_experience")) for row in all_rows]),
            }
        )

    relation_counts = Counter(str(row["relation"]) for row in family_rows)
    shared_families = sum(1 for row in family_rows if row["relation"] == "offen_und_gereift")
    open_only = sum(1 for row in family_rows if row["relation"] == "nur_offen")
    mature_only = sum(1 for row in family_rows if row["relation"] == "nur_gereift")
    total_families = len(family_rows)
    summary = {
        "world": name,
        "ticks": len(rows),
        "families": total_families,
        "shared_families": shared_families,
        "open_only_families": open_only,
        "mature_only_families": mature_only,
        "shared_family_ratio": shared_families / max(1, total_families),
        "open_ticks": layer_counts["offen"],
        "mature_ticks": layer_counts["gereift"],
        "untrained_ticks": layer_counts["untrainiert"],
        "open_tick_ratio": layer_counts["offen"] / max(1, len(rows)),
        "mature_tick_ratio": layer_counts["gereift"] / max(1, len(rows)),
        "milieu_counts": dict(milieu_counts),
        "relation_counts": dict(relation_counts),
    }
    return family_rows, _top_rows(family_rows), summary


def _top_rows(rows: list[dict[str, object]], limit: int = 20) -> list[dict[str, object]]:
    priority = {"offen_und_gereift": 0, "nur_gereift": 1, "nur_offen": 2, "sonstig": 3}
    return sorted(rows, key=lambda row: (priority.get(str(row["relation"]), 9), -int(row["total"]), str(row["family"])))[:limit]


def _write_csv(rows: list[dict[str, object]], summaries: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "world",
        "family",
        "relation",
        "total",
        "open_count",
        "mature_count",
        "open_share",
        "mature_share",
        "avg_rekopplung",
        "avg_adaptive_rekopplung",
        "avg_strain",
        "avg_role_experience",
        "avg_path_experience",
    ]
    with out_path.with_suffix(".csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in fields})

    summary_fields = [
        "world",
        "ticks",
        "families",
        "shared_families",
        "open_only_families",
        "mature_only_families",
        "shared_family_ratio",
        "open_ticks",
        "mature_ticks",
        "untrained_ticks",
        "open_tick_ratio",
        "mature_tick_ratio",
    ]
    with out_path.with_name(out_path.stem + "_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        writer.writeheader()
        for row in summaries:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in summary_fields})


def _write_md(rows: list[dict[str, object]], top_rows: list[dict[str, object]], summaries: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, summaries, out_path)
    lines = [
        "# Adaptive Milieu-Familienlagen",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob `milieu_offen` dieselben Familien beruehrt wie gereifte Milieus oder als eigene Varianzschicht getrennt bleibt.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Ist Offenheit eine eigene Schicht oder ein Vorraum gereifter Familien?",
        "2. Unterpruefung: Familien nach `nur_offen`, `nur_gereift` und `offen_und_gereift` trennen.",
        "3. Folgeschritt: Wenn gemeinsame Familien dominieren, offene Milieus als Varianzschicht ueber stabilen Rollen lesen.",
        "",
        "## Weltuebersicht",
        "",
        "| Welt | Ticks | Familien | Offen+Gereift | Nur offen | Nur gereift | Anteil Offen+Gereift | Offen-Ticks | Gereift-Ticks |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for summary in summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(summary["world"]),
                    str(summary["ticks"]),
                    str(summary["families"]),
                    str(summary["shared_families"]),
                    str(summary["open_only_families"]),
                    str(summary["mature_only_families"]),
                    _fmt(float(summary["shared_family_ratio"])),
                    str(summary["open_ticks"]),
                    str(summary["mature_ticks"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Staerkste Familienlagen",
            "",
            "| Welt | Familie | Relation | Gesamt | Offen | Gereift | Offen-Anteil | Gereift-Anteil | Rekopplung | Adaptive Rekopplung | Strain |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["world"]),
                    str(row["family"]),
                    str(row["relation"]),
                    str(row["total"]),
                    str(row["open_count"]),
                    str(row["mature_count"]),
                    _fmt(float(row["open_share"])),
                    _fmt(float(row["mature_share"])),
                    _fmt(float(row["avg_rekopplung"])),
                    _fmt(float(row["avg_adaptive_rekopplung"])),
                    _fmt(float(row["avg_strain"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn dieselbe Familie sowohl offen als auch gereift erscheint, ist Offenheit keine isolierte Stoerung.",
            "Sie wirkt dann eher wie eine wechselnde Varianzschicht ueber einer wiederkehrenden Rollenfamilie.",
            "",
            "Wenn Familien nur offen erscheinen, bleibt die Lage dagegen noch ungebunden oder jung.",
            "",
            "## Grenze",
            "",
            "Diese Diagnose beschreibt nur passive Milieu-Schichtung.",
            "Sie erzeugt keine Handlung und bewertet Offenheit nicht als Fehler.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", action="append", nargs=2, metavar=("NAME", "EPISODES"), required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    all_top: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for name, path_text in args.world:
        rows, top_rows, summary = _load_world(name, _resolve(path_text))
        all_rows.extend(rows)
        all_top.extend(top_rows)
        summaries.append(summary)

    _write_md(all_rows, all_top, summaries, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(all_rows), "worlds": len(summaries)})


if __name__ == "__main__":
    main()
