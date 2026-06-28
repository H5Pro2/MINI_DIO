from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


TOKENS = {"dio_mcm_episode_0b7nep9", "dio_mcm_episode_0ykar6i"}


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


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _segment_profile(rows: list[dict[str, str]], label: str) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        token = row.get("token", "")
        if token not in TOKENS:
            continue
        grouped[(token, row.get("world", "-"))].append(row)

    out: list[dict[str, str]] = []
    for (token, world), items in sorted(grouped.items()):
        enter = Counter(row.get("enter_from", "-") for row in items)
        exit_to = Counter(row.get("exit_to", "-") for row in items)
        durations = [_float(row.get("duration", "0")) for row in items]
        direct_pair_enters = sum(1 for row in items if row.get("enter_from") in TOKENS)
        direct_pair_exits = sum(1 for row in items if row.get("exit_to") in TOKENS)
        out.append(
            {
                "landscape": label,
                "token": token,
                "short_token": _short(token),
                "world": world,
                "segments": str(len(items)),
                "duration_sum": f"{sum(durations):.6f}",
                "duration_avg": f"{_avg(durations):.6f}",
                "duration_max": f"{max(durations) if durations else 0.0:.6f}",
                "direct_pair_enters": str(direct_pair_enters),
                "direct_pair_exits": str(direct_pair_exits),
                "direct_pair_contact_share": f"{(direct_pair_enters + direct_pair_exits) / max(1, len(items) * 2):.6f}",
                "dominant_enter": enter.most_common(1)[0][0] if enter else "-",
                "dominant_exit": exit_to.most_common(1)[0][0] if exit_to else "-",
                "enter_profile": "; ".join(f"{_short(k)}:{v}" for k, v in enter.most_common(6)),
                "exit_profile": "; ".join(f"{_short(k)}:{v}" for k, v in exit_to.most_common(6)),
                "rekopplung_exit_avg": f"{_avg([_float(row.get('after_rekopplung', '0')) - _float(row.get('end_rekopplung', '0')) for row in items]):.6f}",
                "strain_exit_avg": f"{_avg([_float(row.get('after_strain', '0')) - _float(row.get('end_strain', '0')) for row in items]):.6f}",
                "tension_exit_avg": f"{_avg([_float(row.get('after_tension', '0')) - _float(row.get('end_tension', '0')) for row in items]):.6f}",
            }
        )
    return out


def _edge_profile(rows: list[dict[str, str]], label: str) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        source = row.get("source", "")
        target = row.get("target", "")
        if source not in TOKENS and target not in TOKENS:
            continue
        if source in TOKENS and target in TOKENS:
            relation_group = "direktes_paar"
        elif source in TOKENS:
            relation_group = "token_zu_aussen"
        else:
            relation_group = "aussen_zu_token"
        out.append(
            {
                "landscape": label,
                "source": source,
                "target": target,
                "short_source": _short(source),
                "short_target": _short(target),
                "relation": row.get("relation", "-"),
                "relation_group": relation_group,
                "edge_kind": row.get("edge_kind", "-"),
                "count": row.get("count", "0"),
                "worlds": row.get("worlds", "0"),
                "duration_avg": row.get("duration_avg", "0"),
                "exit_rekopplung_delta_avg": row.get("exit_rekopplung_delta_avg", "0"),
                "exit_strain_delta_avg": row.get("exit_strain_delta_avg", "0"),
                "exit_phase": row.get("exit_phase", "-"),
            }
        )
    out.sort(key=lambda row: (-_int(row["count"]), row["landscape"], row["short_source"], row["short_target"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, segment_rows: list[dict[str, str]], edge_rows: list[dict[str, str]]) -> None:
    edge_group_counts: dict[str, Counter[str]] = defaultdict(Counter)
    edge_group_weights: dict[str, Counter[str]] = defaultdict(Counter)
    for row in edge_rows:
        edge_group_counts[row["landscape"]][row["relation_group"]] += 1
        edge_group_weights[row["landscape"]][row["relation_group"]] += _int(row["count"])

    lines: list[str] = []
    lines.append("# MCM-Rollenwanderung 0b7nep9 / 0ykar6i")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose untersucht, welche Welt- und Kantenmerkmale `0b7nep9` vom verteilenden Anschlussanker zum Kernpartner von `0ykar6i` verschieben.")
    lines.append("")
    lines.append("## Kantenwechsel")
    lines.append("")
    lines.append("| Landschaft | Direkte Paar-Kanten | Direkte Paar-Gewichte | Aussenkontakt-Gewichte |")
    lines.append("|---|---:|---:|---:|")
    for landscape in sorted(edge_group_weights):
        pair_edges = edge_group_counts[landscape].get("direktes_paar", 0)
        pair_weight = edge_group_weights[landscape].get("direktes_paar", 0)
        outside_weight = edge_group_weights[landscape].get("token_zu_aussen", 0) + edge_group_weights[landscape].get("aussen_zu_token", 0)
        lines.append(f"| {landscape} | {pair_edges} | {pair_weight} | {outside_weight} |")
    lines.append("")
    lines.append("## Weltprofile")
    lines.append("")
    lines.append("| Landschaft | Token | Welt | Segmente | Dauer Summe | Dauer Max | Direkter Paaranteil | Dominanter Eintritt | Dominanter Austritt |")
    lines.append("|---|---|---|---:|---:|---:|---:|---|---|")
    for row in sorted(segment_rows, key=lambda item: (item["landscape"], item["short_token"], -_float(item["duration_sum"]))):
        lines.append(
            f"| {row['landscape']} | `{row['short_token']}` | {row['world']} | {row['segments']} | {_float(row['duration_sum']):.0f} | {_float(row['duration_max']):.0f} | {_float(row['direct_pair_contact_share']):.3f} | `{_short(row['dominant_enter'])}` | `{_short(row['dominant_exit'])}` |"
        )
    lines.append("")
    lines.append("## Staerkste Kanten")
    lines.append("")
    lines.append("| Landschaft | Gruppe | Quelle | Ziel | Gewicht | Welten | Dauer | Phase |")
    lines.append("|---|---|---|---|---:|---:|---:|---|")
    for row in edge_rows[:24]:
        lines.append(
            f"| {row['landscape']} | {row['relation_group']} | `{row['short_source']}` | `{row['short_target']}` | {row['count']} | {row['worlds']} | {_float(row['duration_avg']):.2f} | {row['exit_phase']} |"
        )
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("In der Basislandschaft 872/894 ist `0b7nep9` breit an Aussen-, Rand- und Seitenphasen gekoppelt. Der direkte Kontakt zu `0ykar6i` ist vorhanden, aber nicht dominant.")
    lines.append("In der Vergleichslandschaft 898/901 wird die direkte Kopplung `0b7nep9` <-> `0ykar6i` dominant und bidirektional. Dadurch wandert `0b7nep9` aus der Anschlussrolle in den Kernbereich.")
    lines.append("")
    lines.append("Die Rollenwanderung entsteht also nicht aus einem einzelnen Wert, sondern aus einer topologischen Reorganisation:")
    lines.append("")
    lines.append("```text")
    lines.append("breite Aussenkopplung -> verteilender Anschlussanker")
    lines.append("dominante bidirektionale Paarbindung -> Brueckenkern / Kernpartner")
    lines.append("```")
    lines.append("")
    lines.append("## Bedeutung")
    lines.append("")
    lines.append("Das stuetzt die Annahme einer dynamischen MCM-Feldordnung. Ein Zeichen ist nicht absolut eine Rolle, sondern traegt eine Rolle relativ zur Weltspannung und zur Nachbarschaftsstruktur.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte geprueft werden, ob andere Tokens dieselbe Rollenwanderung zeigen: schwacher Anschluss -> starker Anschluss -> Kernpartner.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-details", required=True, type=Path)
    parser.add_argument("--compare-details", required=True, type=Path)
    parser.add_argument("--base-network", required=True, type=Path)
    parser.add_argument("--compare-network", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-segments", required=True, type=Path)
    parser.add_argument("--out-edges", required=True, type=Path)
    args = parser.parse_args()

    segment_rows = (
        _segment_profile(_read(args.base_details), "894_basis")
        + _segment_profile(_read(args.compare_details), "901_vergleich")
    )
    edge_rows = (
        _edge_profile(_read(args.base_network), "894_basis")
        + _edge_profile(_read(args.compare_network), "901_vergleich")
    )
    _write_csv(args.out_segments, segment_rows)
    _write_csv(args.out_edges, edge_rows)
    _write_md(args.out_md, segment_rows, edge_rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_segments}")
    print(f"wrote {args.out_edges}")


if __name__ == "__main__":
    main()
