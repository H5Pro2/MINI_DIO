# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 17:13:23

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_2025_shift_zeitmass_rekopplungszone.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_SHIFT_4000_5000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.6924 | 0.7354 | 0.0430 | 0.6605 | 0.3196 | 977 | 17 | 0 | 0 |
| BTC_2025_1H_SHIFT_5000_6000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6887 | 0.7267 | 0.0380 | 0.5709 | 0.3068 | 978 | 16 | 0 | 0 |
| BTC_2025_1H_SHIFT_6000_7000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.6857 | 0.7274 | 0.0417 | 0.5303 | 0.2731 | 972 | 22 | 0 | 0 |
| BTC_2025_30M_SHIFT_8000_9000 | BTC_30M_SHIFTZONE | verteilt_rekoppelnd | verteilt | 6 | 15 | 5 | 6 | 0.6954 | 0.7380 | 0.0425 | 0.4352 | 0.3467 | 984 | 10 | 0 | 0 |
| BTC_2025_30M_SHIFT_9000_10000 | BTC_30M_SHIFTZONE | verteilt_offen | verteilt | 5 | 10 | 6 | 2 | 0.6910 | 0.7289 | 0.0379 | 0.4932 | 0.3027 | 979 | 15 | 0 | 0 |
| BTC_2025_30M_SHIFT_10000_11000 | BTC_30M_SHIFTZONE | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6903 | 0.7275 | 0.0373 | 0.4445 | 0.3130 | 982 | 12 | 0 | 0 |
| BTC_2025_30M_SHIFT_11000_12000 | BTC_30M_SHIFTZONE | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6884 | 0.7307 | 0.0423 | 0.5880 | 0.3052 | 981 | 13 | 0 | 0 |
| BTC_2025_15M_SHIFT_16000_17000 | BTC_15M_SHIFTZONE | verteilt_offen | verteilt | 6 | 15 | 8 | 4 | 0.6892 | 0.7314 | 0.0423 | 0.4833 | 0.3028 | 984 | 10 | 0 | 0 |
| BTC_2025_15M_SHIFT_17000_18000 | BTC_15M_SHIFTZONE | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.6887 | 0.7305 | 0.0419 | 0.6732 | 0.2836 | 979 | 15 | 0 | 0 |
| BTC_2025_15M_SHIFT_18000_19000 | BTC_15M_SHIFTZONE | verteilt_offen | verteilt | 7 | 20 | 11 | 7 | 0.6875 | 0.7301 | 0.0426 | 0.6244 | 0.2743 | 978 | 16 | 0 | 0 |
| BTC_2025_15M_SHIFT_19000_20000 | BTC_15M_SHIFTZONE | verteilt_offen | verteilt | 6 | 14 | 7 | 4 | 0.6916 | 0.7326 | 0.0410 | 0.5078 | 0.2932 | 984 | 10 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `4`
- `mittlere_uebergangsphase`: `1`
- `verteilt_offen`: `5`
- `verteilt_rekoppelnd`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0373 | 0.0430 | 0.0057 |
| Erfahrung | 0.4352 | 0.6732 | 0.2380 |
| Gewicht carry | 0.2929 | 0.3079 | 0.0150 |
| Gewicht alignment | 0.2199 | 0.2224 | 0.0025 |
| Gewicht strain_relief | 0.2655 | 0.2741 | 0.0086 |
| Gewicht sensory | 0.2044 | 0.2131 | 0.0087 |

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
