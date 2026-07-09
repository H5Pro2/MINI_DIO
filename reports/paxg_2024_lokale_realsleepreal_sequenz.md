# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:43:09

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\paxg_2024_lokale_realsleepreal_sequenz.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_FOLLOW_0_1000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7024 | 0.7095 | 0.0071 | 0.0188 | 0.3336 | 993 | 1 | 0 | 0 |
| PAXG_2024_FOLLOW_1000_2000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.6969 | 0.7005 | 0.0037 | 0.0098 | 0.2992 | 993 | 1 | 0 | 0 |
| PAXG_2024_FOLLOW_2000_3000 | PAXG_2024_LOCAL_SEQ | verteilt_rekoppelnd | verteilt | 5 | 10 | 6 | 2 | 0.7070 | 0.7422 | 0.0352 | 0.1203 | 0.3770 | 992 | 2 | 0 | 0 |
| PAXG_2024_FOLLOW_3000_4000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7087 | 0.7326 | 0.0238 | 0.0613 | 0.3641 | 993 | 1 | 0 | 0 |

## Klassenverteilung

- `mittlere_uebergangsphase`: `3`
- `verteilt_rekoppelnd`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0037 | 0.0352 | 0.0315 |
| Erfahrung | 0.0098 | 0.1203 | 0.1105 |
| Gewicht carry | 0.3127 | 0.4085 | 0.0957 |
| Gewicht alignment | 0.2235 | 0.2382 | 0.0147 |
| Gewicht strain_relief | 0.2067 | 0.2614 | 0.0547 |
| Gewicht sensory | 0.1466 | 0.2024 | 0.0557 |

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
