# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 13:48:54

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\real_drift_2024_2025_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2024_A | SOL_2024_DRIFT | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7068 | 0.7417 | 0.0350 | 0.7515 | 0.6605 | 9924 | 70 | 0 | 0 |
| REAL_DRIFT_2025_A | SOL_2025_DRIFT | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.7066 | 0.7406 | 0.0340 | 0.7708 | 0.6648 | 9913 | 81 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `1`
- `mittlere_uebergangsphase`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0340 | 0.0350 | 0.0010 |
| Erfahrung | 0.7515 | 0.7708 | 0.0193 |
| Gewicht carry | 0.2984 | 0.3008 | 0.0024 |
| Gewicht alignment | 0.2200 | 0.2205 | 0.0005 |
| Gewicht strain_relief | 0.2694 | 0.2708 | 0.0014 |
| Gewicht sensory | 0.2094 | 0.2108 | 0.0014 |

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
