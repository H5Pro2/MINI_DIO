from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _int(value: str) -> int:
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


def _float(value: str) -> float:
    try:
        return float(value or 0.0)
    except ValueError:
        return 0.0


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _path(paths: dict[str, dict[str, str]], token: str) -> dict[str, str]:
    return paths.get(token, {})


def _anchor_class(edge_rows: list[dict[str, str]], core_rows: list[dict[str, str]], token: str) -> str:
    in_core_pair = any(row.get("token_a") == token or row.get("token_b") == token for row in core_rows)
    edge_count = sum(_int(row.get("count", "0")) for row in edge_rows)
    edge_kinds = Counter(row.get("edge_kind", "-") for row in edge_rows)
    bridge_to_bridge = edge_kinds.get("bruecke_zu_bruecke", 0)
    outside_bridge = edge_kinds.get("aussen_zu_bruecke", 0) + edge_kinds.get("bruecke_zu_aussen", 0)
    world_span = max((_int(row.get("worlds", "0")) for row in edge_rows), default=0)
    if in_core_pair:
        return "brueckenkern"
    if edge_count >= 20 and outside_bridge >= 2 and world_span >= 2 and bridge_to_bridge == 0:
        return "starker_anschlussanker"
    if edge_count >= 8 and outside_bridge >= 1:
        return "lokaler_anschlussanker"
    return "schwacher_anschluss"


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, token: str, paths: dict[str, dict[str, str]], edge_rows: list[dict[str, str]], core_rows: list[dict[str, str]], out_rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    token_path = _path(paths, token)
    anchor_class = _anchor_class(edge_rows, core_rows, token)
    edge_count = sum(_int(row.get("count", "0")) for row in edge_rows)
    edge_kind_counts = Counter(row.get("edge_kind", "-") for row in edge_rows)
    relation_counts = Counter(row.get("relation", "-") for row in edge_rows)
    in_core_pairs = [row for row in core_rows if row.get("token_a") == token or row.get("token_b") == token]
    weighted_duration = 0.0
    if edge_count:
        weighted_duration = sum(_float(row.get("duration_avg", "0")) * _int(row.get("count", "0")) for row in edge_rows) / edge_count

    lines: list[str] = []
    lines.append(f"# MCM-Brueckenanker Pruefung: {_short(token)}")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose prueft, ob ein starker Bruecken-Token als Brueckenkern, Anschlussanker oder lokaler Vermittler zu lesen ist.")
    lines.append("")
    lines.append("## Tokenprofil")
    lines.append("")
    lines.append("| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(
        f"| `{_short(token)}` | {token_path.get('path_class', '-')} | {token_path.get('movement', '-')} | {token_path.get('base_zone', '-')} | {token_path.get('follow_zone', '-')} | {token_path.get('base_role', '-')} -> {token_path.get('follow_role', '-')} |"
    )
    lines.append("")
    lines.append("## Netzwerkbefund")
    lines.append("")
    lines.append(f"- Ankerklasse: `{anchor_class}`")
    lines.append(f"- Gewichtete Kantenkontakte: `{edge_count}`")
    lines.append(f"- Gewichtete mittlere Dauer: `{weighted_duration:.2f}`")
    lines.append(f"- Kantentypen: `{'; '.join(f'{k}:{v}' for k, v in edge_kind_counts.items())}`")
    lines.append(f"- Relationen: `{'; '.join(f'{k}:{v}' for k, v in relation_counts.items())}`")
    lines.append(f"- In Kernpaaren aus 876: `{'ja' if in_core_pairs else 'nein'}`")
    lines.append("")
    lines.append("## Staerkste Kanten")
    lines.append("")
    lines.append("| Richtung | Nachbar | Relation | Kantentyp | Gewicht | Welten | Dauer | Phase |")
    lines.append("|---|---|---|---|---:|---:|---:|---|")
    for row in out_rows:
        lines.append(
            f"| {row['direction']} | `{_short(row['neighbor'])}` | {row['relation']} | {row['edge_kind']} | {row['count']} | {row['worlds']} | {float(row['duration_avg']):.2f} | {row['exit_phase']} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    if anchor_class == "brueckenkern":
        lines.append("Der Token gehoert zu einem bekannten Brueckenkern.")
    elif anchor_class == "starker_anschlussanker":
        lines.append("Der Token wirkt nicht wie ein Brueckenkern im Sinne der Paarbildung aus 876.")
        lines.append("Er wirkt als starker Anschlussanker: stabiler Brueckenpfad mit mehreren Ein- und Austrittskanten zu nichtzentralen Feldbereichen.")
    elif anchor_class == "lokaler_anschlussanker":
        lines.append("Der Token wirkt als lokaler Anschlussanker, aber noch nicht als starker sekundaerer Kern.")
    else:
        lines.append("Der Token wirkt in dieser Netzwerklesung nur schwach angeschlossen.")
    lines.append("")
    lines.append("Fachlich ist das relevant:")
    lines.append("")
    lines.append("Ein Anschlussanker kann eine Drift-Eigenphase tragen, ohne selbst Teil des zentralen Brueckenkerns zu sein.")
    lines.append("Damit entsteht eine Zwischenebene zwischen Brueckenkern und offener Drift.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte geprueft werden, ob weitere starke Anschlussanker existieren oder ob `0b7nep9` in dieser Rolle singulaer bleibt.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", required=True)
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--cores", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    paths = {row.get("token", ""): row for row in _read(args.paths)}
    network_rows = [row for row in _read(args.network) if row.get("source") == args.token or row.get("target") == args.token]
    core_rows = _read(args.cores)

    out_rows: list[dict[str, str]] = []
    for row in sorted(network_rows, key=lambda item: _int(item.get("count", "0")), reverse=True):
        if row.get("source") == args.token:
            neighbor = row.get("target", "-")
            direction = "ausgehend"
        else:
            neighbor = row.get("source", "-")
            direction = "eingehend"
        out_rows.append(
            {
                "token": args.token,
                "direction": direction,
                "neighbor": neighbor,
                "relation": row.get("relation", "-"),
                "edge_kind": row.get("edge_kind", "-"),
                "count": row.get("count", "0"),
                "worlds": row.get("worlds", "0"),
                "duration_avg": row.get("duration_avg", "0"),
                "exit_phase": row.get("exit_phase", "-"),
                "exit_rekopplung_delta_avg": row.get("exit_rekopplung_delta_avg", "0"),
                "exit_strain_delta_avg": row.get("exit_strain_delta_avg", "0"),
                "neighbor_path_class": _path(paths, neighbor).get("path_class", "-"),
                "neighbor_movement": _path(paths, neighbor).get("movement", "-"),
            }
        )

    _write_csv(args.out_csv, out_rows)
    _write_md(args.out_md, args.token, paths, network_rows, core_rows, out_rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
