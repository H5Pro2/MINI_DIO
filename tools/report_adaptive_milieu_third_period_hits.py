from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
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


def _index(rows: list[dict[str, str]]) -> dict[tuple[str, str], list[dict[str, str]]]:
    result: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        result[(row.get("family", "-"), row.get("transition", "-"))].append(row)
    return result


def _join_rows(candidates: list[dict[str, str]], third_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    third_index = _index(third_rows)
    result: list[dict[str, object]] = []
    for row in candidates:
        key = (row.get("family", "-"), row.get("transition", "-"))
        matches = third_index.get(key, [])
        if not matches:
            continue
        for match in matches:
            result.append(
                {
                    "family": row.get("family", "-"),
                    "transition": row.get("transition", "-"),
                    "count_2024": row.get("count_2024", "0"),
                    "count_2025": row.get("count_2025", "0"),
                    "world_2023": match.get("world", "-"),
                    "base_total_2023": match.get("base_total", "0"),
                    "follow_total_2023": match.get("follow_total", "0"),
                    "follow_range_2024": row.get("follow_range_2024", "0"),
                    "follow_range_2025": row.get("follow_range_2025", "0"),
                    "follow_range_2023": match.get("follow_avg_range_pct", "0"),
                    "follow_hearing_2024": row.get("follow_hearing_gap_2024", "0"),
                    "follow_hearing_2025": row.get("follow_hearing_gap_2025", "0"),
                    "follow_hearing_2023": match.get("follow_avg_hearing_gap", "0"),
                    "follow_tension_2024": row.get("follow_tension_2024", "0"),
                    "follow_tension_2025": row.get("follow_tension_2025", "0"),
                    "follow_tension_2023": match.get("follow_avg_feld_tension", "0"),
                    "candidate_range_delta_2425": row.get("range_delta_abs", "0"),
                    "candidate_hearing_delta_2425": row.get("hearing_delta_abs", "0"),
                    "candidate_tension_delta_2425": row.get("tension_delta_abs", "0"),
                    "delta_2023_to_2425_range_mid": abs(
                        _float(match.get("follow_avg_range_pct"))
                        - ((_float(row.get("follow_range_2024")) + _float(row.get("follow_range_2025"))) / 2.0)
                    ),
                    "delta_2023_to_2425_hearing_mid": abs(
                        _float(match.get("follow_avg_hearing_gap"))
                        - ((_float(row.get("follow_hearing_gap_2024")) + _float(row.get("follow_hearing_gap_2025"))) / 2.0)
                    ),
                    "delta_2023_to_2425_tension_mid": abs(
                        _float(match.get("follow_avg_feld_tension"))
                        - ((_float(row.get("follow_tension_2024")) + _float(row.get("follow_tension_2025"))) / 2.0)
                    ),
                }
            )
    return result


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: _fmt(value, 6) if isinstance(value, float) else value
                    for key, value in row.items()
                }
            )


def _count_by(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[str(row.get(key, "-"))] += 1
    return dict(sorted(counts.items()))


def _write_md(
    *,
    candidates: list[dict[str, str]],
    hits: list[dict[str, object]],
    out_path: Path,
) -> None:
    _write_csv(hits, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = (
        f"# {title_prefix} - Dritte Periode fuer Wiederkehrfamilien"
        if title_prefix.isdigit()
        else "# Dritte Periode fuer Wiederkehrfamilien"
    )
    unique_hit_keys = {(str(row["family"]), str(row["transition"])) for row in hits}
    transition_counts = _count_by(hits, "transition")
    world_counts = _count_by(hits, "world_2023")
    top_mid = sorted(
        hits,
        key=lambda row: (
            float(row["delta_2023_to_2425_range_mid"])
            + float(row["delta_2023_to_2425_hearing_mid"])
            + float(row["delta_2023_to_2425_tension_mid"]),
            str(row["family"]),
        ),
    )[:30]

    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die 2024/2025-Wiederkehrfamilien in einer dritten Periode erneut mit gleicher Wechselrichtung auftauchen.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Ist die wiederkehrende Familien-/Milieu-Bewegung auch ausserhalb 2024/2025 sichtbar?",
        "2. Unterpruefung: Welche Kandidaten aus 1692 tauchen in 2023 wieder auf?",
        "3. Folgeschritt: Rohweltnahe Treffer ueber weitere Assetfenster verfolgen.",
        "",
        "## Uebersicht",
        "",
        f"- Kandidaten aus 1692: `{len(candidates)}`",
        f"- Treffer in dritter Periode: `{len(unique_hit_keys)}`",
        f"- Trefferquote: `{_fmt(len(unique_hit_keys) / max(1, len(candidates)))}`",
        f"- Trefferzeilen inklusive Mehrfachwelt: `{len(hits)}`",
        "",
        "## Treffer nach Wechseltyp",
        "",
        "| Wechsel | Treffer |",
        "|---|---:|",
    ]
    for transition, count in transition_counts.items():
        lines.append(f"| {transition} | {count} |")

    lines.extend(["", "## Treffer nach 2023-Welt", "", "| Welt | Treffer |", "|---|---:|"])
    for world, count in world_counts.items():
        lines.append(f"| {world} | {count} |")

    lines.extend(
        [
            "",
            "## Rohweltnahe Treffer",
            "",
            "Sortiert nach Naehe des 2023-Folgeprofils zur Mitte aus 2024/2025.",
            "",
            "| Familie | Wechsel | Welt 2023 | Delta Range | Delta Hoeren | Delta Spannung | 2024 | 2025 | 2023 Folge |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in top_mid:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["family"]),
                    str(row["transition"]),
                    str(row["world_2023"]),
                    _fmt(float(row["delta_2023_to_2425_range_mid"])),
                    _fmt(float(row["delta_2023_to_2425_hearing_mid"])),
                    _fmt(float(row["delta_2023_to_2425_tension_mid"])),
                    str(row["count_2024"]),
                    str(row["count_2025"]),
                    str(row["follow_total_2023"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Ein Treffer bedeutet: dieselbe Familie und dieselbe Milieu-Wechselrichtung erscheinen nach 2024/2025 auch in einer dritten Periode.",
            "",
            "Das ist staerker als eine reine Wiederholung der Gesamtverteilung, aber weiterhin kein Ursachebeweis.",
            "",
            "Besonders relevant sind Treffer mit geringer Differenz in Range, Hoeren-Gap und Feldspannung. Dort liegt die naechste Pruefflaeche fuer eine moegliche robuste Milieu-Bewegung.",
            "",
            "## Grenze",
            "",
            "Dieser Bericht zeigt Wiederkehr und Profilnaehe.",
            "Er zeigt noch nicht, ob eine konkrete Weltphase den Wechsel ausloest.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die rohweltnaechsten Treffer einzeln in ihren Episodenabschnitten gelesen werden. Entscheidend ist, ob vor dem Wechsel wiederkehrende Weltspannung, Hoerprofil oder Feldspannung sichtbar wird.",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prueft 1692-Kandidaten gegen eine dritte Periode.")
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--third", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    candidates = _load_csv(_resolve(args.candidates))
    third = _load_csv(_resolve(args.third))
    hits = _join_rows(candidates, third)
    _write_md(candidates=candidates, hits=hits, out_path=_resolve(args.out_md))
    print(
        {
            "out_md": str(_resolve(args.out_md)),
            "candidates": len(candidates),
            "hits": len({(row["family"], row["transition"]) for row in hits}),
            "hit_rows": len(hits),
            "transition_counts": _count_by(hits, "transition"),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
