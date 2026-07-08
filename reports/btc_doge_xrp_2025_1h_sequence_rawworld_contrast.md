# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 17:04:12

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 2 | 1.5000 | 0.5000 | 0.0000 | 0.691933 | 0.729913 | 0.5293 | 0.3279 | 12.3608 | 13.7290 | 1.3682 | 0.059424 | 0.389427 | 0.012026 | 0.012767 |
| mittlere_uebergangsphase | 5 | 3.4000 | 4.2000 | 2.4000 | 0.694551 | 0.733417 | 0.5469 | 0.3443 | 12.8434 | 11.7160 | -1.1274 | 0.088911 | 0.132267 | 0.012107 | 0.011030 |
| verteilt_offen | 4 | 6.0000 | 14.2500 | 7.5000 | 0.692461 | 0.731494 | 0.5737 | 0.3284 | 14.2912 | 12.0096 | -2.2817 | 0.171260 | 0.064087 | 0.013368 | 0.011574 |
| verteilt_rekoppelnd | 1 | 5.0000 | 10.0000 | 4.0000 | 0.695555 | 0.737000 | 0.4432 | 0.3512 | 7.3724 | 5.5083 | -1.8641 | 0.092474 | 0.135584 | 0.006695 | 0.005363 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_0_1000 | BTC_2025_1H_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.695357 | 0.3368 | 8.6427 | 9.4843 | 0.8417 |
| BTC_2025_1H_1000_2000 | BTC_2025_1H_SEQ | verteilt_offen | 6 | 15 | 9 | 0.693540 | 0.3275 | 9.4843 | 7.3724 | -2.1119 |
| BTC_2025_1H_2000_3000 | BTC_2025_1H_SEQ | verteilt_rekoppelnd | 5 | 10 | 4 | 0.695555 | 0.3512 | 7.3724 | 5.5083 | -1.8641 |
| BTC_2025_1H_3000_4000 | BTC_2025_1H_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.693828 | 0.3459 | 5.5083 | 5.0495 | -0.4588 |
| DOGE_2025_1H_0_1000 | DOGE_2025_1H_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.695702 | 0.3441 | 19.1004 | 16.0634 | -3.0370 |
| DOGE_2025_1H_1000_2000 | DOGE_2025_1H_SEQ | verteilt_offen | 5 | 10 | 6 | 0.691510 | 0.3202 | 16.0634 | 13.8054 | -2.2581 |
| DOGE_2025_1H_2000_3000 | DOGE_2025_1H_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.694065 | 0.3455 | 13.8054 | 15.0216 | 1.2162 |
| DOGE_2025_1H_3000_4000 | DOGE_2025_1H_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.691710 | 0.3291 | 15.0216 | 15.2889 | 0.2673 |
| XRP_2025_1H_0_1000 | XRP_2025_1H_SEQ | verteilt_offen | 8 | 22 | 9 | 0.690207 | 0.3176 | 18.6559 | 17.1605 | -1.4955 |
| XRP_2025_1H_1000_2000 | XRP_2025_1H_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.693802 | 0.3492 | 17.1605 | 12.9613 | -4.1992 |
| XRP_2025_1H_2000_3000 | XRP_2025_1H_SEQ | verteilt_offen | 5 | 10 | 6 | 0.694588 | 0.3483 | 12.9613 | 9.7000 | -3.2613 |
| XRP_2025_1H_3000_4000 | XRP_2025_1H_SEQ | kompakt_nachhallend | 2 | 1 | 0 | 0.692157 | 0.3267 | 9.7000 | 12.1691 | 2.4691 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
