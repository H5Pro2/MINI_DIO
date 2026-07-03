from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.report_mcm_hoerbarer_shift_symbol_coupling import (
    EPISODE_MAP,
    _basename,
    _float,
    _load_episode_rows,
    _summarize_window,
)


INPUT = ROOT / "docs" / "befunde" / "1351_HOERBARER_SCHMALER_SHIFT_ROLLELESUNG.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1355_HOERBARER_SCHMALER_SHIFT_NACHHALLSPUR.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1355_HOERBARER_SCHMALER_SHIFT_NACHHALLSPUR.md"


def _safe_window(start: int, end: int) -> tuple[int, int]:
    return max(0, start), max(0, end)


def _phase_summary(
    episodes: list[dict[str, str]],
    start: int,
    end: int,
    prefix: str,
) -> dict[str, str]:
    summary = _summarize_window(episodes, start, end)
    return {f"{prefix}_{key}": value for key, value in summary.items()}


def build_report(input_path: Path = INPUT, csv_out: Path = OUT_CSV, md_out: Path = OUT_MD) -> None:
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    episode_cache: dict[str, list[dict[str, str]]] = {}
    out_rows: list[dict[str, str]] = []

    for row in rows:
        basename = _basename(row["source_file"])
        path = EPISODE_MAP.get(basename)
        if path is None:
            continue

        cache_key = str(path)
        if cache_key not in episode_cache:
            episode_cache[cache_key] = _load_episode_rows(path)
        episodes = episode_cache[cache_key]
        if not episodes:
            continue

        start = int(_float(row["start_tick"]))
        end = int(_float(row["end_tick"]))
        width = max(1, end - start)
        pre_start, pre_end = _safe_window(start - width, start)
        post_start, post_end = _safe_window(end, end + width)

        pre = _phase_summary(episodes, pre_start, pre_end, "pre")
        during = _phase_summary(episodes, start, end, "during")
        post = _phase_summary(episodes, post_start, post_end, "post")

        during_preview = during.get("during_top_preview_symbol", "-")
        during_family = during.get("during_top_symbol_family", "-")
        pre_preview = pre.get("pre_top_preview_symbol", "-")
        post_preview = post.get("post_top_preview_symbol", "-")
        pre_family = pre.get("pre_top_symbol_family", "-")
        post_family = post.get("post_top_symbol_family", "-")

        preview_pre_carry = int(during_preview != "-" and during_preview == pre_preview)
        preview_post_carry = int(during_preview != "-" and during_preview == post_preview)
        family_pre_carry = int(during_family != "-" and during_family == pre_family)
        family_post_carry = int(during_family != "-" and during_family == post_family)

        post_rekopplung_delta = _float(post.get("post_avg_rekopplung")) - _float(during.get("during_avg_rekopplung"))
        post_strain_delta = _float(post.get("post_avg_strain")) - _float(during.get("during_avg_strain"))

        out = {
            "asset": row["asset"],
            "world": row["world"],
            "start_tick": str(start),
            "end_tick": str(end),
            "phase_role": row["phase_role"],
            "base_sequence": row["base_sequence"],
            "compact_sensory_phase": row["compact_sensory_phase"],
            "pre_window": f"{pre_start}-{pre_end}",
            "during_window": f"{start}-{end}",
            "post_window": f"{post_start}-{post_end}",
        }
        out.update(pre)
        out.update(during)
        out.update(post)
        out.update(
            {
                "preview_pre_carry": str(preview_pre_carry),
                "preview_post_carry": str(preview_post_carry),
                "family_pre_carry": str(family_pre_carry),
                "family_post_carry": str(family_post_carry),
                "post_rekopplung_delta": f"{post_rekopplung_delta:.6f}",
                "post_strain_delta": f"{post_strain_delta:.6f}",
            }
        )
        out_rows.append(out)

    if not out_rows:
        raise RuntimeError("no rows mapped")

    csv_out.parent.mkdir(parents=True, exist_ok=True)
    with csv_out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    preview_post = sum(int(row["preview_post_carry"]) for row in out_rows)
    preview_pre = sum(int(row["preview_pre_carry"]) for row in out_rows)
    family_post = sum(int(row["family_post_carry"]) for row in out_rows)
    family_pre = sum(int(row["family_pre_carry"]) for row in out_rows)
    during_previews = Counter(row["during_top_preview_symbol"] for row in out_rows)
    post_previews = Counter(row["post_top_preview_symbol"] for row in out_rows)
    roles = Counter(row["phase_role"] for row in out_rows)
    post_re_delta = mean(_float(row["post_rekopplung_delta"]) for row in out_rows)
    post_str_delta = mean(_float(row["post_strain_delta"]) for row in out_rows)

    lines = [
        "# 1355 - Hoerbarer schmaler Shift: Nachhallspur",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob die in `1352`/`1354` auffaelligen Shift-Preview-Symbole zeitlich weitertragen.",
        "Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.",
        "",
        "## Befund",
        "",
        f"- Fenster gesamt: `{len(out_rows)}`",
        f"- Preview traegt aus Vorfenster in Trefferfenster: `{preview_pre}`",
        f"- Preview traegt aus Trefferfenster in Folgefenster: `{preview_post}`",
        f"- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `{family_pre}`",
        f"- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `{family_post}`",
        f"- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `{post_re_delta:.6f}`",
        f"- Durchschnittliches Straindelta Folge minus Treffer: `{post_str_delta:.6f}`",
        f"- Rollenverteilung: {roles.most_common()}",
        f"- Preview im Trefferfenster: {during_previews.most_common(8)}",
        f"- Preview im Folgefenster: {post_previews.most_common(8)}",
        "",
        "## Interpretation",
        "",
    ]

    if preview_post >= max(1, len(out_rows) // 3):
        lines.append(
            "Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur."
        )
    else:
        lines.append(
            "Die meisten Shift-Preview-Symbole bleiben nicht als identisches Top-Preview-Symbol erhalten. Das spricht eher fuer lokalen Kontakt als fuer starre Symbolfortsetzung."
        )

    lines.extend(
        [
            "",
            "Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte die Nachhallspur rollenbezogen gelesen werden: Brueckenfenster, Randdruck und Zentrumskontakt getrennt vergleichen, statt alle Shiftfenster zusammenzufassen.",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(INPUT))
    parser.add_argument("--csv-out", default=str(OUT_CSV))
    parser.add_argument("--out", default=str(OUT_MD))
    args = parser.parse_args()
    build_report(Path(args.input), Path(args.csv_out), Path(args.out))
