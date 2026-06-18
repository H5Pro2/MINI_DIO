# Aktueller Forschungslauf

Stand: 2026-06-18 22:53:05

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2024_15m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1720` -> `1720`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `107` -> `105`
- MCM-Rekopplung: `0.631538` -> `0.631196`
- MCM-Tragqualitaet: `0.362053` -> `0.362364`
- Sinnes-MCM-Kopplung: `0.835175` -> `0.834866`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_03t5leb, dio_08mmra5, dio_0wa7wjp, dio_1clyymx, dio_1fhx1gw, dio_1q022yy, dio_1rsllrx, dio_1x999tg`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_03t5, dio_08mm, dio_0j9a, dio_1cly, dio_1fhx, dio_1q02, dio_1rsl, dio_1x99`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `15`
- `gespannt`: `83`
- `kippend`: `93`
- `stabil`: `1011`
- `tragend_unruhig`: `792`

Episodenzustaende:

- `field_carried`: `1911`
- `field_strained`: `83`

## Artefakte

- Debug: `debug\research_chain_btc_2024_15m_2k`
- Memory: `memory\research_chain_btc_2024_15m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
