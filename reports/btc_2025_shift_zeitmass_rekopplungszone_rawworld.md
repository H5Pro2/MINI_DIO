# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 17:13:38

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 4 | 1.5000 | 0.5000 | 0.0000 | 0.688870 | 0.729995 | 0.6087 | 0.2958 | 4.3378 | 5.2492 | 0.9114 | 0.051113 | 0.089678 | 0.003982 | 0.004887 |
| mittlere_uebergangsphase | 1 | 4.0000 | 6.0000 | 3.0000 | 0.688445 | 0.730733 | 0.5880 | 0.3052 | 3.5779 | 2.7463 | -0.8316 | 0.037272 | 0.008035 | 0.003333 | 0.002487 |
| verteilt_offen | 5 | 5.8000 | 13.8000 | 7.6000 | 0.689900 | 0.730095 | 0.5107 | 0.2972 | 2.9994 | 2.6670 | -0.3324 | 0.050783 | 0.022916 | 0.002753 | 0.002452 |
| verteilt_rekoppelnd | 1 | 6.0000 | 15.0000 | 5.0000 | 0.695411 | 0.737957 | 0.4352 | 0.3467 | 3.4174 | 3.6072 | 0.1899 | 0.009467 | 0.096631 | 0.003063 | 0.003366 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_1H_SHIFT_4000_5000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | 2 | 1 | 0 | 0.692402 | 0.3196 | 5.0495 | 4.9615 | -0.0879 |
| BTC_2025_1H_SHIFT_5000_6000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | 1 | 0 | 0 | 0.688662 | 0.3068 | 4.9615 | 5.5836 | 0.6220 |
| BTC_2025_1H_SHIFT_6000_7000 | BTC_1H_SHIFTZONE | kompakt_nachhallend | 1 | 0 | 0 | 0.685738 | 0.2731 | 5.5836 | 7.7418 | 2.1582 |
| BTC_2025_30M_SHIFT_8000_9000 | BTC_30M_SHIFTZONE | verteilt_rekoppelnd | 6 | 15 | 5 | 0.695411 | 0.3467 | 3.4174 | 3.6072 | 0.1899 |
| BTC_2025_30M_SHIFT_9000_10000 | BTC_30M_SHIFTZONE | verteilt_offen | 5 | 10 | 6 | 0.690981 | 0.3027 | 3.6072 | 3.2765 | -0.3307 |
| BTC_2025_30M_SHIFT_10000_11000 | BTC_30M_SHIFTZONE | verteilt_offen | 5 | 10 | 6 | 0.690278 | 0.3130 | 3.2765 | 3.5779 | 0.3013 |
| BTC_2025_30M_SHIFT_11000_12000 | BTC_30M_SHIFTZONE | mittlere_uebergangsphase | 4 | 6 | 3 | 0.688445 | 0.3052 | 3.5779 | 2.7463 | -0.8316 |
| BTC_2025_15M_SHIFT_16000_17000 | BTC_15M_SHIFTZONE | verteilt_offen | 6 | 15 | 8 | 0.689152 | 0.3028 | 3.0149 | 1.7565 | -1.2585 |
| BTC_2025_15M_SHIFT_17000_18000 | BTC_15M_SHIFTZONE | kompakt_nachhallend | 2 | 1 | 0 | 0.688680 | 0.2836 | 1.7565 | 2.7099 | 0.9535 |
| BTC_2025_15M_SHIFT_18000_19000 | BTC_15M_SHIFTZONE | verteilt_offen | 7 | 20 | 11 | 0.687460 | 0.2743 | 2.7099 | 2.3883 | -0.3216 |
| BTC_2025_15M_SHIFT_19000_20000 | BTC_15M_SHIFTZONE | verteilt_offen | 6 | 14 | 7 | 0.691627 | 0.2932 | 2.3883 | 2.3360 | -0.0523 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.
