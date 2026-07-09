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


def _shift_label(real: dict[str, str] | None, shuffle: dict[str, str] | None, random_sign: dict[str, str] | None) -> str:
    real_origin = _value(real, "origin_quality")
    shuffle_origin = _value(shuffle, "origin_quality")
    random_origin = _value(random_sign, "origin_quality")
    if real_origin == "realwelt_getragen" and shuffle_origin == "realwelt_getragen" and random_origin == "realwelt_getragen":
        return "realwelt_stabil"
    if real_origin == "realwelt_getragen" and "feldinterne_nullordnung" in {shuffle_origin, random_origin}:
        return "kippt_zu_feldintern"
    if real_origin == "realwelt_getragen" and "gemischte_bindung" in {shuffle_origin, random_origin}:
        return "kippt_zu_gemischt"
    if real_origin == "-" and (shuffle_origin != "-" or random_origin != "-"):
        return "nur_stoerketten_sichtbar"
    if real_origin != "-" and shuffle_origin == "-" and random_origin == "-":
        return "nur_real_sichtbar"
    return "offener_wechsel"


def _row(symbol: str, real: dict[str, str] | None, shuffle: dict[str, str] | None, random_sign: dict[str, str] | None) -> dict[str, object]:
    return {
        "preview_symbol": symbol,
        "shift_label": _shift_label(real, shuffle, random_sign),
        "real_origin": _value(real, "origin_quality"),
        "shuffle_origin": _value(shuffle, "origin_quality"),
        "random_sign_origin": _value(random_sign, "origin_quality"),
        "real_state": _value(real, "phase_quality_state"),
        "shuffle_state": _value(shuffle, "phase_quality_state"),
        "random_sign_state": _value(random_sign, "phase_quality_state"),
        "real_function": _value(real, "dominant_field_function"),
        "shuffle_function": _value(shuffle, "dominant_field_function"),
        "random_sign_function": _value(random_sign, "dominant_field_function"),
        "real_depth": _float(real, "phase_quality_depth"),
        "shuffle_depth": _float(shuffle, "phase_quality_depth"),
        "random_sign_depth": _float(random_sign, "phase_quality_depth"),
        "real_null_share": _float(real, "null_share"),
        "shuffle_null_share": _float(shuffle, "null_share"),
        "random_sign_null_share": _float(random_sign, "null_share"),
        "real_mixed_share": _float(real, "mixed_binding_share"),
        "shuffle_mixed_share": _float(shuffle, "mixed_binding_share"),
        "random_sign_mixed_share": _float(random_sign, "mixed_binding_share"),
        "real_count": int(float(_value(real, "count") if real else 0) or 0),
        "shuffle_count": int(float(_value(shuffle, "count") if shuffle else 0) or 0),
        "random_sign_count": int(float(_value(random_sign, "count") if random_sign else 0) or 0),
    }


def _write_markdown(path: Path, rows: list[dict[str, object]], title: str) -> None:
    shift_counts = Counter(str(row["shift_label"]) for row in rows)
    function_counts = Counter(str(row["real_function"]) for row in rows if row["real_function"] != "-")
    stable_rows = [row for row in rows if row["shift_label"] == "realwelt_stabil"]
    mixed_rows = [row for row in rows if row["shift_label"] == "kippt_zu_gemischt"]
    internal_rows = [row for row in rows if row["shift_label"] == "kippt_zu_feldintern"]

    def top(items: list[dict[str, object]]) -> list[dict[str, object]]:
        return sorted(
            items,
            key=lambda row: (
                float(row["real_depth"]),
                float(row["shuffle_depth"]),
                float(row["random_sign_depth"]),
                int(row["real_count"]),
            ),
            reverse=True,
        )[:20]

    lines = [
        f"# {title}",
        "",
        "## Zweck",
        "",
        "Dieser Bericht vergleicht die Herkunftsqualität derselben Feldphasen-Signaturen über drei Ketten:",
        "",
        "- reale Folgewelten",
        "- Shuffle-Nullwelten",
        "- Random-Sign-Nullwelten",
        "",
        "Damit wird geprüft, ob eine Signatur realweltgetragen bleibt oder unter Störung in gemischte beziehungsweise feldinterne Ordnung kippt.",
        "",
        "## Übersicht",
        "",
        f"- geprüfte Signaturen: `{len(rows)}`",
        "",
        "### Wechselklassen",
        "",
    ]
    for key, count in shift_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "### Realwelt-Feldfunktionen", ""])
    for key, count in function_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    sections = [
        ("Realweltstabil", top(stable_rows)),
        ("Kippt zu gemischt", top(mixed_rows)),
        ("Kippt zu feldintern", top(internal_rows)),
    ]
    for heading, items in sections:
        lines.extend(["", f"## {heading}", ""])
        if not items:
            lines.append("- keine Top-Signaturen in dieser Klasse")
            continue
        lines.append("| Signatur | Real | Shuffle | Random | Tiefe real/shuffle/random | Null shuffle/random |")
        lines.append("|---|---|---|---|---:|---:|")
        for row in items[:12]:
            lines.append(
                "| "
                f"`{row['preview_symbol']}` | "
                f"`{row['real_origin']}` | "
                f"`{row['shuffle_origin']}` | "
                f"`{row['random_sign_origin']}` | "
                f"{float(row['real_depth']):.3f}/{float(row['shuffle_depth']):.3f}/{float(row['random_sign_depth']):.3f} | "
                f"{float(row['shuffle_null_share']):.3f}/{float(row['random_sign_null_share']):.3f} |"
            )

    lines.extend(
        [
            "",
            "## Lesung",
            "",
            "Die Herkunftsqualität macht sichtbar, dass Tiefe allein nicht genügt.",
            "",
            "Eine Signatur kann tief, häufig und stabil wirken, aber unter Störung eine andere Herkunft zeigen. Das ist für MINI_DIO wichtig, weil es zwischen realweltgetragener Wiederkehr und feldinterner Ordnung unterscheiden muss.",
            "",
            "## Wie es weitergeht",
            "",
            "Als nächstes sollte dieser Vergleich mit längeren realen Weltketten wiederholt werden. Entscheidend ist, ob realweltstabile Signaturen bei mehr Außenwelt stabil bleiben oder ob neue gemischte Übergangsklassen entstehen.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", required=True)
    parser.add_argument("--shuffle", required=True)
    parser.add_argument("--random-sign", required=True)
    parser.add_argument("--out-prefix", required=True)
    args = parser.parse_args()

    real = _load_csv(Path(args.real))
    shuffle = _load_csv(Path(args.shuffle))
    random_sign = _load_csv(Path(args.random_sign))
    symbols = sorted(set(real) | set(shuffle) | set(random_sign))
    rows = [_row(symbol, real.get(symbol), shuffle.get(symbol), random_sign.get(symbol)) for symbol in symbols]

    rows.sort(
        key=lambda row: (
            str(row["shift_label"]),
            float(row["real_depth"]),
            float(row["shuffle_depth"]),
            float(row["random_sign_depth"]),
        ),
        reverse=True,
    )

    out_dir = Path("docs") / "befunde"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / f"{args.out_prefix}.csv"
    out_md = out_dir / f"{args.out_prefix}.md"

    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else ["preview_symbol"])
        writer.writeheader()
        writer.writerows(rows)

    _write_markdown(out_md, rows, f"{args.out_prefix} - Herkunftsdiagnose-Kettenvergleich")
    print(f"wrote={out_csv}")
    print(f"wrote={out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
