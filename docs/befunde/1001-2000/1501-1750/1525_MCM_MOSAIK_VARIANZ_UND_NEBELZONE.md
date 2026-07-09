# 1525 - MCM-Mosaik Varianz und Nebelzone

## Zweck

Nach 1524 war klar:

```text
Eine verlaengerte Wiederholung der Mosaik-Welt erhaelt die Rollenlandschaft.
```

Die naechste Unterpruefung musste daher echte neue Varianz enthalten.

Die konkrete Frage:

```text
Bleibt die Mosaik-Rollenlandschaft auch bei neu verschraenkter Phasenfolge stabil,
oder entstehen neue Nebel-/Kippanteile?
```

## Datenbasis

```text
data/synthetic_1525_melody_randrollen_interwoven_mosaic_2400_5m.csv
```

Die Welt wurde aus den Phasen der 1521-Mosaik-Welt neu zusammengesetzt:

- Bruchphasen,
- Startphasen,
- Shiftphasen,
- Endphasen,
- Wellenphasen.

Die OHLC-Werte wurden fortlaufend gestitcht, damit keine kuenstlichen Preisspruenge entstehen.

Ausgefuehrt:

```text
--runs 2
--reset-memory
--sense-mode world_relative
```

## Ergebnis

| Welt | Kerzen | Unique Symbols | Stable Ratio | Carried Unrest | Tipping Ratio | Avg Afterimage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1521 Mosaik 1200 | 1200 | 85 | 0.8719 | 0.1281 | 0.0000 | 0.3666 |
| 1524 Mosaik 3600 | 3600 | 86 | 0.8703 | 0.1297 | 0.0000 | 0.4269 |
| 1525 verschraenktes Mosaik 2400 | 2400 | 97 | 0.8759 | 0.1236 | 0.0004 | 0.4053 |

Die wichtigsten Rollen bleiben reproduzierbar erhalten:

| Rolle | 1521 Count pro Lauf | 1525 Count pro Lauf | Lesung |
| --- | ---: | ---: | --- |
| `dio_0l7p` | 134 | 256 | fuehrende Rekopplungs-/Wechselnaehe |
| `dio_1wdi` | 94 | 195 | nachhallender Randbruch |
| `dio_14wj` | 65 | 134 | ruhige sensorische Rekopplungsnaehe |
| `dio_1fll` | 40 | 77 | robuste Rand-/Bruch-Feldqualitaet |

## Deutung

1525 erzeugt keine neue dominante Einzelrolle.

Stattdessen passiert Folgendes:

```text
Die Rollenlandschaft bleibt erhalten.
Die Symbolbreite steigt.
Eine sehr kleine Kippnaehe erscheint.
Der Nachhall bleibt hoeher als in 1521.
```

Damit wirkt 1525 wie eine echte Mosaik-Varianz:

- nicht nur Wiederholung,
- nicht nur Zerfall,
- nicht nur Einzelrollendominanz,
- sondern verteilte Rollen mit groesserer Oberflaechenvarianz.

## MCM-Lesung

Der Befund passt zur aktuellen Feldraum-Deutung:

```text
Zentrum ist nicht nur ein Punkt, sondern Gravitation/Bindung.
Rand ist nicht nur Grenze, sondern ein Spannungsraum.
Bruecken sind Uebergangskorridore.
Nebelzonen sind noch nicht vollstaendig verdichtete Bedeutungsraeume.
Nachhall gibt Tiefe in die Zeit.
Wiederkehr verdichtet aus Nebel eine Rolle.
```

1525 zeigt besonders den Nebelzonen-Aspekt:

```text
Mehr Symbolbreite entsteht,
aber die tragenden Rollen zerfallen nicht.
```

Die neue Kippnaehe ist extrem klein. Sie wird daher nicht als Feldkollaps gelesen, sondern als Randkontakt innerhalb einer weiter tragenden Mosaiklandschaft.

## Grenze

Die Welt ist synthetisch und aus vorhandenen Mosaikphasen gebaut.

Sie beweist keine allgemeine Topologie. Sie zeigt aber, dass neue Phasenverschraenkung nicht automatisch zu beliebigem Rauschen fuehrt.
