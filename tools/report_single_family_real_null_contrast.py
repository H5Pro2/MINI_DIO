from __future__ import annotations

import argparse
import csv
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
BEFUNDE = befunde_root(ROOT)


def _load_csv(path: Path) -> list[dict[str, str]]:
    path = path if path.is_absolute() else ROOT / path
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _fmt(value: float) -> str:
    return f"{value:.6f}"


def _summary_row(label: str, family: str, summary_path: Path, families_path: Path) -> dict[str, object]:
    summary = next((row for row in _load_csv(summary_path) if row.get("symbol_family") == family), {})
    all_rows = _load_csv(families_path)
    total_events = sum(_safe_int(row.get("events")) for row in all_rows)
    family_events = _safe_int(summary.get("total_events"))
    event_share = family_events / max(1, total_events)
    return {
        "raum": label,
        "symbol_family": family,
        "role_status": summary.get("role_status", "nicht_wiedergefunden"),
        "worlds": _safe_int(summary.get("worlds")),
        "family_events": family_events,
        "total_events": total_events,
        "event_share": event_share,
        "fields": summary.get("fields", "-"),
        "bridge_reifung": summary.get("bridge_reifung", "-"),
        "bridge_mcm": summary.get("bridge_mcm", "-"),
    }


def _write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            out = dict(row)
            out["event_share"] = _fmt(_safe_float(out.get("event_share")))
            writer.writerow({field: out.get(field, "") for field in fieldnames})


def _md_table(rows: list[dict[str, object]], fields: list[str]) -> list[str]:
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        out = dict(row)
        out["event_share"] = _fmt(_safe_float(out.get("event_share")))
        lines.append("| " + " | ".join(str(out.get(field, "")) for field in fields) + " |")
    return lines


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    real = next(row for row in rows if row["raum"] == "real_multi_asset")
    null = next(row for row in rows if row["raum"] == "null_shuffle")
    real_share = _safe_float(real["event_share"])
    null_share = _safe_float(null["event_share"])
    ratio = real_share / null_share if null_share > 0 else 0.0
    lines = [
        "# 2061 - Real-/Null-Kontrast einer isolierten Feldrolle",
        "",
        "## Zweck",
        "",
        "Diese Auswertung vergleicht `dio_17j2` zwischen realen Multi-Asset-Welten und Null-/Shuffle-Welten.",
        "",
        "Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.",
        "",
        "## Übersicht",
        "",
    ]
    lines.extend(
        _md_table(
            rows,
            [
                "raum",
                "role_status",
                "worlds",
                "family_events",
                "total_events",
                "event_share",
                "fields",
                "bridge_reifung",
                "bridge_mcm",
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Lesung",
            "",
            f"- Realer Ereignisanteil: `{_fmt(real_share)}`",
            f"- Null-/Shuffle-Ereignisanteil: `{_fmt(null_share)}`",
            f"- Verhältnis Real zu Null/Shuffle: `{ratio:.3f}`",
            "",
            "`dio_17j2` ist damit nicht exklusiv an reale Weltsequenzen gebunden. Die Rolle taucht auch in entkoppelten Null-/Shuffle-Räumen auf, aber im geprüften Stand schwächer.",
            "",
            "Das spricht nicht gegen die Rolle, sondern präzisiert sie: Sie ist wahrscheinlich eine feldnahe Grundform, die durch reale Weltordnung stärker aktiviert wird, aber nicht vollständig von Realordnung abhängig ist.",
            "",
            "## Grenze",
            "",
            "Das ist kein Beweis für Bedeutung und kein Handlungsargument. Es ist eine passive Kontrastmessung zwischen realer Weltkopplung und entkoppeltem Kontrollraum.",
            "",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", default="dio_17j2")
    parser.add_argument("--out-prefix", default="2061_DIO17J2_REAL_NULL_KONTRAST")
    parser.add_argument("--real-summary", default="docs/befunde/2001-3000/2058_DIO17J2_EINZELROLLE_MULTI_ASSET.summary.csv")
    parser.add_argument("--real-families", default="docs/befunde/2001-3000/2057_MULTI_ASSET_FELDKLASSEN_ZU_SYNTAXNAEHE.families.csv")
    parser.add_argument("--null-summary", default="docs/befunde/2001-3000/2060_DIO17J2_NULL_SHUFFLE_GEGENPRUEFUNG.summary.csv")
    parser.add_argument("--null-families", default="docs/befunde/2001-3000/2059_NULL_SHUFFLE_FELDKLASSEN_ZU_SYNTAXNAEHE.families.csv")
    args = parser.parse_args()

    rows = [
        _summary_row("real_multi_asset", args.family, Path(args.real_summary), Path(args.real_families)),
        _summary_row("null_shuffle", args.family, Path(args.null_summary), Path(args.null_families)),
    ]
    fields = [
        "raum",
        "symbol_family",
        "role_status",
        "worlds",
        "family_events",
        "total_events",
        "event_share",
        "fields",
        "bridge_reifung",
        "bridge_mcm",
    ]
    _write_csv(BEFUNDE / f"{args.out_prefix}.csv", rows, fields)
    _write_markdown(BEFUNDE / f"{args.out_prefix}.md", rows)
    print(f"family={args.family}")
    print(f"real_share={_fmt(_safe_float(rows[0]['event_share']))}")
    print(f"null_share={_fmt(_safe_float(rows[1]['event_share']))}")
    print(f"wrote={BEFUNDE / (args.out_prefix + '.md')}")


if __name__ == "__main__":
    main()
