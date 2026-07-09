# 1880D - DOGE Hartkern neues Folgefenster

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
| `real` | 1 | 34.00 | 0.615 | 0.239 | 0.4186 | 0.3676 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 34.00 | 0.585 | 0.213 | 0.3956 | 0.3062 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 35.00 | 0.527 | 0.160 | 0.4342 | 0.3657 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| DOGE | 0 | 0.0305 | 0.0264 | -0.0156 | 0.0019 | 0.0174 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |

## Befund

Fensterzustände:
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
