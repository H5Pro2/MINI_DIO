from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "docs" / "befunde" / "1382_FELDFUNKTIONSKARTE_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1383_BRUECKE_ZENTRUM_MISCHROLLE_ROHWELTLINIE.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1383_BRUECKE_ZENTRUM_MISCHROLLE_ROHWELTLINIE.md"

TARGET_ROLE = "mischrolle_brueckennaehe_zentrumsnaehe"
TARGET_FORM = "gemischte_rohwelt"


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


def build_report() -> None:
    rows = [
        row
        for row in _read()
        if row.get("passive_role_near") == TARGET_ROLE and row.get("raw_form") == TARGET_FORM
    ]
    if not rows:
        raise RuntimeError("no bridge-center mixed rawline rows")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    world_counts = Counter(row.get("world", "-") for row in rows)
    preview_counts = Counter(row.get("preview", "-") for row in rows)
    family_counts = Counter(row.get("family", "-") for row in rows)
    effect_counts = Counter(row.get("effect_class", "-") for row in rows)
    carry_count = sum(int(_float(row, "preview_carry_next")) for row in rows)

    lines = [
        "# 1383 - Bruecke/Zentrum-Mischrolle: Rohweltlinie",
        "",
        "## Zweck",
        "",
        "Diese Diagnose isoliert die staerkste Kopplung aus `1382`:",
        "",
        "```text",
        "mischrolle_brueckennaehe_zentrumsnaehe + gemischte_rohwelt",
        "```",
        "",
        "Geprueft wird, ob diese Linie eine echte wiederkehrende Feldform sein koennte oder nur eine breite interne Metriknaehe.",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Befund",
        "",
        f"- Fenster: `{len(rows)}`",
        f"- Preview-Folgecarry: `{carry_count}/{len(rows)}`",
        f"- Welten: {sorted(world_counts.items())}",
        f"- Effekte: {sorted(effect_counts.items())}",
        "",
        "## Durchschnittliche Rohweltmerkmale",
        "",
        f"- Drift: `{_avg(rows, 'drift_pct'):.6f}`",
        f"- absolute Drift: `{_avg(rows, 'abs_drift_pct'):.6f}`",
        f"- durchschnittliche absolute Bewegung: `{_avg(rows, 'avg_abs_return_pct'):.6f}`",
        f"- durchschnittliche Range: `{_avg(rows, 'avg_range_pct'):.6f}`",
        f"- maximale Range: `{_avg(rows, 'max_range_pct'):.6f}`",
        f"- Richtungswechsel: `{_avg(rows, 'direction_change_ratio'):.6f}`",
        f"- Persistenz: `{_avg(rows, 'direction_persistence'):.6f}`",
        "",
        "## Innenfeldmerkmale",
        "",
        f"- mittleres Sensorikdelta: `{_avg(rows, 'sensory_delta'):.6f}`",
        f"- mittleres Rekopplungsdelta: `{_avg(rows, 'rekopplung_delta'):.6f}`",
        f"- mittleres Folge-Strain-Delta: `{_avg(rows, 'strain_delta_next'):.6f}`",
        f"- mittleres Folge-Rekopplungsdelta: `{_avg(rows, 'rekopplung_delta_next'):.6f}`",
        "",
        "## Dominante Symbole",
        "",
        f"- Preview: {preview_counts.most_common(8)}",
        f"- Familien: {family_counts.most_common(8)}",
        "",
        "## Lesung",
        "",
        "Diese Linie liegt nicht in lauter oder eindeutig druckvoller Rohwelt, sondern in gemischter Rohwelt.",
        "Gleichzeitig zeigt sie hohe Rekopplung, tragende Carry-Naehe und niedrigen Strain.",
        "",
        "Das spricht dafuer, dass die Mischrolle nicht einfach aus Aussenlaerm entsteht.",
        "Sie wirkt eher wie ein Feldzustand, in dem Uebergang und Zentrumsnaehe gleichzeitig getragen werden.",
        "",
        "## Grenze",
        "",
        "Der Befund ist ein Indiz.",
        "Die Rohweltform `gemischte_rohwelt` ist breit. Sie muss spaeter feiner visuell/tonal zerlegt werden.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte diese Mischrolle gegen Bruecke-only und Zentrum-only verglichen werden. Entscheidend ist, ob sie eigene Rohweltmerkmale traegt oder nur zwischen beiden Rollen vermittelt.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
