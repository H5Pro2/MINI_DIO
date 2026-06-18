# Weltlautstaerke-Diagnose

Stand: 2026-06-18 23:21:04

## Zweck

Diese Diagnose prueft, ob unterschiedliche Welten unterschiedlich laut oder intensiv in MINI_DIO ankommen.
Sie trennt Rohwelt-Lautstaerke von MCM-Feldwirkung.

Hierarchie der Pruefung:

1. Grundfrage: Ist die staerkere Feldlast eine reale Weltwirkung oder eine Sensorik-/Normierungsfrage?
2. Unterpruefung: Wie verhalten sich Rohwelt-Lautstaerke, Rekopplung, Strain und Episodenmemory zueinander?
3. Folgeschritt: Entscheiden, ob eine bessere Welt-Normierung oder eine separate Verdichtungs-Sensitivitaet notwendig ist.

## Uebersicht

| Welt | Lautstaerke | avg_ret | p95_ret | avg_range | p95_range | Strain | Memory | Rekopplung | Tragqualitaet |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| btc_2024_15m | 4.622 | 0.002042 | 0.005873 | 0.004016 | 0.010103 | 83 | 105 | 0.631196 | 0.362364 |
| btc_2024_1h | 9.779 | 0.004020 | 0.013160 | 0.008416 | 0.021051 | 277 | 329 | 0.610376 | 0.345005 |
| btc_2024_30m | 5.741 | 0.002435 | 0.007756 | 0.005000 | 0.012001 | 129 | 179 | 0.626156 | 0.359372 |
| btc_2024_5m | 2.453 | 0.001154 | 0.003274 | 0.002102 | 0.004929 | 42 | 63 | 0.636577 | 0.366108 |
| btc_2025_15m | 4.170 | 0.001887 | 0.005400 | 0.003695 | 0.008696 | 79 | 125 | 0.631429 | 0.363392 |
| btc_2025_1h | 9.321 | 0.003934 | 0.012215 | 0.008045 | 0.020355 | 282 | 347 | 0.611240 | 0.347018 |
| btc_2025_30m | 6.057 | 0.002731 | 0.007796 | 0.005388 | 0.012781 | 132 | 167 | 0.623087 | 0.355382 |
| btc_2025_5m | 1.730 | 0.000779 | 0.002393 | 0.001355 | 0.003521 | 44 | 87 | 0.638380 | 0.368524 |
| sol_2024_15m | 9.731 | 0.004505 | 0.012157 | 0.009292 | 0.019965 | 266 | 309 | 0.606542 | 0.343678 |
| sol_2024_1h | 18.874 | 0.008273 | 0.024205 | 0.017364 | 0.039861 | 630 | 643 | 0.587027 | 0.333433 |
| sol_2024_30m | 11.939 | 0.005375 | 0.015539 | 0.011323 | 0.023928 | 365 | 441 | 0.600205 | 0.341420 |
| sol_2024_5m | 5.735 | 0.002809 | 0.007116 | 0.005589 | 0.011282 | 105 | 149 | 0.622776 | 0.358038 |
| sol_2025_15m | 9.769 | 0.003975 | 0.013892 | 0.007683 | 0.021081 | 218 | 247 | 0.615512 | 0.351537 |
| sol_2025_1h | 18.005 | 0.008056 | 0.023777 | 0.016035 | 0.037411 | 587 | 591 | 0.589067 | 0.335489 |
| sol_2025_30m | 13.461 | 0.005871 | 0.018367 | 0.011423 | 0.028202 | 402 | 434 | 0.600912 | 0.343351 |
| sol_2025_5m | 2.639 | 0.001263 | 0.003421 | 0.002423 | 0.005160 | 28 | 55 | 0.636504 | 0.365647 |

## Sensitivitaet

| Welt | Strain/Lautstaerke | Memory/Lautstaerke | field_strained_ratio | field_carried_ratio | Richtungswechsel | Drift |
|---|---:|---:|---:|---:|---:|---:|
| btc_2024_15m | 0.009007 | 22.720 | 0.0416 | 0.9584 | 1063 | -0.018090 |
| btc_2024_1h | 0.014206 | 33.645 | 0.1389 | 0.8611 | 1056 | 0.520496 |
| btc_2024_30m | 0.011270 | 31.182 | 0.0647 | 0.9353 | 1032 | 0.135095 |
| btc_2024_5m | 0.008587 | 25.684 | 0.0211 | 0.9789 | 1048 | 0.035835 |
| btc_2025_15m | 0.009501 | 29.976 | 0.0396 | 0.9604 | 1009 | 0.142811 |
| btc_2025_1h | 0.015172 | 37.226 | 0.1414 | 0.8586 | 1054 | -0.084367 |
| btc_2025_30m | 0.010930 | 27.572 | 0.0662 | 0.9338 | 1058 | 0.034616 |
| btc_2025_5m | 0.012755 | 50.290 | 0.0221 | 0.9779 | 1037 | 0.037023 |
| sol_2024_15m | 0.013709 | 31.755 | 0.1334 | 0.8666 | 1023 | -0.096717 |
| sol_2024_1h | 0.016739 | 34.067 | 0.3159 | 0.6841 | 1046 | 0.702040 |
| sol_2024_30m | 0.015332 | 36.937 | 0.1830 | 0.8170 | 1051 | 0.066131 |
| sol_2024_5m | 0.009181 | 25.979 | 0.0527 | 0.9473 | 955 | -0.125012 |
| sol_2025_15m | 0.011191 | 25.284 | 0.1093 | 0.8907 | 989 | 0.330166 |
| sol_2025_1h | 0.016350 | 32.825 | 0.2944 | 0.7056 | 1050 | -0.275683 |
| sol_2025_30m | 0.014977 | 32.241 | 0.2016 | 0.7984 | 1021 | 0.045879 |
| sol_2025_5m | 0.005321 | 20.840 | 0.0140 | 0.9860 | 990 | 0.072110 |

## Befund

Die Lautstaerke ist keine Feldklasse. Sie beschreibt nur, wie stark die Rohwelt durch Bewegung, Range und Volumenrhythmus auftritt.

Wenn eine Welt bei vergleichbarer Lautstaerke deutlich mehr `field_strained` oder Episodenmemory erzeugt, spricht das fuer andere Verdichtungs-Sensitivitaet.
Wenn eine Welt zugleich lauter ist und staerker kippt, muss geprueft werden, ob die Sensorik sauber asset-relativ normiert ist.

## Wie es weitergeht

Als naechstes sollte aus dieser Diagnose eine Verdichtungs-Sensitivitaetskarte entstehen.
Sie soll nicht regulieren und keine Handlung ausloesen, sondern nur zeigen, welche Welten bei welcher Zeitaufloesung ueberproportional viel Innenfeldlast erzeugen.
