# Aktueller Forschungslauf

Stand: 2026-06-18 17:13:20

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `972` -> `972`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `107` -> `107`
- MCM-Rekopplung: `0.615284` -> `0.614985`
- MCM-Tragqualitaet: `0.345875` -> `0.346134`
- Sinnes-MCM-Kopplung: `0.820898` -> `0.820632`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0qb31rn, dio_0ssnx5h, dio_14ai6ie, dio_1hh75e1, dio_1njwjyw, dio_1tlc5jt, dio_1uy8mtr, dio_1ybz8e6`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0qb3, dio_0ssn, dio_0tlm, dio_14ai, dio_1njw, dio_1tlc, dio_1uy8, dio_1ybz`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `19`
- `gespannt`: `89`
- `kippend`: `102`
- `stabil`: `348`
- `tragend_unruhig`: `436`

Episodenzustaende:

- `field_carried`: `905`
- `field_strained`: `89`

## Artefakte

- Debug: `debug\research_chain_2023_stress_01`
- Memory: `memory\research_chain_2023_stress_01.json`

## Wie es weitergeht

Als naechstes sollte dieser Stresslauf als Gegenpol zu den ruhigeren 2025-Welten gelesen werden. Entscheidend ist, welche Feldmerkmale unter hoher Spannung kippen und welche trotzdem reproduzierbar bleiben.
