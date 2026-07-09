# 1895D25A - DOGE 2025 1h Folgefenster 0 1000

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
| `real` | 1 | 34.00 | 0.585 | 0.188 | 0.3798 | 0.3116 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 34.00 | 0.527 | 0.188 | 0.4023 | 0.3655 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 32.00 | 0.556 | 0.170 | 0.4076 | 0.3352 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| DOGE | 0 | 0.0294 | 0.0000 | -0.0278 | -0.0540 | -0.0049 | `graduell_gemischt` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
