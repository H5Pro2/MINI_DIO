# Befund 1212 - Reale Hochlast-Rohwelt-Ruecklesung

## Grundfrage

Welche reale Weltform steht vor Hochlast-Offenheit und welche vor Hochlast-Randnaehe?

Diese Diagnose bleibt passiv. Sie liest nur zurueck, welche Rohwelt- und Sinneswerte vor bestimmten Feldrollen auftreten.

## Hochlast-Rollen

| Welt | Rolle | Ereignisse | Rohfeld | Adaptfeld | Lautheit | Schaerfe | Druck | Rekopplung | Strain | abs Return | Range | Volumenwechsel | Richtungswechsel | Fenster-Range | Fenster-Richtung |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | offene_variante | 161 | 0.2702 | 0.2220 | 0.4767 | 0.6211 | 0.2154 | 0.6447 | 0.2075 | 0.002321 | 0.005002 | 0.7137 | 0.4596 | 0.030903 | 0.1686 |
| SOL_2024_5M | spannungsrand_kippnaehe | 39 | 0.3856 | 0.3021 | 0.6754 | 0.5682 | 0.3087 | 0.5849 | 0.2804 | 0.010443 | 0.015108 | 0.8775 | 0.2821 | 0.051873 | 0.1280 |
| BTC_2024_5M | offene_variante | 165 | 0.2720 | 0.2236 | 0.4777 | 0.6309 | 0.2166 | 0.6478 | 0.2031 | 0.001169 | 0.002029 | 0.5116 | 0.5273 | 0.012461 | 0.1522 |
| BTC_2024_5M | spannungsrand_kippnaehe | 35 | 0.3968 | 0.3116 | 0.6973 | 0.6027 | 0.3121 | 0.5863 | 0.2808 | 0.002098 | 0.003739 | 1.4440 | 0.3714 | 0.025611 | 0.1777 |
| KAS_2024_5M | offene_variante | 162 | 0.2729 | 0.2242 | 0.4794 | 0.6263 | 0.2170 | 0.6454 | 0.2050 | 0.002919 | 0.005588 | 0.8571 | 0.4815 | 0.032593 | 0.1555 |
| KAS_2024_5M | spannungsrand_kippnaehe | 38 | 0.3837 | 0.3002 | 0.6708 | 0.5407 | 0.3065 | 0.5880 | 0.2753 | 0.012284 | 0.016534 | 0.6764 | 0.4211 | 0.072081 | 0.1595 |
| PAXG_2024_5M | offene_variante | 164 | 0.2806 | 0.2296 | 0.4842 | 0.6203 | 0.2255 | 0.6535 | 0.2037 | 0.000521 | 0.001121 | 34.2853 | 0.2073 | 0.003914 | 0.1300 |
| PAXG_2024_5M | rekopplungsnaehe | 3 | 0.2494 | 0.2070 | 0.4152 | 0.6193 | 0.2007 | 0.7043 | 0.1717 | 0.000827 | 0.000827 | 3.3608 | 0.6667 | 0.004301 | 0.0613 |
| PAXG_2024_5M | spannungsrand_kippnaehe | 33 | 0.4094 | 0.3200 | 0.7122 | 0.5821 | 0.3250 | 0.5900 | 0.2777 | 0.000299 | 0.000523 | 3.7194 | 0.1818 | 0.006127 | 0.1153 |

## Befund

- Staerkste Hochlast-Offenheit: `BTC_2024_5M` mit `165` Ereignissen.
- Staerkste Hochlast-Randnaehe: `SOL_2024_5M` mit `39` Ereignissen.
- Offenheit tritt in den Hochlastfenstern haeufiger auf als Rand/Kipp.
- Rand/Kipp ist nicht einfach die lauteste oder bewegteste Stelle, sondern eine engere Kopplung aus Rohaufnahme, Feldspannung und schwacherer Rekopplung.
- Damit bleibt die zentrale Lesart: reale Weltspannung erzeugt zuerst Uebergangsraum; Randnaehe ist ein speziellerer Zustand.

## Beispiele

| Welt | Rolle | Tick | Familie | Rohfeld | Lautheit | Schaerfe | Rekopplung | Strain | Fenster-Return | Fenster-Range |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_5M | offene_variante | 1871 | dio_1r19 | 0.4329 | 0.7235 | 0.5083 | 0.6314 | 0.2246 | -0.000992 | 0.002976 |
| PAXG_2024_5M | offene_variante | 1531 | dio_1r19 | 0.4307 | 0.7365 | 0.6016 | 0.6223 | 0.2356 | 0.001487 | 0.001983 |
| PAXG_2024_5M | offene_variante | 1568 | dio_00u2 | 0.4298 | 0.7259 | 0.4337 | 0.6570 | 0.2277 | 0.000000 | 0.001485 |
| BTC_2024_5M | offene_variante | 1682 | dio_1clq | 0.4234 | 0.7351 | 0.5991 | 0.6122 | 0.2487 | -0.003646 | 0.008532 |
| KAS_2024_5M | offene_variante | 185 | dio_0zac | 0.4198 | 0.7216 | 0.7413 | 0.6244 | 0.2362 | -0.000801 | 0.018594 |
| KAS_2024_5M | offene_variante | 281 | dio_0zac | 0.4131 | 0.7166 | 0.6528 | 0.6195 | 0.2458 | 0.028636 | 0.036793 |
| BTC_2024_5M | offene_variante | 1116 | dio_0fta | 0.4012 | 0.6970 | 0.2828 | 0.6058 | 0.2472 | 0.010792 | 0.018179 |
| KAS_2024_5M | offene_variante | 1503 | dio_0zac | 0.3989 | 0.6945 | 0.6615 | 0.6222 | 0.2480 | -0.026423 | 0.040515 |
| BTC_2024_5M | offene_variante | 561 | dio_05vd | 0.3966 | 0.6778 | 0.3841 | 0.6075 | 0.2439 | -0.002494 | 0.011019 |
| PAXG_2024_5M | offene_variante | 1173 | dio_04z8 | 0.3927 | 0.6708 | 0.7349 | 0.6147 | 0.2423 | 0.001979 | 0.002969 |
| BTC_2024_5M | offene_variante | 1476 | dio_17rn | 0.3879 | 0.6743 | 0.6229 | 0.6230 | 0.2344 | -0.000899 | 0.004687 |
| BTC_2024_5M | offene_variante | 1961 | dio_03yt | 0.3876 | 0.6724 | 0.6773 | 0.6270 | 0.2341 | 0.001619 | 0.005183 |
| BTC_2024_5M | offene_variante | 1165 | dio_14fv | 0.3863 | 0.6589 | 0.5042 | 0.6054 | 0.2482 | -0.014232 | 0.041498 |
| BTC_2024_5M | offene_variante | 1188 | dio_0cks | 0.3846 | 0.6776 | 0.4167 | 0.6132 | 0.2385 | 0.002057 | 0.016073 |
| KAS_2024_5M | offene_variante | 696 | dio_13l3 | 0.3841 | 0.6455 | 0.5213 | 0.6139 | 0.2379 | 0.001368 | 0.015991 |
| PAXG_2024_5M | offene_variante | 1422 | dio_09yl | 0.3838 | 0.6543 | 0.7446 | 0.6334 | 0.2285 | 0.000495 | 0.003962 |
| PAXG_2024_5M | offene_variante | 1819 | dio_1of5 | 0.3802 | 0.6539 | 0.6036 | 0.6355 | 0.2200 | -0.001982 | 0.002973 |
| SOL_2024_5M | offene_variante | 1886 | dio_1bmy | 0.3784 | 0.6573 | 0.7481 | 0.6300 | 0.2358 | 0.029967 | 0.033699 |
| PAXG_2024_5M | offene_variante | 1283 | dio_17rn | 0.3775 | 0.6591 | 0.5942 | 0.6490 | 0.2411 | -0.002470 | 0.003458 |
| PAXG_2024_5M | offene_variante | 1227 | dio_13l3 | 0.3768 | 0.6300 | 0.5199 | 0.6406 | 0.2158 | -0.001481 | 0.003951 |
| SOL_2024_5M | offene_variante | 1878 | dio_1pol | 0.3755 | 0.6659 | 0.5478 | 0.6089 | 0.2488 | 0.019504 | 0.028938 |
| PAXG_2024_5M | offene_variante | 1810 | dio_0seb | 0.3744 | 0.6586 | 0.7097 | 0.6151 | 0.2489 | -0.000496 | 0.002480 |
| BTC_2024_5M | offene_variante | 30 | dio_1of5 | 0.3743 | 0.6487 | 0.6182 | 0.6062 | 0.2492 | -0.001499 | 0.008369 |
| KAS_2024_5M | offene_variante | 1152 | dio_0ofe | 0.3732 | 0.6777 | 0.4667 | 0.6096 | 0.2479 | 0.014784 | 0.027688 |

## Ableitung

Die reale Ruecklesung bestaetigt die Hierarchie der Pruefung:

1. Grundfrage: Welche Weltform erzeugt Felduebergang oder Randnaehe?
2. Unterpruefung: Hochlastfenster nach Feldrolle trennen.
3. Folgeschritt: konkrete Chartfenster fuer die staerksten offenen und randnahen Beispiele visualisieren.

Wie es weitergeht: Die naechste Pruefung sollte die Beispiel-Ticks als Chartfenster plotten, damit sichtbar wird, ob Offenheit eher aus Richtungswechsel, Verdichtung oder Ton-/Form-Desynchronisation entsteht.
