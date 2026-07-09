# 1863 - Passive lokale Reifegruppe: weitere Folgefenster

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
| `real` | 10 | 30.50 | 0.691 | 0.309 | 0.3443 | 0.1675 | `reifungsrolle_reproduziert:10` |
| `null_random` | 10 | 30.50 | 0.678 | 0.307 | 0.3406 | 0.1652 | `reifungsrolle_reproduziert:10` |
| `null_shuffle` | 10 | 30.20 | 0.650 | 0.273 | 0.3352 | 0.1610 | `reifungsrolle_reproduziert:10` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 5000 | 0.0700 | 0.0590 | 0.0056 | 0.0043 | 0.0455 | `realwelt_kernnaehe_staerker` |
| BTC | 10000 | 0.0343 | 0.0000 | -0.0021 | 0.0024 | 0.0086 | `graduell_gemischt` |
| DOGE | 5000 | 0.0000 | 0.0358 | -0.0126 | -0.0068 | 0.0132 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |
| DOGE | 10000 | -0.0343 | -0.0459 | -0.0292 | -0.0160 | -0.0360 | `graduell_nullnaeher` |
| PAXG | 5000 | 0.0000 | -0.0174 | 0.0043 | 0.0025 | -0.0068 | `graduell_realer_nachhall_ohne_kern` |
| PAXG | 10000 | 0.0000 | -0.0631 | 0.0019 | 0.0008 | -0.0280 | `graduell_nullnaeher` |
| SOL | 5000 | -0.0343 | -0.0989 | 0.0006 | 0.0013 | -0.0528 | `graduell_nullnaeher` |
| SOL | 10000 | -0.0329 | 0.0314 | 0.0056 | 0.0034 | 0.0072 | `graduell_gemischt` |
| XRP | 5000 | 0.0000 | 0.0173 | 0.0108 | 0.0064 | 0.0104 | `graduell_gemischt` |
| XRP | 10000 | 0.0000 | 0.0000 | 0.0065 | 0.0036 | 0.0015 | `graduell_realer_nachhall_ohne_kern` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 3
- `graduell_nullnaeher`: 3
- `graduell_realer_nachhall_ohne_kern`: 2
- `realwelt_kernnaehe_staerker`: 1
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
