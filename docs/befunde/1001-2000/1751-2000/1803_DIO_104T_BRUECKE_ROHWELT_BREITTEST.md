# 1803 - Dio 104T Bruecke Rohwelt Breittest

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Welche uebersetzten Rohweltfenster liegen unter realen Brueckenfamilien, wenn dieselbe Symbolfamilie einmal als `tragende_verarbeitung` und einmal als `kippnaehe` erscheint?

## Methode

- Geprueft werden ausgewaehlte reale Brueckenfamilien aus 1798.
- Pro Fundstelle werden Ziel-Episode und Vorfenster gelesen.
- Rohwelt meint hier die MINI_DIO-Weltuebersetzung: Sehen, Hoeren, Rezeptoren und MCM-Feldwirkung.
- Keine OHLC-Handlungslesung, keine Strategie, keine Runtime-Regel.

## Familienvergleich

| Weltgruppe | Familie | Muster | Events | Ticks | Visual | Ton | Feld | Vorfeld | Target Spannung | Vor Spannung | Delta Spannung | Target Rekopplung | Target Strain |
|---|---|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|
| feld_5m | dio_104t | kippnaehe | 4 | 5-253 | wechselnde_form | geordnetes_hinhoeren | offen | offen | 0.0849 | 0.0832 | 0.0017 | 0.6864 | 0.1627 |
| feld_5m | dio_104t | tragende_verarbeitung | 71 | 79-8714 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0688 | 0.1035 | -0.0347 | 0.7301 | 0.1355 |
| regime | dio_104t | kippnaehe | 2 | 9-9 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | offen | 0.0862 | 0.1185 | -0.0323 | 0.6581 | 0.1736 |
| regime | dio_104t | tragende_verarbeitung | 110 | 197-9231 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0670 | 0.1057 | -0.0387 | 0.7312 | 0.1352 |
| zeit_1h | dio_104t | tragende_verarbeitung | 100 | 157-8748 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | offen | 0.0672 | 0.1001 | -0.0329 | 0.7297 | 0.1365 |

## Lesart

Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.

Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.

## Schluss

Diese Pruefung schliesst direkt an 1798 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.
