# 1467-1469 - Melodie-Gleichlage Stoerpruefung

## Zweck

Diese Pruefung stoert den reproduzierten Gleichlagenpunkt aus `1466`.

Die konkrete Frage war:

Ist die Gleichlage bei `0.00112 / block_size 13` punktfoermig, oder bildet sie ein kleines robustes Plateau?

## Aufbau

Geprueft wurden drei nahe Amplituden:

- `0.00110`
- `0.00112`
- `0.00114`

Alle Welten nutzen:

- `block_size 13`
- gleiche Melodiephasen,
- gleiche Richtungswechselzahl `455`,
- `world_relative`,
- frischen Speicher.

## Ergebnis

| Welt | Amp | `dio_0ein` | `dio_1fll` | Differenz | Dominanz | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1467 | 0.00110 | 175 | 173 | 2 | `dio_0ein` | 51 | 1140 | 54 | 0.732630 | 0.571927 |
| 1468 | 0.00112 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |
| 1469 | 0.00114 | 173 | 173 | 0 | gleich | 52 | 1138 | 56 | 0.732268 | 0.571119 |

## Befund

Die Gleichlage ist nicht nur ein isolierter Einzelpunkt.

`0.00112` und `0.00114` bleiben exakt in Balance.

`0.00110` kippt nur schwach zu `dio_0ein` mit einer Differenz von `2`.

Damit wirkt der Bereich wie ein kleines Gleichlagenplateau, nicht wie eine harte Linie.

## Lesung

MINI_DIO bildet hier eine stabile Bedeutungsnaehe zwischen `dio_0ein` und `dio_1fll`.

Die Feldantwort bleibt in allen drei Welten sehr eng:

- Rekopplung bleibt fast gleich,
- Nachhall bleibt fast gleich,
- stabile Wirkung bleibt hoch,
- tragende Unruhe steigt nur leicht.

Die Symbolentscheidung ist also nicht willkuerlich, sondern liegt in einem engen Feldnaehebereich.

## Schlussfolgerung

Der Kippbereich enthaelt ein kleines Plateau:

`0.00112` bis `0.00114`

Bei `0.00110` ist die Feldlage noch leicht `dio_0ein`-nah.

Die Grenze sollte deshalb nicht als Wert, sondern als Gleichlagenraum beschrieben werden.

## Grenze

Diese Pruefung bleibt innerhalb einer synthetischen Melodiefamilie.

Sie zeigt robuste lokale Balance, aber keine allgemeine Aussage ueber alle moeglichen Welten.
