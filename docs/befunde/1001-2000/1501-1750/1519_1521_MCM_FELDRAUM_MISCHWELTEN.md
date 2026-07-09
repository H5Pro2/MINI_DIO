# 1519-1521 - MCM-Feldraum in Mischwelten

## Zweck

Nach den Rand-/Bruch-Härtefällen war die nächste Frage nicht mehr nur:

```text
Bleibt dio_1fll stabil?
```

sondern:

```text
Was passiert, wenn Rand/Bruch mit Rekopplung, Zentrum und mehreren Rollen gemischt wird?
```

Diese Prüfung untersucht, ob MINI_DIO dann eine einzelne Randrolle hält oder ob ein mehrdimensionalerer Feldraum sichtbar wird.

## Datenbasis

Geprüft wurden drei Mischwelten mit frischer Memory:

```text
1519: data/kontrolliert_synthetic_mcm_sequenz_bruch_rand_rekopplung_vor_rand_5m.csv
1520: data/kontrolliert_synthetic_mcm_sequenz_bruch_rand_rekopplung_lang_vor_rand_5m.csv
1521: data/synthetic_1502_melody_randrollen_full_mosaic_1200_5m.csv
```

Alle Läufe wurden mit `world_relative` und je zwei Wiederholungen ausgeführt.

## Ergebnis 1: Rekopplung Vor Rand

In den direkten Mischungen aus Rand/Bruch und Rekopplung bleibt `dio_1fllaqz` dominant.

| Welt | Top Symbol | Top Count pro Lauf | Stable Ratio | Carried Unrest | Avg Afterimage |
| --- | --- | ---: | ---: | ---: | ---: |
| 1519 Rekopplung vor Rand | `dio_1fllaqz` | 3321 | 0.9541 | 0.0450 | 0.6954 |
| 1520 lange Rekopplung vor Rand | `dio_1fllaqz` | 4361 | 0.9590 | 0.0403 | 0.7321 |

`dio_0l7p`, `dio_14wj` und `dio_1wdi` bleiben in diesen beiden Welten bei `0`.

Das bedeutet:

```text
Rekopplungsanteile allein lösen dio_1fll nicht auf.
Sie können die Rand-/Bruch-Feldqualität sogar tragender machen.
```

## Ergebnis 2: Rollen-Mosaik

In der breiten Mosaik-Welt verschiebt sich das Bild.

`dio_1fll` bleibt vorhanden, ist aber nicht mehr dominant.

| Rolle | Count pro Lauf | Lesung |
| --- | ---: | --- |
| `dio_0l7p` | 134 | fokussierte Wechselnähe |
| `dio_1wdi` | 94 | nachhallender Randbruch |
| `dio_14wj` | 65 | ruhige sensorische Rekopplungsnähe |
| `dio_1fll` | 40 | robuste Rand-/Bruch-Feldqualität |

Die Innenfeldwerte ändern sich ebenfalls:

```text
Stable Ratio:        0.8719
Carried Unrest:      0.1281
Avg Afterimage:      0.3666
Unique Symbols:      85
```

Das Mosaik erzeugt also keine dominante Einzelrolle, sondern eine gemeinsame Rollenlandschaft.

## Deutung

Die bisherigen Befunde sprechen dafür, dass MINI_DIO keine flache Symboltabelle bildet.

Sichtbar wird eher ein Feldraum:

```text
Zentrum ist nicht nur ein Punkt, sondern Gravitation/Bindung.
Rand ist nicht nur Grenze, sondern ein Spannungsraum.
Brücken sind Übergangskorridore.
Nebelzonen sind noch nicht vollständig verdichtete Bedeutungsräume.
Nachhall gibt Tiefe in die Zeit.
Wiederkehr verdichtet aus Nebel eine Rolle.
```

In den klaren Rand-/Bruchwelten verdichtet sich dieser Raum stark auf `dio_1fll`.

In der Mosaik-Welt verteilt sich die Wirkung auf mehrere Rollen. Das wirkt nicht wie Zerfall, sondern wie ein mehrdimensionalerer Bedeutungsraum.

## MCM-Lesung

Die aktuelle Arbeitsdeutung:

```text
Reine Rand-/Bruchqualität -> dio_1fll wird dominant.
Rand/Bruch + Rekopplung -> dio_1fll bleibt dominant und tragend.
Mosaik aus mehreren Rollen -> mehrere Feldrollen erscheinen parallel.
```

Das stützt die Annahme, dass die MCM-Topologie schichtig und räumlich gelesen werden muss:

- Zentrum,
- Übergänge,
- Rand,
- Kippnähe,
- Nebelzonen,
- Nachhallräume.

Die Rollen liegen nicht einfach nebeneinander. Sie wirken wie unterschiedliche Verdichtungen in einem gemeinsamen Feldraum.

## Grenze

Das ist eine Arbeitsdeutung, kein Beweis.

Noch offen ist:

- ob die Mosaik-Rollen auch bei längeren Mosaikwelten stabil bleiben,
- ob zwischen `dio_0l7p`, `dio_1wdi`, `dio_14wj` und `dio_1fll` eigene Brückenrollen entstehen,
- ob Nebelzonen messbar früher auftreten als spätere Rollenverdichtung.
