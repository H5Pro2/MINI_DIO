# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 17:03:56

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_doge_xrp_2025_1h_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_0_1000 | BTC_2025_1H_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 1 | 0.6954 | 0.7319 | 0.0366 | 0.5410 | 0.3368 | 981 | 13 | 0 | 0 |
| BTC_2025_1H_1000_2000 | BTC_2025_1H_SEQ | verteilt_offen | verteilt | 6 | 15 | 9 | 6 | 0.6935 | 0.7359 | 0.0424 | 0.5672 | 0.3275 | 977 | 17 | 0 | 0 |
| BTC_2025_1H_2000_3000 | BTC_2025_1H_SEQ | verteilt_rekoppelnd | verteilt | 5 | 10 | 4 | 6 | 0.6956 | 0.7370 | 0.0414 | 0.4432 | 0.3512 | 984 | 10 | 0 | 0 |
| BTC_2025_1H_3000_4000 | BTC_2025_1H_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6938 | 0.7307 | 0.0369 | 0.4693 | 0.3459 | 984 | 10 | 0 | 0 |
| DOGE_2025_1H_0_1000 | DOGE_2025_1H_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6957 | 0.7375 | 0.0418 | 0.5851 | 0.3441 | 977 | 17 | 0 | 0 |
| DOGE_2025_1H_1000_2000 | DOGE_2025_1H_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6915 | 0.7336 | 0.0421 | 0.6273 | 0.3202 | 977 | 17 | 0 | 0 |
| DOGE_2025_1H_2000_3000 | DOGE_2025_1H_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6941 | 0.7335 | 0.0395 | 0.5104 | 0.3455 | 981 | 13 | 0 | 0 |
| DOGE_2025_1H_3000_4000 | DOGE_2025_1H_SEQ | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6917 | 0.7307 | 0.0390 | 0.4506 | 0.3291 | 983 | 11 | 0 | 0 |
| XRP_2025_1H_0_1000 | XRP_2025_1H_SEQ | verteilt_offen | verteilt | 8 | 22 | 9 | 13 | 0.6902 | 0.7289 | 0.0387 | 0.5475 | 0.3176 | 975 | 19 | 0 | 0 |
| XRP_2025_1H_1000_2000 | XRP_2025_1H_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6938 | 0.7334 | 0.0396 | 0.6284 | 0.3492 | 978 | 16 | 0 | 0 |
| XRP_2025_1H_2000_3000 | XRP_2025_1H_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6946 | 0.7276 | 0.0330 | 0.5528 | 0.3483 | 978 | 16 | 0 | 0 |
| XRP_2025_1H_3000_4000 | XRP_2025_1H_SEQ | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.6922 | 0.7291 | 0.0370 | 0.6079 | 0.3267 | 983 | 11 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `2`
- `mittlere_uebergangsphase`: `5`
- `verteilt_offen`: `4`
- `verteilt_rekoppelnd`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0330 | 0.0424 | 0.0094 |
| Erfahrung | 0.4432 | 0.6284 | 0.1852 |
| Gewicht carry | 0.2943 | 0.3192 | 0.0248 |
| Gewicht alignment | 0.2201 | 0.2240 | 0.0039 |
| Gewicht strain_relief | 0.2585 | 0.2731 | 0.0146 |
| Gewicht sensory | 0.1983 | 0.2126 | 0.0143 |

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
