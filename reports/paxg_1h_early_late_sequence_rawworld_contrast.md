# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:37:05

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 2 | 1.0000 | 0.0000 | 0.0000 | 0.685962 | 0.728532 | 0.5089 | 0.2608 | 3.0313 | 4.4165 | 1.3851 | 0.048752 | 0.055003 | 0.003351 | 0.004720 |
| mittlere_uebergangsphase | 2 | 3.5000 | 4.5000 | 2.5000 | 0.686438 | 0.725739 | 0.4216 | 0.2656 | 2.7925 | 3.1257 | 0.3332 | 0.063799 | 0.052791 | 0.002979 | 0.003314 |
| verteilt_offen | 8 | 7.1250 | 19.0000 | 10.0000 | 0.691141 | 0.730564 | 0.4607 | 0.3014 | 3.2229 | 3.1731 | -0.0497 | 0.076674 | 0.065699 | 0.003230 | 0.003124 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_1H_EARLY_0_1000 | PAXG_2024_1H_EARLY_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.690007 | 0.2901 | 2.5120 | 3.3679 | 0.8559 |
| PAXG_2024_1H_EARLY_1000_2000 | PAXG_2024_1H_EARLY_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.688426 | 0.2702 | 3.3679 | 5.4806 | 2.1128 |
| PAXG_2024_1H_EARLY_2000_3000 | PAXG_2024_1H_EARLY_SEQ | verteilt_offen | 6 | 15 | 8 | 0.692984 | 0.3113 | 5.4806 | 2.9753 | -2.5053 |
| PAXG_2025_1H_EARLY_0_1000 | PAXG_2025_1H_EARLY_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.682868 | 0.2410 | 3.0731 | 2.8836 | -0.1894 |
| PAXG_2025_1H_EARLY_1000_2000 | PAXG_2025_1H_EARLY_SEQ | verteilt_offen | 8 | 23 | 14 | 0.690680 | 0.2986 | 2.8836 | 4.0049 | 1.1212 |
| PAXG_2025_1H_EARLY_2000_3000 | PAXG_2025_1H_EARLY_SEQ | verteilt_offen | 8 | 22 | 11 | 0.690059 | 0.2975 | 4.0049 | 3.3833 | -0.6215 |
| PAXG_2024_1H_FOLLOW_4000_5000 | PAXG_2024_1H_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.683498 | 0.2513 | 2.6948 | 3.3523 | 0.6575 |
| PAXG_2024_1H_FOLLOW_5000_6000 | PAXG_2024_1H_SEQ | verteilt_offen | 6 | 14 | 7 | 0.694814 | 0.3293 | 3.3523 | 2.5695 | -0.7827 |
| PAXG_2024_1H_FOLLOW_6000_7000 | PAXG_2024_1H_SEQ | verteilt_offen | 7 | 18 | 8 | 0.690216 | 0.2878 | 2.5695 | 3.0599 | 0.4904 |
| PAXG_2025_1H_FOLLOW_4000_5000 | PAXG_2025_1H_SEQ | verteilt_offen | 8 | 22 | 9 | 0.694612 | 0.3227 | 2.1852 | 2.0408 | -0.1443 |
| PAXG_2025_1H_FOLLOW_5000_6000 | PAXG_2025_1H_SEQ | verteilt_offen | 7 | 20 | 11 | 0.690124 | 0.2935 | 2.0408 | 3.2661 | 1.2253 |
| PAXG_2025_1H_FOLLOW_6000_7000 | PAXG_2025_1H_SEQ | verteilt_offen | 7 | 18 | 12 | 0.685636 | 0.2707 | 3.2661 | 4.0851 | 0.8190 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
