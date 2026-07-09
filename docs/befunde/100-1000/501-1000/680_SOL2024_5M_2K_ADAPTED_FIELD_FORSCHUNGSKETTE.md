# Aktueller Forschungslauf

Stand: 2026-06-22 11:03:27

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `351` -> `351`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `5` -> `5`
- MCM-Rekopplung: `0.69333` -> `0.692536`
- MCM-Tragqualitaet: `0.509904` -> `0.510687`
- Sinnes-MCM-Kopplung: `0.837933` -> `0.837187`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_0oc3c1g, dio_0pz659c, dio_104t4us, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_0h9h, dio_0l7p, dio_0m9z, dio_0oc3, dio_0pz6, dio_104t, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `2`
- `kippend`: `15`
- `stabil`: `1504`
- `tragend_unruhig`: `473`

Episodenzustaende:

- `field_carried`: `1992`
- `field_strained`: `2`

## Artefakte

- Debug: `debug\adapted_field_sol_2024_5m_2k`
- Memory: `bot_memory\adapted_field_sol_2024_5m_2k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
