# Aktueller Forschungslauf

Stand: 2026-06-22 12:47:51

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_xrp_2024_1h_10k_XRPUSDT.csv`
- Kerzen: `8784`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `643` -> `643`
- Episoden: `8778` -> `8778`
- geschriebene Episodenmemory: `11` -> `11`
- MCM-Rekopplung: `0.706391` -> `0.70599`
- MCM-Tragqualitaet: `0.537675` -> `0.538075`
- Sinnes-MCM-Kopplung: `0.843857` -> `0.843478`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0dd2ogm, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0dd2, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `4`
- `kippend`: `69`
- `stabil`: `7142`
- `tragend_unruhig`: `1563`

Episodenzustaende:

- `field_carried`: `8774`
- `field_strained`: `4`

## Artefakte

- Debug: `debug\adapted_time_xrp_2024_1h_10k`
- Memory: `bot_memory\adapted_time_xrp_2024_1h_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
