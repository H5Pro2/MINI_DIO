# 1853 - Familien-Anschlusskarte: neue Weltfenster

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
| `real` | 10 | 28.30 | 0.698 | 0.313 | 0.3150 | 0.1529 | `reifungsrolle_reproduziert:10` |
| `null_random` | 10 | 28.30 | 0.675 | 0.274 | 0.3048 | 0.1466 | `reifungsrolle_reproduziert:10` |
| `null_shuffle` | 10 | 29.00 | 0.635 | 0.263 | 0.3061 | 0.1468 | `reifungsrolle_reproduziert:10` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 1000 | 0.0000 | 0.0407 | 0.0153 | 0.0082 | 0.0218 | `realwelt_kernnaehe_staerker` |
| BTC | 7000 | 0.0700 | 0.0947 | -0.0078 | -0.0028 | 0.0585 | `graduell_realnaeher_kern` |
| DOGE | 1000 | 0.0000 | -0.0194 | -0.0029 | -0.0011 | -0.0093 | `graduell_gemischt` |
| DOGE | 7000 | 0.0000 | 0.0083 | 0.0022 | 0.0025 | 0.0045 | `graduell_gemischt` |
| PAXG | 1000 | 0.0329 | 0.0534 | 0.0063 | 0.0030 | 0.0337 | `realwelt_kernnaehe_staerker` |
| PAXG | 7000 | 0.0000 | 0.0119 | 0.0140 | 0.0094 | 0.0089 | `graduell_gemischt` |
| SOL | 1000 | 0.0672 | 0.0743 | 0.0250 | 0.0214 | 0.0572 | `realwelt_kernnaehe_staerker` |
| SOL | 7000 | 0.0646 | 0.0619 | 0.0113 | 0.0051 | 0.0465 | `realwelt_kernnaehe_staerker` |
| XRP | 1000 | -0.0672 | -0.0567 | -0.0072 | -0.0018 | -0.0437 | `nullwelt_staerker` |
| XRP | 7000 | 0.0000 | 0.0183 | -0.0024 | -0.0018 | 0.0076 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |

## Befund

Fensterzustände:
- `realwelt_kernnaehe_staerker`: 4
- `graduell_gemischt`: 3
- `graduell_realnaeher_kern`: 1
- `nullwelt_staerker`: 1
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.
