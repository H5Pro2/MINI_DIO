# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 14:40:39

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 2 | 3.5000 | 4.5000 | 2.5000 | 0.689025 | 0.731232 | 0.6555 | 0.2934 | 2.7319 | 2.1861 | -0.5458 | 0.060863 | 0.041696 | 0.002502 | 0.002075 |
| verteilt_offen | 10 | 6.4000 | 15.4000 | 7.8000 | 0.690511 | 0.730288 | 0.5165 | 0.3002 | 2.2472 | 2.0477 | -0.1994 | 0.036626 | 0.033806 | 0.001984 | 0.001856 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_FOLLOW_0_1000 | BTC_2024_LOCAL_SEQ | verteilt_offen | 5 | 10 | 6 | 0.693136 | 0.3185 | 1.8726 | 2.3523 | 0.4797 |
| DOGE_2024_FOLLOW_0_1000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | 8 | 22 | 4 | 0.692157 | 0.3010 | 3.7720 | 3.4607 | -0.3113 |
| XRP_2024_FOLLOW_0_1000 | XRP_2024_LOCAL_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.690265 | 0.2956 | 2.0031 | 2.6008 | 0.5977 |
| BTC_2024_FOLLOW_1000_2000 | BTC_2024_LOCAL_SEQ | verteilt_offen | 5 | 10 | 6 | 0.688281 | 0.2815 | 2.3523 | 1.5846 | -0.7677 |
| DOGE_2024_FOLLOW_1000_2000 | DOGE_2024_LOCAL_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.687785 | 0.2911 | 3.4607 | 1.7714 | -1.6894 |
| XRP_2024_FOLLOW_1000_2000 | XRP_2024_LOCAL_SEQ | verteilt_offen | 6 | 14 | 8 | 0.691871 | 0.3035 | 2.6008 | 1.5042 | -1.0966 |
| BTC_2024_FOLLOW_2000_3000 | BTC_2024_LOCAL_SEQ | verteilt_offen | 6 | 14 | 8 | 0.690215 | 0.3071 | 1.5846 | 1.9014 | 0.3168 |
| DOGE_2024_FOLLOW_2000_3000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | 10 | 29 | 14 | 0.687989 | 0.2801 | 1.7714 | 2.6028 | 0.8314 |
| XRP_2024_FOLLOW_2000_3000 | XRP_2024_LOCAL_SEQ | verteilt_offen | 6 | 14 | 8 | 0.688835 | 0.2830 | 1.5042 | 2.5096 | 1.0054 |
| BTC_2024_FOLLOW_3000_4000 | BTC_2024_LOCAL_SEQ | verteilt_offen | 7 | 17 | 10 | 0.689866 | 0.3091 | 1.9014 | 1.2992 | -0.6022 |
| DOGE_2024_FOLLOW_3000_4000 | DOGE_2024_LOCAL_SEQ | verteilt_offen | 6 | 14 | 8 | 0.690349 | 0.3024 | 2.6028 | 1.3111 | -1.2917 |
| XRP_2024_FOLLOW_3000_4000 | XRP_2024_LOCAL_SEQ | verteilt_offen | 5 | 10 | 6 | 0.692412 | 0.3153 | 2.5096 | 1.9514 | -0.5581 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
