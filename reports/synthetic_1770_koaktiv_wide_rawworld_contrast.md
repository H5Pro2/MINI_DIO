# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:58:17

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 7 | 1.0000 | 0.0000 | 0.0000 | 0.747611 | 0.747611 | 0.0000 | 0.7424 | 5.2864 | 3.9980 | -1.2884 | 0.478120 | 0.226697 | 0.008629 | 0.006035 |
| mittlere_uebergangsphase | 2 | 3.0000 | 3.0000 | 2.0000 | 0.751526 | 0.762191 | 0.0285 | 0.7769 | 3.9402 | 6.7223 | 2.7821 | 2.083367 | 0.325181 | 0.004922 | 0.012160 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1770_A_0_2000 | SYN1770_A_WIDE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751625 | 0.7779 | 3.9044 | 6.7738 | 2.8694 |
| SYN1770_A_3000_5000 | SYN1770_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.745702 | 0.7331 | 6.2318 | 4.3329 | -1.8989 |
| SYN1770_A_6000_8000 | SYN1770_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.749683 | 0.7567 | 4.4579 | 1.4895 | -2.9684 |
| SYN1770_B_0_2000 | SYN1770_B_WIDE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751427 | 0.7759 | 3.9760 | 6.6709 | 2.6948 |
| SYN1770_B_3000_5000 | SYN1770_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.745235 | 0.7329 | 6.6594 | 4.5753 | -2.0841 |
| SYN1770_B_6000_8000 | SYN1770_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.748344 | 0.7376 | 4.5683 | 3.3325 | -1.2358 |
| SYN1770_C_0_2000 | SYN1770_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750837 | 0.7706 | 4.0834 | 6.6716 | 2.5882 |
| SYN1770_C_3000_5000 | SYN1770_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.744697 | 0.7266 | 6.5216 | 4.1444 | -2.3772 |
| SYN1770_C_6000_8000 | SYN1770_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.748779 | 0.7394 | 4.4826 | 3.4396 | -1.0429 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
