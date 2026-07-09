# Adaptive Milieu-Familienlagen

Stand: 2026-07-07 18:32:07

## Zweck

Diese Diagnose prueft, ob `milieu_offen` dieselben Familien beruehrt wie gereifte Milieus oder als eigene Varianzschicht getrennt bleibt.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Ist Offenheit eine eigene Schicht oder ein Vorraum gereifter Familien?
2. Unterpruefung: Familien nach `nur_offen`, `nur_gereift` und `offen_und_gereift` trennen.
3. Folgeschritt: Wenn gemeinsame Familien dominieren, offene Milieus als Varianzschicht ueber stabilen Rollen lesen.

## Weltuebersicht

| Welt | Ticks | Familien | Offen+Gereift | Nur offen | Nur gereift | Anteil Offen+Gereift | Offen-Ticks | Gereift-Ticks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_5M | 4994 | 512 | 177 | 72 | 261 | 0.3457 | 2134 | 2841 |
| DOGE_2024_5M | 4994 | 523 | 187 | 76 | 259 | 0.3576 | 2169 | 2813 |
| XRP_2024_5M | 4994 | 529 | 170 | 71 | 288 | 0.3214 | 2114 | 2874 |
| PAXG_2024_5M | 4994 | 474 | 182 | 61 | 231 | 0.3840 | 2190 | 2798 |

## Staerkste Familienlagen

| Welt | Familie | Relation | Gesamt | Offen | Gereift | Offen-Anteil | Gereift-Anteil | Rekopplung | Adaptive Rekopplung | Strain |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_5M | dio_104t | offen_und_gereift | 354 | 26 | 325 | 0.0734 | 0.9181 | 0.7221 | 0.7562 | 0.1494 |
| BTC_2024_5M | dio_155c | offen_und_gereift | 254 | 20 | 232 | 0.0787 | 0.9134 | 0.7163 | 0.7515 | 0.1554 |
| BTC_2024_5M | dio_0m9z | offen_und_gereift | 218 | 89 | 128 | 0.4083 | 0.5872 | 0.7087 | 0.7425 | 0.1643 |
| BTC_2024_5M | dio_0l7p | offen_und_gereift | 212 | 47 | 163 | 0.2217 | 0.7689 | 0.7278 | 0.7639 | 0.1360 |
| BTC_2024_5M | dio_0h9h | offen_und_gereift | 144 | 18 | 126 | 0.1250 | 0.8750 | 0.7252 | 0.7627 | 0.1374 |
| BTC_2024_5M | dio_14wj | offen_und_gereift | 116 | 101 | 14 | 0.8707 | 0.1207 | 0.7315 | 0.7694 | 0.1239 |
| BTC_2024_5M | dio_00ly | offen_und_gereift | 95 | 77 | 18 | 0.8105 | 0.1895 | 0.7221 | 0.7608 | 0.1349 |
| BTC_2024_5M | dio_0oc3 | offen_und_gereift | 93 | 90 | 3 | 0.9677 | 0.0323 | 0.6998 | 0.7371 | 0.1683 |
| BTC_2024_5M | dio_00ja | offen_und_gereift | 80 | 58 | 22 | 0.7250 | 0.2750 | 0.7012 | 0.7354 | 0.1616 |
| BTC_2024_5M | dio_1lsu | offen_und_gereift | 73 | 65 | 8 | 0.8904 | 0.1096 | 0.7128 | 0.7510 | 0.1488 |
| BTC_2024_5M | dio_1ewh | offen_und_gereift | 65 | 55 | 9 | 0.8462 | 0.1385 | 0.7101 | 0.7463 | 0.1475 |
| BTC_2024_5M | dio_06s7 | offen_und_gereift | 64 | 55 | 9 | 0.8594 | 0.1406 | 0.7284 | 0.7684 | 0.1234 |
| BTC_2024_5M | dio_1kpz | offen_und_gereift | 61 | 46 | 15 | 0.7541 | 0.2459 | 0.7272 | 0.7677 | 0.1235 |
| BTC_2024_5M | dio_0obq | offen_und_gereift | 56 | 51 | 5 | 0.9107 | 0.0893 | 0.7042 | 0.7428 | 0.1558 |
| BTC_2024_5M | dio_1q85 | offen_und_gereift | 55 | 49 | 5 | 0.8909 | 0.0909 | 0.7057 | 0.7424 | 0.1587 |
| BTC_2024_5M | dio_06er | offen_und_gereift | 52 | 25 | 27 | 0.4808 | 0.5192 | 0.7312 | 0.7726 | 0.1200 |
| BTC_2024_5M | dio_1u5i | offen_und_gereift | 48 | 43 | 5 | 0.8958 | 0.1042 | 0.7207 | 0.7597 | 0.1303 |
| BTC_2024_5M | dio_05yg | offen_und_gereift | 47 | 36 | 11 | 0.7660 | 0.2340 | 0.6889 | 0.7240 | 0.1755 |
| BTC_2024_5M | dio_09bn | offen_und_gereift | 46 | 34 | 12 | 0.7391 | 0.2609 | 0.7251 | 0.7670 | 0.1269 |
| BTC_2024_5M | dio_0tay | offen_und_gereift | 45 | 23 | 22 | 0.5111 | 0.4889 | 0.7158 | 0.7558 | 0.1405 |
| DOGE_2024_5M | dio_104t | offen_und_gereift | 315 | 43 | 271 | 0.1365 | 0.8603 | 0.7216 | 0.7560 | 0.1496 |
| DOGE_2024_5M | dio_0m9z | offen_und_gereift | 247 | 56 | 190 | 0.2267 | 0.7692 | 0.7090 | 0.7424 | 0.1648 |
| DOGE_2024_5M | dio_155c | offen_und_gereift | 226 | 34 | 191 | 0.1504 | 0.8451 | 0.7153 | 0.7508 | 0.1558 |
| DOGE_2024_5M | dio_0l7p | offen_und_gereift | 200 | 79 | 120 | 0.3950 | 0.6000 | 0.7280 | 0.7641 | 0.1353 |
| DOGE_2024_5M | dio_0h9h | offen_und_gereift | 152 | 26 | 124 | 0.1711 | 0.8158 | 0.7244 | 0.7612 | 0.1389 |
| DOGE_2024_5M | dio_14wj | offen_und_gereift | 105 | 99 | 6 | 0.9429 | 0.0571 | 0.7306 | 0.7688 | 0.1249 |
| DOGE_2024_5M | dio_1lsu | offen_und_gereift | 95 | 84 | 10 | 0.8842 | 0.1053 | 0.7116 | 0.7488 | 0.1505 |
| DOGE_2024_5M | dio_00ly | offen_und_gereift | 90 | 56 | 34 | 0.6222 | 0.3778 | 0.7230 | 0.7616 | 0.1367 |
| DOGE_2024_5M | dio_17ct | offen_und_gereift | 78 | 49 | 29 | 0.6282 | 0.3718 | 0.7166 | 0.7553 | 0.1492 |
| DOGE_2024_5M | dio_00ja | offen_und_gereift | 72 | 67 | 5 | 0.9306 | 0.0694 | 0.7002 | 0.7344 | 0.1619 |
| DOGE_2024_5M | dio_0oc3 | offen_und_gereift | 71 | 57 | 13 | 0.8028 | 0.1831 | 0.6970 | 0.7335 | 0.1685 |
| DOGE_2024_5M | dio_1q85 | offen_und_gereift | 71 | 35 | 36 | 0.4930 | 0.5070 | 0.7064 | 0.7433 | 0.1596 |
| DOGE_2024_5M | dio_1ewh | offen_und_gereift | 66 | 57 | 9 | 0.8636 | 0.1364 | 0.7107 | 0.7479 | 0.1472 |
| DOGE_2024_5M | dio_09bn | offen_und_gereift | 61 | 56 | 5 | 0.9180 | 0.0820 | 0.7269 | 0.7680 | 0.1281 |
| DOGE_2024_5M | dio_0nlj | offen_und_gereift | 61 | 58 | 3 | 0.9508 | 0.0492 | 0.7355 | 0.7773 | 0.1185 |
| DOGE_2024_5M | dio_06s7 | offen_und_gereift | 58 | 53 | 5 | 0.9138 | 0.0862 | 0.7295 | 0.7696 | 0.1224 |
| DOGE_2024_5M | dio_0pz6 | offen_und_gereift | 58 | 50 | 8 | 0.8621 | 0.1379 | 0.7259 | 0.7671 | 0.1292 |
| DOGE_2024_5M | dio_0obq | offen_und_gereift | 56 | 40 | 16 | 0.7143 | 0.2857 | 0.7044 | 0.7430 | 0.1558 |
| DOGE_2024_5M | dio_0tay | offen_und_gereift | 56 | 43 | 13 | 0.7679 | 0.2321 | 0.7162 | 0.7549 | 0.1435 |
| DOGE_2024_5M | dio_1kpz | offen_und_gereift | 54 | 52 | 2 | 0.9630 | 0.0370 | 0.7282 | 0.7689 | 0.1218 |
| XRP_2024_5M | dio_104t | offen_und_gereift | 350 | 28 | 322 | 0.0800 | 0.9200 | 0.7223 | 0.7571 | 0.1484 |
| XRP_2024_5M | dio_155c | offen_und_gereift | 245 | 21 | 224 | 0.0857 | 0.9143 | 0.7157 | 0.7514 | 0.1562 |
| XRP_2024_5M | dio_0m9z | offen_und_gereift | 238 | 131 | 107 | 0.5504 | 0.4496 | 0.7101 | 0.7439 | 0.1639 |
| XRP_2024_5M | dio_0l7p | offen_und_gereift | 207 | 91 | 115 | 0.4396 | 0.5556 | 0.7290 | 0.7654 | 0.1349 |
| XRP_2024_5M | dio_14wj | offen_und_gereift | 127 | 54 | 73 | 0.4252 | 0.5748 | 0.7300 | 0.7678 | 0.1261 |
| XRP_2024_5M | dio_0h9h | offen_und_gereift | 125 | 21 | 104 | 0.1680 | 0.8320 | 0.7234 | 0.7613 | 0.1373 |
| XRP_2024_5M | dio_00ly | offen_und_gereift | 79 | 73 | 6 | 0.9241 | 0.0759 | 0.7224 | 0.7618 | 0.1338 |
| XRP_2024_5M | dio_0oc3 | offen_und_gereift | 74 | 66 | 8 | 0.8919 | 0.1081 | 0.6977 | 0.7351 | 0.1678 |
| XRP_2024_5M | dio_1q85 | offen_und_gereift | 71 | 55 | 16 | 0.7746 | 0.2254 | 0.7062 | 0.7427 | 0.1610 |
| XRP_2024_5M | dio_17ct | offen_und_gereift | 69 | 51 | 18 | 0.7391 | 0.2609 | 0.7156 | 0.7547 | 0.1481 |
| XRP_2024_5M | dio_06er | offen_und_gereift | 67 | 55 | 11 | 0.8209 | 0.1642 | 0.7345 | 0.7745 | 0.1225 |
| XRP_2024_5M | dio_1kpz | offen_und_gereift | 66 | 36 | 30 | 0.5455 | 0.4545 | 0.7283 | 0.7687 | 0.1228 |
| XRP_2024_5M | dio_0pz6 | offen_und_gereift | 65 | 59 | 6 | 0.9077 | 0.0923 | 0.7253 | 0.7661 | 0.1315 |
| XRP_2024_5M | dio_1lsu | offen_und_gereift | 65 | 41 | 24 | 0.6308 | 0.3692 | 0.7092 | 0.7478 | 0.1502 |
| XRP_2024_5M | dio_1ewh | offen_und_gereift | 64 | 58 | 6 | 0.9062 | 0.0938 | 0.7090 | 0.7461 | 0.1492 |
| XRP_2024_5M | dio_0dd2 | offen_und_gereift | 62 | 22 | 39 | 0.3548 | 0.6290 | 0.7242 | 0.7637 | 0.1340 |
| XRP_2024_5M | dio_00ja | offen_und_gereift | 61 | 49 | 12 | 0.8033 | 0.1967 | 0.7000 | 0.7345 | 0.1618 |
| XRP_2024_5M | dio_06s7 | offen_und_gereift | 53 | 49 | 4 | 0.9245 | 0.0755 | 0.7261 | 0.7669 | 0.1230 |
| XRP_2024_5M | dio_0z9t | offen_und_gereift | 53 | 32 | 21 | 0.6038 | 0.3962 | 0.7138 | 0.7538 | 0.1475 |
| XRP_2024_5M | dio_0tay | offen_und_gereift | 52 | 46 | 6 | 0.8846 | 0.1154 | 0.7167 | 0.7559 | 0.1421 |
| PAXG_2024_5M | dio_104t | offen_und_gereift | 290 | 38 | 252 | 0.1310 | 0.8690 | 0.7274 | 0.7629 | 0.1478 |
| PAXG_2024_5M | dio_14wj | offen_und_gereift | 257 | 39 | 218 | 0.1518 | 0.8482 | 0.7425 | 0.7793 | 0.1305 |
| PAXG_2024_5M | dio_0l7p | offen_und_gereift | 172 | 67 | 105 | 0.3895 | 0.6105 | 0.7311 | 0.7683 | 0.1352 |
| PAXG_2024_5M | dio_155c | offen_und_gereift | 146 | 26 | 120 | 0.1781 | 0.8219 | 0.7202 | 0.7571 | 0.1531 |
| PAXG_2024_5M | dio_0m9z | offen_und_gereift | 143 | 92 | 51 | 0.6434 | 0.3566 | 0.7115 | 0.7466 | 0.1631 |
| PAXG_2024_5M | dio_0h9h | offen_und_gereift | 123 | 45 | 77 | 0.3659 | 0.6260 | 0.7265 | 0.7644 | 0.1380 |
| PAXG_2024_5M | dio_1fll | offen_und_gereift | 108 | 59 | 49 | 0.5463 | 0.4537 | 0.7544 | 0.7944 | 0.1149 |
| PAXG_2024_5M | dio_1u5i | offen_und_gereift | 101 | 80 | 21 | 0.7921 | 0.2079 | 0.7292 | 0.7665 | 0.1319 |
| PAXG_2024_5M | dio_00ja | offen_und_gereift | 87 | 70 | 17 | 0.8046 | 0.1954 | 0.7056 | 0.7405 | 0.1596 |
| PAXG_2024_5M | dio_00ly | offen_und_gereift | 84 | 78 | 6 | 0.9286 | 0.0714 | 0.7260 | 0.7650 | 0.1358 |
| PAXG_2024_5M | dio_06er | offen_und_gereift | 83 | 68 | 15 | 0.8193 | 0.1807 | 0.7436 | 0.7850 | 0.1224 |
| PAXG_2024_5M | dio_1lsu | offen_und_gereift | 76 | 54 | 22 | 0.7105 | 0.2895 | 0.7187 | 0.7569 | 0.1532 |
| PAXG_2024_5M | dio_1gp2 | offen_und_gereift | 66 | 61 | 5 | 0.9242 | 0.0758 | 0.7117 | 0.7485 | 0.1475 |
| PAXG_2024_5M | dio_0oc3 | offen_und_gereift | 63 | 52 | 11 | 0.8254 | 0.1746 | 0.7017 | 0.7396 | 0.1694 |
| PAXG_2024_5M | dio_0z9t | offen_und_gereift | 63 | 54 | 9 | 0.8571 | 0.1429 | 0.7217 | 0.7610 | 0.1475 |
| PAXG_2024_5M | dio_1ewh | offen_und_gereift | 62 | 38 | 24 | 0.6129 | 0.3871 | 0.7108 | 0.7483 | 0.1486 |
| PAXG_2024_5M | dio_06s7 | offen_und_gereift | 61 | 54 | 7 | 0.8852 | 0.1148 | 0.7305 | 0.7708 | 0.1267 |
| PAXG_2024_5M | dio_1kpz | offen_und_gereift | 61 | 35 | 26 | 0.5738 | 0.4262 | 0.7299 | 0.7698 | 0.1255 |
| PAXG_2024_5M | dio_0g2r | offen_und_gereift | 59 | 47 | 12 | 0.7966 | 0.2034 | 0.7130 | 0.7508 | 0.1467 |
| PAXG_2024_5M | dio_0dd2 | offen_und_gereift | 53 | 34 | 19 | 0.6415 | 0.3585 | 0.7308 | 0.7723 | 0.1326 |

## Lesung

Wenn dieselbe Familie sowohl offen als auch gereift erscheint, ist Offenheit keine isolierte Stoerung.
Sie wirkt dann eher wie eine wechselnde Varianzschicht ueber einer wiederkehrenden Rollenfamilie.

Wenn Familien nur offen erscheinen, bleibt die Lage dagegen noch ungebunden oder jung.

## Grenze

Diese Diagnose beschreibt nur passive Milieu-Schichtung.
Sie erzeugt keine Handlung und bewertet Offenheit nicht als Fehler.

## Wie es weitergeht

Als naechstes wird geprueft, ob gemeinsame Offen/Gereift-Familien in spaeteren Segmenten stabiler werden oder ob sie zwischen Offenheit und Reifung pendeln.
