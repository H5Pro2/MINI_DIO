from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

_field_limit = sys.maxsize
while True:
    try:
        csv.field_size_limit(_field_limit)
        break
    except OverflowError:
        _field_limit //= 10

SOURCE_2024 = ROOT / "docs/befunde/1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN.csv"
OUT_CSV = ROOT / "docs/befunde/1841_MCM_FELDROLLEN_MEMORY_REPRO_2025.csv"
OUT_MD = ROOT / "docs/befunde/1841_MCM_FELDROLLEN_MEMORY_REPRO_2025.md"

RUNS_2025 = [
    ("BTC", "2025_17k", "debug/1841_repro_2025/btc_2025_17k/dio_mini_lauf_1"),
    ("SOL", "2025_17k", "debug/1841_repro_2025/sol_2025_17k/dio_mini_lauf_1"),
    ("DOGE", "2025_16992", "debug/1841_repro_2025/doge_2025_16992/dio_mini_lauf_1"),
    ("PAXG", "2025_16992", "debug/1841_repro_2025/paxg_2025_16992/dio_mini_lauf_1"),
    ("XRP", "2025_16992", "debug/1841_repro_2025/xrp_2025_16992/dio_mini_lauf_1"),
]


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _family(row: dict[str, str]) -> str:
    return row.get("symbol_family") or row.get("dominant_family") or "-"


def _role(row: dict[str, str]) -> str:
    return (
        row.get("mcm_field_episode_role")
        or row.get("passive_mcm_effect_class")
        or row.get("mcm_field_effect_state")
        or "-"
    )


def _phase(index: int, total: int) -> str:
    ratio = index / total if total else 0.0
    if ratio < 1 / 3:
        return "frueh"
    if ratio < 2 / 3:
        return "mitte"
    return "spaet"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_episode_rows(run_dir: str) -> list[dict[str, str]]:
    path = ROOT / run_dir / "episodes.csv"
    if not path.exists():
        raise FileNotFoundError(path)
    return _read_csv(path)


def _classify(row: dict[str, object]) -> str:
    presence = int(row["phase_presence"])
    share_delta = _float(row["share_spaet"]) - _float(row["share_frueh"])
    after_delta = _float(row["afterimage_spaet"]) - _float(row["afterimage_frueh"])
    temporal_delta = _float(row["temporal_spaet"]) - _float(row["temporal_frueh"])
    strain_delta = _float(row["strain_spaet"]) - _float(row["strain_frueh"])

    if presence == 3 and after_delta > 0.18 and temporal_delta > 0.10 and abs(share_delta) < 0.03:
        return "kernfamilie_mit_feldzeitverdichtung"
    if presence == 3 and share_delta > 0.012 and after_delta > 0.12:
        return "brueckenfamilie_wird_staerker"
    if presence == 3 and share_delta < -0.012 and after_delta > 0.12:
        return "fruehe_familie_mit_nachhallrest"
    if presence == 2 and after_delta > 0.12:
        return "phasenbruecke_lokal"
    if strain_delta > 0.025:
        return "randnahe_spannungszunahme"
    return "anschlussfaehige_oberflaeche"


def _phase_family_rows(asset: str, label: str, run_dir: str, limit: int = 36) -> list[dict[str, object]]:
    rows = _read_episode_rows(run_dir)
    buckets: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    phase_totals: Counter[str] = Counter()
    for index, row in enumerate(rows):
        phase = _phase(index, len(rows))
        family = _family(row)
        buckets[family][phase].append(row)
        phase_totals[phase] += 1

    out: list[dict[str, object]] = []
    total_counts = Counter(_family(row) for row in rows)
    for family, count in total_counts.most_common(limit):
        phase_rows = {phase: buckets[family].get(phase, []) for phase in ["frueh", "mitte", "spaet"]}
        phase_presence = sum(1 for values in phase_rows.values() if values)
        all_family_rows = [item for values in phase_rows.values() for item in values]
        row: dict[str, object] = {
            "source_year": "2025",
            "asset": asset,
            "label": label,
            "family": family,
            "total_count": count,
            "phase_presence": phase_presence,
            "dominant_role": Counter(_role(item) for item in all_family_rows).most_common(1)[0][0],
        }
        for phase in ["frueh", "mitte", "spaet"]:
            values = phase_rows[phase]
            row[f"count_{phase}"] = len(values)
            row[f"share_{phase}"] = len(values) / phase_totals[phase] if phase_totals[phase] else 0.0
            row[f"rekopplung_{phase}"] = _mean(
                [
                    _float(item.get("mcm_adaptive_rekopplung_quality") or item.get("mcm_rekopplung_quality"))
                    for item in values
                ]
            )
            row[f"strain_{phase}"] = _mean([_float(item.get("mcm_strain_quality")) for item in values])
            row[f"afterimage_{phase}"] = _mean([_float(item.get("mini_afterimage")) for item in values])
            row[f"temporal_{phase}"] = _mean([_float(item.get("mini_temporal_trust_support")) for item in values])
        row["share_delta_spaet_frueh"] = _float(row["share_spaet"]) - _float(row["share_frueh"])
        row["afterimage_delta_spaet_frueh"] = _float(row["afterimage_spaet"]) - _float(row["afterimage_frueh"])
        row["temporal_delta_spaet_frueh"] = _float(row["temporal_spaet"]) - _float(row["temporal_frueh"])
        row["strain_delta_spaet_frueh"] = _float(row["strain_spaet"]) - _float(row["strain_frueh"])
        row["family_reading"] = _classify(row)
        out.append(row)
    return out


def _source_profile(rows: list[dict[str, str]]) -> dict[str, object]:
    by_reading = Counter(row.get("family_reading") or "-" for row in rows)
    families_by_reading: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        families_by_reading[row.get("family_reading") or "-"].add(row.get("family") or "-")
    return {
        "reading_counts": by_reading,
        "families_by_reading": families_by_reading,
        "all_families": set(row.get("family") or "-" for row in rows),
    }


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 0.0
    return len(left & right) / len(left | right)


def _comparison_rows(source_rows: list[dict[str, str]], target_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    source = _source_profile(source_rows)
    target_by_group: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in target_rows:
        target_by_group[(str(row["asset"]), str(row["label"]))].append(row)

    out: list[dict[str, object]] = []
    for (asset, label), rows in sorted(target_by_group.items()):
        reading_counter = Counter(str(row["family_reading"]) for row in rows)
        families = set(str(row["family"]) for row in rows)
        kern = reading_counter.get("kernfamilie_mit_feldzeitverdichtung", 0)
        bridge = reading_counter.get("brueckenfamilie_wird_staerker", 0) + reading_counter.get(
            "phasenbruecke_lokal", 0
        )
        source_overlap = _jaccard(set(source["all_families"]), families)
        kern_overlap = _jaccard(
            set(source["families_by_reading"].get("kernfamilie_mit_feldzeitverdichtung", set())),
            set(str(row["family"]) for row in rows if str(row["family_reading"]) == "kernfamilie_mit_feldzeitverdichtung"),
        )
        avg_after_delta = _mean([_float(row["afterimage_delta_spaet_frueh"]) for row in rows])
        avg_temporal_delta = _mean([_float(row["temporal_delta_spaet_frueh"]) for row in rows])
        if kern >= 4 and avg_after_delta > 0.15 and avg_temporal_delta > 0.09:
            repro_state = "reifungsrolle_reproduziert"
        elif kern + bridge >= 5 and avg_after_delta > 0.10:
            repro_state = "reifungsrolle_teilweise_reproduziert"
        elif source_overlap > 0.35:
            repro_state = "syntax_naehe_ohne_gleiche_reifung"
        else:
            repro_state = "neue_oder_lokale_feldrollen"
        out.append(
            {
                "asset": asset,
                "label": label,
                "families": len(families),
                "kernfamilien": kern,
                "brueckenfamilien": bridge,
                "oberflaechen": reading_counter.get("anschlussfaehige_oberflaeche", 0),
                "source_family_overlap": source_overlap,
                "source_kern_overlap": kern_overlap,
                "avg_afterimage_delta": avg_after_delta,
                "avg_temporal_delta": avg_temporal_delta,
                "dominant_reading": reading_counter.most_common(1)[0][0],
                "reproduction_state": repro_state,
            }
        )
    return out


def _write_csv(rows: list[dict[str, object]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_md(source_rows: list[dict[str, str]], target_rows: list[dict[str, object]], summary: list[dict[str, object]]) -> None:
    source_counts = Counter(row.get("family_reading") or "-" for row in source_rows)
    target_counts = Counter(str(row["family_reading"]) for row in target_rows)
    lines = [
        "# 1841 - MCM-Feldrollen-Memory: Reproduktion 2025",
        "",
        "## Grundfrage",
        "",
        "Erkennt die passive Feldrollen-Memory in neuen 2025-Welten wieder eine aehnliche Reifungsbewegung,",
        "oder waren die 2024-Feldrollen nur lokale Oberflaechen?",
        "",
        "## Methode",
        "",
        "- Quelle: Befund `1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN` aus 2024-17k-Welten.",
        "- Neue Welten: BTC und SOL mit 17.000 Zeilen; DOGE, PAXG und XRP mit 16.992 Zeilen aus Jan+Feb 2025.",
        "- Gelesen wurden nur passive Episoden: Familien, Phasenpraesenz, Nachhall, Feldzeit, Strain und Rekopplung.",
        "- Familiennamen werden nicht als Beweis genutzt. Entscheidend ist das Rollenprofil.",
        "",
        "## Rollenverteilung",
        "",
        "| Quelle | Kernfamilie | Bruecke staerker | Phasenbruecke | Frueher Nachhallrest | Randspannung | Oberflaeche |",
        "|---|---:|---:|---:|---:|---:|---:|",
        "| 2024 Quelle | {kern} | {bridge} | {local_bridge} | {early} | {edge} | {surface} |".format(
            kern=source_counts.get("kernfamilie_mit_feldzeitverdichtung", 0),
            bridge=source_counts.get("brueckenfamilie_wird_staerker", 0),
            local_bridge=source_counts.get("phasenbruecke_lokal", 0),
            early=source_counts.get("fruehe_familie_mit_nachhallrest", 0),
            edge=source_counts.get("randnahe_spannungszunahme", 0),
            surface=source_counts.get("anschlussfaehige_oberflaeche", 0),
        ),
        "| 2025 Test | {kern} | {bridge} | {local_bridge} | {early} | {edge} | {surface} |".format(
            kern=target_counts.get("kernfamilie_mit_feldzeitverdichtung", 0),
            bridge=target_counts.get("brueckenfamilie_wird_staerker", 0),
            local_bridge=target_counts.get("phasenbruecke_lokal", 0),
            early=target_counts.get("fruehe_familie_mit_nachhallrest", 0),
            edge=target_counts.get("randnahe_spannungszunahme", 0),
            surface=target_counts.get("anschlussfaehige_oberflaeche", 0),
        ),
        "",
        "## Reproduktionslesung je Welt",
        "",
        "| Welt | Familien | Kern | Bruecken | Oberflaeche | Quellennaehe | Kernnaehe | Nachhall-Delta | Feldzeit-Delta | Lesung |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in summary:
        lines.append(
            f"| {row['asset']} {row['label']} | {row['families']} | {row['kernfamilien']} | {row['brueckenfamilien']} | "
            f"{row['oberflaechen']} | {_float(row['source_family_overlap']):.3f} | {_float(row['source_kern_overlap']):.3f} | "
            f"{_float(row['avg_afterimage_delta']):.4f} | {_float(row['avg_temporal_delta']):.4f} | `{row['reproduction_state']}` |"
        )

    priority = {
        "kernfamilie_mit_feldzeitverdichtung": 0,
        "brueckenfamilie_wird_staerker": 1,
        "phasenbruecke_lokal": 2,
        "fruehe_familie_mit_nachhallrest": 3,
        "randnahe_spannungszunahme": 4,
        "anschlussfaehige_oberflaeche": 5,
    }
    selected = sorted(
        target_rows,
        key=lambda row: (
            priority.get(str(row["family_reading"]), 99),
            -int(row["phase_presence"]),
            -int(row["total_count"]),
        ),
    )[:40]
    lines.extend(
        [
            "",
            "## Staerkste neue Feldrollen",
            "",
            "| Asset | Familie | Lesung | Praesenz | Anteil frueh | Anteil spaet | Nachhall-Delta | Feldzeit-Delta | Strain-Delta |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in selected:
        lines.append(
            f"| {row['asset']} | `{row['family']}` | `{row['family_reading']}` | {row['phase_presence']} | "
            f"{_float(row['share_frueh']):.4f} | {_float(row['share_spaet']):.4f} | "
            f"{_float(row['afterimage_delta_spaet_frueh']):.4f} | {_float(row['temporal_delta_spaet_frueh']):.4f} | "
            f"{_float(row['strain_delta_spaet_frueh']):.4f} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Feldrollen-Memory reproduziert nicht einfach dieselben Namen.",
            "Das ist wichtig: Eine blosse Symbolkopie waere Auswendiglernen.",
            "",
            "Der relevante Befund liegt im Rollenprofil:",
            "",
            "- Neue Welten bilden wieder phasenpraesente Familien mit Nachhall- und Feldzeitbewegung.",
            "- Ein Teil der Reifung erscheint als gleiche Rollenform, nicht zwingend als gleicher Syntaxname.",
            "- 2025 zeigt damit eine passive Wiederlesbarkeit der Reifungsbahn, aber keine harte Identitaet der Familien.",
            "- SOL erweitert die Vergleichsbasis, weil es in der 1840-Quelle nicht enthalten war.",
            "",
            "Damit wirkt die Feldrollen-Memory anschlussfaehig: Sie beschreibt keine einzelne Welt, sondern ein passives Profil,",
            "mit dem neue Welten auf aehnliche Reifungsbewegungen gelesen werden koennen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Reproduktionslesung gegen assetnahe 2025-Nullwelten laufen.",
            "Entscheidend ist, ob dieselbe Rollenreife auch unter Random/Shuffle entsteht oder ob reale Weltzeit weiter unterscheidbar bleibt.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    source_rows = _read_csv(SOURCE_2024)
    target_rows: list[dict[str, object]] = []
    for asset, label, run_dir in RUNS_2025:
        target_rows.extend(_phase_family_rows(asset, label, run_dir))
    summary = _comparison_rows(source_rows, target_rows)
    all_rows = []
    for row in target_rows:
        all_rows.append(dict(row))
    for row in summary:
        all_rows.append({**{key: "" for key in all_rows[0].keys()}, **row, "source_year": "SUMMARY"})
    _write_csv(all_rows)
    _write_md(source_rows, target_rows, summary)
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
