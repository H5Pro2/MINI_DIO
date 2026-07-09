from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
SOURCE = befunde_root(ROOT) / "1961_MEHRWELTLICHE_PREVIEW_ANKER_KONTEXT.csv"
OUT_CSV = befunde_root(ROOT) / "1962_PREVIEW_ANKER_OBERFLAECHENURSACHE.csv"
OUT_MD = befunde_root(ROOT) / "1962_PREVIEW_ANKER_OBERFLAECHENURSACHE.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def as_float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def classify_cause(row: dict[str, str]) -> str:
    rekopplung = as_float(row, "anchor_avg_rekopplung")
    strain = as_float(row, "anchor_avg_strain")
    afterimage = as_float(row, "anchor_avg_afterimage")
    recurrence = as_float(row, "anchor_avg_recurrence")
    profile_share = as_float(row, "target_profile_share")
    occurrences = as_float(row, "occurrences")

    weak_afterimage = afterimage < 0.12
    weak_recurrence = recurrence < 0.18
    broad_symbol = occurrences >= 500 and profile_share < 0.25
    weak_profile = profile_share < 0.22
    healthy_field = rekopplung >= 0.63 and strain <= 0.22

    if healthy_field and broad_symbol and (weak_afterimage or weak_recurrence):
        return "zu_breit_und_zu_wenig_nachhall"
    if healthy_field and weak_profile:
        return "feld_traegt_aber_profil_zu_duenn"
    if weak_afterimage and weak_recurrence:
        return "nachhall_und_rekurrenz_zu_schwach"
    if weak_afterimage:
        return "nachhall_zu_schwach"
    if weak_recurrence:
        return "rekurrenz_zu_schwach"
    if rekopplung < 0.63:
        return "rekopplung_zu_schwach"
    if strain > 0.22:
        return "zu_viel_feldspannung"
    return "oberflaeche_noch_nicht_spezifisch_genug"


def strength_reading(row: dict[str, str]) -> str:
    profile_share = as_float(row, "target_profile_share")
    afterimage = as_float(row, "anchor_avg_afterimage")
    recurrence = as_float(row, "anchor_avg_recurrence")
    if profile_share >= 0.30 and afterimage >= 0.12 and recurrence >= 0.18:
        return "nahe_am_rollenkeim"
    if profile_share >= 0.20 or afterimage >= 0.12 or recurrence >= 0.18:
        return "vorform_mit_teilbindung"
    return "breite_oberflaeche"


def collect() -> list[dict[str, str]]:
    rows = read_csv(SOURCE)
    out: list[dict[str, str]] = []
    for row in rows:
        result = {
            "preview_symbol": row["preview_symbol"],
            "world": row["world"],
            "occurrences": row["occurrences"],
            "target_profile_share": row["target_profile_share"],
            "anchor_avg_rekopplung": row["anchor_avg_rekopplung"],
            "anchor_avg_strain": row["anchor_avg_strain"],
            "anchor_avg_afterimage": row["anchor_avg_afterimage"],
            "anchor_avg_recurrence": row["anchor_avg_recurrence"],
            "anchor_effects": row["anchor_effects"],
            "surface_cause": classify_cause(row),
            "strength_reading": strength_reading(row),
        }
        out.append(result)
    priority = {"nahe_am_rollenkeim": 3, "vorform_mit_teilbindung": 2, "breite_oberflaeche": 1}
    return sorted(
        out,
        key=lambda row: (
            priority[row["strength_reading"]],
            float(row["target_profile_share"]),
            float(row["anchor_avg_afterimage"]),
            float(row["anchor_avg_recurrence"]),
        ),
        reverse=True,
    )


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = list(rows[0].keys()) if rows else []
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    causes = Counter(row["surface_cause"] for row in rows)
    strengths = Counter(row["strength_reading"] for row in rows)
    lines = [
        "# 1962 - Ursachen der Preview-Oberflächenanker",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Warum bleiben mehrweltliche Preview-Anker oberflächlich?",
        "- Unterprüfung: Nachhall, Rekurrenz, Rekopplung, Strain, Profilanteil und Symbolbreite werden getrennt gelesen.",
        "- Folgeschritt: Nur Teilbindungen werden als mögliche organische Vertiefungskandidaten weiterverfolgt.",
        "",
        "## Datengrundlage",
        "",
        f"- Quelle: `{SOURCE.relative_to(ROOT)}`",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        f"- geprüfte Anker/Welt-Kombinationen: {len(rows)}",
        f"- Ursachen: {', '.join(f'{key}:{value}' for key, value in causes.most_common())}",
        f"- Stärke: {', '.join(f'{key}:{value}' for key, value in strengths.most_common())}",
        "",
        "| Preview | Welt | Stärke | Ursache | Profilanteil | Rekopplung | Strain | Nachhall | Rekurrenz |",
        "|---|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['preview_symbol']} | {row['world']} | {row['strength_reading']} | {row['surface_cause']} | {row['target_profile_share']} | {row['anchor_avg_rekopplung']} | {row['anchor_avg_strain']} | {row['anchor_avg_afterimage']} | {row['anchor_avg_recurrence']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die Oberflächlichkeit entsteht nicht durch ein kollabiertes Feld. Rekopplung ist meist tragfähig und Strain bleibt niedrig. Das Problem liegt eher darin, dass die Preview-Symbole zu breit über stabile Feldwirkung verteilt sind und der spezifische Profilanteil zu dünn bleibt.",
            "",
            "Damit ist die nächste organische Verbesserung nicht mehr Feldstärkung allgemein. Sie muss die Differenzierung vertiefen: ein Anker soll nicht häufiger werden, sondern spezifischer an Nachhall, Rekurrenz und Profilnähe koppeln.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes muss geprüft werden, ob Nachhall und Rekurrenz grundsätzlich zu flach skaliert sind oder ob nur diese Preview-Anker keine spezifische Tiefe tragen. Erst danach wäre eine organische Vertiefung sinnvoll.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = collect()
    write_csv(rows)
    write_md(rows)
    print(f"rows={len(rows)}")
    for row in rows[:12]:
        print(row["preview_symbol"], row["world"], row["strength_reading"], row["surface_cause"], row["target_profile_share"])


if __name__ == "__main__":
    main()
