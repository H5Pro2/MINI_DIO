from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


SYNTH_FEATURES = ("max_open", "max_rand", "max_raw_field", "max_reduction")
REAL_FEATURES = ("high_offen", "high_rand_kipp", "high_raw_field_intake", "high_intake_reduction")


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _nearest_synth(real: dict[str, str], synth_rows: list[dict[str, str]]) -> tuple[str, float]:
    best_name = "-"
    best_distance = float("inf")
    real_values = [_float(real, key) for key in REAL_FEATURES]
    for synth in synth_rows:
        synth_values = [_float(synth, key) for key in SYNTH_FEATURES]
        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(real_values, synth_values)))
        if distance < best_distance:
            best_distance = distance
            best_name = synth.get("world", "-") or "-"
    return best_name, best_distance


def _real_class(row: dict[str, str]) -> str:
    high_open = _float(row, "high_offen")
    high_rand = _float(row, "high_rand_kipp")
    center = _float(row, "zentrum")
    if high_open >= 0.75 and high_rand >= 0.15:
        return "reale_starke_rand_oeffnung"
    if high_open >= 0.75 and high_rand >= 0.08:
        return "reale_oeffnung_mit_randanteil"
    if center >= 0.65 and high_rand < 0.11:
        return "zentriert_mit_hochlast_oeffnung"
    if high_open >= 0.50:
        return "reale_oeffnung"
    return "reale_stabile_zentrierung"


def _build_rows(real_rows: list[dict[str, str]], synth_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    synth_rand = max(synth_rows, key=lambda row: _float(row, "max_rand"))
    synth_open = max(synth_rows, key=lambda row: _float(row, "max_open"))
    synth_max_rand = _float(synth_rand, "max_rand")
    synth_max_open = _float(synth_open, "max_open")
    for real in real_rows:
        nearest, distance = _nearest_synth(real, synth_rows)
        rows.append(
            {
                "world": real.get("world", "-"),
                "class": _real_class(real),
                "nearest_synth": nearest,
                "nearest_distance": round(distance, 6),
                "zentrum": round(_float(real, "zentrum"), 6),
                "offen": round(_float(real, "offen"), 6),
                "rand_kipp": round(_float(real, "rand_kipp"), 6),
                "high_offen": round(_float(real, "high_offen"), 6),
                "high_rand_kipp": round(_float(real, "high_rand_kipp"), 6),
                "high_raw_field_intake": round(_float(real, "high_raw_field_intake"), 6),
                "high_intake_reduction": round(_float(real, "high_intake_reduction"), 6),
                "high_auditory_loudness": round(_float(real, "high_auditory_loudness"), 6),
                "rand_over_synth_max": round(_float(real, "high_rand_kipp") - synth_max_rand, 6),
                "open_over_synth_max": round(_float(real, "high_offen") - synth_max_open, 6),
            }
        )
    return rows


def _write_csv(rows: list[dict[str, object]], csv_out: Path) -> None:
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], synth_rows: list[dict[str, str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    strongest_real_rand = max(rows, key=lambda row: float(row["high_rand_kipp"]))
    strongest_real_open = max(rows, key=lambda row: float(row["high_offen"]))
    most_centered = max(rows, key=lambda row: float(row["zentrum"]))
    synth_rand = max(synth_rows, key=lambda row: _float(row, "max_rand"))
    synth_open = max(synth_rows, key=lambda row: _float(row, "max_open"))

    lines: list[str] = [
        "# Reale Welten Gegen Synthetische Rezeptorklassen",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest reale Welt-Hochlastfenster gegen die synthetischen Rezeptorklassen.",
        "Sie prueft, ob reale Welten eher zentriert, offen oder randnah gelesen werden.",
        "",
        "Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.",
        "",
        "## Synthetische Referenz",
        "",
        "| Referenz | Max Offen | Max Rand/Kipp | Max Rohfeld | Max Reduktion | Klasse |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in synth_rows:
        lines.append(
            "| {world} | {max_open:.4f} | {max_rand:.4f} | {max_raw_field:.4f} | {max_reduction:.4f} | {world_class} |".format(
                world=row.get("world", "-"),
                max_open=_float(row, "max_open"),
                max_rand=_float(row, "max_rand"),
                max_raw_field=_float(row, "max_raw_field"),
                max_reduction=_float(row, "max_reduction"),
                world_class=row.get("world_class", "-"),
            )
        )
    lines.extend(
        [
            "",
            "## Reale Weltmatrix",
            "",
            "| Welt | Klasse | Naechste Synth-Klasse | Zentrum | Offen | Rand | High-Offen | High-Rand | High-Rohfeld | High-Reduktion | High-Lautheit | Rand ueber Synth-Max |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| {world} | {class} | {nearest_synth} | {zentrum:.4f} | {offen:.4f} | {rand_kipp:.4f} | {high_offen:.4f} | {high_rand_kipp:.4f} | {high_raw_field_intake:.4f} | {high_intake_reduction:.4f} | {high_auditory_loudness:.4f} | {rand_over_synth_max:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkstes reales Hochlast-Randfenster: `{strongest_real_rand['world']}` mit `{float(strongest_real_rand['high_rand_kipp']):.4f}`.",
            f"- Staerkste reale Hochlast-Oeffnung: `{strongest_real_open['world']}` mit `{float(strongest_real_open['high_offen']):.4f}`.",
            f"- Staerkste reale Gesamtzentrierung in dieser Gruppe: `{most_centered['world']}` mit `{float(most_centered['zentrum']):.4f}`.",
            f"- Staerkste synthetische Randreferenz: `{synth_rand.get('world', '-')}` mit `{_float(synth_rand, 'max_rand'):.4f}`.",
            f"- Staerkste synthetische Oeffnungsreferenz: `{synth_open.get('world', '-')}` mit `{_float(synth_open, 'max_open'):.4f}`.",
            "",
            "## Einordnung",
            "",
            "Die realen Hochlastfenster sind nicht schwaecher als die synthetischen Klassen. Besonders KAS zeigt deutlich mehr reale Rand/Kipp-Naehe als die bisherige synthetische Randdominanz.",
            "",
            "Damit ist die synthetische Randwelt kein Maximalstressmodell. Sie ist ein kontrolliertes Referenzmuster. Reale Welten koennen lokal staerker randnah werden, waehrend das Gesamtfeld trotzdem zentriert oder gemischt bleibt.",
            "",
            "Die Rezeptoradaptation wirkt auch hier nicht als Wegloeschen der Wirkung. Sie begrenzt Rohaufnahme, aber laesst Hochlastfenster als offene oder randnahe Innenfeldlagen sichtbar.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte KAS als reale Randreferenz phasenweise isoliert werden. Ziel ist zu verstehen, welche Weltabschnitte die starke reale Randnaehe erzeugen.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--synth", required=True)
    parser.add_argument("--real", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    args = parser.parse_args()

    synth_rows = _load(Path(args.synth))
    real_rows = _load(Path(args.real))
    rows = _build_rows(real_rows, synth_rows)
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, synth_rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
