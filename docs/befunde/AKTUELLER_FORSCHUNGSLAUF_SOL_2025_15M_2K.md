# Aktueller Forschungslauf

Stand: 2026-06-18 23:11:05

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_sol_2025_15m_test1_2000_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1895` -> `1895`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `247` -> `247`
- MCM-Rekopplung: `0.615843` -> `0.615512`
- MCM-Tragqualitaet: `0.351247` -> `0.351537`
- Sinnes-MCM-Kopplung: `0.818004` -> `0.817708`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03u57ii, dio_05oth2z, dio_078axxd, dio_0bqhlnm, dio_0csjbaq, dio_0f2wa5g, dio_0uy5dey, dio_1vhwfiv`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03u5, dio_05ot, dio_078a, dio_0bqh, dio_0f2w, dio_0st3, dio_0uy5, dio_1ywz`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `36`
- `gespannt`: `218`
- `kippend`: `202`
- `stabil`: `676`
- `tragend_unruhig`: `862`

Episodenzustaende:

- `field_carried`: `1776`
- `field_strained`: `218`

## Artefakte

- Debug: `debug\research_chain_sol_2025_15m_2k`
- Memory: `memory\research_chain_sol_2025_15m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
