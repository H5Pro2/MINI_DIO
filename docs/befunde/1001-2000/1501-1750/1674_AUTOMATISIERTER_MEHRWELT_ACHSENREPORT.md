# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 10:56:39

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1674_AUTOMATISIERTER_MEHRWELT_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| multi_axis_sideways_0_to_2000 | sideways | verteilt_rekoppelnd | verteilt | 7 | 19 | 11 | 8 | 0.7028 | 0.1748 | 1745 | 240 | 8 | 1 |
| multi_axis_sideways_4000_to_6000 | sideways | kompakt_gebunden | kompakt | 2 | 1 | 0 | 1 | 0.6956 | 0.1383 | 1604 | 376 | 14 | 0 |
| multi_axis_stress_2000_to_4000 | negative_stress | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.7005 | 0.1600 | 1681 | 303 | 9 | 1 |
| multi_axis_stress_4000_to_6000 | negative_stress | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7024 | 0.1820 | 1703 | 276 | 15 | 0 |
| multi_axis_expansion_4000_to_6000 | positive_expansion | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6894 | 0.1005 | 1393 | 580 | 20 | 1 |
| multi_axis_expansion_2000_to_4000 | positive_expansion | rand_kippnah | mittel | 3 | 3 | 0 | 3 | 0.6885 | 0.1079 | 1433 | 532 | 28 | 1 |

## Klassenverteilung

- `kompakt_gebunden`: `1`
- `kompakt_nachhallend`: `1`
- `mittlere_uebergangsphase`: `1`
- `rand_kippnah`: `1`
- `verteilt_offen`: `1`
- `verteilt_rekoppelnd`: `1`

## Befund

Der Report macht sichtbar, ob eine Weltphase kompakt gebunden, verteilt offen, verteilt rekoppelnd, nachhallend kompakt oder rand-/kippnah wirkt.

Wichtig ist die gemeinsame Lesung:

```text
Rollenbreite allein reicht nicht.
Nachhall allein reicht nicht.
Topologie allein reicht nicht.
Erst die gemeinsame Achsenlage beschreibt das Feldmilieu.
```

## Grenze

Die Klassifikation ist eine passive Diagnose. Sie beschreibt Feldmilieu und Anschlussfaehigkeit, aber keine Richtung, keine Handlung und keine Strategie.
