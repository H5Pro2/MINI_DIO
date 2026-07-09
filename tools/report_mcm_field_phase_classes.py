from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from befunde_paths import befunde_root


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


DEFAULT_INPUT = befunde_root(ROOT) / "1243_MCM_FELDPHASEN_MEMORY_MEHRWELT.csv"
DEFAULT_OUT = befunde_root(ROOT) / "1245_MCM_FELDPHASEN_KLASSEN.md"


def _resolve(path_text: str | Path) -> Path:
    path = Path(path_text)
    if not path.is_absolute():
        path = ROOT / path
    return path


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


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _phase_class(row: dict[str, str], *, max_world_count: int, max_seen_count: int) -> str:
    world_count = _safe_int(row.get("world_count"))
    seen_count = _safe_int(row.get("seen_count"))
    quality = str(row.get("phase_memory_quality", "") or "")
    effect = str(row.get("dominant_effect", "") or "")

    world_ratio = world_count / max_world_count if max_world_count > 0 else 0.0
    seen_ratio = seen_count / max_seen_count if max_seen_count > 0 else 0.0

    if quality == "young_phase_trace" or world_count <= 1 or seen_count <= 1:
        return "junge_phasenspur"
    if effect in {"rand_entlastet_in_offenheit", "zentrumsbruch_in_offenheit"} and world_ratio >= 0.5:
        return "grenzphase_mit_entlastung"
    if world_ratio >= 0.85 and seen_ratio >= 0.10:
        return "allgemeine_feldphase"
    if world_ratio >= 0.55:
        return "breit_getragene_feldphase"
    if world_ratio >= 0.25:
        return "weltgebundene_feldphase"
    return "lokale_oder_driftende_phase"


def _role_family(row: dict[str, str]) -> str:
    previous_role = str(row.get("previous_role", "") or "")
    current_role = str(row.get("current_role", "") or "")
    next_role = str(row.get("next_role", "") or "")
    roles = {previous_role, current_role, next_role}
    if roles <= {"zentrum_stabil", "rekopplungsnaehe", "offene_variante"}:
        return "zentrum_offen_rekopplung"
    if "spannungsrand_kippnaehe" in roles and "offene_variante" in roles:
        return "rand_offen_kopplung"
    if "spannungsrand_kippnaehe" in roles:
        return "randgebundene_phase"
    return "sonstige_phase"


def _classify_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    max_world_count = max((_safe_int(row.get("world_count")) for row in rows), default=0)
    max_seen_count = max((_safe_int(row.get("seen_count")) for row in rows), default=0)
    classified: list[dict[str, object]] = []
    for row in rows:
        world_count = _safe_int(row.get("world_count"))
        seen_count = _safe_int(row.get("seen_count"))
        classified.append(
            {
                **row,
                "phase_class": _phase_class(
                    row,
                    max_world_count=max_world_count,
                    max_seen_count=max_seen_count,
                ),
                "role_family": _role_family(row),
                "world_coverage": round(world_count / max_world_count, 6) if max_world_count else 0.0,
                "seen_density": round(seen_count / max_seen_count, 6) if max_seen_count else 0.0,
            }
        )
    return classified


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
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def _write_markdown(path: Path, rows: list[dict[str, object]], input_path: Path) -> None:
    phase_class_counts = Counter(str(row["phase_class"]) for row in rows)
    role_family_counts = Counter(str(row["role_family"]) for row in rows)
    by_class: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        by_class.setdefault(str(row["phase_class"]), []).append(row)

    lines: list[str] = [
        "# MCM-Feldphasen-Klassen",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose trennt die Feldphasen-Memory in allgemeine, breit getragene, weltgebundene und junge/driftende Phasen.",
        "",
        "Die Klassifikation ist relativ zur gelesenen Mehrwelt-Matrix. Sie ist keine feste Regel fuer MINI_DIO.",
        "",
        "## Eingabe",
        "",
        f"- `{input_path.relative_to(ROOT)}`",
        "",
        "## Profil",
        "",
        f"- Phasenfamilien: `{len(rows)}`",
        f"- Klassen: `{dict(phase_class_counts.most_common())}`",
        f"- Rollenfamilien: `{dict(role_family_counts.most_common())}`",
        "",
        "## Klassenuebersicht",
        "",
        "| Klasse | Anzahl | Lesart |",
        "|---|---:|---|",
    ]

    class_notes = {
        "allgemeine_feldphase": "ueber viele Welten und mit hoher Wiederkehr getragen",
        "breit_getragene_feldphase": "ueber viele Welten sichtbar, aber weniger dicht",
        "grenzphase_mit_entlastung": "Rand/Kipp wirkt als Grenzimpuls mit Entlastung",
        "weltgebundene_feldphase": "an bestimmte Welten oder Weltarten gebunden",
        "lokale_oder_driftende_phase": "lokal sichtbar oder noch nicht stabil getragen",
        "junge_phasenspur": "einzelne junge Spur, noch keine Familie",
    }
    for phase_class, count in phase_class_counts.most_common():
        lines.append(f"| {phase_class} | {count} | {class_notes.get(phase_class, '-')} |")

    lines.extend(["", "## Relevante Phasen", ""])
    for phase_class in phase_class_counts:
        class_rows = sorted(
            by_class[phase_class],
            key=lambda row: (-_safe_int(row.get("seen_count")), -_safe_float(row.get("world_coverage"))),
        )
        lines.extend(
            [
                f"### {phase_class}",
                "",
                "| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |",
                "|---|---:|---:|---:|---|---|",
            ]
        )
        for row in class_rows[:12]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["phase_key"]),
                        str(row["seen_count"]),
                        _fmt(row["world_coverage"]),
                        _fmt(row["seen_density"]),
                        str(row["dominant_effect"]),
                        str(row["role_family"]),
                    ]
                )
                + " |"
            )
        lines.append("")

    lines.extend(
        [
            "## Befund",
            "",
            "Die Feldphasen-Memory zeigt eine klare Schichtung:",
            "",
            "- Ein Kern aus allgemeinen Zentrum/Offenheit/Rekopplungs-Phasen.",
            "- Ein zweiter Bereich aus Rand/Kipp-Phasen, die meist in Offenheit entlasten.",
            "- Wenige junge oder lokale Spuren.",
            "",
            "Damit wirkt die Feldphasen-Memory nicht wie beliebiges Sammeln, sondern wie eine sortierte passive Bewegungsordnung.",
            "",
            "## Bedeutung",
            "",
            "MINI_DIO bekommt dadurch keine Handlung. Es bekommt eine bessere passive Innenzeit:",
            "",
            "```text",
            "nicht nur: Das Feld ist so.",
            "sondern: Das Feld bewegt sich wiederholt so.",
            "```",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Klassifiziert passive MCM-Feldphasenfamilien.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Feldphasen-Memory CSV.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Markdown-Ausgabe.")
    args = parser.parse_args()

    input_path = _resolve(args.input)
    out_path = _resolve(args.out)
    rows = _classify_rows(_load_rows(input_path))
    _write_csv(out_path.with_suffix(".csv"), rows)
    _write_markdown(out_path, rows, input_path)

    print(f"records={len(rows)} out={out_path}")
    for phase_class, count in Counter(str(row["phase_class"]) for row in rows).most_common():
        print(f"{phase_class}: {count}")


if __name__ == "__main__":
    main()
