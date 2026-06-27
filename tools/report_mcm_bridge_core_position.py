from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _short_token(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _score_position(row: dict[str, str]) -> tuple[float, str]:
    roles = [row.get("base_role", ""), row.get("follow_role", "")]
    zones = [row.get("base_zone", ""), row.get("follow_zone", "")]

    center_hits = sum(1 for role in roles if role == "zentrum_stabil")
    rand_hits = sum(1 for role in roles if "rand" in role or "chaos" in role)
    stable_zone_hits = sum(1 for zone in zones if zone == "stabile_bedeutungsinsel")
    bridge_zone_hits = sum(1 for zone in zones if zone == "hoeherer_cluster_uebergang")
    rand_zone_hits = sum(1 for zone in zones if "rand" in zone or "chaos" in zone)

    score = (
        center_hits * 1.0
        + stable_zone_hits * 0.55
        + bridge_zone_hits * 0.35
        - rand_hits * 1.0
        - rand_zone_hits * 0.65
    ) / 3.8
    score = max(-1.0, min(1.0, score))

    if rand_hits or rand_zone_hits:
        label = "randnah"
    elif center_hits == 2 and stable_zone_hits >= 1 and bridge_zone_hits >= 1:
        label = "zentrumsnaher_uebergang"
    elif center_hits == 2 and stable_zone_hits == 2:
        label = "zentrumsnahe_insel"
    elif center_hits == 2 and bridge_zone_hits == 2:
        label = "zentrumsnahe_bruecke"
    elif center_hits:
        label = "teilweise_zentrumsnah"
    else:
        label = "unklar"

    return score, label


def _core_rows(paths_rows: list[dict[str, str]], core_tokens: list[str]) -> list[dict[str, str]]:
    tokens = {token if token.startswith("dio_mcm_episode_") else f"dio_mcm_episode_{token}" for token in core_tokens}
    return [row for row in paths_rows if row.get("token") in tokens]


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "core_name",
        "token",
        "path_class",
        "movement",
        "base_zone",
        "follow_zone",
        "base_role",
        "follow_role",
        "center_position_score",
        "position_label",
        "base_worlds",
        "follow_worlds",
        "rekopplung_delta",
        "strain_delta",
        "loudness_delta",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_core: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_core.setdefault(row["core_name"], []).append(row)

    lines: list[str] = []
    lines.append("# MCM-Brueckenkerne Positionslupe")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append(
        "Diese Diagnose prueft, ob die Brueckenkerne selbst zentrumsnah liegen oder ob ihre Zentrumsnaehe nur indirekt durch stabile Anschlussinseln entsteht."
    )
    lines.append("")
    lines.append("## Befund")
    lines.append("")

    for core_name, core_rows in by_core.items():
        labels = Counter(row["position_label"] for row in core_rows)
        avg_score = sum(float(row["center_position_score"]) for row in core_rows) / max(1, len(core_rows))
        lines.append(f"### {core_name}")
        lines.append("")
        lines.append(f"- Tokens: {len(core_rows)}")
        lines.append(f"- Mittlerer Positionswert: `{avg_score:.4f}`")
        lines.append(f"- Rollenlabel: `{', '.join(f'{key}={value}' for key, value in labels.items())}`")
        lines.append("")
        lines.append("| Token | Klasse | Zone vorher | Zone nachher | Rolle | Positionslabel | Score |")
        lines.append("|---|---|---|---|---|---|---:|")
        for row in core_rows:
            role = f"{row['base_role']} -> {row['follow_role']}"
            lines.append(
                f"| `{_short_token(row['token'])}` | {row['path_class']} | {row['base_zone']} | {row['follow_zone']} | {role} | {row['position_label']} | {float(row['center_position_score']):.4f} |"
            )
        lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("Die untersuchten Brueckenkerne sind in der Pfadklassifikation nicht randnah.")
    lines.append("Ihre Tokens tragen durchgehend `zentrum_stabil` als Rollenlage.")
    lines.append("")
    lines.append("Der Unterschied liegt in der Zonenbewegung:")
    lines.append("")
    lines.append("- reine Bruecken-Tokens bleiben im hoeheren Clusteruebergang,")
    lines.append("- reifende Bruecken-Tokens verbinden Uebergang und stabile Bedeutungsinsel,")
    lines.append("- der stabile Anschlusskern koppelt enger an stabile Inselbereiche.")
    lines.append("")
    lines.append("Damit wirkt die Zentrumsnaehe nicht nur indirekt durch stabile Inseln.")
    lines.append("Die Brueckenkerne selbst tragen bereits eine zentrumsnahe Rollenlage, unterscheiden sich aber in ihrer Anschlussfunktion.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append(
        "Als naechstes sollte geprueft werden, ob Randpfade eigene Gegenkerne bilden oder ob sie nur kurzlebige Oberflaechen- und Austrittsphaenomene bleiben."
    )
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    path_rows = _read_rows(args.paths)
    core_definitions = {
        "zentraler_kern_0e7qvj1_18l3thm": ["0e7qvj1", "18l3thm"],
        "sekundaerer_anschlusskern_0db07p4_1joiyc3": ["0db07p4", "1joiyc3"],
        "seitenarm_0e7qvj1_0mji3u6": ["0e7qvj1", "0mji3u6"],
    }

    out_rows: list[dict[str, str]] = []
    for core_name, tokens in core_definitions.items():
        for row in _core_rows(path_rows, tokens):
            score, label = _score_position(row)
            out = dict(row)
            out["core_name"] = core_name
            out["center_position_score"] = f"{score:.6f}"
            out["position_label"] = label
            out_rows.append(out)

    _write_csv(args.out_csv, out_rows)
    _write_md(args.out_md, out_rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
