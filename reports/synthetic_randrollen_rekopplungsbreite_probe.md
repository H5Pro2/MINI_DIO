# Automatisierter Mehrwelt-Achsenreport

Stand: 2026-07-08 14:56:30

## Zweck

Dieser Report erzeugt aus neuen Real-Sleep-Real-Laeufen eine gemeinsame Tabelle fuer:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

CSV: `reports\synthetic_randrollen_rekopplungsbreite_probe.csv`

## Achsentabelle

| Label | Welt | Achsenklasse | Breite | Rollen | Kombis | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall | Stabil | Unruhig | Kippend | Gespannt |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN_RANDROLLEN_BRIDGE_TO_SHIFT | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7269 | 0.7269 | 0.0000 | 0.0000 | 0.5508 | 1194 | 0 | 0 | 0 |
| SYN_RANDROLLEN_SHIFT_TO_MOSAIC | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7239 | 0.7239 | 0.0000 | 0.0000 | 0.5372 | 1194 | 0 | 0 | 0 |
| SYN_RANDROLLEN_MOSAIC_TO_LONG | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | kompakt | 1 | 0 | 0 | 0 | 0.7203 | 0.7203 | 0.0000 | 0.0000 | 0.4966 | 1194 | 0 | 0 | 0 |
| SYN_RANDROLLEN_INTERWOVEN_TO_LONG | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7273 | 0.7322 | 0.0048 | 0.0080 | 0.6239 | 2394 | 0 | 0 | 0 |
| SYN_NULL_SHUFFLE_TO_RANDOM | SYN_NULL_KONTROLLE | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7156 | 0.7205 | 0.0049 | 0.0080 | 0.6004 | 2394 | 0 | 0 | 0 |
| SYN_NULL_RANDOM_TO_SHUFFLE | SYN_NULL_KONTROLLE | kompakt_nachhallend | kompakt | 2 | 1 | 0 | 1 | 0.7211 | 0.7262 | 0.0051 | 0.0080 | 0.5804 | 2394 | 0 | 0 | 0 |

## Klassenverteilung

- `kompakt_nachhallend`: `6`

## Adaptive Rekopplung

Lesung: `adaptive_rekopplung_aktiv_und_gewichte_differenzieren`

| Messung | Minimum | Maximum | Spanne |
|---|---:|---:|---:|
| Delta adaptiv-statisch | 0.0000 | 0.0051 | 0.0051 |
| Erfahrung | 0.0000 | 0.0080 | 0.0080 |
| Gewicht carry | 0.4026 | 0.4200 | 0.0174 |
| Gewicht alignment | 0.2367 | 0.2400 | 0.0033 |
| Gewicht strain_relief | 0.2000 | 0.2100 | 0.0100 |
| Gewicht sensory | 0.1400 | 0.1508 | 0.0108 |

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
