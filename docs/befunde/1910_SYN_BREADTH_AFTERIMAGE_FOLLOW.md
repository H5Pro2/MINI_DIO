# 1910 - Synthetische Weltpassung Breite Nachhall Follow

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
| `real` | 1 | 3.00 | 0.053 | 0.000 | 0.1841 | 0.1631 | `reifungsrolle_teilweise_reproduziert:1` |
| `null_random` | 1 | 8.00 | 0.095 | 0.000 | 0.1782 | 0.1107 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 32.00 | 0.556 | 0.279 | 0.4186 | 0.2065 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| DOGE | 0 | -0.5029 | -0.2791 | -0.2345 | -0.0434 | -0.2930 | `nullwelt_staerker` |

## Befund

Fensterzustände:
- `nullwelt_staerker`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
