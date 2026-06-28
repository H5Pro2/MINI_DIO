from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _read(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _by_short(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        short = row.get("short_token") or row.get("token", "").replace("dio_mcm_episode_", "")
        if short:
            out[short] = row
    return out


def _read_state(memory: dict[str, str], current: dict[str, str] | None) -> tuple[str, str]:
    previous_target = memory.get("to_nonbridge_class", "-")
    previous_quality = memory.get("shift_quality", "-")
    if current is None:
        return "shift_spur_nicht_sichtbar", "Rollenwechselspur wird in der Folgewelt nicht sichtbar."

    current_class = current.get("nonbridge_class", "-")
    if current_class == previous_target:
        return "shift_zielrolle_reproduziert", "Rollenwechsel fuehrt erneut in dieselbe Nicht-Bruecken-Klasse."
    if previous_target.startswith("nichtbruecke_zentrum") and current_class.startswith("nichtbruecke_zentrum"):
        return "shift_zentrum_erhalten", "Zielrolle bleibt zentrumsnah, aber mit anderer Schaerfe."
    if "rekopplung" in previous_target and "rekopplung" in current_class:
        return "shift_rekopplung_erhalten", "Rekopplungsnaehe bleibt erhalten."
    if previous_quality == "shift_nicht_sichtbar" and current_class != "-":
        return "shift_neu_sichtbar", "Vorher unsichtbare Spur wird in Folgewelt sichtbar."
    if current_class in {"nichtbruecke_randspannung", "nichtbruecke_sinnesrauschen"}:
        return "shift_in_last_oder_rauschen", "Rollenwechselspur erscheint unter Last/Rauschen."
    return "shift_umorganisiert", "Rollenwechselspur bleibt sichtbar, aber in anderer Nicht-Bruecken-Klasse."


def _build(memory_rows: list[dict[str, str]], nonbridge_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    current_by_short = _by_short(nonbridge_rows)
    out: list[dict[str, str]] = []
    for memory in memory_rows:
        short = memory.get("short_token", "")
        current = current_by_short.get(short)
        state, note = _read_state(memory, current)
        out.append(
            {
                "shift_symbol": memory.get("shift_symbol", ""),
                "short_token": short,
                "previous_shift_quality": memory.get("shift_quality", "-"),
                "previous_to_nonbridge_class": memory.get("to_nonbridge_class", "-"),
                "current_nonbridge_class": (current or {}).get("nonbridge_class", "-"),
                "current_zone": (current or {}).get("condensation_zone", "-"),
                "current_role": (current or {}).get("dominant_role", "-"),
                "current_observations": (current or {}).get("observations", "0"),
                "current_worlds": (current or {}).get("worlds", "0"),
                "read_state": state,
                "note": note,
            }
        )
    out.sort(key=lambda row: (row["read_state"], row["short_token"]))
    return out


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, str]]) -> None:
    counts = Counter(row["read_state"] for row in rows)
    lines = [
        "# MCM-Rollenwechsel-Memory Lesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest passive `dio_shift_*` Rollenwechsel-Memory gegen eine weitere Nicht-Bruecken-Landschaft.",
        "Geprueft wird, ob Rollenwechsel erneut sichtbar wird, dieselbe Zielrolle erreicht oder weiter umorganisiert.",
        "",
        "## Lesestatus",
        "",
        "| Status | Anzahl |",
        "|---|---:|",
    ]
    for state, count in counts.most_common():
        lines.append(f"| `{state}` | {count} |")

    lines.extend(
        [
            "",
            "## Token-Lesung",
            "",
            "| Token | Shift | vorher nach | jetzt | Beobachtungen | Welten | Lesung |",
            "|---|---|---|---|---:|---:|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['short_token']}` | `{row['shift_symbol']}` | `{row['previous_to_nonbridge_class']}` | `{row['current_nonbridge_class']}` / `{row['current_zone']}` | {row['current_observations']} | {row['current_worlds']} | `{row['read_state']}` |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "Wenn `dio_shift_*` erneut sichtbar wird, ist Rollenwechsel nicht nur ein einmaliger Befund der siebten Welt.",
            "Wenn Zielrollen reproduziert werden, kann Rollenwechsel selbst als passive Bedeutungsbewegung gelesen werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Lesung synthetisiert werden: Welche Rollenwechsel sind stabil, welche driften, welche verschwinden?",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory", required=True, type=Path)
    parser.add_argument("--nonbridge", required=True, type=Path)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = _build(_read(args.memory), _read(args.nonbridge))
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"rows={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
