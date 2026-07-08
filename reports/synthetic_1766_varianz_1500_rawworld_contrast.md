# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:13:24

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 9 | 1.0000 | 0.0000 | 0.0000 | 0.750059 | 0.750059 | 0.0000 | 0.7431 | 2.9887 | 3.0578 | 0.0691 | 0.847961 | 0.619388 | 0.004239 | 0.004192 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1766_A_1500_3000 | SYN1766_A_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.750732 | 0.7494 | 2.0298 | 3.1005 | 1.0707 |
| SYN1766_A_2500_4000 | SYN1766_A_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.749510 | 0.7296 | 3.1005 | 3.0534 | -0.0471 |
| SYN1766_A_3500_5000 | SYN1766_A_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.751366 | 0.7604 | 3.0534 | 3.5129 | 0.4594 |
| SYN1766_B_1500_3000 | SYN1766_B_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.750514 | 0.7489 | 3.1453 | 2.2945 | -0.8507 |
| SYN1766_B_2500_4000 | SYN1766_B_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.750817 | 0.7572 | 2.2945 | 3.5045 | 1.2099 |
| SYN1766_B_3500_5000 | SYN1766_B_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.748855 | 0.7261 | 3.5045 | 3.2829 | -0.2216 |
| SYN1766_C_1500_3000 | SYN1766_C_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.752333 | 0.7811 | 2.6877 | 3.6138 | 0.9261 |
| SYN1766_C_2500_4000 | SYN1766_C_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.746803 | 0.7020 | 3.6138 | 3.4686 | -0.1452 |
| SYN1766_C_3500_5000 | SYN1766_C_1500 | kompakt_nachhallend | 1 | 0 | 0 | 0.749603 | 0.7330 | 3.4686 | 1.6887 | -1.7799 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
