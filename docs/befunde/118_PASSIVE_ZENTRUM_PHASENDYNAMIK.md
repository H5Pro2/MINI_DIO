# 118 - Passive Zentrum-Phasendynamik

Datum: 2026-06-18

## Grundfrage

Besitzt auch das Zentrum eine eigene Vorlauf-/Ruecklaufstruktur,
oder ist es nur ein statischer Mittelpunkt?

## Unterpruefung

Alle `zentrum`-Zustaende wurden ueber die vier grossen Welten passiv gelesen.

Geprueft wurden:

- Offset-Fenster `-3` bis `+3`
- Zentrum-Segmente
- Rollen vor und nach Zentrum
- dominante Zentrum-Merkmale

Skript:

`DIO_MINI/report_passive_center_phase_dynamics.py`

Ausgabe:

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_offset_profile.csv`

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_transition_pairs.csv`

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_segments.csv`

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_segment_summary.csv`

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_features.csv`

`debug/dio_mini_passive_center_phase_dynamics_20260618/center_phase_dynamics_summary.json`

## Ergebnis

Zentrum-Ereignisse:

`123223`

Zentrum-Segmente:

`63449`

Mittlere Segmentlaenge:

`1.942079`

Maximale Segmentlaenge:

`16`

Segmentklassen:

- kurzer Zentrumskontakt: `33546`
- Zentrum haelt kurz: `22410`
- Zentrumslauf: `7283`
- langes Zentrum: `210`

Dominante Rolle vor Zentrum:

`tragende_bruecke`

Dominante Rolle nach Zentrum:

`tragende_bruecke`

## Offset-Lesung

Zentrum bleibt im Vor- und Ruecklauf dominant:

- Offset `-3`: Zentrum-Anteil `0.357694`
- Offset `-2`: Zentrum-Anteil `0.390864`
- Offset `-1`: Zentrum-Anteil `0.485088`
- Offset `0`: Zentrum-Anteil `1.0`
- Offset `1`: Zentrum-Anteil `0.485092`
- Offset `2`: Zentrum-Anteil `0.390873`
- Offset `3`: Zentrum-Anteil `0.357702`

Gleichzeitig steigen an den Raendern die Brueckenanteile.

Das bedeutet:
Zentrum ist nicht isoliert.
Zentrum besitzt eine Peripherie,
ueber die es mit tragenden Bruecken gekoppelt ist.

## Zentrum-Merkmale

Dominante Zentrum-Merkmale:

- `feld_coherence_positive`: `0.849176`
- `feld_tension_mid`: `0.825617`
- `sehen_motion_mid`: `0.794884`
- `hoeren_tone_mid`: `0.783198`
- `folge_strain_bleibt`: `0.715142`
- `folge_rekopplung_bleibt`: `0.636854`
- `sehen_neutral`: `0.519035`

Passiv gelesen:

Zentrum ist keine Reizlosigkeit.
Zentrum ist eine aktive Stabilisationslage:
positive Feldkohaerenz,
mittlere Spannung,
mittlere Bewegung,
mittlere Tonlage
und haltender Strain/Rekopplung.

## MCM-Schluss

Zentrum ist kein leerer Nullpunkt.

Zentrum ist eine organisierende Feldphase.

Es besitzt:

- Vorlauf,
- Ruecklauf,
- kurze und lange Segmente,
- Brueckenperipherie,
- eigene multisensorische Signatur.

Damit wird die MCM-Topologie konkreter:

Die `0` ist nicht Abwesenheit.
Die `0` ist eine aktive Rueckfuehrungs- und Organisationslage.

## Bedeutung fuer Mini-DIO

Mini-DIO liest Zentrum nicht nur als Wert.

Mini-DIO liest Zentrum als Zustand,
der von Bruecken getragen wird
und nach Drift oder Uebergang wieder erreicht werden kann.

Das ist relevant fuer spaetere organische Regulation:
Regulation bedeutet nicht,
einen Wert auf `0` zu zwingen.
Regulation bedeutet,
Rueckfuehrungsbewegungen zum Zentrum passiv zu erkennen
und ihre Tragfaehigkeit zu lernen.

## Grenze des Befunds

Die Analyse bleibt passiv.

Sie erzeugt keine Handlung,
kein Gate
und kein Entry-Signal.

Sie beschreibt eine Feldordnung,
keinen Handelsmechanismus.

## Wie es weitergeht

Grundfrage:

Wie verhalten sich Zentrum,
Drift
und Uebergang gemeinsam als zyklische Feldbewegung?

Unterpruefung:

Sequenzen lesen:

- Zentrum -> Drift -> Zentrum
- Zentrum -> Uebergang -> Zentrum
- Bruecke -> Zentrum -> Bruecke
- Drift -> Zentrum -> Bruecke
- Uebergang -> Zentrum -> Bruecke

Folgeschritt:

Passive MCM-Zykluskarte bauen.
