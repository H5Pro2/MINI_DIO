# Aktueller Forschungslauf

Stand: 2026-06-18 18:22:41

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_auto_stress_segment6_5m_SOLUSDT.csv`
- Kerzen: `99`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `93` -> `93`
- Episoden: `93` -> `93`
- geschriebene Episodenmemory: `23` -> `23`
- MCM-Rekopplung: `0.606725` -> `0.606419`
- MCM-Tragqualitaet: `0.338745` -> `0.339007`
- Sinnes-MCM-Kopplung: `0.809931` -> `0.809659`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0buzx9p, dio_0m86ps7, dio_0otpfv7, dio_0qg4xkv, dio_1jug49c, dio_1k0x3xu, dio_1lkcgwc, dio_1wmvc0p`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0buz, dio_0m86, dio_0otp, dio_0qg4, dio_1jug, dio_1k0x, dio_1lkc, dio_1wmv`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `2`
- `gespannt`: `12`
- `kippend`: `12`
- `stabil`: `21`
- `tragend_unruhig`: `46`

Episodenzustaende:

- `field_carried`: `81`
- `field_strained`: `12`

## Artefakte

- Debug: `debug\research_chain_auto_stress_segment6_01`
- Memory: `memory\research_chain_auto_stress_segment6_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
