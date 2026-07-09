from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


ASSETS = ("BTC", "SOL", "DOGE", "PAXG", "XRP", "KAS")


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _load_by_symbol(path: Path) -> dict[str, dict[str, str]]:
    return {row["preview_symbol"]: row for row in _load_csv(path) if row.get("preview_symbol")}


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


def _parse_counter_text(value: str) -> Counter[str]:
    counter: Counter[str] = Counter()
    for raw_part in str(value or "").split(";"):
        part = raw_part.strip()
        if not part or ":" not in part:
            continue
        key, raw_count = part.rsplit(":", 1)
        counter[key.strip()] += _safe_int(raw_count)
    return counter


def _asset_from_world(world: str) -> str:
    text = world.upper()
    for asset in ASSETS:
        if asset in text:
            return asset
    if "SYNTH" in text:
        return "SYNTH"
    if "NULL" in text or "SHUFFLE" in text or "RANDSIGN" in text:
        return "NULL"
    return "UNK"


def _segment_from_world(world: str) -> str:
    text = world.upper()
    if "LONG_REAL" in text:
        match = re.search(r"_(\d+K(?:_\d+K)?)$", text)
        if match:
            return match.group(1)
        return "LONG_REAL"
    if "MULTI_REAL" in text:
        match = re.search(r"_(\d+K(?:_\d+K)?)$", text)
        if match:
            return match.group(1)
        return "MULTI_REAL"
    for token in ("STRESS", "QUIET", "EXPANSION", "REAL", "5M", "1H"):
        if token in text:
            return token.lower()
    return "offen"


def _counter_summary(counter: Counter[str], limit: int = 6) -> str:
    if not counter:
        return "-"
    return ";".join(f"{key}:{count}" for key, count in counter.most_common(limit))


def _world_profile(row: dict[str, str]) -> dict[str, object]:
    worlds = _parse_counter_text(row.get("worlds", ""))
    assets: Counter[str] = Counter()
    segments: Counter[str] = Counter()
    for world, count in worlds.items():
        assets[_asset_from_world(world)] += count
        segments[_segment_from_world(world)] += count
    total = sum(worlds.values())
    top_asset, top_asset_count = assets.most_common(1)[0] if assets else ("-", 0)
    top_segment, top_segment_count = segments.most_common(1)[0] if segments else ("-", 0)
    return {
        "worlds": _counter_summary(worlds),
        "assets": _counter_summary(assets),
        "segments": _counter_summary(segments),
        "top_asset": top_asset,
        "top_asset_share": top_asset_count / max(1, total),
        "top_segment": top_segment,
        "top_segment_share": top_segment_count / max(1, total),
        "total": total,
    }


def _role_reading(functions: list[str], top_assets: list[str]) -> str:
    path = " -> ".join(functions)
    if functions == ["active_recoupling", "milieu_island", "active_recoupling"]:
        return "lange_btc_sol_welt_verdichtet_kurz_zu_milieu"
    if functions == ["milieu_island", "active_recoupling", "active_recoupling"]:
        return "breitere_realwelt_rekoppelt_fruehes_milieu_aktiv"
    if functions == ["milieu_island", "active_recoupling", "milieu_island"]:
        return "weltkoerper_wechsel_schiebt_zwischen_milieu_und_rekopplung"
    if functions == ["open_surface", "active_recoupling", "active_recoupling"]:
        return "offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd"
    if functions == ["active_recoupling", "active_recoupling", "milieu_island"]:
        return "multiasset_welt_bindet_rekopplung_zu_milieu"
    if functions == ["active_recoupling", "open_surface", "open_surface"]:
        return "lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche"
    if functions == ["milieu_island", "milieu_island", "active_recoupling"]:
        return "multiasset_welt_aktiviert_milieunahe_phase"
    if functions == ["open_surface", "open_surface", "active_recoupling"]:
        return "multiasset_welt_rekoppelt_offene_oberflaeche"
    if len(set(top_assets)) > 1:
        return f"assetwechsel_mit_rollenwechsel:{path}"
    return f"offener_rollenwechsel:{path}"


def _build_rows(
    shift_rows: list[dict[str, str]],
    labels: list[str],
    reports: dict[str, dict[str, dict[str, str]]],
) -> list[dict[str, object]]:
    out_rows: list[dict[str, object]] = []
    for shift in shift_rows:
        if shift.get("function_shift") != "1":
            continue
        symbol = shift["preview_symbol"]
        functions = [shift.get(f"{label}_function", "-") for label in labels]
        states = [shift.get(f"{label}_state", "-") for label in labels]
        depths = [_safe_float(shift.get(f"{label}_depth")) for label in labels]
        profiles = [_world_profile(reports[label][symbol]) for label in labels]
        top_assets = [str(profile["top_asset"]) for profile in profiles]
        row: dict[str, object] = {
            "preview_symbol": symbol,
            "shift_class": shift.get("shift_class", "-"),
            "state_path": " -> ".join(states),
            "function_path": " -> ".join(functions),
            "role_backread": _role_reading(functions, top_assets),
            "depth_path": " -> ".join(f"{value:.6f}" for value in depths),
            "depth_range": max(depths) - min(depths) if depths else 0.0,
        }
        for label, profile in zip(labels, profiles):
            row[f"{label}_worlds"] = profile["worlds"]
            row[f"{label}_assets"] = profile["assets"]
            row[f"{label}_segments"] = profile["segments"]
            row[f"{label}_top_asset"] = profile["top_asset"]
            row[f"{label}_top_asset_share"] = profile["top_asset_share"]
            row[f"{label}_top_segment"] = profile["top_segment"]
            row[f"{label}_top_segment_share"] = profile["top_segment_share"]
        out_rows.append(row)
    out_rows.sort(key=lambda row: (float(row["depth_range"]), str(row["preview_symbol"])), reverse=True)
    return out_rows


def _write_markdown(path: Path, rows: list[dict[str, object]], labels: list[str]) -> None:
    reading_counts = Counter(str(row["role_backread"]) for row in rows)
    function_paths = Counter(str(row["function_path"]) for row in rows)
    top_asset_paths = Counter(" -> ".join(str(row[f"{label}_top_asset"]) for label in labels) for row in rows)

    lines = [
        "# 2033 - Feldfunktionswechsel Rohwelt-Rücklesung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die Feldfunktionswechsel aus `2032` zurück in die tragenden Weltkörper.",
        "",
        "Sie prüft passiv, ob eine gleiche Feldsignatur ihre Rolle abhängig von Asset, Segment oder Weltkörper verschiebt.",
        "",
        "## Übersicht",
        "",
        f"- untersuchte Feldfunktionswechsel: `{len(rows)}`",
        "",
        "### Rollenlesung",
        "",
    ]
    for key, count in reading_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Feldfunktionspfade", ""])
    for key, count in function_paths.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Top-Asset-Pfade", ""])
    for key, count in top_asset_paths.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(
        [
            "",
            "## Einzelrücklesung",
            "",
            "| Signatur | Rollenlesung | Funktion | Zustand | Top-Assets | Tiefe |",
            "|---|---|---|---|---|---:|",
        ]
    )
    for row in rows:
        asset_path = " -> ".join(str(row[f"{label}_top_asset"]) for label in labels)
        lines.append(
            "| "
            f"`{row['preview_symbol']}` | "
            f"`{row['role_backread']}` | "
            f"`{row['function_path']}` | "
            f"`{row['state_path']}` | "
            f"`{asset_path}` | "
            f"`{row['depth_path']}` |"
        )

    lines.extend(["", "## Weltkörperdetails", ""])
    for row in rows:
        lines.extend(["", f"### `{row['preview_symbol']}`", ""])
        lines.append(f"- Rollenlesung: `{row['role_backread']}`")
        lines.append(f"- Funktion: `{row['function_path']}`")
        for label in labels:
            lines.append(
                f"- `{label}`: Top-Asset `{row.get(label + '_top_asset', '-')}`, Assets `{row.get(label + '_assets', '-')}`, Segmente `{row.get(label + '_segments', '-')}`"
            )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Der Feldfunktionswechsel ist kein Verschwinden der Signatur.",
            "",
            "Die Signatur bleibt im gemeinsamen Realwelt-Kern erhalten, aber ihre Einbindung verschiebt sich je nach Weltkörper.",
            "",
            "Damit wird die MCM-Topologie als dynamisches Bedeutungsnetz lesbar: Der Knoten bleibt, seine Rolle kann sich unter anderer Weltspannung verändern.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollten die stärksten Rollenwechsel mit Rohweltfenstern verglichen werden. Besonders relevant sind `active_recoupling -> open_surface` und `open_surface -> active_recoupling`, weil sie zeigen können, wann Weltkontakt öffnet oder rekoppelt.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shift-report", required=True)
    parser.add_argument("--report", action="append", required=True, help="Format: label=path")
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()

    labels: list[str] = []
    reports: dict[str, dict[str, dict[str, str]]] = {}
    for raw in args.report:
        if "=" not in raw:
            raise SystemExit(f"Ungültiges Report-Format: {raw}")
        label, path = raw.split("=", 1)
        label = label.strip()
        labels.append(label)
        reports[label] = _load_by_symbol(Path(path))

    shift_rows = _load_csv(Path(args.shift_report))
    rows = _build_rows(shift_rows, labels, reports)

    out_dir = Path("docs") / "befunde"
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    out_dir.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(rows[0].keys()) if rows else ["preview_symbol"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    _write_markdown(out_md, rows, labels)
    print(f"function_shift_rows={len(rows)}")
    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
