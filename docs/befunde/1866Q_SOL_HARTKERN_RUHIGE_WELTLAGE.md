# 1866Q - SOL Hartkern unter ruhiger Weltlage

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
| `real` | 1 | 31.00 | 0.680 | 0.256 | 0.3799 | 0.1886 | `reifungsrolle_reproduziert:1` |
| `null_random` | 1 | 30.00 | 0.615 | 0.205 | 0.3737 | 0.1909 | `reifungsrolle_reproduziert:1` |
| `null_shuffle` | 1 | 30.00 | 0.615 | 0.262 | 0.3387 | 0.1638 | `reifungsrolle_reproduziert:1` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| SOL | 0 | 0.0646 | -0.0061 | 0.0063 | -0.0023 | 0.0140 | `realwelt_anschluss_staerker` |

## Befund

Fensterzustände:
- `realwelt_anschluss_staerker`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
