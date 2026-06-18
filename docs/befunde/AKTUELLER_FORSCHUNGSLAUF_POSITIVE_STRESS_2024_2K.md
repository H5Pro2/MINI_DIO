# Aktueller Forschungslauf

Stand: 2026-06-18 22:15:42

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1775` -> `1775`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `79` -> `79`
- MCM-Rekopplung: `0.631567` -> `0.631225`
- MCM-Tragqualitaet: `0.362323` -> `0.362635`
- Sinnes-MCM-Kopplung: `0.836539` -> `0.836229`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_02wrx00, dio_0bhk095, dio_0hzwx83, dio_0k5ft3o, dio_0l7vivy, dio_0qkxqdx, dio_1aa3owj, dio_1jnclbr`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_02wr, dio_0bhk, dio_0hzw, dio_0k5f, dio_0qkx, dio_0tyr, dio_1aa3, dio_1jnc`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `21`
- `gespannt`: `47`
- `kippend`: `83`
- `rekoppelnd`: `1`
- `stabil`: `1044`
- `tragend_unruhig`: `798`

Episodenzustaende:

- `field_carried`: `1946`
- `field_strained`: `48`

## Artefakte

- Debug: `debug\research_chain_positive_stress_2024_2k`
- Memory: `memory\research_chain_positive_stress_2024_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
