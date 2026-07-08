# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 14:43:22

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 3 | 3.0000 | 3.0000 | 2.0000 | 0.702651 | 0.714176 | 0.0300 | 0.3323 | 1.1525 | 1.0663 | -0.0862 | 0.005651 | 0.003314 | 0.000802 | 0.000723 |
| verteilt_rekoppelnd | 1 | 5.0000 | 10.0000 | 6.0000 | 0.707040 | 0.742225 | 0.1203 | 0.3770 | 0.9458 | 1.0352 | 0.0893 | 0.002001 | 0.010978 | 0.000640 | 0.000685 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_FOLLOW_0_1000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.702374 | 0.3336 | 1.2007 | 1.2217 | 0.0210 |
| PAXG_2024_FOLLOW_1000_2000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.696857 | 0.2992 | 1.2217 | 0.9458 | -0.2758 |
| PAXG_2024_FOLLOW_2000_3000 | PAXG_2024_LOCAL_SEQ | verteilt_rekoppelnd | 5 | 10 | 6 | 0.707040 | 0.3770 | 0.9458 | 1.0352 | 0.0893 |
| PAXG_2024_FOLLOW_3000_4000 | PAXG_2024_LOCAL_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.708721 | 0.3641 | 1.0352 | 1.0313 | -0.0039 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
