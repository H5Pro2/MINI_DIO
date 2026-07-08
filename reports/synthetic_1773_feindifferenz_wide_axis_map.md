# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 16:14:27

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1773_feindifferenz_wide_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1773_A_0_2000 | SYN1773_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7577 | 0.7577 | 0.0000 | 0.0000 | 0.8508 | 1994 | 0 | 0 | 0 |
| SYN1773_A_3000_5000 | SYN1773_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7562 | 0.7562 | 0.0000 | 0.0000 | 0.8259 | 1994 | 0 | 0 | 0 |
| SYN1773_A_6000_8000 | SYN1773_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7579 | 0.7579 | 0.0000 | 0.0000 | 0.8464 | 1994 | 0 | 0 | 0 |
| SYN1773_B_0_2000 | SYN1773_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7575 | 0.7575 | 0.0000 | 0.0000 | 0.8475 | 1994 | 0 | 0 | 0 |
| SYN1773_B_3000_5000 | SYN1773_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7551 | 0.7551 | 0.0000 | 0.0000 | 0.8146 | 1994 | 0 | 0 | 0 |
| SYN1773_B_6000_8000 | SYN1773_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7561 | 0.7561 | 0.0000 | 0.0000 | 0.8323 | 1994 | 0 | 0 | 0 |
| SYN1773_C_0_2000 | SYN1773_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7578 | 0.7578 | 0.0000 | 0.0000 | 0.8508 | 1994 | 0 | 0 | 0 |
| SYN1773_C_3000_5000 | SYN1773_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7555 | 0.7555 | 0.0000 | 0.0000 | 0.8173 | 1994 | 0 | 0 | 0 |
| SYN1773_C_6000_8000 | SYN1773_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7569 | 0.7569 | 0.0000 | 0.0000 | 0.8390 | 1994 | 0 | 0 | 0 |

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
