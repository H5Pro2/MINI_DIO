from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import fmean, pstdev


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = ROOT / "docs" / "befunde" / "337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv"
DEFAULT_OUT = ROOT / "docs" / "befunde" / "338_KONTAKTMILIEU_WIEDERKEHR_DRIFT.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


def _float(value: object) -> float:
    try:
        result = float(value or 0.0)
    except Exception:
        return 0.0
    if result != result:
        return 0.0
    return result


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _mean(values: list[float]) -> float:
    return fmean(values) if values else 0.0


def _std(values: list[float]) -> float:
    return pstdev(values) if len(values) > 1 else 0.0


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _signature(row: dict[str, str]) -> str:
    return "->".join(
        [
            row.get("before_class", "-") or "-",
            row.get("switch_class", "-") or "-",
            row.get("after_class", "-") or "-",
        ]
    )


def _drift_label(dominant_share: float, worlds: int, pressure_std: float, rekopplung_std: float) -> str:
    if worlds >= 4 and dominant_share >= 0.55 and pressure_std <= 0.07 and rekopplung_std <= 0.04:
        return "wiederkehrend_stabil"
    if worlds >= 3 and dominant_share >= 0.40:
        return "wiederkehrend_variabel"
    if pressure_std > 0.10 or rekopplung_std > 0.06:
        return "driftend"
    return "lokal_offen"


def _summarize(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("pair", "-") or "-"].append(row)

    pair_rows: list[dict[str, object]] = []
    signature_rows: list[dict[str, object]] = []
    for pair, items in sorted(grouped.items(), key=lambda entry: len(entry[1]), reverse=True):
        signatures = Counter(_signature(item) for item in items)
        top_signature, top_count = signatures.most_common(1)[0]
        pressure_values = [_float(item.get("pressure_delta")) for item in items]
        rekopplung_values = [_float(item.get("rekopplung_delta")) for item in items]
        worlds = len({item.get("world", "-") or "-" for item in items})
        dominant_share = top_count / max(1, len(items))
        pressure_std = _std(pressure_values)
        rekopplung_std = _std(rekopplung_values)
        pair_rows.append(
            {
                "pair": pair,
                "events": len(items),
                "worlds": worlds,
                "signature_count": len(signatures),
                "top_signature": top_signature,
                "top_signature_share": dominant_share,
                "pressure_delta": _mean(pressure_values),
                "pressure_std": pressure_std,
                "rekopplung_delta": _mean(rekopplung_values),
                "rekopplung_std": rekopplung_std,
                "drift_label": _drift_label(dominant_share, worlds, pressure_std, rekopplung_std),
            }
        )

        for signature, count in signatures.most_common():
            sig_items = [item for item in items if _signature(item) == signature]
            signature_rows.append(
                {
                    "pair": pair,
                    "signature": signature,
                    "events": count,
                    "worlds": len({item.get("world", "-") or "-" for item in sig_items}),
                    "share": count / max(1, len(items)),
                    "pressure_delta": _mean([_float(item.get("pressure_delta")) for item in sig_items]),
                    "rekopplung_delta": _mean([_float(item.get("rekopplung_delta")) for item in sig_items]),
                }
            )
    return pair_rows, signature_rows


def _write_csv(pair_rows: list[dict[str, object]], signature_rows: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pair_path = out_path.with_suffix(".csv")
    pair_fields = [
        "pair",
        "events",
        "worlds",
        "signature_count",
        "top_signature",
        "top_signature_share",
        "pressure_delta",
        "pressure_std",
        "rekopplung_delta",
        "rekopplung_std",
        "drift_label",
    ]
    with pair_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=pair_fields)
        writer.writeheader()
        for row in pair_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in pair_fields})

    sig_path = out_path.with_name(out_path.stem + "_signaturen.csv")
    sig_fields = ["pair", "signature", "events", "worlds", "share", "pressure_delta", "rekopplung_delta"]
    with sig_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=sig_fields)
        writer.writeheader()
        for row in signature_rows:
            writer.writerow({key: _fmt(float(row[key]), 6) if isinstance(row.get(key), float) else row.get(key, "") for key in sig_fields})


def _write_md(pair_rows: list[dict[str, object]], signature_rows: list[dict[str, object]], out_path: Path) -> None:
    _write_csv(pair_rows, signature_rows, out_path)
    lines = [
        "# Kontaktmilieu Wiederkehr Und Drift",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die Kontaktmilieus um passive Feldbewegungen wiederkehren oder pro Welt driften.",
        "Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.",
        "",
        "## Hierarchie",
        "",
        "1. Grundfrage: Traegt dieselbe Feldbewegung ein wiederkehrendes Kontaktmilieu?",
        "2. Unterpruefung: Vorher-Wechsel-Nachher-Signaturen pro Paar und Welt vergleichen.",
        "3. Folgeschritt: stabile Milieus als passive Ausloesemilieus beobachten, nicht als Regeln verwenden.",
        "",
        "## Paaruebersicht",
        "",
        "| Paar | Events | Welten | Signaturen | Top-Signatur | Anteil | dDruck | Druck-Streuung | dRekopplung | Rekopplung-Streuung | Driftlabel |",
        "|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in pair_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["events"]),
                    str(row["worlds"]),
                    str(row["signature_count"]),
                    str(row["top_signature"]),
                    _fmt(float(row["top_signature_share"])),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["pressure_std"])),
                    _fmt(float(row["rekopplung_delta"])),
                    _fmt(float(row["rekopplung_std"])),
                    str(row["drift_label"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Signaturdetails",
            "",
            "| Paar | Signatur | Events | Welten | Anteil | dDruck | dRekopplung |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in signature_rows[:80]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["pair"]),
                    str(row["signature"]),
                    str(row["events"]),
                    str(row["worlds"]),
                    _fmt(float(row["share"])),
                    _fmt(float(row["pressure_delta"])),
                    _fmt(float(row["rekopplung_delta"])),
                ]
            )
            + " |"
        )

    stable = [row for row in pair_rows if row["drift_label"] == "wiederkehrend_stabil"]
    variable = [row for row in pair_rows if row["drift_label"] == "wiederkehrend_variabel"]
    lines.extend(
        [
            "",
            "## Befund",
            "",
            f"Stabile Milieus: {len(stable)}",
            f"Variable wiederkehrende Milieus: {len(variable)}",
            "",
            "Ein wiederkehrendes Kontaktmilieu bedeutet hier nicht, dass die Feldbewegung mechanisch ausgeloest wird.",
            "Es bedeutet: Die Feldbewegung erscheint in einem aehnlichen Rezeptor-/Innenfeld-Kontext wieder.",
            "",
            "Das ist fuer MINI_DIO wichtig, weil dadurch Bedeutung nicht nur als Insel, sondern als Lagefolge gelesen werden kann.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten stabile Milieus gegen laengere Welten geprueft werden.",
            "Wenn sie dort stabil bleiben, koennen sie als passive Regulationswahrnehmung dokumentiert werden.",
            "",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze recurrence and drift of contact milieus around MCM preview movements.")
    parser.add_argument("--input", default=str(DEFAULT_IN))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    rows = _load_rows(_resolve(args.input))
    pair_rows, signature_rows = _summarize(rows)
    _write_md(pair_rows, signature_rows, _resolve(args.out))
    print(f"wrote {_resolve(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
