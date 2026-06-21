# Aktueller Forschungslauf

Stand: 2026-06-21 21:04:06

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `361` -> `361`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `11` -> `11`
- MCM-Rekopplung: `0.692872` -> `0.692134`
- MCM-Tragqualitaet: `0.50748` -> `0.508206`
- Sinnes-MCM-Kopplung: `0.84372` -> `0.843028`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00jaski, dio_00lyjkf, dio_0h9h06p, dio_0m9zys3, dio_104t4us, dio_155c3g6, dio_1ewh8ej, dio_1pij39c`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00ja, dio_00ly, dio_0h9h, dio_0m9z, dio_104t, dio_155c, dio_1ewh, dio_1pij`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `gespannt`: `5`
- `kippend`: `22`
- `stabil`: `1636`
- `tragend_unruhig`: `331`

Episodenzustaende:

- `field_carried`: `1989`
- `field_strained`: `5`

## Artefakte

- Debug: `debug\independent_btc2025_5m_2k`
- Memory: `memory\independent_btc2025_5m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
