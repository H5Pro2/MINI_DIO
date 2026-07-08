# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:02:59

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1764_zwischenwelt_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1764_A_0_1000 | SYN1764_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7555 | 0.7555 | 0.0000 | 0.0000 | 0.8052 | 994 | 0 | 0 | 0 |
| SYN1764_A_1000_2000 | SYN1764_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7534 | 0.7534 | 0.0000 | 0.0000 | 0.7822 | 994 | 0 | 0 | 0 |
| SYN1764_A_2000_3000 | SYN1764_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7519 | 0.7519 | 0.0000 | 0.0000 | 0.7518 | 994 | 0 | 0 | 0 |
| SYN1764_A_3000_4000 | SYN1764_A | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7545 | 0.7545 | 0.0000 | 0.0000 | 0.7865 | 994 | 0 | 0 | 0 |
| SYN1764_B_0_1000 | SYN1764_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7555 | 0.7555 | 0.0000 | 0.0000 | 0.8057 | 994 | 0 | 0 | 0 |
| SYN1764_B_1000_2000 | SYN1764_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7536 | 0.7536 | 0.0000 | 0.0000 | 0.7915 | 994 | 0 | 0 | 0 |
| SYN1764_B_2000_3000 | SYN1764_B | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7468 | 0.7468 | 0.0000 | 0.0000 | 0.6765 | 994 | 0 | 0 | 0 |
| SYN1764_B_3000_4000 | SYN1764_B | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7508 | 0.7788 | 0.0281 | 0.0797 | 0.7438 | 993 | 1 | 0 | 0 |
| SYN1764_C_0_1000 | SYN1764_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7555 | 0.7555 | 0.0000 | 0.0000 | 0.8066 | 994 | 0 | 0 | 0 |
| SYN1764_C_1000_2000 | SYN1764_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7529 | 0.7529 | 0.0000 | 0.0000 | 0.7737 | 994 | 0 | 0 | 0 |
| SYN1764_C_2000_3000 | SYN1764_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7236 | 0.7236 | 0.0000 | 0.0000 | 0.4664 | 994 | 0 | 0 | 0 |
| SYN1764_C_3000_4000 | SYN1764_C | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7538 | 0.7538 | 0.0000 | 0.0000 | 0.8083 | 994 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `11`
- `mittlere_uebergangsphase`: `1`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0281 | 0.0281 |
| Erfahrung | 0.0000 | 0.0797 | 0.0797 |
| Gewicht carry | 0.3263 | 0.4200 | 0.0937 |
| Gewicht alignment | 0.2241 | 0.2400 | 0.0159 |
| Gewicht strain_relief | 0.2000 | 0.2543 | 0.0543 |
| Gewicht sensory | 0.1400 | 0.1953 | 0.0553 |

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
