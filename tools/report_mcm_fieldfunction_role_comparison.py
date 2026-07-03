from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "docs" / "befunde" / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1384_FELDFUNKTIONSROLLEN_VERGLEICH.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1384_FELDFUNKTIONSROLLEN_VERGLEICH.md"

ROLES = [
    "brueckennaehe",
    "zentrumsnaehe",
    "mischrolle_brueckennaehe_zentrumsnaehe",
]

NUMERIC_KEYS = [
    "drift_pct",
    "abs_drift_pct",
    "avg_abs_return_pct",
    "avg_range_pct",
    "max_range_pct",
    "direction_change_ratio",
    "direction_persistence",
    "sensory_delta",
    "rekopplung_delta",
    "strain_delta_next",
    "rekopplung_delta_next",
]


def _float(row: dict[str, str], key: str) -> float:
    try:
        out = float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if out != out else out


def _read() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _avg(rows: list[dict[str, str]], key: str) -> float:
    return mean(_float(row, key) for row in rows) if rows else 0.0


def _ratio(rows: list[dict[str, str]], key: str) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if int(_float(row, key))) / len(rows)


def _top(counter: Counter[str], n: int = 5) -> str:
    return ", ".join(f"{name}:{count}" for name, count in counter.most_common(n)) or "-"


def build_report() -> None:
    rows = _read()
    selected = {role: [row for row in rows if row.get("passive_role_near") == role] for role in ROLES}
    if not any(selected.values()):
        raise RuntimeError("no role rows found")

    summary_rows: list[dict[str, str]] = []
    for role, role_rows in selected.items():
        raw_forms = Counter(row.get("raw_form", "-") for row in role_rows)
        worlds = Counter(row.get("world", "-") for row in role_rows)
        effects = Counter(row.get("effect_class", "-") for row in role_rows)
        previews = Counter(row.get("preview", "-") for row in role_rows)
        families = Counter(row.get("family", "-") for row in role_rows)
        out = {
            "role": role,
            "count": str(len(role_rows)),
            "preview_carry_ratio": f"{_ratio(role_rows, 'preview_carry_next'):.6f}",
            "raw_forms": _top(raw_forms),
            "worlds": _top(worlds),
            "effects": _top(effects),
            "previews": _top(previews),
            "families": _top(families),
        }
        for key in NUMERIC_KEYS:
            out[key] = f"{_avg(role_rows, key):.6f}"
        summary_rows.append(out)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    lines = [
        "# 1384 - Feldfunktionsrollen im Vergleich",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht drei passive Rollenlinien aus `1382`:",
        "",
        "- Bruecke-only",
        "- Zentrum-only",
        "- Bruecke/Zentrum-Mischrolle",
        "",
        "Ziel ist zu pruefen, ob die Mischrolle eigene Merkmale traegt oder nur eine Zwischenbezeichnung aus Bruecke und Zentrum ist.",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Kurzbefund",
        "",
    ]

    for row in summary_rows:
        lines.extend(
            [
                f"### {row['role']}",
                "",
                f"- Fenster: `{row['count']}`",
                f"- Preview-Folgecarry: `{row['preview_carry_ratio']}`",
                f"- Rohweltformen: `{row['raw_forms']}`",
                f"- Welten: `{row['worlds']}`",
                f"- Effekte: `{row['effects']}`",
                f"- Familien: `{row['families']}`",
                f"- Drift: `{row['drift_pct']}`",
                f"- absolute Drift: `{row['abs_drift_pct']}`",
                f"- durchschnittliche Bewegung: `{row['avg_abs_return_pct']}`",
                f"- Range: `{row['avg_range_pct']}`",
                f"- Richtungswechsel: `{row['direction_change_ratio']}`",
                f"- Persistenz: `{row['direction_persistence']}`",
                f"- Sensorikdelta: `{row['sensory_delta']}`",
                f"- Rekopplungsdelta: `{row['rekopplung_delta']}`",
                f"- Folge-Strain-Delta: `{row['strain_delta_next']}`",
                f"- Folge-Rekopplungsdelta: `{row['rekopplung_delta_next']}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Lesung",
            "",
            "Bruecke-only ist die breiteste Rolle und tritt in mehreren Rohweltformen auf.",
            "Zentrum-only ist deutlich seltener und liegt ebenfalls meist in gemischter Rohwelt.",
            "Die Mischrolle ist nicht nur die Summe beider Rollen: sie ist haeufiger als Zentrum-only, stark in gemischter Rohwelt gebunden und zeigt hohe Carry-Naehe.",
            "",
            "Damit wirkt sie wie eine eigene passive Feldlinie zwischen Uebergang und Zentrumsnaehe.",
            "Sie sollte vorerst nicht als harte neue Kategorie behandelt werden, sondern als Kandidat fuer eine wiederkehrende Kopplungsfunktion.",
            "",
            "## Grenze",
            "",
            "Die Rohweltform `gemischte_rohwelt` ist noch zu breit.",
            "Der naechste saubere Schritt ist eine feinere Zerlegung dieser gemischten Rohwelt in visuelle und tonale Unterformen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte `gemischte_rohwelt` innerhalb der Mischrolle feiner gelesen werden: welche konkreten Ton-, Range-, Richtungswechsel- und Verdichtungsfolgen tragen diese Kopplung?",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
