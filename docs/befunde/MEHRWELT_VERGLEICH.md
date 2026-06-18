# Mehrwelt-Vergleich

Stand: 2026-06-18 16:54:23

## Zweck

Dieser Bericht vergleicht mehrere passive MINI_DIO-Forschungsketten.
Er prüft, ob Reproduktion nur innerhalb einer Welt stabil ist oder ob über verschiedene Welten neue Bedeutungsräume, Drift oder stabile Feldrollen sichtbar werden.

## Einzelwelten

### welt_2023_01

- Datenwelt: `data\kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `947` -> `947`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `87`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.623022`
- MCM-Tragqualität Lauf 2: `0.353039`
- dominante Feldwirkung: `stabil` (`0.4688`)

Feldprofil:

- `diffus`: `11`
- `gespannt`: `60`
- `kippend`: `69`
- `stabil`: `466`
- `tragend_unruhig`: `388`

### welt_2024_01

- Datenwelt: `data\kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `967` -> `967`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `81`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.622297`
- MCM-Tragqualität Lauf 2: `0.358091`
- dominante Feldwirkung: `tragend_unruhig` (`0.4557`)

Feldprofil:

- `diffus`: `11`
- `gespannt`: `60`
- `kippend`: `68`
- `rekoppelnd`: `2`
- `stabil`: `400`
- `tragend_unruhig`: `453`

### welt_2025_core_01

- Datenwelt: `data\kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `923` -> `923`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `25`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.633885`
- MCM-Tragqualität Lauf 2: `0.361269`
- dominante Feldwirkung: `stabil` (`0.5443`)

Feldprofil:

- `diffus`: `7`
- `gespannt`: `12`
- `kippend`: `17`
- `stabil`: `541`
- `tragend_unruhig`: `417`

## Weltvergleich

### welt_2023_01 gegen welt_2024_01

- Feldprofil-Ähnlichkeit: `0.9326`
- Top-Syntax-Ähnlichkeit: `0.0667`
- Top-Familien-Ähnlichkeit: `0.0667`
- dominante Feldwirkung: `stabil -> tragend_unruhig`
- Rekopplungsdelta: `-0.000725`
- Tragqualitätsdelta: `0.005052`

### welt_2023_01 gegen welt_2025_core_01

- Feldprofil-Ähnlichkeit: `0.8954`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `0.010863`
- Tragqualitätsdelta: `0.00823`

### welt_2024_01 gegen welt_2025_core_01

- Feldprofil-Ähnlichkeit: `0.8581`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `tragend_unruhig -> stabil`
- Rekopplungsdelta: `0.011588`
- Tragqualitätsdelta: `0.003178`

## Befund

Die drei geprüften Welten zeigen eine hohe Reproduktion innerhalb der jeweiligen Welt, aber klare Verschiebungen zwischen den Welten. Das spricht dafür, dass MINI_DIO nicht wahllos speichert, sondern weltbezogene Innenfeldordnungen bildet.

Die 2025-Core-Welt fällt dabei als ruhigerer Feldraum auf: weniger gespannte und kippende Wirkungen, höhere Rekopplung und eine deutlich stärkere stabile Dominanz. Das ist kein Beweis für eine universelle Topologie, aber ein relevanter Hinweis auf feldbezogene Anpassung an unterschiedliche Weltspannungen.

Wichtig bleibt: Das ist passive Feldforschung. Der Bericht erzeugt keine Handlung, kein Gate und keine Strategie.

## Wie es weitergeht

Als nächstes sollten weitere Welten ergänzt werden. Entscheidend ist, ob sich ein stabiler Kern der Feldtopologie zeigt, während Bedeutungsinseln je nach Weltspannung entstehen, driften oder rekoppeln.
