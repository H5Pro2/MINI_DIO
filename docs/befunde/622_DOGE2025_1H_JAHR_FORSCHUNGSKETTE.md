# Aktueller Forschungslauf

Stand: 2026-06-22 00:27:32

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_doge_2025_1h_10k_DOGEUSDT.csv`
- Kerzen: `8760`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `606` -> `606`
- Episoden: `8754` -> `8754`
- geschriebene Episodenmemory: `41` -> `39`
- MCM-Rekopplung: `0.703664` -> `0.70326`
- MCM-Tragqualitaet: `0.534177` -> `0.53458`
- Sinnes-MCM-Kopplung: `0.843424` -> `0.843042`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `19`
- `kippend`: `111`
- `stabil`: `7119`
- `tragend_unruhig`: `1505`

Episodenzustaende:

- `field_carried`: `8735`
- `field_strained`: `19`

## Artefakte

- Debug: `debug\doge_2025_1h_year`
- Memory: `memory\doge_2025_1h_year_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
