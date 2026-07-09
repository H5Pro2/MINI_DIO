from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = befunde_root(ROOT) / "1396_HOLDOUT_ROHWELT_RUECKLESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1397_FELDROLLEN_BENENNUNGSPRUEFUNG.csv"
OUT_MD = befunde_root(ROOT) / "1397_FELDROLLEN_BENENNUNGSPRUEFUNG.md"


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "0") or 0.0)
    except ValueError:
        return 0.0


def _name_assessment(role: str, tensions: Counter[str]) -> str:
    if role == "weite_weltspannungsnaehe" and tensions.get("enge_unruhige_spannung", 0) > tensions.get("weite_unruhige_spannung", 0):
        return "name_zu_eng_unruhe_statt_weite"
    if role == "weite_weltspannungsnaehe":
        return "name_derzeit_plausibel"
    if role == "gerichtete_spannungsrolle":
        return "name_derzeit_plausibel"
    return "nicht_genug_daten"


def main() -> None:
    rows = _read_rows(IN_CSV)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["nearest_role_family"]].append(row)

    out_rows: list[dict[str, str]] = []
    for role, role_rows in sorted(grouped.items()):
        tensions = Counter(row["world_tension"] for row in role_rows)
        directions = Counter(row["raw_direction"] for row in role_rows)
        out_rows.append(
            {
                "role_family": role,
                "windows": str(len(role_rows)),
                "avg_range_pct": f"{mean(_float(row, 'raw_range_pct') for row in role_rows):.6f}",
                "avg_direction_changes": f"{mean(_float(row, 'raw_direction_changes') for row in role_rows):.6f}",
                "avg_tone_shift_abs": f"{mean(abs(_float(row, 'shift')) for row in role_rows):.6f}",
                "tensions": " | ".join(f"{key}:{value}" for key, value in tensions.most_common()),
                "directions": " | ".join(f"{key}:{value}" for key, value in directions.most_common()),
                "name_assessment": _name_assessment(role, tensions),
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "# 1397 - Feldrollen Benennungspruefung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die bisherige Rollenbezeichnung aus `1394` fachlich zur Rohwelt-Ruecklesung aus `1396` passt.",
        "",
        "## Befund",
        "",
        *[
            f"- `{row['role_family']}`: Fenster `{row['windows']}`, avg_range `{row['avg_range_pct']}`, avg_wechsel `{row['avg_direction_changes']}`, Spannungen `{row['tensions']}`, Bewertung `{row['name_assessment']}`"
            for row in out_rows
        ],
        "",
        "## Lesung",
        "",
        "`weite_weltspannungsnaehe` ist als Name wahrscheinlich zu eng.",
        "Die Rolle wird im Kontrast-Holdout auch durch enge, aber stark wechselnde Weltspannung beruehrt.",
        "Der synthetisch glatte Kontrolllauf beruehrt diese Rolle nicht stark, sondern landet bei `offene_nachbarschaftsrolle`.",
        "Die ruhige Driftwelt bleibt ebenfalls nur schwach bei `offene_nachbarschaftsrolle` und bildet keine starke Spannungsnaehe.",
        "Die High-Noisy-Drift beruehrt Spannungsnaehe nur schwach. Mehr Rauschen allein reicht also nicht aus, um eine starke Spannungsnaehe zu erzeugen.",
        "Fachlich genauer waere vorerst `unruhige_spannungsnaehe`: eine Feldrolle, die nicht nur grosse Range, sondern allgemein unruhige Spannungsdichte traegt.",
        "",
        "## Grenze",
        "",
        "Das ist eine Benennungspruefung, keine Umbenennung im Code.",
        "Die bestehende Datenkette bleibt reproduzierbar.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
