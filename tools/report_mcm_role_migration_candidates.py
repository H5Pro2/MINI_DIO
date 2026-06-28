from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _migration(row: dict[str, str]) -> str:
    base = row.get("base_class", "-")
    compare = row.get("compare_class", "-")
    base_rank = CLASS_RANK.get(base, 0)
    compare_rank = CLASS_RANK.get(compare, 0)
    if base == compare:
        return "stabile_rolle"
    if base_rank == 0 and compare_rank > 0:
        return "neue_rolle"
    if base_rank > 0 and compare_rank == 0:
        return "rolle_zerfallen"
    if compare_rank > base_rank:
        return "rolle_verdichtet"
    if compare_rank < base_rank:
        return "rolle_entlastet_oder_driftet"
    return "rolle_umorganisiert"


def _annotate(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        base_weight = _int(row.get("base_weight", "0"))
        compare_weight = _int(row.get("compare_weight", "0"))
        base_duration = _float(row.get("base_duration", "0"))
        compare_duration = _float(row.get("compare_duration", "0"))
        migration = _migration(row)
        out.append(
            {
                **row,
                "migration": migration,
                "weight_delta": str(compare_weight - base_weight),
                "duration_delta": f"{compare_duration - base_duration:.6f}",
            }
        )
    out.sort(
        key=lambda row: (
            row["migration"] not in {"rolle_verdichtet", "neue_rolle"},
            -_int(row.get("weight_delta", "0")),
            row.get("short_token", ""),
        )
    )
    return out


def _top(rows: list[dict[str, str]], migration: str, limit: int = 12) -> list[dict[str, str]]:
    return [row for row in rows if row["migration"] == migration][:limit]


def _table(rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| Token | Basisrolle | Vergleichsrolle | Gewicht Delta | Dauer Delta |",
        "|---|---|---|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row.get('short_token', '-')}` | {row.get('base_class', '-')} | {row.get('compare_class', '-')} | {row.get('weight_delta', '0')} | {_float(row.get('duration_delta', '0')):.2f} |"
        )
    return lines


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["migration"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Rollenwanderung Kandidaten")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose fasst zusammen, welche Tokens zwischen 894 und 901 ihre topologische Rolle wechseln.")
    lines.append("Damit wird geprueft, ob `0b7nep9` ein Einzelphaenomen ist oder Teil einer allgemeinen Rollenwanderung.")
    lines.append("")
    lines.append("## Profil")
    lines.append("")
    lines.append("| Migration | Anzahl |")
    lines.append("|---|---:|")
    for name, count in counts.most_common():
        lines.append(f"| {name} | {count} |")
    lines.append("")
    lines.append("## Verdichtende Rollen")
    lines.append("")
    lines.extend(_table(_top(rows, "rolle_verdichtet")))
    lines.append("")
    lines.append("## Neue Rollen")
    lines.append("")
    lines.extend(_table(_top(rows, "neue_rolle")))
    lines.append("")
    lines.append("## Entlastende Oder Driftende Rollen")
    lines.append("")
    lines.extend(_table(_top(rows, "rolle_entlastet_oder_driftet")))
    lines.append("")
    lines.append("## Zerfallende Rollen")
    lines.append("")
    lines.extend(_table(_top(rows, "rolle_zerfallen")))
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Rollenwanderung ist kein Einzelereignis. Mehrere Tokens verdichten sich von schwachen oder lokalen Anschlussrollen in starke Anschlussanker oder Brueckenkerne.")
    lines.append("Gleichzeitig zerfallen andere Rollen oder entlasten sich. Das passt zu einer dynamischen MCM-Topologie: Rollen werden durch Weltspannung, Nachbarschaft und Feldkopplung getragen, nicht durch eine fixe Token-Eigenschaft.")
    lines.append("")
    lines.append("Besonders relevant:")
    lines.append("")
    lines.append("- `0b7nep9`: starker Anschlussanker -> Brueckenkern.")
    lines.append("- `0ykar6i`: schwacher Anschluss -> Brueckenkern.")
    lines.append("- `1jx2k4i`: starker Anschlussanker -> Brueckenkern.")
    lines.append("- `1xx3u1e`: lokaler Anschlussanker -> Brueckenkern.")
    lines.append("- `0z748ck`: lokaler Anschlussanker -> Brueckenkern.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte eine einzelne zweite Rollenwanderung isoliert werden, vorzugsweise `0ykar6i`, weil es vom schwachen Anschluss zum Kernpartner von `0b7nep9` wird.")
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _annotate(_read(args.roles))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
