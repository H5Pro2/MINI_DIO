# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:31:01

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 9 | 1.0000 | 0.0000 | 0.0000 | 0.750641 | 0.750641 | 0.0000 | 0.7629 | 2.7509 | 2.8588 | 0.1080 | 0.781603 | 0.413419 | 0.004345 | 0.004599 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1768_A_0_2000 | SYN1768_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750473 | 0.7640 | 2.7661 | 2.4956 | -0.2705 |
| SYN1768_A_3000_5000 | SYN1768_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.749950 | 0.7512 | 2.7995 | 2.7996 | 0.0001 |
| SYN1768_A_6000_8000 | SYN1768_A_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750170 | 0.7590 | 2.8724 | 3.0445 | 0.1721 |
| SYN1768_B_0_2000 | SYN1768_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750618 | 0.7671 | 2.7515 | 2.5597 | -0.1918 |
| SYN1768_B_3000_5000 | SYN1768_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750550 | 0.7590 | 2.7513 | 2.8730 | 0.1217 |
| SYN1768_B_6000_8000 | SYN1768_B_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750695 | 0.7627 | 2.8461 | 3.1855 | 0.3393 |
| SYN1768_C_0_2000 | SYN1768_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.750473 | 0.7640 | 2.7661 | 2.5006 | -0.2655 |
| SYN1768_C_3000_5000 | SYN1768_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.751361 | 0.7646 | 2.5042 | 3.0872 | 0.5830 |
| SYN1768_C_6000_8000 | SYN1768_C_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.751479 | 0.7744 | 2.7005 | 3.1838 | 0.4833 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
