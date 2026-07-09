# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 16:31:10

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\paxg_1h_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_1H_FOLLOW_4000_5000 | PAXG_2024_1H_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6835 | 0.7271 | 0.0436 | 0.5222 | 0.2513 | 972 | 22 | 0 | 0 |
| PAXG_2024_1H_FOLLOW_5000_6000 | PAXG_2024_1H_SEQ | verteilt_offen | verteilt | 6 | 14 | 7 | 7 | 0.6948 | 0.7325 | 0.0377 | 0.5006 | 0.3293 | 984 | 10 | 0 | 0 |
| PAXG_2024_1H_FOLLOW_6000_7000 | PAXG_2024_1H_SEQ | verteilt_offen | verteilt | 7 | 18 | 8 | 6 | 0.6902 | 0.7314 | 0.0411 | 0.5615 | 0.2878 | 984 | 10 | 0 | 0 |
| PAXG_2025_1H_FOLLOW_4000_5000 | PAXG_2025_1H_SEQ | verteilt_offen | verteilt | 8 | 22 | 9 | 8 | 0.6946 | 0.7308 | 0.0362 | 0.2779 | 0.3227 | 989 | 5 | 0 | 0 |
| PAXG_2025_1H_FOLLOW_5000_6000 | PAXG_2025_1H_SEQ | verteilt_offen | verteilt | 7 | 20 | 11 | 9 | 0.6901 | 0.7315 | 0.0414 | 0.6229 | 0.2935 | 980 | 14 | 0 | 0 |
| PAXG_2025_1H_FOLLOW_6000_7000 | PAXG_2025_1H_SEQ | verteilt_offen | verteilt | 7 | 18 | 12 | 6 | 0.6856 | 0.7276 | 0.0419 | 0.5853 | 0.2707 | 969 | 25 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `1`
- `verteilt_offen`: `5`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0362 | 0.0436 | 0.0074 |
| Erfahrung | 0.2779 | 0.6229 | 0.3450 |
| Gewicht carry | 0.2930 | 0.3109 | 0.0179 |
| Gewicht alignment | 0.2205 | 0.2230 | 0.0025 |
| Gewicht strain_relief | 0.2634 | 0.2736 | 0.0102 |
| Gewicht sensory | 0.2026 | 0.2129 | 0.0103 |

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
