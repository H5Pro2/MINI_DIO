from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _load_csv(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {str(row.get("preview_symbol") or ""): row for row in csv.DictReader(handle) if row.get("preview_symbol")}


def _float(row: dict[str, str] | None, key: str) -> float:
    if not row:
        return 0.0
    try:
        value = float(row.get(key) or 0.0)
    except Exception:
        return 0.0
    return 0.0 if value != value else value


def _value(row: dict[str, str] | None, key: str) -> str:
    if not row:
        return "-"
    return str(row.get(key) or "-")


def _sequence(values: list[str]) -> str:
    return " -> ".join(values)


def _changed(values: list[str]) -> bool:
    cleaned = [value for value in values if value != "-"]
    return len(set(cleaned)) > 1


def _classify(state_shift: bool, function_shift: bool, variant_shift: bool, depth_range: float) -> str:
    if state_shift and function_shift:
        return "zustand_und_funktion_verschoben"
    if state_shift:
        return "zustand_reift_oder_kippt"
    if function_shift:
        return "funktion_verschoben"
    if variant_shift:
        return "variante_verschoben"
    if depth_range >= 0.08:
        return "tiefe_deutlich_bewegt"
    return "funktion_stabil"


def _row(symbol: str, labels: list[str], rows: list[dict[str, str]]) -> dict[str, object]:
    states = [_value(row, "phase_quality_state") for row in rows]
    origins = [_value(row, "origin_quality") for row in rows]
    functions = [_value(row, "dominant_field_function") for row in rows]
    variants = [_value(row, "dominant_field_variant") for row in rows]
    bindings = [_value(row, "dominant_world_binding") for row in rows]
    depths = [_float(row, "phase_quality_depth") for row in rows]
    drifts = [_float(row, "avg_phase_drift") for row in rows]
    counts = [int(_float(row, "count")) for row in rows]
    worlds = [int(_float(row, "world_count")) for row in rows]

    state_shift = _changed(states)
    function_shift = _changed(functions)
    variant_shift = _changed(variants)
    depth_range = max(depths) - min(depths) if depths else 0.0

    output: dict[str, object] = {
        "preview_symbol": symbol,
        "shift_class": _classify(state_shift, function_shift, variant_shift, depth_range),
        "state_shift": int(state_shift),
        "function_shift": int(function_shift),
        "variant_shift": int(variant_shift),
        "state_path": _sequence(states),
        "origin_path": _sequence(origins),
        "function_path": _sequence(functions),
        "variant_path": _sequence(variants),
        "binding_path": _sequence(bindings),
        "depth_path": _sequence([f"{value:.6f}" for value in depths]),
        "drift_path": _sequence([f"{value:.6f}" for value in drifts]),
        "count_path": _sequence([str(value) for value in counts]),
        "world_count_path": _sequence([str(value) for value in worlds]),
        "depth_range": depth_range,
        "max_depth": max(depths) if depths else 0.0,
        "min_depth": min(depths) if depths else 0.0,
    }

    for label, row in zip(labels, rows):
        output[f"{label}_state"] = _value(row, "phase_quality_state")
        output[f"{label}_origin"] = _value(row, "origin_quality")
        output[f"{label}_function"] = _value(row, "dominant_field_function")
        output[f"{label}_variant"] = _value(row, "dominant_field_variant")
        output[f"{label}_depth"] = _float(row, "phase_quality_depth")
        output[f"{label}_drift"] = _float(row, "avg_phase_drift")
        output[f"{label}_count"] = int(_float(row, "count"))
        output[f"{label}_world_count"] = int(_float(row, "world_count"))
    return output


def _write_markdown(path: Path, rows: list[dict[str, object]], title: str, labels: list[str]) -> None:
    class_counts = Counter(str(row["shift_class"]) for row in rows)
    function_paths = Counter(str(row["function_path"]) for row in rows)
    state_paths = Counter(str(row["state_path"]) for row in rows)
    origin_paths = Counter(str(row["origin_path"]) for row in rows)

    function_shift_rows = [row for row in rows if int(row["function_shift"])]
    state_shift_rows = [row for row in rows if int(row["state_shift"])]
    stable_rows = [row for row in rows if row["shift_class"] == "funktion_stabil"]

    def by_depth(items: list[dict[str, object]], limit: int = 16) -> list[dict[str, object]]:
        return sorted(items, key=lambda row: (float(row["max_depth"]), float(row["depth_range"])), reverse=True)[:limit]

    lines = [
        f"# {title}",
        "",
        "## Zweck",
        "",
        "Dieser Bericht vergleicht dieselben Feldphasen-Signaturen über mehrere reale Weltketten.",
        "",
        "Geprüft wird nicht, ob eine Signatur nur wiederkehrt, sondern ob sie ihre Feldfunktion hält oder je nach Weltkörper eine andere Rolle annimmt.",
        "",
        "Verglichene Ketten:",
        "",
    ]
    for label in labels:
        lines.append(f"- `{label}`")

    lines.extend(
        [
            "",
            "## Übersicht",
            "",
            f"- gemeinsamer Realwelt-Kern: `{len(rows)}` Signaturen",
            f"- Signaturen mit Feldfunktionswechsel: `{len(function_shift_rows)}`",
            f"- Signaturen mit Zustandswechsel: `{len(state_shift_rows)}`",
            "",
            "### Wechselklassen",
            "",
        ]
    )
    for key, count in class_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Häufigste Feldfunktionspfade", ""])
    for key, count in function_paths.most_common(12):
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Häufigste Zustandspfade", ""])
    for key, count in state_paths.most_common(10):
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Häufigste Herkunftspfade", ""])
    for key, count in origin_paths.most_common(10):
        lines.append(f"- `{key}`: `{count}`")

    sections = [
        ("Feldfunktionswechsel", by_depth(function_shift_rows)),
        ("Zustandswechsel", by_depth(state_shift_rows)),
        ("Stabile Kernsignaturen", by_depth(stable_rows)),
    ]
    for heading, items in sections:
        lines.extend(["", f"## {heading}", ""])
        if not items:
            lines.append("- keine Signaturen in dieser Klasse")
            continue
        lines.append("| Signatur | Klasse | Zustandspfad | Funktionspfad | Tiefe | Drift |")
        lines.append("|---|---|---|---|---:|---:|")
        for row in items:
            lines.append(
                "| "
                f"`{row['preview_symbol']}` | "
                f"`{row['shift_class']}` | "
                f"`{row['state_path']}` | "
                f"`{row['function_path']}` | "
                f"`{row['depth_path']}` | "
                f"`{row['drift_path']}` |"
            )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der gemeinsame Realwelt-Kern bleibt nicht nur als Symbolmenge interessant. Entscheidend ist, ob eine Signatur über verschiedene Weltkörper dieselbe Feldrolle trägt oder ihre Rolle verschiebt.",
            "",
            "Ein stabiler Funktionspfad spricht für eine robuste Kernrolle. Ein Feldfunktionswechsel spricht dagegen für eine Signatur, die nicht verschwindet, sondern je nach Weltspannung anders eingebunden wird.",
            "",
            "Damit wird die Topologie nicht als starre Karte gelesen, sondern als dynamisches Bedeutungsnetz: gleiche Signatur, mögliche andere Rolle.",
            "",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", required=True, help="Format: label=path")
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()

    labels: list[str] = []
    reports: list[dict[str, dict[str, str]]] = []
    for raw in args.input:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Input-Format: {raw}")
        label, path = raw.split("=", 1)
        label = label.strip()
        if not label:
            raise SystemExit(f"Leeres Label: {raw}")
        labels.append(label)
        reports.append(_load_csv(Path(path)))

    if len(reports) < 2:
        raise SystemExit("Mindestens zwei Inputs nötig.")

    common_symbols = sorted(set.intersection(*(set(report) for report in reports)))
    rows = [_row(symbol, labels, [report[symbol] for report in reports]) for symbol in common_symbols]
    rows.sort(
        key=lambda row: (
            int(row["function_shift"]),
            int(row["state_shift"]),
            float(row["max_depth"]),
            float(row["depth_range"]),
        ),
        reverse=True,
    )

    out_dir = Path("docs") / "befunde"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    fieldnames = list(rows[0].keys()) if rows else ["preview_symbol"]
    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _write_markdown(out_md, rows, f"{args.out_prefix} - Feldfunktionswechsel im Realwelt-Kern", labels)
    print(f"common_symbols={len(common_symbols)}")
    print(f"function_shift={sum(int(row['function_shift']) for row in rows)}")
    print(f"state_shift={sum(int(row['state_shift']) for row in rows)}")
    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
