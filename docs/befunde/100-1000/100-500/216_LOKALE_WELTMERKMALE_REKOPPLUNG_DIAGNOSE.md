# Lokale Weltmerkmale und Rekopplung - Diagnose

Stand: 2026-06-19 04:57:39

## Zweck

Diese Diagnose legt Rohweltmerkmale neben lokale Rekopplungsrollen.
Sie prueft, welche Weltmerkmale den Uebergang von aktiv-rekoppelnd zu bindend begleiten.

Hierarchie der Pruefung:

1. Grundfrage: Welche Weltmerkmale erzeugen oder begleiten Rekopplungsbindung?
2. Unterpruefung: Drift, Range, Volumenrhythmus, Richtungswechsel und Verdichtung gegen Feldlast/Memory/Rekopplung legen.
3. Folgeschritt: Bewerten, ob Bindung eher aus Weltstruktur, Nachhall oder Feldzustand entsteht.

## Einzelwerte

| Welt | Gruppe | Rolle | Kontrast | Feldlast | Memorylast | Rekopplung | Verdichtung | Drift | avg Range | p95 Range | Richtungswechsel | Persistenz |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| QUIET_2024_REAL | ruhe | reiz_aktiv_rekoppelnd | -0.4875 | 0.0213 | 0.0532 | 0.630744 | 4.0469 | 0.0184 | 0.003683 | 0.008079 | 0.4796 | 0.5204 |
| QUIET_2024_SIDEWAYS | ruhe | reiz_aktiv_rekoppelnd | -0.5529 | 0.0213 | 0.0532 | 0.639653 | 1.0056 | -0.0093 | 0.000980 | 0.001606 | 0.3776 | 0.6224 |
| QUIET_2025_CORE | ruhe | reiz_aktiv_rekoppelnd | -0.4944 | 0.0106 | 0.0319 | 0.628376 | 2.0029 | -0.0017 | 0.001950 | 0.003392 | 0.4694 | 0.5306 |
| QUIET_2025_STRESS | ruhe | reiz_aktiv_rekoppelnd | -0.6129 | 0.0000 | 0.0106 | 0.639352 | 1.8325 | -0.0044 | 0.001911 | 0.003205 | 0.3367 | 0.6633 |
| QUIET_2026_ANCHOR | ruhe | reiz_aktiv_rekoppelnd | -0.5830 | 0.0213 | 0.0532 | 0.639974 | 1.0530 | 0.0000 | 0.000998 | 0.001762 | 0.4082 | 0.5918 |
| AUTO_STRESS_SEGMENT5 | stress | uebergang_bindend | -0.0642 | 0.2151 | 0.2258 | 0.607085 | 11.3986 | 0.0750 | 0.009399 | 0.026740 | 0.3608 | 0.6392 |
| AUTO_STRESS_SEGMENT5_6 | stress | uebergang_bindend | -0.0917 | 0.1719 | 0.2344 | 0.606201 | 8.8606 | 0.1634 | 0.008655 | 0.017579 | 0.4082 | 0.5918 |
| AUTO_STRESS_SEGMENT6 | stress | uebergang_bindend | -0.1357 | 0.1290 | 0.2473 | 0.606419 | 7.8841 | 0.0806 | 0.007911 | 0.015935 | 0.4536 | 0.5464 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | 0.1294 | 0.2660 | 0.2447 | 0.596927 | 17.0762 | 0.2797 | 0.015069 | 0.042703 | 0.4592 | 0.5408 |
| STRESS_2024_REAL | stress | uebergang_bindend | 0.0322 | 0.2340 | 0.2447 | 0.601652 | 16.8929 | -0.1059 | 0.014709 | 0.033383 | 0.4286 | 0.5714 |
| STRESS_2024_SIDEWAYS | stress | reiz_aktiv_rekoppelnd | -0.4669 | 0.0532 | 0.0532 | 0.629551 | 4.6274 | -0.0253 | 0.004247 | 0.009205 | 0.4898 | 0.5102 |
| STRESS_2025_STRESS | stress | last_memory_bindend | 0.1203 | 0.2872 | 0.2234 | 0.594327 | 19.0124 | 0.2532 | 0.013453 | 0.043544 | 0.5204 | 0.4796 |

## Gruppenmittel

### Stress

- Kontrast Bindung-Aktiv: `-0.0681`
- Feldlast: `0.1938`
- Memorylast: `0.2105`
- Weltverdichtung: `12.2503`
- Richtungswechsel: `0.4458`

### Ruhe

- Kontrast Bindung-Aktiv: `-0.5462`
- Feldlast: `0.0149`
- Memorylast: `0.0404`
- Weltverdichtung: `1.9882`
- Richtungswechsel: `0.4143`

## Staerkste Bindung

- `STRESS_2023_TEST4`: Kontrast `0.1294`, Verdichtung `17.0762`, Range `0.015069`, Richtungswechsel `0.4592`
- `STRESS_2025_STRESS`: Kontrast `0.1203`, Verdichtung `19.0124`, Range `0.013453`, Richtungswechsel `0.5204`
- `STRESS_2024_REAL`: Kontrast `0.0322`, Verdichtung `16.8929`, Range `0.014709`, Richtungswechsel `0.4286`
- `AUTO_STRESS_SEGMENT5`: Kontrast `-0.0642`, Verdichtung `11.3986`, Range `0.009399`, Richtungswechsel `0.3608`
- `AUTO_STRESS_SEGMENT5_6`: Kontrast `-0.0917`, Verdichtung `8.8606`, Range `0.008655`, Richtungswechsel `0.4082`

## Staerkste Rohweltverdichtung

- `STRESS_2025_STRESS`: Verdichtung `19.0124`, Rolle `last_memory_bindend`, Kontrast `0.1203`
- `STRESS_2023_TEST4`: Verdichtung `17.0762`, Rolle `last_memory_bindend`, Kontrast `0.1294`
- `STRESS_2024_REAL`: Verdichtung `16.8929`, Rolle `uebergang_bindend`, Kontrast `0.0322`
- `AUTO_STRESS_SEGMENT5`: Verdichtung `11.3986`, Rolle `uebergang_bindend`, Kontrast `-0.0642`
- `AUTO_STRESS_SEGMENT5_6`: Verdichtung `8.8606`, Rolle `uebergang_bindend`, Kontrast `-0.0917`

## Befund

Diese Diagnose ist noch keine Erklaerung, sondern eine Kopplungskarte.
Sie zeigt, ob lokale Bindung mit Rohweltmerkmalen zusammenfaellt oder ob Feldzustand und Memory staerker erklaeren.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Dabei wird bewertet, ob lokale Bindung vor allem durch Verdichtung, Richtungswechsel, Range oder bereits vorhandene Feld-/Memorylage entsteht.
