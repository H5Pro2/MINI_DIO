# 1845 - MCM-Feldrollen-Memory: automatischer Mehrfenster-Test

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
| `real` | 6 | 10.50 | 0.720 | 0.283 | 0.1663 | 0.0831 | `reifungsrolle_teilweise_reproduziert:5; reifungsrolle_reproduziert:1` |
| `null_random` | 6 | 11.33 | 0.697 | 0.226 | 0.1664 | 0.0833 | `reifungsrolle_teilweise_reproduziert:6` |
| `null_shuffle` | 6 | 8.33 | 0.675 | 0.191 | 0.1577 | 0.0786 | `reifungsrolle_teilweise_reproduziert:6` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 0 | 0.0357 | 0.1200 | 0.0021 | 0.0016 | 0.0635 | `realwelt_kernnaehe_staerker` |
| BTC | 17000 | 0.0000 | 0.0207 | -0.0082 | -0.0043 | 0.0075 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |
| BTC | 34000 | 0.0343 | 0.0492 | -0.0035 | -0.0020 | 0.0299 | `graduell_realnaeher_kern` |
| SOL | 0 | 0.0000 | -0.0345 | 0.0086 | 0.0036 | -0.0137 | `graduell_realer_nachhall_ohne_kern` |
| SOL | 17000 | 0.0343 | 0.1538 | -0.0020 | -0.0005 | 0.0774 | `graduell_realnaeher_kern` |
| SOL | 34000 | 0.0000 | -0.0826 | -0.0046 | -0.0022 | -0.0382 | `graduell_nullnaeher` |

## Befund

Fensterzustände:
- `graduell_realnaeher_kern`: 2
- `realwelt_kernnaehe_staerker`: 1
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1
- `graduell_realer_nachhall_ohne_kern`: 1
- `graduell_nullnaeher`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Wie es weitergeht

Als nächstes sollte der Test auf mehr Assets mit vollständigen Jahresdateien erweitert werden.
Wenn die Fensterlesung stabil bleibt, kann daraus eine robustere Reifungs-Metrik für die passive Feldrollen-Memory entstehen.
