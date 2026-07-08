# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:07:16

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 5 | 1.2000 | 0.2000 | 0.0000 | 0.752100 | 0.753453 | 0.0020 | 0.7839 | 4.1442 | 2.9799 | -1.1643 | 4.798124 | 1.770037 | 0.005286 | 0.004343 |
| mittlere_uebergangsphase | 2 | 3.0000 | 3.0000 | 2.0000 | 0.753054 | 0.784993 | 0.0828 | 0.7875 | 2.6791 | 3.5394 | 0.8602 | 1.264037 | 1.581330 | 0.004106 | 0.004408 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1765_2400_3900_TO_2800_4300 | SYN1765_B_FOCUS | kompakt_nachhallend | 1 | 0 | 0 | 0.750377 | 0.7505 | 4.5655 | 3.6033 | -0.9623 |
| SYN1765_2800_4300_TO_3000_4500 | SYN1765_B_FOCUS | kompakt_nachhallend | 1 | 0 | 0 | 0.753732 | 0.8082 | 3.6033 | 2.6523 | -0.9510 |
| SYN1765_3000_4500_TO_3200_4700 | SYN1765_B_FOCUS | mittlere_uebergangsphase | 3 | 3 | 2 | 0.753456 | 0.7870 | 2.6523 | 2.0920 | -0.5603 |
| SYN1765_2400_4400_TO_2800_4800 | SYN1765_B_FOCUS_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.752471 | 0.7841 | 4.2390 | 3.2320 | -1.0070 |
| SYN1765_2800_4800_TO_3000_5000 | SYN1765_B_FOCUS_WIDE | kompakt_nachhallend | 1 | 0 | 0 | 0.754236 | 0.8090 | 3.2320 | 2.7059 | -0.5261 |
| SYN1765_3000_5000_TO_3200_5200 | SYN1765_B_FOCUS_WIDE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.752651 | 0.7880 | 2.7059 | 4.9867 | 2.2808 |
| SYN1765_2600_5100_TO_3000_5000 | SYN1765_B_FOCUS_LONG | kompakt_nachhallend | 2 | 1 | 0 | 0.749682 | 0.7679 | 5.0810 | 2.7059 | -2.3751 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
