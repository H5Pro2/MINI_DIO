# Aktueller Forschungslauf

Stand: 2026-06-18 18:22:43

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_auto_stress_segment5_6_5m_SOLUSDT.csv`
- Kerzen: `198`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `191` -> `191`
- Episoden: `192` -> `192`
- geschriebene Episodenmemory: `45` -> `45`
- MCM-Rekopplung: `0.60653` -> `0.606201`
- MCM-Tragqualitaet: `0.34475` -> `0.345029`
- Sinnes-MCM-Kopplung: `0.808968` -> `0.808677`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_003yryj, dio_07ukkoj, dio_0f10dj6, dio_0gm9pvb, dio_0nuq766, dio_0p0s7cd, dio_1ebpxut, dio_1f86qhd`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_003y, dio_07uk, dio_0eu7, dio_0f10, dio_0gm9, dio_0nuq, dio_0p0s, dio_1f86`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `4`
- `gespannt`: `33`
- `kippend`: `26`
- `stabil`: `47`
- `tragend_unruhig`: `82`

Episodenzustaende:

- `field_carried`: `159`
- `field_strained`: `33`

## Artefakte

- Debug: `debug\research_chain_auto_stress_segment5_6_01`
- Memory: `memory\research_chain_auto_stress_segment5_6_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
