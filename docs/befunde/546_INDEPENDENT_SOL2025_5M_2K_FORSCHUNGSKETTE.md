# Aktueller Forschungslauf

Stand: 2026-06-21 21:04:20

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `360` -> `360`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `11` -> `11`
- MCM-Rekopplung: `0.69156` -> `0.690776`
- MCM-Tragqualitaet: `0.506507` -> `0.507279`
- Sinnes-MCM-Kopplung: `0.84074` -> `0.840004`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_155c, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `5`
- `kippend`: `17`
- `stabil`: `1564`
- `tragend_unruhig`: `408`

Episodenzustaende:

- `field_carried`: `1989`
- `field_strained`: `5`

## Artefakte

- Debug: `debug\independent_sol2025_5m_2k`
- Memory: `memory\independent_sol2025_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
