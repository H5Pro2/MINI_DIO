from __future__ import annotations

import argparse
import csv
from collections import defaultdict
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


def _short_token(value: object) -> str:
    return str(value or "-").replace("dio_mcm_episode_", "")


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _axis_key(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def _reading(rows: list[dict[str, str]], reciprocal_count: int) -> str:
    avg_rek = sum(_safe_float(row.get("avg_rekopplung")) for row in rows) / max(1, len(rows))
    avg_strain = sum(_safe_float(row.get("avg_strain")) for row in rows) / max(1, len(rows))
    worlds = {str(row.get("world_group", "") or "-") for row in rows}
    if reciprocal_count >= 2 and len(worlds) >= 2 and avg_rek > avg_strain:
        return "reziproke_verlegte_zentrumsachse"
    if reciprocal_count >= 1 and avg_rek > avg_strain:
        return "duenne_zentrumsachse"
    return "offene_paarnaehe"


def build_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    reciprocal: dict[tuple[str, str], int] = defaultdict(int)

    token_set = {_short_token(row.get("token")) for row in rows}
    for row in rows:
        token = _short_token(row.get("token"))
        neighbors = {_short_token(row.get("top_previous")), _short_token(row.get("top_next"))}
        for neighbor in neighbors:
            if neighbor in token_set and neighbor != token:
                key = _axis_key(token, neighbor)
                groups[key].append(row)
                reciprocal[key] += 1

    output: list[dict[str, object]] = []
    for (a, b), items in sorted(groups.items(), key=lambda item: len(item[1]), reverse=True):
        worlds = sorted({str(row.get("world_group", "") or "-") for row in items})
        observations = sum(_safe_int(row.get("observations")) for row in items)
        evidence_hits = sum(_safe_int(row.get("evidence_hits")) for row in items)
        avg_rek = sum(_safe_float(row.get("avg_rekopplung")) for row in items) / max(1, len(items))
        avg_strain = sum(_safe_float(row.get("avg_strain")) for row in items) / max(1, len(items))
        avg_sensory = sum(_safe_float(row.get("avg_sensory")) for row in items) / max(1, len(items))
        output.append(
            {
                **PASSIVE_FLAGS,
                "axis_a": a,
                "axis_b": b,
                "worlds": " | ".join(worlds),
                "axis_rows": len(items),
                "reciprocal_links": reciprocal[(a, b)],
                "observations_total": observations,
                "evidence_hits_total": evidence_hits,
                "avg_rekopplung": round(avg_rek, 6),
                "avg_strain": round(avg_strain, 6),
                "avg_sensory": round(avg_sensory, 6),
                "axis_reading": _reading(items, reciprocal[(a, b)]),
            }
        )
    return output


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Zentrumsverlagerung: Achsenpaare",
        "",
        "## Zweck",
        "",
        "Diese Datei prueft, ob neue Zentrumskandidaten nur Einzelknoten sind oder reziproke Achsen bilden.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Diagnose",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Achsen",
        "",
        "| Achse | Welten | Zeilen | Reziproke Links | Beob. | Belege | Rekopplung | Strain | Sensorik | Lesung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['axis_a']} <-> {row['axis_b']}` | `{row['worlds']}` | {row['axis_rows']} | {row['reciprocal_links']} | "
            f"{row['observations_total']} | {row['evidence_hits_total']} | {row['avg_rekopplung']} | {row['avg_strain']} | "
            f"{row['avg_sensory']} | `{row['axis_reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Eine verlegte Mitte wird staerker, wenn sie nicht nur als einzelner Knoten erscheint,",
            "sondern als gegenseitige Achse mit wiederkehrender Rueckbindung.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Mitte kann im MCM-Feld als Achse entstehen:",
            "zwei Knoten tragen sich gegenseitig und bleiben ueber Weltwechsel als Zentrumsnaehe lesbar.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die staerkste Achse gegen Rohweltsegmente gelesen werden.",
            "Dann wird sichtbar, welche Weltform diese reziproke Mitte ausloest oder traegt.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_rows(_load_csv(args.candidates))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"axes={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
