# Aktueller Forschungslauf

Stand: 2026-06-18 19:10:47

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_stress_segment_2025_stress_5m_SOLUSDT.csv`
- Kerzen: `100`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `94` -> `94`
- Episoden: `94` -> `94`
- geschriebene Episodenmemory: `21` -> `21`
- MCM-Rekopplung: `0.594644` -> `0.594327`
- MCM-Tragqualitaet: `0.328918` -> `0.329181`
- Sinnes-MCM-Kopplung: `0.786712` -> `0.786433`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_04rp7vx, dio_054dhj0, dio_0gb0aog, dio_0gdyct8, dio_128jmxo, dio_1etbb1u, dio_1lum0qt, dio_1u121hs`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_04rp, dio_054d, dio_0gb0, dio_0gdy, dio_128j, dio_1etb, dio_1lum, dio_1u12`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `5`
- `gespannt`: `27`
- `kippend`: `9`
- `stabil`: `16`
- `tragend_unruhig`: `37`

Episodenzustaende:

- `field_carried`: `67`
- `field_strained`: `27`

## Artefakte

- Debug: `debug\research_chain_stress_segment_2025_stress_01`
- Memory: `memory\research_chain_stress_segment_2025_stress_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
