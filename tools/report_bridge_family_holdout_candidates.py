from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path

from report_bridge_family_rawworld_windows import (
    PATTERNS,
    _band,
    _float,
    _iter_episode_files,
    _quantile,
    _role,
    _world_group,
)


KNOWN_FAMILIES = {"dio_17ct", "dio_0g2r", "dio_1ewh", "dio_155c", "dio_1gp2"}


def _mean(values: list[float]) -> float:
    return statistics.fmean(values) if values else 0.0


def _matches(row: dict[str, str], pattern: str, qs: dict[str, float]) -> bool:
    spec = PATTERNS[pattern]
    band = _band(_float(row, "hoeren_energy_tone"), qs["tone_q33"], qs["tone_q66"])
    role = _role(row, qs)
    return band == spec["tonal_band"] and role == spec["target_role"]


def _episode_qs(rows: list[dict[str, str]]) -> dict[str, float]:
    tone_values = [_float(row, "hoeren_energy_tone") for row in rows]
    return {
        "tone_q33": _quantile(tone_values, 0.33),
        "tone_q66": _quantile(tone_values, 0.66),
        "rekopplung_q33": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.33),
        "rekopplung_q50": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.50),
        "rekopplung_q66": _quantile([_float(row, "mcm_rekopplung_quality") for row in rows], 0.66),
        "strain_q33": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.33),
        "strain_q50": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.50),
        "strain_q66": _quantile([_float(row, "mcm_strain_quality") for row in rows], 0.66),
        "carry_q66": _quantile([_float(row, "mcm_carry_quality") for row in rows], 0.66),
        "tension_q66": _quantile([_float(row, "mcm_feldwirkung_mcm_tension") for row in rows], 0.66),
    }


def _family(row: dict[str, str]) -> str:
    family = (row.get("symbol_family") or "").strip()
    return family if family and family != "-" else "-"


def _collect(world_dirs: list[Path]) -> dict[str, dict[str, list[dict[str, str]]]]:
    collected: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for path in _iter_episode_files(world_dirs):
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            continue
        qs = _episode_qs(rows)
        group = _world_group(path)
        for row in rows:
            family = _family(row)
            if family == "-":
                continue
            for pattern in PATTERNS:
                if _matches(row, pattern, qs):
                    enriched = dict(row)
                    enriched["_world_group"] = group
                    enriched["_world"] = path.parent.parent.name
                    enriched["_pattern"] = pattern
                    collected[family][pattern].append(enriched)
    return collected


def _worlds(rows: list[dict[str, str]]) -> set[str]:
    return {row.get("_world", "-") for row in rows}


def _groups(rows: list[dict[str, str]]) -> set[str]:
    return {row.get("_world_group", "-") for row in rows}


def _candidate_class(row: dict[str, object]) -> str:
    if row["known_family"] == 1:
        return "bekannte_karte"
    if row["tragend_events"] >= 10 and row["kipp_events"] >= 10 and row["rekopplung_gap"] >= 0.025 and row["strain_gap"] >= 0.025:
        return "neuer_starker_brueckenkandidat"
    if row["tragend_events"] >= 5 and row["kipp_events"] >= 5 and row["rekopplung_gap"] >= 0.015 and row["strain_gap"] >= 0.015:
        return "neuer_lokaler_brueckenkandidat"
    return "schwacher_kontakt"


def _summarize(collected: dict[str, dict[str, list[dict[str, str]]]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for family, by_pattern in collected.items():
        tragend = by_pattern.get("tragende_verarbeitung", [])
        kipp = by_pattern.get("kippnaehe", [])
        if not tragend or not kipp:
            continue
        row: dict[str, object] = {
            "passive_only": 1,
            "read_by_mini_dio": 0,
            "influences_action": 0,
            "is_gate": 0,
            "is_motoric": 0,
            "is_entry_signal": 0,
            "is_direction_signal": 0,
            "family": family,
            "known_family": 1 if family in KNOWN_FAMILIES else 0,
            "tragend_events": len(tragend),
            "kipp_events": len(kipp),
            "tragend_worlds": len(_worlds(tragend)),
            "kipp_worlds": len(_worlds(kipp)),
            "world_groups": ";".join(sorted(_groups(tragend + kipp))),
            "tragend_rekopplung": _mean([_float(row, "mcm_rekopplung_quality") for row in tragend]),
            "kipp_rekopplung": _mean([_float(row, "mcm_rekopplung_quality") for row in kipp]),
            "tragend_strain": _mean([_float(row, "mcm_strain_quality") for row in tragend]),
            "kipp_strain": _mean([_float(row, "mcm_strain_quality") for row in kipp]),
            "tragend_tension": _mean([_float(row, "mcm_feldwirkung_mcm_tension") for row in tragend]),
            "kipp_tension": _mean([_float(row, "mcm_feldwirkung_mcm_tension") for row in kipp]),
        }
        row["rekopplung_gap"] = float(row["tragend_rekopplung"]) - float(row["kipp_rekopplung"])
        row["strain_gap"] = float(row["kipp_strain"]) - float(row["tragend_strain"])
        row["tension_gap"] = float(row["kipp_tension"]) - float(row["tragend_tension"])
        row["candidate_class"] = _candidate_class(row)
        out.append(row)
    return sorted(
        out,
        key=lambda item: (
            int(item["known_family"]),
            {"neuer_starker_brueckenkandidat": 3, "neuer_lokaler_brueckenkandidat": 2, "schwacher_kontakt": 1, "bekannte_karte": 0}.get(str(item["candidate_class"]), 0),
            int(item["tragend_events"]) + int(item["kipp_events"]),
            float(item["rekopplung_gap"]) + float(item["strain_gap"]),
        ),
        reverse=True,
    )


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    known = [row for row in rows if row["known_family"] == 1]
    new_strong = [row for row in rows if row["candidate_class"] == "neuer_starker_brueckenkandidat"]
    new_local = [row for row in rows if row["candidate_class"] == "neuer_lokaler_brueckenkandidat"]
    lines = [
        "# 1095 - Neue Brueckenfamilien im Holdout",
        "",
        "Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.",
        "",
        "## Frage",
        "",
        "Entstehen in den Holdout-Welten Brueckenfamilien, die nicht in der bisherigen Qualitaetskarte liegen?",
        "",
        "## Gesamtbefund",
        "",
        f"- Familien mit beiden Lesarten: `{len(rows)}`",
        f"- Bekannte Familien aus 1092: `{len(known)}`",
        f"- Neue starke Kandidaten: `{len(new_strong)}`",
        f"- Neue lokale Kandidaten: `{len(new_local)}`",
        "",
        "## Staerkste neuen Kandidaten",
        "",
        "| Familie | Klasse | Tragend | Kippnah | Welten T/K | Rekopplung Gap | Strain Gap | Tension Gap | Gruppen |",
        "|---|---|---:|---:|---|---:|---:|---:|---|",
    ]
    for row in [item for item in rows if item["known_family"] == 0][:20]:
        lines.append(
            f"| `{row['family']}` | {row['candidate_class']} | {row['tragend_events']} | {row['kipp_events']} | "
            f"{row['tragend_worlds']}/{row['kipp_worlds']} | {float(row['rekopplung_gap']):.4f} | "
            f"{float(row['strain_gap']):.4f} | {float(row['tension_gap']):.4f} | {row['world_groups']} |"
        )
    lines.extend(
        [
            "",
            "## Bekannte Kartenfamilien im Holdout",
            "",
            "| Familie | Tragend | Kippnah | Rekopplung Gap | Strain Gap | Tension Gap |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in known:
        lines.append(
            f"| `{row['family']}` | {row['tragend_events']} | {row['kipp_events']} | "
            f"{float(row['rekopplung_gap']):.4f} | {float(row['strain_gap']):.4f} | {float(row['tension_gap']):.4f} |"
        )
    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "Ein neuer Kandidat ist nur dann interessant, wenn er in beiden Lesarten vorkommt und diese Lesarten durch Rekopplung und Strain unterscheidbar bleiben.",
            "Damit wird keine neue Bedeutung gesetzt. Es wird nur markiert, wo das Bedeutungsnetz moeglicherweise neue Knoten ausbildet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die staerksten neuen Kandidaten einzeln mit Tickfenstern gelesen werden. Erst dann kann entschieden werden, ob sie echte neue Brueckenanker oder nur lokale Kontaktfragmente sind.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world-dir", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _summarize(_collect([Path(item) for item in args.world_dir]))
    _write_csv(rows, Path(args.out_csv))
    _write_md(rows, Path(args.out_md))
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
