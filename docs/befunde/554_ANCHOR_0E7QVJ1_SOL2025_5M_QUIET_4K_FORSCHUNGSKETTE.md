# Aktueller Forschungslauf

Stand: 2026-06-21 21:12:41

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_long_sol_2025_5m_quiet_4000.csv`
- Kerzen: `4000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `449` -> `449`
- Episoden: `3994` -> `3994`
- geschriebene Episodenmemory: `17` -> `17`
- MCM-Rekopplung: `0.697618` -> `0.696999`
- MCM-Tragqualitaet: `0.520809` -> `0.521423`
- Sinnes-MCM-Kopplung: `0.841532` -> `0.840949`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_1ewh8ej, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_155c, dio_1ewh, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `8`
- `kippend`: `38`
- `stabil`: `3153`
- `tragend_unruhig`: `795`

Episodenzustaende:

- `field_carried`: `3986`
- `field_strained`: `8`

## Artefakte

- Debug: `debug\anchor_0e7qvj1_sol2025_5m_quiet_4k`
- Memory: `memory\anchor_0e7qvj1_sol2025_5m_quiet_4k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
