# Aktueller Forschungslauf

Stand: 2026-06-22 11:03:28

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `350` -> `350`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `1` -> `1`
- MCM-Rekopplung: `0.693993` -> `0.693192`
- MCM-Tragqualitaet: `0.50987` -> `0.510659`
- Sinnes-MCM-Kopplung: `0.840392` -> `0.83964`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0l7pvdk, dio_0m9zys3, dio_104t4us, dio_14wjmk5, dio_155c3g6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0l7p, dio_0m9z, dio_104t, dio_14wj, dio_155c`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `kippend`: `17`
- `stabil`: `1552`
- `tragend_unruhig`: `425`

Episodenzustaende:

- `field_carried`: `1994`

## Artefakte

- Debug: `debug\adapted_field_kas_2024_5m_2k`
- Memory: `bot_memory\adapted_field_kas_2024_5m_2k.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
