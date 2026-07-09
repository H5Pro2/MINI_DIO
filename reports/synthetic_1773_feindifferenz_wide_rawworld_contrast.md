# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:15:09

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 9 | 1.0000 | 0.0000 | 0.0000 | 0.756751 | 0.756751 | 0.0000 | 0.8361 | 0.7339 | 0.6609 | -0.0730 | 0.105715 | 0.083392 | 0.001222 | 0.001178 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1773_A_0_2000 | SYN1773_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.757744 | 0.8508 | 0.6787 | 0.6468 | -0.0318 |
| SYN1773_A_3000_5000 | SYN1773_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.756210 | 0.8259 | 0.7934 | 0.7167 | -0.0767 |
| SYN1773_A_6000_8000 | SYN1773_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.757861 | 0.8464 | 0.6775 | 0.6003 | -0.0772 |
| SYN1773_B_0_2000 | SYN1773_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.757524 | 0.8475 | 0.6901 | 0.6396 | -0.0505 |
| SYN1773_B_3000_5000 | SYN1773_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.755141 | 0.8146 | 0.8043 | 0.6968 | -0.1075 |
| SYN1773_B_6000_8000 | SYN1773_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.756107 | 0.8323 | 0.7643 | 0.6400 | -0.1243 |
| SYN1773_C_0_2000 | SYN1773_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.757780 | 0.8508 | 0.6777 | 0.6532 | -0.0245 |
| SYN1773_C_3000_5000 | SYN1773_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.755470 | 0.8173 | 0.8017 | 0.7346 | -0.0671 |
| SYN1773_C_6000_8000 | SYN1773_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.756920 | 0.8390 | 0.7177 | 0.6205 | -0.0972 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
