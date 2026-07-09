from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root

from report_late_drift_profile_holdout_scan import HOLDOUT_EPISODES, profile_from_episode


ROOT = Path(__file__).resolve().parents[1]
SOURCE = befunde_root(ROOT) / "1956_SPAETE_DRIFTROLLEN_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1958_SPAETE_DRIFTROLLEN_PROFILE_ROLLENBINDUNG.csv"
OUT_MD = befunde_root(ROOT) / "1958_SPAETE_DRIFTROLLEN_PROFILE_ROLLENBINDUNG.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def source_profiles() -> tuple[set[tuple[str, str, str]], set[str], dict[str, str]]:
    rows = read_csv(SOURCE)
    profiles: set[tuple[str, str, str]] = set()
    source_families: set[str] = set()
    family_roles: dict[str, str] = {}
    for row in rows:
        if row.get("raw_backread_status") != "ruecklesbar":
            continue
        if int(row.get("matched_rows") or 0) < 3:
            continue
        profile = (row["visual_reading"], row["hearing_reading"], row["field_reading"])
        profiles.add(profile)
        source_families.add(row["family"])
        family_roles[row["family"]] = row["late_role_reading"]
    return profiles, source_families, family_roles


def classify_binding(known_hits: int, total_hits: int, top_family: str, top_count: int, distinct_families: int) -> str:
    if not total_hits:
        return "keine_vorform"
    known_share = known_hits / total_hits
    top_share = top_count / total_hits if total_hits else 0.0
    if known_hits and known_share >= 0.10:
        return "bekannte_driftrolle_beruehrt"
    if top_share >= 0.20 and distinct_families <= 8:
        return "neue_nachbarschaftsverdichtung"
    if distinct_families >= 20:
        return "offene_vorform_breit"
    return "offene_vorform_lokal"


def scan_world(label: str, path: Path, target_profiles: set[tuple[str, str, str]], source_families: set[str]) -> dict[str, str]:
    rows = read_csv(path)
    hits = [row for row in rows if profile_from_episode(row) in target_profiles]
    family_counts = Counter(row.get("symbol_family", "") for row in hits if row.get("symbol_family", ""))
    effect_counts = Counter(row.get("passive_mcm_effect_class", "") for row in hits if row.get("passive_mcm_effect_class", ""))
    preview_counts = Counter(row.get("mcm_field_episode_preview_symbol", "") for row in hits if row.get("mcm_field_episode_preview_symbol", ""))
    known_hits = sum(count for family, count in family_counts.items() if family in source_families)
    top_family, top_count = family_counts.most_common(1)[0] if family_counts else ("", 0)
    top_effect, top_effect_count = effect_counts.most_common(1)[0] if effect_counts else ("", 0)
    top_preview, top_preview_count = preview_counts.most_common(1)[0] if preview_counts else ("", 0)
    binding = classify_binding(known_hits, len(hits), top_family, top_count, len(family_counts))
    return {
        "world": label,
        "episode_path": str(path.relative_to(ROOT)),
        "episode_rows": str(len(rows)),
        "target_profile_hits": str(len(hits)),
        "target_profile_share": f"{len(hits) / len(rows):.6f}" if rows else "",
        "distinct_families": str(len(family_counts)),
        "known_source_family_hits": str(known_hits),
        "known_source_family_share": f"{known_hits / len(hits):.6f}" if hits else "",
        "top_family": top_family,
        "top_family_count": str(top_count),
        "top_family_share": f"{top_count / len(hits):.6f}" if hits else "",
        "top_effect": top_effect,
        "top_effect_count": str(top_effect_count),
        "top_preview_symbol": top_preview,
        "top_preview_count": str(top_preview_count),
        "binding_reading": binding,
        "top_10_families": ";".join(f"{family}:{count}" for family, count in family_counts.most_common(10)),
        "top_10_effects": ";".join(f"{effect}:{count}" for effect, count in effect_counts.most_common(10)),
    }


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "world",
        "episode_path",
        "episode_rows",
        "target_profile_hits",
        "target_profile_share",
        "distinct_families",
        "known_source_family_hits",
        "known_source_family_share",
        "top_family",
        "top_family_count",
        "top_family_share",
        "top_effect",
        "top_effect_count",
        "top_preview_symbol",
        "top_preview_count",
        "binding_reading",
        "top_10_families",
        "top_10_effects",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]], profile_count: int, source_family_count: int) -> None:
    binding_counts = Counter(row["binding_reading"] for row in rows)
    lines = [
        "# 1958 - Rollenbindung der späten Driftprofile",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Wird aus Profilnähe in Anschlusswelten eine Rollenbindung?",
        "- Unterprüfung: Zielprofil-Zeilen werden nach bekannter Familie, neuer Nachbarschaft oder offener Vorform gelesen.",
        "- Folgeschritt: Nur gebundene oder verdichtete Welten eignen sich für die nächste Tiefenprüfung.",
        "",
        "## Datengrundlage",
        "",
        f"- Profilquelle: `{SOURCE.relative_to(ROOT)}`",
        f"- Zielprofile: {profile_count}",
        f"- bekannte Quellfamilien: {source_family_count}",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        f"- Bindungsarten: {', '.join(f'{key}:{value}' for key, value in binding_counts.most_common())}",
        "",
        "| Welt | Treffer | Familienbreite | bekannte Treffer | Top-Familie | Top-Wirkung | Lesung |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['world']} | {row['target_profile_hits']} | {row['distinct_families']} | {row['known_source_family_hits']} | {row['top_family']} ({row['top_family_count']}) | {row['top_effect']} ({row['top_effect_count']}) | {row['binding_reading']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die Anschlusswelten zeigen keine simple Kopie der späten Driftfamilien. Die bekannten Quellfamilien bleiben schwach oder fehlen ganz. Das Zielprofil wirkt daher eher als offene Sinnes-/Feldvorform, aus der je nach Welt neue Nachbarschaften entstehen können.",
            "",
            "Wichtig ist die Trennung: Profilnähe ist eine wiederkehrende Wahrnehmungslage. Rollenbindung entsteht erst, wenn diese Lage im Feld wiederholt an Familien, Wirkung und Nachhall koppelt.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    profiles, source_families, _family_roles = source_profiles()
    rows = [scan_world(label, path, profiles, source_families) for label, path in HOLDOUT_EPISODES.items()]
    write_csv(rows)
    write_md(rows, len(profiles), len(source_families))
    print(f"profiles={len(profiles)} source_families={len(source_families)} worlds={len(rows)}")
    for row in rows:
        print(row["world"], row["binding_reading"], row["target_profile_hits"], row["distinct_families"], row["known_source_family_hits"])


if __name__ == "__main__":
    main()
