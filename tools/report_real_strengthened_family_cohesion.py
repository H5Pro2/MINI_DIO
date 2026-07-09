from __future__ import annotations

import argparse
import csv
import math
from itertools import combinations
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


def _labels(value: str) -> set[str]:
    labels: set[str] = set()
    for part in str(value or "").split(";"):
        if not part or ":" not in part:
            continue
        key, _ = part.split(":", 1)
        labels.add(key.strip())
    return labels


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    return len(left & right) / max(1, len(left | right))


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _distance(left: tuple[float, float, float], right: tuple[float, float, float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _family_reading(
    *,
    shared_label_count: int,
    mean_label_jaccard: float,
    event_concentration: float,
) -> str:
    if shared_label_count > 0 and event_concentration < 0.65:
        return "familie_breit_getragen"
    if shared_label_count > 0:
        return "familie_kernlastig_getragen"
    if mean_label_jaccard >= 0.50:
        return "familie_nachbarschaft_getragen"
    return "familie_fragmentiert_offen"


def _build_rows(source_rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in source_rows:
        role_family = str(row.get("role_family", "-"))
        grouped.setdefault(role_family, []).append(row)

    detail: list[dict[str, object]] = []
    summary: list[dict[str, object]] = []
    for role_family, bucket in sorted(grouped.items()):
        if len(bucket) <= 1:
            continue
        label_sets = [_labels(row.get("follow_labels", "")) for row in bucket]
        label_support: dict[str, int] = {}
        for labels in label_sets:
            for label in labels:
                label_support[label] = label_support.get(label, 0) + 1

        shared_labels = sorted(label for label, count in label_support.items() if count == len(bucket))
        majority_labels = sorted(label for label, count in label_support.items() if count >= math.ceil(len(bucket) / 2))
        pair_scores = [_jaccard(left, right) for left, right in combinations(label_sets, 2)]

        events = [_safe_int(row.get("follow_events")) for row in bucket]
        total_events = sum(events)
        event_concentration = max(events) / total_events if total_events else 0.0

        points = [
            (
                _safe_float(row.get("carry")),
                _safe_float(row.get("strain")),
                _safe_float(row.get("rekopplung")),
            )
            for row in bucket
        ]
        center = tuple(_mean([point[i] for point in points]) for i in range(3))
        distances = [_distance(point, center) for point in points]

        mean_label_jaccard = _mean(pair_scores)
        reading = _family_reading(
            shared_label_count=len(shared_labels),
            mean_label_jaccard=mean_label_jaccard,
            event_concentration=event_concentration,
        )

        summary.append(
            {
                "role_family": role_family,
                "members": len(bucket),
                "total_follow_events": total_events,
                "event_concentration": _fmt(event_concentration),
                "shared_label_count": len(shared_labels),
                "majority_label_count": len(majority_labels),
                "mean_label_jaccard": _fmt(mean_label_jaccard),
                "min_label_jaccard": _fmt(min(pair_scores) if pair_scores else 1.0),
                "max_mcm_distance": _fmt(max(distances) if distances else 0.0),
                "mean_mcm_distance": _fmt(_mean(distances)),
                "avg_carry": _fmt(center[0]),
                "avg_strain": _fmt(center[1]),
                "avg_rekopplung": _fmt(center[2]),
                "family_reading": reading,
                "shared_labels": ";".join(shared_labels[:12]) or "-",
                "majority_labels": ";".join(majority_labels[:12]) or "-",
                "member_symbols": ";".join(str(row.get("symbol_family", "-")) for row in bucket),
                "boundary": "passive_family_cohesion_trace_no_action_no_direction",
            }
        )

        for row, labels in zip(bucket, label_sets):
            detail.append(
                {
                    "role_family": role_family,
                    "symbol_family": row.get("symbol_family", "-"),
                    "family_reading": reading,
                    "follow_events": _safe_int(row.get("follow_events")),
                    "event_share": _fmt(_safe_int(row.get("follow_events")) / total_events if total_events else 0.0),
                    "shared_label_hits": len(labels & set(shared_labels)),
                    "majority_label_hits": len(labels & set(majority_labels)),
                    "carry": row.get("carry", "0"),
                    "strain": row.get("strain", "0"),
                    "rekopplung": row.get("rekopplung", "0"),
                    "follow_labels": row.get("follow_labels", "-"),
                    "boundary": "passive_family_member_cohesion_trace_no_action_no_direction",
                }
            )

    summary.sort(
        key=lambda row: (
            str(row["family_reading"]),
            -_safe_int(row["members"]),
            -_safe_int(row["total_follow_events"]),
            str(row["role_family"]),
        )
    )
    detail.sort(key=lambda row: (str(row["role_family"]), -_safe_int(row["follow_events"]), str(row["symbol_family"])))
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
    reading_counts: dict[str, int] = {}
    for row in summary:
        key = str(row["family_reading"])
        reading_counts[key] = reading_counts.get(key, 0) + 1

    lines = [
        "# 2066 - Kohäsion realverstärkter Rollenfamilien",
        "",
        "## Zweck",
        "",
        "Diese Auswertung prüft die Mehrrollen-Familien aus 2065 als kleine Bedeutungsräume.",
        "",
        "Gefragt wird nicht, ob eine Einzelrolle wieder auftaucht, sondern ob eine ganze Rollenfamilie gemeinsame Folgewelt-Präsenz, ähnliche MCM-Wirkung und verteilte Ereignistragung zeigt.",
        "",
        "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte Mehrrollen-Familien: `{len(summary)}`",
        f"- geprüfte Rollenmitglieder: `{len(detail)}`",
        f"- Lesungsverteilung: `{dict(sorted(reading_counts.items()))}`",
        "",
        "## Familienkohäsion",
        "",
    ]
    lines.extend(
        _md_table(
            summary,
            [
                "role_family",
                "members",
                "total_follow_events",
                "event_concentration",
                "shared_label_count",
                "mean_label_jaccard",
                "max_mcm_distance",
                "family_reading",
                "member_symbols",
            ],
            limit=30,
        )
    )
    lines.extend(["", "## Mitglieder", ""])
    lines.extend(
        _md_table(
            detail,
            [
                "role_family",
                "symbol_family",
                "family_reading",
                "follow_events",
                "event_share",
                "shared_label_hits",
                "majority_label_hits",
            ],
            limit=60,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Eine breit getragene Familie ist stärker als ein isoliertes Zeichen: mehrere nahe Rollen werden in ähnlichen Welten und mit ähnlicher Feldwirkung weitergetragen.",
            "",
            "Eine kernlastige Familie ist noch nicht falsch, aber sie hängt stärker an einem dominanten Mitglied. Das spricht eher für eine Rolleninsel mit Kern und Nebenfragmenten.",
            "",
            "Fragmentierte Familien bleiben offene Bedeutungsräume. Sie zeigen Nähe, aber noch keine ausreichend gemeinsame Folgewelt-Tragung.",
            "",
            "## Grenze",
            "",
            "Die Klassen sind diagnostische Lesarten. Sie sind keine Regel, keine Handlungsvorgabe und keine Aussage über spätere Motorik.",
            "",
            "Wie es weitergeht: Als nächstes sollten die breit getragenen und kernlastigen Familien gegen zusätzliche reale Weltfenster geprüft werden. Entscheidend ist, ob die Familienstruktur erhalten bleibt oder ob nur einzelne Mitglieder weiterleben.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="docs/befunde/2001-3000/2065_REALVERSTAERKTE_FOLGEWELT_ROLLENFAMILIEN.detail.csv")
    parser.add_argument("--out-prefix", default="2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION")
    args = parser.parse_args()

    detail, summary = _build_rows(_load_csv(Path(args.source)))
    summary_fields = [
        "role_family",
        "members",
        "total_follow_events",
        "event_concentration",
        "shared_label_count",
        "majority_label_count",
        "mean_label_jaccard",
        "min_label_jaccard",
        "max_mcm_distance",
        "mean_mcm_distance",
        "avg_carry",
        "avg_strain",
        "avg_rekopplung",
        "family_reading",
        "shared_labels",
        "majority_labels",
        "member_symbols",
        "boundary",
    ]
    detail_fields = [
        "role_family",
        "symbol_family",
        "family_reading",
        "follow_events",
        "event_share",
        "shared_label_hits",
        "majority_label_hits",
        "carry",
        "strain",
        "rekopplung",
        "follow_labels",
        "boundary",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", detail, detail_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", detail, summary)
    print(f"multi_role_families={len(summary)}")
    print(f"members={len(detail)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
