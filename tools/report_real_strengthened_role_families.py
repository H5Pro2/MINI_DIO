from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
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


def _fmt(value: float) -> str:
    return f"{value:.6f}"


def _parse_mcm(value: str) -> tuple[float, float, float]:
    parts = str(value or "").split("/")
    while len(parts) < 3:
        parts.append("0")
    return (_safe_float(parts[0]), _safe_float(parts[1]), _safe_float(parts[2]))


def _labels(value: str) -> set[str]:
    out: set[str] = set()
    for part in str(value or "").split(";"):
        if not part or ":" not in part:
            continue
        key, _ = part.split(":", 1)
        out.add(key.strip())
    return out


def _distance(left: tuple[float, float, float], right: tuple[float, float, float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    return len(left & right) / max(1, len(left | right))


def _nearest_threshold(records: list[dict[str, object]]) -> float:
    if len(records) <= 1:
        return 0.0
    nearest: list[float] = []
    for left in records:
        distances = [
            _distance(left["mcm"], right["mcm"])  # type: ignore[arg-type]
            for right in records
            if left is not right
        ]
        if distances:
            nearest.append(min(distances))
    nearest.sort()
    if not nearest:
        return 0.0
    median = nearest[len(nearest) // 2]
    return median * 1.35


def _records(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row in rows:
        if row.get("follow_status") not in {"folge_stabil_feldgleich", "folge_offen_feldgleich"}:
            continue
        out.append(
            {
                "symbol_family": row.get("symbol_family", "-"),
                "follow_status": row.get("follow_status", "-"),
                "seed_ratio": _safe_float(row.get("seed_ratio")),
                "seed_real_events": _safe_int(row.get("seed_real_events")),
                "seed_null_events": _safe_int(row.get("seed_null_events")),
                "follow_events": _safe_int(row.get("follow_events")),
                "follow_labels": row.get("follow_labels", "-"),
                "follow_label_set": _labels(row.get("follow_labels", "")),
                "follow_field": row.get("follow_field", "-"),
                "follow_reifung": row.get("follow_reifung", "-"),
                "mcm": _parse_mcm(row.get("follow_mcm", "")),
                "follow_mcm": row.get("follow_mcm", "-"),
            }
        )
    return out


def _components(records: list[dict[str, object]]) -> dict[str, int]:
    threshold = _nearest_threshold(records)
    adjacency: dict[str, set[str]] = defaultdict(set)
    for i, left in enumerate(records):
        left_name = str(left["symbol_family"])
        adjacency[left_name].add(left_name)
        for right in records[i + 1 :]:
            right_name = str(right["symbol_family"])
            dist = _distance(left["mcm"], right["mcm"])  # type: ignore[arg-type]
            label_jaccard = _jaccard(left["follow_label_set"], right["follow_label_set"])  # type: ignore[arg-type]
            if dist <= threshold and label_jaccard >= 0.45:
                adjacency[left_name].add(right_name)
                adjacency[right_name].add(left_name)
    component_by_family: dict[str, int] = {}
    component_id = 0
    for record in sorted(records, key=lambda item: str(item["symbol_family"])):
        family = str(record["symbol_family"])
        if family in component_by_family:
            continue
        component_id += 1
        stack = [family]
        while stack:
            current = stack.pop()
            if current in component_by_family:
                continue
            component_by_family[current] = component_id
            stack.extend(sorted(adjacency[current] - set(component_by_family)))
    return component_by_family


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _build_rows(records: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    component_by_family = _components(records)
    detail: list[dict[str, object]] = []
    for record in records:
        carry, strain, rekopplung = record["mcm"]  # type: ignore[misc]
        detail.append(
            {
                "role_family": f"rf_{component_by_family[str(record['symbol_family'])]:02d}",
                "symbol_family": record["symbol_family"],
                "follow_status": record["follow_status"],
                "seed_ratio": _fmt(_safe_float(record["seed_ratio"])),
                "seed_real_events": record["seed_real_events"],
                "seed_null_events": record["seed_null_events"],
                "follow_events": record["follow_events"],
                "follow_field": record["follow_field"],
                "follow_reifung": record["follow_reifung"],
                "carry": _fmt(carry),
                "strain": _fmt(strain),
                "rekopplung": _fmt(rekopplung),
                "follow_labels": record["follow_labels"],
                "boundary": "passive_role_family_trace_no_action_no_direction",
            }
        )
    detail.sort(key=lambda row: (str(row["role_family"]), -_safe_int(row["follow_events"]), str(row["symbol_family"])))

    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        grouped[str(row["role_family"])].append(row)
    summary: list[dict[str, object]] = []
    for role_family, bucket in grouped.items():
        label_counter: Counter[str] = Counter()
        for row in bucket:
            label_counter.update(_labels(str(row["follow_labels"])))
        summary.append(
            {
                "role_family": role_family,
                "families": len(bucket),
                "members": ";".join(str(row["symbol_family"]) for row in bucket[:12]),
                "total_follow_events": sum(_safe_int(row["follow_events"]) for row in bucket),
                "avg_seed_ratio": _fmt(_mean([_safe_float(row["seed_ratio"]) for row in bucket])),
                "avg_carry": _fmt(_mean([_safe_float(row["carry"]) for row in bucket])),
                "avg_strain": _fmt(_mean([_safe_float(row["strain"]) for row in bucket])),
                "avg_rekopplung": _fmt(_mean([_safe_float(row["rekopplung"]) for row in bucket])),
                "top_follow_labels": ";".join(f"{key}:{value}" for key, value in label_counter.most_common(8)),
            }
        )
    summary.sort(key=lambda row: (-_safe_int(row["families"]), -_safe_int(row["total_follow_events"]), str(row["role_family"])))
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


def _write_markdown(path: Path, detail: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    multi = [row for row in summary if _safe_int(row["families"]) > 1]
    lines = [
        "# 2065 - Rollenfamilien realverstärkter Folgewelt-Rollen",
        "",
        "## Zweck",
        "",
        "Diese Auswertung prüft, ob die realverstärkten und in Folgewelten feldgleich stabilen Rollen nur Einzelzeichen sind oder nähere Rollenfamilien bilden.",
        "",
        "Gruppiert wird passiv über Nähe der MCM-Folgeweltwirkung und gemeinsame Folgewelt-Präsenz. Die Prüfung erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte Einzelrollen: `{len(detail)}`",
        f"- Rollenfamilien gesamt: `{len(summary)}`",
        f"- Mehrrollen-Familien: `{len(multi)}`",
        "",
        "## Rollenfamilien",
        "",
    ]
    lines.extend(
        _md_table(
            summary,
            [
                "role_family",
                "families",
                "total_follow_events",
                "avg_seed_ratio",
                "avg_carry",
                "avg_strain",
                "avg_rekopplung",
                "members",
            ],
            limit=30,
        )
    )
    lines.extend(["", "## Detail", ""])
    lines.extend(
        _md_table(
            detail,
            [
                "role_family",
                "symbol_family",
                "follow_status",
                "seed_ratio",
                "follow_events",
                "carry",
                "strain",
                "rekopplung",
            ],
            limit=50,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Wenn mehrere Rollen in derselben Familie liegen, ist das kein einzelnes Wort mehr, sondern ein kleiner Bedeutungsraum mit gemeinsamer Feldfunktion.",
            "",
            "Wenn eine Rolle allein bleibt, ist sie weiterhin eine isolierte Spur. Das kann stark sein, aber es zeigt noch keine interne Bedeutungsbreite.",
            "",
            "## Grenze",
            "",
            "Die Familienbildung ist diagnostisch. Sie ist kein Mechanismus im Organismus und keine Vorgabe für Verhalten.",
            "",
            "Wie es weitergeht: Als nächstes sollten die Mehrrollen-Familien gegen neue Folgewelten geprüft werden. Entscheidend ist, ob ganze Familien stabil bleiben oder ob nur einzelne Mitglieder weitergetragen werden.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="docs/befunde/2001-3000/2064_REALVERSTAERKTE_ROLLEN_IN_FOLGEWELTEN.detail.csv")
    parser.add_argument("--out-prefix", default="2065_REALVERSTAERKTE_FOLGEWELT_ROLLENFAMILIEN")
    args = parser.parse_args()

    detail, summary = _build_rows(_records(_load_csv(Path(args.source))))
    detail_fields = [
        "role_family",
        "symbol_family",
        "follow_status",
        "seed_ratio",
        "seed_real_events",
        "seed_null_events",
        "follow_events",
        "follow_field",
        "follow_reifung",
        "carry",
        "strain",
        "rekopplung",
        "follow_labels",
        "boundary",
    ]
    summary_fields = [
        "role_family",
        "families",
        "members",
        "total_follow_events",
        "avg_seed_ratio",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "top_follow_labels",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", detail, detail_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", detail, summary)
    print(f"roles={len(detail)}")
    print(f"role_families={len(summary)}")
    print(f"multi_role_families={sum(1 for row in summary if _safe_int(row['families']) > 1)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
