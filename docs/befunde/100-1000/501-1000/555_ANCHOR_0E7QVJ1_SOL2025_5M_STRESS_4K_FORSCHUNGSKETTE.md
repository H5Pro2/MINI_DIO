# Aktueller Forschungslauf

Stand: 2026-06-21 21:12:57

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_long_sol_2025_5m_stress_4000.csv`
- Kerzen: `4000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `478` -> `478`
- Episoden: `3994` -> `3994`
- geschriebene Episodenmemory: `21` -> `21`
- MCM-Rekopplung: `0.699048` -> `0.698428`
- MCM-Tragqualitaet: `0.522253` -> `0.522866`
- Sinnes-MCM-Kopplung: `0.844451` -> `0.843867`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `10`
- `kippend`: `44`
- `stabil`: `3281`
- `tragend_unruhig`: `659`

Episodenzustaende:

- `field_carried`: `3984`
- `field_strained`: `10`

## Artefakte

- Debug: `debug\anchor_0e7qvj1_sol2025_5m_stress_4k`
- Memory: `memory\anchor_0e7qvj1_sol2025_5m_stress_4k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
