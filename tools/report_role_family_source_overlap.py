from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _source_families(rows: list[dict[str, str]]) -> set[str]:
    out: set[str] = set()
    for row in rows:
        if row.get("row_type") == "detail" and row.get("kind") == "real" and row.get("family"):
            out.add(str(row["family"]))
    return out


def _build_rows(target_rows: list[dict[str, str]], source_rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    source = _source_families(source_rows)
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in target_rows:
        grouped[str(row.get("role_family", "-"))].append(str(row.get("symbol_family", "-")))

    detail: list[dict[str, object]] = []
    summary: list[dict[str, object]] = []
    for role_family, members in sorted(grouped.items()):
        found = sorted(member for member in members if member in source)
        missing = sorted(member for member in members if member not in source)
        status = "anschluss_genuegend" if len(found) == len(members) else "anschluss_teilweise" if found else "anschluss_fehlend"
        if len(members) <= 1:
            status = "einzelrolle_nicht_ziel"
        summary.append(
            {
                "role_family": role_family,
                "members": len(members),
                "found_members": len(found),
                "missing_members": len(missing),
                "overlap_ratio": f"{len(found) / max(1, len(members)):.6f}",
                "source_overlap_status": status,
                "found_symbols": ";".join(found) or "-",
                "missing_symbols": ";".join(missing[:20]) or "-",
                "boundary": "passive_source_overlap_trace_no_action_no_direction",
            }
        )
        for member in members:
            detail.append(
                {
                    "role_family": role_family,
                    "symbol_family": member,
                    "source_present": "1" if member in source else "0",
                    "source_overlap_status": status,
                    "boundary": "passive_source_overlap_member_trace_no_action_no_direction",
                }
            )

    summary.sort(key=lambda row: (-_safe_int(row["members"]), -_safe_int(row["found_members"]), str(row["role_family"])))
    detail.sort(key=lambda row: (str(row["role_family"]), -_safe_int(row["source_present"]), str(row["symbol_family"])))
    return detail, summary


def _write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _md_table(rows: list[dict[str, object]], fields: list[str], limit: int = 30) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows[:limit]:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, detail: list[dict[str, object]], summary: list[dict[str, object]], source_name: str) -> None:
    total_members = len(detail)
    found_members = sum(_safe_int(row["source_present"]) for row in detail)
    status_counts: dict[str, int] = {}
    for row in summary:
        key = str(row["source_overlap_status"])
        status_counts[key] = status_counts.get(key, 0) + 1

    lines = [
        "# 2067 - Anschlusscheck realverstärkter Rollenfamilien",
        "",
        "## Zweck",
        "",
        "Diese Auswertung prüft, ob die Rollenfamilien aus 2066 direkt gegen eine ältere Folgeweltbasis gelesen werden dürfen.",
        "",
        "Der Test verhindert eine methodische Vermischung: Wenn die Symbolfamilien in der Vergleichsbasis kaum vorkommen, darf daraus keine starke Aussage über Stabilität oder Drift abgeleitet werden.",
        "",
        "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- Vergleichsbasis: `{source_name}`",
        f"- geprüfte 2066-Mitglieder: `{total_members}`",
        f"- in der Vergleichsbasis gefunden: `{found_members}`",
        f"- Statusverteilung: `{dict(sorted(status_counts.items()))}`",
        "",
        "## Rollenfamilien",
        "",
    ]
    lines.extend(
        _md_table(
            summary,
            [
                "role_family",
                "members",
                "found_members",
                "missing_members",
                "overlap_ratio",
                "source_overlap_status",
                "found_symbols",
            ],
            limit=30,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die vorhandene ältere Folgeweltbasis ist nur eingeschränkt anschlussfähig für die 2066-Familien.",
            "",
            "Das ist kein negativer Befund gegen die Rollenfamilien. Es bedeutet methodisch nur: Für eine saubere Familien-Stabilitätsprüfung brauchen wir Folgewelten, die auf derselben Symbolbasis erzeugt oder ausdrücklich daran rückgelesen werden.",
            "",
            "## Grenze",
            "",
            "Dieser Report bewertet nicht die Qualität der Familien. Er bewertet nur, ob eine Vergleichsbasis ausreichend überlappt.",
            "",
            "Wie es weitergeht: Als nächstes sollten neue Folgeweltläufe mit derselben 2066-Symbolbasis erzeugt oder ein Rückleser gebaut werden, der die 2066-Familien explizit in vorhandenen Weltfenstern sucht.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="docs/befunde/2001-3000/2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.detail.csv")
    parser.add_argument("--source", default="docs/befunde/1001-2000/1751-2000/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv")
    parser.add_argument("--out-prefix", default="2067_REALVERSTAERKTE_ROLLENFAMILIEN_ANSCHLUSSCHECK")
    args = parser.parse_args()

    detail, summary = _build_rows(_load_csv(Path(args.target)), _load_csv(Path(args.source)))
    _write_csv(
        BEFUNDE / f"{args.out_prefix}.detail.csv",
        detail,
        ["role_family", "symbol_family", "source_present", "source_overlap_status", "boundary"],
    )
    _write_csv(
        BEFUNDE / f"{args.out_prefix}.summary.csv",
        summary,
        [
            "role_family",
            "members",
            "found_members",
            "missing_members",
            "overlap_ratio",
            "source_overlap_status",
            "found_symbols",
            "missing_symbols",
            "boundary",
        ],
    )
    _write_markdown(
        BEFUNDE / f"{args.out_prefix}.md",
        detail,
        summary,
        str(Path(args.source)),
    )
    print(f"members={len(detail)}")
    print(f"found={sum(_safe_int(row['source_present']) for row in detail)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
