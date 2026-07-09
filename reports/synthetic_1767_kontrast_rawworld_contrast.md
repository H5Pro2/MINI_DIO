# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 15:21:07

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 12 | 1.0000 | 0.0000 | 0.0000 | 0.749641 | 0.749641 | 0.0000 | 0.7354 | 2.5785 | 2.4156 | -0.1629 | 0.346294 | 0.260605 | 0.004468 | 0.004259 |
| mittlere_uebergangsphase | 3 | 3.0000 | 3.0000 | 2.0000 | 0.751469 | 0.763683 | 0.0328 | 0.7500 | 2.2681 | 3.1390 | 0.8709 | 0.528828 | 0.464747 | 0.002635 | 0.005556 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN1767_A_0_1000 | SYN1767_A | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751285 | 0.7473 | 2.2923 | 3.0615 | 0.7692 |
| SYN1767_A_1000_2000 | SYN1767_A | kompakt_nachhallend | 1 | 0 | 0 | 0.747015 | 0.7061 | 3.0615 | 3.2064 | 0.1449 |
| SYN1767_A_2000_3000 | SYN1767_A | kompakt_nachhallend | 1 | 0 | 0 | 0.745932 | 0.6805 | 3.2064 | 1.7440 | -1.4623 |
| SYN1767_A_3000_4000 | SYN1767_A | kompakt_nachhallend | 1 | 0 | 0 | 0.754358 | 0.8150 | 1.7440 | 2.0685 | 0.3245 |
| SYN1767_A_4000_5000 | SYN1767_A | kompakt_nachhallend | 1 | 0 | 0 | 0.752328 | 0.7563 | 2.0685 | 2.3850 | 0.3165 |
| SYN1767_B_0_1000 | SYN1767_B | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751836 | 0.7555 | 2.2197 | 3.2940 | 1.0743 |
| SYN1767_B_1000_2000 | SYN1767_B | kompakt_nachhallend | 1 | 0 | 0 | 0.745841 | 0.6848 | 3.2940 | 3.0433 | -0.2508 |
| SYN1767_B_2000_3000 | SYN1767_B | kompakt_nachhallend | 1 | 0 | 0 | 0.745882 | 0.6837 | 3.0433 | 2.8648 | -0.1784 |
| SYN1767_B_3000_4000 | SYN1767_B | kompakt_nachhallend | 1 | 0 | 0 | 0.749970 | 0.7394 | 2.8648 | 1.5089 | -1.3559 |
| SYN1767_B_4000_5000 | SYN1767_B | kompakt_nachhallend | 1 | 0 | 0 | 0.754805 | 0.8000 | 1.5089 | 2.4065 | 0.8976 |
| SYN1767_C_0_1000 | SYN1767_C | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751285 | 0.7473 | 2.2923 | 3.0615 | 0.7692 |
| SYN1767_C_1000_2000 | SYN1767_C | kompakt_nachhallend | 1 | 0 | 0 | 0.747015 | 0.7061 | 3.0615 | 3.2821 | 0.2206 |
| SYN1767_C_2000_3000 | SYN1767_C | kompakt_nachhallend | 1 | 0 | 0 | 0.745300 | 0.6747 | 3.2821 | 1.7554 | -1.5267 |
| SYN1767_C_3000_4000 | SYN1767_C | kompakt_nachhallend | 1 | 0 | 0 | 0.754084 | 0.8106 | 1.7554 | 2.0515 | 0.2961 |
| SYN1767_C_4000_5000 | SYN1767_C | kompakt_nachhallend | 1 | 0 | 0 | 0.753161 | 0.7680 | 2.0515 | 2.6705 | 0.6190 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
