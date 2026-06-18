# 120 - Passive MCM-Zykluskarte

Datum: 2026-06-18

## Grundfrage

Wie verhalten sich Zentrum,
Drift
und Uebergang gemeinsam als zyklische Feldbewegung?

## Unterpruefung

Aus den Rollenfolgen der vier grossen Welten wurden Sequenzen gelesen:

- Laenge `3`
- Laenge `4`
- Laenge `5`

Die Sequenzen wurden passiv klassifiziert,
unter anderem als:

- `zentrum_haelt`
- `zentrum_drift_zentrum`
- `zentrum_uebergang_zentrum`
- `bruecke_zentrum_bruecke`
- `drift_zentrum_bruecke`
- `uebergang_zentrum_bruecke`
- `rueckfuehrung_zum_zentrum`
- `auslauf_aus_zentrum`

Skript:

`DIO_MINI/report_passive_mcm_cycle_map.py`

Ausgabe:

`debug/dio_mini_passive_mcm_cycle_map_20260618/mcm_cycle_sequences.csv`

`debug/dio_mini_passive_mcm_cycle_map_20260618/mcm_cycle_class_summary.csv`

`debug/dio_mini_passive_mcm_cycle_map_20260618/mcm_target_cycle_sequences.csv`

`debug/dio_mini_passive_mcm_cycle_map_20260618/mcm_cycle_map_summary.json`

## Ergebnis

Es wurden `9280` unterschiedliche Sequenzzeilen gelesen.

Zyklusklassen:

- `rueckfuehrung_zum_zentrum`: `233588`
- `auslauf_aus_zentrum`: `233577`
- `offene_peripherie_bewegung`: `229327`
- `zentrum_bruecken_kopplung`: `97809`
- `bruecke_zentrum_bruecke`: `66331`
- `zentrum_haelt`: `51676`
- `zentrum_uebergang_zentrum`: `23766`
- `uebergang_zentrum_bruecke`: `22122`
- `drift_zentrum_bruecke`: `20526`
- `zentrum_drift_zentrum`: `18748`

## Zentrale Zyklen

### Zentrum haelt

Staerkste Sequenzen:

- `zentrum -> zentrum -> zentrum`
  - `29871`
  - Weltpraesenz: `4`
  - Carry `0.452512`
  - Strain `0.180881`
  - Rekopplung `0.703577`
- `zentrum -> zentrum -> zentrum -> zentrum`
  - `14649`
  - Weltpraesenz: `4`
- `zentrum -> zentrum -> zentrum -> zentrum -> zentrum`
  - `7156`
  - Weltpraesenz: `4`

Lesung:

Zentrum kann sich selbst halten.
Wenn Zentrum laenger haelt,
steigen Carry und Rekopplung leicht.

### Bruecke -> Zentrum -> Bruecke

Staerkste Sequenz:

- `tragende_bruecke -> zentrum -> tragende_bruecke`
  - `4122`
  - Weltpraesenz: `4`
  - Carry `0.421535`
  - Strain `0.180855`
  - Rekopplung `0.687147`

Weitere tragende Sequenzen:

- `entlastende_bruecke -> zentrum -> tragende_bruecke`
- `tragende_bruecke -> zentrum -> zentrum -> tragende_bruecke`
- `entlastende_bruecke_mit_offener_varianz -> zentrum -> tragende_bruecke`

Lesung:

Zentrum ist nicht isoliert.
Zentrum wird haeufig ueber Bruecken betreten
und wieder ueber Bruecken verlassen.

Das bestaetigt die Brueckenperipherie des Zentrums.

### Zentrum -> Drift -> Zentrum

Staerkste Sequenz:

- `zentrum -> selbstnahe_drift -> zentrum`
  - `2308`
  - Weltpraesenz: `4`
  - Carry `0.38085`
  - Strain `0.167651`
  - Rekopplung `0.670815`

Lesung:

Drift ist eine Rueckkehrfaehige Abweichung.
Sie fuehrt nicht zwingend in Zerfall,
sondern kann in Zentrum zuruecklaufen.

### Zentrum -> Uebergang -> Zentrum

Staerkste Sequenz:

- `zentrum -> uebergangszone -> zentrum`
  - `4686`
  - Weltpraesenz: `4`
  - Carry `0.418558`
  - Strain `0.192544`
  - Rekopplung `0.682973`

Lesung:

Uebergang ist eine Rekopplungsbewegung.
Sie liegt haeufig zwischen Zentrum-Zustaenden
und bleibt in allen vier Welten sichtbar.

### Drift / Uebergang -> Zentrum -> Bruecke

Staerkste Drift-Sequenz:

- `selbstnahe_drift -> zentrum -> tragende_bruecke`
  - `2137`
  - Weltpraesenz: `4`

Staerkste Uebergangs-Sequenz:

- `uebergangszone -> zentrum -> tragende_bruecke`
  - `2934`
  - Weltpraesenz: `4`

Lesung:

Drift und Uebergang muessen nicht im Zentrum enden.
Sie koennen ueber Zentrum in eine tragende Bruecke laufen.

Das ist eine wichtige passive Regulationsbewegung:
Abweichung oder Uebergang werden nicht nur neutralisiert,
sondern koennen in tragende Peripherie ueberfuehrt werden.

## MCM-Schluss

Die MCM-Feldordnung zeigt zyklische Bewegungen.

Nicht nur:

`Zustand A ist vorhanden.`

Sondern:

`Zustand A geht in Zustand B ueber und findet Rueckfuehrung oder Brueckenkopplung.`

Die staerksten Zielzyklen sind in allen vier Welten praesent.

Damit wird der Befund zur MCM-Feld-Eigenregulation staerker:

- Zentrum haelt sich.
- Zentrum wird von Bruecken getragen.
- Drift kann zurueckfuehren.
- Uebergang kann rekoppeln.
- Drift/Uebergang koennen ueber Zentrum in Bruecken laufen.

## Grenze des Befunds

Die Zykluskarte bleibt passiv.

Sie ist keine Handlungslogik,
kein Gate
und kein Entry-Signal.

Sie zeigt wiederkehrende Feldbewegungen,
aber keine harte Kausalitaet.

## Bedeutung fuer Mini-DIO

Mini-DIO kann nicht nur Bedeutungsraeume lesen.

Mini-DIO kann auch Bewegungen zwischen Bedeutungsraeumen lesen.

Das ist eine wichtige Stufe:

Von passiver Topologie
zu passiver Feldkinematik.

## Wie es weitergeht

Grundfrage:

Sind diese Zyklen nur haeufig,
oder tragen sie unterschiedliche Qualitaet?

Unterpruefung:

Zyklen nach Carry,
Strain,
Rekopplung
und Weltpraesenz bewerten.

Folgeschritt:

Passive Zyklus-Reife pruefen:
Welche Zyklen wirken stabil,
welche offen,
welche belastet,
welche reorganisierend?
