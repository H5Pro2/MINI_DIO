# 110 - `nu25d5` Rollen-Drift-Lupe

## Zweck

Diese Datei isoliert `nu25d5`,
weil diese Spur im Jahres-Haertetest
als einzige Zielraumrolle driftete.

Ausgangspunkt:

- `109_MCM_TOPOLOGIE_JAHRES_HAERTETEST.md`

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Skript

`DIO_MINI/report_passive_nu25d5_role_drift_lupe.py`

## Eingabe

Verglichen wurden:

- Basis-Zugangsdynamik:
  `debug/dio_mini_passive_target_access_dynamics_20260618/target_access_dynamics_by_pair.csv`
- Jahres-Haertetest:
  `debug/dio_mini_passive_target_access_dynamics_year_hardtest_20260618/target_access_dynamics_by_pair.csv`

## Ausgabe

Ordner:

`debug/dio_mini_passive_nu25d5_role_drift_lupe_20260618/`

Dateien:

- `nu25d5_role_drift_rows.csv`
- `nu25d5_role_drift_compare.csv`
- `nu25d5_role_drift_summary.json`

## Ergebnis

Der staerkste Zugang zu `nu25d5` bleibt stabil:

```text
po4hjv -> nu25d5
```

Basis:

- Anteil am Zielraum: `0.356944`
- dominante Bewegungsqualitaet: `tragend_fallend`
- Belastungsanteil: `0.220260`
- Tragend-fallend-Anteil: `0.424935`

Jahres-Haertetest:

- Anteil am Zielraum: `0.333333`
- dominante Bewegungsqualitaet: `tragend_fallend`
- Belastungsanteil: `0.187888`
- Tragend-fallend-Anteil: `0.452127`

## Wichtige Verschiebungen

Die Hauptkopplung bleibt gleich.

Die Rollenverschiebung entsteht nicht,
weil `nu25d5` ploetzlich aus einer voellig anderen Quelle kommt.

Sie entsteht,
weil sich die Gesamtverteilung im groesseren Feld verschiebt:

- `po4hjv -> nu25d5` bleibt dominant.
- `rj8h9z -> nu25d5` wechselt von `belastend` zu `tragend_fallend`.
- `nh7ss1 -> nu25d5` wechselt von `belastend` zu `tragend_fallend`.
- Belastungsanteile sinken bei mehreren Zugaengen.
- Die Spur bleibt belastungsnah,
  aber bekommt mehr entlastende/offene Brueckenqualitaet.

## MCM-Lesung

`nu25d5` ist kein instabiler Fehlerpunkt.

Es wirkt eher wie ein Uebergangsbereich:

```text
Randspannung
<-> offene entlastende Bruecke
```

In kleineren kontrollierten Welten wird die Randspannung staerker gelesen.

In groesseren Jahreswelten wird dieselbe Spur
staerker als offene Brueckenbewegung lesbar.

## Schluss

Der beste aktuelle Befund lautet:

```text
nu25d5_is_transition_zone_between_tension_edge_and_open_relief_bridge
```

Das ist fuer die MCM-Topologie wichtig:

Nicht jede Rolle ist starr.
Einige Bereiche koennen Uebergangszonen sein,
die je nach Weltvarianz anders gelesen werden,
ohne ihre Grundkopplung zu verlieren.

## Wie es weitergeht

Grundfrage:

Gibt es weitere Zielraeume,
die als Uebergangszonen wirken,
oder ist `nu25d5` aktuell der einzige klare Rollen-Drift-Bereich?

Unterpruefung:

Alle Zielraeume nach Rollenstabilitaet,
Qualitaetswechseln und Belastungsverschiebung vergleichen.

Folgeschritt:

Passive Rollenstabilitaets- und Uebergangszonenkarte bauen.
