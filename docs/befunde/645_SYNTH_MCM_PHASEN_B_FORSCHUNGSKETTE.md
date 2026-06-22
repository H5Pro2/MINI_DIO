# Aktueller Forschungslauf

Stand: 2026-06-22 10:09:56

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_phasen_b_5m.csv`
- Kerzen: `5400`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `42` -> `42`
- Episoden: `5394` -> `5394`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.756718` -> `0.75677`
- MCM-Tragqualitaet: `0.617037` -> `0.617003`
- Sinnes-MCM-Kopplung: `0.916763` -> `0.916804`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0g3bu28, dio_0gfmxqu, dio_0n0i1kn, dio_13o0i6x, dio_13s036n, dio_1fllaqz, dio_1le1nvy, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0g3b, dio_0gfm, dio_0n0i, dio_13o0, dio_13s0, dio_1fll, dio_1le1, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `1`
- `stabil`: `5389`
- `tragend_unruhig`: `4`

Episodenzustaende:

- `field_carried`: `5394`

## Artefakte

- Debug: `debug\synthetic_mcm_phasen_b_5m`
- Memory: `memory\synthetic_mcm_phasen_b_5m_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
