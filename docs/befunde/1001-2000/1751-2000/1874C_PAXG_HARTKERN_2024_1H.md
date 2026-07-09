# 1874C - PAXG Hartkern unter 2024-1h-Realwelt

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
| `real` | 1 | 30.00 | 0.615 | 0.205 | 0.3503 | 0.1687 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 30.00 | 0.680 | 0.293 | 0.3318 | 0.1582 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 31.00 | 0.680 | 0.286 | 0.3354 | 0.1618 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | -0.0646 | -0.0881 | 0.0149 | 0.0069 | -0.0525 | `nullwelt_staerker` |

## Befund

Fensterzustände:
- `nullwelt_staerker`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
