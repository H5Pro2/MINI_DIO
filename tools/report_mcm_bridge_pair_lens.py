from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def _load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _float(row: dict[str, str], key: str) -> float:
    try:
        value = float(row.get(key, "") or 0.0)
    except ValueError:
        return 0.0
    return 0.0 if value != value else value


def _avg(values: list[float]) -> float:
    return sum(values) / max(1, len(values))


def _phase(rek_delta: float, strain_delta: float) -> str:
    if rek_delta > 0.0 and strain_delta <= 0.0:
        return "rekoppelnd"
    if rek_delta < 0.0 and strain_delta > 0.0:
        return "oeffnend_belastend"
    return "gemischt"


def _edge_rows(rows: list[dict[str, str]], token_a: str, token_b: str) -> list[dict[str, object]]:
    wanted = {token_a, token_b}
    out: list[dict[str, object]] = []
    for row in rows:
        token = row.get("token", "-") or "-"
        if token not in wanted:
            continue
        world = row.get("world", "-") or "-"
        duration = _float(row, "duration")
        exit_rek = _float(row, "after_rekopplung") - _float(row, "end_rekopplung")
        exit_strain = _float(row, "after_strain") - _float(row, "end_strain")
        within_rek = _float(row, "end_rekopplung") - _float(row, "start_rekopplung")
        within_strain = _float(row, "end_strain") - _float(row, "start_strain")
        within_loud = _float(row, "end_loudness") - _float(row, "start_loudness")
        exit_loud = _float(row, "after_loudness") - _float(row, "end_loudness")

        enter_from = row.get("enter_from", "-") or "-"
        exit_to = row.get("exit_to", "-") or "-"
        if enter_from in wanted:
            out.append(
                {
                    "source": enter_from,
                    "target": token,
                    "relation": "eintritt",
                    "world": world,
                    "duration": duration,
                    "within_rekopplung_delta": within_rek,
                    "within_strain_delta": within_strain,
                    "within_loudness_delta": within_loud,
                    "exit_rekopplung_delta": exit_rek,
                    "exit_strain_delta": exit_strain,
                    "exit_loudness_delta": exit_loud,
                    "exit_phase": _phase(exit_rek, exit_strain),
                }
            )
        if exit_to in wanted:
            out.append(
                {
                    "source": token,
                    "target": exit_to,
                    "relation": "austritt",
                    "world": world,
                    "duration": duration,
                    "within_rekopplung_delta": within_rek,
                    "within_strain_delta": within_strain,
                    "within_loudness_delta": within_loud,
                    "exit_rekopplung_delta": exit_rek,
                    "exit_strain_delta": exit_strain,
                    "exit_loudness_delta": exit_loud,
                    "exit_phase": _phase(exit_rek, exit_strain),
                }
            )
    out.sort(key=lambda item: (str(item["source"]), str(item["target"]), str(item["relation"]), str(item["world"])))
    return out


def _summary(rows: list[dict[str, str]], token_a: str, token_b: str) -> list[dict[str, object]]:
    wanted = {token_a, token_b}
    by_token: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        token = row.get("token", "-") or "-"
        if token in wanted:
            by_token[token].append(row)

    out: list[dict[str, object]] = []
    for token in sorted(wanted):
        items = by_token.get(token, [])
        worlds = Counter(row.get("world", "-") or "-" for row in items)
        enter_from = Counter(row.get("enter_from", "-") or "-" for row in items)
        exit_to = Counter(row.get("exit_to", "-") or "-" for row in items)
        other = token_b if token == token_a else token_a
        out.append(
            {
                "token": token,
                "segments": len(items),
                "worlds": len(worlds),
                "world_profile": "; ".join(f"{name}:{count}" for name, count in worlds.most_common()),
                "dominant_enter": enter_from.most_common(1)[0][0] if enter_from else "-",
                "dominant_enter_count": enter_from.most_common(1)[0][1] if enter_from else 0,
                "pair_enter_count": enter_from.get(other, 0),
                "dominant_exit": exit_to.most_common(1)[0][0] if exit_to else "-",
                "dominant_exit_count": exit_to.most_common(1)[0][1] if exit_to else 0,
                "pair_exit_count": exit_to.get(other, 0),
                "duration_avg": _avg([_float(row, "duration") for row in items]),
                "within_rekopplung_delta_avg": _avg(
                    [_float(row, "end_rekopplung") - _float(row, "start_rekopplung") for row in items]
                ),
                "exit_rekopplung_delta_avg": _avg(
                    [_float(row, "after_rekopplung") - _float(row, "end_rekopplung") for row in items]
                ),
                "within_strain_delta_avg": _avg(
                    [_float(row, "end_strain") - _float(row, "start_strain") for row in items]
                ),
                "exit_strain_delta_avg": _avg(
                    [_float(row, "after_strain") - _float(row, "end_strain") for row in items]
                ),
                "within_loudness_delta_avg": _avg(
                    [_float(row, "end_loudness") - _float(row, "start_loudness") for row in items]
                ),
                "exit_loudness_delta_avg": _avg(
                    [_float(row, "after_loudness") - _float(row, "end_loudness") for row in items]
                ),
            }
        )
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


def _write_markdown(summary: list[dict[str, object]], edges: list[dict[str, object]], token_a: str, token_b: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    edge_counts = Counter((str(row["source"]), str(row["target"])) for row in edges)
    edge_phase = Counter(str(row["exit_phase"]) for row in edges)
    edge_worlds: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in edges:
        edge_worlds[(str(row["source"]), str(row["target"]))].add(str(row["world"]))

    lines = [
        "# MCM-Brueckenpaar Lupe",
        "",
        "## Zweck",
        "",
        f"Diese Diagnose liest das staerkste stabile Brueckenpaar `{token_a}` und `{token_b}`.",
        "Sie prueft, ob das Paar nur gemeinsam haeufig erscheint oder ob gerichtete Rueckbezuege zwischen beiden Tokens bestehen.",
        "",
        "## Tokenprofil",
        "",
        "| Token | Segmente | Welten | Dauer | Paar-Eintritte | Paar-Austritte | Rekopplung innen | Rekopplung Austritt | Strain innen | Strain Austritt |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        lines.append(
            f"| {row['token']} | {row['segments']} | {row['worlds']} | {float(row['duration_avg']):.2f} | "
            f"{row['pair_enter_count']} | {row['pair_exit_count']} | "
            f"{float(row['within_rekopplung_delta_avg']):+.4f} | {float(row['exit_rekopplung_delta_avg']):+.4f} | "
            f"{float(row['within_strain_delta_avg']):+.4f} | {float(row['exit_strain_delta_avg']):+.4f} |"
        )

    lines.extend(["", "## Gerichtete Paarkanten", "", "| Quelle | Ziel | Anzahl | Welten |", "|---|---|---:|---:|"])
    for (source, target), count in sorted(edge_counts.items(), key=lambda item: (-item[1], item[0][0], item[0][1])):
        lines.append(f"| {source} | {target} | {count} | {len(edge_worlds[(source, target)])} |")

    lines.extend(["", "## Austrittsphasen Im Paar", "", "| Phase | Anzahl |", "|---|---:|"])
    for phase, count in sorted(edge_phase.items()):
        lines.append(f"| {phase} | {count} |")

    a_to_b = edge_counts.get((token_a, token_b), 0)
    b_to_a = edge_counts.get((token_b, token_a), 0)
    worlds_a_to_b = len(edge_worlds.get((token_a, token_b), set()))
    worlds_b_to_a = len(edge_worlds.get((token_b, token_a), set()))

    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"`{token_a}` -> `{token_b}` tritt `{a_to_b}` mal in `{worlds_a_to_b}` Welten auf.",
            f"`{token_b}` -> `{token_a}` tritt `{b_to_a}` mal in `{worlds_b_to_a}` Welten auf.",
            "",
        ]
    )
    if a_to_b > 0 and b_to_a > 0:
        lines.append(
            "Das Paar ist gegenseitig gerichtet. Es ist damit kein einfacher einseitiger Uebergang, sondern ein Rueckbezugsbereich im Brueckennetz."
        )
    else:
        lines.append("Das Paar wirkt einseitig. Es muesste eher als gerichteter Kanal denn als Rueckbezugsbereich gelesen werden.")

    if min(worlds_a_to_b, worlds_b_to_a) >= 4:
        lines.append(
            "Die Gegenseitigkeit erscheint ueber mehrere Welten. Das spricht gegen eine zufaellige Einzelwelt-Kopplung."
        )

    lines.extend(
        [
            "",
            "## Bedeutung",
            "",
            "Das Paar wirkt wie ein zentraler Uebergangsknoten im MCM-Feld:",
            "",
            "```text",
            "Aussenwelt aktiviert Bruecke A/B",
            "Bruecke A fuehrt zu Bruecke B",
            "Bruecke B fuehrt wieder zu Bruecke A",
            "danach erfolgt ein Austritt in weitere Feldzustaende",
            "```",
            "",
            "Damit entsteht eine kleine Rueckbezugsstruktur, nicht nur eine isolierte Bedeutung.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieses Paar gegen andere Brueckenpaare verglichen werden: Ist `0e7qvj1`/`18l3thm` der zentrale Brueckenkern, oder gibt es mehrere getrennte Brueckenkerne im Feld?",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--details", required=True)
    parser.add_argument("--token-a", required=True)
    parser.add_argument("--token-b", required=True)
    parser.add_argument("--out-md", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--summary-csv", required=True)
    args = parser.parse_args()

    details = _load(Path(args.details))
    summary_rows = _summary(details, args.token_a, args.token_b)
    edge_rows = _edge_rows(details, args.token_a, args.token_b)
    _write_csv(summary_rows, Path(args.summary_csv))
    _write_csv(edge_rows, Path(args.out_csv))
    _write_markdown(summary_rows, edge_rows, args.token_a, args.token_b, Path(args.out_md))
    print(f"pair_edges={len(edge_rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.summary_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
