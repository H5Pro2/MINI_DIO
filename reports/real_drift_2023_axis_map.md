# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 13:40:30

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\real_drift_2023_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2023_A | SOL_2023_DRIFT | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.7077 | 0.7432 | 0.0356 | 0.7428 | 0.6575 | 9875 | 119 | 0 | 0 |
| REAL_DRIFT_2023_B | SOL_2023_DRIFT | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.7070 | 0.7413 | 0.0343 | 0.7461 | 0.6601 | 9888 | 106 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0343 | 0.0356 | 0.0013 |
| Erfahrung | 0.7428 | 0.7461 | 0.0032 |
| Gewicht carry | 0.2972 | 0.3002 | 0.0030 |
| Gewicht alignment | 0.2197 | 0.2204 | 0.0007 |
| Gewicht strain_relief | 0.2700 | 0.2716 | 0.0016 |
| Gewicht sensory | 0.2094 | 0.2115 | 0.0021 |

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
