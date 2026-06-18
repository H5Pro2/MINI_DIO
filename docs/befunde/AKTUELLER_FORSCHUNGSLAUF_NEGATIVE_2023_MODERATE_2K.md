# Aktueller Forschungslauf

Stand: 2026-06-18 22:05:36

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_2000_5m_SOLUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1824` -> `1824`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `105` -> `105`
- MCM-Rekopplung: `0.629991` -> `0.62966`
- MCM-Tragqualitaet: `0.360177` -> `0.360479`
- Sinnes-MCM-Kopplung: `0.834751` -> `0.83445`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_01ufvm3, dio_05c8wrw, dio_0c3o0fd, dio_0chknce, dio_0f2wa5g, dio_0nv8zkr, dio_0wiayhe, dio_1doxjd2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_01uf, dio_05c8, dio_0c3o, dio_0chk, dio_0f2w, dio_0j34, dio_0nv8, dio_1dox`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `19`
- `gespannt`: `67`
- `kippend`: `75`
- `stabil`: `1067`
- `tragend_unruhig`: `766`

Episodenzustaende:

- `field_carried`: `1927`
- `field_strained`: `67`

## Artefakte

- Debug: `debug\research_chain_negative_2023_moderate_2k`
- Memory: `memory\research_chain_negative_2023_moderate_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
