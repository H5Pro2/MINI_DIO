from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _int(row: dict[str, str], key: str) -> int:
    try:
        return int(float(row.get(key, "") or 0))
    except ValueError:
        return 0


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _pair_key(source: str, target: str) -> tuple[str, str]:
    return tuple(sorted((source, target)))  # type: ignore[return-value]


def _classify_pair(weight: int, worlds: int, bidirectional: bool) -> str:
    if weight >= 60 and worlds >= 5 and bidirectional:
        return "zentraler_brueckenkern"
    if weight >= 25 and worlds >= 4 and bidirectional:
        return "sekundaerer_brueckenkern"
    if weight >= 8 and worlds >= 3:
        return "lokaler_brueckenpfad"
    return "schwache_brueckenkante"


def _build_pair_rows(edges: list[dict[str, str]]) -> list[dict[str, object]]:
    pairs: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in edges:
        if row.get("edge_kind") != "bruecke_zu_bruecke":
            continue
        pairs[_pair_key(row.get("source", "-") or "-", row.get("target", "-") or "-")].append(row)

    out: list[dict[str, object]] = []
    for (a, b), items in sorted(pairs.items()):
        dirs = Counter((row.get("source", "-") or "-", row.get("target", "-") or "-") for row in items)
        worlds = set()
        weight = 0
        duration_values: list[float] = []
        rek_values: list[float] = []
        strain_values: list[float] = []
        phases = Counter()
        for row in items:
            worlds_count = _int(row, "worlds")
            worlds.update(f"world_{index}" for index in range(worlds_count))
            count = _int(row, "count")
            weight += count
            duration_values.extend([_float(row, "duration_avg")] * max(1, count))
            rek_values.extend([_float(row, "exit_rekopplung_delta_avg")] * max(1, count))
            strain_values.extend([_float(row, "exit_strain_delta_avg")] * max(1, count))
            phases[row.get("exit_phase", "-") or "-"] += count
        a_to_b = dirs.get((a, b), 0)
        b_to_a = dirs.get((b, a), 0)
        bidirectional = a_to_b > 0 and b_to_a > 0
        world_span = max(_int(row, "worlds") for row in items) if items else 0
        out.append(
            {
                "token_a": a,
                "token_b": b,
                "weight": weight,
                "world_span": world_span,
                "directions": len(dirs),
                "bidirectional": int(bidirectional),
                "a_to_b_edges": a_to_b,
                "b_to_a_edges": b_to_a,
                "duration_avg_weighted": round(_avg(duration_values), 6),
                "exit_rekopplung_delta_avg": round(_avg(rek_values), 6),
                "exit_strain_delta_avg": round(_avg(strain_values), 6),
                "dominant_exit_phase": phases.most_common(1)[0][0] if phases else "-",
                "phase_profile": "; ".join(f"{phase}:{count}" for phase, count in phases.most_common()),
                "core_class": _classify_pair(weight, world_span, bidirectional),
            }
        )
    out.sort(key=lambda row: (-int(row["weight"]), str(row["token_a"]), str(row["token_b"])))
    return out


def _write_csv(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out.write_text("", encoding="utf-8")
        return
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(rows: list[dict[str, object]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    class_counts = Counter(str(row["core_class"]) for row in rows)
    lines = [
        "# MCM-Brueckenkerne Vergleich",
        "",
        "## Zweck",
        "",
        "Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.",
        "Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.",
        "",
        "## Kernklassen",
        "",
        "| Klasse | Anzahl |",
        "|---|---:|",
    ]
    for name, count in sorted(class_counts.items()):
        lines.append(f"| {name} | {count} |")

    lines.extend(
        [
            "",
            "## Brueckenpaare",
            "",
            "| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| {row['core_class']} | {row['token_a']} | {row['token_b']} | {row['weight']} | {row['world_span']} | "
            f"{row['bidirectional']} | {row['a_to_b_edges']} | {row['b_to_a_edges']} | "
            f"{float(row['duration_avg_weighted']):.2f} | {row['dominant_exit_phase']} |"
        )

    lines.extend(["", "## Befund", ""])
    if rows:
        top = rows[0]
        lines.append(
            f"Der staerkste Kern ist `{top['token_a']}` <-> `{top['token_b']}` mit Gewicht `{top['weight']}` und Weltspanne `{top['world_span']}`."
        )
    if class_counts.get("zentraler_brueckenkern", 0) == 1:
        lines.append("Es gibt genau einen zentralen Brueckenkern. Die uebrigen Paare wirken als sekundaere Kerne oder lokale Pfade.")
    elif class_counts.get("zentraler_brueckenkern", 0) > 1:
        lines.append("Es gibt mehrere zentrale Brueckenkerne. Das wuerde fuer eine verteilte Uebergangstopologie sprechen.")
    else:
        lines.append("Es gibt keinen einzelnen dominanten zentralen Kern. Das Feld waere eher verteilt oder lokal organisiert.")

    secondary = [row for row in rows if row["core_class"] == "sekundaerer_brueckenkern"]
    if secondary:
        lines.append(
            "Sekundaere Kerne sind vorhanden. Sie bilden wahrscheinlich lokale Uebergangsbereiche um den Hauptkern herum."
        )

    lines.extend(
        [
            "",
            "## Bedeutung",
            "",
            "Die Brueckentopologie wirkt hier hierarchisch:",
            "",
            "```text",
            "zentraler Brueckenkern",
            "sekundaere Brueckenkerne",
            "lokale Brueckenpfade",
            "schwache Brueckenkanten",
            "```",
            "",
            "Damit entsteht keine flache Verbindungsliste, sondern eine strukturierte Uebergangstopologie.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Rolle des zentralen Kerns gegen Randpfade und stabile Inseln gelesen werden: fuehrt der Kern eher in Zentrum, Rand oder offene Feldlagen?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edges", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    args = parser.parse_args()

    rows = _build_pair_rows(_load(Path(args.edges)))
    _write_csv(rows, Path(args.out_csv))
    _write_markdown(rows, Path(args.out_md))
    print(f"pairs={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
