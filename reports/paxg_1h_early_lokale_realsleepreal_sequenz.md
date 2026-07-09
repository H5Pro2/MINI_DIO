# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 16:36:32

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\paxg_1h_early_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_1H_EARLY_0_1000 | PAXG_2024_1H_EARLY_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6900 | 0.7309 | 0.0409 | 0.4508 | 0.2901 | 984 | 10 | 0 | 0 |
| PAXG_2024_1H_EARLY_1000_2000 | PAXG_2024_1H_EARLY_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6884 | 0.7299 | 0.0415 | 0.4955 | 0.2702 | 979 | 15 | 0 | 0 |
| PAXG_2024_1H_EARLY_2000_3000 | PAXG_2024_1H_EARLY_SEQ | verteilt_offen | verteilt | 6 | 15 | 8 | 4 | 0.6930 | 0.7270 | 0.0340 | 0.4778 | 0.3113 | 979 | 15 | 0 | 0 |
| PAXG_2025_1H_EARLY_0_1000 | PAXG_2025_1H_EARLY_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6829 | 0.7206 | 0.0377 | 0.3925 | 0.2410 | 982 | 12 | 0 | 0 |
| PAXG_2025_1H_EARLY_1000_2000 | PAXG_2025_1H_EARLY_SEQ | verteilt_offen | verteilt | 8 | 23 | 14 | 6 | 0.6907 | 0.7310 | 0.0403 | 0.3379 | 0.2986 | 987 | 7 | 0 | 0 |
| PAXG_2025_1H_EARLY_2000_3000 | PAXG_2025_1H_EARLY_SEQ | verteilt_offen | verteilt | 8 | 22 | 11 | 8 | 0.6901 | 0.7327 | 0.0426 | 0.3215 | 0.2975 | 987 | 7 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `1`
- `mittlere_uebergangsphase`: `2`
- `verteilt_offen`: `3`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0340 | 0.0426 | 0.0086 |
| Erfahrung | 0.3215 | 0.4955 | 0.1740 |
| Gewicht carry | 0.2949 | 0.3178 | 0.0228 |
| Gewicht alignment | 0.2205 | 0.2243 | 0.0038 |
| Gewicht strain_relief | 0.2596 | 0.2730 | 0.0133 |
| Gewicht sensory | 0.1983 | 0.2116 | 0.0132 |

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
