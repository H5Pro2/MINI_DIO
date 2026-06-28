from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


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


def _load_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;")
    except Exception:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _token_short(row: dict[str, str]) -> str:
    token = str(row.get("short_token") or row.get("token") or "-")
    return token.replace("dio_mcm_episode_", "")


def _is_center_candidate(row: dict[str, str], min_observations: int) -> bool:
    text = " ".join(str(row.get(key, "") or "") for key in ("nonbridge_class", "dominant_role", "condensation_zone", "classification_note"))
    has_center_language = "zentrum" in text or "center" in text
    if not has_center_language:
        return False
    observations = _safe_int(row.get("observations"))
    nonbridge = str(row.get("nonbridge_class", "") or "")
    # Getragene Zentren duerfen auch bei kleinerer Stichprobe sichtbar bleiben.
    if "zentrum_getragen" in nonbridge:
        return observations >= max(1, min_observations // 2)
    return observations >= min_observations


def _candidate_quality(row: dict[str, str]) -> str:
    nonbridge = str(row.get("nonbridge_class", "") or "")
    avg_rekopplung = _safe_float(row.get("avg_rekopplung"))
    avg_strain = _safe_float(row.get("avg_strain"))
    neighbor_count = _safe_int(row.get("neighbor_count"))
    observations = _safe_int(row.get("observations"))

    if "zentrum_getragen" in nonbridge or (avg_rekopplung > 0.55 and avg_strain < 0.22 and observations >= 20):
        return "zentrum_getragen"
    if "zentrum_schwach" in nonbridge or (avg_rekopplung > 0.45 and neighbor_count <= 2):
        return "zentrum_schwach"
    if avg_strain > avg_rekopplung:
        return "zentrum_belastet"
    return "zentrum_offen"


def _world_label(path: Path) -> str:
    stem = path.stem
    for prefix in ("969_MCM_NICHTBRUECKEN_ORDNUNG_", "974_MCM_NICHTBRUECKEN_ORDNUNG_", "978_MCM_NICHTBRUECKEN_ORDNUNG_"):
        if stem.startswith(prefix):
            return stem[len(prefix) :]
    return stem


def _top(counter: Counter[str], limit: int = 6) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def build_rows(paths: list[Path], previous_nodes: set[str], min_observations: int) -> list[dict[str, object]]:
    rows_out: list[dict[str, object]] = []
    for path in paths:
        candidates = [row for row in _load_rows(path) if _is_center_candidate(row, min_observations)]
        qualities = Counter(_candidate_quality(row) for row in candidates)
        tokens = Counter(_token_short(row) for row in candidates)
        previous_hits = sum(1 for row in candidates if _token_short(row) in previous_nodes)
        rekopplung = [_safe_float(row.get("avg_rekopplung")) for row in candidates]
        strain = [_safe_float(row.get("avg_strain")) for row in candidates]
        sensory = [_safe_float(row.get("avg_sensory")) for row in candidates]
        rows_out.append(
            {
                **PASSIVE_FLAGS,
                "world_group": _world_label(path),
                "source_file": path.name,
                "min_observations": min_observations,
                "center_candidates": len(candidates),
                "previous_center_hits": previous_hits,
                "new_center_candidates": max(0, len(candidates) - previous_hits),
                "avg_rekopplung": round(sum(rekopplung) / max(1, len(rekopplung)), 6),
                "avg_strain": round(sum(strain) / max(1, len(strain)), 6),
                "avg_sensory": round(sum(sensory) / max(1, len(sensory)), 6),
                "quality_profile": _top(qualities),
                "top_center_tokens": _top(tokens),
                "center_reading": _reading(len(candidates), previous_hits, qualities),
            }
        )
    return rows_out


def _reading(candidate_count: int, previous_hits: int, qualities: Counter[str]) -> str:
    if candidate_count == 0:
        return "keine_zentrumsbildung_sichtbar"
    if previous_hits > 0:
        return "alte_mitte_reproduziert_mit_folgeanschluss"
    if qualities.get("zentrum_getragen", 0) > 0:
        return "mitte_verlagert_sich_getragen"
    if qualities.get("zentrum_schwach", 0) > 0:
        return "mitte_verlagert_sich_schwach"
    return "mitte_verlagert_sich_offen"


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Zentrumsverlagerung: Folgewelten",
        "",
        "## Zweck",
        "",
        "Diese Datei prueft passiv, ob die spaete Zentrumsqualitaet als gleiche Knotenkopie wiederkehrt oder ob die Mitte in Folgewelten wandert.",
        "Einmalige Oberflaechentreffer werden dabei ueber eine Mindestwiederkehr gedaempft.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Lesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Vergleich",
        "",
        "| Weltgruppe | Mindestwiederkehr | Zentrumskandidaten | Alte Zentrumstreffer | Neue Kandidaten | Rekopplung | Strain | Qualitaeten | Top Knoten | Lesung |",
        "|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['world_group']}` | {row['min_observations']} | {row['center_candidates']} | {row['previous_center_hits']} | {row['new_center_candidates']} | "
            f"{row['avg_rekopplung']} | {row['avg_strain']} | `{row['quality_profile']}` | `{row['top_center_tokens']}` | `{row['center_reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Wenn alte Zentrumsknoten nicht wieder erscheinen, ist das nicht automatisch Bedeutungsverlust.",
            "Die Folgewelten koennen neue Zentrumskandidaten bilden.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Mitte wird nicht zwingend als identischer Knoten kopiert.",
            "Mitte kann sich als Feldrolle verlagern.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die neuen Top-Zentrumsknoten einzeln gegen ihre Rohwelt- und Sinnesachsen zurueckgelesen werden.",
            "Dann wird sichtbar, ob die Verlagerung eine echte neue Feldmitte oder nur Oberflaechennaehe ist.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nonbridge", action="append", type=Path, required=True)
    parser.add_argument("--previous-center", action="append", default=[])
    parser.add_argument("--min-observations", type=int, default=5)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_rows(
        args.nonbridge,
        {str(item).replace("dio_mcm_episode_", "") for item in args.previous_center},
        max(1, int(args.min_observations)),
    )
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"world_groups={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
