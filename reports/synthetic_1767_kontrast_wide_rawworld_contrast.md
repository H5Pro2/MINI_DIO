# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:21:07

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 9 | 1.0000 | 0.0000 | 0.0000 | 0.748524 | 0.748524 | 0.0000 | 0.7414 | 3.1062 | 2.5299 | -0.5763 | 0.625110 | 0.399691 | 0.005508 | 0.004045 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1767_A_1000_2500 | SYN1767_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.747952 | 0.7353 | 3.1181 | 2.9513 | -0.1668 |
| SYN1767_A_2000_3500 | SYN1767_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.749648 | 0.7450 | 2.9513 | 1.6562 | -1.2951 |
| SYN1767_A_1000_3000 | SYN1767_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.748994 | 0.7542 | 3.1497 | 2.4356 | -0.7141 |
| SYN1767_B_1000_2500 | SYN1767_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.747550 | 0.7273 | 3.1456 | 3.1236 | -0.0221 |
| SYN1767_B_2000_3500 | SYN1767_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.747914 | 0.7278 | 3.1236 | 2.6549 | -0.4686 |
| SYN1767_B_1000_3000 | SYN1767_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.748684 | 0.7558 | 3.1683 | 2.8055 | -0.3628 |
| SYN1767_C_1000_2500 | SYN1767_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.747997 | 0.7356 | 3.1243 | 2.9865 | -0.1379 |
| SYN1767_C_2000_3500 | SYN1767_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.749272 | 0.7397 | 2.9865 | 1.6503 | -1.3362 |
| SYN1767_C_1000_3000 | SYN1767_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.748705 | 0.7523 | 3.1887 | 2.5054 | -0.6833 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
