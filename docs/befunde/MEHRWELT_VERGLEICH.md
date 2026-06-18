# Mehrwelt-Vergleich

Stand: 2026-06-18 17:13:32

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

### welt_2025_mid_shift_01

- Datenwelt: `data\kontrolliert_2025_mid_shift_test_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `923` -> `923`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `57`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.63049`
- MCM-Tragqualität Lauf 2: `0.359369`
- dominante Feldwirkung: `stabil` (`0.5131`)

Feldprofil:

- `diffus`: `11`
- `gespannt`: `32`
- `kippend`: `30`
- `rekoppelnd`: `1`
- `stabil`: `510`
- `tragend_unruhig`: `410`

### welt_2025_late_shift_01

- Datenwelt: `data\kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `923` -> `923`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `21`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.633998`
- MCM-Tragqualität Lauf 2: `0.361895`
- dominante Feldwirkung: `stabil` (`0.5473`)

Feldprofil:

- `diffus`: `8`
- `gespannt`: `14`
- `kippend`: `23`
- `stabil`: `544`
- `tragend_unruhig`: `405`

### welt_2023_stress_01

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- Kerzen: `1000`
- Unique Syntax: `972` -> `972`
- Episoden: `994` -> `994`
- Episodenmemory Lauf 2: `107`
- Top-Syntax-Reproduktion: `1.0`
- Top-Familien-Reproduktion: `1.0`
- MCM-Rekopplung Lauf 2: `0.614985`
- MCM-Tragqualität Lauf 2: `0.346134`
- dominante Feldwirkung: `tragend_unruhig` (`0.4386`)

Feldprofil:

- `diffus`: `19`
- `gespannt`: `89`
- `kippend`: `102`
- `stabil`: `348`
- `tragend_unruhig`: `436`

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

### welt_2023_01 gegen welt_2025_mid_shift_01

- Feldprofil-Ähnlichkeit: `0.9326`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `0.007468`
- Tragqualitätsdelta: `0.00633`

### welt_2023_01 gegen welt_2025_late_shift_01

- Feldprofil-Ähnlichkeit: `0.9044`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `0.010976`
- Tragqualitätsdelta: `0.008856`

### welt_2023_01 gegen welt_2023_stress_01

- Feldprofil-Ähnlichkeit: `0.8813`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> tragend_unruhig`
- Rekopplungsdelta: `-0.008037`
- Tragqualitätsdelta: `-0.006905`

### welt_2024_01 gegen welt_2025_core_01

- Feldprofil-Ähnlichkeit: `0.8581`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `tragend_unruhig -> stabil`
- Rekopplungsdelta: `0.011588`
- Tragqualitätsdelta: `0.003178`

### welt_2024_01 gegen welt_2025_mid_shift_01

- Feldprofil-Ähnlichkeit: `0.8893`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `tragend_unruhig -> stabil`
- Rekopplungsdelta: `0.008193`
- Tragqualitätsdelta: `0.001278`

### welt_2024_01 gegen welt_2025_late_shift_01

- Feldprofil-Ähnlichkeit: `0.8551`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `tragend_unruhig -> stabil`
- Rekopplungsdelta: `0.011701`
- Tragqualitätsdelta: `0.003804`

### welt_2024_01 gegen welt_2023_stress_01

- Feldprofil-Ähnlichkeit: `0.9286`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `tragend_unruhig -> tragend_unruhig`
- Rekopplungsdelta: `-0.007312`
- Tragqualitätsdelta: `-0.011957`

### welt_2025_core_01 gegen welt_2025_mid_shift_01

- Feldprofil-Ähnlichkeit: `0.9618`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `-0.003395`
- Tragqualitätsdelta: `-0.0019`

### welt_2025_core_01 gegen welt_2025_late_shift_01

- Feldprofil-Ähnlichkeit: `0.9879`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `0.000113`
- Tragqualitätsdelta: `0.000626`

### welt_2025_core_01 gegen welt_2023_stress_01

- Feldprofil-Ähnlichkeit: `0.8058`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> tragend_unruhig`
- Rekopplungsdelta: `-0.0189`
- Tragqualitätsdelta: `-0.015135`

### welt_2025_mid_shift_01 gegen welt_2025_late_shift_01

- Feldprofil-Ähnlichkeit: `0.9658`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> stabil`
- Rekopplungsdelta: `0.003508`
- Tragqualitätsdelta: `0.002526`

### welt_2025_mid_shift_01 gegen welt_2023_stress_01

- Feldprofil-Ähnlichkeit: `0.836`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> tragend_unruhig`
- Rekopplungsdelta: `-0.015505`
- Tragqualitätsdelta: `-0.013235`

### welt_2025_late_shift_01 gegen welt_2023_stress_01

- Feldprofil-Ähnlichkeit: `0.8028`
- Top-Syntax-Ähnlichkeit: `0.0`
- Top-Familien-Ähnlichkeit: `0.0`
- dominante Feldwirkung: `stabil -> tragend_unruhig`
- Rekopplungsdelta: `-0.019013`
- Tragqualitätsdelta: `-0.015761`

## Befund

Die sechs geprüften Welten zeigen eine hohe Reproduktion innerhalb der jeweiligen Welt, aber klare Verschiebungen zwischen den Welten. Das spricht dafür, dass MINI_DIO nicht wahllos speichert, sondern weltbezogene Innenfeldordnungen bildet.

Die drei 2025-Welten bilden feldseitig eine ruhige Nähegruppe. Sie teilen keine Top-Syntax und keine Top-Familien, bleiben im Feldprofil aber eng beieinander:

- 2025-Core gegen 2025-Mid-Shift: `0.9618`
- 2025-Core gegen 2025-Late-Shift: `0.9879`
- 2025-Mid-Shift gegen 2025-Late-Shift: `0.9658`

Der 2023-Stresslauf bildet den Gegenpol: niedrigere Rekopplung, niedrigere Tragqualität, mehr gespannte und kippende Wirkungen und deutlich mehr Episodenmemory. Das ist fachlich relevant, weil MINI_DIO hier nicht nur andere Wörter bildet, sondern eine andere Feldbelastung zeigt.

Damit entsteht eine klarere Arbeitsthese: Syntax ist stark weltbezogen, das Feldprofil kann aber weltübergreifende Nähegruppen bilden. MINI_DIO scheint also nicht nur einzelne Bedeutungsinseln zu reproduzieren, sondern auch größere Innenfeldklassen zu tragen.

Wichtig bleibt: Das ist passive Feldforschung. Der Bericht erzeugt keine Handlung, kein Gate und keine Strategie.

## Wie es weitergeht

Als nächstes sollten weitere Welten ergänzt werden. Entscheidend ist, ob sich ein stabiler Kern der Feldtopologie zeigt, während Bedeutungsinseln je nach Weltspannung entstehen, driften oder rekoppeln.
