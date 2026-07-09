# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:17:51

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1767_kontrast_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1767_A_0_1000 | SYN1767_A | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7513 | 0.7635 | 0.0123 | 0.0328 | 0.7473 | 993 | 1 | 0 | 0 |
| SYN1767_A_1000_2000 | SYN1767_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7470 | 0.7470 | 0.0000 | 0.0000 | 0.7061 | 994 | 0 | 0 | 0 |
| SYN1767_A_2000_3000 | SYN1767_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7459 | 0.7459 | 0.0000 | 0.0000 | 0.6805 | 994 | 0 | 0 | 0 |
| SYN1767_A_3000_4000 | SYN1767_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7544 | 0.7544 | 0.0000 | 0.0000 | 0.8150 | 994 | 0 | 0 | 0 |
| SYN1767_A_4000_5000 | SYN1767_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7523 | 0.7523 | 0.0000 | 0.0000 | 0.7563 | 994 | 0 | 0 | 0 |
| SYN1767_B_0_1000 | SYN1767_B | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7518 | 0.7640 | 0.0121 | 0.0328 | 0.7555 | 993 | 1 | 0 | 0 |
| SYN1767_B_1000_2000 | SYN1767_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7458 | 0.7458 | 0.0000 | 0.0000 | 0.6848 | 994 | 0 | 0 | 0 |
| SYN1767_B_2000_3000 | SYN1767_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7459 | 0.7459 | 0.0000 | 0.0000 | 0.6837 | 994 | 0 | 0 | 0 |
| SYN1767_B_3000_4000 | SYN1767_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7500 | 0.7500 | 0.0000 | 0.0000 | 0.7394 | 994 | 0 | 0 | 0 |
| SYN1767_B_4000_5000 | SYN1767_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7548 | 0.7548 | 0.0000 | 0.0000 | 0.8000 | 994 | 0 | 0 | 0 |
| SYN1767_C_0_1000 | SYN1767_C | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7513 | 0.7635 | 0.0123 | 0.0328 | 0.7473 | 993 | 1 | 0 | 0 |
| SYN1767_C_1000_2000 | SYN1767_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7470 | 0.7470 | 0.0000 | 0.0000 | 0.7061 | 994 | 0 | 0 | 0 |
| SYN1767_C_2000_3000 | SYN1767_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7453 | 0.7453 | 0.0000 | 0.0000 | 0.6747 | 994 | 0 | 0 | 0 |
| SYN1767_C_3000_4000 | SYN1767_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7541 | 0.7541 | 0.0000 | 0.0000 | 0.8106 | 994 | 0 | 0 | 0 |
| SYN1767_C_4000_5000 | SYN1767_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7532 | 0.7532 | 0.0000 | 0.0000 | 0.7680 | 994 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `12`
- `mittlere_uebergangsphase`: `3`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0123 | 0.0123 |
| Erfahrung | 0.0000 | 0.0328 | 0.0328 |
| Gewicht carry | 0.3830 | 0.4200 | 0.0370 |
| Gewicht alignment | 0.2342 | 0.2400 | 0.0058 |
| Gewicht strain_relief | 0.2000 | 0.2203 | 0.0203 |
| Gewicht sensory | 0.1400 | 0.1625 | 0.0225 |

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
