# Aktueller Forschungslauf

Stand: 2026-06-22 12:33:51

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv`
- Kerzen: `10000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `643` -> `643`
- Episoden: `9994` -> `9994`
- geschriebene Episodenmemory: `10` -> `10`
- MCM-Rekopplung: `0.704545` -> `0.70412`
- MCM-Tragqualitaet: `0.536426` -> `0.536851`
- Sinnes-MCM-Kopplung: `0.839894` -> `0.839491`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `3`
- `kippend`: `47`
- `stabil`: `7771`
- `tragend_unruhig`: `2173`

Episodenzustaende:

- `field_carried`: `9991`
- `field_strained`: `3`

## Artefakte

- Debug: `debug\adapted_state_sideways_2024_5m_10k`
- Memory: `bot_memory\adapted_state_sideways_2024_5m_10k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
