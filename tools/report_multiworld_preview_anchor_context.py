from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root

from report_late_drift_profile_holdout_scan import HOLDOUT_EPISODES, profile_from_episode
from report_late_drift_profile_role_binding import source_profiles


ROOT = Path(__file__).resolve().parents[1]
ANCHORS = befunde_root(ROOT) / "1960_OFFENE_VORFORM_PREVIEW_SYMBOL_REKURRENZ.csv"
OUT_CSV = befunde_root(ROOT) / "1961_MEHRWELTLICHE_PREVIEW_ANKER_KONTEXT.csv"
OUT_MD = befunde_root(ROOT) / "1961_MEHRWELTLICHE_PREVIEW_ANKER_KONTEXT.md"

CONTEXT = 6


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def avg_float(rows: list[dict[str, str]], key: str) -> float:
    values: list[float] = []
    for row in rows:
        try:
            values.append(float(row.get(key, "") or 0.0))
        except ValueError:
            pass
    return sum(values) / len(values) if values else 0.0


def top(counter: Counter[str], n: int = 4) -> str:
    return ";".join(f"{key}:{value}" for key, value in counter.most_common(n) if key)


def summarize(rows: list[dict[str, str]]) -> dict[str, str]:
    return {
        "effects": top(Counter(row.get("passive_mcm_effect_class", "") for row in rows)),
        "families": top(Counter(row.get("symbol_family", "") for row in rows)),
        "preview_symbols": top(Counter(row.get("mcm_field_episode_preview_symbol", "") for row in rows)),
        "avg_rekopplung": f"{avg_float(rows, 'mcm_rekopplung_quality'):.6f}",
        "avg_strain": f"{avg_float(rows, 'mcm_strain_quality'):.6f}",
        "avg_afterimage": f"{avg_float(rows, 'mini_afterimage'):.6f}",
        "avg_recurrence": f"{avg_float(rows, 'mini_recurrence_strength'):.6f}",
        "avg_form_stability": f"{avg_float(rows, 'sehen_form_stability'):.6f}",
        "avg_energy_shift": f"{avg_float(rows, 'hoeren_energy_shift'):.6f}",
        "avg_tension": f"{avg_float(rows, 'fuehlen_mcm_tension'):.6f}",
    }


def anchor_reading(row: dict[str, str]) -> str:
    rek = float(row["anchor_avg_rekopplung"])
    strain = float(row["anchor_avg_strain"])
    afterimage = float(row["anchor_avg_afterimage"])
    recurrence = float(row["anchor_avg_recurrence"])
    profile_share = float(row["target_profile_share"])
    if rek >= 0.65 and strain <= 0.20 and recurrence >= 0.20:
        return "rekoppelnder_rollenkeim"
    if profile_share >= 0.40 and afterimage >= 0.15:
        return "nachhallender_vorformanker"
    if strain >= 0.25:
        return "spannungsnaher_vorformanker"
    return "oberflaechenanker"


def collect() -> list[dict[str, str]]:
    target_profiles, _families, _roles = source_profiles()
    anchors = [row for row in read_csv(ANCHORS) if row.get("reading") == "mehrweltlicher_preview_anker"]
    anchor_symbols = {row["preview_symbol"] for row in anchors}

    out: list[dict[str, str]] = []
    for world, path in HOLDOUT_EPISODES.items():
        rows = read_csv(path)
        positions: dict[str, list[int]] = defaultdict(list)
        for idx, row in enumerate(rows):
            symbol = row.get("mcm_field_episode_preview_symbol", "")
            if symbol in anchor_symbols:
                positions[symbol].append(idx)

        for anchor in anchors:
            symbol = anchor["preview_symbol"]
            idxs = positions.get(symbol, [])
            if not idxs:
                continue
            before_rows: list[dict[str, str]] = []
            anchor_rows: list[dict[str, str]] = []
            after_rows: list[dict[str, str]] = []
            target_hits = 0
            for idx in idxs:
                before_rows.extend(rows[max(0, idx - CONTEXT) : idx])
                anchor_rows.append(rows[idx])
                after_rows.extend(rows[idx + 1 : min(len(rows), idx + 1 + CONTEXT)])
                if profile_from_episode(rows[idx]) in target_profiles:
                    target_hits += 1

            before = summarize(before_rows)
            center = summarize(anchor_rows)
            after = summarize(after_rows)
            record = {
                "preview_symbol": symbol,
                "world": world,
                "occurrences": str(len(idxs)),
                "target_profile_hits": str(target_hits),
                "target_profile_share": f"{target_hits / len(idxs):.6f}" if idxs else "0.000000",
                "first_tick": rows[idxs[0]].get("tick", str(idxs[0] + 1)),
                "last_tick": rows[idxs[-1]].get("tick", str(idxs[-1] + 1)),
                "before_effects": before["effects"],
                "anchor_effects": center["effects"],
                "after_effects": after["effects"],
                "before_preview_symbols": before["preview_symbols"],
                "after_preview_symbols": after["preview_symbols"],
                "anchor_families": center["families"],
                "anchor_avg_rekopplung": center["avg_rekopplung"],
                "anchor_avg_strain": center["avg_strain"],
                "anchor_avg_afterimage": center["avg_afterimage"],
                "anchor_avg_recurrence": center["avg_recurrence"],
                "anchor_avg_form_stability": center["avg_form_stability"],
                "anchor_avg_energy_shift": center["avg_energy_shift"],
                "anchor_avg_tension": center["avg_tension"],
            }
            record["anchor_reading"] = anchor_reading(record)
            out.append(record)
    return sorted(out, key=lambda row: (row["anchor_reading"], int(row["occurrences"])), reverse=True)


def write_csv(rows: list[dict[str, str]]) -> None:
    fields = list(rows[0].keys()) if rows else []
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]]) -> None:
    reading_counts = Counter(row["anchor_reading"] for row in rows)
    symbol_counts = Counter(row["preview_symbol"] for row in rows)
    lines = [
        "# 1961 - Kontext mehrweltlicher Preview-Anker",
        "",
        "## Hierarchie der Prüfung",
        "",
        "- Grundfrage: Sind mehrweltliche Preview-Anker Rollenkeime oder nur Oberflächenmarken?",
        "- Unterprüfung: Auftreten, Vorlauf, Nachlauf, Nachhall und Rekurrenz werden pro Welt gelesen.",
        "- Folgeschritt: Nur rekoppelnde oder nachhallende Anker werden später als Kandidaten für organische Feldvertiefung genutzt.",
        "",
        "## Datengrundlage",
        "",
        f"- Ankerquelle: `{ANCHORS.relative_to(ROOT)}`",
        f"- Ergebnis-Tabelle: `{OUT_CSV.relative_to(ROOT)}`",
        "",
        "## Ergebnis",
        "",
        f"- Anker/Welt-Kombinationen: {len(rows)}",
        f"- Lesungen: {', '.join(f'{key}:{value}' for key, value in reading_counts.most_common())}",
        f"- Symbole: {', '.join(f'{key}:{value}' for key, value in symbol_counts.most_common())}",
        "",
        "| Preview | Welt | Treffer | Profilanteil | Lesung | Wirkung | Vorlauf | Nachlauf |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for row in rows[:18]:
        lines.append(
            f"| {row['preview_symbol']} | {row['world']} | {row['occurrences']} | {row['target_profile_share']} | {row['anchor_reading']} | {row['anchor_effects']} | {row['before_effects']} | {row['after_effects']} |"
        )
    lines.extend(
        [
            "",
            "## Arbeitsdeutung",
            "",
            "Mehrweltliche Preview-Anker sind nicht automatisch Rollenkeime. Ein Teil wirkt nur als Oberflächenanker. Interessant werden sie dort, wo Profilanteil, Nachhall, Rekurrenz und Rekopplung gemeinsam tragen.",
            "",
            "Damit entsteht eine saubere Trennung: Feldlage kann breit wiederkehren, Preview-Symbol kann mehrweltlich sein, aber Rollenkeim entsteht erst durch zusätzliche Kopplungsqualität.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = collect()
    write_csv(rows)
    write_md(rows)
    print(f"anchor_contexts={len(rows)}")
    for row in rows[:12]:
        print(row["preview_symbol"], row["world"], row["occurrences"], row["anchor_reading"], row["target_profile_share"])


if __name__ == "__main__":
    main()
