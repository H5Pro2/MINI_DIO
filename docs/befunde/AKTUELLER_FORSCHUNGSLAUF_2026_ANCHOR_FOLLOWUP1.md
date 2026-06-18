# Aktueller Forschungslauf

Stand: 2026-06-18 17:57:22

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2026_anchor_followup1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `875` -> `875`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `47` -> `47`
- MCM-Rekopplung: `0.636847` -> `0.636513`
- MCM-Tragqualitaet: `0.365862` -> `0.366169`
- Sinnes-MCM-Kopplung: `0.836783` -> `0.83648`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00pss5g, dio_08mmra5, dio_0enba31, dio_0f10dj6, dio_0gk9pyh, dio_1a4a9da, dio_1tg921i, dio_1us7tte`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ps, dio_08mm, dio_0enb, dio_0f10, dio_0gk9, dio_1a4a, dio_1tg9, dio_1us7`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `7`
- `gespannt`: `25`
- `kippend`: `14`
- `stabil`: `562`
- `tragend_unruhig`: `386`

Episodenzustaende:

- `field_carried`: `969`
- `field_strained`: `25`

## Artefakte

- Debug: `debug\research_chain_2026_anchor_followup1_01`
- Memory: `memory\research_chain_2026_anchor_followup1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
