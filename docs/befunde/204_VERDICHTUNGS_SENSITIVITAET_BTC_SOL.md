# Verdichtungs-Sensitivitaet

Stand: 2026-06-18 23:24:53

## Zweck

Diese Diagnose misst passiv, wie empfindlich eine Welt auf zeitliche Verdichtung reagiert.
Sie ist keine Regel, kein Gate und keine Handlungsempfehlung.

Hierarchie der Pruefung:

1. Grundfrage: Wie stark veraendert Zeitverdichtung die MCM-Feldwirkung?
2. Unterpruefung: Steigen Lautstaerke, Strain und Memory proportional oder ueberproportional?
3. Folgeschritt: Unterscheiden, ob eine Welt nur lauter wird oder ob das Innenfeld ueberempfindlich reagiert.

## Einzelwerte

| Welt | Minuten | Lautstaerke | Strain | Memory | Rekopplung | Tragqualitaet | field_carried_ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_5m | 5 | 2.453 | 42 | 63 | 0.636577 | 0.366108 | 0.9789 |
| BTC_2024_15m | 15 | 4.622 | 83 | 105 | 0.631196 | 0.362364 | 0.9584 |
| BTC_2024_30m | 30 | 5.741 | 129 | 179 | 0.626156 | 0.359372 | 0.9353 |
| BTC_2024_1h | 60 | 9.779 | 277 | 329 | 0.610376 | 0.345005 | 0.8611 |
| BTC_2025_5m | 5 | 1.730 | 44 | 87 | 0.638380 | 0.368524 | 0.9779 |
| BTC_2025_15m | 15 | 4.170 | 79 | 125 | 0.631429 | 0.363392 | 0.9604 |
| BTC_2025_30m | 30 | 6.057 | 132 | 167 | 0.623087 | 0.355382 | 0.9338 |
| BTC_2025_1h | 60 | 9.321 | 282 | 347 | 0.611240 | 0.347018 | 0.8586 |
| SOL_2024_5m | 5 | 5.735 | 105 | 149 | 0.622776 | 0.358038 | 0.9473 |
| SOL_2024_15m | 15 | 9.731 | 266 | 309 | 0.606542 | 0.343678 | 0.8666 |
| SOL_2024_30m | 30 | 11.939 | 365 | 441 | 0.600205 | 0.341420 | 0.8170 |
| SOL_2024_1h | 60 | 18.874 | 630 | 643 | 0.587027 | 0.333433 | 0.6841 |
| SOL_2025_5m | 5 | 2.639 | 28 | 55 | 0.636504 | 0.365647 | 0.9860 |
| SOL_2025_15m | 15 | 9.769 | 218 | 247 | 0.615512 | 0.351537 | 0.8907 |
| SOL_2025_30m | 30 | 13.461 | 402 | 434 | 0.600912 | 0.343351 | 0.7984 |
| SOL_2025_1h | 60 | 18.005 | 587 | 591 | 0.589067 | 0.335489 | 0.7056 |

## Verdichtungs-Schritte

| Gruppe | Schritt | Lautstaerke-Delta | Strain-Delta | Memory-Delta | Rekopplungs-Delta | Strain/Lautstaerke-Delta | Memory/Lautstaerke-Delta |
|---|---|---:|---:|---:|---:|---:|---:|
| BTC_2024 | 5m->15m | 2.169 | 41 | 42 | -0.005381 | 18.906 | 19.367 |
| BTC_2024 | 15m->30m | 1.119 | 46 | 74 | -0.005040 | 41.109 | 66.132 |
| BTC_2024 | 30m->1h | 4.038 | 148 | 150 | -0.015780 | 36.652 | 37.147 |
| BTC_2025 | 5m->15m | 2.440 | 35 | 38 | -0.006951 | 14.344 | 15.573 |
| BTC_2025 | 15m->30m | 1.887 | 53 | 42 | -0.008342 | 28.090 | 22.260 |
| BTC_2025 | 30m->1h | 3.265 | 150 | 180 | -0.011847 | 45.948 | 55.137 |
| SOL_2024 | 5m->15m | 3.995 | 161 | 160 | -0.016234 | 40.296 | 40.046 |
| SOL_2024 | 15m->30m | 2.208 | 99 | 132 | -0.006337 | 44.830 | 59.773 |
| SOL_2024 | 30m->1h | 6.935 | 265 | 202 | -0.013178 | 38.211 | 29.127 |
| SOL_2025 | 5m->15m | 7.130 | 190 | 192 | -0.020992 | 26.648 | 26.929 |
| SOL_2025 | 15m->30m | 3.692 | 184 | 187 | -0.014600 | 49.837 | 50.650 |
| SOL_2025 | 30m->1h | 4.544 | 185 | 157 | -0.011845 | 40.717 | 34.554 |

## Jahresprofile

### BTC 2024

- Lautstaerke 5m->1h: `7.326`
- Strain 5m->1h: `235`
- Memory 5m->1h: `266`
- Rekopplung 5m->1h: `-0.026201`
- Strain pro Lautstaerke-Delta: `32.079`

### BTC 2025

- Lautstaerke 5m->1h: `7.591`
- Strain 5m->1h: `238`
- Memory 5m->1h: `260`
- Rekopplung 5m->1h: `-0.027140`
- Strain pro Lautstaerke-Delta: `31.351`

### SOL 2024

- Lautstaerke 5m->1h: `13.139`
- Strain 5m->1h: `525`
- Memory 5m->1h: `494`
- Rekopplung 5m->1h: `-0.035749`
- Strain pro Lautstaerke-Delta: `39.957`

### SOL 2025

- Lautstaerke 5m->1h: `15.366`
- Strain 5m->1h: `559`
- Memory 5m->1h: `536`
- Rekopplung 5m->1h: `-0.047437`
- Strain pro Lautstaerke-Delta: `36.380`

## Befund

Verdichtungs-Sensitivitaet beschreibt, wie stark das Innenfeld auf groessere Weltpakete reagiert.
Eine Welt kann absolut laut sein, aber proportional gut getragen werden. Eine andere Welt kann bei aehnlicher Lautstaerke schneller in Strain und Memorylast kippen.

## Wie es weitergeht

Als naechstes sollte diese Diagnose in die Forschungsuebersicht aufgenommen werden.
Danach koennen weitere Assets geprueft werden, um zu sehen, ob BTC und SOL zwei Extreme oder nur zwei Punkte auf einer groesseren MCM-Weltkarte sind.
