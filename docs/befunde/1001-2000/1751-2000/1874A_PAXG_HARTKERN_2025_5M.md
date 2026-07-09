# 1874A - PAXG Hartkern unter 2025-5m-Realwelt

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
| `real` | 1 | 29.00 | 0.647 | 0.268 | 0.3521 | 0.1715 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 28.00 | 0.556 | 0.186 | 0.3167 | 0.1531 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 29.00 | 0.585 | 0.182 | 0.3283 | 0.1576 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| PAXG | 0 | 0.0622 | 0.0822 | 0.0238 | 0.0139 | 0.0582 | `realwelt_kernnaehe_staerker` |

## Befund

Fensterzustände:
- `realwelt_kernnaehe_staerker`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
