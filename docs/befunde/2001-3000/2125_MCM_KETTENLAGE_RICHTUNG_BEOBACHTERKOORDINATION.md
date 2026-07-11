# 2125 - Kettenlage, Richtung und Beobachterkoordination

## Fragestellung

2124 lokalisierte den dominanten Aktivierungs-Nachhall-
Synchronitaetsueberschuss in der fest programmierten Nachbarschaftsweitergabe
des aktuellen MCM-Feldes. 2125 prueft, welcher Teil dieser Wirkung an der
konkreten Indexordnung `0 -> 1 -> ... -> 11` haengt.

Dabei werden keine neuen Verbindungen, Gewichte oder Lernregeln eingefuehrt.
Dieselbe gerichtete Kettenform wird nur an allen moeglichen Kopfpositionen und
in beiden Laufrichtungen diagnostisch gelesen.

## Ordnungsraum

Bei zwoelf Neuronen entstehen:

- die produktive Originalordnung,
- elf weitere Vorwaertsrotationen,
- zwoelf Rueckwaertsrotationen.

Damit werden 23 vollstaendige Alternativen geprueft. Jede Neuronenidentitaet
steht in jeder Richtung einmal am Kettenkopf. Vorwaertsrotationen erhalten den
gerichteten Nachbarschaftssinn der Originalkette und verschieben nur ihren
Schnittpunkt. Rueckwaertsrotationen kehren diesen Sinn vollstaendig um.

Fuer jede Ordnung werden eigene kontinuierliche Vorwelt-Zielwelt-Felder
erzeugt. Ein fertiger Feldverlauf wird nicht nachtraeglich umsortiert.

## Erhaltene Bedingungen

- identische weltrelative Sinnesfolgen,
- identische Neuronenidentitaeten und Eingangsgewichte,
- identische Kopplungsstaerke `0,12`,
- identische Nachhallgleichung,
- identische Neuronenzahl,
- identische Zieluniversen und Quellen,
- identische Beobachter und Kadenzkorrektur.

Die Originalordnung des Diagnose-Runners erzeugt byte-identisch die produktive
Feldspur. Ihr Synchronitaetsueberschuss stimmt in beiden Bestaenden exakt mit
2124 ueberein.

## Gesamtbefund

| Bestand | Universum | Original | Vorwaerts-Mittel | Rueckwaerts-Mittel | alle Alternativen | Vorwaertsordnungen >= Original |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2091 | A | 3.987,34 | 3.534,91 | 96,39 | 1.740,90 | 4 / 11 |
| 2091 | B | 5.101,62 | 3.588,33 | 277,91 | 1.861,15 | 0 / 11 |
| 2091 | gesamt | 9.088,96 | 7.123,23 | 374,30 | 3.602,05 | 1 / 11 |
| 2092 | A | 4.234,14 | 3.665,68 | 164,50 | 1.838,98 | 5 / 11 |
| 2092 | B | 3.865,59 | 3.989,76 | 126,71 | 1.974,25 | 9 / 11 |
| 2092 | gesamt | 8.099,74 | 7.655,44 | 291,21 | 3.813,23 | 6 / 11 |

Vorwaertsrotationen bewahren im Gesamtbestand `78,37 %` beziehungsweise
`94,51 %` des Originalueberschusses. Rueckwaertsrotationen bewahren nur
`4,12 %` beziehungsweise `3,60 %`.

Die Spannweite zeigt zugleich, dass auch die Kopfposition wirkt:

| Bestand | Vorwaerts-Minimum | Vorwaerts-Maximum | Rueckwaerts-Minimum | Rueckwaerts-Maximum |
| --- | ---: | ---: | ---: | ---: |
| 2091 | -945,86 | 9.237,04 | 203,73 | 580,50 |
| 2092 | 914,69 | 9.127,76 | 143,15 | 765,52 |

Eine Vorwaertsrotation uebertrifft den Originalgesamtwert im
Entwicklungsbestand; im Holdout tun dies sechs von elf. Die Originalkette ist
damit keine einzigartige oder allgemein optimale Kopfposition.

## Quellen- und Pfadgrenze

Gegen das Mittel aller Vorwaertsrotationen liegt die Originalordnung im
Gesamtbestand in allen 48 beziehungsweise 44 Quellen hoeher. Dieser
Gesamtvorteil ist jedoch kontextabhaengig:

- Im Holdout-Universum A tragen 44 von 44 Quellen die Originalordnung hoeher.
- Im Holdout-Universum B tragen nur 3 von 44 Quellen die Originalordnung
  hoeher; 41 von 44 bevorzugen das Vorwaertsmittel.
- Auf Pfadebene liegt die Originalordnung nur in 576 von 768 beziehungsweise
  395 von 704 Faellen ueber dem Vorwaertsmittel.

Gegen das Rueckwaertsmittel liegt die Originalordnung dagegen in beiden
Gesamtbestaenden in jeder Quelle und jedem einzelnen Pfad hoeher.

## Einordnung

2125 trennt zwei Architekturanteile:

1. **Kettenkopf:** Die genaue Startposition ist beweglich und
   zieluniversumsabhaengig. Index `0` ist kein reproduzierbar einzigartiger
   Traeger.
2. **Kettenrichtung:** Die vorgegebene Laufrichtung entlang der
   indexgebundenen Neuronenordnung ist der dominante und breite Traeger der
   beobachteten Koordination.

Damit wird die Grenze aus 2124 schaerfer. Die Mehrprojektionskoordination ist
reale Wirkung des aktuellen Feldmechanismus, folgt aber wesentlich einer
festen gerichteten Architektur. Auch die Neuronengewichte werden im Kern
deterministisch aus ihrem Index initialisiert. Richtung und Gewichtsordnung
sind daher nicht organisch aus Erfahrung entstanden.

2125 belegt keine organische Topologie, keine Feldintelligenz und keine
Semantik. Der Befund warnt ausdruecklich davor, die starke Synchronitaet als
Wachstumssignal oder Memory-Grundlage zu verwenden. Es wird nichts in den
produktiven Feldkern uebernommen.

## Methodische Grenze

Die 23 Kontrollen decken alle Kopfpositionen in beiden Richtungen derselben
Kettenform ab. Sie pruefen noch keine beliebigen neuen Nachbarschaften oder
frei entstehenden Graphen. Der empirische Ordnungsrang beschreibt deshalb nur
diesen vollstaendigen Lage-Richtungs-Raum und keine allgemeine
Topologienwahrscheinlichkeit.

## Reproduzierbarkeit

Ausgaben:

- `2125_MCM_KETTENLAGE_RICHTUNG_BEOBACHTERKOORDINATION.paths.csv`
- `2125_MCM_KETTENLAGE_RICHTUNG_BEOBACHTERKOORDINATION.sources.csv`
- `2125_MCM_KETTENLAGE_RICHTUNG_BEOBACHTERKOORDINATION.summary.csv`
- `2125_MCM_KETTENLAGE_RICHTUNG_BEOBACHTERKOORDINATION.orders.csv`

SHA-256:

- `paths`: `D2A51F04052FC01D74B1D0AF523C186EEC52DF7B1B79F758653503F5613782B7`
- `sources`: `4326A2EAABA26FD70D801F2C746E05055D28DD72097181B5E5FA07A50E3A8AF4`
- `summary`: `B71275B7B1789A761B7777904B156BED7216391215A349C4EEAAAD1A5862593D`
- `orders`: `B6A59A99AB797034FF4642DF234C43D9C50392921D97B41FFC006B91EC762CA4`

Runner: `tools/run_mcm_chain_order_observer_coordination.py`

Test: `tests/test_mcm_chain_order_observer_coordination.py`
