from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from report_late_drift_profile_holdout_scan import HOLDOUT_EPISODES, profile_from_episode
from report_late_drift_profile_role_binding import source_profiles


ROOT = Path(__file__).resolve().parents[1]
WINDOWS = ROOT / "docs" / "befunde" / "1959_OFFENE_VORFORM_LOKALER_KONTEXT.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1960_OFFENE_VORFORM_PREVIEW_SYMBOL_REKURRENZ.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1960_OFFENE_VORFORM_PREVIEW_SYMBOL_REKURRENZ.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def to_int(value: str) -> int:
    try:
        return int(float(value))
    except ValueError:
        return 0


def avg(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def classify_symbol(world_count: int, total_count: int, target_profile_share: float, effect_count: int) -> str:
    if world_count >= 3 and total_count >= 6:
        return "mehrweltlicher_preview_anker"
    if world_count >= 2 and total_count >= 4:
        return "wiederkehrender_preview_anker"
    if target_profile_share >= 0.60 and effect_count >= 2:
        return "lokaler_vorform_anker"
    return "einzelspur"


def collect() -> list[dict[str, str]]:
    target_profiles, _families, _roles = source_profiles()
    windows = read_csv(WINDOWS)
    symbol_rows: dict[str, list[dict[str, str]]] = defaultdict(list)

    for window in windows:
        world = window["world"]
        path = HOLDOUT_EPISODES[world]
        episodes = read_csv(path)
        start = max(0, to_int(window["start_tick"]) - 1)
        end = min(len(episodes), to_int(window["end_tick"]))
        for row in episodes[start:end]:
            symbol = row.get("mcm_field_episode_preview_symbol", "").strip()
            if not symbol:
                continue
            profile_hit = profile_from_episode(row) in target_profiles
            symbol_rows[symbol].append(
                {
                    "world": world,
                    "profile_hit": "1" if profile_hit else "0",
                    "effect": row.get("passive_mcm_effect_class", ""),
                    "family": row.get("symbol_family", ""),
                    "rekopplung": row.get("mcm_rekopplung_quality", ""),
                    "strain": row.get("mcm_strain_quality", ""),
                    "form_stability": row.get("sehen_form_stability", ""),
                    "energy_shift": row.get("hoeren_energy_shift", ""),
                }
            )

    out: list[dict[str, str]] = []
    for symbol, rows in symbol_rows.items():
        world_counts = Counter(row["world"] for row in rows)
        effects = Counter(row["effect"] for row in rows if row["effect"])
        families = Counter(row["family"] for row in rows if row["family"])
        profile_hits = sum(1 for row in rows if row["profile_hit"] == "1")
        rekopplung = [float(row["rekopplung"]) for row in rows if row["rekopplung"]]
        strain = [float(row["strain"]) for row in rows if row["strain"]]
        stability = [float(row["form_stability"]) for row in rows if row["form_stability"]]
        shift = [float(row["energy_shift"]) for row in rows if row["energy_shift"]]
        share = profile_hits / len(rows) if rows else 0.0
        reading = classify_symbol(len(world_counts), len(rows), share, len(effects))
        out.append(
            {
                "preview_symbol": symbol,
                "reading": reading,
                "total_count": str(len(rows)),
                "world_count": str(len(world_counts)),
                "target_profile_hits": str(profile_hits),
                "target_profile_share": f"{share:.6f}",
                "worlds": ";".join(f"{world}:{count}" for world, count in world_counts.most_common()),
                "effects": ";".join(f"{effect}:{count}" for effect, count in effects.most_common(6)),
                "families": ";".join(f"{family}:{count}" for family, count in families.most_common(6)),
                "avg_rekopplung": f"{avg(rekopplung):.6f}",
                "avg_strain": f"{avg(strain):.6f}",
                "avg_form_stability": f"{avg(stability):.6f}",
                "avg_energy_shift": f"{avg(shift):.6f}",
            }
        )
    priority = {
        "mehrweltlicher_preview_anker": 4,
        "wiederkehrender_preview_anker": 3,
        "lokaler_vorform_anker": 2,
        "einzelspur": 1,
    }
    return sorted(
        out,
        key=lambda row: (priority.get(row["reading"], 0), int(row["total_count"]), float(row["target_profile_share"])),
        reverse=True,
    )


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = [
        "preview_symbol",
        "reading",
        "total_count",
        "world_count",
        "target_profile_hits",
        "target_profile_share",
        "worlds",
        "effects",
        "families",
        "avg_rekopplung",
        "avg_strain",
        "avg_form_stability",
        "avg_energy_shift",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    readings = Counter(row["reading"] for row in rows)
    strongest = rows[:12]
    lines = [
        "# 1960 - Preview-Symbol-Rekurrenz offener Vorformen",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Tragen die dichten Vorform-Fenster semantische Anker oder nur Feldlage?",
        "- Unterprüfung: Preview-Symbole aus den Dichtefenstern werden über Welten, Wirkung und Profiltreffer gelesen.",
        "- Folgeschritt: Mehrweltliche Preview-Anker werden später als Kandidaten für neue Rollenkeime verfolgt.",
        "",
        "## Datengrundlage",
        "",
        f"- Dichtefenster: `{WINDOWS.relative_to(ROOT)}`",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        f"- Preview-Symbole: {len(rows)}",
        f"- Lesungen: {', '.join(f'{key}:{value}' for key, value in readings.most_common())}",
        "",
        "| Preview | Lesung | Anzahl | Welten | Profiltreffer | Wirkungen | Familien |",
        "|---|---|---:|---:|---:|---|---|",
    ]
    for row in strongest:
        lines.append(
            f"| {row['preview_symbol']} | {row['reading']} | {row['total_count']} | {row['world_count']} | {row['target_profile_hits']} / {row['target_profile_share']} | {row['effects']} | {row['families']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die offenen Vorformen enthalten semantische Anker, aber nicht als einfache Kopie einer alten Familie. Entscheidend ist die Mehrweltlichkeit: Ein Preview-Symbol wird dann interessant, wenn es in mehreren Welten im gleichen Vorform-Milieu wiederkehrt.",
            "",
            "Wenn ein Symbol nur lokal auftaucht, bleibt es Einzelspur. Wenn es über Welten stabil bleibt, kann daraus ein Rollenkeim entstehen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten die mehrweltlichen Preview-Anker lokal gegen Vorlauf, Nachlauf und Nachhall geprüft werden. Ziel ist zu klären, ob sie echte Rollenkeime sind oder nur wiederkehrende Oberflächenmarken.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = collect()
    write_csv(rows)
    write_md(rows)
    print(f"preview_symbols={len(rows)}")
    for row in rows[:10]:
        print(row["preview_symbol"], row["reading"], row["total_count"], row["world_count"], row["target_profile_share"])


if __name__ == "__main__":
    main()
