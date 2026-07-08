# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:40:26

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_doge_xrp_2024_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_FOLLOW_0_1000 | BTC_2024_LOCAL_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6931 | 0.7323 | 0.0392 | 0.3580 | 0.3185 | 987 | 7 | 0 | 0 |
| DOGE_2024_FOLLOW_0_1000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | verteilt | 8 | 22 | 4 | 12 | 0.6922 | 0.7317 | 0.0396 | 0.2848 | 0.3010 | 986 | 8 | 0 | 0 |
| XRP_2024_FOLLOW_0_1000 | XRP_2024_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.6903 | 0.7312 | 0.0409 | 0.6297 | 0.2956 | 982 | 12 | 0 | 0 |
| BTC_2024_FOLLOW_1000_2000 | BTC_2024_LOCAL_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 2 | 0.6883 | 0.7293 | 0.0410 | 0.3991 | 0.2815 | 988 | 6 | 0 | 0 |
| DOGE_2024_FOLLOW_1000_2000 | DOGE_2024_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6878 | 0.7313 | 0.0435 | 0.6813 | 0.2911 | 980 | 14 | 0 | 0 |
| XRP_2024_FOLLOW_1000_2000 | XRP_2024_LOCAL_SEQ | verteilt_offen | verteilt | 6 | 14 | 8 | 4 | 0.6919 | 0.7324 | 0.0405 | 0.5581 | 0.3035 | 978 | 16 | 0 | 0 |
| BTC_2024_FOLLOW_2000_3000 | BTC_2024_LOCAL_SEQ | verteilt_offen | verteilt | 6 | 14 | 8 | 6 | 0.6902 | 0.7271 | 0.0369 | 0.6061 | 0.3071 | 979 | 15 | 0 | 0 |
| DOGE_2024_FOLLOW_2000_3000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | verteilt | 10 | 29 | 14 | 12 | 0.6880 | 0.7292 | 0.0412 | 0.5497 | 0.2801 | 984 | 10 | 0 | 0 |
| XRP_2024_FOLLOW_2000_3000 | XRP_2024_LOCAL_SEQ | verteilt_offen | verteilt | 6 | 14 | 8 | 6 | 0.6888 | 0.7299 | 0.0411 | 0.7234 | 0.2830 | 972 | 22 | 0 | 0 |
| BTC_2024_FOLLOW_3000_4000 | BTC_2024_LOCAL_SEQ | verteilt_offen | verteilt | 7 | 17 | 10 | 5 | 0.6899 | 0.7308 | 0.0409 | 0.6236 | 0.3091 | 979 | 15 | 0 | 0 |
| DOGE_2024_FOLLOW_3000_4000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | verteilt | 6 | 14 | 8 | 6 | 0.6903 | 0.7315 | 0.0411 | 0.5425 | 0.3024 | 978 | 16 | 0 | 0 |
| XRP_2024_FOLLOW_3000_4000 | XRP_2024_LOCAL_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6924 | 0.7287 | 0.0362 | 0.5198 | 0.3153 | 975 | 19 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`
- `verteilt_offen`: `10`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0362 | 0.0435 | 0.0073 |
| Erfahrung | 0.2848 | 0.7234 | 0.4386 |
| Gewicht carry | 0.2921 | 0.3109 | 0.0189 |
| Gewicht alignment | 0.2201 | 0.2226 | 0.0026 |
| Gewicht strain_relief | 0.2634 | 0.2746 | 0.0112 |
| Gewicht sensory | 0.2030 | 0.2133 | 0.0103 |

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
