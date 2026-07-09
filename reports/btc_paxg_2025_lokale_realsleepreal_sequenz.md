# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:27:34

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\btc_paxg_2025_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_FOLLOW_0_1000 | BTC_2025_LOCAL_SEQ | verteilt_offen | verteilt | 7 | 20 | 11 | 9 | 0.6922 | 0.7326 | 0.0404 | 0.4775 | 0.3269 | 974 | 20 | 0 | 0 |
| PAXG_2025_FOLLOW_0_1000 | PAXG_2025_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.6943 | 0.7352 | 0.0409 | 0.5706 | 0.3160 | 983 | 11 | 0 | 0 |
| BTC_2025_FOLLOW_1000_2000 | BTC_2025_LOCAL_SEQ | verteilt_offen | verteilt | 5 | 10 | 6 | 4 | 0.6910 | 0.7342 | 0.0432 | 0.6306 | 0.3115 | 972 | 22 | 0 | 0 |
| PAXG_2025_FOLLOW_1000_2000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | verteilt | 7 | 18 | 8 | 6 | 0.6997 | 0.7429 | 0.0431 | 0.4159 | 0.3426 | 988 | 6 | 0 | 0 |
| BTC_2025_FOLLOW_2000_3000 | BTC_2025_LOCAL_SEQ | verteilt_offen | verteilt | 6 | 15 | 8 | 4 | 0.6908 | 0.7207 | 0.0299 | 0.3545 | 0.2993 | 987 | 7 | 0 | 0 |
| PAXG_2025_FOLLOW_2000_3000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | verteilt | 5 | 10 | 4 | 3 | 0.7080 | 0.7252 | 0.0172 | 0.0965 | 0.3996 | 990 | 4 | 0 | 0 |
| BTC_2025_FOLLOW_3000_4000 | BTC_2025_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 4 | 6 | 4 | 1 | 0.6882 | 0.7315 | 0.0433 | 0.6218 | 0.2831 | 984 | 10 | 0 | 0 |
| PAXG_2025_FOLLOW_3000_4000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | verteilt | 12 | 32 | 18 | 9 | 0.7048 | 0.7405 | 0.0357 | 0.3731 | 0.3837 | 987 | 7 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `2`
- `verteilt_offen`: `3`
- `verteilt_rekoppelnd`: `3`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0172 | 0.0433 | 0.0261 |
| Erfahrung | 0.0965 | 0.6306 | 0.5340 |
| Gewicht carry | 0.2926 | 0.3669 | 0.0743 |
| Gewicht alignment | 0.2200 | 0.2316 | 0.0116 |
| Gewicht strain_relief | 0.2306 | 0.2743 | 0.0437 |
| Gewicht sensory | 0.1709 | 0.2139 | 0.0430 |

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
