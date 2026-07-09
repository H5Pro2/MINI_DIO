# 1880B - BTC Hartkern neues Folgefenster

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
| `real` | 1 | 28.00 | 0.647 | 0.186 | 0.3644 | 0.2898 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 33.00 | 0.527 | 0.167 | 0.3870 | 0.3152 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 32.00 | 0.585 | 0.196 | 0.4077 | 0.3623 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 0 | 0.0622 | -0.0096 | -0.0433 | -0.0725 | -0.0062 | `graduell_gemischt` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
