# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 17:08:52

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_2025_zeitmass_rekopplungszone.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_NEIGHBOR_1000_2000 | BTC_1H_REKOPPLUNGSZONE | verteilt_offen | verteilt | 6 | 15 | 9 | 6 | 0.6935 | 0.7359 | 0.0424 | 0.5672 | 0.3275 | 977 | 17 | 0 | 0 |
| BTC_2025_1H_CORE_2000_3000 | BTC_1H_REKOPPLUNGSZONE | verteilt_rekoppelnd | verteilt | 5 | 10 | 4 | 6 | 0.6956 | 0.7370 | 0.0414 | 0.4432 | 0.3512 | 984 | 10 | 0 | 0 |
| BTC_2025_1H_NEIGHBOR_3000_4000 | BTC_1H_REKOPPLUNGSZONE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6938 | 0.7307 | 0.0369 | 0.4693 | 0.3459 | 984 | 10 | 0 | 0 |
| BTC_2025_30M_ZONE_4000_5000 | BTC_30M_SAME_PHASE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6849 | 0.7256 | 0.0408 | 0.5375 | 0.2725 | 974 | 20 | 0 | 0 |
| BTC_2025_30M_ZONE_5000_6000 | BTC_30M_SAME_PHASE | verteilt_offen | verteilt | 6 | 15 | 9 | 6 | 0.6940 | 0.7337 | 0.0397 | 0.5794 | 0.3267 | 978 | 16 | 0 | 0 |
| BTC_2025_30M_ZONE_6000_7000 | BTC_30M_SAME_PHASE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6911 | 0.7270 | 0.0359 | 0.4512 | 0.3116 | 983 | 11 | 0 | 0 |
| BTC_2025_30M_ZONE_7000_8000 | BTC_30M_SAME_PHASE | kompakt_nachhallend | kompakt | 2 | 1 | 1 | 0 | 0.6920 | 0.7349 | 0.0430 | 0.6011 | 0.3183 | 982 | 12 | 0 | 0 |
| BTC_2025_15M_ZONE_8000_9000 | BTC_15M_SAME_PHASE | kompakt_nachhallend | kompakt | 2 | 1 | 1 | 0 | 0.6843 | 0.7269 | 0.0427 | 0.5780 | 0.2603 | 971 | 23 | 0 | 0 |
| BTC_2025_15M_ZONE_9000_10000 | BTC_15M_SAME_PHASE | verteilt_rekoppelnd | verteilt | 5 | 10 | 4 | 3 | 0.6952 | 0.7272 | 0.0320 | 0.4249 | 0.3388 | 984 | 10 | 0 | 0 |
| BTC_2025_15M_ZONE_10000_11000 | BTC_15M_SAME_PHASE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6839 | 0.7256 | 0.0417 | 0.6481 | 0.2611 | 969 | 25 | 0 | 0 |
| BTC_2025_15M_ZONE_11000_12000 | BTC_15M_SAME_PHASE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6891 | 0.7323 | 0.0432 | 0.6487 | 0.3017 | 978 | 16 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `3`
- `mittlere_uebergangsphase`: `4`
- `verteilt_offen`: `2`
- `verteilt_rekoppelnd`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0320 | 0.0432 | 0.0111 |
| Erfahrung | 0.4249 | 0.6487 | 0.2238 |
| Gewicht carry | 0.2928 | 0.3223 | 0.0295 |
| Gewicht alignment | 0.2200 | 0.2245 | 0.0045 |
| Gewicht strain_relief | 0.2569 | 0.2747 | 0.0178 |
| Gewicht sensory | 0.1963 | 0.2126 | 0.0162 |

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

## Wie es weitergeht

Als naechstes sollte dieser Report auf neue Assets oder neue synthetische Kontrollwelten angewendet werden. Ziel ist zu pruefen, ob die Achsenklassen stabil bleiben oder neue Feldmilieus entstehen.
