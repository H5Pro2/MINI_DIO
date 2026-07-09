# Reale gekoppelte Feldlast Rohweltfenster 5m

## Grundfrage

Sind reale `gekoppelte_feldlast`-/Rand-Kipp-Fenster eher an Bewegungsbruch, Expansion oder Rekopplungsversuch gebunden?

Diese Diagnose verbindet reale Rand/Kipp-Segmente mit einem kleinen OHLCV-Fenster um den Segmentmittelpunkt. Sie ist passiv und erzeugt keine Runtime-Regel.

## Bewegungsarten

- `bewegungsbruch`: `80`

## Rollenfolge um Rand/Kipp

Vorherige Rolle:
- `zentrum_stabil`: `43`
- `offene_variante`: `21`
- `rekopplungsnaehe`: `16`

Naechste Rolle:
- `offene_variante`: `71`
- `zentrum_stabil`: `5`
- `rekopplungsnaehe`: `4`

Hauefigste Sequenzen:
- `zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante`: `38`
- `offene_variante -> spannungsrand_kippnaehe -> offene_variante`: `18`
- `rekopplungsnaehe -> spannungsrand_kippnaehe -> offene_variante`: `15`
- `zentrum_stabil -> spannungsrand_kippnaehe -> zentrum_stabil`: `3`
- `zentrum_stabil -> spannungsrand_kippnaehe -> rekopplungsnaehe`: `2`
- `offene_variante -> spannungsrand_kippnaehe -> rekopplungsnaehe`: `2`
- `offene_variante -> spannungsrand_kippnaehe -> zentrum_stabil`: `1`
- `rekopplungsnaehe -> spannungsrand_kippnaehe -> zentrum_stabil`: `1`

## Staerkste Fenster

| Welt | Ticks | Lautheit | Rohfeld | Schaerfe | Rekopplung | Strain | Return | Range | Expansion | Richtung | Klasse |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC_STRESS_CURRENT | 3620-3620 | 0.9709 | 0.5513 | 0.6044 | 0.5489 | 0.3364 | +0.03447 | 0.05890 | 4.486 | 0.171 | bewegungsbruch |
| BTC_STRESS_CURRENT | 3510-3510 | 0.9580 | 0.5370 | 0.5027 | 0.5554 | 0.3246 | +0.03115 | 0.04439 | 5.480 | 0.114 | bewegungsbruch |
| SOL_STRESS_CURRENT | 1776-1776 | 0.9552 | 0.5537 | 0.6405 | 0.5508 | 0.3302 | -0.01109 | 0.04972 | 5.297 | 0.057 | bewegungsbruch |
| BTC_STRESS_CURRENT | 481-481 | 0.9477 | 0.5417 | 0.5285 | 0.5578 | 0.3187 | +0.02287 | 0.02696 | 4.918 | 0.101 | bewegungsbruch |
| BTC_QUIET_CURRENT | 1555-1555 | 0.9289 | 0.5269 | 0.5125 | 0.5618 | 0.3141 | +0.00224 | 0.01389 | 4.779 | 0.217 | bewegungsbruch |
| SOL_QUIET_CURRENT | 3902-3902 | 0.9277 | 0.5363 | 0.5887 | 0.5589 | 0.3133 | -0.00774 | 0.01090 | 4.765 | 0.043 | bewegungsbruch |
| BTC_QUIET_CURRENT | 3189-3189 | 0.9193 | 0.5446 | 0.7255 | 0.5598 | 0.3178 | -0.00076 | 0.00506 | 5.773 | 0.143 | bewegungsbruch |
| BTC_QUIET_CURRENT | 1338-1338 | 0.9181 | 0.5274 | 0.6189 | 0.5588 | 0.3204 | +0.00142 | 0.00919 | 4.932 | 0.114 | bewegungsbruch |
| BTC_STRESS_CURRENT | 48-48 | 0.9181 | 0.5377 | 0.6882 | 0.5561 | 0.3230 | +0.01286 | 0.02137 | 3.864 | 0.029 | bewegungsbruch |
| SOL_STRESS_CURRENT | 276-276 | 0.9176 | 0.5379 | 0.7165 | 0.5552 | 0.3255 | +0.01911 | 0.05541 | 3.202 | 0.014 | bewegungsbruch |
| SOL_STRESS_CURRENT | 2092-2092 | 0.9121 | 0.5186 | 0.5511 | 0.5627 | 0.3138 | +0.04665 | 0.06939 | 4.224 | 0.114 | bewegungsbruch |
| BTC_QUIET_CURRENT | 1506-1506 | 0.9081 | 0.5189 | 0.4488 | 0.5490 | 0.3237 | -0.00215 | 0.01147 | 8.942 | 0.143 | bewegungsbruch |
| SOL_STRESS_CURRENT | 1795-1795 | 0.9057 | 0.5270 | 0.5939 | 0.5742 | 0.2909 | +0.01295 | 0.05042 | 5.304 | 0.130 | bewegungsbruch |
| BTC_STRESS_CURRENT | 1203-1203 | 0.9022 | 0.5297 | 0.6314 | 0.5622 | 0.3110 | +0.00363 | 0.01351 | 3.436 | 0.000 | bewegungsbruch |
| SOL_QUIET_CURRENT | 2550-2550 | 0.9013 | 0.5279 | 0.7207 | 0.5805 | 0.2871 | -0.00855 | 0.01500 | 3.989 | 0.029 | bewegungsbruch |
| SOL_QUIET_CURRENT | 2664-2664 | 0.9003 | 0.5131 | 0.4954 | 0.5410 | 0.3345 | -0.01542 | 0.02830 | 3.520 | 0.014 | bewegungsbruch |

## Ableitung

Wenn `expansion_impuls` dominiert, ist reale Rand/Kipp-Naehe eher an gerichtete starke Weltbewegung gebunden.

Wenn `bewegungsbruch` dominiert, ist sie eher an Richtungsbruch oder instabile Umordnung gebunden.

Wenn `rekopplungsversuch` dominiert, waere Rand/Kipp eher ein kurzer Zustand vor Rueckbindung.
