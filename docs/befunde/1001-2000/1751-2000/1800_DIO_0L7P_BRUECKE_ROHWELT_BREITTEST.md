# 1800 - Dio 0L7P Bruecke Rohwelt Breittest

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
| feld_5m | dio_0l7p | kippnaehe | 2 | 3-3 | stabile_scharfe_form | geordnetes_hinhoeren | offen | offen | 0.0478 | 0.1059 | -0.0581 | 0.6664 | 0.1616 |
| feld_5m | dio_0l7p | tragende_verarbeitung | 741 | 37-9949 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0511 | 0.0979 | -0.0468 | 0.7300 | 0.1309 |
| regime | dio_0l7p | tragende_verarbeitung | 1059 | 118-9982 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0511 | 0.1010 | -0.0498 | 0.7323 | 0.1316 |
| zeit_1h | dio_0l7p | tragende_verarbeitung | 845 | 73-8765 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0514 | 0.1003 | -0.0489 | 0.7298 | 0.1318 |

## Lesart

Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.

Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.

## Schluss

Diese Pruefung schliesst direkt an 1074 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.

## Wie es weitergeht

Als naechstes sollte die staerkste reale Familie aus dieser Tabelle einzeln visualisiert werden: Tickfenster, Vorfenster, Tonlage und Feldwirkung nebeneinander.
