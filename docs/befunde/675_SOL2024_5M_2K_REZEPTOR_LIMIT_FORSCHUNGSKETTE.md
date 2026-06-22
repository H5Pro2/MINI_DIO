# Aktueller Forschungslauf

Stand: 2026-06-22 10:55:21

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
- Unique Syntaxsymbole: `348` -> `348`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `11` -> `11`
- MCM-Rekopplung: `0.692315` -> `0.69155`
- MCM-Tragqualitaet: `0.508614` -> `0.509367`
- Sinnes-MCM-Kopplung: `0.840529` -> `0.839811`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_0pz659c, dio_104t4us, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_0pz6, dio_104t, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `5`
- `kippend`: `23`
- `stabil`: `1567`
- `tragend_unruhig`: `399`

Episodenzustaende:

- `field_carried`: `1989`
- `field_strained`: `5`

## Artefakte

- Debug: `debug\receptor_limit_sol_2024_5m_2k_current`
- Memory: `bot_memory\receptor_limit_sol_2024_5m_2k_current.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
