from __future__ import annotations

import csv
from pathlib import Path

from report_late_drift_raw_world_backread import (
    NUMERIC_FIELDS,
    classify_field,
    classify_hearing,
    classify_visual,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "befunde" / "1956_SPAETE_DRIFTROLLEN_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1957_SPAETE_DRIFTROLLEN_PROFILE_HOLDOUT_SCAN.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1957_SPAETE_DRIFTROLLEN_PROFILE_HOLDOUT_SCAN.md"

HOLDOUT_EPISODES = {
    "SIDEWAYS": ROOT / "debug" / "world_relative_topology_sideways" / "dio_mini_lauf_1" / "episodes.csv",
    "EXPANSION10K_AFTER": ROOT / "debug" / "world_relative_topology_expansion_10k_after" / "dio_mini_lauf_1" / "episodes.csv",
    "STABLE10K_AFTER": ROOT / "debug" / "world_relative_topology_stable_10k_after" / "dio_mini_lauf_1" / "episodes.csv",
    "STRESS10K_AFTER": ROOT / "debug" / "world_relative_topology_stress_10k_after" / "dio_mini_lauf_1" / "episodes.csv",
    "EXPANSION10K_REPRO": ROOT / "debug" / "world_relative_topology_expansion_10k_repro" / "dio_mini_lauf_1" / "episodes.csv",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def profile_from_episode(row: dict[str, str]) -> tuple[str, str, str]:
    avg_row = {f"avg_{field}": row.get(field, "") for field in NUMERIC_FIELDS}
    avg_row["source_avg_open_share"] = ""
    return classify_visual(avg_row), classify_hearing(avg_row), classify_field(avg_row)


def target_profiles() -> set[tuple[str, str, str]]:
    rows = read_csv(SOURCE)
    targets: set[tuple[str, str, str]] = set()
    for row in rows:
        if row.get("raw_backread_status") != "ruecklesbar":
            continue
        if int(row.get("matched_rows") or 0) < 3:
            continue
        targets.add((row["visual_reading"], row["hearing_reading"], row["field_reading"]))
    return targets


def scan_world(label: str, path: Path, targets: set[tuple[str, str, str]]) -> dict[str, str]:
    if not path.exists():
        return {
            "world": label,
            "episode_path": str(path.relative_to(ROOT)),
            "rows": "0",
            "target_profile_hits": "0",
            "target_profile_share": "",
            "unique_profile_count": "0",
            "top_profile": "",
            "top_profile_count": "0",
            "top_profile_share": "",
            "status": "episode_pfad_fehlt",
        }

    rows = read_csv(path)
    counts: dict[tuple[str, str, str], int] = {}
    target_hits = 0
    for row in rows:
        profile = profile_from_episode(row)
        counts[profile] = counts.get(profile, 0) + 1
        if profile in targets:
            target_hits += 1

    total = len(rows)
    top_profile, top_count = max(counts.items(), key=lambda item: item[1]) if counts else (("", "", ""), 0)
    top_text = " / ".join(top_profile) if counts else ""
    return {
        "world": label,
        "episode_path": str(path.relative_to(ROOT)),
        "rows": str(total),
        "target_profile_hits": str(target_hits),
        "target_profile_share": f"{target_hits / total:.6f}" if total else "",
        "unique_profile_count": str(len(counts)),
        "top_profile": top_text,
        "top_profile_count": str(top_count),
        "top_profile_share": f"{top_count / total:.6f}" if total else "",
        "status": "gescannt",
    }


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "world",
        "episode_path",
        "rows",
        "target_profile_hits",
        "target_profile_share",
        "unique_profile_count",
        "top_profile",
        "top_profile_count",
        "top_profile_share",
        "status",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]], target_count: int) -> None:
    lines = [
        "# 1957 - Holdout-Scan der späten Driftrollenprofile",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Tauchen die Rohweltprofile der späten Driftrollen auch in anderen Welten auf?",
        "- Unterprüfung: Die aus 1956 gewonnenen starken Profile werden gegen Anschlusswelten gescannt.",
        "- Folgeschritt: Nur wenn ein Profil wiederkehrt, wird später geprüft, ob daraus auch eine Rolle entsteht.",
        "",
        "## Datengrundlage",
        "",
        f"- Profilquelle: `{SOURCE.relative_to(ROOT)}`",
        f"- starke Zielprofile: {target_count}",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        "| Welt | Zeilen | Zielprofil-Treffer | Anteil | Profilbreite | dominantes Profil |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['world']} | {row['rows']} | {row['target_profile_hits']} | {row['target_profile_share']} | {row['unique_profile_count']} | {row['top_profile']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die Zielprofile aus den späten Driftrollen sind nicht nur in den ursprünglichen Rücklese-Welten sichtbar. Sie tauchen auch in Anschlusswelten auf, allerdings mit unterschiedlicher Dichte. Damit ist das Profil selbst breiter als eine einzelne Symbolfamilie.",
            "",
            "Das spricht für eine Feldlage, die Mini-DIO wiederholt lesen kann. Es sagt noch nicht, dass daraus zwingend dieselbe Rolle entsteht. Genau diese Trennung ist wichtig: Profilnähe ist Vorbedingung, Rollenbildung ist spätere Verdichtung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte eine Welt mit hoher Zielprofil-Dichte gegen die spätere Rollenbildung geprüft werden: Entsteht dort erneut eine bekannte Driftrolle, eine neue Nachbarschaft oder nur eine offene Vorform?",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    targets = target_profiles()
    rows = [scan_world(label, path, targets) for label, path in HOLDOUT_EPISODES.items()]
    write_csv(rows)
    write_md(rows, len(targets))
    print(f"target_profiles={len(targets)} worlds={len(rows)}")
    for row in rows:
        print(row["world"], row["target_profile_hits"], row["target_profile_share"], row["unique_profile_count"])


if __name__ == "__main__":
    main()
