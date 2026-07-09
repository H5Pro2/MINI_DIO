# 1869BQ - BTC Hartkern unter ruhiger Weltlage

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
| `real` | 1 | 33.00 | 0.647 | 0.273 | 0.4334 | 0.2155 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 33.00 | 0.647 | 0.273 | 0.4138 | 0.2031 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 33.00 | 0.647 | 0.217 | 0.4253 | 0.2100 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 0 | 0.0000 | 0.0000 | 0.0081 | 0.0055 | 0.0020 | `graduell_realer_nachhall_ohne_kern` |

## Befund

Fensterzustände:
- `graduell_realer_nachhall_ohne_kern`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
