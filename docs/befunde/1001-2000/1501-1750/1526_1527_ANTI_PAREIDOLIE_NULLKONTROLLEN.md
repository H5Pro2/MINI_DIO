# 1526-1527 - Anti-Pareidolie Nullkontrollen

## Zweck

Diese Pruefung ist methodisch wichtig.

Die Grundfrage lautet:

```text
Lernt oder ordnet MINI_DIO tatsaechlich wiederkehrende Feldlagen,
oder interpretiert der Mensch nur Muster in Rauschen?
```

Stichwort: Pareidolie.

Darum wurden zu 1525 zwei Nullkontrollen gebaut. Beide behalten Teile der statistischen Oberflaeche, zerstoeren aber gezielt die Weltordnung.

## Kontrollaufbau

Vergleichswelt:

```text
1525: data/synthetic_1525_melody_randrollen_interwoven_mosaic_2400_5m.csv
```

Nullkontrollen:

```text
1526: data/synthetic_1526_null_shuffle_order_2400_5m.csv
      gleiche Candle-Formen, aber zerstoerte Reihenfolge

1527: data/synthetic_1527_null_random_sign_2400_5m.csv
      gleiche Groessenordnung, aber randomisierte Richtungszeichen
```

Alle Pruefungen wurden mit frischer Memory, zwei Wiederholungen und `world_relative` ausgefuehrt.

## Ergebnis

| Welt | Kerzen | Unique Symbols | Stable Ratio | Carried Unrest | Avg Afterimage | Kernrollen |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1525 strukturierte Mosaikvarianz | 2400 | 97 | 0.8759 | 0.1236 | 0.4053 | `dio_0l7p`, `dio_1wdi`, `dio_14wj`, `dio_1fll` |
| 1526 Null Shuffle | 2400 | 224 | 0.8045 | 0.1955 | 0.1512 | `dio_104t`, `dio_155c`, schwacher `dio_0l7p` |
| 1527 Null Random Sign | 2400 | 221 | 0.8517 | 0.1483 | 0.2452 | `dio_0l7p`, `dio_14wj`, `dio_104t` |

## Rollenvergleich

| Rolle | 1525 strukturiert | 1526 Shuffle | 1527 Random Sign |
| --- | ---: | ---: | ---: |
| `dio_0l7p` | 256 | 70 | 205 |
| `dio_1wdi` | 195 | 0 | 0 |
| `dio_14wj` | 134 | 0 | 141 |
| `dio_1fll` | 77 | 0 | 0 |
| `dio_104t` | 0 | 140 | 101 |

## Deutung

Die Nullkontrollen widerlegen Pareidolie nicht vollstaendig.

Sie zeigen aber einen klaren Unterschied:

```text
Die strukturierte Mosaikwelt erzeugt eine engere, wiedererkennbare Rollenlandschaft.
Die Nullwelten erzeugen deutlich mehr Symbolstreuung und andere Toprollen.
```

Besonders wichtig:

- `dio_1wdi` verschwindet in beiden Nullkontrollen.
- `dio_1fll` verschwindet in beiden Nullkontrollen.
- Die Symbolbreite steigt von `97` auf `224` bzw. `221`.
- Der Nachhall sinkt deutlich.
- Die Shuffle-Kontrolle senkt Stable Ratio und erhoeht Carried Unrest klar.

Damit spricht der aktuelle Befund gegen eine reine menschliche Musterdeutung.

Die Rollen erscheinen nicht beliebig. Sie reagieren auf die konkrete Weltordnung.

## Was Das Noch Nicht Beweist

Diese Pruefung beweist noch nicht, dass MINI_DIO im starken Sinn "lernt".

Sicherer ist aktuell:

```text
MINI_DIO bildet reproduzierbare Feldantworten,
die sich bei strukturierter Welt anders verhalten als bei Nullwelten.
```

Ob daraus Lernen im engeren Sinn wird, muss zusaetzlich geprueft werden:

- gleiche Welt mit wachsender Memory,
- Folgegeneration ohne Reset,
- Holdout-Welt nach Memory-Aufbau,
- Messung, ob alte Bedeutungen wiederverwendet statt neu erfunden werden,
- Vergleich gegen mehrere zufaellige Nullwelten.

## MCM-Lesung

Die bisherige MCM-Deutung wird dadurch methodisch staerker:

```text
Nicht jedes Rauschen erzeugt dieselbe Bedeutungslandschaft.
Weltordnung beeinflusst Feldordnung.
Zerstoerte Ordnung fuehrt zu breiterer Symbolstreuung.
Strukturierte Ordnung fuehrt zu engerer Rollenbindung.
```

Das ist kein endgueltiger Beweis, aber ein wichtiger Schritt weg von reiner Pareidolie.
