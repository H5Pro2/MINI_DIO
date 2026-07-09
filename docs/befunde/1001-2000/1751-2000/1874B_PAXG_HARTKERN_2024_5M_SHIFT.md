# 1874B - PAXG Hartkern unter 2024-5m-Folgefenster

## Grundfrage

Bleibt der Realwelt-Vorsprung ueber mehrere Startpunkte hinweg sichtbar, oder ist er nur ein Fensterartefakt?

## Methode

- Pro Asset und Startpunkt wird ein Realfenster geschnitten.
- Daraus entstehen zwei assetnahe Nullwelten: Random-Sign und Shuffle-Order.
- Alle Laeufe bleiben passiv und nutzen `world_relative`.
- Bewertet werden Quellennaehe, Kernnaehe, Nachhall-Delta und Feldzeit-Delta.

## Gruppenvergleich

| Gruppe | Welten | Kernfamilien Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |
|---|---:|---:|---:|---:|---:|---:|---|
| `real` | 1 | 29.00 | 0.585 | 0.268 | 0.3288 | 0.1589 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 31.00 | 0.615 | 0.256 | 0.3106 | 0.1498 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 32.00 | 0.556 | 0.222 | 0.3157 | 0.1521 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 4000 | -0.0305 | 0.0125 | 0.0131 | 0.0068 | 0.0010 | `graduell_gemischt` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
