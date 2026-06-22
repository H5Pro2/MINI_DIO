# Aktueller Forschungslauf

Stand: 2026-06-21 23:54:52

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_paxg_2024_5m_10k_PAXGUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `528` -> `528`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `18` -> `18`
- MCM-Rekopplung: `0.713904` -> `0.713532`
- MCM-Tragqualitaet: `0.538243` -> `0.538615`
- Sinnes-MCM-Kopplung: `0.854857` -> `0.854505`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_1ewh8ej, dio_1fllaqz, dio_1pij39c, dio_1u5il5a`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0h9h, dio_0m9z, dio_104t, dio_14wj, dio_1ewh, dio_1fll, dio_1pij, dio_1u5i`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `7`
- `kippend`: `54`
- `stabil`: `8792`
- `tragend_unruhig`: `1141`

Episodenzustaende:

- `field_carried`: `9987`
- `field_strained`: `7`

## Artefakte

- Debug: `debug\paxg_2024_5m_10k`
- Memory: `memory\paxg_2024_5m_10k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
