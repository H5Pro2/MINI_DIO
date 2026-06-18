# Aktueller Forschungslauf

Stand: 2026-06-18 18:09:21

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_auto_stress_extreme_expansion_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `966` -> `966`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `103` -> `103`
- MCM-Rekopplung: `0.618778` -> `0.618465`
- MCM-Tragqualitaet: `0.350394` -> `0.350669`
- Sinnes-MCM-Kopplung: `0.825315` -> `0.825036`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00bcwq3, dio_0fvh3f6, dio_0xnnhq1, dio_0ywtu20, dio_1h70o6u, dio_1mviffh, dio_1r94suh, dio_1tfp0vk`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00bc, dio_0fvh, dio_0ov5, dio_0xnn, dio_1h70, dio_1mvi, dio_1r94, dio_1tfp`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `16`
- `gespannt`: `78`
- `kippend`: `80`
- `stabil`: `405`
- `tragend_unruhig`: `415`

Episodenzustaende:

- `field_carried`: `916`
- `field_strained`: `78`

## Artefakte

- Debug: `debug\research_chain_auto_stress_extreme_expansion_test1_01`
- Memory: `memory\research_chain_auto_stress_extreme_expansion_test1_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
