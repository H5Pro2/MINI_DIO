from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "docs" / "befunde" / "1386_BRUECKE_ZENTRUM_UNTERFORMEN_WIEDERKEHR.csv"
OUT_CSV = ROOT / "docs" / "befunde" / "1387_UNTERFORMEN_SEMANTISCHE_WIEDERKEHR.csv"
OUT_MD = ROOT / "docs" / "befunde" / "1387_UNTERFORMEN_SEMANTISCHE_WIEDERKEHR.md"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _top(counter: Counter[str], n: int = 6) -> str:
    return ", ".join(f"{name}:{count}" for name, count in counter.most_common(n)) or "-"


def build_report() -> None:
    rows = _read_csv(INPUT)
    reference = [row for row in rows if row.get("is_reference_target") == "1"]
    outside_seen = [
        row
        for row in rows
        if row.get("is_reference_target") != "1" and row.get("signature_seen_in_reference") == "1"
    ]
    if not reference:
        raise RuntimeError("missing reference rows")

    ref_families_by_signature: dict[str, set[str]] = defaultdict(set)
    ref_previews_by_signature: dict[str, set[str]] = defaultdict(set)
    ref_signature_counts = Counter(row["mischlinien_signature"] for row in reference)
    for row in reference:
        signature = row["mischlinien_signature"]
        ref_families_by_signature[signature].add(row.get("family", "-"))
        ref_previews_by_signature[signature].add(row.get("preview", "-"))

    out_rows: list[dict[str, str]] = []
    for row in outside_seen:
        signature = row["mischlinien_signature"]
        family = row.get("family", "-")
        preview = row.get("preview", "-")
        same_family = family in ref_families_by_signature[signature]
        same_preview = preview in ref_previews_by_signature[signature]
        semantic_binding = "none"
        if same_family and same_preview:
            semantic_binding = "family_and_preview"
        elif same_family:
            semantic_binding = "family"
        elif same_preview:
            semantic_binding = "preview"
        out = dict(row)
        out["reference_signature_count"] = str(ref_signature_counts[signature])
        out["reference_families"] = "|".join(sorted(ref_families_by_signature[signature]))
        out["reference_previews"] = "|".join(sorted(ref_previews_by_signature[signature]))
        out["same_family_as_reference"] = "1" if same_family else "0"
        out["same_preview_as_reference"] = "1" if same_preview else "0"
        out["semantic_binding"] = semantic_binding
        out_rows.append(out)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out_rows[0].keys()) if out_rows else list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    binding_counts = Counter(row["semantic_binding"] for row in out_rows)
    role_binding: dict[str, Counter[str]] = defaultdict(Counter)
    world_binding: dict[str, Counter[str]] = defaultdict(Counter)
    signature_binding: dict[str, Counter[str]] = defaultdict(Counter)
    family_counts = Counter(row.get("family", "-") for row in out_rows)
    preview_counts = Counter(row.get("preview", "-") for row in out_rows)
    for row in out_rows:
        role_binding[row.get("passive_role_near", "-")][row["semantic_binding"]] += 1
        world_binding[row.get("world", "-")][row["semantic_binding"]] += 1
        signature_binding[row.get("mischlinien_signature", "-")][row["semantic_binding"]] += 1

    role_lines = [
        f"- `{role}`: {_top(counter, 4)}"
        for role, counter in sorted(role_binding.items())
    ]
    world_lines = [
        f"- `{world}`: {_top(counter, 4)}"
        for world, counter in sorted(world_binding.items())
    ]
    signature_lines = [
        f"- `{signature}`: {_top(counter, 4)}"
        for signature, counter in sorted(signature_binding.items(), key=lambda item: sum(item[1].values()), reverse=True)[:8]
    ]

    same_family_count = sum(1 for row in out_rows if row["same_family_as_reference"] == "1")
    same_preview_count = sum(1 for row in out_rows if row["same_preview_as_reference"] == "1")
    semantic_count = sum(1 for row in out_rows if row["semantic_binding"] != "none")

    lines = [
        "# 1387 - Unterformen: semantische Wiederkehr",
        "",
        "## Zweck",
        "",
        "Diese Diagnose prueft, ob wiederkehrende Unterformen aus `1386` nur sensorisch aehnlich sind oder auch semantisch an denselben Familien- oder Preview-Kern koppeln.",
        "",
        "Referenz ist weiterhin die Bruecke/Zentrum-Mischrolle aus `1385`.",
        "Geprueft werden nur Fenster ausserhalb dieser Referenz, deren Unterform in der Referenz bereits vorkam.",
        "",
        "Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.",
        "",
        "## Befund",
        "",
        f"- Referenzfenster: `{len(reference)}`",
        f"- Wiederkehrfenster ausserhalb der Referenz: `{len(out_rows)}`",
        f"- gleiche Familie wie Referenzsignatur: `{same_family_count}`",
        f"- gleicher Preview-Kern wie Referenzsignatur: `{same_preview_count}`",
        f"- irgendeine semantische Kopplung: `{semantic_count}`",
        f"- Bindungsklassen: `{_top(binding_counts, 6)}`",
        f"- dominante Familien ausserhalb: `{_top(family_counts, 8)}`",
        f"- dominante Previews ausserhalb: `{_top(preview_counts, 8)}`",
        "",
        "## Semantische Kopplung nach Rollen",
        "",
        *role_lines,
        "",
        "## Semantische Kopplung nach Welten",
        "",
        *world_lines,
        "",
        "## Dominante Signaturen",
        "",
        *signature_lines,
        "",
        "## Lesung",
        "",
        "Wenn Unterformen ausserhalb der Referenz denselben Familien- oder Preview-Kern tragen, ist die Wiederkehr nicht nur sensorisch.",
        "Dann koppelt eine Oberflaechenverwandtschaft an eine gespeicherte Bedeutungsnaehe.",
        "",
        "Wenn dagegen viele Wiederkehren ohne semantische Bindung bleiben, ist die Aehnlichkeit eher oberflaechlich oder noch nicht gereift.",
        "",
        "Dieser Befund hilft, zwischen reiner Sinnesnaehe und echter Bedeutungsnaehe im MCM-Feld zu unterscheiden.",
        "",
        "## Grenze",
        "",
        "Familie und Preview sind interne MINI_DIO-Syntax, keine menschliche Bedeutung.",
        "Der Befund zeigt semantische Naehe im System, nicht eine externe Interpretation.",
        "",
        "## Wie es weitergeht",
        "",
        "Als naechstes sollte geprueft werden, ob semantisch gebundene Wiederkehr spaeter stabilere Feldzeit, geringeren Strain oder staerkere Rekopplung zeigt als reine Oberflaechenwiederkehr.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_report()
