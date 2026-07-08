# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:31:28

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 1 | 1.0000 | 0.0000 | 0.0000 | 0.683498 | 0.727129 | 0.5222 | 0.2513 | 2.6948 | 3.3523 | 0.6575 | 0.024003 | 0.047739 | 0.003013 | 0.003556 |
| verteilt_offen | 5 | 7.0000 | 18.4000 | 9.4000 | 0.691080 | 0.730759 | 0.5096 | 0.3008 | 2.6828 | 3.0043 | 0.3215 | 0.082526 | 0.074321 | 0.002659 | 0.002956 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
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

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
