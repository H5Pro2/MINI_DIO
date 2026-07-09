# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:07:03

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1765_b_focus_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1765_2400_3900_TO_2800_4300 | SYN1765_B_FOCUS | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7504 | 0.7504 | 0.0000 | 0.0000 | 0.7505 | 1494 | 0 | 0 | 0 |
| SYN1765_2800_4300_TO_3000_4500 | SYN1765_B_FOCUS | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7537 | 0.7537 | 0.0000 | 0.0000 | 0.8082 | 1494 | 0 | 0 | 0 |
| SYN1765_3000_4500_TO_3200_4700 | SYN1765_B_FOCUS | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7535 | 0.7845 | 0.0311 | 0.0807 | 0.7870 | 1493 | 1 | 0 | 0 |
| SYN1765_2400_4400_TO_2800_4800 | SYN1765_B_FOCUS_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7525 | 0.7525 | 0.0000 | 0.0000 | 0.7841 | 1994 | 0 | 0 | 0 |
| SYN1765_2800_4800_TO_3000_5000 | SYN1765_B_FOCUS_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7542 | 0.7542 | 0.0000 | 0.0000 | 0.8090 | 1994 | 0 | 0 | 0 |
| SYN1765_3000_5000_TO_3200_5200 | SYN1765_B_FOCUS_WIDE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7527 | 0.7855 | 0.0328 | 0.0848 | 0.7880 | 1993 | 1 | 0 | 0 |
| SYN1765_2600_5100_TO_3000_5000 | SYN1765_B_FOCUS_LONG | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7497 | 0.7565 | 0.0068 | 0.0099 | 0.7679 | 2494 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `5`
- `mittlere_uebergangsphase`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0328 | 0.0328 |
| Erfahrung | 0.0000 | 0.0848 | 0.0848 |
| Gewicht carry | 0.3107 | 0.4200 | 0.1093 |
| Gewicht alignment | 0.2209 | 0.2400 | 0.0191 |
| Gewicht strain_relief | 0.2000 | 0.2631 | 0.0631 |
| Gewicht sensory | 0.1400 | 0.2052 | 0.0652 |

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
