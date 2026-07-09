# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:53:51

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 2 | 3.0000 | 3.0000 | 2.0000 | 0.688316 | 0.731159 | 0.5747 | 0.3000 | 3.2569 | 3.2079 | -0.0490 | 0.057522 | 0.042702 | 0.003131 | 0.002781 |
| verteilt_offen | 10 | 6.8000 | 17.4000 | 10.2000 | 0.686443 | 0.722955 | 0.4987 | 0.2782 | 4.2218 | 4.5754 | 0.3536 | 0.026593 | 0.054158 | 0.003870 | 0.004159 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_FOLLOW_5000_6000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | 5 | 10 | 6 | 0.686624 | 0.2797 | 4.1171 | 2.6488 | -1.4683 |
| BTC_2025_FOLLOW_6000_7000 | BTC_2025_LOCAL_SEQ_LATE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.688127 | 0.2900 | 2.6488 | 2.3037 | -0.3451 |
| BTC_2025_FOLLOW_7000_8000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | 7 | 18 | 12 | 0.681067 | 0.2186 | 2.3037 | 1.9435 | -0.3602 |
| BTC_2025_FOLLOW_8000_9000 | BTC_2025_LOCAL_SEQ_LATE | verteilt_offen | 5 | 10 | 6 | 0.689468 | 0.2892 | 1.9435 | 3.1789 | 1.2355 |
| DOGE_2025_FOLLOW_5000_6000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | 6 | 15 | 9 | 0.688901 | 0.2997 | 8.6213 | 3.8650 | -4.7563 |
| DOGE_2025_FOLLOW_6000_7000 | DOGE_2025_LOCAL_SEQ_LATE | mittlere_uebergangsphase | 3 | 3 | 2 | 0.688504 | 0.3100 | 3.8650 | 4.1122 | 0.2472 |
| DOGE_2025_FOLLOW_7000_8000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | 7 | 21 | 12 | 0.679671 | 0.2245 | 4.1122 | 3.4339 | -0.6783 |
| DOGE_2025_FOLLOW_8000_9000 | DOGE_2025_LOCAL_SEQ_LATE | verteilt_offen | 6 | 15 | 8 | 0.690038 | 0.3069 | 3.4339 | 9.3185 | 5.8845 |
| XRP_2025_FOLLOW_5000_6000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | 5 | 10 | 6 | 0.687928 | 0.3035 | 6.9130 | 3.5747 | -3.3383 |
| XRP_2025_FOLLOW_6000_7000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | 8 | 25 | 15 | 0.689787 | 0.3161 | 3.5747 | 4.3504 | 0.7757 |
| XRP_2025_FOLLOW_7000_8000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | 7 | 18 | 10 | 0.677412 | 0.1966 | 4.3504 | 2.8478 | -1.5026 |
| XRP_2025_FOLLOW_8000_9000 | XRP_2025_LOCAL_SEQ_LATE | verteilt_offen | 12 | 32 | 18 | 0.693538 | 0.3469 | 2.8478 | 10.5925 | 7.7447 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
