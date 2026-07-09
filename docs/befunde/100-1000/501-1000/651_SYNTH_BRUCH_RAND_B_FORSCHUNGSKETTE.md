# Aktueller Forschungslauf

Stand: 2026-06-22 10:17:36

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_bruch_rand_b_5m.csv`
- Kerzen: `6000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `166` -> `166`
- Episoden: `5994` -> `5994`
- geschriebene Episodenmemory: `8` -> `8`
- MCM-Rekopplung: `0.745792` -> `0.74568`
- MCM-Tragqualitaet: `0.597622` -> `0.597741`
- Sinnes-MCM-Kopplung: `0.904611` -> `0.904501`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `3`
- `kippend`: `1`
- `stabil`: `5732`
- `tragend_unruhig`: `258`

Episodenzustaende:

- `field_carried`: `5991`
- `field_strained`: `3`

## Artefakte

- Debug: `debug\synthetic_mcm_bruch_rand_b_5m`
- Memory: `memory\synthetic_mcm_bruch_rand_b_5m_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
