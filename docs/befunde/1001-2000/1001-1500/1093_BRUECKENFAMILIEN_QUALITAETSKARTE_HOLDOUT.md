# 1093 - Brueckenfamilien Qualitaetskarte Holdout

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
| feld_5m | dio_0g2r | kippnaehe | 30 | 7-9843 | wechselnde_distanzform | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0957 | 0.0988 | -0.0031 | 0.6779 | 0.1712 |
| feld_5m | dio_0g2r | tragende_verarbeitung | 34 | 245-9699 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0732 | 0.1112 | -0.0381 | 0.7202 | 0.1337 |
| zeit_1h | dio_0g2r | kippnaehe | 8 | 161-2810 | wechselnde_form | geordnetes_hinhoeren | offen | belastet_kippnah | 0.0976 | 0.1291 | -0.0316 | 0.6658 | 0.1746 |
| zeit_1h | dio_0g2r | tragende_verarbeitung | 4 | 6517-8577 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0632 | 0.0964 | -0.0333 | 0.7242 | 0.1302 |
| feld_5m | dio_155c | kippnaehe | 22 | 36-9163 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1278 | 0.1018 | 0.0259 | 0.6915 | 0.1765 |
| feld_5m | dio_155c | tragende_verarbeitung | 32 | 280-8230 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.1018 | 0.1179 | -0.0161 | 0.7275 | 0.1364 |
| zeit_1h | dio_155c | kippnaehe | 6 | 1372-2520 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | rekoppelt | 0.1318 | 0.0782 | 0.0536 | 0.7016 | 0.1762 |
| zeit_1h | dio_155c | tragende_verarbeitung | 3 | 2287-5790 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | rekoppelt | 0.0951 | 0.1081 | -0.0130 | 0.7339 | 0.1334 |
| feld_5m | dio_17ct | kippnaehe | 22 | 1051-8314 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1403 | 0.1261 | 0.0142 | 0.7014 | 0.1658 |
| feld_5m | dio_17ct | tragende_verarbeitung | 36 | 209-9323 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.1018 | 0.1210 | -0.0191 | 0.7273 | 0.1348 |
| zeit_1h | dio_17ct | kippnaehe | 4 | 412-766 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.1327 | 0.1015 | 0.0312 | 0.6966 | 0.1646 |
| zeit_1h | dio_17ct | tragende_verarbeitung | 16 | 1134-8345 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | rekoppelt | 0.1043 | 0.1097 | -0.0054 | 0.7272 | 0.1339 |
| feld_5m | dio_1ewh | kippnaehe | 22 | 13-5549 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | belastet_kippnah | 0.0936 | 0.1304 | -0.0367 | 0.6761 | 0.1679 |
| feld_5m | dio_1ewh | tragende_verarbeitung | 75 | 149-9379 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0695 | 0.1057 | -0.0361 | 0.7238 | 0.1350 |
| zeit_1h | dio_1ewh | tragende_verarbeitung | 37 | 989-8324 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0710 | 0.0997 | -0.0287 | 0.7239 | 0.1342 |
| feld_5m | dio_1gp2 | kippnaehe | 8 | 496-5349 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0991 | 0.0975 | 0.0016 | 0.6935 | 0.1632 |
| feld_5m | dio_1gp2 | tragende_verarbeitung | 17 | 330-7511 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0690 | 0.1147 | -0.0457 | 0.7203 | 0.1324 |
| zeit_1h | dio_1gp2 | kippnaehe | 18 | 184-8718 | stabile_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0884 | 0.1041 | -0.0156 | 0.6861 | 0.1661 |
| zeit_1h | dio_1gp2 | tragende_verarbeitung | 10 | 1344-7287 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0648 | 0.1104 | -0.0456 | 0.7244 | 0.1278 |

## Lesart

Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.

Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.

## Schluss

Diese Pruefung schliesst direkt an 1074 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.

## Wie es weitergeht

Als naechstes sollte die staerkste reale Familie aus dieser Tabelle einzeln visualisiert werden: Tickfenster, Vorfenster, Tonlage und Feldwirkung nebeneinander.
