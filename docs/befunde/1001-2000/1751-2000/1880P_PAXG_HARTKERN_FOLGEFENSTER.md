# 1880P - PAXG Hartkern neues Folgefenster

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
| `real` | 1 | 33.00 | 0.585 | 0.244 | 0.3930 | 0.3154 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 36.00 | 0.556 | 0.204 | 0.4200 | 0.3349 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 33.00 | 0.556 | 0.120 | 0.3908 | 0.3592 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | 0.0294 | 0.0404 | -0.0270 | -0.0439 | 0.0149 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |

## Befund

Fensterzustände:
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
