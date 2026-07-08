# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 17:09:05

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 3 | 1.6667 | 0.6667 | 0.6667 | 0.686713 | 0.729166 | 0.6090 | 0.2799 | 3.3720 | 3.7042 | 0.3322 | 0.049183 | 0.010539 | 0.003130 | 0.003308 |
| mittlere_uebergangsphase | 4 | 3.0000 | 3.0000 | 2.0000 | 0.689719 | 0.728911 | 0.5267 | 0.3079 | 4.6754 | 3.8321 | -0.8433 | 0.076975 | 0.082205 | 0.004348 | 0.003563 |
| verteilt_offen | 2 | 6.0000 | 15.0000 | 9.0000 | 0.693761 | 0.734779 | 0.5733 | 0.3271 | 6.6248 | 5.8856 | -0.7393 | 0.107668 | 0.122271 | 0.005917 | 0.005392 |
| verteilt_rekoppelnd | 2 | 5.0000 | 10.0000 | 4.0000 | 0.695355 | 0.732094 | 0.4341 | 0.3450 | 6.3039 | 4.2242 | -2.0798 | 0.054344 | 0.121266 | 0.005674 | 0.004023 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_NEIGHBOR_1000_2000 | BTC_1H_REKOPPLUNGSZONE | verteilt_offen | 6 | 15 | 9 | 0.693540 | 0.3275 | 9.4843 | 7.3724 | -2.1119 |
| BTC_2025_1H_CORE_2000_3000 | BTC_1H_REKOPPLUNGSZONE | verteilt_rekoppelnd | 5 | 10 | 4 | 0.695555 | 0.3512 | 7.3724 | 5.5083 | -1.8641 |
| BTC_2025_1H_NEIGHBOR_3000_4000 | BTC_1H_REKOPPLUNGSZONE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.693828 | 0.3459 | 5.5083 | 5.0495 | -0.4588 |
| BTC_2025_30M_ZONE_4000_5000 | BTC_30M_SAME_PHASE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.684869 | 0.2725 | 6.3348 | 3.7654 | -2.5694 |
| BTC_2025_30M_ZONE_5000_6000 | BTC_30M_SAME_PHASE | verteilt_offen | 6 | 15 | 9 | 0.693982 | 0.3267 | 3.7654 | 4.3987 | 0.6333 |
| BTC_2025_30M_ZONE_6000_7000 | BTC_30M_SAME_PHASE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.691095 | 0.3116 | 4.3987 | 3.5667 | -0.8319 |
| BTC_2025_30M_ZONE_7000_8000 | BTC_30M_SAME_PHASE | kompakt_nachhallend | 2 | 1 | 1 | 0.691953 | 0.3183 | 3.5667 | 3.4174 | -0.1493 |
| BTC_2025_15M_ZONE_8000_9000 | BTC_15M_SAME_PHASE | kompakt_nachhallend | 2 | 1 | 1 | 0.684251 | 0.2603 | 3.6092 | 5.2354 | 1.6262 |
| BTC_2025_15M_ZONE_9000_10000 | BTC_15M_SAME_PHASE | verteilt_rekoppelnd | 5 | 10 | 4 | 0.695155 | 0.3388 | 5.2354 | 2.9400 | -2.2954 |
| BTC_2025_15M_ZONE_10000_11000 | BTC_15M_SAME_PHASE | kompakt_nachhallend | 1 | 0 | 0 | 0.683936 | 0.2611 | 2.9400 | 2.4598 | -0.4801 |
| BTC_2025_15M_ZONE_11000_12000 | BTC_15M_SAME_PHASE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.689084 | 0.3017 | 2.4598 | 2.9467 | 0.4868 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
