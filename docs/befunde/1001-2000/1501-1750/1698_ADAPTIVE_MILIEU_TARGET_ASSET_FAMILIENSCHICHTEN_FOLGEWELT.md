# Adaptive Milieu-Familienlagen

Stand: 2026-07-07 18:32:08

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
| BTC_2024_5M_FOLLOW | 4994 | 503 | 177 | 54 | 271 | 0.3519 | 1855 | 3132 |
| DOGE_2024_5M_FOLLOW | 4994 | 526 | 159 | 56 | 311 | 0.3023 | 2188 | 2800 |
| XRP_2024_5M_FOLLOW | 4994 | 508 | 174 | 64 | 270 | 0.3425 | 2270 | 2717 |
| PAXG_2024_5M_FOLLOW | 4994 | 364 | 113 | 15 | 235 | 0.3104 | 1931 | 3056 |

## Staerkste Familienlagen

| Welt | Familie | Relation | Gesamt | Offen | Gereift | Offen-Anteil | Gereift-Anteil | Rekopplung | Adaptive Rekopplung | Strain |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_5M_FOLLOW | dio_104t | offen_und_gereift | 362 | 39 | 323 | 0.1077 | 0.8923 | 0.7226 | 0.7572 | 0.1489 |
| BTC_2024_5M_FOLLOW | dio_155c | offen_und_gereift | 241 | 19 | 222 | 0.0788 | 0.9212 | 0.7157 | 0.7516 | 0.1553 |
| BTC_2024_5M_FOLLOW | dio_0m9z | offen_und_gereift | 211 | 48 | 163 | 0.2275 | 0.7725 | 0.7078 | 0.7420 | 0.1654 |
| BTC_2024_5M_FOLLOW | dio_0l7p | offen_und_gereift | 172 | 37 | 134 | 0.2151 | 0.7791 | 0.7277 | 0.7641 | 0.1352 |
| BTC_2024_5M_FOLLOW | dio_0h9h | offen_und_gereift | 131 | 36 | 95 | 0.2748 | 0.7252 | 0.7229 | 0.7612 | 0.1373 |
| BTC_2024_5M_FOLLOW | dio_14wj | offen_und_gereift | 99 | 84 | 15 | 0.8485 | 0.1515 | 0.7301 | 0.7688 | 0.1247 |
| BTC_2024_5M_FOLLOW | dio_00ly | offen_und_gereift | 91 | 71 | 20 | 0.7802 | 0.2198 | 0.7227 | 0.7619 | 0.1348 |
| BTC_2024_5M_FOLLOW | dio_17ct | offen_und_gereift | 86 | 45 | 41 | 0.5233 | 0.4767 | 0.7179 | 0.7563 | 0.1472 |
| BTC_2024_5M_FOLLOW | dio_00ja | offen_und_gereift | 82 | 44 | 38 | 0.5366 | 0.4634 | 0.7018 | 0.7363 | 0.1604 |
| BTC_2024_5M_FOLLOW | dio_0oc3 | offen_und_gereift | 81 | 51 | 30 | 0.6296 | 0.3704 | 0.6983 | 0.7355 | 0.1687 |
| BTC_2024_5M_FOLLOW | dio_0obq | offen_und_gereift | 80 | 58 | 21 | 0.7250 | 0.2625 | 0.7068 | 0.7439 | 0.1562 |
| BTC_2024_5M_FOLLOW | dio_06s7 | offen_und_gereift | 71 | 45 | 26 | 0.6338 | 0.3662 | 0.7289 | 0.7691 | 0.1237 |
| BTC_2024_5M_FOLLOW | dio_1lsu | offen_und_gereift | 69 | 15 | 54 | 0.2174 | 0.7826 | 0.7104 | 0.7489 | 0.1496 |
| BTC_2024_5M_FOLLOW | dio_0pz6 | offen_und_gereift | 68 | 66 | 2 | 0.9706 | 0.0294 | 0.7273 | 0.7682 | 0.1307 |
| BTC_2024_5M_FOLLOW | dio_1kpz | offen_und_gereift | 66 | 46 | 20 | 0.6970 | 0.3030 | 0.7295 | 0.7700 | 0.1212 |
| BTC_2024_5M_FOLLOW | dio_1ewh | offen_und_gereift | 62 | 52 | 10 | 0.8387 | 0.1613 | 0.7095 | 0.7467 | 0.1459 |
| BTC_2024_5M_FOLLOW | dio_0g2r | offen_und_gereift | 53 | 51 | 2 | 0.9623 | 0.0377 | 0.7083 | 0.7458 | 0.1460 |
| BTC_2024_5M_FOLLOW | dio_1gp2 | offen_und_gereift | 51 | 49 | 2 | 0.9608 | 0.0392 | 0.7060 | 0.7433 | 0.1498 |
| BTC_2024_5M_FOLLOW | dio_1q85 | offen_und_gereift | 47 | 37 | 10 | 0.7872 | 0.2128 | 0.7032 | 0.7414 | 0.1588 |
| BTC_2024_5M_FOLLOW | dio_09bn | offen_und_gereift | 46 | 20 | 26 | 0.4348 | 0.5652 | 0.7242 | 0.7654 | 0.1288 |
| DOGE_2024_5M_FOLLOW | dio_104t | offen_und_gereift | 382 | 30 | 352 | 0.0785 | 0.9215 | 0.7223 | 0.7568 | 0.1496 |
| DOGE_2024_5M_FOLLOW | dio_0l7p | offen_und_gereift | 224 | 37 | 187 | 0.1652 | 0.8348 | 0.7292 | 0.7652 | 0.1355 |
| DOGE_2024_5M_FOLLOW | dio_155c | offen_und_gereift | 208 | 31 | 177 | 0.1490 | 0.8510 | 0.7148 | 0.7511 | 0.1549 |
| DOGE_2024_5M_FOLLOW | dio_0m9z | offen_und_gereift | 185 | 156 | 29 | 0.8432 | 0.1568 | 0.7097 | 0.7443 | 0.1613 |
| DOGE_2024_5M_FOLLOW | dio_14wj | offen_und_gereift | 119 | 50 | 69 | 0.4202 | 0.5798 | 0.7313 | 0.7694 | 0.1245 |
| DOGE_2024_5M_FOLLOW | dio_0h9h | offen_und_gereift | 106 | 37 | 69 | 0.3491 | 0.6509 | 0.7220 | 0.7602 | 0.1378 |
| DOGE_2024_5M_FOLLOW | dio_00ly | offen_und_gereift | 102 | 100 | 2 | 0.9804 | 0.0196 | 0.7232 | 0.7615 | 0.1360 |
| DOGE_2024_5M_FOLLOW | dio_17ct | offen_und_gereift | 86 | 76 | 10 | 0.8837 | 0.1163 | 0.7189 | 0.7578 | 0.1453 |
| DOGE_2024_5M_FOLLOW | dio_0oc3 | offen_und_gereift | 84 | 78 | 6 | 0.9286 | 0.0714 | 0.6982 | 0.7353 | 0.1687 |
| DOGE_2024_5M_FOLLOW | dio_0pz6 | offen_und_gereift | 81 | 47 | 34 | 0.5802 | 0.4198 | 0.7275 | 0.7674 | 0.1333 |
| DOGE_2024_5M_FOLLOW | dio_1q85 | offen_und_gereift | 76 | 64 | 12 | 0.8421 | 0.1579 | 0.7082 | 0.7453 | 0.1572 |
| DOGE_2024_5M_FOLLOW | dio_1lsu | offen_und_gereift | 75 | 64 | 11 | 0.8533 | 0.1467 | 0.7104 | 0.7484 | 0.1522 |
| DOGE_2024_5M_FOLLOW | dio_06s7 | offen_und_gereift | 66 | 50 | 16 | 0.7576 | 0.2424 | 0.7291 | 0.7696 | 0.1221 |
| DOGE_2024_5M_FOLLOW | dio_0obq | offen_und_gereift | 65 | 63 | 2 | 0.9692 | 0.0308 | 0.7043 | 0.7427 | 0.1562 |
| DOGE_2024_5M_FOLLOW | dio_0dd2 | offen_und_gereift | 61 | 28 | 33 | 0.4590 | 0.5410 | 0.7240 | 0.7646 | 0.1331 |
| DOGE_2024_5M_FOLLOW | dio_00ja | offen_und_gereift | 58 | 47 | 11 | 0.8103 | 0.1897 | 0.6986 | 0.7332 | 0.1626 |
| DOGE_2024_5M_FOLLOW | dio_1ewh | offen_und_gereift | 57 | 39 | 18 | 0.6842 | 0.3158 | 0.7093 | 0.7471 | 0.1458 |
| DOGE_2024_5M_FOLLOW | dio_0tay | offen_und_gereift | 52 | 38 | 14 | 0.7308 | 0.2692 | 0.7172 | 0.7564 | 0.1407 |
| DOGE_2024_5M_FOLLOW | dio_06er | offen_und_gereift | 51 | 15 | 35 | 0.2941 | 0.6863 | 0.7320 | 0.7725 | 0.1211 |
| DOGE_2024_5M_FOLLOW | dio_09bn | offen_und_gereift | 49 | 25 | 24 | 0.5102 | 0.4898 | 0.7242 | 0.7653 | 0.1293 |
| XRP_2024_5M_FOLLOW | dio_104t | offen_und_gereift | 307 | 40 | 266 | 0.1303 | 0.8664 | 0.7216 | 0.7564 | 0.1486 |
| XRP_2024_5M_FOLLOW | dio_0l7p | offen_und_gereift | 204 | 30 | 174 | 0.1471 | 0.8529 | 0.7280 | 0.7646 | 0.1354 |
| XRP_2024_5M_FOLLOW | dio_155c | offen_und_gereift | 202 | 37 | 165 | 0.1832 | 0.8168 | 0.7152 | 0.7513 | 0.1553 |
| XRP_2024_5M_FOLLOW | dio_0m9z | offen_und_gereift | 200 | 97 | 103 | 0.4850 | 0.5150 | 0.7088 | 0.7432 | 0.1641 |
| XRP_2024_5M_FOLLOW | dio_0h9h | offen_und_gereift | 148 | 27 | 121 | 0.1824 | 0.8176 | 0.7242 | 0.7619 | 0.1375 |
| XRP_2024_5M_FOLLOW | dio_14wj | offen_und_gereift | 120 | 116 | 4 | 0.9667 | 0.0333 | 0.7314 | 0.7698 | 0.1249 |
| XRP_2024_5M_FOLLOW | dio_00ly | offen_und_gereift | 94 | 68 | 26 | 0.7234 | 0.2766 | 0.7228 | 0.7618 | 0.1343 |
| XRP_2024_5M_FOLLOW | dio_17ct | offen_und_gereift | 76 | 65 | 11 | 0.8553 | 0.1447 | 0.7165 | 0.7552 | 0.1476 |
| XRP_2024_5M_FOLLOW | dio_1q85 | offen_und_gereift | 76 | 69 | 7 | 0.9079 | 0.0921 | 0.7071 | 0.7437 | 0.1599 |
| XRP_2024_5M_FOLLOW | dio_00ja | offen_und_gereift | 75 | 60 | 15 | 0.8000 | 0.2000 | 0.7005 | 0.7352 | 0.1613 |
| XRP_2024_5M_FOLLOW | dio_0pz6 | offen_und_gereift | 75 | 54 | 21 | 0.7200 | 0.2800 | 0.7270 | 0.7675 | 0.1304 |
| XRP_2024_5M_FOLLOW | dio_06s7 | offen_und_gereift | 68 | 64 | 4 | 0.9412 | 0.0588 | 0.7290 | 0.7692 | 0.1244 |
| XRP_2024_5M_FOLLOW | dio_1ewh | offen_und_gereift | 67 | 59 | 8 | 0.8806 | 0.1194 | 0.7107 | 0.7478 | 0.1472 |
| XRP_2024_5M_FOLLOW | dio_1kpz | offen_und_gereift | 66 | 38 | 27 | 0.5758 | 0.4091 | 0.7288 | 0.7683 | 0.1224 |
| XRP_2024_5M_FOLLOW | dio_0oc3 | offen_und_gereift | 64 | 61 | 3 | 0.9531 | 0.0469 | 0.6954 | 0.7333 | 0.1684 |
| XRP_2024_5M_FOLLOW | dio_09bn | offen_und_gereift | 61 | 16 | 45 | 0.2623 | 0.7377 | 0.7247 | 0.7655 | 0.1311 |
| XRP_2024_5M_FOLLOW | dio_0tay | offen_und_gereift | 55 | 33 | 21 | 0.6000 | 0.3818 | 0.7184 | 0.7567 | 0.1407 |
| XRP_2024_5M_FOLLOW | dio_0obq | offen_und_gereift | 49 | 27 | 22 | 0.5510 | 0.4490 | 0.7026 | 0.7421 | 0.1561 |
| XRP_2024_5M_FOLLOW | dio_1jc2 | offen_und_gereift | 47 | 42 | 5 | 0.8936 | 0.1064 | 0.7334 | 0.7751 | 0.1156 |
| XRP_2024_5M_FOLLOW | dio_0dd2 | offen_und_gereift | 45 | 40 | 5 | 0.8889 | 0.1111 | 0.7243 | 0.7649 | 0.1357 |
| PAXG_2024_5M_FOLLOW | dio_104t | offen_und_gereift | 350 | 10 | 340 | 0.0286 | 0.9714 | 0.7298 | 0.7655 | 0.1485 |
| PAXG_2024_5M_FOLLOW | dio_14wj | offen_und_gereift | 300 | 31 | 268 | 0.1033 | 0.8933 | 0.7437 | 0.7806 | 0.1291 |
| PAXG_2024_5M_FOLLOW | dio_0m9z | offen_und_gereift | 169 | 56 | 113 | 0.3314 | 0.6686 | 0.7157 | 0.7504 | 0.1632 |
| PAXG_2024_5M_FOLLOW | dio_0l7p | offen_und_gereift | 161 | 65 | 96 | 0.4037 | 0.5963 | 0.7325 | 0.7700 | 0.1352 |
| PAXG_2024_5M_FOLLOW | dio_1u5i | offen_und_gereift | 159 | 103 | 56 | 0.6478 | 0.3522 | 0.7324 | 0.7693 | 0.1326 |
| PAXG_2024_5M_FOLLOW | dio_1fll | offen_und_gereift | 136 | 108 | 28 | 0.7941 | 0.2059 | 0.7530 | 0.7933 | 0.1132 |
| PAXG_2024_5M_FOLLOW | dio_0h9h | offen_und_gereift | 123 | 43 | 80 | 0.3496 | 0.6504 | 0.7283 | 0.7668 | 0.1380 |
| PAXG_2024_5M_FOLLOW | dio_155c | offen_und_gereift | 116 | 52 | 64 | 0.4483 | 0.5517 | 0.7200 | 0.7575 | 0.1530 |
| PAXG_2024_5M_FOLLOW | dio_0oc3 | offen_und_gereift | 111 | 77 | 34 | 0.6937 | 0.3063 | 0.7072 | 0.7440 | 0.1699 |
| PAXG_2024_5M_FOLLOW | dio_00ja | offen_und_gereift | 90 | 46 | 44 | 0.5111 | 0.4889 | 0.7085 | 0.7429 | 0.1599 |
| PAXG_2024_5M_FOLLOW | dio_0obq | offen_und_gereift | 87 | 45 | 42 | 0.5172 | 0.4828 | 0.7130 | 0.7513 | 0.1574 |
| PAXG_2024_5M_FOLLOW | dio_0dd2 | offen_und_gereift | 85 | 72 | 13 | 0.8471 | 0.1529 | 0.7325 | 0.7725 | 0.1339 |
| PAXG_2024_5M_FOLLOW | dio_1ewh | offen_und_gereift | 82 | 39 | 43 | 0.4756 | 0.5244 | 0.7169 | 0.7540 | 0.1495 |
| PAXG_2024_5M_FOLLOW | dio_1jc2 | offen_und_gereift | 82 | 76 | 6 | 0.9268 | 0.0732 | 0.7368 | 0.7772 | 0.1163 |
| PAXG_2024_5M_FOLLOW | dio_00ly | offen_und_gereift | 80 | 33 | 47 | 0.4125 | 0.5875 | 0.7255 | 0.7646 | 0.1357 |
| PAXG_2024_5M_FOLLOW | dio_06er | offen_und_gereift | 77 | 58 | 19 | 0.7532 | 0.2468 | 0.7430 | 0.7841 | 0.1210 |
| PAXG_2024_5M_FOLLOW | dio_1lsu | offen_und_gereift | 67 | 52 | 15 | 0.7761 | 0.2239 | 0.7161 | 0.7551 | 0.1515 |
| PAXG_2024_5M_FOLLOW | dio_0kx9 | offen_und_gereift | 62 | 52 | 10 | 0.8387 | 0.1613 | 0.7384 | 0.7797 | 0.1162 |
| PAXG_2024_5M_FOLLOW | dio_1kpz | offen_und_gereift | 60 | 55 | 5 | 0.9167 | 0.0833 | 0.7317 | 0.7723 | 0.1235 |
| PAXG_2024_5M_FOLLOW | dio_07o8 | offen_und_gereift | 58 | 42 | 16 | 0.7241 | 0.2759 | 0.7181 | 0.7574 | 0.1527 |

## Lesung

Wenn dieselbe Familie sowohl offen als auch gereift erscheint, ist Offenheit keine isolierte Stoerung.
Sie wirkt dann eher wie eine wechselnde Varianzschicht ueber einer wiederkehrenden Rollenfamilie.

Wenn Familien nur offen erscheinen, bleibt die Lage dagegen noch ungebunden oder jung.

## Grenze

Diese Diagnose beschreibt nur passive Milieu-Schichtung.
Sie erzeugt keine Handlung und bewertet Offenheit nicht als Fehler.
