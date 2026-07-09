# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:08:04

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 9 | 1.0000 | 0.0000 | 0.0000 | 0.759551 | 0.759551 | 0.0000 | 0.8684 | 0.6137 | 0.6080 | -0.0057 | 0.147605 | 0.116587 | 0.001142 | 0.001144 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1772_A_0_2000 | SYN1772_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759483 | 0.8654 | 0.6050 | 0.6108 | 0.0058 |
| SYN1772_A_3000_5000 | SYN1772_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759072 | 0.8655 | 0.6294 | 0.6160 | -0.0134 |
| SYN1772_A_6000_8000 | SYN1772_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.760518 | 0.8772 | 0.5607 | 0.6160 | 0.0553 |
| SYN1772_B_0_2000 | SYN1772_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759483 | 0.8654 | 0.6050 | 0.6174 | 0.0124 |
| SYN1772_B_3000_5000 | SYN1772_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759118 | 0.8655 | 0.6390 | 0.6480 | 0.0090 |
| SYN1772_B_6000_8000 | SYN1772_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759889 | 0.8753 | 0.6166 | 0.5659 | -0.0508 |
| SYN1772_C_0_2000 | SYN1772_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759533 | 0.8662 | 0.6146 | 0.5975 | -0.0171 |
| SYN1772_C_3000_5000 | SYN1772_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.758913 | 0.8599 | 0.6368 | 0.6353 | -0.0015 |
| SYN1772_C_6000_8000 | SYN1772_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.759948 | 0.8750 | 0.6158 | 0.5650 | -0.0508 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
