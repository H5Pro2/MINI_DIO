from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
INPUT = befunde_root(ROOT) / "1358_HOERBARER_SCHMALER_SHIFT_ERWEITERTE_ROLLELESUNG.csv"
OUT_CSV = befunde_root(ROOT) / "1379_FELDFUNKTIONSKARTE_WELTVERTEILUNG.csv"
OUT_MD = befunde_root(ROOT) / "1379_FELDFUNKTIONSKARTE_WELTVERTEILUNG.md"

PRIMARY_ROLES = {
    "brueckenuebergang_zum_lauten_kontakt": "Bruecke",
    "zentrumskontakt_mit_hoeranstieg": "Zentrumskontakt",
    "zentrumskontakt_wird_aktiviert": "Zentrumskontakt",
    "randnaher_kontaktdruck": "Randdruck",
}


def _read_rows() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(rows: list[dict[str, str]]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "field_function",
                "role",
                "asset",
                "world",
                "count",
                "sequences",
                "raw_classes",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def build_report() -> None:
    rows = _read_rows()
    selected = [row for row in rows if row.get("phase_role") in PRIMARY_ROLES]

    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in selected:
        function = PRIMARY_ROLES[row["phase_role"]]
        grouped[(function, row["phase_role"], row["asset"], row["world"])].append(row)

    out_rows: list[dict[str, str]] = []
    for (function, role, asset, world), items in sorted(grouped.items()):
        sequences = Counter(row.get("base_sequence", "") for row in items)
        raw_classes = Counter(row.get("during_raw_class", "") for row in items)
        out_rows.append(
            {
                "field_function": function,
                "role": role,
                "asset": asset,
                "world": world,
                "count": str(len(items)),
                "sequences": "; ".join(f"{key}:{value}" for key, value in sequences.most_common()),
                "raw_classes": "; ".join(f"{key}:{value}" for key, value in raw_classes.most_common()),
            }
        )
    _write_csv(out_rows)

    function_counts = Counter(PRIMARY_ROLES[row["phase_role"]] for row in selected)
    function_assets: dict[str, Counter[str]] = defaultdict(Counter)
    function_worlds: dict[str, Counter[str]] = defaultdict(Counter)
    function_sequences: dict[str, Counter[str]] = defaultdict(Counter)
    for row in selected:
        function = PRIMARY_ROLES[row["phase_role"]]
        function_assets[function][row.get("asset", "")] += 1
        function_worlds[function][row.get("world", "")] += 1
        function_sequences[function][row.get("base_sequence", "")] += 1

    lines = [
        "# 1379 - Feldfunktionskarte: Weltverteilung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die passive Feldfunktionskarte aus `1378` gegen die vorhandenen erweiterten Weltfenster.",
        "",
        "Geprueft wird:",
        "",
        "```text",
        "Sind Bruecke, Zentrumskontakt und Randdruck nur lokale Einzelbefunde,",
        "oder treten sie ueber mehrere Welten/Assets verteilt auf?",
        "```",
        "",
        "Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Strategie.",
        "",
        "## Uebersicht",
        "",
        f"- gelesene Rollenfenster gesamt: `{len(rows)}`",
        f"- Feldfunktionsfenster: `{len(selected)}`",
        "",
    ]
    for function in ["Bruecke", "Zentrumskontakt", "Randdruck"]:
        lines.extend(
            [
                f"## {function}",
                "",
                f"- Fenster: `{function_counts.get(function, 0)}`",
                f"- Assets: {sorted(function_assets[function].items())}",
                f"- Welten: {sorted(function_worlds[function].items())}",
                f"- Lagefolgen: {sorted(function_sequences[function].items())}",
                "",
            ]
        )

    lines.extend(
        [
            "## Lesung",
            "",
            "Die drei Feldfunktionen verteilen sich unterschiedlich:",
            "",
            "- Bruecke liegt asset- und weltuebergreifend vor.",
            "- Zentrumskontakt liegt aktuell konzentrierter, aber nicht nur in einer einzelnen Welt.",
            "- Randdruck liegt stark in BTC-nahen lauten Kontaktfolgen und erscheint zusaetzlich in einzelnen SOL/PAXG-Fenstern.",
            "",
            "Damit wirkt die Karte nicht wie eine reine Einzelwelt-Artefaktliste. Gleichzeitig ist die Verteilung noch ungleichgewichtig.",
            "",
            "## Grenze",
            "",
            "Der Befund ist ein Indiz, kein Beweis.",
            "",
            "Besonders Randdruck ist derzeit stark BTC-lastig. Zentrumskontakt ist staerker auf DOGE/XRP/SOL verteilt. Das muss gegen weitere Welten geprueft werden.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
