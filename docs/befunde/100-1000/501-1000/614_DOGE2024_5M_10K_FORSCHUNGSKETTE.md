# Aktueller Forschungslauf

Stand: 2026-06-22 00:20:18

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_doge_2024_5m_10k_DOGEUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `685` -> `685`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `38` -> `36`
- MCM-Rekopplung: `0.704075` -> `0.703649`
- MCM-Tragqualitaet: `0.534556` -> `0.53498`
- Sinnes-MCM-Kopplung: `0.844305` -> `0.843903`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `19`
- `kippend`: `90`
- `stabil`: `8230`
- `tragend_unruhig`: `1655`

Episodenzustaende:

- `field_carried`: `9975`
- `field_strained`: `19`

## Artefakte

- Debug: `debug\doge_2024_5m_10k`
- Memory: `memory\doge_2024_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
