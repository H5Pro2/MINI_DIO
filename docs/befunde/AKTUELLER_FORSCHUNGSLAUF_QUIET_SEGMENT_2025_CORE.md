# Aktueller Forschungslauf

Stand: 2026-06-18 18:25:45

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_quiet_segment_2025_core_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `93` -> `93`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.628666` -> `0.628376`
- MCM-Tragqualitaet: `0.345008` -> `0.345272`
- Sinnes-MCM-Kopplung: `0.831457` -> `0.831195`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0mpbteu, dio_0o4vfuj, dio_0p9tw3g, dio_16829ds, dio_17jjxav, dio_19xhwhh, dio_1lp1roa, dio_1x999tg`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0mpb, dio_0o4v, dio_0p9t, dio_1682, dio_17jj, dio_19xh, dio_1lp1, dio_1x99`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `1`
- `gespannt`: `1`
- `kippend`: `1`
- `stabil`: `45`
- `tragend_unruhig`: `46`

Episodenzustaende:

- `field_carried`: `93`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\research_chain_quiet_segment_2025_core_01`
- Memory: `memory\research_chain_quiet_segment_2025_core_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
