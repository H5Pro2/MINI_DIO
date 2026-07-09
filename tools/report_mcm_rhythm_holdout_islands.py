from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1395_HOLDOUT_FELDROLLEN_STABILITAET.csv"
OUT_CSV = befunde_root(ROOT) / "1414_RHYTHMUS_HOLDOUT_INSELN.csv"
OUT_MD = befunde_root(ROOT) / "1414_RHYTHMUS_HOLDOUT_INSELN.md"

RHYTHM_WORLDS = {
    "HOLDOUT_RHYTHM_REGULAR",
    "HOLDOUT_RHYTHM_BLOCK",
    "HOLDOUT_RHYTHM_IRREGULAR",
    "HOLDOUT_RHYTHM_WAVE",
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _state_for_group(rows: list[dict[str, str]], total_world_windows: int) -> str:
    if not rows:
        return "nicht_vorhanden"
    recurrence = len(rows)
    share = recurrence / max(1, total_world_windows)
    avg_strain = mean(_float(row, "strain") for row in rows)
    avg_rekopplung = mean(_float(row, "rekopplung") for row in rows)
    avg_carry = mean(_float(row, "carry") for row in rows)
    if recurrence >= 3 and avg_rekopplung >= 0.70 and avg_carry >= 0.53 and avg_strain <= 0.16:
        return "wiederkehrende_feldinsel"
    if recurrence >= 2 and share >= 0.20:
        return "schwache_inselwiederkehr"
    return "oberflaechenvarianz"


def main() -> None:
    rows = [row for row in _read_rows(IN_CSV) if row.get("world") in RHYTHM_WORLDS]
    by_world: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_world[row["world"]].append(row)

    out_rows: list[dict[str, str]] = []
    for world, world_rows in sorted(by_world.items()):
        total = len(world_rows)
        new_rows = [row for row in world_rows if row.get("holdout_state") == "neue_holdout_lage"]
        weak_rows = [row for row in world_rows if row.get("holdout_state") == "rolle_schwach_beruehrt"]
        neighbor_rows = [row for row in world_rows if row.get("holdout_state") == "rolle_als_nachbarschaft"]
        signature_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in new_rows:
            signature_groups[row["signature"]].append(row)

        if signature_groups:
            for signature, group_rows in sorted(signature_groups.items(), key=lambda item: (-len(item[1]), item[0])):
                family_counts = Counter(row.get("family", "") for row in group_rows)
                effect_mix_counts = Counter(row.get("effect_mix", "") for row in group_rows)
                starts = [int(row["start_tick"]) for row in group_rows]
                ends = [int(row["end_tick"]) for row in group_rows]
                out_rows.append(
                    {
                        "world": world,
                        "signature": signature,
                        "new_windows": str(len(group_rows)),
                        "world_windows": str(total),
                        "new_share": f"{len(new_rows) / max(1, total):.6f}",
                        "weak_windows": str(len(weak_rows)),
                        "neighbor_windows": str(len(neighbor_rows)),
                        "dominant_family": family_counts.most_common(1)[0][0],
                        "family_mix": " | ".join(f"{key}:{value}" for key, value in family_counts.most_common()),
                        "effect_mix": " | ".join(f"{key}:{value}" for key, value in effect_mix_counts.most_common()),
                        "avg_carry": f"{mean(_float(row, 'carry') for row in group_rows):.6f}",
                        "avg_strain": f"{mean(_float(row, 'strain') for row in group_rows):.6f}",
                        "avg_rekopplung": f"{mean(_float(row, 'rekopplung') for row in group_rows):.6f}",
                        "first_start": str(min(starts)),
                        "last_end": str(max(ends)),
                        "island_state": _state_for_group(group_rows, total),
                    }
                )
        else:
            out_rows.append(
                {
                    "world": world,
                    "signature": "-",
                    "new_windows": "0",
                    "world_windows": str(total),
                    "new_share": "0.000000",
                    "weak_windows": str(len(weak_rows)),
                    "neighbor_windows": str(len(neighbor_rows)),
                    "dominant_family": "-",
                    "family_mix": "-",
                    "effect_mix": "-",
                    "avg_carry": "0.000000",
                    "avg_strain": "0.000000",
                    "avg_rekopplung": "0.000000",
                    "first_start": "-",
                    "last_end": "-",
                    "island_state": "keine_neue_lage",
                }
            )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    state_counts = Counter(row["island_state"] for row in out_rows)
    world_summary = []
    for world in sorted(by_world):
        world_out = [row for row in out_rows if row["world"] == world]
        world_summary.append(
            f"- `{world}`: {', '.join(f'{key}:{value}' for key, value in Counter(row['island_state'] for row in world_out).most_common())}"
        )

    island_lines = [
        f"- `{row['world']}` -> `{row['island_state']}`, Fenster `{row['new_windows']}/{row['world_windows']}`, Familie `{row['dominant_family']}`, Carry `{row['avg_carry']}`, Strain `{row['avg_strain']}`, Rekopplung `{row['avg_rekopplung']}`"
        for row in out_rows
        if row["island_state"] in {"wiederkehrende_feldinsel", "schwache_inselwiederkehr"}
    ]

    lines = [
        "# 1414 - Rhythmus Holdout Inseln",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft die neuen Rhythmus-Holdout-Lagen aus `1395`.",
        "",
        "Grundfrage:",
        "",
        "Sind die neuen Rhythmuslagen beginnende Bedeutungsinseln oder nur kurzlebige Oberflaechenvarianz?",
        "",
        "## Befund",
        "",
        f"- ausgewertete Rhythmuswelten: `{len(by_world)}`",
        f"- Inselzustaende: `{', '.join(f'{key}:{value}' for key, value in state_counts.most_common())}`",
        "",
        "## Weltuebersicht",
        "",
        *world_summary,
        "",
        "## Wiederkehrende oder schwache Inseln",
        "",
        *(island_lines or ["- keine wiederkehrende neue Rhythmusinsel"]),
        "",
        "## Lesung",
        "",
        "Neue Holdout-Lage bedeutet hier nicht automatisch neue Bedeutung.",
        "Entscheidend ist, ob dieselbe Signatur wiederkehrt, ueber mehrere Fenster getragen wird und dabei Carry, Rekopplung und Strain stabil bleiben.",
        "",
        "Die Rhythmuspruefung trennt damit zwei Faelle:",
        "",
        "- kurzlebige Oberflaechenvarianz: neue Lage taucht nur einzeln auf",
        "- beginnende Feldinsel: neue Lage wiederholt sich mit tragfaehiger Feldkopplung",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte eine Folgewelt mit derselben Rhythmusform, aber anderer Amplitude geprueft werden. Dadurch laesst sich unterscheiden, ob die Insel am Rhythmus selbst haengt oder nur an der konkreten Lautstaerke der Welt.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
