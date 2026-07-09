# 1799 - Dio 0L7P Bruecke Rohwelt Ruecklesung

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
| feld_5m | dio_0l7p | tragende_verarbeitung | 691 | 119-9948 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0543 | 0.1185 | -0.0642 | 0.7313 | 0.1313 |
| zeit_1h | dio_0l7p | tragende_verarbeitung | 642 | 318-8748 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | offen | 0.0544 | 0.1149 | -0.0605 | 0.7313 | 0.1318 |

## Lesart

Eine Brueckenfamilie wird nicht dadurch interessant, dass sie in zwei Mustern vorkommt. Interessant ist, ob sich ihre Welt- und Feldlage zwischen diesen Mustern unterscheidet.

Wenn dieselbe Familie bei `tragende_verarbeitung` mehr Rekopplung, Schaerfe und Hinhoeren zeigt, bei `kippnaehe` aber mehr Lautheit, Spannung, Distanz oder Feldaufnahme, dann ist sie keine fertige Bedeutung. Sie ist ein Uebergangstraeger, dessen Lesart durch Weltkontakt rueckgekoppelt wird.

## Schluss

Diese Pruefung schliesst direkt an 1074 an: Innennaehe allein reicht nicht. Die Familie muss gegen Rohweltfenster und Feldfolge gelesen werden.

## Wie es weitergeht

Als naechstes sollte die staerkste reale Familie aus dieser Tabelle einzeln visualisiert werden: Tickfenster, Vorfenster, Tonlage und Feldwirkung nebeneinander.
