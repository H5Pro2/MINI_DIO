# Aktueller Forschungslauf

Stand: 2026-06-18 22:55:48

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_btc_2025_30m_test1_2000_BTCUSDT.csv`
- Kerzen: `2000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `1855` -> `1855`
- Episoden: `1994` -> `1994`
- geschriebene Episodenmemory: `169` -> `167`
- MCM-Rekopplung: `0.623403` -> `0.623087`
- MCM-Tragqualitaet: `0.3551` -> `0.355382`
- Sinnes-MCM-Kopplung: `0.828549` -> `0.828265`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_00fvyh6, dio_01d68ps, dio_0nmiyar, dio_0sf3qm1, dio_14n0zjd, dio_1a1178d, dio_1j8u3sd, dio_1vhwfiv`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_00fv, dio_01d6, dio_0nmi, dio_0sf3, dio_14n0, dio_1a11, dio_1j8u, dio_1vhw`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `32`
- `gespannt`: `131`
- `kippend`: `144`
- `rekoppelnd`: `1`
- `stabil`: `845`
- `tragend_unruhig`: `841`

Episodenzustaende:

- `field_carried`: `1862`
- `field_strained`: `132`

## Artefakte

- Debug: `debug\research_chain_btc_2025_30m_2k`
- Memory: `memory\research_chain_btc_2025_30m_2k_memory.json`

## Wie es weitergeht

Als naechstes sollte dieselbe Kette mit einer zweiten kontrollierten Welt laufen. Dabei wird geprueft, ob dieselben Familien stabil bleiben, ob neue Inseln entstehen oder ob vorhandene Bedeutungen driften.
