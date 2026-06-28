from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


CLASS_RANK = {
    "-": 0,
    "schwacher_anschluss": 1,
    "schwacher_brueckenpfad": 1,
    "lokaler_anschlussanker": 2,
    "starker_anschlussanker": 3,
    "brueckenkern": 4,
}


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _short(token: str) -> str:
    return token.replace("dio_mcm_episode_", "")


def _rank(anchor_class: str) -> int:
    return CLASS_RANK.get(anchor_class or "-", 0)


def _by_short(rows: list[dict[str, str]], token_key: str = "token") -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        short = row.get("short_token") or _short(row.get(token_key, ""))
        if short:
            out[short] = row
    return out


def _follow_state(previous: dict[str, str], follow: dict[str, str] | None) -> tuple[str, str]:
    previous_class = previous.get("current_class", "-")
    previous_rank = _rank(previous_class)
    follow_class = (follow or {}).get("anchor_class", "-")
    follow_rank = _rank(follow_class)
    axis_profile = previous.get("axis_profile", "-")

    if follow is None:
        return "verschwindet", "Die Spur ist in der Folgewelt nicht als Anschlussrolle sichtbar."
    if previous_rank == 0 and follow_rank > 0:
        return "taucht_auf", "Die Spur wird in der Folgewelt erstmals als Anschlussrolle sichtbar."
    if follow_rank > previous_rank:
        return "reift_weiter", "Die Spur gewinnt Anschluss- oder Kernnaehe."
    if follow_rank == previous_rank and follow_rank > 0:
        if axis_profile in {"junge_drift_oeffnung", "neu_ohne_basisdrift"}:
            return "jung_gehalten", "Die junge Spur bleibt sichtbar, reift aber noch nicht weiter."
        return "rolle_gehalten", "Die Rolle bleibt auf aehnlicher Reifestufe sichtbar."
    if follow_rank < previous_rank and follow_rank > 0:
        return "entlastet_weiter", "Die Rolle bleibt sichtbar, aber mit geringerer Reifestufe."
    return "offen", "Keine klare Folgelesung."


def _rows(previous_rows: list[dict[str, str]], follow_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    follow = _by_short(follow_rows)
    out: list[dict[str, str]] = []
    for previous in previous_rows:
        short = previous.get("short_token", "")
        current = follow.get(short)
        state, reason = _follow_state(previous, current)
        out.append(
            {
                "short_token": short,
                "previous_status": previous.get("status", "-"),
                "previous_axis_profile": previous.get("axis_profile", "-"),
                "previous_class": previous.get("current_class", "-"),
                "previous_weight": previous.get("current_weight", "0"),
                "follow_class": (current or {}).get("anchor_class", "-"),
                "follow_weight": (current or {}).get("total_weight", "0"),
                "follow_world_span": (current or {}).get("max_world_span", "0"),
                "follow_path_class": (current or {}).get("path_class", "-"),
                "follow_movement": (current or {}).get("movement", "-"),
                "follow_state": state,
                "reason": reason,
            }
        )
    out.sort(key=lambda row: (row["follow_state"], row["short_token"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["follow_state"] for row in rows)
    lines: list[str] = []
    lines.append("# MCM-Reorganisationsgruppe gegen Folgewelt")
    lines.append("")
    lines.append("## Zweck")
    lines.append("")
    lines.append("Diese Diagnose liest die in 927 isolierte Reorganisationsgruppe gegen eine weitere Folgewelt.")
    lines.append("Geprueft wird, ob junge Spuren verschwinden, gehalten werden oder in tragendere Anschlussrollen reifen.")
    lines.append("")
    lines.append("## Folgestatus")
    lines.append("")
    lines.append("| Folgestatus | Anzahl |")
    lines.append("|---|---:|")
    for state, count in counts.most_common():
        lines.append(f"| {state} | {count} |")
    lines.append("")
    lines.append("## Tokens")
    lines.append("")
    lines.append("| Token | Vorher | Achse | Folgerolle | Folgegewicht | Folgestatus |")
    lines.append("|---|---|---|---|---:|---|")
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | {row['previous_class']} | {row['previous_axis_profile']} | {row['follow_class']} | {row['follow_weight']} | {row['follow_state']} |"
        )
    lines.append("")
    lines.append("## Befund")
    lines.append("")
    lines.append("Die Reorganisationsgruppe kann als kleine Pruefgruppe weiterverfolgt werden.")
    lines.append("Relevant ist, ob ein junger oder driftender Zustand in einer Folgewelt verschwindet, gehalten bleibt oder Anschlussreife gewinnt.")
    lines.append("")
    lines.append("## Wie es weitergeht")
    lines.append("")
    lines.append("Als naechstes sollte nur fuer die gehaltenen oder weiter reifenden Tokens eine Segmentlupe gebaut werden. So wird sichtbar, durch welche Weltphasen die Reifung getragen wird.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous", required=True, type=Path)
    parser.add_argument("--follow-landscape", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _rows(_read(args.previous), _read(args.follow_landscape))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
