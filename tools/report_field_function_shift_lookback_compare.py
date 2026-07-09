from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _key(row: dict[str, str]) -> tuple[str, str]:
    return str(row.get("target_group", "-")), str(row.get("chain", "-"))


def _load_labeled(raw_items: list[str]) -> dict[str, dict[tuple[str, str], dict[str, str]]]:
    data: dict[str, dict[tuple[str, str], dict[str, str]]] = {}
    for raw in raw_items:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Input-Format: {raw}")
        label, path = raw.split("=", 1)
        rows = _load_csv(Path(path))
        data[label] = {_key(row): row for row in rows}
    return data


def _diff(data: dict[str, dict[tuple[str, str], dict[str, str]]], base_label: str, target_label: str, key: tuple[str, str], field: str) -> float:
    return _safe_float(data[target_label][key].get(field)) - _safe_float(data[base_label][key].get(field))


def _build_rows(data: dict[str, dict[tuple[str, str], dict[str, str]]], labels: list[str]) -> list[dict[str, object]]:
    common = sorted(set.intersection(*(set(rows) for rows in data.values())))
    base_label = labels[0]
    last_label = labels[-1]
    rows: list[dict[str, object]] = []
    for key in common:
        target_group, chain = key
        row: dict[str, object] = {
            "target_group": target_group,
            "chain": chain,
        }
        for label in labels:
            source = data[label][key]
            for field in (
                "events",
                "avg_raw_range_pct",
                "avg_raw_direction_changes",
                "avg_visual_stability",
                "avg_visual_change",
                "avg_hearing_tone",
                "avg_hearing_shift_abs",
                "avg_mcm_carry",
                "avg_mcm_strain",
                "avg_mcm_rekopplung",
            ):
                row[f"{label}_{field}"] = source.get(field, "0")
        row["range_growth"] = _diff(data, base_label, last_label, key, "avg_raw_range_pct")
        row["direction_change_growth"] = _diff(data, base_label, last_label, key, "avg_raw_direction_changes")
        row["mcm_carry_delta"] = _diff(data, base_label, last_label, key, "avg_mcm_carry")
        row["mcm_strain_delta"] = _diff(data, base_label, last_label, key, "avg_mcm_strain")
        row["mcm_rekopplung_delta"] = _diff(data, base_label, last_label, key, "avg_mcm_rekopplung")
        rows.append(row)
    rows.sort(key=lambda item: (str(item["target_group"]), str(item["chain"])))
    return rows


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["target_group"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(path: Path, rows: list[dict[str, object]], labels: list[str]) -> None:
    base_label = labels[0]
    last_label = labels[-1]
    lines = [
        "# 2037 - Feldfunktionswechsel Lookback-Vergleich",
        "",
        "## Zweck",
        "",
        "Dieser Bericht vergleicht die Rohweltfenster-Lupe mit mehreren Lookback-Längen.",
        "",
        "Geprüft wird, ob Öffnung und Rekopplung nur direkt am Signaturmoment sichtbar sind oder bereits in einem längeren Weltfenster unterscheidbare Profile tragen.",
        "",
        "## Eingaben",
        "",
    ]
    for label in labels:
        lines.append(f"- `{label}`")

    lines.extend(
        [
            "",
            "## Vergleich",
            "",
            "| Gruppe | Kette | Range 48/96/144 | Wechsel 48/96/144 | MCM 48 | MCM 144 | Wachstum Range/Wechsel | MCM-Delta |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        range_path = " / ".join(f"{_safe_float(row.get(label + '_avg_raw_range_pct')):.3f}" for label in labels)
        change_path = " / ".join(f"{_safe_float(row.get(label + '_avg_raw_direction_changes')):.2f}" for label in labels)
        mcm_base = (
            f"{_safe_float(row.get(base_label + '_avg_mcm_carry')):.3f}/"
            f"{_safe_float(row.get(base_label + '_avg_mcm_strain')):.3f}/"
            f"{_safe_float(row.get(base_label + '_avg_mcm_rekopplung')):.3f}"
        )
        mcm_last = (
            f"{_safe_float(row.get(last_label + '_avg_mcm_carry')):.3f}/"
            f"{_safe_float(row.get(last_label + '_avg_mcm_strain')):.3f}/"
            f"{_safe_float(row.get(last_label + '_avg_mcm_rekopplung')):.3f}"
        )
        mcm_delta = (
            f"{float(row['mcm_carry_delta']):.3f}/"
            f"{float(row['mcm_strain_delta']):.3f}/"
            f"{float(row['mcm_rekopplung_delta']):.3f}"
        )
        lines.append(
            "| "
            f"`{row['target_group']}` | "
            f"`{row['chain']}` | "
            f"{range_path} | "
            f"{change_path} | "
            f"{mcm_base} | "
            f"{mcm_last} | "
            f"{float(row['range_growth']):.3f}/{float(row['direction_change_growth']):.2f} | "
            f"{mcm_delta} |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Rohwelt wird mit längerem Lookback erwartbar breiter: Range und Richtungswechsel steigen deutlich.",
            "",
            "Die MCM-Werte der Gruppen bleiben dagegen praktisch stabil, weil sie am Signaturmoment gemessen werden. Damit sind Öffnung und Rekopplung nicht nur Ergebnis eines beliebig längeren Fensters, sondern an konkrete Feldzustände am Kontaktpunkt gebunden.",
            "",
            "Wichtig ist die Trennung:",
            "",
            "- längerer Lookback zeigt mehr Vorgeschichte und Weltunruhe",
            "- der eigentliche Rollenwechsel bleibt im MCM-Profil unterscheidbar",
            "",
            "## Lesung für DIO",
            "",
            "DIO braucht keine harte Vorhersage aus langer Historie.",
            "",
            "Sinnvoller ist eine zweistufige Feldlesung: Vorgeschichte als Weltphase lesen, den Rollenwechsel aber am aktuellen Feldkontakt prüfen.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, help="Format: label=path")
    parser.add_argument("--out-prefix", default="2037_FELDFUNKTIONSWECHSEL_LOOKBACK_VERGLEICH")
    args = parser.parse_args()

    labels = [raw.split("=", 1)[0].strip() for raw in args.input]
    data = _load_labeled(args.input)
    rows = _build_rows(data, labels)

    out_dir = Path("docs") / "befunde"
    _write_csv(out_dir / f"{args.out_prefix}.csv", rows)
    _write_markdown(out_dir / f"{args.out_prefix}.md", rows, labels)

    print(f"rows={len(rows)}")
    print(f"wrote={out_dir / (args.out_prefix + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
