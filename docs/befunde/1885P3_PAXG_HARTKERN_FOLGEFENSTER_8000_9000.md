# 1885P3 - PAXG Hartkern Folgefenster 8000 9000

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
| `real` | 1 | 32.00 | 0.585 | 0.250 | 0.3998 | 0.3389 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 34.00 | 0.474 | 0.188 | 0.4375 | 0.3585 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 32.00 | 0.527 | 0.196 | 0.4257 | 0.3794 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | 0.0576 | 0.0543 | -0.0377 | -0.0405 | 0.0271 | `graduell_realnaeher_kern` |

## Befund

Fensterzustände:
- `graduell_realnaeher_kern`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
