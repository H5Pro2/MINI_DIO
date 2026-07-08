# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 16:53:24

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_doge_xrp_2025_late_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_FOLLOW_5000_6000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6866 | 0.7218 | 0.0352 | 0.4916 | 0.2797 | 967 | 27 | 0 | 0 |
| BTC_2025_FOLLOW_6000_7000 | BTC_2025_LOCAL_SEQ_LATE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6881 | 0.7315 | 0.0434 | 0.5917 | 0.2900 | 968 | 26 | 0 | 0 |
| BTC_2025_FOLLOW_7000_8000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 7 | 18 | 12 | 6 | 0.6811 | 0.7114 | 0.0304 | 0.4894 | 0.2186 | 973 | 21 | 0 | 0 |
| BTC_2025_FOLLOW_8000_9000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 5 | 10 | 6 | 2 | 0.6895 | 0.7328 | 0.0433 | 0.5412 | 0.2892 | 986 | 8 | 0 | 0 |
| DOGE_2025_FOLLOW_5000_6000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 6 | 15 | 9 | 6 | 0.6889 | 0.7188 | 0.0299 | 0.4347 | 0.2997 | 975 | 19 | 0 | 0 |
| DOGE_2025_FOLLOW_6000_7000 | DOGE_2025_LOCAL_SEQ_LATE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.6885 | 0.7308 | 0.0423 | 0.5576 | 0.3100 | 976 | 18 | 0 | 0 |
| DOGE_2025_FOLLOW_7000_8000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 7 | 21 | 12 | 9 | 0.6797 | 0.7194 | 0.0397 | 0.4809 | 0.2245 | 971 | 23 | 0 | 0 |
| DOGE_2025_FOLLOW_8000_9000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 6 | 15 | 8 | 4 | 0.6900 | 0.7323 | 0.0423 | 0.5642 | 0.3069 | 983 | 11 | 0 | 0 |
| XRP_2025_FOLLOW_5000_6000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6879 | 0.7225 | 0.0346 | 0.5107 | 0.3035 | 977 | 17 | 0 | 0 |
| XRP_2025_FOLLOW_6000_7000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 8 | 25 | 15 | 10 | 0.6898 | 0.7239 | 0.0341 | 0.5345 | 0.3161 | 975 | 19 | 0 | 0 |
| XRP_2025_FOLLOW_7000_8000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 7 | 18 | 10 | 8 | 0.6774 | 0.7124 | 0.0350 | 0.5125 | 0.1966 | 959 | 35 | 0 | 0 |
| XRP_2025_FOLLOW_8000_9000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | verteilt | 12 | 32 | 18 | 9 | 0.6935 | 0.7343 | 0.0407 | 0.4277 | 0.3469 | 987 | 7 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`
- `verteilt_offen`: `10`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0299 | 0.0434 | 0.0135 |
| Erfahrung | 0.4277 | 0.5917 | 0.1640 |
| Gewicht carry | 0.2928 | 0.3307 | 0.0380 |
| Gewicht alignment | 0.2199 | 0.2262 | 0.0063 |
| Gewicht strain_relief | 0.2529 | 0.2745 | 0.0215 |
| Gewicht sensory | 0.1899 | 0.2128 | 0.0229 |

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
