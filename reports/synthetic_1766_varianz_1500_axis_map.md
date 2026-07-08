# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:13:07

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1766_varianz_1500_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1766_A_1500_3000 | SYN1766_A_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7507 | 0.7507 | 0.0000 | 0.0000 | 0.7494 | 1494 | 0 | 0 | 0 |
| SYN1766_A_2500_4000 | SYN1766_A_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7495 | 0.7495 | 0.0000 | 0.0000 | 0.7296 | 1494 | 0 | 0 | 0 |
| SYN1766_A_3500_5000 | SYN1766_A_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7514 | 0.7514 | 0.0000 | 0.0000 | 0.7604 | 1494 | 0 | 0 | 0 |
| SYN1766_B_1500_3000 | SYN1766_B_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7505 | 0.7505 | 0.0000 | 0.0000 | 0.7489 | 1494 | 0 | 0 | 0 |
| SYN1766_B_2500_4000 | SYN1766_B_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7508 | 0.7508 | 0.0000 | 0.0000 | 0.7572 | 1494 | 0 | 0 | 0 |
| SYN1766_B_3500_5000 | SYN1766_B_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7489 | 0.7489 | 0.0000 | 0.0000 | 0.7261 | 1494 | 0 | 0 | 0 |
| SYN1766_C_1500_3000 | SYN1766_C_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7523 | 0.7523 | 0.0000 | 0.0000 | 0.7811 | 1494 | 0 | 0 | 0 |
| SYN1766_C_2500_4000 | SYN1766_C_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7468 | 0.7468 | 0.0000 | 0.0000 | 0.7020 | 1494 | 0 | 0 | 0 |
| SYN1766_C_3500_5000 | SYN1766_C_1500 | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7496 | 0.7496 | 0.0000 | 0.0000 | 0.7330 | 1494 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `9`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_aber_gewichte_noch_gleichfoermig`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0000 | 0.0000 |
| Erfahrung | 0.0000 | 0.0000 | 0.0000 |
| Gewicht carry | 0.4200 | 0.4200 | 0.0000 |
| Gewicht alignment | 0.2400 | 0.2400 | 0.0000 |
| Gewicht strain_relief | 0.2000 | 0.2000 | 0.0000 |
| Gewicht sensory | 0.1400 | 0.1400 | 0.0000 |

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
