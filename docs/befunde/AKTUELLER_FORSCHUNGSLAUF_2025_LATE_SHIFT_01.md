# Aktueller Forschungslauf

Stand: 2026-06-18 17:13:18

## Zweck

Dieser Lauf prueft die kleine MINI_DIO-Forschungskette:

- gleicher Datensatz,
- gleiche Memory zwischen Lauf 1 und Lauf 2,
- passive Beobachtung ohne Entry, Gate oder Motorik,
- Vergleich von Innenfeld, Syntax und Episodenbildung.

## Ergebnis

- Datenwelt: `data\kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Trades: `0` -> `0`
- Unique Syntaxsymbole: `923` -> `923`
- Episoden: `994` -> `994`
- geschriebene Episodenmemory: `21` -> `21`
- MCM-Rekopplung: `0.63431` -> `0.633998`
- MCM-Tragqualitaet: `0.36161` -> `0.361895`
- Sinnes-MCM-Kopplung: `0.842286` -> `0.842004`

## Reproduktionsnaehe

- Top-Syntax-Ueberlappung: `1.0`
- gemeinsame Top-Syntax: `dio_0chknce, dio_0jtlv4q, dio_0ml9pby, dio_0niklu5, dio_11bpacy, dio_13tnvon, dio_17shqdn, dio_1esirfb`
- Top-Familien-Ueberlappung: `1.0`
- gemeinsame Top-Familien: `dio_0chk, dio_0ml9, dio_0nik, dio_0srq, dio_11bp, dio_13tn, dio_17sh, dio_1esi`

## Innenfeld

Passive MCM-Wirkungsklassen:

- `diffus`: `8`
- `gespannt`: `14`
- `kippend`: `23`
- `stabil`: `544`
- `tragend_unruhig`: `405`

Episodenzustaende:

- `field_carried`: `980`
- `field_strained`: `14`

## Artefakte

- Debug: `debug\research_chain_2025_late_shift_01`
- Memory: `memory\research_chain_2025_late_shift_01.json`

## Wie es weitergeht

Als naechstes sollte dieser Lauf mit den anderen 2025-Welten verglichen werden. Entscheidend ist, ob trotz anderer Syntax eine gemeinsame ruhige Feldnaehe sichtbar bleibt.
