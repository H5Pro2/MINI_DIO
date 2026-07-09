# 1885P1 - PAXG Hartkern Folgefenster 6000 7000

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
| `real` | 1 | 34.00 | 0.647 | 0.188 | 0.4034 | 0.3265 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 35.00 | 0.647 | 0.289 | 0.4059 | 0.3396 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 33.00 | 0.615 | 0.244 | 0.4144 | 0.3590 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | 0.0000 | -0.1014 | -0.0110 | -0.0325 | -0.0522 | `graduell_nullnaeher` |

## Befund

Fensterzustände:
- `graduell_nullnaeher`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
