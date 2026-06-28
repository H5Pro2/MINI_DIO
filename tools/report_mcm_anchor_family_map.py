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


def _neighbor_edges(token: str, network: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in network if row.get("source") == token or row.get("target") == token]


def _classify_family(
    token: str,
    edges: list[dict[str, str]],
    landscape: dict[str, dict[str, str]],
    paths: dict[str, dict[str, str]],
) -> tuple[str, str]:
    neighbor_classes = Counter()
    neighbor_paths = Counter()
    neighbor_tokens = Counter()
    total_weight = 0
    weighted_duration = 0.0
    for edge in edges:
        count = _int(edge.get("count", "0"))
        total_weight += count
        weighted_duration += _float(edge.get("duration_avg", "0")) * count
        neighbor = edge.get("target", "") if edge.get("source") == token else edge.get("source", "")
        neighbor_tokens[neighbor] += count
        neighbor_classes[landscape.get(neighbor, {}).get("anchor_class", "-")] += count
        neighbor_paths[paths.get(neighbor, {}).get("path_class", "-")] += count
    duration = weighted_duration / total_weight if total_weight else 0.0
    path = paths.get(token, {})

    if neighbor_tokens.get("dio_mcm_episode_0b7nep9", 0) >= 5:
        return "verteilungsanker_familie", "Direkte gewichtete Kopplung an 0b7nep9."
    if neighbor_tokens.get("dio_mcm_episode_1jx2k4i", 0) >= 5:
        return "kernnaher_inselanker_familie", "Direkte gewichtete Kopplung an 1jx2k4i."
    if neighbor_classes.get("brueckenkern", 0) >= 10 and path.get("path_class") == "stabile_insel":
        return "kernnaher_inselanker_familie", "Stabile Insel mit starker Kopplung an Brueckenkern."
    if duration >= 120 and total_weight >= 20:
        return "verteilungsanker_familie", "Lange gewichtete Dauer und starke Anschlussbreite deuten auf verteilende Feldphase."
    if path.get("path_class") == "brueckenpfad" or "rekopplungszone" in path.get("follow_zone", ""):
        return "uebergangsanker_familie", "Brueckenpfad oder Rekopplungszone ohne klare starke Kernfamilie."
    return "offene_anschlussfamilie", "Anschluss sichtbar, aber Familiennaehe bleibt offen."


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    family_counts = Counter(row["family"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Anschlussanker Familienkarte")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese passive Diagnose ordnet lokale Anschlussanker den beobachteten starken Anschlussanker-Unterrollen zu.")
    lines.append("Geprueft wird, ob lokale Anker eher zum verteilenden `0b7nep9`-Typ, zum kernnahen `1jx2k4i`-Typ oder zu einer eigenen Uebergangsrolle tendieren.")
    lines.append("")
    lines.append("## Gesamtbefund")
    lines.append("")
    lines.append(f"- Lokale/starke Anschlussanker in der Familienkarte: `{len(rows)}`")
    lines.append(f"- Familienprofil: `{'; '.join(f'{k}:{v}' for k, v in family_counts.most_common())}`")
    lines.append("")
    lines.append("## Familienkarte")
    lines.append("")
    lines.append("| Token | Ankerklasse | Familie | Gewicht | Welten | Dauer | Pfadklasse | Bewegung | Hauptnachbar | Begruendung |")
    lines.append("|---|---|---|---:|---:|---:|---|---|---|---|")
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | {row['anchor_class']} | {row['family']} | {row['total_weight']} | {row['max_world_span']} | {float(row['weighted_duration']):.2f} | {row['path_class']} | {row['movement']} | `{row['main_neighbor']}` | {row['reason']} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("Die Anschlussanker-Ebene teilt sich in mindestens drei lesbare Familien:")
    lines.append("")
    lines.append("- `verteilungsanker_familie`: bindet offene oder lange Feldphasen an und wirkt eher als breiter Anschlussraum.")
    lines.append("- `kernnaher_inselanker_familie`: koppelt stabile Inseln direkt an Brueckenkerne.")
    lines.append("- `uebergangsanker_familie`: wirkt als Reifungs- oder Rekopplungsstueck zwischen stabiler Insel und Brueckenpfad.")
    lines.append("")
    lines.append("Das spricht dafuer, dass die MCM-Topologie nicht nur Zentrum/Rand kennt, sondern eine differenzierte Anschlusszone zwischen stabiler Bedeutung und offener Feldbewegung ausbildet.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte geprueft werden, ob diese Anschlussanker-Familien in anderen Weltgruppen wieder auftauchen oder ob sie nur aus dieser Brueckenlandschaft entstehen.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--landscape", required=True, type=Path)
    parser.add_argument("--network", required=True, type=Path)
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    landscape_rows = _read(args.landscape)
    landscape = {row.get("token", ""): row for row in landscape_rows}
    paths = {row.get("token", ""): row for row in _read(args.paths)}
    network = _read(args.network)

    rows: list[dict[str, str]] = []
    for row in landscape_rows:
        if row.get("anchor_class") not in {"starker_anschlussanker", "lokaler_anschlussanker"}:
            continue
        token = row.get("token", "")
        edges = _neighbor_edges(token, network)
        total_weight = sum(_int(edge.get("count", "0")) for edge in edges)
        weighted_duration = (
            sum(_float(edge.get("duration_avg", "0")) * _int(edge.get("count", "0")) for edge in edges) / total_weight
            if total_weight
            else 0.0
        )
        neighbor_weights: Counter[str] = Counter()
        for edge in edges:
            neighbor = edge.get("target", "") if edge.get("source") == token else edge.get("source", "")
            neighbor_weights[_short(neighbor)] += _int(edge.get("count", "0"))
        family, reason = _classify_family(token, edges, landscape, paths)
        path = paths.get(token, {})
        rows.append(
            {
                "token": token,
                "short_token": _short(token),
                "anchor_class": row.get("anchor_class", "-"),
                "family": family,
                "total_weight": str(total_weight),
                "max_world_span": row.get("max_world_span", "0"),
                "weighted_duration": f"{weighted_duration:.6f}",
                "path_class": path.get("path_class", "-"),
                "movement": path.get("movement", "-"),
                "base_zone": path.get("base_zone", "-"),
                "follow_zone": path.get("follow_zone", "-"),
                "main_neighbor": neighbor_weights.most_common(1)[0][0] if neighbor_weights else "-",
                "neighbor_profile": "; ".join(f"{k}:{v}" for k, v in neighbor_weights.most_common()),
                "reason": reason,
            }
        )

    rows.sort(key=lambda item: (item["family"], -_int(item["total_weight"]), item["short_token"]))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
