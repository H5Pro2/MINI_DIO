# 1848 - Anschlussqualität: neue Mehrasset-Fenster

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
| `real` | 10 | 28.00 | 0.708 | 0.326 | 0.2937 | 0.1421 | `reifungsrolle_reproduziert:10` |
| `null_random` | 10 | 28.10 | 0.671 | 0.291 | 0.2966 | 0.1439 | `reifungsrolle_reproduziert:10` |
| `null_shuffle` | 10 | 27.30 | 0.645 | 0.276 | 0.2805 | 0.1351 | `reifungsrolle_reproduziert:10` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 2000 | -0.0343 | -0.0638 | -0.0002 | -0.0001 | -0.0373 | `graduell_nullnaeher` |
| BTC | 8000 | 0.0700 | 0.0419 | -0.0039 | -0.0046 | 0.0351 | `graduell_realnaeher_kern` |
| DOGE | 2000 | 0.0700 | 0.0963 | -0.0163 | -0.0076 | 0.0573 | `graduell_realnaeher_kern` |
| DOGE | 8000 | 0.0672 | 0.0650 | -0.0063 | -0.0032 | 0.0447 | `graduell_realnaeher_kern` |
| PAXG | 2000 | 0.0672 | 0.0473 | 0.0008 | -0.0004 | 0.0381 | `realwelt_anschluss_staerker` |
| PAXG | 8000 | 0.0000 | -0.0067 | -0.0023 | -0.0031 | -0.0038 | `graduell_gemischt` |
| SOL | 2000 | 0.0357 | 0.0286 | 0.0058 | 0.0049 | 0.0234 | `graduell_gemischt` |
| SOL | 8000 | -0.0343 | -0.0407 | -0.0116 | -0.0066 | -0.0296 | `graduell_nullnaeher` |
| XRP | 2000 | 0.0000 | 0.0175 | -0.0025 | -0.0020 | 0.0072 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |
| XRP | 8000 | 0.0343 | 0.0173 | 0.0034 | 0.0008 | 0.0170 | `graduell_gemischt` |

## Befund

Fensterzustände:
- `graduell_realnaeher_kern`: 3
- `graduell_gemischt`: 3
- `graduell_nullnaeher`: 2
- `realwelt_anschluss_staerker`: 1
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Einordnung

Die neuen Fenster bestätigen die Anschlussqualitäten aus `1846`, aber sie verschieben die Gewichtung.
Damit wirkt die Anschlussqualität nicht wie ein einmaliger Artefaktbegriff.

Wieder sichtbar:

- `graduell_realnaeher_kern`
- `graduell_kernnaehe_ohne_feldzeitvorsprung`
- `graduell_gemischt`

Neu deutlicher sichtbar:

- `graduell_nullnaeher`
- `realwelt_anschluss_staerker`

Der Gruppenvergleich bleibt vorsichtig zu lesen:
Realwelt liegt im Mittel bei Quellen- und Kernnähe vorne,
Null-Random liegt aber leicht höher bei Nachhall- und Feldzeit-Delta.
Das bestätigt die bisherige Linie:
Reifung ist keine harte Real/Null-Trennung, sondern eine Feldqualität mit mehreren Anschlussarten.

Fachlich bedeutet das:
Die passive Anschlussqualität sollte nicht aus einem einzigen Bericht gelesen werden.
Sie sollte mehrere Quellen bündeln und als breite Innenfeldbeschreibung tragen.
Dadurch wird die Feldrollen-Memory robuster, ohne daraus eine Steuerung zu machen.
