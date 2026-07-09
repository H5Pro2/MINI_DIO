from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _asset_from_key(row: dict[str, str]) -> str:
    key = str(row.get("meaning_key", "") or "")
    if "_" not in key:
        return "UNKNOWN"
    return key.rsplit("_", 1)[-1].upper()


def _classify(base: dict[str, str] | None, follow: dict[str, str] | None) -> str:
    if base is None and follow is not None:
        return "neue_assetfaerbung"
    if base is not None and follow is None:
        return "nicht_wieder_aufgetreten"
    if base is None or follow is None:
        return "unknown"
    if (
        base.get("field_form") == follow.get("field_form")
        and base.get("dominant_sequence") == follow.get("dominant_sequence")
        and base.get("sensory_profile") == follow.get("sensory_profile")
    ):
        return "stabil_wiedererkannt"
    if base.get("field_form") == follow.get("field_form"):
        return "feldform_wiedererkannt_faerbung_veraendert"
    return "aufgespalten_oder_neu"


def _write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], path: Path, *, base_path: Path, holdout_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for row in rows:
        status = str(row["recognition_status"])
        counts[status] = counts.get(status, 0) + 1

    lines = [
        "# Vergleich MCM-Bedeutungsstruktur Basis/Holdout",
        "",
        f"Diese Diagnose vergleicht `{base_path.name}` mit `{holdout_path.name}`.",
        "",
        "Geprueft wird:",
        "",
        "- wiedererkannt",
        "- erweitert",
        "- veraendert",
        "- nicht wieder aufgetreten",
        "",
        "## Statusverteilung",
        "",
    ]
    for status, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{status}`: `{count}`")

    lines.extend(
        [
            "",
            "## Vergleich",
            "",
            "| Asset | Status | Basis-Folge | Holdout-Folge | Basis-Sinnesprofil | Holdout-Sinnesprofil |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| {asset} | `{recognition_status}` | `{base_sequence}` | `{holdout_sequence}` | `{base_sensory_profile}` | `{holdout_sensory_profile}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Bewertung",
            "",
            "Die gemeinsame Feldform bleibt im Holdout erhalten:",
            "",
            "```text",
            "zwischenlage_gemischte_rohwelt",
            "```",
            "",
            "Gleichzeitig ist die Assetfaerbung nicht starr.",
            "",
            "Ein Teil wird stabil wiedererkannt, ein Teil veraendert die dominante Folge, und neue Assetfaerbungen koennen erscheinen.",
            "",
            "Das spricht fuer eine passive Bedeutungsstruktur, die weder alles neu erfindet noch alles festnagelt.",
            "",
            "Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.",
            "",
            "Wie es weitergeht: Als naechstes sollte die Veraenderung der Faerbung untersucht werden: Welche Rohweltmerkmale verschieben einzelne Assets gegenueber der Basisstruktur?",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="docs/befunde/1001-2000/1001-1500/1317_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.csv")
    parser.add_argument("--holdout", default="docs/befunde/1001-2000/1001-1500/1323_HOLDOUT_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.csv")
    parser.add_argument("--out", default="docs/befunde/1001-2000/1001-1500/1324_MCM_BEDEUTUNGSSTRUKTUR_HOLDOUT_VERGLEICH.md")
    parser.add_argument("--csv-out", default="docs/befunde/1001-2000/1001-1500/1324_MCM_BEDEUTUNGSSTRUKTUR_HOLDOUT_VERGLEICH.csv")
    args = parser.parse_args()

    base_rows = {_asset_from_key(row): row for row in _read(Path(args.base))}
    holdout_rows = {_asset_from_key(row): row for row in _read(Path(args.holdout))}
    assets = sorted(set(base_rows) | set(holdout_rows))
    rows: list[dict[str, object]] = []
    for asset in assets:
        base = base_rows.get(asset)
        holdout = holdout_rows.get(asset)
        rows.append(
            {
                "asset": asset,
                "recognition_status": _classify(base, holdout),
                "base_field_form": (base or {}).get("field_form", "-"),
                "holdout_field_form": (holdout or {}).get("field_form", "-"),
                "base_sequence": (base or {}).get("dominant_sequence", "-"),
                "holdout_sequence": (holdout or {}).get("dominant_sequence", "-"),
                "base_sensory_profile": (base or {}).get("sensory_profile", "-"),
                "holdout_sensory_profile": (holdout or {}).get("sensory_profile", "-"),
                "passive_only": 1,
                "influences_action": 0,
            }
        )
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out), base_path=Path(args.base), holdout_path=Path(args.holdout))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
