from __future__ import annotations

import argparse
import csv
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


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _target_members(target_rows: list[dict[str, str]], overlap_rows: list[dict[str, str]]) -> dict[str, set[str]]:
    allowed_roles = {
        row["role_family"]
        for row in overlap_rows
        if row.get("source_overlap_status") in {"anschluss_genuegend", "anschluss_teilweise"}
    }
    members: dict[str, set[str]] = defaultdict(set)
    for row in target_rows:
        role_family = str(row.get("role_family", "-"))
        if role_family in allowed_roles:
            members[role_family].add(str(row.get("symbol_family", "-")))
    return members


def _source_details(source_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        row
        for row in source_rows
        if row.get("row_type") == "detail" and row.get("kind") == "real" and row.get("family")
    ]


def _build_rows(
    target_rows: list[dict[str, str]],
    overlap_rows: list[dict[str, str]],
    source_rows: list[dict[str, str]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    members_by_role = _target_members(target_rows, overlap_rows)
    source_detail = _source_details(source_rows)

    detail: list[dict[str, object]] = []
    for row in source_detail:
        family = str(row.get("family", "-"))
        for role_family, members in members_by_role.items():
            if family not in members:
                continue
            detail.append(
                {
                    "role_family": role_family,
                    "symbol_family": family,
                    "asset": row.get("asset", "-"),
                    "label": row.get("label", "-"),
                    "window_start": row.get("window_start", "0"),
                    "total_count": _safe_int(row.get("total_count")),
                    "phase_presence": _safe_int(row.get("phase_presence")),
                    "dominant_role": row.get("dominant_role", "-"),
                    "family_reading": row.get("family_reading", "-"),
                    "rekopplung_frueh": _fmt(_safe_float(row.get("rekopplung_frueh"))),
                    "rekopplung_mitte": _fmt(_safe_float(row.get("rekopplung_mitte"))),
                    "rekopplung_spaet": _fmt(_safe_float(row.get("rekopplung_spaet"))),
                    "strain_frueh": _fmt(_safe_float(row.get("strain_frueh"))),
                    "strain_mitte": _fmt(_safe_float(row.get("strain_mitte"))),
                    "strain_spaet": _fmt(_safe_float(row.get("strain_spaet"))),
                    "afterimage_delta_spaet_frueh": _fmt(_safe_float(row.get("afterimage_delta_spaet_frueh"))),
                    "temporal_delta_spaet_frueh": _fmt(_safe_float(row.get("temporal_delta_spaet_frueh"))),
                    "boundary": "passive_connected_family_followworld_trace_no_action_no_direction",
                }
            )

    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        grouped[str(row["role_family"])].append(row)

    summary: list[dict[str, object]] = []
    for role_family, rows in sorted(grouped.items()):
        target_members = members_by_role[role_family]
        found_members = {str(row["symbol_family"]) for row in rows}
        reading_counts = Counter(str(row["family_reading"]) for row in rows)
        asset_counts = Counter(str(row["asset"]) for row in rows)
        member_counts = Counter(str(row["symbol_family"]) for row in rows)
        total_events = sum(_safe_int(row["total_count"]) for row in rows)
        summary.append(
            {
                "role_family": role_family,
                "target_members": len(target_members),
                "found_members": len(found_members),
                "member_coverage": _fmt(len(found_members) / max(1, len(target_members))),
                "real_follow_rows": len(rows),
                "total_follow_count": total_events,
                "dominant_reading": reading_counts.most_common(1)[0][0] if reading_counts else "-",
                "reading_profile": ";".join(f"{key}:{value}" for key, value in reading_counts.most_common()),
                "asset_profile": ";".join(f"{key}:{value}" for key, value in asset_counts.most_common()),
                "member_profile": ";".join(f"{key}:{value}" for key, value in member_counts.most_common()),
                "mean_rekopplung_spaet": _fmt(_mean([_safe_float(row["rekopplung_spaet"]) for row in rows])),
                "mean_strain_spaet": _fmt(_mean([_safe_float(row["strain_spaet"]) for row in rows])),
                "mean_afterimage_delta": _fmt(_mean([_safe_float(row["afterimage_delta_spaet_frueh"]) for row in rows])),
                "mean_temporal_delta": _fmt(_mean([_safe_float(row["temporal_delta_spaet_frueh"]) for row in rows])),
                "source_follow_reading": (
                    "familie_als_ganzes_lesbar"
                    if len(found_members) == len(target_members)
                    else "familie_nur_fragmentarisch_lesbar"
                ),
                "boundary": "passive_connected_family_followworld_summary_no_action_no_direction",
            }
        )

    summary.sort(key=lambda row: (-_safe_int(row["found_members"]), -_safe_int(row["total_follow_count"]), str(row["role_family"])))
    detail.sort(key=lambda row: (str(row["role_family"]), str(row["asset"]), str(row["label"]), str(row["symbol_family"])))
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
    lines = [
        "# 2068 - Anschlussfähige Rollenfamilien in realen Folgewelten",
        "",
        "## Zweck",
        "",
        "Diese Auswertung liest nur die Rollenfamilien aus 2066, die laut 2067 in der älteren 1853-Neuweltbasis ausreichend oder teilweise anschlussfähig sind.",
        "",
        "Damit wird keine fehlende Familie bewertet. Geprüft werden nur Familien, deren Mitglieder in der Vergleichsbasis tatsächlich vorkommen.",
        "",
        "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte anschlussfähige Rollenfamilien: `{len(summary)}`",
        f"- gelesene reale Folgewelt-Zeilen: `{len(detail)}`",
        "",
        "## Familien",
        "",
    ]
    lines.extend(
        _md_table(
            summary,
            [
                "role_family",
                "target_members",
                "found_members",
                "member_coverage",
                "real_follow_rows",
                "total_follow_count",
                "dominant_reading",
                "source_follow_reading",
                "member_profile",
            ],
            limit=20,
        )
    )
    lines.extend(
        [
            "",
            "## Feldzeitwerte",
            "",
        ]
    )
    lines.extend(
        _md_table(
            summary,
            [
                "role_family",
                "mean_rekopplung_spaet",
                "mean_strain_spaet",
                "mean_afterimage_delta",
                "mean_temporal_delta",
                "asset_profile",
                "reading_profile",
            ],
            limit=20,
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die vollständig anschlussfähigen Familien können in der älteren Neuweltbasis als Familie gelesen werden. Das ist schwächer als ein neu erzeugter Folgeweltlauf auf gleicher Symbolbasis, aber stärker als ein reiner Einzelrollenfund.",
            "",
            "Teilweise anschlussfähige Familien bleiben fragmentarisch. Dort darf nicht behauptet werden, dass die ganze Familie stabil bleibt.",
            "",
            "## Grenze",
            "",
            "Dieser Report ersetzt keine neue Folgeweltprüfung auf derselben Symbolbasis. Er zeigt nur, welche 2066-Familien in vorhandenen realen Neuwelten überhaupt lesbar sind.",
            "",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default="docs/befunde/2001-3000/2066_REALVERSTAERKTE_ROLLENFAMILIEN_KOHAESION.detail.csv")
    parser.add_argument("--overlap", default="docs/befunde/2001-3000/2067_REALVERSTAERKTE_ROLLENFAMILIEN_ANSCHLUSSCHECK.summary.csv")
    parser.add_argument("--source", default="docs/befunde/1001-2000/1751-2000/1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv")
    parser.add_argument("--out-prefix", default="2068_ANSCHLUSSFAEHIGE_ROLLENFAMILIEN_IN_FOLGEWELTEN")
    args = parser.parse_args()

    detail, summary = _build_rows(
        _load_csv(Path(args.target)),
        _load_csv(Path(args.overlap)),
        _load_csv(Path(args.source)),
    )
    summary_fields = [
        "role_family",
        "target_members",
        "found_members",
        "member_coverage",
        "real_follow_rows",
        "total_follow_count",
        "dominant_reading",
        "reading_profile",
        "asset_profile",
        "member_profile",
        "mean_rekopplung_spaet",
        "mean_strain_spaet",
        "mean_afterimage_delta",
        "mean_temporal_delta",
        "source_follow_reading",
        "boundary",
    ]
    detail_fields = [
        "role_family",
        "symbol_family",
        "asset",
        "label",
        "window_start",
        "total_count",
        "phase_presence",
        "dominant_role",
        "family_reading",
        "rekopplung_frueh",
        "rekopplung_mitte",
        "rekopplung_spaet",
        "strain_frueh",
        "strain_mitte",
        "strain_spaet",
        "afterimage_delta_spaet_frueh",
        "temporal_delta_spaet_frueh",
        "boundary",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.summary.csv", summary, summary_fields)
    _write_csv(BEFUNDE / f"{args.out_prefix}.detail.csv", detail, detail_fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", detail, summary)
    print(f"families={len(summary)}")
    print(f"detail_rows={len(detail)}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
