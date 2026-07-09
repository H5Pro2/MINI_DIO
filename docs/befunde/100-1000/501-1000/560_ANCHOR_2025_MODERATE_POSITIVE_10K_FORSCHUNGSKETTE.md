# Aktueller Forschungslauf

Stand: 2026-06-21 21:17:57

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2025_moderate_positive_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `625` -> `625`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `39` -> `39`
- MCM-Rekopplung: `0.703122` -> `0.702686`
- MCM-Tragqualitaet: `0.534406` -> `0.534841`
- Sinnes-MCM-Kopplung: `0.841867` -> `0.841455`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_1ewh8ej, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_155c, dio_1ewh, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `19`
- `kippend`: `96`
- `stabil`: `8031`
- `tragend_unruhig`: `1848`

Episodenzustaende:

- `field_carried`: `9975`
- `field_strained`: `19`

## Artefakte

- Debug: `debug\anchor_2025_moderate_positive_10k`
- Memory: `memory\anchor_2025_moderate_positive_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
