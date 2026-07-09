# Aktueller Forschungslauf

Stand: 2026-06-21 22:50:36

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2024_5m_10k_BTCUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `689` -> `689`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `40` -> `40`
- MCM-Rekopplung: `0.704055` -> `0.703662`
- MCM-Tragqualitaet: `0.534634` -> `0.535027`
- Sinnes-MCM-Kopplung: `0.844386` -> `0.844014`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `20`
- `kippend`: `79`
- `stabil`: `8297`
- `tragend_unruhig`: `1598`

Episodenzustaende:

- `field_carried`: `9974`
- `field_strained`: `20`

## Artefakte

- Debug: `debug\cross_anchor_btc2024_5m_10k`
- Memory: `memory\cross_anchor_btc2024_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
