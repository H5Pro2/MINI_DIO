from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


MELODY_DEFAULT = ROOT / "docs" / "befunde" / "834_MARKTMELODIE_STRESS2024_TONFOLGE.csv"
EPISODES_DEFAULT = ROOT / "debug" / "adapted_state_negative_stress_2024_5m_10k" / "dio_mini_lauf_1" / "episodes.csv"
CSV_DEFAULT = ROOT / "docs" / "befunde" / "835_MARKTMELODIE_MCM_KOPPLUNG.csv"
MD_DEFAULT = ROOT / "docs" / "befunde" / "835_MARKTMELODIE_MCM_KOPPLUNG.md"


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}f}"


def _percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * fraction)))
    return ordered[index]


def _dominant(counter: Counter[str]) -> str:
    if not counter:
        return "-"
    return counter.most_common(1)[0][0] or "-"


@dataclass
class CouplingBucket:
    key_type: str
    key: str
    count: int = 0
    tone_roles: Counter[str] = field(default_factory=Counter)
    mcm_classes: Counter[str] = field(default_factory=Counter)
    inner_states: Counter[str] = field(default_factory=Counter)
    episode_previews: Counter[str] = field(default_factory=Counter)
    symbol_families: Counter[str] = field(default_factory=Counter)
    relative_energy: list[float] = field(default_factory=list)
    pitch_hz: list[float] = field(default_factory=list)
    roughness: list[float] = field(default_factory=list)
    carry: list[float] = field(default_factory=list)
    strain: list[float] = field(default_factory=list)
    rekopplung: list[float] = field(default_factory=list)
    sensory_coupling: list[float] = field(default_factory=list)
    rezeptor_pressure: list[float] = field(default_factory=list)
    rezeptor_alignment: list[float] = field(default_factory=list)

    def add(self, melody: dict[str, str], episode: dict[str, str]) -> None:
        self.count += 1
        self.tone_roles[str(melody.get("tone_role") or "-")] += 1
        self.mcm_classes[str(episode.get("passive_mcm_effect_class") or "-")] += 1
        self.inner_states[str(episode.get("passive_inner_effect_awareness_state") or "-")] += 1
        self.episode_previews[str(episode.get("mcm_field_episode_preview_symbol") or "-")] += 1
        self.symbol_families[str(episode.get("symbol_family") or "-")] += 1
        self.relative_energy.append(_float(melody.get("relative_energy")))
        self.pitch_hz.append(_float(melody.get("pitch_hz")))
        self.roughness.append(_float(melody.get("roughness")))
        self.carry.append(_float(episode.get("mcm_carry_quality")))
        self.strain.append(_float(episode.get("mcm_strain_quality")))
        self.rekopplung.append(_float(episode.get("mcm_rekopplung_quality")))
        self.sensory_coupling.append(_float(episode.get("mcm_sensory_coupling")))
        self.rezeptor_pressure.append(_float(episode.get("rezeptor_contact_pressure")))
        self.rezeptor_alignment.append(_float(episode.get("rezeptor_contact_alignment")))

    def row(self, coupling_role: str) -> dict[str, object]:
        return {
            "key_type": self.key_type,
            "key": self.key,
            "count": self.count,
            "dominant_tone_role": _dominant(self.tone_roles),
            "dominant_mcm_effect_class": _dominant(self.mcm_classes),
            "dominant_inner_state": _dominant(self.inner_states),
            "dominant_episode_preview": _dominant(self.episode_previews),
            "dominant_symbol_family": _dominant(self.symbol_families),
            "avg_relative_energy": _fmt(_mean(self.relative_energy)),
            "avg_pitch_hz": _fmt(_mean(self.pitch_hz), 2),
            "avg_roughness": _fmt(_mean(self.roughness)),
            "avg_mcm_carry_quality": _fmt(_mean(self.carry)),
            "avg_mcm_strain_quality": _fmt(_mean(self.strain)),
            "avg_mcm_rekopplung_quality": _fmt(_mean(self.rekopplung)),
            "avg_mcm_sensory_coupling": _fmt(_mean(self.sensory_coupling)),
            "avg_rezeptor_contact_pressure": _fmt(_mean(self.rezeptor_pressure)),
            "avg_rezeptor_contact_alignment": _fmt(_mean(self.rezeptor_alignment)),
            "coupling_role": coupling_role,
        }


def _read_csv(path: Path, delimiter: str) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def _match_rows(melody_rows: list[dict[str, str]], episode_rows: list[dict[str, str]]) -> list[tuple[dict[str, str], dict[str, str]]]:
    melody_by_timestamp = {str(row.get("timestamp_ms") or ""): row for row in melody_rows}
    matched: list[tuple[dict[str, str], dict[str, str]]] = []
    for episode in episode_rows:
        timestamp = str(episode.get("timestamp_ms") or "")
        melody = melody_by_timestamp.get(timestamp)
        if melody is None:
            tick_index = int(_float(episode.get("tick"))) - 1
            if 0 <= tick_index < len(melody_rows):
                melody = melody_rows[tick_index]
        if melody is not None:
            matched.append((melody, episode))
    return matched


def _build_buckets(pairs: list[tuple[dict[str, str], dict[str, str]]]) -> list[CouplingBucket]:
    buckets: dict[tuple[str, str], CouplingBucket] = {}
    for melody, episode in pairs:
        for key_type, key in (
            ("phrase_symbol", str(melody.get("phrase_symbol") or "-")),
            ("speech_token", str(melody.get("speech_token") or "-")),
            ("tone_role", str(melody.get("tone_role") or "-")),
        ):
            bucket_key = (key_type, key)
            bucket = buckets.get(bucket_key)
            if bucket is None:
                bucket = CouplingBucket(key_type=key_type, key=key)
                buckets[bucket_key] = bucket
            bucket.add(melody, episode)
    return list(buckets.values())


def _assign_roles(buckets: list[CouplingBucket]) -> dict[tuple[str, str], str]:
    carry_values = [_mean(bucket.carry) for bucket in buckets if bucket.count >= 3]
    strain_values = [_mean(bucket.strain) for bucket in buckets if bucket.count >= 3]
    rekopplung_values = [_mean(bucket.rekopplung) for bucket in buckets if bucket.count >= 3]
    carry_high = _percentile(carry_values, 0.66)
    strain_high = _percentile(strain_values, 0.66)
    rekopplung_mid = _percentile(rekopplung_values, 0.50)
    roles: dict[tuple[str, str], str] = {}
    for bucket in buckets:
        carry = _mean(bucket.carry)
        strain = _mean(bucket.strain)
        rekopplung = _mean(bucket.rekopplung)
        if bucket.count < 3:
            role = "einzelkontakt"
        elif strain >= strain_high and strain > carry:
            role = "belastete_klangkopplung"
        elif carry >= carry_high and rekopplung >= rekopplung_mid:
            role = "tragende_klangkopplung"
        else:
            role = "offene_klangkopplung"
        roles[(bucket.key_type, bucket.key)] = role
    return roles


def _write_csv(path: Path, buckets: list[CouplingBucket], roles: dict[tuple[str, str], str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [bucket.row(roles[(bucket.key_type, bucket.key)]) for bucket in buckets]
    rows.sort(key=lambda row: (str(row["key_type"]), -int(row["count"]), str(row["key"])))
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), delimiter=";")
        writer.writeheader()
        writer.writerows(rows)


def _write_markdown(
    path: Path,
    melody_path: Path,
    episodes_path: Path,
    csv_path: Path,
    matched_count: int,
    buckets: list[CouplingBucket],
    roles: dict[tuple[str, str], str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report_id = path.stem.split("_", 1)[0]
    role_counts = Counter(roles.values())
    phrase_buckets = [bucket for bucket in buckets if bucket.key_type == "phrase_symbol"]
    token_buckets = [bucket for bucket in buckets if bucket.key_type == "speech_token"]
    tone_buckets = [bucket for bucket in buckets if bucket.key_type == "tone_role"]

    def top_rows(source: list[CouplingBucket], limit: int = 12) -> list[CouplingBucket]:
        return sorted(source, key=lambda bucket: (-bucket.count, bucket.key))[:limit]

    lines = [
        f"# {report_id} - Marktmelodie MCM-Kopplung",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft passiv, ob Klangrollen, Melodiephrasen und DIO-Klangtokens wiederkehrend mit MCM-Innenfeldlagen zusammenfallen.",
        "Sie erzeugt keine Handlung, kein Gate und keine Vorhersage.",
        "",
        "Hierarchie:",
        "",
        "1. Die Aussenwelt wird als Tonfolge gelesen.",
        "2. Die gleiche Welt wird ueber MINI_DIO als Innenfeldspur gelesen.",
        "3. Beide Spuren werden zeitlich gekoppelt.",
        "4. Geprueft wird nur, ob Klangformen und Innenfeldqualitaeten gemeinsam wiederkehren.",
        "",
        "## Quellen",
        "",
        f"- Melodie: `{melody_path}`",
        f"- Episoden: `{episodes_path}`",
        f"- CSV: `{csv_path}`",
        f"- gekoppelte Frames: `{matched_count}`",
        "",
        "## Kopplungsrollen",
        "",
        "| Rolle | Anzahl |",
        "|---|---:|",
    ]
    for role, count in role_counts.most_common():
        lines.append(f"| {role} | {count} |")
    lines.extend(["", "## Dominante Melodiephrasen", "", "| Phrase | Anzahl | Rolle | MCM-Klasse | Innenlage | Carry | Strain | Rekopplung |", "|---|---:|---|---|---|---:|---:|---:|"])
    for bucket in top_rows(phrase_buckets):
        lines.append(
            "| `{}` | {} | {} | {} | {} | {} | {} | {} |".format(
                bucket.key,
                bucket.count,
                roles[(bucket.key_type, bucket.key)],
                _dominant(bucket.mcm_classes),
                _dominant(bucket.inner_states),
                _fmt(_mean(bucket.carry)),
                _fmt(_mean(bucket.strain)),
                _fmt(_mean(bucket.rekopplung)),
            )
        )
    lines.extend(["", "## Dominante DIO-Klangtokens", "", "| Token | Anzahl | Rolle | Tonrolle | MCM-Klasse | Carry | Strain |", "|---|---:|---|---|---|---:|---:|"])
    for bucket in top_rows(token_buckets):
        lines.append(
            "| `{}` | {} | {} | {} | {} | {} | {} |".format(
                bucket.key,
                bucket.count,
                roles[(bucket.key_type, bucket.key)],
                _dominant(bucket.tone_roles),
                _dominant(bucket.mcm_classes),
                _fmt(_mean(bucket.carry)),
                _fmt(_mean(bucket.strain)),
            )
        )
    lines.extend(["", "## Klangrollen gegen MCM-Feld", "", "| Klangrolle | Anzahl | Rolle | MCM-Klasse | Innenlage | Carry | Strain | Rekopplung |", "|---|---:|---|---|---|---:|---:|---:|"])
    for bucket in top_rows(tone_buckets, limit=20):
        lines.append(
            "| {} | {} | {} | {} | {} | {} | {} | {} |".format(
                bucket.key,
                bucket.count,
                roles[(bucket.key_type, bucket.key)],
                _dominant(bucket.mcm_classes),
                _dominant(bucket.inner_states),
                _fmt(_mean(bucket.carry)),
                _fmt(_mean(bucket.strain)),
                _fmt(_mean(bucket.rekopplung)),
            )
        )
    lines.extend(
        [
            "",
            "## Befund",
            "",
            "Die Marktmelodie koppelt in dieser Diagnose nicht direkt in das MCM-Feld, sondern wird neben die bereits entstandene Innenfeldspur gelegt.",
            "Damit wird sichtbar, ob ein Klangmuster nur akustische Oberflaeche bleibt oder wiederholt in aehnlicher Feldwirkung erscheint.",
            "",
            "Wenn eine Melodiephrase wiederkehrend mit hoher Carry-Qualitaet und Rekopplung erscheint, ist das ein Hinweis auf eine tragende Klangnaehe.",
            "Wenn sie mit erhoehter Strain-Qualitaet erscheint, ist das ein Hinweis auf belastete Klangnaehe.",
            "Offene Kopplungen bleiben beobachtbar, ohne sofort Bedeutung zu erzwingen.",
            "",
            "## Wie es weitergeht",
            "",
            "Als naechstes sollte geprueft werden, ob diese Klangkopplungen in einer anderen Welt wieder auftauchen oder ob sie nur situationsgebundene Klang-Innenfeld-Inseln dieser Stresswelt sind.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Koppelt eine passive Marktmelodie mit MINI_DIO-MCM-Episoden.")
    parser.add_argument("--melody", type=Path, default=MELODY_DEFAULT)
    parser.add_argument("--episodes", type=Path, default=EPISODES_DEFAULT)
    parser.add_argument("--csv-out", type=Path, default=CSV_DEFAULT)
    parser.add_argument("--md-out", type=Path, default=MD_DEFAULT)
    args = parser.parse_args()

    melody_path = args.melody if args.melody.is_absolute() else ROOT / args.melody
    episodes_path = args.episodes if args.episodes.is_absolute() else ROOT / args.episodes
    csv_path = args.csv_out if args.csv_out.is_absolute() else ROOT / args.csv_out
    md_path = args.md_out if args.md_out.is_absolute() else ROOT / args.md_out

    melody_rows = _read_csv(melody_path, delimiter=";")
    episode_rows = _read_csv(episodes_path, delimiter=",")
    matched = _match_rows(melody_rows, episode_rows)
    buckets = _build_buckets(matched)
    roles = _assign_roles(buckets)
    _write_csv(csv_path, buckets, roles)
    _write_markdown(md_path, melody_path, episodes_path, csv_path, len(matched), buckets, roles)
    print(f"melody={melody_path}")
    print(f"episodes={episodes_path}")
    print(f"matched={len(matched)}")
    print(f"buckets={len(buckets)}")
    print(f"wrote {csv_path}")
    print(f"wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
