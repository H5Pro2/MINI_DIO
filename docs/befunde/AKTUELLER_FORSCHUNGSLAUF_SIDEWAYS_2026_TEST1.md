# Aktueller Forschungslauf

Stand: 2026-06-18 21:46:56

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `973` -> `973`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `117` -> `117`
- MCM-Rekopplung: `0.615539` -> `0.615214`
- MCM-Tragqualitaet: `0.351681` -> `0.351964`
- Sinnes-MCM-Kopplung: `0.819008` -> `0.818717`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_07y1h7q, dio_0feua68, dio_0fiqo2u, dio_0n481ri, dio_0qog7ei, dio_0sz7fmr, dio_0u9308n, dio_1ter11d`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_07y1, dio_0feu, dio_0fiq, dio_0n48, dio_0qog, dio_0sz7, dio_1n1b, dio_1q1o`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `24`
- `gespannt`: `84`
- `kippend`: `108`
- `rekoppelnd`: `2`
- `stabil`: `317`
- `tragend_unruhig`: `459`

Episodenzustaende:

- `field_carried`: `908`
- `field_strained`: `86`

## Artefakte

- Debug: `debug\research_chain_sideways_2026_test1`
- Memory: `memory\research_chain_sideways_2026_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
