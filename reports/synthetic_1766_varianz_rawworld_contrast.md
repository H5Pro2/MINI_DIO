# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:13:24

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 12 | 1.0000 | 0.0000 | 0.0000 | 0.749229 | 0.749229 | 0.0000 | 0.7207 | 2.4309 | 2.6581 | 0.2271 | 0.548039 | 0.553591 | 0.003611 | 0.004070 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1766_A_0_1000 | SYN1766_A | kompakt_nachhallend | 1 | 0 | 0 | 0.751668 | 0.7569 | 1.7017 | 1.7431 | 0.0415 |
| SYN1766_A_1000_2000 | SYN1766_A | kompakt_nachhallend | 1 | 0 | 0 | 0.750177 | 0.7296 | 1.7431 | 2.1266 | 0.3834 |
| SYN1766_A_2000_3000 | SYN1766_A | kompakt_nachhallend | 1 | 0 | 0 | 0.747845 | 0.6936 | 2.1266 | 3.3085 | 1.1819 |
| SYN1766_A_3000_4000 | SYN1766_A | kompakt_nachhallend | 1 | 0 | 0 | 0.749658 | 0.7270 | 3.3085 | 2.1057 | -1.2027 |
| SYN1766_B_0_1000 | SYN1766_B | kompakt_nachhallend | 1 | 0 | 0 | 0.751668 | 0.7569 | 1.7017 | 1.7431 | 0.0415 |
| SYN1766_B_1000_2000 | SYN1766_B | kompakt_nachhallend | 1 | 0 | 0 | 0.750177 | 0.7296 | 1.7431 | 3.4478 | 1.7047 |
| SYN1766_B_2000_3000 | SYN1766_B | kompakt_nachhallend | 1 | 0 | 0 | 0.747435 | 0.6923 | 3.4478 | 2.1542 | -1.2936 |
| SYN1766_B_3000_4000 | SYN1766_B | kompakt_nachhallend | 1 | 0 | 0 | 0.749404 | 0.7236 | 2.1542 | 3.9712 | 1.8170 |
| SYN1766_C_0_1000 | SYN1766_C | kompakt_nachhallend | 1 | 0 | 0 | 0.751668 | 0.7569 | 1.7017 | 3.5064 | 1.8047 |
| SYN1766_C_1000_2000 | SYN1766_C | kompakt_nachhallend | 1 | 0 | 0 | 0.745560 | 0.6630 | 3.5064 | 1.8386 | -1.6678 |
| SYN1766_C_2000_3000 | SYN1766_C | kompakt_nachhallend | 1 | 0 | 0 | 0.752011 | 0.7650 | 1.8386 | 4.1976 | 2.3591 |
| SYN1766_C_3000_4000 | SYN1766_C | kompakt_nachhallend | 1 | 0 | 0 | 0.743472 | 0.6546 | 4.1976 | 1.7539 | -2.4437 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
