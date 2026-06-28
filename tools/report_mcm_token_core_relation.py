from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _find_path(paths: list[dict[str, str]], token: str) -> dict[str, str]:
    return next((row for row in paths if row.get("token") == token), {})


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(
    path: Path,
    token: str,
    core_tokens: list[str],
    path_rows: list[dict[str, str]],
    relation_rows: list[dict[str, str]],
    neighbor_pairs: Counter[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    token_path = _find_path(path_rows, token)
    core_path_rows = [_find_path(path_rows, core) for core in core_tokens]
    bridge_neighbors = [
        row
        for row in relation_rows
        if row.get("neighbor_path_class") == "brueckenpfad"
    ]
    direct_core = [
        row
        for row in relation_rows
        if row.get("neighbor_token") in set(core_tokens)
    ]

    lines: list[str] = []
    lines.append(f"# MCM-Token Kernrelation: {_short(token)}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose legt einen isolierten Token gegen den zentralen Brueckenkern und prueft, ob er Gegenbereich, paralleler Driftpol oder Seitenphase im selben Topologieraum ist."
    )
    lines.append("")
    lines.append("## Zieltoken")
    lines.append("")
    lines.append("| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(
        f"| `{_short(token)}` | {token_path.get('path_class', '-')} | {token_path.get('movement', '-')} | {token_path.get('base_zone', '-')} | {token_path.get('follow_zone', '-')} | {token_path.get('base_role', '-')} -> {token_path.get('follow_role', '-')} |"
    )
    lines.append("")
    lines.append("## Zentraler Brueckenkern")
    lines.append("")
    lines.append("| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |")
    lines.append("|---|---|---|---|---|---|")
    for row in core_path_rows:
        lines.append(
            f"| `{_short(row.get('token', '-'))}` | {row.get('path_class', '-')} | {row.get('movement', '-')} | {row.get('base_zone', '-')} | {row.get('follow_zone', '-')} | {row.get('base_role', '-')} -> {row.get('follow_role', '-')} |"
        )
    lines.append("")
    lines.append("## Direkte Kopplung")
    lines.append("")
    if direct_core:
        lines.append("Direkte Nachbarschaft zum zentralen Kern ist sichtbar:")
        for row in direct_core:
            lines.append(f"- `{row['relation']}` mit `{_short(row['neighbor_token'])}`: `{row['count']}` Kontakte")
    else:
        lines.append("Keine direkte Nachbarschaft zum zentralen Kern sichtbar.")
    lines.append("")
    lines.append("## Staerkste Nachbarpaare")
    lines.append("")
    lines.append("| Paar | Kontakte |")
    lines.append("|---|---:|")
    for pair, count in neighbor_pairs.most_common(12):
        lines.append(f"| `{pair}` | {count} |")
    lines.append("")
    lines.append("## Brueckennahe Kopplung")
    lines.append("")
    if bridge_neighbors:
        lines.append("| Relation | Nachbar | Klasse | Bewegung | Kontakte |")
        lines.append("|---|---|---|---|---:|")
        for row in bridge_neighbors:
            lines.append(
                f"| {row['relation']} | `{_short(row['neighbor_token'])}` | {row['neighbor_path_class']} | {row['neighbor_movement']} | {row['count']} |"
            )
    else:
        lines.append("Keine brueckennahe Kopplung sichtbar.")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    if not direct_core and bridge_neighbors:
        lines.append("Der Token ist kein direkter Gegenpol des zentralen Brueckenkerns.")
        lines.append("Er koppelt indirekt ueber andere Brueckenpfade, besonders ueber brueckennahe Nachbarn.")
        lines.append("")
        lines.append("Damit wirkt er eher wie eine lange Seitenphase im selben Topologieraum als wie ein separater Gegenbereich.")
    elif direct_core:
        lines.append("Der Token besitzt direkte Kopplung an den zentralen Kern und sollte als moeglicher Seitenarm oder Gegenbereich weiter geprueft werden.")
    else:
        lines.append("Der Token wirkt isoliert gegenueber dem zentralen Kern.")
    lines.append("")
    lines.append("Wichtig:")
    lines.append("")
    lines.append("Wenn ein Token von `brueckenpfad` zu `offener_driftpfad` wechselt, kann das eine Feldoeffnung aus einer Brueckenlage heraus bedeuten.")
    lines.append("Das ist fachlich anders als chaotischer Rand: es ist eher eine gehaltene Eigenphase, die aus dem Uebergangsraum heraus driftet.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte der wichtigste Vermittler `0b7nep9` isoliert werden. Ziel: pruefen, ob er der eigentliche Anschluss zwischen Brueckenkern und Drift-Eigenphase ist.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", type=Path, required=True)
    parser.add_argument("--details", type=Path, required=True)
    parser.add_argument("--token", required=True)
    parser.add_argument("--core-token", action="append", default=[])
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path, required=True)
    args = parser.parse_args()

    paths = _read(args.paths)
    details = [row for row in _read(args.details) if row.get("token") == args.token]
    path_by_token = {row.get("token"): row for row in paths}
    core_set = set(args.core_token)

    counter: Counter[tuple[str, str]] = Counter()
    pair_counter: Counter[str] = Counter()
    for row in details:
        prev_token = row.get("prev_token", "-")
        next_token = row.get("next_token", "-")
        pair_counter[f"{_short(prev_token)} -> {_short(next_token)}"] += 1
        if prev_token != args.token and prev_token != "-":
            counter[("entry", prev_token)] += 1
        if next_token != args.token and next_token != "-":
            counter[("exit", next_token)] += 1

    out_rows: list[dict[str, str]] = []
    for (relation, neighbor_token), count in counter.most_common():
        neighbor_path = path_by_token.get(neighbor_token, {})
        out_rows.append(
            {
                "token": args.token,
                "relation": relation,
                "neighbor_token": neighbor_token,
                "count": str(count),
                "is_core_token": "1" if neighbor_token in core_set else "0",
                "neighbor_path_class": neighbor_path.get("path_class", "-"),
                "neighbor_movement": neighbor_path.get("movement", "-"),
                "neighbor_base_zone": neighbor_path.get("base_zone", "-"),
                "neighbor_follow_zone": neighbor_path.get("follow_zone", "-"),
                "neighbor_base_role": neighbor_path.get("base_role", "-"),
                "neighbor_follow_role": neighbor_path.get("follow_role", "-"),
            }
        )

    _write_csv(args.out_csv, out_rows)
    _write_md(args.out_md, args.token, args.core_token, paths, out_rows, pair_counter)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
