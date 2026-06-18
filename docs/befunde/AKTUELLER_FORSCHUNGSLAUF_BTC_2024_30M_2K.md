# Aktueller Forschungslauf

Stand: 2026-06-18 22:55:46

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2024_30m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1808` -> `1808`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `179` -> `179`
- MCM-Rekopplung: `0.626473` -> `0.626156`
- MCM-Tragqualitaet: `0.359087` -> `0.359372`
- Sinnes-MCM-Kopplung: `0.831779` -> `0.831493`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_01zvlp5, dio_02thfip, dio_0chknce, dio_0mgdi48, dio_0t5d11f, dio_1g35sz0, dio_1ne0pgm, dio_1v8ev4a`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_01zv, dio_02th, dio_0chk, dio_0mgd, dio_0t5d, dio_1g35, dio_1ne0, dio_1v8e`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `29`
- `gespannt`: `125`
- `kippend`: `123`
- `rekoppelnd`: `4`
- `stabil`: `928`
- `tragend_unruhig`: `785`

Episodenzustaende:

- `field_carried`: `1865`
- `field_strained`: `129`

## Artefakte

- Debug: `debug\research_chain_btc_2024_30m_2k`
- Memory: `memory\research_chain_btc_2024_30m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
