# 1874D - PAXG Hartkern unter 2025-1h-Realwelt

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
| `real` | 1 | 30.00 | 0.680 | 0.293 | 0.3405 | 0.1647 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 31.00 | 0.714 | 0.317 | 0.3398 | 0.1640 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 31.00 | 0.647 | 0.256 | 0.3370 | 0.1617 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | -0.0343 | -0.0244 | 0.0007 | 0.0006 | -0.0193 | `graduell_realer_nachhall_ohne_kern` |

## Befund

Fensterzustände:
- `graduell_realer_nachhall_ohne_kern`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
