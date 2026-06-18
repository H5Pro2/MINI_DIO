# Aktueller Forschungslauf

Stand: 2026-06-18 18:22:41

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_auto_stress_segment5_5m_SOLUSDT.csv`
- Kerzen: `99`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `93` -> `93`
- Episoden: `93` -> `93`
- geschriebene Episodenmemory: `21` -> `21`
- MCM-Rekopplung: `0.607432` -> `0.607085`
- MCM-Tragqualitaet: `0.351637` -> `0.351929`
- Sinnes-MCM-Kopplung: `0.809667` -> `0.80936`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_003yryj, dio_07ukkoj, dio_0f10dj6, dio_0gm9pvb, dio_0nuq766, dio_1ebpxut, dio_1f86qhd, dio_1ojh5ma`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_003y, dio_07uk, dio_0f10, dio_0gm9, dio_0nuq, dio_1ebp, dio_1f86, dio_1ojh`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `1`
- `gespannt`: `20`
- `kippend`: `13`
- `stabil`: `26`
- `tragend_unruhig`: `33`

Episodenzustaende:

- `field_carried`: `73`
- `field_strained`: `20`

## Artefakte

- Debug: `debug\research_chain_auto_stress_segment5_01`
- Memory: `memory\research_chain_auto_stress_segment5_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
