from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _float(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _weighted(rows: list[dict[str, str]], key: str) -> float:
    total = sum(max(0.0, _float(row, "episodes")) for row in rows)
    if total <= 0.0:
        return 0.0
    return sum(_float(row, key) * max(0.0, _float(row, "episodes")) for row in rows) / total


def _max_row(rows: list[dict[str, str]], key: str) -> dict[str, str]:
    return max(rows, key=lambda row: _float(row, key))


def _world_class(summary: dict[str, object]) -> str:
    max_open = float(summary["max_open"])
    max_rand = float(summary["max_rand"])
    avg_center = float(summary["avg_center"])
    if max_open >= 0.60 and max_rand >= 0.02:
        return "lokale_rand_oeffnung"
    if max_open >= 0.35:
        return "lokale_oeffnung_ohne_rand"
    if avg_center >= 0.94 and max_open < 0.05:
        return "stabile_zentrierung"
    return "gemischte_aufnahme"


def _summarize(label: str, path: Path) -> dict[str, object]:
    rows = _load(path)
    open_row = _max_row(rows, "offen")
    rand_row = _max_row(rows, "rand_kipp")
    loud_row = _max_row(rows, "auditory_loudness")
    reduction_row = _max_row(rows, "intake_reduction")
    raw_row = _max_row(rows, "raw_field_intake")
    blur_row = _max_row(rows, "visual_blur")
    summary: dict[str, object] = {
        "world": label,
        "phases": len(rows),
        "episodes": int(sum(_float(row, "episodes") for row in rows)),
        "avg_center": round(_weighted(rows, "zentrum"), 6),
        "avg_open": round(_weighted(rows, "offen"), 6),
        "avg_rand": round(_weighted(rows, "rand_kipp"), 6),
        "avg_raw_field": round(_weighted(rows, "raw_field_intake"), 6),
        "avg_adapted_field": round(_weighted(rows, "adapted_field_intake"), 6),
        "avg_reduction": round(_weighted(rows, "intake_reduction"), 6),
        "avg_ratio": round(_weighted(rows, "adaptation_ratio"), 6),
        "max_open_phase": open_row.get("phase", "-"),
        "max_open": round(_float(open_row, "offen"), 6),
        "max_open_center": round(_float(open_row, "zentrum"), 6),
        "max_open_rand": round(_float(open_row, "rand_kipp"), 6),
        "max_rand_phase": rand_row.get("phase", "-"),
        "max_rand": round(_float(rand_row, "rand_kipp"), 6),
        "max_rand_open": round(_float(rand_row, "offen"), 6),
        "max_loud_phase": loud_row.get("phase", "-"),
        "max_loudness": round(_float(loud_row, "auditory_loudness"), 6),
        "max_raw_phase": raw_row.get("phase", "-"),
        "max_raw_field": round(_float(raw_row, "raw_field_intake"), 6),
        "max_reduction_phase": reduction_row.get("phase", "-"),
        "max_reduction": round(_float(reduction_row, "intake_reduction"), 6),
        "lowest_ratio": round(min(_float(row, "adaptation_ratio") for row in rows), 6),
        "max_blur_phase": blur_row.get("phase", "-"),
        "max_visual_blur": round(_float(blur_row, "visual_blur"), 6),
    }
    summary["world_class"] = _world_class(summary)
    return summary


def _write_csv(rows: list[dict[str, object]], csv_out: Path) -> None:
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    strongest_open = max(rows, key=lambda row: float(row["max_open"]))
    strongest_rand = max(rows, key=lambda row: float(row["max_rand"]))
    strongest_reduction = max(rows, key=lambda row: float(row["max_reduction"]))
    most_centered = max(rows, key=lambda row: float(row["avg_center"]))

    lines: list[str] = [
        "# Synthetische Rezeptor-Limit-Synthese",
        "",
        "## Zweck",
        "",
        "Diese Synthese fuehrt die phasenweisen Rezeptor-Limitdiagnosen zusammen.",
        "Sie prueft, welche synthetische Weltform zentriert bleibt, welche nur oeffnet und welche lokal in Rand/Kippnaehe kommt.",
        "",
        "Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.",
        "",
        "## Vergleichsmatrix",
        "",
        "| Welt | Klasse | Episoden | Zentrum avg | Offen avg | Rand avg | Max Offen | Offen-Phase | Max Rand | Rand-Phase | Max Rohfeld | Max Reduktion | niedrigste Ratio | max Blur |",
        "|---|---|---:|---:|---:|---:|---:|---|---:|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {world} | {world_class} | {episodes} | {avg_center:.4f} | {avg_open:.4f} | {avg_rand:.4f} | {max_open:.4f} | {max_open_phase} | {max_rand:.4f} | {max_rand_phase} | {max_raw_field:.4f} | {max_reduction:.4f} | {lowest_ratio:.4f} | {max_visual_blur:.4f} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"- Staerkste lokale Oeffnung: `{strongest_open['world']}` / `{strongest_open['max_open_phase']}` mit `{float(strongest_open['max_open']):.4f}`.",
            f"- Staerkste lokale Rand/Kipp-Naehe: `{strongest_rand['world']}` / `{strongest_rand['max_rand_phase']}` mit `{float(strongest_rand['max_rand']):.4f}`.",
            f"- Staerkste rezeptorische Reduktion: `{strongest_reduction['world']}` / `{strongest_reduction['max_reduction_phase']}` mit `{float(strongest_reduction['max_reduction']):.4f}`.",
            f"- Staerkste durchschnittliche Zentrierung: `{most_centered['world']}` mit `{float(most_centered['avg_center']):.4f}`.",
            "",
            "## Einordnung",
            "",
            "Die drei synthetischen Weltformen fallen nicht in dieselbe Feldreaktion:",
            "",
            "- Harmonie bleibt global und lokal stark zentriert.",
            "- Bruch/Rand erzeugt eine lokale Oeffnung, aber kaum Rand/Kippnaehe.",
            "- Randdominanz erzeugt eine lokale Oeffnung mit zusaetzlicher Rand/Kippnaehe.",
            "",
            "Damit trennt MINI_DIO nach aktuellem Befund mindestens drei rezeptorisch vermittelte Innenfeldlagen:",
            "",
            "```text",
            "zentriert",
            "offen ohne Randkippung",
            "offen mit Rand/Kippnaehe",
            "```",
            "",
            "Die Rezeptoradaptation wirkt in allen drei Welten als Aufnahmegrenze. Sie verhindert keine Weltwirkung, sondern verhindert, dass Rohspannung ungeordnet als globale Feldueberlastung erscheint.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Synthese gegen reale Welten gelesen werden: KAS als gemischte reale Welt, PAXG als zentrierte reale Welt und DOGE/XRP als zentrierte, aber lautere reale Welten.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_input(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("input must be LABEL=PATH")
    label, path = value.split("=", 1)
    return label, Path(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, type=_parse_input)
    parser.add_argument("--out", required=True)
    parser.add_argument("--csv-out", required=True)
    args = parser.parse_args()

    rows = [_summarize(label, path) for label, path in args.input]
    _write_csv(rows, Path(args.csv_out))
    _write_markdown(rows, Path(args.out))
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
