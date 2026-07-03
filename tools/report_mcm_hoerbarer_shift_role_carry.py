from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "docs" / "befunde" / "1355_HOERBARER_SCHMALER_SHIFT_NACHHALLSPUR.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1356_HOERBARER_SCHMALER_SHIFT_ROLLEN_NACHHALL.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1356_HOERBARER_SCHMALER_SHIFT_ROLLEN_NACHHALL.md"


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0


def build_report(input_path: Path = INPUT, csv_out: Path = OUT_CSV, md_out: Path = OUT_MD) -> None:
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    by_role: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_role[row["phase_role"]].append(row)

    out_rows: list[dict[str, str]] = []
    for role, role_rows in sorted(by_role.items()):
        out_rows.append(
            {
                "phase_role": role,
                "windows": str(len(role_rows)),
                "preview_pre_carry": str(sum(int(row["preview_pre_carry"]) for row in role_rows)),
                "preview_post_carry": str(sum(int(row["preview_post_carry"]) for row in role_rows)),
                "family_pre_carry": str(sum(int(row["family_pre_carry"]) for row in role_rows)),
                "family_post_carry": str(sum(int(row["family_post_carry"]) for row in role_rows)),
                "avg_during_rekopplung": f"{mean(_float(row['during_avg_rekopplung']) for row in role_rows):.6f}",
                "avg_post_rekopplung": f"{mean(_float(row['post_avg_rekopplung']) for row in role_rows):.6f}",
                "avg_post_rekopplung_delta": f"{mean(_float(row['post_rekopplung_delta']) for row in role_rows):.6f}",
                "avg_during_strain": f"{mean(_float(row['during_avg_strain']) for row in role_rows):.6f}",
                "avg_post_strain": f"{mean(_float(row['post_avg_strain']) for row in role_rows):.6f}",
                "avg_post_strain_delta": f"{mean(_float(row['post_strain_delta']) for row in role_rows):.6f}",
            }
        )

    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    lines = [
        "# 1356 - Hoerbarer schmaler Shift: Rollen-Nachhall",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die Nachhallspur aus `1355` rollenbezogen.",
        "Damit wird getrennt, ob Bruecke, Randdruck und Zentrumskontakt unterschiedlich weitertragen.",
        "",
        "## Rollenbefund",
        "",
        "| Rolle | Fenster | Preview weiter | Familie weiter | Rekopplung Delta | Strain Delta |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in out_rows:
        lines.append(
            "| {phase_role} | {windows} | {preview_post_carry} | {family_post_carry} | {avg_post_rekopplung_delta} | {avg_post_strain_delta} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Die Nachhallspur ist rollenabhaengig zu lesen.",
            "Preview-Gleichheit zeigt, ob ein lokaler Kontakt als gleiche MCM-Preview weiterliegt.",
            "Familien-Gleichheit zeigt, ob die grobe `dio_*`-Familie weiterliegt.",
            "Rekopplungs- und Straindelta zeigen, ob der Kontakt danach entlastet, stabilisiert oder belastet.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte nur die staerkste Rollenlinie ausgewaehlt und gegen weitere Welten geprueft werden. Dadurch vermeiden wir Fragmentanalyse und testen gezielt, ob eine Feldfunktion reproduzierbar ist.",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(INPUT))
    parser.add_argument("--csv-out", default=str(OUT_CSV))
    parser.add_argument("--out", default=str(OUT_MD))
    args = parser.parse_args()
    build_report(Path(args.input), Path(args.csv_out), Path(args.out))
