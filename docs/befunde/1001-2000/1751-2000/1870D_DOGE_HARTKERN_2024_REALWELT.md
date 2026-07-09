# 1870D - DOGE Hartkern unter 2024-Realwelt

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
| `real` | 1 | 31.00 | 0.680 | 0.286 | 0.3429 | 0.1656 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 30.00 | 0.714 | 0.293 | 0.3428 | 0.1666 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 29.00 | 0.680 | 0.300 | 0.3356 | 0.1624 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| DOGE | 0 | -0.0343 | -0.0143 | 0.0000 | -0.0009 | -0.0151 | `graduell_gemischt` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
