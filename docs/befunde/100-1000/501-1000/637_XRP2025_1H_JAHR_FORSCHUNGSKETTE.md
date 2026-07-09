# Aktueller Forschungslauf

Stand: 2026-06-22 01:11:56

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_xrp_2025_1h_10k_XRPUSDT.csv`
- Kerzen: `8760`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `647` -> `647`
- Episoden: `8754` -> `8754`
- geschriebene Episodenmemory: `51` -> `51`
- MCM-Rekopplung: `0.703798` -> `0.703396`
- MCM-Tragqualitaet: `0.53425` -> `0.53465`
- Sinnes-MCM-Kopplung: `0.84377` -> `0.84339`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1ewh8ej`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1ewh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `26`
- `kippend`: `106`
- `stabil`: `7185`
- `tragend_unruhig`: `1437`

Episodenzustaende:

- `field_carried`: `8728`
- `field_strained`: `26`

## Artefakte

- Debug: `debug\xrp_2025_1h_10k`
- Memory: `memory\xrp_2025_1h_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
