from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_OUT = befunde_root(ROOT) / "1264_MCM_FOLGEHALT_NACH_RANDKONTAKT.md"

RAND_ROLE = "spannungsrand_kippnaehe"
FOLLOW_ROLES = {"zentrum_stabil", "rekopplungsnaehe", "offene_variante"}


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


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


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _segment_paths() -> list[Path]:
    return sorted((befunde_root(ROOT)).glob("*FELDPHASEN*SEGMENTE.csv"))


def _world_kind(world: str, source: str) -> str:
    text = f"{world} {source}".lower()
    if "quiet" in text or "seit" in text:
        return "ruhige_oder_seitwaerts_welt"
    if "stress" in text or "neg" in text or "bear" in text:
        return "stress_oder_negative_welt"
    if "expansion" in text or "bull" in text or "positive" in text:
        return "expansive_oder_positive_welt"
    if "btc" in text:
        return "btc_welt"
    if "paxg" in text:
        return "paxg_welt"
    if "kas" in text:
        return "kas_welt"
    if "synth" in text:
        return "synthetische_sinneswelt"
    return "sequenz_oder_asset_welt"


def _followhold_kind(current: dict[str, str], follow: dict[str, str], after: dict[str, str] | None) -> str:
    follow_role = str(follow.get("role", "") or "")
    after_role = str(after.get("role", "") or "") if after else ""
    delta_reko = _safe_float(follow.get("avg_rekopplung")) - _safe_float(current.get("avg_rekopplung"))
    delta_strain = _safe_float(follow.get("avg_strain")) - _safe_float(current.get("avg_strain"))

    if follow_role == RAND_ROLE:
        return "rand_bleibt"
    if follow_role not in FOLLOW_ROLES:
        return "unbekannte_folge"
    if after_role == RAND_ROLE:
        if follow_role == "zentrum_stabil":
            return "zentrum_kurz_getragen_dann_rueckfall"
        if follow_role == "rekopplungsnaehe":
            return "rekopplung_kurz_getragen_dann_rueckfall"
        return "offenheit_kurz_getragen_dann_rueckfall"
    if delta_reko >= 0.0 and delta_strain <= 0.0:
        return f"{follow_role}_entlastend_gehalten"
    if delta_reko < 0.0 and delta_strain > 0.0:
        return f"{follow_role}_nachlastig"
    return f"{follow_role}_gemischt_gehalten"


def _build_rows(limit: int) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    for path in _segment_paths():
        rows = _load_csv(path)
        by_world: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            world = str(row.get("world", "") or "")
            if world:
                by_world[world].append(row)

        for world, world_rows in by_world.items():
            for idx in range(0, len(world_rows) - 1):
                current = world_rows[idx]
                if str(current.get("role", "") or "") != RAND_ROLE:
                    continue
                follow = world_rows[idx + 1]
                after = world_rows[idx + 2] if idx + 2 < len(world_rows) else None
                kind = _followhold_kind(current, follow, after)
                events.append(
                    {
                        "followhold_kind": kind,
                        "world": world,
                        "world_kind": _world_kind(world, path.name),
                        "source_file": path.name,
                        "rand_start_tick": current.get("start_tick", ""),
                        "rand_end_tick": current.get("end_tick", ""),
                        "rand_duration": current.get("duration", ""),
                        "follow_role": follow.get("role", ""),
                        "follow_start_tick": follow.get("start_tick", ""),
                        "follow_end_tick": follow.get("end_tick", ""),
                        "follow_duration": follow.get("duration", ""),
                        "after_role": after.get("role", "") if after else "",
                        "after_duration": after.get("duration", "") if after else "",
                        "rand_loudness": round(_safe_float(current.get("avg_auditory_loudness")), 6),
                        "rand_intake": round(_safe_float(current.get("avg_raw_field_intake")), 6),
                        "rand_sharpness": round(_safe_float(current.get("avg_visual_sharpness")), 6),
                        "rand_rekopplung": round(_safe_float(current.get("avg_rekopplung")), 6),
                        "rand_strain": round(_safe_float(current.get("avg_strain")), 6),
                        "follow_loudness": round(_safe_float(follow.get("avg_auditory_loudness")), 6),
                        "follow_intake": round(_safe_float(follow.get("avg_raw_field_intake")), 6),
                        "follow_sharpness": round(_safe_float(follow.get("avg_visual_sharpness")), 6),
                        "follow_rekopplung": round(_safe_float(follow.get("avg_rekopplung")), 6),
                        "follow_strain": round(_safe_float(follow.get("avg_strain")), 6),
                        "delta_follow_rekopplung": round(
                            _safe_float(follow.get("avg_rekopplung")) - _safe_float(current.get("avg_rekopplung")),
                            6,
                        ),
                        "delta_follow_strain": round(
                            _safe_float(follow.get("avg_strain")) - _safe_float(current.get("avg_strain")),
                            6,
                        ),
                    }
                )

    events.sort(
        key=lambda row: (
            str(row["followhold_kind"]),
            str(row["world"]),
            _safe_int(row["rand_start_tick"]),
        )
    )
    return events[:limit]


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: object) -> str:
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    kind_counts = Counter(str(row["followhold_kind"]) for row in rows)
    role_counts = Counter(str(row["follow_role"]) for row in rows)
    world_counts = Counter(str(row["world"]) for row in rows)

    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["followhold_kind"])].append(row)

    lines: list[str] = [
        "# MCM Folgehalt nach Randkontakt",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Grundfrage",
        "",
        "Wie lange traegt eine Folgeordnung nach `spannungsrand_kippnaehe`, bevor das Feld erneut in Rand/Kipp naehe zurueckfaellt?",
        "",
        "## Unterpruefung",
        "",
        "Diese Diagnose liest Segmentfolgen aus vorhandenen Feldphasen. Sie modelliert keine neue Regulation und setzt keine Handlungsschwelle.",
        "",
        "## Profil",
        "",
        f"- Randkontakte gelesen: `{len(rows)}`",
        f"- Folgearten: `{dict(kind_counts.most_common())}`",
        f"- direkte Folgerollen: `{dict(role_counts.most_common())}`",
        f"- staerkste Welten nach Anzahl: `{dict(world_counts.most_common(10))}`",
        "",
        "## Mittelwerte nach Folgeart",
        "",
        "| Folgeart | Anzahl | Folge-Dauer | Delta Rekopplung | Delta Strain | Rand-Lautheit | Rand-Strain |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for kind, count in kind_counts.most_common():
        group = grouped[kind]
        lines.append(
            "| "
            + " | ".join(
                [
                    kind,
                    str(count),
                    _fmt(_mean([_safe_float(row["follow_duration"]) for row in group])),
                    _fmt(_mean([_safe_float(row["delta_follow_rekopplung"]) for row in group])),
                    _fmt(_mean([_safe_float(row["delta_follow_strain"]) for row in group])),
                    _fmt(_mean([_safe_float(row["rand_loudness"]) for row in group])),
                    _fmt(_mean([_safe_float(row["rand_strain"]) for row in group])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Beispiel-Fenster",
            "",
            "| Folgeart | Welt | Rand Tick | Folge | Folge-Dauer | Danach | Delta Rekopplung | Delta Strain |",
            "|---|---|---:|---|---:|---|---:|---:|",
        ]
    )
    for row in rows[:32]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["followhold_kind"]),
                    str(row["world"]),
                    str(row["rand_start_tick"]),
                    str(row["follow_role"]),
                    str(row["follow_duration"]),
                    str(row["after_role"] or "-"),
                    _fmt(row["delta_follow_rekopplung"]),
                    _fmt(row["delta_follow_strain"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Randkontakt ist kein Endzustand. Entscheidend ist die Folgebewegung des Feldes.",
            "",
            "Die Diagnose trennt drei passive Lesarten:",
            "",
            "```text",
            "1. Rand bleibt oder kehrt schnell zurueck.",
            "2. Zentrum/Rekopplung/Offenheit erscheint, haelt aber nur kurz.",
            "3. Folgeordnung entlastet und bleibt vorerst ohne direkten Rueckfall sichtbar.",
            "```",
            "",
            "Damit wird die Aussage aus 1262-1263 konkretisiert: Ordnung braucht Folgehalt.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte dieser Folgehalt mit Rohweltfenstern gekoppelt werden: Welche Weltspannung erzeugt kurzen Rueckfall, welche Weltspannung laesst Folgeordnung tragen?",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_assessment(path: Path, rows: list[dict[str, object]]) -> None:
    kind_counts = Counter(str(row["followhold_kind"]) for row in rows)
    direct_return = sum(1 for row in rows if str(row.get("after_role", "")) == RAND_ROLE)
    no_direct_return = len(rows) - direct_return
    lines = [
        "# Bewertung: MCM Folgehalt nach Randkontakt",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Kernaussage",
        "",
        "Die MCM-Topologie wirkt nicht nur ueber Positionen, sondern ueber gehaltene Folgen.",
        "",
        "Ein Zentrumskontakt nach Rand/Kipp ist nur dann stabil lesbar, wenn die Folge nicht sofort wieder in Rand/Kipp zurueckfaellt.",
        "",
        "## Messbild",
        "",
        f"- untersuchte Randkontakte: `{len(rows)}`",
        f"- direkter Rueckfall in Rand/Kipp nach Folgephase: `{direct_return}`",
        f"- kein direkter Rueckfall im naechsten Segment sichtbar: `{no_direct_return}`",
        f"- Folgearten: `{dict(kind_counts.most_common())}`",
        "",
        "## Interpretation",
        "",
        "Das Feld bildet keine starre Karte. Es zeigt eine dynamische Topologie:",
        "",
        "- Rand/Kipp kann eine kurze Lastspitze sein.",
        "- Zentrum kann nur ein Durchgang sein.",
        "- Rekopplung kann tragen oder direkt wieder brechen.",
        "- Offenheit kann Entlastung sein oder nur Zwischenraum vor neuer Spannung.",
        "",
        "Das ist fuer MINI_DIO wichtig, weil Bedeutung nicht aus einem Einzelpunkt entsteht, sondern aus Feldfolge plus Folgehalt.",
        "",
        "## Naechste Pruefung",
        "",
        "Folgehalt mit Rohweltspannung koppeln: Nicht nur `was folgt im Feld`, sondern `welche Aussenweltform stand davor`.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Liest passiven Folgehalt nach Randkontakt.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    parser.add_argument("--limit", type=int, default=2000, help="Maximale Randkontakte.")
    args = parser.parse_args()

    out_path = _resolve(args.out)
    rows = _build_rows(limit=args.limit)
    csv_path = out_path.with_suffix(".csv")
    assessment_path = out_path.with_name("1265_MCM_FOLGEHALT_NACH_RANDKONTAKT_BEWERTUNG.md")

    _write_csv(csv_path, rows)
    _write_markdown(out_path, rows)
    _write_assessment(assessment_path, rows)

    print(f"rows={len(rows)}")
    print(f"wrote={out_path.relative_to(ROOT)}")
    print(f"wrote={csv_path.relative_to(ROOT)}")
    print(f"wrote={assessment_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
