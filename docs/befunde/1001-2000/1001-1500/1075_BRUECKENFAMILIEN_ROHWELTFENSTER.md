# 1075 - Brueckenfamilien gegen Rohweltfenster

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Welche uebersetzten Rohweltfenster liegen unter realen Brueckenfamilien, wenn dieselbe Symbolfamilie einmal als `tragende_verarbeitung` und einmal als `kippnaehe` erscheint?

## Methode

- Geprueft werden ausgewaehlte reale Brueckenfamilien aus 1072.
- Pro Fundstelle werden Ziel-Episode und Vorfenster gelesen.
- Rohwelt meint hier die MINI_DIO-Weltuebersetzung: Sehen, Hoeren, Rezeptoren und MCM-Feldwirkung.
- Keine OHLC-Handlungslesung, keine Strategie, keine Runtime-Regel.

## Familienvergleich

| Weltgruppe | Familie | Muster | Events | Ticks | Visual | Ton | Feld | Vorfeld | Target Spannung | Vor Spannung | Delta Spannung | Target Rekopplung | Target Strain |
|---|---|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|
| feld_5m | dio_0g2r | kippnaehe | 19 | 7-8217 | wechselnde_distanzform | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0952 | 0.0974 | -0.0021 | 0.6822 | 0.1670 |
| feld_5m | dio_0g2r | tragende_verarbeitung | 16 | 916-9155 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0710 | 0.1147 | -0.0437 | 0.7183 | 0.1327 |
| real_segment | dio_0g2r | kippnaehe | 4 | 4-390 | wechselnde_form | geordnetes_hinhoeren | offen | offen | 0.0804 | 0.1061 | -0.0257 | 0.6617 | 0.1668 |
| real_segment | dio_0g2r | tragende_verarbeitung | 4 | 861-1788 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0762 | 0.0791 | -0.0030 | 0.7176 | 0.1347 |
| regime | dio_0g2r | kippnaehe | 12 | 27-4633 | wechselnde_distanzform | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0888 | 0.1154 | -0.0266 | 0.6871 | 0.1628 |
| regime | dio_0g2r | tragende_verarbeitung | 30 | 2620-9967 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0659 | 0.1074 | -0.0415 | 0.7243 | 0.1318 |
| zeit_1h | dio_0g2r | kippnaehe | 12 | 37-8560 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0924 | 0.1096 | -0.0173 | 0.6886 | 0.1661 |
| zeit_1h | dio_0g2r | tragende_verarbeitung | 14 | 797-7997 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0680 | 0.1161 | -0.0482 | 0.7221 | 0.1316 |
| feld_5m | dio_155c | kippnaehe | 20 | 36-9673 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1288 | 0.1085 | 0.0203 | 0.6899 | 0.1761 |
| feld_5m | dio_155c | tragende_verarbeitung | 16 | 1396-9986 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.1020 | 0.1410 | -0.0389 | 0.7293 | 0.1359 |
| real_segment | dio_155c | kippnaehe | 2 | 10-10 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | belastet_kippnah | offen | 0.1094 | 0.0743 | 0.0351 | 0.6549 | 0.1793 |
| real_segment | dio_155c | tragende_verarbeitung | 2 | 1386-1386 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0901 | 0.0837 | 0.0064 | 0.7263 | 0.1381 |
| regime | dio_155c | kippnaehe | 6 | 2013-4745 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1399 | 0.1101 | 0.0298 | 0.6984 | 0.1777 |
| regime | dio_155c | tragende_verarbeitung | 18 | 1373-9944 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0999 | 0.1065 | -0.0066 | 0.7316 | 0.1337 |
| zeit_1h | dio_155c | kippnaehe | 10 | 246-7983 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | belastet_kippnah | rekoppelt | 0.1405 | 0.1005 | 0.0400 | 0.7007 | 0.1754 |
| zeit_1h | dio_155c | tragende_verarbeitung | 16 | 589-8149 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0979 | 0.1060 | -0.0082 | 0.7316 | 0.1377 |
| feld_5m | dio_17ct | kippnaehe | 23 | 66-9079 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1380 | 0.0967 | 0.0413 | 0.6904 | 0.1701 |
| feld_5m | dio_17ct | tragende_verarbeitung | 20 | 209-9358 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.1013 | 0.1087 | -0.0074 | 0.7238 | 0.1320 |
| real_segment | dio_17ct | kippnaehe | 4 | 26-118 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1292 | 0.1118 | 0.0174 | 0.6634 | 0.1740 |
| real_segment | dio_17ct | tragende_verarbeitung | 2 | 811-811 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | belastet_kippnah | 0.0927 | 0.1385 | -0.0458 | 0.7207 | 0.1303 |
| regime | dio_17ct | kippnaehe | 13 | 40-2400 | stabile_scharfe_form | geordnetes_hinhoeren | offen | offen | 0.1331 | 0.1324 | 0.0007 | 0.6941 | 0.1675 |
| regime | dio_17ct | tragende_verarbeitung | 18 | 2104-9310 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0954 | 0.1076 | -0.0121 | 0.7308 | 0.1325 |
| zeit_1h | dio_17ct | kippnaehe | 13 | 126-3001 | stabile_scharfe_form | geordnetes_hinhoeren | offen | offen | 0.1399 | 0.1200 | 0.0199 | 0.6931 | 0.1677 |
| zeit_1h | dio_17ct | tragende_verarbeitung | 16 | 1057-8655 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0947 | 0.0970 | -0.0023 | 0.7261 | 0.1333 |
| feld_5m | dio_1ewh | kippnaehe | 12 | 5-4583 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0946 | 0.1024 | -0.0077 | 0.6712 | 0.1716 |
| feld_5m | dio_1ewh | tragende_verarbeitung | 39 | 700-9781 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0682 | 0.1077 | -0.0396 | 0.7237 | 0.1343 |
| real_segment | dio_1ewh | kippnaehe | 2 | 69-69 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1026 | 0.1026 | -0.0000 | 0.6547 | 0.1789 |
| real_segment | dio_1ewh | tragende_verarbeitung | 8 | 633-1785 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0658 | 0.0905 | -0.0247 | 0.7210 | 0.1292 |
| regime | dio_1ewh | kippnaehe | 8 | 44-2135 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0997 | 0.1004 | -0.0007 | 0.6853 | 0.1682 |
| regime | dio_1ewh | tragende_verarbeitung | 54 | 2255-9901 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0684 | 0.1029 | -0.0345 | 0.7250 | 0.1336 |
| zeit_1h | dio_1ewh | kippnaehe | 16 | 35-1436 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0893 | 0.1125 | -0.0232 | 0.6644 | 0.1721 |
| zeit_1h | dio_1ewh | tragende_verarbeitung | 63 | 365-8628 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0658 | 0.1020 | -0.0362 | 0.7210 | 0.1336 |
| feld_5m | dio_1gp2 | kippnaehe | 24 | 249-7576 | stabile_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0914 | 0.1081 | -0.0167 | 0.6832 | 0.1663 |
| feld_5m | dio_1gp2 | tragende_verarbeitung | 11 | 845-8856 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0657 | 0.1210 | -0.0553 | 0.7192 | 0.1342 |
| real_segment | dio_1gp2 | kippnaehe | 6 | 3-1920 | stabile_scharfe_form | geordnetes_hinhoeren | offen | offen | 0.0857 | 0.1051 | -0.0194 | 0.6626 | 0.1732 |
| real_segment | dio_1gp2 | tragende_verarbeitung | 2 | 902-902 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0725 | 0.1007 | -0.0282 | 0.7165 | 0.1389 |
| regime | dio_1gp2 | kippnaehe | 11 | 443-5019 | stabile_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0972 | 0.0992 | -0.0020 | 0.6935 | 0.1656 |
| regime | dio_1gp2 | tragende_verarbeitung | 21 | 3343-9675 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0673 | 0.1097 | -0.0424 | 0.7240 | 0.1326 |
| zeit_1h | dio_1gp2 | kippnaehe | 14 | 1622-6230 | stabile_form | geordnetes_hinhoeren | offen | offen | 0.1001 | 0.0922 | 0.0079 | 0.6969 | 0.1669 |
| zeit_1h | dio_1gp2 | tragende_verarbeitung | 18 | 1878-8150 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0715 | 0.1022 | -0.0307 | 0.7224 | 0.1319 |

## Lesart

Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.

Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.

## Schluss

Diese Pruefung schliesst direkt an 1074 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.

## Wie es weitergeht

Als naechstes sollte die staerkste reale Familie aus dieser Tabelle einzeln visualisiert werden: Tickfenster, Vorfenster, Tonlage und Feldwirkung nebeneinander.
