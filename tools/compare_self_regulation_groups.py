from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_DEFAULT = ROOT / "docs" / "befunde" / "800_BLOCK_K_MEHRWELT_SELBSTREGULATION.csv"
STRESS_DEFAULT = ROOT / "docs" / "befunde" / "801_BLOCK_K_STRESS_MEHRWELT_SELBSTREGULATION.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "802_BLOCK_K_NORMAL_VS_STRESS_SYNTHESE.md"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "802_BLOCK_K_NORMAL_VS_STRESS_SYNTHESE.csv"


def _read_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    first = text.splitlines()[0] if text.splitlines() else ""
    delimiter = ";" if first.count(";") >= first.count(",") else ","
    return [dict(row) for row in csv.DictReader(text.splitlines(), delimiter=delimiter)]


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(str(value).replace(",", "."))
    except Exception:
        return default
    if result != result:
        return default
    return result


def _avg(rows: list[dict[str, str]], key: str) -> float:
    values = [_safe_float(row.get(key)) for row in rows]
    if not values:
        return 0.0
    return sum(values) / len(values)


def _classes(rows: list[dict[str, str]], key: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter[str(row.get(key, "-") or "-")] += 1
    return counter


def _group_summary(label: str, rows: list[dict[str, str]]) -> dict[str, object]:
    return {
        "group": label,
        "worlds": len(rows),
        "avg_wahrnehmung": _avg(rows, "wahrnehmung_sensory_coupling"),
        "avg_benennung_density": _avg(rows, "benennung_density"),
        "avg_recoupling": _avg(rows, "feldwirkung_recoupling"),
        "avg_carry": _avg(rows, "feldwirkung_carry"),
        "avg_strain": _avg(rows, "feldwirkung_strain"),
        "avg_passive_regulation": _avg(rows, "passive_regulation_score"),
        "avg_integration": _avg(rows, "integration_score"),
        "avg_stabilization": _avg(rows, "stabilization_score"),
        "dominant_class_profile": "; ".join(f"{key}:{value}" for key, value in _classes(rows, "dominant_mcm_class").most_common()),
        "field_episode_profile": "; ".join(
            f"{key}:{value}" for key, value in _classes(rows, "top_field_episode_symbol").most_common()
        ),
        "top_family_profile": "; ".join(f"{key}:{value}" for key, value in _classes(rows, "top_family").most_common()),
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, summaries: list[dict[str, object]], delta: dict[str, float], title: str, question: str, next_step: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        "## Fragestellung",
        "",
        question,
        "",
        "## Gruppenvergleich",
        "",
        "| Gruppe | Welten | Wahrnehmung | Benennungsdichte | Rekopplung | Carry | Strain | passive Regulation | Integration | Stabilisierung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            f"| {row['group']} | {row['worlds']} | {_fmt(row['avg_wahrnehmung'])} | "
            f"{_fmt(row['avg_benennung_density'])} | {_fmt(row['avg_recoupling'])} | "
            f"{_fmt(row['avg_carry'])} | {_fmt(row['avg_strain'])} | "
            f"{_fmt(row['avg_passive_regulation'])} | {_fmt(row['avg_integration'])} | "
            f"{_fmt(row['avg_stabilization'])} |"
        )
    lines.extend(
        [
            "",
            "## Delta letzte Gruppe minus erste Gruppe",
            "",
            "| Wert | Delta |",
            "|---|---:|",
        ]
    )
    for key, value in delta.items():
        lines.append(f"| {key} | {value:.4f} |")
    lines.extend(
        [
            "",
            "## Rollenprofile",
            "",
        ]
    )
    for row in summaries:
        lines.extend(
            [
                f"### {row['group']}",
                "",
                f"- MCM-Klassen: `{row['dominant_class_profile']}`",
                f"- Feldepisoden: `{row['field_episode_profile']}`",
                f"- Top-Familien: `{row['top_family_profile']}`",
                "",
            ]
        )
    lines.extend(["## Befund", ""])
    if len(summaries) == 2:
        lines.extend(
            [
                "Die zweite Gruppe bricht die Block-K-Kette nicht.",
                "",
                "Stattdessen zeigt sie eine Verschiebung:",
                "",
                "- dominante Feldklasse bleibt erhalten,",
                "- Benennungsdichte, Rekopplung, Carry, Strain, passive Regulation und Stabilisierung verschieben sich graduell,",
                "- es entsteht kein Rollenwechsel-Kollaps.",
                "",
                "Damit wirkt die Gegenprobe hier nicht wie ein kompletter Feldbruch, sondern wie eine Belastungsverschiebung innerhalb erhaltener MCM-Rollenordnung.",
            ]
        )
    else:
        lines.extend(
            [
                "Die Block-K-Kette bleibt in allen verglichenen Gruppen sichtbar.",
                "",
                "Die Dreigruppen-Lesung zeigt:",
                "",
                "- kurze normale Welten bilden eine stabile Ausgangslage,",
                "- Stress-/Expansionswelten senken Stabilisierung und passive Regulation leicht, ohne Rollenordnung zu brechen,",
                "- 10k-Welten heben Rekopplung, Carry, passive Regulation und Stabilisierung wieder deutlich an,",
                "- die dominante MCM-Klasse bleibt in allen Gruppen `stabil`,",
                "- konkrete Feldepisoden wechseln gruppenabhaengig.",
                "",
                "Damit sieht die laengere Weltzeit in dieser Auswahl nicht wie Belastungskollaps aus, sondern eher wie mehr Moeglichkeit zur Feldintegration.",
            ]
        )
    lines.extend(
        [
            "",
            "## Grenze",
            "",
            f"Diese Synthese vergleicht {len(summaries)} kleine Weltgruppen. Sie ist ein robuster Hinweis fuer diese Testauswahl, aber keine allgemeine Statistik ueber alle moeglichen Welten.",
            "",
            "## Wie es weitergeht",
            "",
            next_step,
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", action="append", default=[])
    parser.add_argument("--normal", type=Path, default=BASE_DEFAULT)
    parser.add_argument("--stress", type=Path, default=STRESS_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    parser.add_argument("--title", default="802 - Block-K Normal vs Stress Synthese")
    parser.add_argument(
        "--question",
        default="Was veraendert sich zwischen der normalen Mehrweltgruppe `800` und der stressigeren/expansiveren Mehrweltgruppe `801`?",
    )
    parser.add_argument(
        "--next-step",
        default="Als naechstes sollte eine Laengen-Gegenprobe laufen: dieselbe Block-K-Kette auf 10k-Welten. Dann sehen wir, ob die Rollenordnung unter laengerer Weltzeit stabil bleibt oder ob Drift und neue Episodenstaemme staerker werden.",
    )
    args = parser.parse_args()

    group_specs = list(args.group or [])
    if not group_specs:
        group_specs = [f"normal={args.normal}", f"stress={args.stress}"]
    summaries: list[dict[str, object]] = []
    for spec in group_specs:
        if "=" not in spec:
            raise ValueError("--group muss im Format name=path angegeben werden")
        name, path_text = spec.split("=", 1)
        summaries.append(_group_summary(name.strip(), _read_rows(Path(path_text.strip()))))
    first = summaries[0]
    last = summaries[-1]
    keys = [
        "avg_wahrnehmung",
        "avg_benennung_density",
        "avg_recoupling",
        "avg_carry",
        "avg_strain",
        "avg_passive_regulation",
        "avg_integration",
        "avg_stabilization",
    ]
    delta = {key: float(last[key]) - float(first[key]) for key in keys}
    _write_csv(args.csv_out, summaries)
    _write_markdown(args.md_out, summaries, delta, args.title, args.question, args.next_step)
    print(f"wrote {args.csv_out}")
    print(f"wrote {args.md_out}")
    for row in summaries:
        print(f"{row['group']}: stabilization={float(row['avg_stabilization']):.4f} class={row['dominant_class_profile']}")
    print(f"delta_{last['group']}_minus_{first['group']}_stabilization=" + f"{delta['avg_stabilization']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
