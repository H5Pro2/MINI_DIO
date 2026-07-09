# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 14:36:22

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 1 | 1.0000 | 0.0000 | 0.0000 | 0.689703 | 0.731929 | 0.5395 | 0.3191 | 3.8650 | 4.1122 | 0.2472 | 0.092485 | 0.067761 | 0.003885 | 0.003708 |
| mittlere_uebergangsphase | 5 | 4.0000 | 6.0000 | 3.4000 | 0.690288 | 0.729783 | 0.5703 | 0.3023 | 3.6197 | 5.6034 | 1.9838 | 0.018913 | 0.089451 | 0.003386 | 0.005020 |
| verteilt_offen | 7 | 5.8571 | 14.0000 | 7.5714 | 0.690667 | 0.727302 | 0.4730 | 0.3086 | 4.0028 | 3.0147 | -0.9882 | 0.030303 | 0.017405 | 0.003597 | 0.002744 |
| verteilt_rekoppelnd | 3 | 8.0000 | 20.0000 | 10.0000 | 0.704207 | 0.736206 | 0.2952 | 0.3753 | 0.9887 | 1.4035 | 0.4147 | 0.011629 | 0.012492 | 0.000783 | 0.001135 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| XRP_2025_FOLLOW_0_1000 | XRP_2025_LOCAL | verteilt_offen | 6 | 15 | 9 | 0.689200 | 0.3101 | 6.9130 | 3.5747 | -3.3383 |
| DOGE_2025_FOLLOW_0_1000 | DOGE_2025_LOCAL | mittlere_uebergangsphase | 4 | 6 | 4 | 0.689700 | 0.3039 | 8.6213 | 3.8650 | -4.7563 |
| XRP_2025_FOLLOW_1000_2000 | XRP_2025_LOCAL_2 | verteilt_offen | 6 | 13 | 7 | 0.690662 | 0.3206 | 3.5747 | 4.3504 | 0.7757 |
| DOGE_2025_FOLLOW_1000_2000 | DOGE_2025_LOCAL_2 | kompakt_nachhallend | 1 | 0 | 0 | 0.689703 | 0.3191 | 3.8650 | 4.1122 | 0.2472 |
| XRP_2025_FOLLOW_2000_3000 | XRP_2025_LOCAL_3 | verteilt_offen | 5 | 10 | 4 | 0.692256 | 0.3075 | 4.3504 | 2.8478 | -1.5026 |
| DOGE_2025_FOLLOW_2000_3000 | DOGE_2025_LOCAL_3 | verteilt_offen | 6 | 15 | 8 | 0.688473 | 0.2843 | 4.1122 | 3.4339 | -0.6783 |
| XRP_2025_FOLLOW_3000_4000 | XRP_2025_LOCAL_4 | mittlere_uebergangsphase | 4 | 6 | 3 | 0.690080 | 0.3103 | 2.8478 | 10.5925 | 7.7447 |
| DOGE_2025_FOLLOW_3000_4000 | DOGE_2025_LOCAL_4 | mittlere_uebergangsphase | 4 | 6 | 3 | 0.689136 | 0.2984 | 3.4339 | 9.3185 | 5.8845 |
| BTC_2025_FOLLOW_0_1000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 7 | 20 | 11 | 0.692227 | 0.3269 | 4.1171 | 2.6488 | -1.4683 |
| PAXG_2025_FOLLOW_0_1000 | PAXG_2025_LOCAL_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.694303 | 0.3160 | 1.2518 | 1.0622 | -0.1896 |
| BTC_2025_FOLLOW_1000_2000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 5 | 10 | 6 | 0.691002 | 0.3115 | 2.6488 | 2.3037 | -0.3451 |
| PAXG_2025_FOLLOW_1000_2000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 7 | 18 | 8 | 0.699749 | 0.3426 | 1.0622 | 0.9637 | -0.0985 |
| BTC_2025_FOLLOW_2000_3000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 6 | 15 | 8 | 0.690850 | 0.2993 | 2.3037 | 1.9435 | -0.3602 |
| PAXG_2025_FOLLOW_2000_3000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 5 | 10 | 4 | 0.708043 | 0.3996 | 0.9637 | 0.9402 | -0.0235 |
| BTC_2025_FOLLOW_3000_4000 | BTC_2025_LOCAL_SEQ | mittlere_uebergangsphase | 4 | 6 | 4 | 0.688220 | 0.2831 | 1.9435 | 3.1789 | 1.2355 |
| PAXG_2025_FOLLOW_3000_4000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 12 | 32 | 18 | 0.704830 | 0.3837 | 0.9402 | 2.3065 | 1.3663 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
