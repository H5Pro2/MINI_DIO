from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
SHIFT_CSV = ROOT / "docs" / "befunde" / "1352_HOERBARER_SCHMALER_SHIFT_SYMBOLKOPPLUNG.csv"
CONTROL_CSV = ROOT / "docs" / "befunde" / "1353_HOERBARER_SCHMALER_SHIFT_KONTROLLKOPPLUNG.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1354_HOERBARER_SCHMALER_SHIFT_DIFFERENZPROFIL.md"
OUT_CSV = ROOT / "docs" / "befunde" / "1354_HOERBARER_SCHMALER_SHIFT_DIFFERENZPROFIL.csv"


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _counter(rows: list[dict[str, str]], key: str) -> Counter[str]:
    return Counter(row.get(key, "-") or "-" for row in rows)


def _mean(rows: list[dict[str, str]], key: str) -> float:
    return mean(_float(row.get(key, "0")) for row in rows)


def _delta_counter(shift: Counter[str], control: Counter[str]) -> list[dict[str, str]]:
    keys = sorted(set(shift) | set(control))
    total_shift = sum(shift.values()) or 1
    total_control = sum(control.values()) or 1
    out = []
    for key in keys:
        shift_share = shift[key] / total_shift
        control_share = control[key] / total_control
        out.append(
            {
                "item": key,
                "shift_count": str(shift[key]),
                "control_count": str(control[key]),
                "shift_share": f"{shift_share:.6f}",
                "control_share": f"{control_share:.6f}",
                "share_delta": f"{shift_share - control_share:.6f}",
            }
        )
    out.sort(key=lambda row: abs(_float(row["share_delta"])), reverse=True)
    return out


def build_report() -> None:
    shift = _rows(SHIFT_CSV)
    control = _rows(CONTROL_CSV)

    symbol_delta = _delta_counter(_counter(shift, "top_symbol_family"), _counter(control, "top_symbol_family"))
    preview_delta = _delta_counter(_counter(shift, "top_preview_symbol"), _counter(control, "top_preview_symbol"))
    meaning_delta = _delta_counter(_counter(shift, "top_meaning_state"), _counter(control, "top_meaning_state"))

    rows = []
    for category, deltas in [
        ("symbol_family", symbol_delta),
        ("mcm_preview_symbol", preview_delta),
        ("meaning_state", meaning_delta),
    ]:
        for row in deltas:
            out = {"category": category}
            out.update(row)
            rows.append(out)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    shift_rekopplung = _mean(shift, "avg_rekopplung")
    control_rekopplung = _mean(control, "avg_rekopplung")
    shift_strain = _mean(shift, "avg_strain")
    control_strain = _mean(control, "avg_strain")
    shift_coupling = _mean(shift, "avg_sensory_coupling")
    control_coupling = _mean(control, "avg_sensory_coupling")

    lines = [
        "# 1354 - Hoerbarer schmaler Shift: Differenzprofil",
        "",
        "## Zweck",
        "",
        "Dieses Profil vergleicht die Symbolkopplung der Hoer-/Druckfenster aus `1352` mit Kontrollfenstern ohne Hoeranstieg aus `1353`.",
        "Damit wird getrennt, was allgemeine Innenfeldstabilitaet ist und was spezifischer zur kompakten Hoer-/Druckphase gehoert.",
        "",
        "## Metrische Differenz",
        "",
        f"- Rekopplung: Shift `{shift_rekopplung:.6f}` vs Kontrolle `{control_rekopplung:.6f}`; Delta `{shift_rekopplung - control_rekopplung:.6f}`",
        f"- Strain: Shift `{shift_strain:.6f}` vs Kontrolle `{control_strain:.6f}`; Delta `{shift_strain - control_strain:.6f}`",
        f"- Sinneskopplung: Shift `{shift_coupling:.6f}` vs Kontrolle `{control_coupling:.6f}`; Delta `{shift_coupling - control_coupling:.6f}`",
        "",
        "## Staerkste Unterschiede: Symbolfamilien",
        "",
    ]
    for row in symbol_delta[:8]:
        lines.append(
            f"- `{row['item']}`: Shift {row['shift_count']} / Kontrolle {row['control_count']} / Delta {row['share_delta']}"
        )
    lines.extend(["", "## Staerkste Unterschiede: MCM-Preview-Symbole", ""])
    for row in preview_delta[:8]:
        lines.append(
            f"- `{row['item']}`: Shift {row['shift_count']} / Kontrolle {row['control_count']} / Delta {row['share_delta']}"
        )
    lines.extend(["", "## Staerkste Unterschiede: Bedeutungszustaende", ""])
    for row in meaning_delta[:5]:
        lines.append(
            f"- `{row['item']}`: Shift {row['shift_count']} / Kontrolle {row['control_count']} / Delta {row['share_delta']}"
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "`meaning_stable_inner_field` ist nicht spezifisch fuer den Hoeranstieg; es erscheint auch in der Kontrollgruppe.",
            "Spezifischer sind die Rollen-/Preview-Verschiebungen und die leicht hoehere Rekopplung der Shiftfenster.",
            "Damit liegt die relevante Information nicht im blossen Stabilitaetslabel, sondern in der Feldrolle und der lokalen Symbolkopplung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob die Shift-spezifischen Preview-Symbole vor oder nach dem Fenster weitertragen. Das klaert, ob der Shift nur ein lokaler Kontakt ist oder eine kurze Uebergangsspur im Feld hinterlaesst.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
