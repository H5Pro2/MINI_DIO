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


def _profile(
    token: str,
    landscape: dict[str, dict[str, str]],
    network_rows: list[dict[str, str]],
    paths: dict[str, dict[str, str]],
) -> dict[str, object]:
    edges = [row for row in network_rows if row.get("source") == token or row.get("target") == token]
    total_weight = sum(_int(row.get("count", "0")) for row in edges)
    weighted_duration = (
        sum(_float(row.get("duration_avg", "0")) * _int(row.get("count", "0")) for row in edges) / total_weight
        if total_weight
        else 0.0
    )
    incoming = [row for row in edges if row.get("target") == token]
    outgoing = [row for row in edges if row.get("source") == token]
    neighbor_rows: list[dict[str, str]] = []
    for row in sorted(edges, key=lambda item: _int(item.get("count", "0")), reverse=True):
        if row.get("source") == token:
            direction = "ausgehend"
            neighbor = row.get("target", "")
        else:
            direction = "eingehend"
            neighbor = row.get("source", "")
        neighbor_path = paths.get(neighbor, {})
        neighbor_landscape = landscape.get(neighbor, {})
        neighbor_rows.append(
            {
                "token": token,
                "short_token": _short(token),
                "direction": direction,
                "neighbor": neighbor,
                "short_neighbor": _short(neighbor),
                "neighbor_anchor_class": neighbor_landscape.get("anchor_class", "-"),
                "neighbor_path_class": neighbor_path.get("path_class", "-"),
                "neighbor_movement": neighbor_path.get("movement", "-"),
                "neighbor_role": f"{neighbor_path.get('base_role', '-')}->{neighbor_path.get('follow_role', '-')}",
                "relation": row.get("relation", "-"),
                "edge_kind": row.get("edge_kind", "-"),
                "count": row.get("count", "0"),
                "worlds": row.get("worlds", "0"),
                "duration_avg": row.get("duration_avg", "0"),
                "exit_phase": row.get("exit_phase", "-"),
                "exit_rekopplung_delta_avg": row.get("exit_rekopplung_delta_avg", "0"),
                "exit_strain_delta_avg": row.get("exit_strain_delta_avg", "0"),
            }
        )

    profile = {
        "token": token,
        "short_token": _short(token),
        "landscape": landscape.get(token, {}),
        "path": paths.get(token, {}),
        "edges": edges,
        "neighbor_rows": neighbor_rows,
        "total_weight": total_weight,
        "weighted_duration": weighted_duration,
        "incoming_weight": sum(_int(row.get("count", "0")) for row in incoming),
        "outgoing_weight": sum(_int(row.get("count", "0")) for row in outgoing),
        "incoming_count": len(incoming),
        "outgoing_count": len(outgoing),
        "edge_kinds": Counter(row.get("edge_kind", "-") for row in edges),
        "exit_phases": Counter(row.get("exit_phase", "-") for row in edges),
        "neighbor_classes": Counter(row["neighbor_anchor_class"] for row in neighbor_rows),
        "neighbor_paths": Counter(row["neighbor_path_class"] for row in neighbor_rows),
    }
    return profile


def _subrole(profile: dict[str, object]) -> str:
    total_weight = int(profile["total_weight"])
    weighted_duration = float(profile["weighted_duration"])
    edge_count = len(profile["edges"])  # type: ignore[arg-type]
    landscape = profile["landscape"]  # type: ignore[assignment]
    path_class = landscape.get("path_class", "-") if isinstance(landscape, dict) else "-"
    max_world_span = _int(landscape.get("max_world_span", "0")) if isinstance(landscape, dict) else 0
    if edge_count >= 8 and weighted_duration >= 300:
        return "tiefer_verteilender_anschlussanker"
    if max_world_span >= 5 and edge_count <= 3 and path_class == "stabile_insel":
        return "weltbreiter_kernnaher_inselanker"
    if total_weight >= 20:
        return "starker_lokaler_anschluss"
    return "offener_anschluss"


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(out_path: Path, profiles: list[dict[str, object]]) -> None:
    lines: list[str] = []
    lines.append("# MCM-Anschlussanker Unterrollen")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese passive Diagnose prueft, ob die starken Anschlussanker dieselbe Feldfunktion tragen oder unterschiedliche Unterrollen ausbilden.")
    lines.append("Sie vergleicht Kantenbreite, Dauer, Weltspanne, Ein-/Austrittsverhalten und Nachbarschaftstypen.")
    lines.append("")
    lines.append("## Rollenvergleich")
    lines.append("")
    lines.append("| Token | Unterrolle | Gewicht | Dauer | Ein Gewicht | Aus Gewicht | Kanten | Welten | Pfadklasse | Zone |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---|---|")
    for profile in profiles:
        landscape = profile["landscape"] if isinstance(profile["landscape"], dict) else {}
        path_profile = profile["path"] if isinstance(profile["path"], dict) else {}
        lines.append(
            f"| `{profile['short_token']}` | {_subrole(profile)} | {profile['total_weight']} | {float(profile['weighted_duration']):.2f} | {profile['incoming_weight']} | {profile['outgoing_weight']} | {len(profile['edges'])} | {landscape.get('max_world_span', '-')} | {path_profile.get('path_class', '-')} | {path_profile.get('base_zone', '-')} -> {path_profile.get('follow_zone', '-')} |"
        )
    lines.append("")
    lines.append("## Nachbarschaft")
    lines.append("")
    for profile in profiles:
        lines.append(f"### `{profile['short_token']}`")
        lines.append("")
        lines.append(f"- Kantentypen: `{'; '.join(f'{k}:{v}' for k, v in profile['edge_kinds'].most_common())}`")
        lines.append(f"- Austrittsphasen: `{'; '.join(f'{k}:{v}' for k, v in profile['exit_phases'].most_common())}`")
        lines.append(f"- Nachbar-Klassen: `{'; '.join(f'{k}:{v}' for k, v in profile['neighbor_classes'].most_common())}`")
        lines.append(f"- Nachbar-Pfade: `{'; '.join(f'{k}:{v}' for k, v in profile['neighbor_paths'].most_common())}`")
        lines.append("")
        lines.append("| Richtung | Nachbar | Nachbarrolle | Relation | Kantentyp | Gewicht | Welten | Dauer | Phase |")
        lines.append("|---|---|---|---|---|---:|---:|---:|---|")
        for row in profile["neighbor_rows"][:8]:  # type: ignore[index]
            lines.append(
                f"| {row['direction']} | `{row['short_neighbor']}` | {row['neighbor_anchor_class']} / {row['neighbor_path_class']} | {row['relation']} | {row['edge_kind']} | {row['count']} | {row['worlds']} | {float(row['duration_avg']):.2f} | {row['exit_phase']} |"
            )
        lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("Die starken Anschlussanker sind nicht gleichartig:")
    lines.append("")
    lines.append("- `0b7nep9` wirkt als tiefer verteilender Anschlussanker. Er hat viele Ein- und Austritte, sehr lange Phasen und bindet offene Drift-/Seitenbereiche an.")
    lines.append("- `1jx2k4i` wirkt als weltbreiter kernnaher Inselanker. Er koppelt stabil ueber mehrere Welten, aber deutlich fokussierter und mit weniger Nachbarschaftsbreite.")
    lines.append("")
    lines.append("Damit ist Anschlussanker nicht nur eine Staerke-Klasse, sondern wahrscheinlich eine eigene Zwischenebene mit Unterrollen.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte geprueft werden, ob lokale Anschlussanker eher zu `0b7nep9` oder zu `1jx2k4i` tendieren. Daraus kann eine feinere Anschlussanker-Familienkarte entstehen.")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokens", nargs="+", required=True)
    parser.add_argument("--landscape", required=True, type=Path)
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    landscape = {row.get("token", ""): row for row in _read(args.landscape)}
    paths = {row.get("token", ""): row for row in _read(args.paths)}
    network = _read(args.network)
    profiles = [_profile(token, landscape, network, paths) for token in args.tokens]

    csv_rows: list[dict[str, str]] = []
    for profile in profiles:
        for row in profile["neighbor_rows"]:  # type: ignore[index]
            out = dict(row)
            out["subrole"] = _subrole(profile)
            csv_rows.append(out)
    _write_csv(args.out_csv, csv_rows)
    _write_md(args.out_md, profiles)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
