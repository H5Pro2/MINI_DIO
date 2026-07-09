from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _quantile(values: list[float], fraction: float) -> float:
    clean = sorted(value for value in values if value == value)
    if not clean:
        return 0.0
    idx = min(len(clean) - 1, max(0, int(round((len(clean) - 1) * fraction))))
    return clean[idx]


def _classify(row: dict[str, str], medians: dict[str, float]) -> tuple[str, dict[str, float]]:
    range_delta = abs(_float(row.get("follow_raw_range_pct")) - _float(row.get("pre_raw_range_pct")))
    hearing_delta = abs(_float(row.get("follow_hearing_gap")) - _float(row.get("pre_hearing_gap")))
    tension_delta = abs(_float(row.get("follow_mcm_tension")) - _float(row.get("pre_mcm_tension")))
    follow_hearing = _float(row.get("follow_hearing_gap"))
    follow_tension = _float(row.get("follow_mcm_tension"))

    values = {
        "range_delta": range_delta,
        "hearing_delta": hearing_delta,
        "tension_delta": tension_delta,
        "follow_hearing": follow_hearing,
        "follow_tension": follow_tension,
    }
    if (
        range_delta <= medians["range_delta"]
        and hearing_delta <= medians["hearing_delta"]
        and tension_delta <= medians["tension_delta"]
    ):
        return "milieu_umlagert_nahe", values
    if hearing_delta >= range_delta and hearing_delta >= tension_delta:
        if follow_hearing >= medians["follow_hearing"]:
            return "hoerprofil_springt_hoch", values
        return "hoerprofil_entlastet", values
    if tension_delta >= range_delta and tension_delta >= hearing_delta:
        if follow_tension >= medians["follow_tension"]:
            return "feldspannung_springt_hoch", values
        return "feldspannung_entlastet", values
    return "rangegetriebene_umgebung", values


def _write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    csv_path = out_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _fmt(value, 6) if isinstance(value, float) else value for key, value in row.items()})


def _write_md(rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(rows, out_path)
    title_prefix = out_path.stem.split("_", 1)[0]
    title = f"# {title_prefix} - Lupenprofile der Drittperioden-Treffer" if title_prefix.isdigit() else "# Lupenprofile der Drittperioden-Treffer"
    counts = Counter(str(row["profile"]) for row in rows)
    by_profile: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_profile[str(row["profile"])].append(row)

    lines = [
        title,
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose gruppiert die Rohwelt-Lupe aus 1696 in relative Arbeitsprofile.",
        "Die Gruppen entstehen aus dem jeweiligen Datensatz selbst und sind keine festen Regeln.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Welche Typen von Vorfenster-zu-Folgephase-Bewegung liegen unter den Treffern?",
        "2. Unterpruefung: Range, Hoeren-Gap und Feldspannung relativ zueinander gruppieren.",
        "3. Folgeschritt: Die Profile gegen weitere Assetfenster testen.",
        "",
        "## Profilzaehlung",
        "",
        "| Profil | Anzahl |",
        "|---|---:|",
    ]
    for profile, count in sorted(counts.items()):
        lines.append(f"| {profile} | {count} |")

    lines.extend(["", "## Beispiele", ""])
    for profile, items in sorted(by_profile.items()):
        lines.extend([f"### {profile}", "", "| Familie | Wechsel | Welt | Range-Delta | Hoeren-Delta | Spannungs-Delta |", "|---|---|---|---:|---:|---:|"])
        for row in sorted(items, key=lambda item: str(item["family"]))[:8]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["family"]),
                        str(row["transition"]),
                        str(row["world"]),
                        _fmt(float(row["range_delta"])),
                        _fmt(float(row["hearing_delta"])),
                        _fmt(float(row["tension_delta"])),
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.extend(
        [
            "## Lesung",
            "",
            "`milieu_umlagert_nahe` ist der interessanteste passive Kandidat: Familie und Wechselrichtung wiederholen sich, waehrend Vorfenster und Folgephase in Hoeren und Spannung nahe bleiben.",
            "",
            "Hoer-, Spannungs- und Rangeprofile zeigen dagegen eher, dass eine erkennbare Weltveraenderung am Wechsel beteiligt ist.",
            "",
            "Das trennt zwei Arbeitsfragen:",
            "",
            "```text",
            "Milieu-Umlagerung: aehnliche Welt-/Feldlage, andere Milieuschicht.",
            "Weltgetriebener Wechsel: veraenderte Range, Hoeren oder Feldspannung faerbt die Familie um.",
            "```",
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Gruppiert 1696-Lupentreffer in relative Rohweltprofile.")
    parser.add_argument("--loupe-csv", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    rows = _load_csv(_resolve(args.loupe_csv))
    deltas = {
        "range_delta": [abs(_float(row.get("follow_raw_range_pct")) - _float(row.get("pre_raw_range_pct"))) for row in rows],
        "hearing_delta": [abs(_float(row.get("follow_hearing_gap")) - _float(row.get("pre_hearing_gap"))) for row in rows],
        "tension_delta": [abs(_float(row.get("follow_mcm_tension")) - _float(row.get("pre_mcm_tension"))) for row in rows],
        "follow_hearing": [_float(row.get("follow_hearing_gap")) for row in rows],
        "follow_tension": [_float(row.get("follow_mcm_tension")) for row in rows],
    }
    medians = {key: _quantile(value, 0.50) for key, value in deltas.items()}
    out: list[dict[str, object]] = []
    for row in rows:
        profile, values = _classify(row, medians)
        out.append(
            {
                "family": row.get("family", "-"),
                "transition": row.get("transition", "-"),
                "world": row.get("world", "-"),
                "profile": profile,
                **values,
            }
        )
    _write_md(out, _resolve(args.out_md))
    print({"out_md": str(_resolve(args.out_md)), "rows": len(out), "profiles": dict(Counter(str(row["profile"]) for row in out))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
