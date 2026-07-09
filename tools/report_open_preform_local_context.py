from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from befunde_paths import befunde_root

from report_late_drift_profile_holdout_scan import HOLDOUT_EPISODES, profile_from_episode
from report_late_drift_profile_role_binding import source_profiles


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = befunde_root(ROOT) / "1959_OFFENE_VORFORM_LOKALER_KONTEXT.csv"
OUT_MD = befunde_root(ROOT) / "1959_OFFENE_VORFORM_LOKALER_KONTEXT.md"

TARGET_WORLDS = ["SIDEWAYS", "EXPANSION10K_AFTER", "STABLE10K_AFTER", "STRESS10K_AFTER"]
WINDOW = 100
STEP = 50
CONTEXT = 25
TOP_WINDOWS_PER_WORLD = 5


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def top(counter: Counter[str], n: int = 3) -> str:
    return ";".join(f"{key}:{value}" for key, value in counter.most_common(n) if key)


def avg_float(rows: list[dict[str, str]], key: str) -> float:
    values: list[float] = []
    for row in rows:
        try:
            values.append(float(row.get(key, "") or 0.0))
        except ValueError:
            pass
    return sum(values) / len(values) if values else 0.0


def summarize_slice(rows: list[dict[str, str]]) -> dict[str, str]:
    return {
        "rows": str(len(rows)),
        "families": top(Counter(row.get("symbol_family", "") for row in rows)),
        "effects": top(Counter(row.get("passive_mcm_effect_class", "") for row in rows)),
        "preview_symbols": top(Counter(row.get("mcm_field_episode_preview_symbol", "") for row in rows)),
        "avg_carry": f"{avg_float(rows, 'mcm_carry_quality'):.6f}",
        "avg_strain": f"{avg_float(rows, 'mcm_strain_quality'):.6f}",
        "avg_rekopplung": f"{avg_float(rows, 'mcm_rekopplung_quality'):.6f}",
        "avg_form_flow": f"{avg_float(rows, 'sehen_form_flow'):.6f}",
        "avg_form_stability": f"{avg_float(rows, 'sehen_form_stability'):.6f}",
        "avg_energy_tone": f"{avg_float(rows, 'hoeren_energy_tone'):.6f}",
        "avg_energy_shift": f"{avg_float(rows, 'hoeren_energy_shift'):.6f}",
        "avg_tension": f"{avg_float(rows, 'fuehlen_mcm_tension'):.6f}",
    }


def density_windows(rows: list[dict[str, str]], flags: list[bool]) -> list[tuple[int, int, int, float]]:
    windows: list[tuple[int, int, int, float]] = []
    for start in range(0, max(1, len(rows) - WINDOW + 1), STEP):
        end = min(len(rows), start + WINDOW)
        hits = sum(flags[start:end])
        share = hits / (end - start) if end > start else 0.0
        windows.append((start, end - 1, hits, share))
    return sorted(windows, key=lambda item: (item[3], item[2]), reverse=True)


def context_reading(row: dict[str, str]) -> str:
    share = float(row["target_profile_share"])
    strain = float(row["cluster_avg_strain"])
    rekopplung = float(row["cluster_avg_rekopplung"])
    if share >= 0.30 and rekopplung >= 0.65 and strain <= 0.20:
        return "dichte_rekoppelnde_vorform"
    if share >= 0.30 and strain >= 0.25:
        return "dichte_spannungsnahe_vorform"
    if share >= 0.20:
        return "lokal_verdichteter_nebelraum"
    return "breite_offene_vorform"


def scan() -> list[dict[str, str]]:
    target_profiles, _families, _roles = source_profiles()
    out: list[dict[str, str]] = []
    for world in TARGET_WORLDS:
        path = HOLDOUT_EPISODES[world]
        rows = read_csv(path)
        flags = [profile_from_episode(row) in target_profiles for row in rows]
        used_ranges: list[tuple[int, int]] = []
        rank = 0
        for start, end, hits, share in density_windows(rows, flags):
            if any(not (end < left or start > right) for left, right in used_ranges):
                continue
            rank += 1
            used_ranges.append((start, end))
            before = rows[max(0, start - CONTEXT) : start]
            body = rows[start : end + 1]
            after = rows[end + 1 : min(len(rows), end + 1 + CONTEXT)]
            before_s = summarize_slice(before)
            body_s = summarize_slice(body)
            after_s = summarize_slice(after)
            record = {
                "world": world,
                "window_rank": str(rank),
                "start_tick": rows[start].get("tick", str(start + 1)),
                "end_tick": rows[end].get("tick", str(end + 1)),
                "window_length": str(end - start + 1),
                "target_profile_hits": str(hits),
                "target_profile_share": f"{share:.6f}",
                "before_effects": before_s["effects"],
                "cluster_effects": body_s["effects"],
                "after_effects": after_s["effects"],
                "before_families": before_s["families"],
                "cluster_families": body_s["families"],
                "after_families": after_s["families"],
                "before_preview_symbols": before_s["preview_symbols"],
                "cluster_preview_symbols": body_s["preview_symbols"],
                "after_preview_symbols": after_s["preview_symbols"],
                "cluster_avg_rekopplung": body_s["avg_rekopplung"],
                "cluster_avg_strain": body_s["avg_strain"],
                "cluster_avg_form_flow": body_s["avg_form_flow"],
                "cluster_avg_form_stability": body_s["avg_form_stability"],
                "cluster_avg_energy_tone": body_s["avg_energy_tone"],
                "cluster_avg_energy_shift": body_s["avg_energy_shift"],
                "cluster_avg_tension": body_s["avg_tension"],
            }
            record["context_reading"] = context_reading(record)
            out.append(record)
            if rank >= TOP_WINDOWS_PER_WORLD:
                break
    return out


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = list(rows[0].keys()) if rows else []
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    readings = Counter(row["context_reading"] for row in rows)
    lines = [
        "# 1959 - Lokaler Kontext offener Vorformen",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Bleibt die offene Vorform ein breiter Nebelraum oder bildet sie lokale Verdichtungszonen?",
        "- Unterprüfung: Nicht harte Folgeblöcke, sondern dichte Zielprofil-Fenster werden mit Vorlauf und Nachlauf gelesen.",
        "- Folgeschritt: Stabile Dichtefenster können später als mögliche Rollenkeime verfolgt werden.",
        "",
        "## Datengrundlage",
        "",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        f"- Fenstergröße: {WINDOW} Episodenzeilen",
        f"- Schrittweite: {STEP} Episodenzeilen",
        f"- Kontext je Seite: {CONTEXT} Episodenzeilen",
        "",
        "## Ergebnis",
        "",
        f"- Dichtefenster: {len(rows)}",
        f"- Lesungen: {', '.join(f'{key}:{value}' for key, value in readings.most_common())}",
        "",
        "| Welt | Tickbereich | Treffer | Anteil | Lesung | Cluster-Wirkung | Vorlauf | Nachlauf |",
        "|---|---:|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['world']} | {row['start_tick']}-{row['end_tick']} | {row['target_profile_hits']} | {row['target_profile_share']} | {row['context_reading']} | {row['cluster_effects']} | {row['before_effects']} | {row['after_effects']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Die offene Vorform erscheint nicht als harter Block. Sie wirkt verteilt und bildet lokale Dichtefenster. Das passt besser zur bisherigen Lesung als Nebelraum: Die Lage ist wiederkehrend, aber noch nicht zu einer festen Rolle verdichtet.",
            "",
            "Wichtig ist: Gerade weil keine langen Folgeblöcke gefunden wurden, sollte die nächste Prüfung nicht nach starren Sequenzen suchen. Entscheidend ist, ob Dichtefenster über Preview-Symbole, Familiennähe und Feldwirkung wiederkehren.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = scan()
    write_csv(rows)
    write_md(rows)
    print(f"density_windows={len(rows)}")
    for row in rows[:10]:
        print(row["world"], row["start_tick"], row["end_tick"], row["target_profile_share"], row["context_reading"])


if __name__ == "__main__":
    main()
