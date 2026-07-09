# 1860 - Phasenlokale Familien: passende Folgefenster

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
| `real` | 10 | 29.50 | 0.688 | 0.320 | 0.3236 | 0.1577 | `reifungsrolle_reproduziert:10` |
| `null_random` | 10 | 29.10 | 0.684 | 0.300 | 0.3229 | 0.1575 | `reifungsrolle_reproduziert:10` |
| `null_shuffle` | 10 | 28.90 | 0.645 | 0.258 | 0.3065 | 0.1470 | `reifungsrolle_reproduziert:10` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 3000 | -0.0343 | 0.0000 | -0.0098 | -0.0052 | -0.0108 | `graduell_gemischt` |
| BTC | 9000 | 0.0000 | 0.0090 | -0.0093 | -0.0044 | 0.0020 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |
| DOGE | 3000 | 0.0357 | 0.0870 | 0.0069 | 0.0047 | 0.0498 | `realwelt_kernnaehe_staerker` |
| DOGE | 9000 | -0.0343 | -0.0323 | 0.0069 | 0.0028 | -0.0216 | `graduell_realer_nachhall_ohne_kern` |
| PAXG | 3000 | 0.0329 | 0.0395 | 0.0032 | 0.0005 | 0.0265 | `graduell_realnaeher_kern` |
| PAXG | 9000 | -0.0646 | -0.0302 | 0.0113 | 0.0048 | -0.0273 | `graduell_nullnaeher` |
| SOL | 3000 | 0.0343 | 0.0607 | -0.0096 | -0.0052 | 0.0337 | `graduell_realnaeher_kern` |
| SOL | 9000 | -0.0343 | 0.0000 | -0.0082 | -0.0037 | -0.0104 | `graduell_gemischt` |
| XRP | 3000 | -0.0329 | -0.0407 | 0.0053 | 0.0023 | -0.0254 | `graduell_nullnaeher` |
| XRP | 9000 | 0.0989 | 0.0845 | 0.0085 | 0.0058 | 0.0649 | `realwelt_kernnaehe_staerker` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 2
- `realwelt_kernnaehe_staerker`: 2
- `graduell_realnaeher_kern`: 2
- `graduell_nullnaeher`: 2
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1
- `graduell_realer_nachhall_ohne_kern`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
