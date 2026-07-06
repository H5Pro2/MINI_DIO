# Lokale Umschaltpunkte der Rollenöffnung

Stand: 2026-07-06

## Zweck

Nach der Rohwelt-Gegenlesung wurde geprüft, was lokal kurz vor Rollenwechseln geschieht.

Untersucht wurden dieselben breiten und engen Segmente:

```text
sideways Start 0 gegen Start 4000
negative_stress Start 2000 gegen Start 4000
positive_expansion Start 4000 gegen Start 8000
```

Die Frage:

```text
Was passiert kurz vor Rollenöffnung,
und was passiert kurz vor Rückkehr in stabile Einzelbindung?
```

## Rollenwechsel

### Seitwärts breit

```text
field_stabil -> field_tragend_unruhig: 177
field_tragend_unruhig -> field_stabil: 179
field_stabil -> field_kippend: 8
```

### Seitwärts eng

```text
field_stabil -> field_tragend_unruhig: 262
field_tragend_unruhig -> field_stabil: 269
field_stabil -> field_kippend: 9
```

### Stress breit

```text
field_stabil -> field_tragend_unruhig: 211
field_tragend_unruhig -> field_stabil: 211
field_stabil -> field_kippend: 5
```

### Stress eng

```text
field_stabil -> field_tragend_unruhig: 197
field_tragend_unruhig -> field_stabil: 204
field_stabil -> field_kippend: 14
```

### Expansion breit

```text
field_stabil -> field_tragend_unruhig: 353
field_tragend_unruhig -> field_stabil: 366
field_stabil -> field_kippend: 17
```

### Expansion eng

```text
field_stabil -> field_tragend_unruhig: 244
field_tragend_unruhig -> field_stabil: 251
field_stabil -> field_kippend: 12
```

## Lokale Mittelwerte vor Umschaltung

| Segment | Wechsel | n | pre Rekopplung | pre Strain | pre Nachhall | pre Hören | pre Formfluss | post Rekopplung | post Strain |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sideways breit | zu unruhig | 179 | 0.6960 | 0.1537 | 0.1436 | 0.0230 | -0.0243 | 0.6861 | 0.1650 |
| sideways breit | zu stabil | 186 | 0.6850 | 0.1658 | 0.1205 | 0.0705 | -0.0123 | 0.6966 | 0.1533 |
| sideways breit | zu kippend | 9 | 0.7050 | 0.1452 | 0.1486 | -0.0140 | -0.0653 | 0.6523 | 0.2044 |
| sideways eng | zu unruhig | 273 | 0.6931 | 0.1561 | 0.1253 | -0.0038 | -0.0092 | 0.6831 | 0.1675 |
| sideways eng | zu stabil | 272 | 0.6834 | 0.1667 | 0.1086 | 0.0342 | 0.0009 | 0.6935 | 0.1559 |
| sideways eng | zu kippend | 14 | 0.6968 | 0.1520 | 0.1258 | 0.0121 | -0.0078 | 0.6473 | 0.2047 |
| stress breit | zu unruhig | 215 | 0.6974 | 0.1521 | 0.1387 | 0.0084 | 0.0112 | 0.6869 | 0.1642 |
| stress breit | zu stabil | 216 | 0.6865 | 0.1639 | 0.1168 | 0.0382 | 0.0020 | 0.6983 | 0.1515 |
| stress breit | zu kippend | 9 | 0.6865 | 0.1577 | 0.0750 | 0.0749 | 0.1014 | 0.6339 | 0.2171 |
| stress eng | zu unruhig | 206 | 0.6969 | 0.1543 | 0.1591 | 0.0183 | -0.0042 | 0.6889 | 0.1634 |
| stress eng | zu stabil | 210 | 0.6872 | 0.1647 | 0.1380 | 0.0560 | 0.0003 | 0.6991 | 0.1519 |
| stress eng | zu kippend | 15 | 0.7060 | 0.1456 | 0.1641 | 0.0359 | -0.0816 | 0.6492 | 0.2022 |
| expansion breit | zu unruhig | 368 | 0.6897 | 0.1582 | 0.0980 | 0.0068 | 0.0356 | 0.6809 | 0.1684 |
| expansion breit | zu stabil | 371 | 0.6813 | 0.1682 | 0.0888 | 0.0167 | 0.0302 | 0.6897 | 0.1583 |
| expansion breit | zu kippend | 20 | 0.6902 | 0.1618 | 0.1141 | 0.0133 | 0.1462 | 0.6446 | 0.2079 |
| expansion eng | zu unruhig | 253 | 0.6939 | 0.1568 | 0.1390 | -0.0016 | 0.0090 | 0.6861 | 0.1662 |
| expansion eng | zu stabil | 256 | 0.6847 | 0.1676 | 0.1222 | 0.0462 | 0.0189 | 0.6952 | 0.1558 |
| expansion eng | zu kippend | 14 | 0.6989 | 0.1533 | 0.1674 | -0.0417 | -0.0240 | 0.6506 | 0.2027 |

## Befund

Die Umschaltungen zeigen eine stabile lokale Grundmechanik:

```text
stabil -> tragend_unruhig
= Rekopplung sinkt leicht, Strain steigt leicht

tragend_unruhig -> stabil
= Rekopplung steigt, Strain sinkt

zu kippend / gespannt
= kurze Belastungsspitze: Rekopplung fällt deutlich, Strain steigt deutlich
```

Diese Bewegung tritt in allen geprüften Segmenten auf.

## Wichtigste Einordnung

Rollenbreite entsteht nicht einfach aus vielen Rollenwechseln.

Beispiel:

```text
sideways eng hat mehr Wechsel als sideways breit,
aber nur 1/1 Sleep-Kombination statt 19/19.
```

Damit ist Rollenbreite nicht nur Wechselhäufigkeit.
Sie hängt eher davon ab, ob Wechsel eine getragene Mehrrollen-Nähe bilden oder nur zwischen zwei lokalen Zuständen pendeln.

## Rollenöffnung

Aktuelle Lesung:

```text
Rollenöffnung = stabiler Zustand wird nicht zerstört,
sondern kurz in tragend_unruhige Nähe erweitert.
```

Wenn diese Erweiterung mehrere Rollen gleichzeitig berührbar hält,
entsteht ein breiter Rollenraum.

Wenn sie schnell wieder in Einzelrekopplung fällt,
bleibt das Segment eng.

## Kippkontakte

Kippkontakte sind nicht automatisch Rollenbreite.
Sie wirken eher wie kurze Rand-/Belastungspunkte:

```text
zu kippend:
Rekopplung fällt stark,
Strain steigt stark.
```

Sie können Rollenöffnung begleiten,
aber sie tragen die Breite nicht allein.

## Bedeutung für MINI_DIO

MINI_DIOs MCM-Feld zeigt eine passive lokale Dynamik:

- Stabilisierung,
- tragende Unruhe,
- Kippkontakt,
- Rückkehr in Stabilität.

Diese Dynamik ist kein hartes Regelwerk.
Sie ist aus den Episodenwerten lesbar und bleibt über mehrere Welten ähnlich.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, ob breite Rollenräume eine höhere gemeinsame Co-Touch-Qualität besitzen als enge Rollenräume.
Das wäre der direkte Schritt von Rollenwechseln zu Bedeutungsnetz:

```text
nicht wie oft wechselt das Feld,
sondern welche Rollen bleiben gemeinsam anschlussfähig?
```
