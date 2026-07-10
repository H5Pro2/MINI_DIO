# 2088 - Passive Antwort-Erfahrungsbreite

## Zweck

Die passive Antwort-Memory enthält nach Befund 2087 insgesamt 222 Beobachtungen in 32 Familien-Komponenten-Identitäten. Dieser Lauf vermisst ihre innere Breite, ohne aus Streuung oder Richtung neue Klassen zu bilden.

Beobachtungspersistenz ist der Betrag der Vorzeichenbilanz aller Einzelwerte. Quellenpersistenz berechnet dieselbe Bilanz aus den Mittelwerten der Evidenzquellen. Beide liegen kontinuierlich zwischen `0` und `1`; sie sind Forschungsmaße, keine Reifeschwellen.

## Gesamtprofil

- Antwortidentitäten: `32`
- vermessene Antwortachsen: `96`
- vollständig gleichgerichtete Beobachtungsachsen: `31`
- vollständig gleichgerichtete Quellenachsen: `67`
- Achsen mit mindestens einem Quellen-Vorzeichenwechsel: `25`
- Achsen mit 6 Beobachtungen aus 2 Quellen: `84`
- Achsen mit 11 Beobachtungen aus 3 Quellen: `9`
- Achsen mit 21 Beobachtungen aus 5 Quellen: `3`
- Memory- oder Runtime-Änderung: `0`

## rf_05:volume

| Achse | positiv/negativ/null | Beobachtungspersistenz | Quellenpfad | Quellenpersistenz | MAD | Persistenzperzentil |
|---|---:|---:|---|---:|---:|---:|
| `continuity` | 13/8/0 | 0.238 | `1;1;1;1;-1` | 0.600 | 0.0326 | 0.141 |
| `event_share` | 21/0/0 | 1.000 | `1;1;1;1;1` | 1.000 | 0.0008 | 0.844 |
| `member_coverage` | 13/8/0 | 0.238 | `1;1;1;1;-1` | 0.600 | 0.0278 | 0.328 |

## Höchste Richtungsbilanzen

Die Tabelle ist nur eine Sortierung kontinuierlicher Werte und keine Auswahl tragender Klassen.

| Familie | Komponente | Achse | Beobachtungen/Quellen | Beobachtungspersistenz | Quellenpersistenz | positiv/negativ |
|---|---|---|---:|---:|---:|---:|
| `rf_05` | `volume` | `event_share` | 21/5 | 1.000 | 1.000 | 21/0 |
| `rf_06` | `sign` | `event_share` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_06` | `sign` | `member_coverage` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_06` | `volume` | `continuity` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_06` | `volume` | `event_share` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_06` | `volume` | `member_coverage` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_07` | `volume` | `continuity` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_07` | `volume` | `event_share` | 6/2 | 1.000 | 1.000 | 6/0 |
| `rf_07` | `wick` | `continuity` | 6/2 | 1.000 | 1.000 | 0/6 |
| `rf_08` | `magnitude` | `continuity` | 6/2 | 1.000 | 1.000 | 6/0 |

## Befund

`rf_05:volume` trägt auf der Ereignisanteil-Achse `21/21` positive Beobachtungen und den Quellenpfad `1;1;1;1;1`. Beobachtungs- und Quellenpersistenz liegen bei `1.000` und `1.000`. Innerhalb der 32 Ereignisanteil-Achsen liegt seine Beobachtungspersistenz am Perzentil `0.844`.

Vollständige Ereignisanteil-Persistenz ist nicht allein `rf_05` vorbehalten: `10/32` Ereignisanteil-Achsen erreichen den Wert `1.000`. Die Evidenztiefe ist jedoch ungleich verteilt. `84/96` Achsen beruhen nur auf sechs Beobachtungen aus zwei Quellen; lediglich `3/96` besitzen 21 Beobachtungen aus fünf Quellen. Unter diesen tief vermessenen Achsen bleibt genau `1` auf Beobachtungs- und Quellenebene vollständig gleichgerichtet: `rf_05:volume:event_share`.

Kontinuität und Mitgliederabdeckung tragen jeweils `13/8` beziehungsweise `13/8` positive/negative Beobachtungen. Ihre Beobachtungspersistenzen liegen nur bei `0.238` und `0.238`; die widersprechende Erfahrung aus 2086 bleibt damit als reale Breite sichtbar und wird nicht durch den positiven Mittelwert verdeckt.

Über die gesamte Memory sind `31/96` Achsen auf Beobachtungsebene und `67/96` auf Quellenebene vollständig gleichgerichtet. Die heutige Memory erlaubt daher eine belastbarere Aussage zur inneren Breite von `rf_05:volume` als zum Vergleich mit den übrigen 31 Identitäten. Deren Evidenztiefe muss erst wachsen, bevor gleiche Persistenzwerte gleichgewichtig verglichen werden können.

## Organische Grenze

Die Karte ergänzt keine Memory-Felder und wird nicht von MINI_DIO gelesen. Vorzeichenbalance, Streuung und Quellenpfade bleiben Auswertungen vorhandener Erfahrung. Es entstehen keine Kategorien wie stabil oder plastisch, keine Schwellen und keine Handlungswirkung.
