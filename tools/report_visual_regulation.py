from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

from report_auditory_regulation import DEFAULT_SUMMARIES
from report_auditory_regulation import _fmt
from report_recoupling_quality import _load_json, _resolve
from report_recoupling_quality import _row as recoupling_row


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "befunde" / "228_VISUELLE_REGULATION_DIAGNOSE.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _episode_files(summary_path: Path) -> list[Path]:
    root = summary_path.parent
    files = sorted(root.glob("dio_mini_lauf_*/episodes.csv"))
    return files


def _read_episode_rows(summary_path: Path) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for path in _episode_files(summary_path):
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for raw in reader:
                rows.append(
                    {
                        "flow": _float(raw.get("sehen_form_flow")),
                        "stability": _float(raw.get("sehen_form_stability")),
                        "change": _float(raw.get("sehen_form_change")),
                        "visual_gap": _float(raw.get("mcm_visual_field_gap")),
                        "afterimage": _float(raw.get("mini_afterimage")),
                        "rekopplung": _float(raw.get("mcm_rekopplung_quality")),
                        "field_strain": _float(raw.get("mcm_strain_quality")),
                    }
                )
    return rows


def _visual_metrics(rows: list[dict[str, float]]) -> dict:
    if not rows:
        return {
            "avg_motion": 0.0,
            "avg_change": 0.0,
            "avg_stability": 0.0,
            "avg_visual_gap": 0.0,
            "avg_visual_focus": 0.0,
            "avg_visual_noise": 0.0,
            "avg_visual_alarm": 0.0,
            "avg_visual_background": 0.0,
            "avg_visual_afterimage": 0.0,
            "dominant_state": "sicht_unbekannt",
            "state_counts": {},
        }

    focus_values: list[float] = []
    noise_values: list[float] = []
    alarm_values: list[float] = []
    background_values: list[float] = []
    motion_values: list[float] = []
    change_values: list[float] = []
    stability_values: list[float] = []
    gap_values: list[float] = []
    afterimage_values: list[float] = []
    states: list[str] = []

    for row in rows:
        motion = abs(row["flow"])
        change = abs(row["change"])
        stability = _clamp((row["stability"] + 1.0) * 0.5)
        visual_gap = _clamp(row["visual_gap"])
        afterimage = _clamp(row["afterimage"])

        alarm = _clamp((change * 0.34) + (visual_gap * 0.34) + (motion * 0.16) + ((1.0 - stability) * 0.16))
        focus = _clamp((change * 0.28) + (motion * 0.24) + (stability * 0.20) + (visual_gap * 0.16) + (afterimage * 0.12))
        noise = _clamp(((1.0 - stability) * 0.36) + (change * 0.26) + (visual_gap * 0.20) + ((1.0 - motion) * 0.18))
        background = _clamp(((1.0 - change) * 0.30) + ((1.0 - motion) * 0.24) + (stability * 0.24) + ((1.0 - visual_gap) * 0.22))

        if alarm > 0.62:
            state = "visuelle_alarmform"
        elif focus > 0.58:
            state = "form_genauer_ansehen"
        elif stability > 0.68 and visual_gap < 0.20 and change < 0.45:
            state = "form_stabil_tragen"
        elif afterimage > 0.24 and change < 0.38:
            state = "form_abklingen_lassen"
        elif background > 0.68:
            state = "form_hintergrund_halten"
        else:
            state = "visuelles_rauschen_filtern"

        states.append(state)
        focus_values.append(focus)
        noise_values.append(noise)
        alarm_values.append(alarm)
        background_values.append(background)
        motion_values.append(motion)
        change_values.append(change)
        stability_values.append(stability)
        gap_values.append(visual_gap)
        afterimage_values.append(afterimage)

    counts = Counter(states)
    total = max(1, len(rows))
    return {
        "avg_motion": sum(motion_values) / total,
        "avg_change": sum(change_values) / total,
        "avg_stability": sum(stability_values) / total,
        "avg_visual_gap": sum(gap_values) / total,
        "avg_visual_focus": sum(focus_values) / total,
        "avg_visual_noise": sum(noise_values) / total,
        "avg_visual_alarm": sum(alarm_values) / total,
        "avg_visual_background": sum(background_values) / total,
        "avg_visual_afterimage": sum(afterimage_values) / total,
        "dominant_state": counts.most_common(1)[0][0],
        "state_counts": dict(counts),
        "total_rows": total,
    }


def _row(name: str, path_text: str, group: str) -> dict:
    summary_path = _resolve(path_text)
    summary = _load_json(summary_path)
    rec = recoupling_row(name, summary)
    metrics = _visual_metrics(_read_episode_rows(summary_path))
    counts = metrics["state_counts"]
    total = max(1, int(metrics["total_rows"]))
    return {
        "name": name,
        "group": group,
        "role": rec["dominant_role"],
        "rekopplung": rec["rekopplung"],
        "field_strain": rec["field_strain"],
        "memory_load": rec["memory_load"],
        **metrics,
        "genauer_ratio": counts.get("form_genauer_ansehen", 0) / total,
        "alarm_ratio": counts.get("visuelle_alarmform", 0) / total,
        "stabil_ratio": counts.get("form_stabil_tragen", 0) / total,
        "hintergrund_ratio": counts.get("form_hintergrund_halten", 0) / total,
        "rauschen_ratio": counts.get("visuelles_rauschen_filtern", 0) / total,
        "abklingen_ratio": counts.get("form_abklingen_lassen", 0) / total,
    }


def _write_markdown(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: (row["group"], row["name"]))

    lines = [
        "# Visuelle Regulation - Diagnose",
        "",
        f"Stand: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Zweck",
        "",
        "Diese Diagnose liest die Sehspur von MINI_DIO als passive visuelle Regulation.",
        "Sie prueft, ob Formfluss, Formstabilitaet, Formwechsel und visueller Feldabstand getrennt lesbar sind.",
        "",
        "Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.",
        "",
        "Hierarchie der Pruefung:",
        "",
        "1. Grundfrage: Kann MINI_DIO Form sehen, ohne sie direkt als Feldwirkung oder Handlung zu behandeln?",
        "2. Unterpruefung: visuelles Rauschen, genaueres Ansehen, Hintergrund, stabile Form, Alarmform und Abklingen lesen.",
        "3. Folgeschritt: visuelle Zustaende gegen MCM-Feldlast und Rekopplung legen.",
        "",
        "## Einzelwerte",
        "",
        "| Welt | Gruppe | Rolle | dominanter Sehzustand | Bewegung | Wechsel | Stabilitaet | Visueller Gap | Fokus | Rauschen | Alarm | Hintergrund | Nachbild | Rekopplung | Feldlast |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    row["group"],
                    row["role"],
                    row["dominant_state"],
                    _fmt(row["avg_motion"], 4),
                    _fmt(row["avg_change"], 4),
                    _fmt(row["avg_stability"], 4),
                    _fmt(row["avg_visual_gap"], 4),
                    _fmt(row["avg_visual_focus"], 4),
                    _fmt(row["avg_visual_noise"], 4),
                    _fmt(row["avg_visual_alarm"], 4),
                    _fmt(row["avg_visual_background"], 4),
                    _fmt(row["avg_visual_afterimage"], 4),
                    _fmt(row["rekopplung"], 6),
                    _fmt(row["field_strain"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Sehzustandsanteile",
            "",
            "| Welt | genauer ansehen | Alarmform | stabil tragen | Hintergrund | Rauschen filtern | Form abklingen |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["name"],
                    _fmt(row["genauer_ratio"], 4),
                    _fmt(row["alarm_ratio"], 4),
                    _fmt(row["stabil_ratio"], 4),
                    _fmt(row["hintergrund_ratio"], 4),
                    _fmt(row["rauschen_ratio"], 4),
                    _fmt(row["abklingen_ratio"], 4),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Lesart",
            "",
            "- `form_genauer_ansehen`: Formwechsel, Bewegung oder Gap brauchen feinere visuelle Betrachtung.",
            "- `visuelle_alarmform`: Formwechsel und Feldabstand liegen nahe an Kippnaehe.",
            "- `form_stabil_tragen`: Form bleibt stabil und nah am Feld.",
            "- `form_hintergrund_halten`: Form bleibt sichtbar, ohne Vordergrund zu werden.",
            "- `visuelles_rauschen_filtern`: visuelle Unruhe wird nicht strukturtragend gemacht.",
            "- `form_abklingen_lassen`: ein visuelles Nachbild darf auslaufen.",
            "",
            "## Vorlaeufiger Befund",
            "",
            "Sehen sollte als eigene Sinnesregulation gelesen werden.",
            "Form darf sichtbar sein, ohne sofort Feldbedeutung oder Handlung zu werden.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes wird der Befund geschrieben.",
            "Dort wird geprueft, ob SOL 5m visuell anders getragen wird als SOL 30m/1h und Stresssegmente.",
        ]
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Erstellt eine passive Diagnose zur visuellen Regulation.")
    parser.add_argument("--summary", nargs=3, action="append", metavar=("NAME", "PATH", "GROUP"))
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    specs = args.summary or DEFAULT_SUMMARIES
    rows = [_row(name, path_text, group) for name, path_text, group in specs]
    _write_markdown(rows, _resolve(args.out))


if __name__ == "__main__":
    main()
