# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:03:18

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 11 | 1.0000 | 0.0000 | 0.0000 | 0.750638 | 0.750638 | 0.0000 | 0.7504 | 2.6859 | 3.7836 | 1.0977 | 0.625504 | 1.001838 | 0.004151 | 0.005866 |
| mittlere_uebergangsphase | 1 | 3.0000 | 3.0000 | 2.0000 | 0.750783 | 0.778847 | 0.0797 | 0.7438 | 2.8830 | 1.8693 | -1.0137 | 1.224729 | 0.015660 | 0.004594 | 0.003709 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1764_A_0_1000 | SYN1764_A | kompakt_nachhallend | 1 | 0 | 0 | 0.755470 | 0.8052 | 1.2219 | 2.4579 | 1.2360 |
| SYN1764_A_1000_2000 | SYN1764_A | kompakt_nachhallend | 1 | 0 | 0 | 0.753400 | 0.7822 | 2.4579 | 2.0613 | -0.3966 |
| SYN1764_A_2000_3000 | SYN1764_A | kompakt_nachhallend | 1 | 0 | 0 | 0.751921 | 0.7518 | 2.0613 | 1.7625 | -0.2988 |
| SYN1764_A_3000_4000 | SYN1764_A | kompakt_nachhallend | 1 | 0 | 0 | 0.754470 | 0.7865 | 1.7625 | 8.3978 | 6.6353 |
| SYN1764_B_0_1000 | SYN1764_B | kompakt_nachhallend | 1 | 0 | 0 | 0.755505 | 0.8057 | 1.2194 | 2.4693 | 1.2499 |
| SYN1764_B_1000_2000 | SYN1764_B | kompakt_nachhallend | 1 | 0 | 0 | 0.753607 | 0.7915 | 2.4693 | 4.8063 | 2.3370 |
| SYN1764_B_2000_3000 | SYN1764_B | kompakt_nachhallend | 1 | 0 | 0 | 0.746841 | 0.6765 | 4.8063 | 2.8830 | -1.9233 |
| SYN1764_B_3000_4000 | SYN1764_B | mittlere_uebergangsphase | 3 | 3 | 2 | 0.750783 | 0.7438 | 2.8830 | 1.8693 | -1.0137 |
| SYN1764_C_0_1000 | SYN1764_C | kompakt_nachhallend | 1 | 0 | 0 | 0.755499 | 0.8066 | 1.2264 | 2.4253 | 1.1989 |
| SYN1764_C_1000_2000 | SYN1764_C | kompakt_nachhallend | 1 | 0 | 0 | 0.752889 | 0.7737 | 2.4253 | 7.7522 | 5.3268 |
| SYN1764_C_2000_3000 | SYN1764_C | kompakt_nachhallend | 1 | 0 | 0 | 0.723592 | 0.4664 | 7.7522 | 2.1425 | -5.6096 |
| SYN1764_C_3000_4000 | SYN1764_C | kompakt_nachhallend | 1 | 0 | 0 | 0.753822 | 0.8083 | 2.1425 | 4.4616 | 2.3190 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
