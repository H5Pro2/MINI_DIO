# Aktueller Forschungslauf

Stand: 2026-06-21 22:13:28

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_late_positive_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `644` -> `644`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `28` -> `26`
- MCM-Rekopplung: `0.702365` -> `0.701921`
- MCM-Tragqualitaet: `0.533221` -> `0.533663`
- Sinnes-MCM-Kopplung: `0.84153` -> `0.841111`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_1ewh8ej, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_155c, dio_1ewh, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `13`
- `kippend`: `79`
- `stabil`: `8073`
- `tragend_unruhig`: `1829`

Episodenzustaende:

- `field_carried`: `9981`
- `field_strained`: `13`

## Artefakte

- Debug: `debug\cross_anchor_2024_late_positive_10k`
- Memory: `memory\cross_anchor_2024_late_positive_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
