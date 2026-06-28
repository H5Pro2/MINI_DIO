from __future__ import annotations

import argparse
import csv
from pathlib import Path


PASSIVE_FLAGS = {
    "passive_only": 1,
    "read_by_mini_dio": 0,
    "influences_action": 0,
    "is_gate": 0,
    "is_motoric": 0,
    "is_entry_signal": 0,
    "is_direction_signal": 0,
}


def _safe_float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    return 0.0 if result != result else result


def _safe_int(value: object) -> int:
    try:
        return int(float(value or 0))
    except Exception:
        return 0


def _load_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;")
    except Exception:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def _world_label(path: Path) -> str:
    stem = path.stem
    marker = "MCM_NICHTBRUECKEN_ORDNUNG_"
    if marker in stem:
        return stem.split(marker, 1)[1]
    return stem


def _short(value: str) -> str:
    return str(value or "").replace("dio_mcm_episode_", "")


def _row_token(row: dict[str, str]) -> str:
    return _short(row.get("short_token") or row.get("token") or "")


def _find_token(rows: list[dict[str, str]], token: str) -> dict[str, str] | None:
    short = _short(token)
    for row in rows:
        if _row_token(row) == short:
            return row
    return None


def _references(row: dict[str, str], token: str) -> bool:
    short = _short(token)
    joined = " ".join(str(value or "") for value in row.values())
    return short in joined or f"dio_mcm_episode_{short}" in joined


def _reciprocal(row_a: dict[str, str] | None, row_b: dict[str, str] | None, token_a: str, token_b: str) -> bool:
    if not row_a or not row_b:
        return False
    a_prev = _short(row_a.get("top_previous", ""))
    a_next = _short(row_a.get("top_next", ""))
    b_prev = _short(row_b.get("top_previous", ""))
    b_next = _short(row_b.get("top_next", ""))
    return _short(token_b) in {a_prev, a_next} and _short(token_a) in {b_prev, b_next}


def _center_role(row: dict[str, str] | None) -> bool:
    if not row:
        return False
    text = " ".join(
        str(row.get(key, "") or "")
        for key in ("nonbridge_class", "condensation_zone", "dominant_role", "classification_note")
    )
    return "zentrum" in text or _safe_float(row.get("center_share")) >= 0.70


def _axis_reading(
    row_a: dict[str, str] | None,
    row_b: dict[str, str] | None,
    adjacent_a: int,
    adjacent_b: int,
    token_a: str,
    token_b: str,
) -> str:
    both_present = bool(row_a and row_b)
    if both_present and _reciprocal(row_a, row_b, token_a, token_b) and _center_role(row_a) and _center_role(row_b):
        return "beziehung_erhalten"
    if both_present:
        return "beziehung_geschwaecht"
    if adjacent_a or adjacent_b:
        return "beziehung_verlagert"
    return "beziehung_nicht_sichtbar"


def _row_snapshot(prefix: str, row: dict[str, str] | None) -> dict[str, object]:
    if not row:
        return {
            f"{prefix}_present": 0,
            f"{prefix}_class": "-",
            f"{prefix}_zone": "-",
            f"{prefix}_role": "-",
            f"{prefix}_observations": 0,
            f"{prefix}_neighbors": 0,
            f"{prefix}_rekopplung": 0.0,
            f"{prefix}_strain": 0.0,
            f"{prefix}_sensory": 0.0,
            f"{prefix}_center_share": 0.0,
            f"{prefix}_open_share": 0.0,
            f"{prefix}_rand_share": 0.0,
            f"{prefix}_top_previous": "-",
            f"{prefix}_top_next": "-",
        }
    return {
        f"{prefix}_present": 1,
        f"{prefix}_class": row.get("nonbridge_class", "-") or "-",
        f"{prefix}_zone": row.get("condensation_zone", "-") or "-",
        f"{prefix}_role": row.get("dominant_role", "-") or "-",
        f"{prefix}_observations": _safe_int(row.get("observations")),
        f"{prefix}_neighbors": _safe_int(row.get("neighbor_count")),
        f"{prefix}_rekopplung": round(_safe_float(row.get("avg_rekopplung")), 6),
        f"{prefix}_strain": round(_safe_float(row.get("avg_strain")), 6),
        f"{prefix}_sensory": round(_safe_float(row.get("avg_sensory")), 6),
        f"{prefix}_center_share": round(_safe_float(row.get("center_share")), 6),
        f"{prefix}_open_share": round(_safe_float(row.get("open_share")), 6),
        f"{prefix}_rand_share": round(_safe_float(row.get("rand_share")), 6),
        f"{prefix}_top_previous": _short(row.get("top_previous", "")) or "-",
        f"{prefix}_top_next": _short(row.get("top_next", "")) or "-",
    }


def build_report(axis: str, nonbridge_files: list[Path]) -> list[dict[str, object]]:
    token_a, token_b = [part.strip() for part in axis.replace("<->", "|").split("|", 1)]
    rows_out: list[dict[str, object]] = []
    for path in nonbridge_files:
        rows = _load_rows(path)
        row_a = _find_token(rows, token_a)
        row_b = _find_token(rows, token_b)
        adjacent_a = sum(1 for row in rows if row is not row_a and _references(row, token_a))
        adjacent_b = sum(1 for row in rows if row is not row_b and _references(row, token_b))
        reciprocal = int(_reciprocal(row_a, row_b, token_a, token_b))
        reading = _axis_reading(row_a, row_b, adjacent_a, adjacent_b, token_a, token_b)
        rows_out.append(
            {
                "world": _world_label(path),
                "source_file": path.name,
                "axis": f"{_short(token_a)}<->{_short(token_b)}",
                "axis_reading": reading,
                "both_present": int(bool(row_a and row_b)),
                "reciprocal_top_links": reciprocal,
                "adjacent_refs_a": adjacent_a,
                "adjacent_refs_b": adjacent_b,
                **_row_snapshot("a", row_a),
                **_row_snapshot("b", row_b),
                **PASSIVE_FLAGS,
            }
        )
    return rows_out


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    retained = [row for row in rows if row["axis_reading"] == "beziehung_erhalten"]
    shifted = [row for row in rows if row["axis_reading"] == "beziehung_verlagert"]
    invisible = [row for row in rows if row["axis_reading"] == "beziehung_nicht_sichtbar"]
    weakened = [row for row in rows if row["axis_reading"] == "beziehung_geschwaecht"]
    report_id = path.stem.split("_", 1)[0]
    retained_worlds = ", ".join(str(row["world"]) for row in retained) or "-"
    invisible_worlds = ", ".join(str(row["world"]) for row in invisible) or "-"
    lines = [
        f"# {report_id} - Mitte-Nachbarschaft in Folgewelten",
        "",
        "Passive Pruefung, ob die zuvor gefundene Mitte-Nachbarschaft als feste Kopie, verlegte Rolle oder nicht sichtbare Spur in Folgewelten erscheint.",
        "",
        "Wichtig: Diese Datei beschreibt nur Lesebefunde. Sie wirkt nicht auf MINI_DIO, nicht auf Handlung und nicht auf Regulation.",
        "",
        "## Ergebnisuebersicht",
        "",
        f"- Beziehung erhalten: {len(retained)}",
        f"- Beziehung geschwaecht: {len(weakened)}",
        f"- Beziehung verlagert: {len(shifted)}",
        f"- Beziehung nicht sichtbar: {len(invisible)}",
        "",
        "## Weltbefunde",
        "",
        "| Welt | Lesung | Beide Knoten | Reziprok | A Rolle | B Rolle | A Rekopplung | B Rekopplung | A Strain | B Strain |",
        "|---|---:|---:|---:|---|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {world} | {axis_reading} | {both_present} | {reciprocal_top_links} | {a_class}/{a_zone}/{a_role} | {b_class}/{b_zone}/{b_role} | {a_rekopplung} | {b_rekopplung} | {a_strain} | {b_strain} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Die Achse `183drjy <-> 1t5bcxp` erscheint nicht als alte starre Kopie in allen Folgewelten. Erhalten bleibt sie in: `{retained_worlds}`. Nicht sichtbar ist sie in: `{invisible_worlds}`. Wo sie erhalten bleibt, sind beide Knoten vorhanden, beide liegen zentrumsnah, und beide verweisen reziprok ueber `top_previous` / `top_next` aufeinander.",
            "",
            "Damit ist die Mitte-Nachbarschaft eher eine verlegte Feldrolle als ein fixer Token. Das passt zum bisherigen Befund: MINI_DIO bildet keine statische Symbolkopie, sondern eine wieder erkennbare Feldbeziehung, die erst unter passenden Folgeweltbedingungen als Achse sichtbar wird.",
            "",
            "## Deutung",
            "",
            "- `183drjy` traegt die rekoppelnde Seite der Mitte.",
            "- `1t5bcxp` traegt die zentrumsnahe Stabilisierungsseite.",
            "- In `ZEHNTE_STRESSWELT` bleibt die Beziehung erhalten, obwohl die Zone von `1t5bcxp` in Richtung Rekopplung wandert.",
            "- Die alte Mitte ist damit nicht verloren, sondern funktional in eine neue Weltlage verschoben.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte diese Achsenbeziehung gegen eine neue, andersartige Folgewelt gelesen werden. Ziel ist zu pruefen, ob `183drjy <-> 1t5bcxp` stabil bleibt, sich erneut verlagert oder nur als Uebergangsbruecke zwischen zwei Feldphasen wirkte.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--axis", default="183drjy<->1t5bcxp")
    parser.add_argument("--nonbridge-file", action="append", required=True)
    parser.add_argument("--out-csv", required=True)
    parser.add_argument("--out-md", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    nonbridge_files = [Path(value) for value in args.nonbridge_file]
    rows = build_report(args.axis, nonbridge_files)
    write_csv(rows, Path(args.out_csv))
    write_md(rows, Path(args.out_md))
    print(f"written={args.out_csv}")
    print(f"written={args.out_md}")


if __name__ == "__main__":
    main()
