# Aktueller Forschungslauf

Stand: 2026-06-22 11:07:01

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_phasen_a_5m.csv`
- Kerzen: `5400`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `44` -> `44`
- Episoden: `5394` -> `5394`
- geschriebene Episodenmemory: `3` -> `3`
- MCM-Rekopplung: `0.756945` -> `0.756997`
- MCM-Tragqualitaet: `0.617331` -> `0.617297`
- Sinnes-MCM-Kopplung: `0.916861` -> `0.916901`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0g3bu28, dio_0gfmxqu, dio_0n0i1kn, dio_13o0i6x, dio_13s036n, dio_1fllaqz, dio_1le1nvy, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0g3b, dio_0gfm, dio_0n0i, dio_13o0, dio_13s0, dio_1fll, dio_1le1, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `1`
- `stabil`: `5390`
- `tragend_unruhig`: `3`

Episodenzustaende:

- `field_carried`: `5394`

## Artefakte

- Debug: `debug\adapted_synth_harmonie_a`
- Memory: `bot_memory\adapted_synth_harmonie_a.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
