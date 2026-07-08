# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 15:58:16

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_1770_koaktiv_wide_axis_map.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1770_A_0_2000 | SYN1770_A_WIDE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7516 | 0.7623 | 0.0107 | 0.0283 | 0.7779 | 1993 | 1 | 0 | 0 |
| SYN1770_A_3000_5000 | SYN1770_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7457 | 0.7457 | 0.0000 | 0.0000 | 0.7331 | 1994 | 0 | 0 | 0 |
| SYN1770_A_6000_8000 | SYN1770_A_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7497 | 0.7497 | 0.0000 | 0.0000 | 0.7567 | 1994 | 0 | 0 | 0 |
| SYN1770_B_0_2000 | SYN1770_B_WIDE | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 0 | 0.7514 | 0.7621 | 0.0107 | 0.0288 | 0.7759 | 1993 | 1 | 0 | 0 |
| SYN1770_B_3000_5000 | SYN1770_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7452 | 0.7452 | 0.0000 | 0.0000 | 0.7329 | 1994 | 0 | 0 | 0 |
| SYN1770_B_6000_8000 | SYN1770_B_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7483 | 0.7483 | 0.0000 | 0.0000 | 0.7376 | 1994 | 0 | 0 | 0 |
| SYN1770_C_0_2000 | SYN1770_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7508 | 0.7508 | 0.0000 | 0.0000 | 0.7706 | 1994 | 0 | 0 | 0 |
| SYN1770_C_3000_5000 | SYN1770_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7447 | 0.7447 | 0.0000 | 0.0000 | 0.7266 | 1994 | 0 | 0 | 0 |
| SYN1770_C_6000_8000 | SYN1770_C_WIDE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7488 | 0.7488 | 0.0000 | 0.0000 | 0.7394 | 1994 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `7`
- `mittlere_uebergangsphase`: `2`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0107 | 0.0107 |
| Erfahrung | 0.0000 | 0.0288 | 0.0288 |
| Gewicht carry | 0.3861 | 0.4200 | 0.0339 |
| Gewicht alignment | 0.2345 | 0.2400 | 0.0055 |
| Gewicht strain_relief | 0.2000 | 0.2187 | 0.0187 |
| Gewicht sensory | 0.1400 | 0.1606 | 0.0206 |

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
