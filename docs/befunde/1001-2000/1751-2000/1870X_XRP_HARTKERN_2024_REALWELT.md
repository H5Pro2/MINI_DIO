# 1870X - XRP Hartkern unter 2024-Realwelt

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
| `real` | 1 | 30.00 | 0.750 | 0.359 | 0.3471 | 0.1663 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 31.00 | 0.680 | 0.227 | 0.3359 | 0.1617 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 31.00 | 0.647 | 0.256 | 0.3222 | 0.1539 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| XRP | 0 | 0.0700 | 0.1032 | 0.0112 | 0.0046 | 0.0663 | `realwelt_kernnaehe_staerker` |

## Befund

Fensterzustände:
- `realwelt_kernnaehe_staerker`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
