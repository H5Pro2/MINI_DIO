# 1715 - dio_0ly7 Einzelachse gegen gekoppelte Last

Stand: 2026-07-07

## Zweck

Diese Diagnose fasst die letzten synthetischen Gegenproben zusammen.
Sie trennt zwei Fragen:

1. Bricht `dio_0ly7`, wenn nur einzelne Sinnesachsen gestoert werden?
2. Bricht `dio_0ly7`, wenn Range-Aufweitung, Hoeranstieg und Spannungsanstieg gekoppelt auftreten?

Die Diagnose bleibt passiv:

```text
keine Handlung
kein Gate
keine Richtung
keine Strategie
```

## Grundlage

Einzelachsenpruefung:

- Quelle: [1713_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION.md](1713_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION.md)
- Klassifikation: [1714_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION_KLASSEN.md](1714_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION_KLASSEN.md)

Gekoppelte synthetische Last:

- Quelle: [1710_DIO_0LY7_SYNTHETISCHE_BRUCHURSACHEN.md](1710_DIO_0LY7_SYNTHETISCHE_BRUCHURSACHEN.md)
- Klassifikation: [1711_DIO_0LY7_SYNTHETISCHE_BRUCHURSACHEN_KLASSEN.md](1711_DIO_0LY7_SYNTHETISCHE_BRUCHURSACHEN_KLASSEN.md)

## Vergleich

| Pruefung | Sichtbare Welten | Klasse | Delta Hoeren | Delta Spannung | Delta Range |
|---|---:|---|---:|---:|---:|
| Einzelachsenstoerung | 2 von 6 | `oeffnung_getragen` | -0.055357 | -0.052200 | +0.175662 |
| gekoppelte synthetische Last | 6 von 6 | `bruch_mit_range_aufweitung` | +0.015928 | +0.012576 | +0.063908 |

## Lesung

Die Einzelachsenpruefung bricht `dio_0ly7` bisher nicht.
Wenn die Form dort sichtbar genug ist, bleiben Hoeren und Spannung negativ.
Das Feldzeichen wird also weiter als Entlastungsbewegung gelesen.

Die gekoppelte Lastpruefung zeigt das Gegenteil:
Wenn Range-Aufweitung mit Hoeranstieg und Spannungsanstieg zusammenfaellt, kippt `dio_0ly7` stabil in `bruch_mit_range_aufweitung`.

Damit wird die bisherige Ursache enger:

```text
Nicht:
  Range allein
  Hoeren allein
  Sicht allein
  Desynchronisation allein

Sondern:
  gekoppelte synthetische Last
    = Range-Aufweitung
    + Hoeranstieg
    + Spannungsanstieg
```

## Bedeutung fuer die MCM-Lesung

`dio_0ly7` wirkt dadurch nicht wie ein hartes Ausgabesymbol.
Die gleiche Familie kann je nach Weltmilieu anders getragen werden:

```text
reale / einzelachsige Entlastung
  -> Oeffnung bleibt getragen

gekoppelte synthetische Last
  -> Oeffnung kippt in Bruch
```

Das stuetzt die Lesung:

```text
MCM-Bedeutung = Familie + Weltmilieu + Feldwirkung
```

Nicht nur die Symbolfamilie selbst entscheidet.
Entscheidend ist, welche gekoppelte Feldlage sie im Kontakt traegt.

## Grenze

Der Befund zeigt keine Handlung und keine Absicht.
Er zeigt eine passive Feldunterscheidung:

```text
Einzelachsenstoerung wird anders gelesen als gekoppelte Last.
```
