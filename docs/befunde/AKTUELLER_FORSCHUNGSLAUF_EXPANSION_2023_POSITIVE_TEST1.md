# Aktueller Forschungslauf

Stand: 2026-06-18 20:59:31

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `913` -> `913`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `41` -> `41`
- MCM-Rekopplung: `0.633879` -> `0.633577`
- MCM-Tragqualitaet: `0.357669` -> `0.357946`
- Sinnes-MCM-Kopplung: `0.839744` -> `0.839469`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02o7820, dio_03be7u1, dio_0epwh5e, dio_0nv8zkr, dio_0t4ynqc, dio_0tbo7fb, dio_0wbqgju, dio_1bbzssw`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02o7, dio_03be, dio_0epw, dio_0nv8, dio_0rkf, dio_0t4y, dio_0wbq, dio_1bbz`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `5`
- `gespannt`: `22`
- `kippend`: `18`
- `stabil`: `565`
- `tragend_unruhig`: `384`

Episodenzustaende:

- `field_carried`: `972`
- `field_strained`: `22`

## Artefakte

- Debug: `debug\research_chain_expansion_2023_positive_test1`
- Memory: `memory\research_chain_expansion_2023_positive_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
