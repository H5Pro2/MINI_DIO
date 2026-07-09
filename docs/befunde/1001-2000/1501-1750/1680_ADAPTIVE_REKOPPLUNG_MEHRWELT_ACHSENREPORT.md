# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-07 12:43:49

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `docs\befunde\1680_ADAPTIVE_REKOPPLUNG_MEHRWELT_ACHSENREPORT.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| adaptive_btc_2024_5m_0_to_1000 | btc_2024_5m | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6839 | 0.7284 | 0.0445 | 0.6133 | 0.1007 | 706 | 276 | 11 | 1 |
| adaptive_doge_2024_5m_0_to_1000 | doge_2024_5m | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6850 | 0.7291 | 0.0441 | 0.5833 | 0.1071 | 724 | 260 | 10 | 0 |
| adaptive_xrp_2024_5m_0_to_1000 | xrp_2024_5m | verteilt_offen | verteilt | 6 | 14 | 8 | 6 | 0.6767 | 0.7219 | 0.0452 | 0.6563 | 0.0690 | 677 | 298 | 19 | 0 |
| adaptive_sideways_0_to_2000 | sideways | verteilt_rekoppelnd | verteilt | 7 | 19 | 11 | 8 | 0.7028 | 0.7452 | 0.0424 | 0.6462 | 0.1748 | 1745 | 240 | 8 | 1 |
| adaptive_stress_2000_to_4000 | negative_stress | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.7005 | 0.7428 | 0.0423 | 0.6169 | 0.1600 | 1681 | 303 | 9 | 1 |
| adaptive_expansion_2000_to_4000 | positive_expansion | rand_kippnah | mittel | 3 | 3 | 0 | 3 | 0.6885 | 0.7314 | 0.0429 | 0.6188 | 0.1079 | 1433 | 532 | 28 | 1 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`
- `rand_kippnah`: `1`
- `verteilt_offen`: `2`
- `verteilt_rekoppelnd`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0423 | 0.0452 | 0.0029 |
| Erfahrung | 0.5833 | 0.6563 | 0.0730 |
| Gewicht carry | 0.2928 | 0.2950 | 0.0022 |
| Gewicht alignment | 0.2175 | 0.2181 | 0.0006 |
| Gewicht strain_relief | 0.2726 | 0.2741 | 0.0016 |
| Gewicht sensory | 0.2145 | 0.2152 | 0.0007 |

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
