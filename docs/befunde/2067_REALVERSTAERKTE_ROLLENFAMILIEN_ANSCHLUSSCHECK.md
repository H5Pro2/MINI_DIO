# 2067 - Anschlusscheck realverstärkter Rollenfamilien

## Zweck

Diese Auswertung prüft, ob die Rollenfamilien aus 2066 direkt gegen eine ältere Folgeweltbasis gelesen werden dürfen.

Der Test verhindert eine methodische Vermischung: Wenn die Symbolfamilien in der Vergleichsbasis kaum vorkommen, darf daraus keine starke Aussage über Stabilität oder Drift abgeleitet werden.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keinen motorischen Impuls.

## Übersicht

- Vergleichsbasis: `docs\befunde\1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv`
- geprüfte 2066-Mitglieder: `29`
- in der Vergleichsbasis gefunden: `6`
- Statusverteilung: `{'anschluss_fehlend': 5, 'anschluss_genuegend': 2, 'anschluss_teilweise': 1}`

## Rollenfamilien

| role_family | members | found_members | missing_members | overlap_ratio | source_overlap_status | found_symbols |
| --- | --- | --- | --- | --- | --- | --- |
| rf_05 | 8 | 2 | 6 | 0.250000 | anschluss_teilweise | dio_0fe7;dio_1xrt |
| rf_06 | 8 | 0 | 8 | 0.000000 | anschluss_fehlend | - |
| rf_13 | 3 | 0 | 3 | 0.000000 | anschluss_fehlend | - |
| rf_07 | 2 | 2 | 0 | 1.000000 | anschluss_genuegend | dio_0g2r;dio_1ewh |
| rf_21 | 2 | 2 | 0 | 1.000000 | anschluss_genuegend | dio_1pij;dio_1v2w |
| rf_08 | 2 | 0 | 2 | 0.000000 | anschluss_fehlend | - |
| rf_10 | 2 | 0 | 2 | 0.000000 | anschluss_fehlend | - |
| rf_17 | 2 | 0 | 2 | 0.000000 | anschluss_fehlend | - |

## Lesung

Die vorhandene ältere Folgeweltbasis ist nur eingeschränkt anschlussfähig für die 2066-Familien.

Das ist kein negativer Befund gegen die Rollenfamilien. Es bedeutet methodisch nur: Für eine saubere Familien-Stabilitätsprüfung brauchen wir Folgewelten, die auf derselben Symbolbasis erzeugt oder ausdrücklich daran rückgelesen werden.

## Grenze

Dieser Report bewertet nicht die Qualität der Familien. Er bewertet nur, ob eine Vergleichsbasis ausreichend überlappt.

Wie es weitergeht: Als nächstes sollten neue Folgeweltläufe mit derselben 2066-Symbolbasis erzeugt oder ein Rückleser gebaut werden, der die 2066-Familien explizit in vorhandenen Weltfenstern sucht.
