# 2113 - Relationale Salienz zwischen endogenen MCM-Episoden

## Zweck

Befund 2112 zeigt, dass das Feld ohne Grenzreset fortlaufend Rangzyklen
schliessen und wieder oeffnen kann. Die vielen selbst entstandenen Episoden
waehlen den fruehen quellgebundenen Formtraeger jedoch nicht reproduzierbar
aus.

2113 prueft deshalb, ob der kontaktnahe Wechsel zwischen zwei endogenen
Episoden innerhalb des eigenen Feldverlaufs durch eine ungewoehnlich starke
Formveraenderung hervortritt.

## Keine neue Kontaktregel

Feld und Rangzyklus-Segmentierer laufen wie in 2112 durch eine vollstaendige
Vorwelt und die direkt anschliessende Zielwelt. Sie erhalten kein Grenzsignal.

Erst nach dem abgeschlossenen Lauf markiert die Forschung den Uebergang zur
ersten Episode, die vollstaendig nach dem verdeckten Kontaktwechsel selbst
geoeffnet wurde. Verglichen wird deren Form mit der unmittelbar vorherigen
endogenen Episode.

Diese nachtraegliche Markierung dient ausschliesslich der Validierung. Sie wird
nicht als Kontakt-, Auswahl- oder Relevanzmechanik in DIO eingebaut.

## Intrinsische Formdistanz

Jede Episode besteht aus der relativen Verteilung gerichteter Wechsel der 66
paarweisen Neuronenrelationen. Vor dem Vergleich wird die gesamte
Wechselstaerke entfernt. Gelesen wird nur die Form:

```text
staerkenormierte Form der vorherigen Episode
gegen
staerkenormierte Form der naechsten Episode
```

Die ungewichtete Manhattan-Distanz entspricht der bereits verwendeten
Formgeometrie aus 2110 bis 2112. Preis, Richtung, Volumen, Asset, Jahr,
Herkunft und Weltname gehen nicht in die Distanz ein.

## Eigenrang statt Schwellwert

Pro Strom wird die kontaktnahe Distanz gegen alle eigenen aufeinanderfolgenden
Episodenwechsel desselben Vorwelt-Zielwelt-Verlaufs gerankt. Exakte
Distanzgleichstaende erhalten einen gemeinsamen Midrank.

Ein Eigenrang von `0,5` entspricht der Mitte des eigenen Verlaufs. Ein hoher
Wert waere ein Kandidat fuer ungewoehnlich starke relationale Veraenderung.
Kein Rang wird als fester Salienzschwellwert verwendet.

Jeder Strom besitzt einen breiten Vergleichsraum:

| Bestand | Uebergaenge Minimum | Median | Maximum |
|---|---:|---:|---:|
| 2091-Bestand | 337 | 371 | 404 |
| 2092-Holdout | 329 | 370,5 | 415 |

## Positionsverschiebende Null

Die Null waehlt in jedem Strom statt des kontaktmarkierten Kandidaten einen
anderen eigenen Episodenwechsel. Sie bewahrt damit:

- den vollstaendigen Feld- und Episodenverlauf,
- jede individuelle Distanzverteilung,
- Anzahl und Reihenfolge der endogenen Episoden,
- alle Zielkontexte und Quellenhaeufigkeiten.

Nur die Position des als kontaktnahe Veraenderung gelesenen Uebergangs wird
4.096-mal deterministisch verschoben.

## Gesamtbefund

| Bestand | Stroeme | mittlerer Eigenrang | Median | Anteil ueber eigener Mitte | Nullmittel | hohe Salienz p | geringe Aenderung p |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2091 | 768 | 0,380 | 0,320 | 32,4 % | 0,500 | 1,0 | 0,000244 |
| 2092 | 704 | 0,463 | 0,463 | 45,6 % | 0,500 | 0,999756 | 0,000488 |

Der kontaktnahe Episodenwechsel ist in keinem Gesamtbestand besonders stark.
Im Gegenteil: Er liegt in beiden Bestaenden signifikant unter einer zufaellig
positionierten eigenen Episodenveraenderung.

## Vergleich mit beiden Feldhaelften

Der Kandidat wird zusaetzlich getrennt gegen reine Vorwelt- und reine
Zielweltuebergaenge gerankt:

| Bestand | gegen Vorwelt | gegen Zielwelt |
|---|---:|---:|
| 2091 | 0,382 | 0,377 |
| 2092 | 0,476 | 0,451 |

Die geringe Gesamtposition entsteht nicht nur durch eine einzelne besonders
bewegliche Feldhaelfte. Der kontaktnahe Wechsel bleibt gegen beide internen
Vergleichsraeume unauffaellig oder relativ ruhig.

## Getrennte Zieluniversen

| Bestand | Universum | Stroeme | mittlerer Eigenrang | Positionsnull-Richtung | p |
|---|---|---:|---:|---|---:|
| 2091 | A | 384 | 0,361 | geringe Aenderung | 0,000244 |
| 2091 | B | 384 | 0,399 | geringe Aenderung | 0,000244 |
| 2092 | A | 352 | 0,577 | hohe Aenderung | 0,000244 |
| 2092 | B | 352 | 0,349 | geringe Aenderung | 0,000244 |

Der Entwicklungsbestand reproduziert relative Ruhe in beiden Universen. Im
Holdout laufen die beiden disjunkten Zieluniversen jedoch in entgegengesetzte
Richtungen. Ein Universum traegt einen erhoehten, das andere einen stark
verminderten Eigenrang.

Damit existiert keine universumsuebergreifende Richtung, die das Feld als
allgemeines Kontakt- oder Relevanzsignal lesen koennte.

## Grenzuebergreifende Episode

Bei 640 von 768 und 592 von 704 Stroemen war am verdeckten Kontaktwechsel noch
eine Vorweltepisode offen. Auch in diesen grossen Teilgruppen bleibt der
darauffolgende strikte Wechsel niedrig:

| Bestand | mittlerer Eigenrang | geringe Aenderung p |
|---|---:|---:|
| 2091 | 0,369 | 0,000244 |
| 2092 | 0,458 | 0,000488 |

Ohne grenzuebergreifende Episode liegt 2091 bei 0,434 und bleibt niedrig. Der
kleinere Holdoutrest liegt mit 0,493 in seiner Positionsnull. Das Mittragen
einer offenen Episode erzeugt somit ebenfalls keine hohe relationale Salienz.

## Befund

Getragen sind:

- eine rein intrinsische, staerkenormierte Relation zwischen endogenen
  Episodenformen,
- ein tie-erhaltender Eigenrang ohne festen Salienzschwellwert,
- ein breiter individueller Vergleichsraum von 329 bis 415 Uebergaengen,
- signifikant geringe kontaktnahe Formveraenderung in beiden Gesamtbestaenden,
- relative Ruhe gegen Vorwelt- und Zielweltuebergaenge,
- eine strenge positionsverschiebende Null mit 4.096 Wiederholungen.

Nicht getragen sind:

- hohe relationale Salienz am verdeckten Kontaktwechsel,
- eine gemeinsame Richtung in beiden disjunkten Holdout-Universen,
- eine endogene Auswahl der kontaktrelevanten Episode,
- ein allgemeines Neuheits- oder Relevanzsignal,
- eine speicherreife Formrelation,
- Semantik, Memory, Rueckwirkung oder Handlung.

2113 zeigt, dass ein Kontaktwechsel innerhalb der laufenden Rangzyklusfolge
nicht als grosser Sprung zwischen Episoden hervortritt. Die Feldbewegung nimmt
den Wechsel meist relativ kontinuierlich auf. Diese Kontinuitaet ist eine reale
Feldeigenschaft, aber kein reproduzierbares Kriterium dafuer, welche Episode
fuer eine wachsende organische Topologie relevant sein soll.

Damit ist auch einfache Episode-zu-Episode-Neuheit als Auswahlmechanik nicht
fundiert.

## Reproduzierbare Ausgaben

- `2113_MCM_EPISODEN_RELATIONALE_SALIENZ.paths.csv`
- `2113_MCM_EPISODEN_RELATIONALE_SALIENZ.summary.csv`

Der Runner ist `tools/run_mcm_episode_relational_salience.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
