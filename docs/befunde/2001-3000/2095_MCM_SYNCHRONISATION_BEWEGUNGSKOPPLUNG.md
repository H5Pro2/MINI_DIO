# 2095 - Kopplung von MCM-Synchronisation und Bewegungstopologie

## Zweck

Befund 2094 fand in zwei unabhängigen Beständen einen wiederkehrenden, aber
beweglichen Synchronisationsrahmen relationaler Eigenzeiten. Befund 2095
prüft, ob die passive Bewegungsnachbarschaft des Relationslebenslaufs diesen
Rahmen gezielt nutzt.

Die Frage lautet: Liegen die vom Feld ausgewählten Bewegungsnachbarschaften
häufiger auf Synchronisationspaaren, die beim nächsten Relationsalter erhalten
bleiben, als die gleichzeitig vorhandenen, aber nicht ausgewählten Paare?

Außenwerte, Chartmuster und Handlungsergebnisse werden nicht untersucht. Die
Auswertung wird nicht in das Feld zurückgelesen.

## Gemeinsame Vergleichsgelegenheit

Für jeden Übergang von Relationsalter `a` zu `a + 1` werden ausschließlich
Synchronisationspaare betrachtet, deren beide Relationen in beiden
Altersschichten vorkommen.

Innerhalb derselben Menge entstehen zwei Auswertungskategorien:

- **bewegungsselektiert:** Das Synchronisationspaar ist bei Alter `a` zugleich
  eine gegenseitige Bewegungsnachbarschaft des passiven Lebenslaufs.
- **nicht selektiert:** Das Paar besitzt dieselbe Synchronisationsgelegenheit,
  ist aber keine Bewegungsnachbarschaft.

Erhalt bedeutet, dass dieselbe Synchronisationspaaridentität auch bei Alter
`a + 1` besteht. Die Kategorien werden weder gespeichert noch programmiert.

## Rohvergleich

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| informative Altersübergänge | 45 | 38 |
| bewegungsselektierte Paare | 72.404 | 55.031 |
| davon synchron erhalten | 40.076 | 31.894 |
| Erhaltungsrate selektiert | 55,35 % | 57,96 % |
| nicht selektierte Paare | 110.367 | 93.972 |
| davon synchron erhalten | 55.938 | 49.410 |
| Erhaltungsrate nicht selektiert | 50,68 % | 52,58 % |
| Ratendifferenz | +4,67 Prozentpunkte | +5,38 Prozentpunkte |
| relatives Verhältnis | 1,0921 | 1,1023 |

Die einfache altersstratifizierte Kantenlabelnull verteilt nur die
Bewegungsselektion innerhalb derselben Altersschicht. Keine von 2.000
Permutationen erreicht in einem der Bestände den beobachteten Wert;
`p = 1/2001 = 0,000500`.

Diese Kontrolle zeigt eine Zuordnung innerhalb der beobachteten Graphen, kann
aber nicht unterscheiden, ob konkrete Paaridentität oder nur die Einbettung
der beteiligten Relationen in den Zukunftsgraphen trägt.

## Zukunftsgraph-Identitätsnull

Die strengere Null erhält pro Altersübergang:

- dieselben in beiden Altern vorhandenen Relationen,
- den vollständigen nächsten Synchronisationsgraphen,
- dessen Kantenzahl und Gradstruktur,
- die wirklichen aktuellen Bewegungsnachbarschaften.

Nur die Relationsidentitäten des nächsten Synchronisationsgraphen werden
200-mal permutiert. Gemessen wird erneut die Ratendifferenz zwischen
bewegungsselektierten und nicht selektierten aktuellen Paaren.

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| beobachtete Ratendifferenz | 0,04667 | 0,05377 |
| Nullmittel | 0,04891 | 0,05562 |
| Null-Standardabweichung | 0,00786 | 0,00947 |
| Nullbereich | 0,02847 bis 0,06740 | 0,03032 bis 0,08475 |
| empirisches `p` | 0,5821 | 0,6020 |

Der beobachtete Rohvorteil liegt in beiden Beständen leicht unter dem
Nullmittel. Er benötigt keine besondere Synchronisationspaaridentität. Die
Graphform und die darin liegende Knoteneinbettung reichen aus, um ihn zu
erklären.

## Altersgrenze des Rohsignals

| Bereich | 2091: Differenz | 2091: analytisches `p` | 2092: Differenz | 2092: analytisches `p` |
|---|---:|---:|---:|---:|
| Alter 2 bis 4 | +0,05067 | 1,02 * 10^-71 | +0,06210 | 4,12 * 10^-68 |
| ab Alter 5 | +0,00036 | 0,4075 | +0,03140 | 0,1193 |
| Alter 5 bis 10 | -0,00875 | 0,5881 | +0,03540 | 0,0332 |
| ab Alter 11 | +0,04839 | 0,1479 | +0,00005 | 0,7833 |

Der Rohvorteil wird vor allem von den großen frühen Altersschichten getragen.
Ab Alter 5 ist seine Richtung und Stärke zwischen den Beständen nicht stabil.
Diese nachgelagerte Aufteilung begründet keine Altersgrenze.

## Befund

Getragen sind:

- ein ähnlicher positiver Rohabstand in beiden Beständen,
- eine starke Konzentration dieses Abstands in frühen Altersschichten,
- die vollständige Einordnung aller verglichenen Bewegungsnachbarschaften in
  exakte Synchronisationsgelegenheiten,
- die Erklärung des Rohabstands durch Graphform und Knoteneinbettung.

Nicht getragen sind:

- eine besondere Kopplung konkreter Bewegungs- und
  Synchronisationspaaridentitäten,
- ein altersübergreifend stabiler Kopplungseffekt,
- eine passive mehrschichtige Feldstruktur aus diesen beiden Graphen,
- eine feste Alters-, Gewichtungs- oder Auswahlregel,
- eine Rücklesung in Feld, Wahrnehmung oder Handlung.

2095 begrenzt die positive Erkenntnis aus 2094. Der Synchronisationsrahmen ist
eine reale innere Eigenzeitstruktur, aber die Bewegungsnachbarschaft nutzt
keine besondere seiner konkreten Bahnen. Beide Ebenen bleiben passive,
voneinander unterscheidbare Beobachtungsräume. An Runtime und Memory wird
nichts geändert.

## Reproduzierbare Ausgaben

- `2095_MCM_SYNCHRONISATION_BEWEGUNGSKOPPLUNG.ages.csv`
- `2095_MCM_SYNCHRONISATION_BEWEGUNGSKOPPLUNG.sensitivity.csv`
- `2095_MCM_SYNCHRONISATION_BEWEGUNGSKOPPLUNG.null.csv`
- `2095_MCM_SYNCHRONISATION_BEWEGUNGSKOPPLUNG.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089, 2090 und
2092. Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien.
