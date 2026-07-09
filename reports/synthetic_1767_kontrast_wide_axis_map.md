# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:19:04

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1767_kontrast_wide_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1767_A_1000_2500 | SYN1767_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7480 | 0.7480 | 0.0000 | 0.0000 | 0.7353 | 1494 | 0 | 0 | 0 |
| SYN1767_A_2000_3500 | SYN1767_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7496 | 0.7496 | 0.0000 | 0.0000 | 0.7450 | 1494 | 0 | 0 | 0 |
| SYN1767_A_1000_3000 | SYN1767_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7490 | 0.7490 | 0.0000 | 0.0000 | 0.7542 | 1994 | 0 | 0 | 0 |
| SYN1767_B_1000_2500 | SYN1767_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7476 | 0.7476 | 0.0000 | 0.0000 | 0.7273 | 1494 | 0 | 0 | 0 |
| SYN1767_B_2000_3500 | SYN1767_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7479 | 0.7479 | 0.0000 | 0.0000 | 0.7278 | 1494 | 0 | 0 | 0 |
| SYN1767_B_1000_3000 | SYN1767_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7487 | 0.7487 | 0.0000 | 0.0000 | 0.7558 | 1994 | 0 | 0 | 0 |
| SYN1767_C_1000_2500 | SYN1767_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7480 | 0.7480 | 0.0000 | 0.0000 | 0.7356 | 1494 | 0 | 0 | 0 |
| SYN1767_C_2000_3500 | SYN1767_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7493 | 0.7493 | 0.0000 | 0.0000 | 0.7397 | 1494 | 0 | 0 | 0 |
| SYN1767_C_1000_3000 | SYN1767_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7487 | 0.7487 | 0.0000 | 0.0000 | 0.7523 | 1994 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `9`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0000 | 0.0000 |
| Erfahrung | 0.0000 | 0.0000 | 0.0000 |
| Gewicht carry | 0.4200 | 0.4200 | 0.0000 |
| Gewicht alignment | 0.2400 | 0.2400 | 0.0000 |
| Gewicht strain_relief | 0.2000 | 0.2000 | 0.0000 |
| Gewicht sensory | 0.1400 | 0.1400 | 0.0000 |

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

Die adaptive Rekopplung wird als passive Zusatzlesung ausgewiesen. Sie zeigt, ob Erfahrung die Rueckfuehrung gegenueber der statischen Referenz anhebt, daempft oder nahe am Grundwert haelt.

Wenn die adaptiven Gewichte nur sehr wenig streuen, ist die Schicht technisch aktiv, aber noch nicht stark welt- oder familienselektiv. Dann liegt die naechste Arbeit nicht in mehr Daten, sondern in genauerer Erfahrungskopplung pro Feldrolle.

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.
