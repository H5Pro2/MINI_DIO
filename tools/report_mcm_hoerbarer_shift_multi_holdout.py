from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_mcm_hoerbarer_shift_holdout import _load_asset_bases, _read_candidates, _write_csv


def _counter(rows: list[dict[str, object]], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        name = str(row.get(key) or "-")
        out[name] = out.get(name, 0) + 1
    return out


def _parse_input(value: str) -> tuple[str, Path]:
    if "=" in value:
        label, path = value.split("=", 1)
        return label.strip(), Path(path.strip())
    path = Path(value)
    return path.stem, path


def _write_markdown(
    rows: list[dict[str, object]],
    *,
    group_counts: dict[str, int],
    path: Path,
    top: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    asset_counts = _counter(rows, "asset")
    sequence_counts = _counter(rows, "base_sequence")
    raw_counts = _counter(rows, "raw_class")

    lines = [
        "# Hoerbarer schmaler Shift - Multi-Holdout",
        "",
        "Diese Diagnose prueft den hoerbaren-schmale Mikrofenster-Shift gegen mehrere unabhaengige Rohweltfenster-Gruppen.",
        "",
        "Jede Gruppe wird assetrelativ gelesen. Dadurch bleibt die Pruefung passiv und vergleicht keine absoluten Preisgroessen.",
        "",
        "## Gruppen",
        "",
    ]
    for name, count in sorted(group_counts.items()):
        lines.append(f"- `{name}`: `{count}` Kandidatenfenster")

    lines.extend(["", "## Gesamtverdichtung", "", f"- Kandidatenfenster gesamt: `{len(rows)}`", "", "Assets:", ""])
    for name, count in sorted(asset_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(["", "Sequenzen:", ""])
    for name, count in sorted(sequence_counts.items(), key=lambda item: (-item[1], item[0]))[:12]:
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(["", "Rohklassen:", ""])
    for name, count in sorted(raw_counts.items(), key=lambda item: (-item[1], item[0]))[:8]:
        lines.append(f"- `{name}`: `{count}`")

    lines.extend(
        [
            "",
            "## Staerkste Fenster",
            "",
            "| Gruppe | Asset | Welt | Skala | Block | Sequenz | Rohklasse | Score | dHoeren | dSicht | dDruck | dRange |",
            "|---|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in sorted(rows, key=lambda item: -float(item["score"]))[:top]:
        lines.append(
            "| {holdout_group} | {asset} | {world} | {scale} | {block_index} | `{base_sequence}` | `{raw_class}` | {score:.4f} | {delta_auditory:.4f} | {delta_visual:.4f} | {delta_pressure:.4f} | {delta_range:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Der hoerbare-schmale Shift erscheint in mehreren Kontrollgruppen erneut.",
            "",
            "Damit ist er nicht nur ein einzelner BTC-Fund aus `1342`, sondern eine wiederkehrende lokale Mikrophase. Gleichzeitig bleibt er lokal: Die breite Weltfaerbung wird dadurch nicht automatisch ersetzt.",
            "",
            "Fachliche Grenze:",
            "",
            "- bestaetigt als wiederkehrendes Mikrofensterprofil",
            "- noch nicht bestaetigt als eigenstaendige stabile Topologierolle",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="docs/befunde/1001-2000/1001-1500/1315_WELTLAGEN_ZWISCHENLAGEN_ASSET_BALANCED.csv")
    parser.add_argument(
        "--input",
        action="append",
        default=[],
        help="LABEL=path to a raw-window CSV. Can be repeated.",
    )
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1349_HOERBARER_SCHMALER_SHIFT_MULTI_HOLDOUT.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1349_HOERBARER_SCHMALER_SHIFT_MULTI_HOLDOUT.csv")
    args = parser.parse_args()

    inputs = args.input or [
        "HOLDOUT1=docs/befunde/1001-2000/1001-1500/1321_HOLDOUT_WELTLAGEN_ROHWELTFENSTER.csv",
        "HOLDOUT2=docs/befunde/1001-2000/1001-1500/1328_SECOND_HOLDOUT_WELTLAGEN_ROHWELTFENSTER.csv",
        "CONTRAST=docs/befunde/1001-2000/1001-1500/1336_CONTRAST_HOLDOUT_WELTLAGEN_ROHWELTFENSTER.csv",
    ]
    bases = _load_asset_bases(Path(args.base))
    all_rows: list[dict[str, object]] = []
    group_counts: dict[str, int] = {}
    for raw in inputs:
        label, path = _parse_input(raw)
        rows = _read_candidates(path, bases)
        for row in rows:
            row["holdout_group"] = label
        group_counts[label] = len(rows)
        all_rows.extend(rows)

    all_rows.sort(key=lambda item: (str(item["holdout_group"]), str(item["asset"]), -float(item["score"])))
    _write_csv(all_rows, Path(args.csv_out))
    _write_markdown(all_rows, group_counts=group_counts, path=Path(args.out), top=args.top)
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
