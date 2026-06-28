from __future__ import annotations

import argparse
import csv
from collections import Counter
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


def _short_token(row: dict[str, str]) -> str:
    token = str(row.get("short_token") or row.get("token") or "-")
    return token.replace("dio_mcm_episode_", "")


def _hit_row(row: dict[str, str], token: str) -> bool:
    short = token.replace("dio_mcm_episode_", "")
    joined = " ".join(str(value) for value in row.values())
    return short in joined or f"dio_mcm_episode_{short}" in joined


def _top(counter: Counter[str], limit: int = 5) -> str:
    return " | ".join(f"{key}:{value}" for key, value in counter.most_common(limit)) or "-"


def _world_label(path: Path) -> str:
    stem = path.stem
    for prefix in (
        "969_MCM_NICHTBRUECKEN_ORDNUNG_",
        "974_MCM_NICHTBRUECKEN_ORDNUNG_",
        "978_MCM_NICHTBRUECKEN_ORDNUNG_",
    ):
        if stem.startswith(prefix):
            return stem[len(prefix) :]
    return stem


def _candidate_rows(nonbridge: Path, min_observations: int, limit: int) -> list[dict[str, str]]:
    rows = []
    for row in _load_rows(nonbridge):
        text = " ".join(str(row.get(key, "") or "") for key in ("nonbridge_class", "dominant_role", "condensation_zone", "classification_note"))
        if "zentrum" not in text:
            continue
        if _safe_int(row.get("observations")) < min_observations:
            continue
        avg_rekopplung = _safe_float(row.get("avg_rekopplung"))
        avg_strain = _safe_float(row.get("avg_strain"))
        observations = _safe_int(row.get("observations"))
        is_carried_center = "zentrum_getragen" in text or (
            avg_rekopplung > 0.55 and avg_strain < 0.22 and observations >= min_observations
        )
        if not is_carried_center:
            continue
        rows.append(row)
    rows.sort(
        key=lambda row: (
            _safe_int(row.get("observations")),
            _safe_float(row.get("avg_rekopplung")) - _safe_float(row.get("avg_strain")),
            _safe_float(row.get("avg_sensory")),
        ),
        reverse=True,
    )
    return rows[:limit]


def _evidence_summary(token: str, evidence_files: list[Path]) -> dict[str, object]:
    source_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    zone_counter: Counter[str] = Counter()
    effect_counter: Counter[str] = Counter()
    tone_counter: Counter[str] = Counter()
    coupling_counter: Counter[str] = Counter()
    worlds_counter: Counter[str] = Counter()
    rekopplung: list[float] = []
    strain: list[float] = []
    sensory: list[float] = []

    for path in evidence_files:
        if not path.exists():
            continue
        for row in _load_rows(path):
            if not _hit_row(row, token):
                continue
            source_counter[path.name] += 1
            for key in ("dominant_role", "follow_role", "base_role", "role"):
                value = row.get(key)
                if value:
                    role_counter[value] += 1
            for key in ("nonbridge_class", "condensation_zone", "follow_zone", "base_zone", "path_class"):
                value = row.get(key)
                if value:
                    zone_counter[value] += 1
            for key in ("inner_effect_state", "dominant_inner_state"):
                value = row.get(key)
                if value:
                    effect_counter[value] += 1
            value = row.get("dominant_tone_role")
            if value:
                tone_counter[value] += 1
            value = row.get("coupling_role")
            if value:
                coupling_counter[value] += 1
            for key in ("world", "world_names"):
                value = row.get(key)
                if value:
                    for part in str(value).replace('"', "").split(","):
                        part = part.strip()
                        if part:
                            worlds_counter[part] += 1
            for key in ("avg_rekopplung", "avg_mcm_rekopplung_quality"):
                if key in row:
                    rekopplung.append(_safe_float(row.get(key)))
            for key in ("avg_strain", "avg_mcm_strain_quality"):
                if key in row:
                    strain.append(_safe_float(row.get(key)))
            for key in ("avg_sensory", "avg_mcm_sensory_coupling"):
                if key in row:
                    sensory.append(_safe_float(row.get(key)))

    hit_count = sum(source_counter.values())
    return {
        "evidence_hits": hit_count,
        "evidence_sources": _top(source_counter),
        "evidence_roles": _top(role_counter),
        "evidence_zones": _top(zone_counter),
        "evidence_effects": _top(effect_counter),
        "evidence_tones": _top(tone_counter),
        "evidence_couplings": _top(coupling_counter),
        "evidence_worlds": _top(worlds_counter),
        "evidence_avg_rekopplung": round(sum(rekopplung) / max(1, len(rekopplung)), 6),
        "evidence_avg_strain": round(sum(strain) / max(1, len(strain)), 6),
        "evidence_avg_sensory": round(sum(sensory) / max(1, len(sensory)), 6),
    }


def _reading(row: dict[str, object]) -> str:
    observations = _safe_int(row.get("observations"))
    rek = _safe_float(row.get("avg_rekopplung"))
    strain = _safe_float(row.get("avg_strain"))
    evidence_hits = _safe_int(row.get("evidence_hits"))
    if observations >= 20 and rek > strain and evidence_hits > 0:
        return "verlegte_mitte_mit_rueckbindung"
    if observations >= 20 and rek > strain:
        return "verlegte_mitte_lokal_getragen"
    if evidence_hits > 0:
        return "verlegte_mitte_mit_duenner_rueckbindung"
    return "verlegte_mitte_noch_lokal"


def build_rows(nonbridge_files: list[Path], evidence_files: list[Path], min_observations: int, limit: int) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for nonbridge in nonbridge_files:
        for row in _candidate_rows(nonbridge, min_observations, limit):
            token = _short_token(row)
            out = {
                **PASSIVE_FLAGS,
                "world_group": _world_label(nonbridge),
                "source_file": nonbridge.name,
                "token": token,
                "observations": _safe_int(row.get("observations")),
                "worlds": _safe_int(row.get("worlds")),
                "neighbor_count": _safe_int(row.get("neighbor_count")),
                "nonbridge_class": row.get("nonbridge_class", "-"),
                "condensation_zone": row.get("condensation_zone", "-"),
                "dominant_role": row.get("dominant_role", "-"),
                "dominant_family": row.get("dominant_family", "-"),
                "avg_rekopplung": _safe_float(row.get("avg_rekopplung")),
                "avg_strain": _safe_float(row.get("avg_strain")),
                "avg_sensory": _safe_float(row.get("avg_sensory")),
                "top_previous": row.get("top_previous", "-"),
                "top_next": row.get("top_next", "-"),
            }
            out.update(_evidence_summary(token, evidence_files))
            out["reading"] = _reading(out)
            output.append(out)
    return output


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _write_md(path: Path, rows: list[dict[str, object]]) -> None:
    lines = [
        "# MCM-Zentrumsverlagerung: Kandidaten-Ruecklesung",
        "",
        "## Zweck",
        "",
        "Diese Datei liest die staerksten neuen `zentrum_getragen`-Kandidaten der Folgewelten zurueck.",
        "Geprueft wird, ob sie nur lokal zentrumsnah sind oder Rueckbindung an bestehende Feldspuren besitzen.",
        "",
        "## Sicherheitsgrenze",
        "",
        "- passive Ruecklesung",
        "- keine Handlung",
        "- kein Gate",
        "- keine Strategie",
        "",
        "## Kandidaten",
        "",
        "| Welt | Knoten | Beob. | Nachbarn | Rekopplung | Strain | Sensorik | Belege | Zonen | Effekte | Lesung |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['world_group']}` | `{row['token']}` | {row['observations']} | {row['neighbor_count']} | "
            f"{float(row['avg_rekopplung']):.6f} | {float(row['avg_strain']):.6f} | {float(row['avg_sensory']):.6f} | "
            f"{row['evidence_hits']} | `{row['evidence_zones']}` | `{row['evidence_effects']}` | `{row['reading']}` |"
        )

    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Verlagerung der Mitte muss an einzelnen Kandidaten geprueft werden.",
            "Ein Kandidat ist staerker, wenn lokale Wiederkehr, Rekopplung und externe Rueckbindung zusammenkommen.",
            "",
            "Arbeitsableitung:",
            "",
            "```text",
            "Zentrumsverlagerung ist erst dann belastbar, wenn neue Mitte nicht nur lokal auftritt,",
            "sondern ueber Zonen, Sinnesachsen oder Klangspuren wieder Rueckbindung findet.",
            "```",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollten die wiederkehrenden Kandidaten ueber eine weitere Weltgruppe verfolgt werden.",
            "Besonders relevant sind Knoten, die in neunter und zehnter Welt gleichzeitig als verlegte Mitte mit Rueckbindung erscheinen.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nonbridge", action="append", type=Path, required=True)
    parser.add_argument("--evidence", action="append", type=Path, default=[])
    parser.add_argument("--min-observations", type=int, default=5)
    parser.add_argument("--limit-per-world", type=int, default=8)
    parser.add_argument("--out-md", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    args = parser.parse_args()

    rows = build_rows(
        args.nonbridge,
        args.evidence,
        max(1, args.min_observations),
        max(1, args.limit_per_world),
    )
    _write_csv(args.out_csv, rows)
    _write_md(args.out_md, rows)
    print(f"candidates={len(rows)}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.out_csv}")


if __name__ == "__main__":
    main()
