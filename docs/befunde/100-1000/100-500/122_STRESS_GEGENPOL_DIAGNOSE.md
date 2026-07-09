# Stress-Gegenpol-Diagnose

Stand: 2026-06-18 17:30:55

## Zweck

Diese Diagnose untersucht, welche Rohwelt- und Innenfeldmerkmale den Stress-Gegenpol begleiten.
Sie ist passiv: Sie erzeugt keine Handlung, kein Gate und keine Regel.

Hierarchie der Prüfung:

1. Grundfrage: Warum kippt eine Welt in stärkere innere Verarbeitungslast?
2. Unterprüfung: Welche Abschnitte tragen erhöhte Spannung, Kippnähe und Episodenmemory?
3. Folgeschritt: Prüfen, ob diese Merkmale bei neuen Stresswelten wiederkehren.

## Ergebnisübersicht

### welt_2023_stress_01

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2023_stress_01`

Top-Stressabschnitte:

- Abschnitt `8` (`693`-`792`): stress_score `0.8183`, stress_ratio `0.414`, tragend_unruhig `0.343`, Rekopplung `0.601`, avg_abs_return `0.0065`, avg_range `0.0143`, Episodenmemory `23`
- Abschnitt `9` (`792`-`891`): stress_score `0.7940`, stress_ratio `0.394`, tragend_unruhig `0.384`, Rekopplung `0.595`, avg_abs_return `0.0067`, avg_range `0.0131`, Episodenmemory `20`
- Abschnitt `10` (`891`-`994`): stress_score `0.5832`, stress_ratio `0.252`, tragend_unruhig `0.553`, Rekopplung `0.607`, avg_abs_return `0.0045`, avg_range `0.0094`, Episodenmemory `14`

### welt_2024_bridge3_01

- Datenwelt: `data\kontrolliert_2024_bridge_test3_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2024_bridge3_01`

Top-Stressabschnitte:

- Abschnitt `9` (`792`-`891`): stress_score `0.6861`, stress_ratio `0.414`, tragend_unruhig `0.465`, Rekopplung `0.597`, avg_abs_return `0.0049`, avg_range `0.0100`, Episodenmemory `28`
- Abschnitt `6` (`495`-`594`): stress_score `0.5779`, stress_ratio `0.212`, tragend_unruhig `0.495`, Rekopplung `0.614`, avg_abs_return `0.0051`, avg_range `0.0095`, Episodenmemory `14`
- Abschnitt `1` (`0`-`99`): stress_score `0.4976`, stress_ratio `0.242`, tragend_unruhig `0.434`, Rekopplung `0.610`, avg_abs_return `0.0036`, avg_range `0.0080`, Episodenmemory `20`

### welt_2025_core_01

- Datenwelt: `data\kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2025_core_01`

Top-Stressabschnitte:

- Abschnitt `8` (`693`-`792`): stress_score `0.2118`, stress_ratio `0.051`, tragend_unruhig `0.495`, Rekopplung `0.631`, avg_abs_return `0.0017`, avg_range `0.0033`, Episodenmemory `4`
- Abschnitt `5` (`396`-`495`): stress_score `0.1913`, stress_ratio `0.030`, tragend_unruhig `0.475`, Rekopplung `0.629`, avg_abs_return `0.0016`, avg_range `0.0031`, Episodenmemory `4`
- Abschnitt `4` (`297`-`396`): stress_score `0.1874`, stress_ratio `0.051`, tragend_unruhig `0.414`, Rekopplung `0.635`, avg_abs_return `0.0016`, avg_range `0.0033`, Episodenmemory `0`

### welt_2025_late_shift_01

- Datenwelt: `data\kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2025_late_shift_01`

Top-Stressabschnitte:

- Abschnitt `6` (`495`-`594`): stress_score `0.2665`, stress_ratio `0.101`, tragend_unruhig `0.495`, Rekopplung `0.623`, avg_abs_return `0.0021`, avg_range `0.0037`, Episodenmemory `8`
- Abschnitt `5` (`396`-`495`): stress_score `0.2487`, stress_ratio `0.091`, tragend_unruhig `0.465`, Rekopplung `0.631`, avg_abs_return `0.0020`, avg_range `0.0040`, Episodenmemory `0`
- Abschnitt `1` (`0`-`99`): stress_score `0.2289`, stress_ratio `0.051`, tragend_unruhig `0.475`, Rekopplung `0.625`, avg_abs_return `0.0020`, avg_range `0.0035`, Episodenmemory `6`

## Abschnittsdetails

### welt_2023_stress_01

| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.091 | 0.485 | 0.404 | 0.621 | 0.346 | 0.0022 | 0.0046 | -0.017 | 6 |
| 2 | 0.222 | 0.525 | 0.253 | 0.615 | 0.346 | 0.0033 | 0.0068 | 0.055 | 10 |
| 3 | 0.061 | 0.323 | 0.586 | 0.627 | 0.355 | 0.0019 | 0.0038 | -0.031 | 6 |
| 4 | 0.172 | 0.485 | 0.303 | 0.613 | 0.348 | 0.0034 | 0.0073 | 0.032 | 12 |
| 5 | 0.101 | 0.465 | 0.434 | 0.622 | 0.352 | 0.0027 | 0.0053 | -0.001 | 4 |
| 6 | 0.131 | 0.374 | 0.465 | 0.621 | 0.351 | 0.0024 | 0.0054 | 0.008 | 8 |
| 7 | 0.081 | 0.444 | 0.475 | 0.627 | 0.343 | 0.0018 | 0.0046 | 0.017 | 3 |
| 8 | 0.414 | 0.343 | 0.222 | 0.601 | 0.344 | 0.0065 | 0.0143 | 0.288 | 23 |
| 9 | 0.394 | 0.384 | 0.172 | 0.595 | 0.331 | 0.0067 | 0.0131 | 0.001 | 20 |
| 10 | 0.252 | 0.553 | 0.194 | 0.607 | 0.345 | 0.0045 | 0.0094 | 0.043 | 14 |

### welt_2024_bridge3_01

| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.242 | 0.434 | 0.263 | 0.610 | 0.352 | 0.0036 | 0.0080 | -0.009 | 20 |
| 2 | 0.162 | 0.545 | 0.273 | 0.617 | 0.356 | 0.0031 | 0.0061 | 0.060 | 12 |
| 3 | 0.172 | 0.535 | 0.293 | 0.617 | 0.356 | 0.0029 | 0.0063 | 0.040 | 12 |
| 4 | 0.182 | 0.455 | 0.323 | 0.616 | 0.354 | 0.0034 | 0.0069 | 0.039 | 8 |
| 5 | 0.162 | 0.424 | 0.394 | 0.614 | 0.344 | 0.0031 | 0.0070 | -0.020 | 8 |
| 6 | 0.212 | 0.495 | 0.293 | 0.614 | 0.356 | 0.0051 | 0.0095 | 0.000 | 14 |
| 7 | 0.040 | 0.505 | 0.455 | 0.627 | 0.358 | 0.0019 | 0.0043 | -0.028 | 6 |
| 8 | 0.141 | 0.465 | 0.384 | 0.621 | 0.359 | 0.0028 | 0.0065 | -0.026 | 4 |
| 9 | 0.414 | 0.465 | 0.091 | 0.597 | 0.334 | 0.0049 | 0.0100 | 0.063 | 28 |
| 10 | 0.058 | 0.408 | 0.505 | 0.630 | 0.366 | 0.0021 | 0.0046 | 0.002 | 4 |

### welt_2025_core_01

| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.010 | 0.465 | 0.515 | 0.632 | 0.354 | 0.0011 | 0.0021 | 0.004 | 0 |
| 2 | 0.010 | 0.434 | 0.556 | 0.635 | 0.364 | 0.0014 | 0.0026 | 0.004 | 2 |
| 3 | 0.030 | 0.384 | 0.566 | 0.632 | 0.356 | 0.0014 | 0.0028 | 0.028 | 4 |
| 4 | 0.051 | 0.414 | 0.515 | 0.635 | 0.367 | 0.0016 | 0.0033 | 0.050 | 0 |
| 5 | 0.030 | 0.475 | 0.495 | 0.629 | 0.352 | 0.0016 | 0.0031 | 0.006 | 4 |
| 6 | 0.030 | 0.384 | 0.586 | 0.635 | 0.367 | 0.0014 | 0.0025 | -0.005 | 0 |
| 7 | 0.040 | 0.374 | 0.586 | 0.638 | 0.374 | 0.0015 | 0.0027 | 0.023 | 2 |
| 8 | 0.051 | 0.495 | 0.444 | 0.631 | 0.362 | 0.0017 | 0.0033 | 0.030 | 4 |
| 9 | 0.020 | 0.343 | 0.636 | 0.638 | 0.366 | 0.0010 | 0.0020 | -0.004 | 4 |
| 10 | 0.019 | 0.427 | 0.544 | 0.633 | 0.351 | 0.0010 | 0.0018 | -0.004 | 4 |

### welt_2025_late_shift_01

| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.051 | 0.475 | 0.465 | 0.625 | 0.351 | 0.0020 | 0.0035 | 0.011 | 6 |
| 2 | 0.030 | 0.293 | 0.667 | 0.638 | 0.372 | 0.0015 | 0.0033 | -0.024 | 0 |
| 3 | 0.051 | 0.374 | 0.576 | 0.632 | 0.358 | 0.0018 | 0.0033 | 0.008 | 4 |
| 4 | 0.010 | 0.404 | 0.586 | 0.639 | 0.365 | 0.0013 | 0.0026 | 0.024 | 2 |
| 5 | 0.091 | 0.465 | 0.434 | 0.631 | 0.373 | 0.0020 | 0.0040 | 0.001 | 0 |
| 6 | 0.101 | 0.495 | 0.394 | 0.623 | 0.341 | 0.0021 | 0.0037 | 0.033 | 8 |
| 7 | 0.010 | 0.404 | 0.586 | 0.640 | 0.366 | 0.0012 | 0.0024 | -0.006 | 0 |
| 8 | 0.010 | 0.374 | 0.596 | 0.636 | 0.367 | 0.0016 | 0.0029 | -0.003 | 0 |
| 9 | 0.020 | 0.434 | 0.535 | 0.636 | 0.363 | 0.0011 | 0.0022 | -0.010 | 0 |
| 10 | 0.000 | 0.359 | 0.631 | 0.640 | 0.363 | 0.0010 | 0.0020 | -0.002 | 0 |

## Befund

Der Stress-Gegenpol entsteht in den bisherigen Läufen nicht durch ein einzelnes Merkmal.
Er zeigt eine Kopplung aus höherer Rohweltbewegung, größerer Range, erhöhter Kipp-/Spannungswirkung, niedrigerer Rekopplung und mehr Episodenmemory.

Fachlich gelesen heißt das: MINI_DIO reagiert nicht nur auf Bewegung, sondern auf eine Belastungskombination aus Weltunruhe und Innenfeld-Rekopplungsverlust.

Die Diagnose bleibt passiv. Sie beschreibt, welche Abschnitte Last tragen; sie entscheidet nicht, was MINI_DIO tun soll.

## Wie es weitergeht

Als nächstes sollte eine neue Stresswelt gegen diese Abschnittsmerkmale geprüft werden. Entscheidend ist, ob der Stress-Gegenpol wieder aus derselben Kombination entsteht oder ob ein anderer Belastungstyp sichtbar wird.
