from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _float(value: object) -> float:
    try:
        out = float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if out != out else out


def _role(row: dict[str, str]) -> str:
    sequence = str(row.get("base_sequence") or "")
    during_raw = str(row.get("during_raw_class") or "")
    narrows = int(_float(row.get("range_narrows_vs_pre")))
    hearing = int(_float(row.get("hearing_rises_vs_pre")))
    pressure = int(_float(row.get("pressure_rises_vs_pre")))
    compact = narrows and hearing and pressure
    if sequence.startswith("ruhig_zentrumsnah->") and "lauter_feldkontakt" in sequence:
        return "zentrumskontakt_wird_aktiviert" if compact else "zentrumskontakt_mit_hoeranstieg"
    if sequence == "lauter_feldkontakt->lauter_feldkontakt":
        if during_raw == "laute_oder_druckvolle_rohwelt":
            return "randnaher_kontaktdruck"
        return "lauter_kontakt_bleibt_offen"
    if sequence.endswith("->lauter_feldkontakt"):
        return "brueckenuebergang_zum_lauten_kontakt" if compact else "offener_uebergang_zum_lauten_kontakt"
    if sequence.endswith("->normale_weltspannung"):
        return "rueckbindung_in_normale_weltspannung"
    return "unklare_mikrophase"


def _read_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            out: dict[str, object] = dict(row)
            out["phase_role"] = _role(row)
            out["compact_sensory_phase"] = int(
                _float(row.get("range_narrows_vs_pre"))
                and _float(row.get("hearing_rises_vs_pre"))
                and _float(row.get("pressure_rises_vs_pre"))
            )
            rows.append(out)
    return rows


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path) -> None:
    role_counts = Counter(str(row["phase_role"]) for row in rows)
    sequence_counts = Counter(str(row["base_sequence"]) for row in rows)
    compact_count = sum(int(row["compact_sensory_phase"]) for row in rows)
    bridge_count = sum(1 for row in rows if "bruecke" in str(row["phase_role"]))
    rand_count = sum(1 for row in rows if "rand" in str(row["phase_role"]))
    center_count = sum(1 for row in rows if "zentrum" in str(row["phase_role"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Hoerbarer schmaler Shift - passive Rollenlesung",
        "",
        "Diese Diagnose liest die komprimierte Sinnesphase aus `1350` gegen passive Feldrollen.",
        "",
        "Wichtig: Die Rollen werden hier nicht als neue Mechanik gesetzt. Es ist eine Ruecklesung der Lagefolge:",
        "",
        "```text",
        "Welche Feldrolle wird durch diese Mikrophase nahegelegt?",
        "```",
        "",
        "Die Diagnose erzeugt keine Handlung, keine Richtung und kein Gate.",
        "",
        "## Verdichtung",
        "",
        f"- gelesene Fenster: `{len(rows)}`",
        f"- komprimierte Sinnesphase: `{compact_count}`",
        f"- Brueckennaehe: `{bridge_count}`",
        f"- Randnaehe: `{rand_count}`",
        f"- Zentrumskontakt: `{center_count}`",
        "",
        "Rollen:",
        "",
    ]
    for role, count in role_counts.most_common():
        lines.append(f"- `{role}`: `{count}`")
    lines.extend(["", "Lagefolgen:", ""])
    for sequence, count in sequence_counts.most_common():
        lines.append(f"- `{sequence}`: `{count}`")
    lines.extend(
        [
            "",
            "## Fenster",
            "",
            "| Asset | Welt | Ticks | Lagefolge | passive Rolle | kompakt | Klasse | Hoeren | Druck | Range |",
            "|---|---|---:|---|---|---:|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| {asset} | {world} | {start_tick}-{end_tick} | `{base_sequence}` | `{phase_role}` | {compact_sensory_phase} | `{during_raw_class}` | {pre_hoeren}->{during_hoeren}->{post_hoeren} | {pre_druck}->{during_druck}->{post_druck} | {pre_range}->{during_range}->{post_range} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die komprimierte Sinnesphase faellt nicht in eine einzige Rolle.",
            "",
            "Sie erscheint vor allem als Uebergang in lauteren Kontakt, als randnaher Kontaktdruck und als Aktivierung aus zentrumsnaher Ruhe.",
            "",
            "Damit wirkt sie eher wie eine lokale Feldfunktion: Sie kann Bruecke, Randnaehe oder aktivierten Zentrumskontakt tragen, je nachdem aus welcher Lagefolge sie entsteht.",
            "",
            "Wie es weitergeht: Als naechstes sollte diese Rollenlesung gegen das bestehende Bedeutungsnetz gelesen werden: Welche `dio_*`-Familien liegen in Fenstern mit `brueckenuebergang_zum_lauten_kontakt`, und bleiben sie in Folgefenstern stabil oder driften sie?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/befunde/1350_HOERBARER_SCHMALER_SHIFT_ROHWELTLUPE.csv")
    parser.add_argument("--out", default="docs/befunde/1351_HOERBARER_SCHMALER_SHIFT_ROLLELESUNG.md")
    parser.add_argument("--csv-out", default="docs/befunde/1351_HOERBARER_SCHMALER_SHIFT_ROLLELESUNG.csv")
    args = parser.parse_args()

    rows = _read_rows(Path(args.input))
    if not rows:
        raise RuntimeError("no rows to read")
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
