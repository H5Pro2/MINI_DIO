# Aktueller Forschungslauf

Stand: 2026-06-22 22:02:44

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_synthetic_mcm_sequenz_bruch_rand_zufallsnah_5m.csv`
- Kerzen: `5800`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `167` -> `167`
- Episoden: `5794` -> `5794`
- geschriebene Episodenmemory: `4` -> `4`
- MCM-Rekopplung: `0.745666` -> `0.745524`
- MCM-Tragqualitaet: `0.597229` -> `0.59737`
- Sinnes-MCM-Kopplung: `0.903948` -> `0.903814`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_06er2zu, dio_0g3bu28, dio_0n0i1kn, dio_0pz659c, dio_13o0i6x, dio_1492fc4, dio_1fllaqz, dio_1ygxff2`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_06er, dio_0g3b, dio_0n0i, dio_0pz6, dio_13o0, dio_1492, dio_1fll, dio_1ygx`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `1`
- `kippend`: `5`
- `stabil`: `5514`
- `tragend_unruhig`: `274`

Episodenzustaende:

- `field_carried`: `5793`
- `field_strained`: `1`

## Artefakte

- Debug: `debug\adapted_synth_sequenz_bruch_rand_zufallsnah`
- Memory: `bot_memory\adapted_synth_sequenz_bruch_rand_zufallsnah.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
