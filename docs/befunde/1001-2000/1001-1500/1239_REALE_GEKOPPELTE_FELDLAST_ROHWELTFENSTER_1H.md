# Reale gekoppelte Feldlast Rohweltfenster 1h

## Grundfrage

Sind reale `gekoppelte_feldlast`-/Rand-Kipp-Fenster eher an Bewegungsbruch, Expansion oder Rekopplungsversuch gebunden?

Diese Diagnose verbindet reale Rand/Kipp-Segmente mit einem kleinen OHLCV-Fenster um den Segmentmittelpunkt. Sie ist passiv und erzeugt keine Runtime-Regel.

## Bewegungsarten

- `bewegungsbruch`: `80`

## Rollenfolge um Rand/Kipp

Vorherige Rolle:
- `zentrum_stabil`: `45`
- `rekopplungsnaehe`: `19`
- `offene_variante`: `16`

Naechste Rolle:
- `offene_variante`: `73`
- `rekopplungsnaehe`: `5`
- `zentrum_stabil`: `2`

Hauefigste Sequenzen:
- `zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante`: `39`
- `rekopplungsnaehe -> spannungsrand_kippnaehe -> offene_variante`: `18`
- `offene_variante -> spannungsrand_kippnaehe -> offene_variante`: `16`
- `zentrum_stabil -> spannungsrand_kippnaehe -> rekopplungsnaehe`: `4`
- `zentrum_stabil -> spannungsrand_kippnaehe -> zentrum_stabil`: `2`
- `rekopplungsnaehe -> spannungsrand_kippnaehe -> rekopplungsnaehe`: `1`

## Staerkste Fenster

| Welt | Ticks | Lautheit | Rohfeld | Schaerfe | Rekopplung | Strain | Return | Range | Expansion | Richtung | Klasse |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SOL_STRESS_1H | 3285-3285 | 0.9257 | 0.5232 | 0.6259 | 0.5562 | 0.3286 | +0.02639 | 0.11991 | 5.811 | 0.014 | bewegungsbruch |
| BTC_QUIET_1H | 1928-1928 | 0.9158 | 0.5270 | 0.5919 | 0.5605 | 0.3162 | +0.10412 | 0.11373 | 3.403 | 0.200 | bewegungsbruch |
| SOL_STRESS_1H | 2810-2810 | 0.9060 | 0.5195 | 0.7049 | 0.5719 | 0.3062 | -0.08314 | 0.12055 | 8.877 | 0.171 | bewegungsbruch |
| SOL_STRESS_1H | 3057-3057 | 0.9059 | 0.5095 | 0.5862 | 0.5451 | 0.3313 | -0.04934 | 0.16428 | 6.210 | 0.000 | bewegungsbruch |
| SOL_STRESS_1H | 2924-2924 | 0.9036 | 0.5098 | 0.5289 | 0.5905 | 0.2838 | -0.06835 | 0.10463 | 3.810 | 0.000 | bewegungsbruch |
| BTC_STRESS_1H | 2391-2391 | 0.9019 | 0.5074 | 0.4470 | 0.5700 | 0.3017 | +0.06995 | 0.09042 | 5.313 | 0.029 | bewegungsbruch |
| SOL_QUIET_1H | 810-810 | 0.8960 | 0.5113 | 0.6991 | 0.5486 | 0.3297 | -0.08314 | 0.12055 | 8.877 | 0.171 | bewegungsbruch |
| SOL_QUIET_1H | 1057-1057 | 0.8959 | 0.5018 | 0.5826 | 0.5476 | 0.3277 | -0.04934 | 0.16428 | 6.210 | 0.000 | bewegungsbruch |
| SOL_QUIET_1H | 2757-2757 | 0.8932 | 0.5073 | 0.5796 | 0.5427 | 0.3352 | -0.09457 | 0.13438 | 3.598 | 0.143 | bewegungsbruch |
| SOL_QUIET_1H | 924-924 | 0.8928 | 0.5008 | 0.5162 | 0.5671 | 0.3085 | -0.06835 | 0.10463 | 3.810 | 0.000 | bewegungsbruch |
| BTC_STRESS_1H | 1257-1257 | 0.8909 | 0.5044 | 0.5406 | 0.5670 | 0.3092 | -0.06517 | 0.09695 | 4.652 | 0.057 | bewegungsbruch |
| BTC_STRESS_1H | 2930-2930 | 0.8882 | 0.5086 | 0.5975 | 0.5652 | 0.3111 | +0.09249 | 0.13868 | 3.344 | 0.086 | bewegungsbruch |
| BTC_QUIET_1H | 3007-3007 | 0.8808 | 0.4975 | 0.5333 | 0.5425 | 0.3347 | -0.06517 | 0.09695 | 4.652 | 0.057 | bewegungsbruch |
| BTC_STRESS_1H | 698-698 | 0.8779 | 0.4972 | 0.5060 | 0.5391 | 0.3379 | -0.08647 | 0.21516 | 4.175 | 0.029 | bewegungsbruch |
| SOL_STRESS_1H | 1466-1466 | 0.8778 | 0.4927 | 0.6504 | 0.5553 | 0.3194 | -0.19289 | 0.34711 | 5.707 | 0.171 | bewegungsbruch |
| BTC_QUIET_1H | 384-384 | 0.8773 | 0.4917 | 0.5090 | 0.5433 | 0.3324 | -0.00931 | 0.05332 | 5.898 | 0.057 | bewegungsbruch |

## Ableitung

Wenn `expansion_impuls` dominiert, ist reale Rand/Kipp-Naehe eher an gerichtete starke Weltbewegung gebunden.

Wenn `bewegungsbruch` dominiert, ist sie eher an Richtungsbruch oder instabile Umordnung gebunden.

Wenn `rekopplungsversuch` dominiert, waere Rand/Kipp eher ein kurzer Zustand vor Rueckbindung.
