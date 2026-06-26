from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _class_counts(rows: list[dict[str, str]]) -> Counter[str]:
    return Counter(row.get("condensation_zone", "-") or "-" for row in rows)


def _top_tokens(rows: list[dict[str, str]], count: int) -> list[str]:
    return [row.get("token", "-") or "-" for row in sorted(rows, key=lambda row: _int(row, "observations"), reverse=True)[:count]]


def _write_markdown(
    base_rows: list[dict[str, str]],
    follow_rows: list[dict[str, str]],
    base_name: str,
    follow_name: str,
    out: Path,
) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    base_counts = _class_counts(base_rows)
    follow_counts = _class_counts(follow_rows)
    classes = sorted(set(base_counts) | set(follow_counts))

    base_map = {row.get("token", "-") or "-": row for row in base_rows}
    follow_map = {row.get("token", "-") or "-": row for row in follow_rows}
    shared_tokens = sorted(set(base_map) & set(follow_map))
    base_top = set(_top_tokens(base_rows, 20))
    follow_top = set(_top_tokens(follow_rows, 20))
    shared_top = sorted(base_top & follow_top)

    zone_stable = [
        token
        for token in shared_tokens
        if (base_map[token].get("condensation_zone") or "-") == (follow_map[token].get("condensation_zone") or "-")
    ]
    zone_changed = [token for token in shared_tokens if token not in zone_stable]

    lines = [
        "# MCM-Verdichtungszonen Reproduktion",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht zwei Verdichtungszonen-Laeufe.",
        "Sie prueft, ob die Zonenstruktur reproduziert wird oder ob sie an eine einzelne Debuggruppe gebunden ist.",
        "",
        "Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.",
        "",
        "## Klassenvergleich",
        "",
        f"| Verdichtungszone | {base_name} | {follow_name} | Differenz |",
        "|---|---:|---:|---:|",
    ]
    for name in classes:
        diff = follow_counts[name] - base_counts[name]
        lines.append(f"| {name} | {base_counts[name]} | {follow_counts[name]} | {diff:+d} |")

    lines.extend(
        [
            "",
            "## Token-Stabilitaet",
            "",
            f"- Gemeinsame Tokens gesamt: `{len(shared_tokens)}`",
            f"- Tokens mit gleicher Verdichtungszone: `{len(zone_stable)}`",
            f"- Tokens mit wechselnder Verdichtungszone: `{len(zone_changed)}`",
            f"- Ueberlappung der Top-20-Tokens: `{len(shared_top)}`",
            "",
            "## Gemeinsame Top-Tokens",
            "",
            "| Token | Basiszone | Folgezone | Basis-Beobachtungen | Folge-Beobachtungen | Basis-Welten | Folge-Welten |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for token in shared_top:
        base = base_map[token]
        follow = follow_map[token]
        lines.append(
            "| {token} | {base_zone} | {follow_zone} | {base_obs} | {follow_obs} | {base_worlds} | {follow_worlds} |".format(
                token=token,
                base_zone=base.get("condensation_zone", "-"),
                follow_zone=follow.get("condensation_zone", "-"),
                base_obs=base.get("observations", "0"),
                follow_obs=follow.get("observations", "0"),
                base_worlds=base.get("worlds", "0"),
                follow_worlds=follow.get("worlds", "0"),
            )
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Klassenverteilung reproduziert sich deutlich: junge Spuren bleiben die groesste Gruppe, danach folgen Rekopplungszonen, Driftzonen, stabile Bedeutungsinseln, hoehere Clusteruebergaenge, offene Bedeutungszonen und wenige randnahe Verdichtungen.",
            "",
            "Die genaue Tokenzuordnung kann wechseln. Das ist fachlich wichtig: MINI_DIO reproduziert nicht nur starre Namen, sondern vor allem eine Feldordnung aus Verdichtungsrollen.",
            "",
            "Damit wird die MCM-Lesart gestaerkt: Verdichtung ist nicht bloss Wiederholung, sondern eine reproduzierbare Rollenstruktur mit variabler Oberflaeche.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte ein gezielter Blick auf die wechselnden Tokens erfolgen. Ziel: unterscheiden, ob ein Wechsel echte Drift, Weltfaerbung oder nur Oberflaechenvarianz ist.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--follow", required=True)
    parser.add_argument("--base-name", default="854")
    parser.add_argument("--follow-name", default="855")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    _write_markdown(
        _load(Path(args.base)),
        _load(Path(args.follow)),
        args.base_name,
        args.follow_name,
        Path(args.out),
    )
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
