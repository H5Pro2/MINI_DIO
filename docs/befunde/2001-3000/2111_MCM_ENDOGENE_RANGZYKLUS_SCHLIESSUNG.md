# 2111 - Endogene Schliessung intrinsischer MCM-Formepisoden

## Zweck

Befund 2110 zeigt einen intrinsisch lesbaren Quellformtraeger aus
aufeinanderfolgenden eigenen Feldzustaenden. Der robuste gemeinsame Bereich
liegt bei 1 bis 4 Kontaktticks. Eine feste Tickzahl waere jedoch keine
organische Episodengrenze.

2111 prueft deshalb, ob das Feld sein laufendes Formprofil durch ein eigenes
topologisches Ereignis schliessen kann.

## Oeffnung und Schliessung

Der Kontakt beginnt mit der vorhandenen neuronalen Rangordnung des
Vorweltfeldes.

Das Profil wird erst geoeffnet, wenn sich diese innere Ordnung tatsaechlich
aendert:

```text
erste neue Rangordnung -> Episode ist offen
```

Danach wird jede exakte Rangordnung innerhalb desselben Kontakts bewahrt. Die
Episode schliesst beim ersten Zustand, der bereits zuvor in diesem Kontakt
oder als Ausgangsordnung vorhanden war:

```text
erste exakte Rangwiederkehr -> Episode schliesst
```

Es gibt:

- keine feste Mindest- oder Maximaldauer,
- keine Epsilon- oder Aehnlichkeitsschwelle,
- kein Resetfeld,
- kein Herkunfts-, Asset-, Jahres- oder Weltwissen,
- kein Lernen, Memory oder Handlung.

Ein noch nicht geschlossener Pfad duerfte bis zum Ende seiner realen Zielwelt
laufen. Die Schliessung wird nicht durch ein Forschungszeitlimit erzwungen.

## Verbleibende aeussere Grenze

Der Episodenbeginn wird in 2111 weiterhin durch den bereitgestellten
Kontaktwechsel zwischen Vorwelt und Zielwelt gesetzt. Nur das Ende entsteht
endogen aus der Feldtopologie.

2111 prueft damit eine feldinterne Schliessung, noch keinen vollstaendig
autonomen Episodenstart.

## Vollstaendige Schliessung

| Bestand | Quell-Ziel-Pfade | geoeffnet | geschlossen | Anteil |
|---|---:|---:|---:|---:|
| 2091-Bestand | 768 | 768 | 768 | 100 % |
| 2092-Holdout | 704 | 704 | 704 | 100 % |

Jeder der 1.472 Pfade oeffnet durch eine reale Rangveraenderung und schliesst
durch eine exakte Wiederkehr. Es bleibt kein ungeschlossener Pfad.

## Entstehende Dauer

| Bestand | Oeffnung Median | Schliessung Minimum | Schliessung Median | Schliessung Mittel | Schliessung Maximum |
|---|---:|---:|---:|---:|---:|
| 2091 | 1 | 2 | 4 | 4,94 | 13 |
| 2092 | 1 | 2 | 5 | 5,62 | 13 |

Im 2091-Bestand oeffnen 720 von 768 Pfaden bereits bei Tick 1, im Holdout 657
von 704. Spaetere Oeffnungen reichen nur bis Tick 4 beziehungsweise 3.

Die Schliessung verteilt sich dagegen ueber alle Ticks von 2 bis 13. Sie ist
nicht auf den Median festgelegt und reproduziert dennoch in beiden Bestaenden
dieselbe Groessenordnung.

## Nichttriviale Zyklusform

| Bestand | Zyklusspanne | verschiedene Rangordnungen | gerichtete Uebergangsbeobachtungen |
|---|---|---|---|
| 2091 | 1 bis 10, Median 2 | 2 bis 13, Median 4 | 1 bis 64, Median 14 |
| 2092 | 1 bis 11, Median 3 | 2 bis 13, Median 5 | 1 bis 65, Median 20 |

Die Schliessung ist damit nicht nur ein identischer Ein-Tick-Selbstloop. Die
Pfade tragen unterschiedlich lange Zyklen, verschieden viele innere Ordnungen
und eine breite Zahl gerichteter Rangwechsel.

## Variable intrinsische Formprofile

Alle bis zur endogenen Schliessung beobachteten gerichteten Rangwechsel bilden
das Profil des jeweiligen Quell-Ziel-Pfads. Acht Pfade derselben Vorwelt werden
pro Zieluniversum addiert und durch ihre gesamte Wechselzahl geteilt.

Kein Universumsprofil bleibt leer. Verglichen wird nur die relative innere
Form, nicht Dauer oder Bewegungsmenge.

## Universumsuebergreifende Quelltrennung

| Bestand | Richtung | mittlere AUC | Median Identitaetsrang | eindeutig naechste Identitaet | hoechste Labelnull-AUC |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 0,836 | 4,5 | 10 | 0,635 |
| 2091 | B nach A | 0,867 | 4 | 13 | 0,644 |
| 2092 | A nach B | 0,902 | 3 | 10 | 0,636 |
| 2092 | B nach A | 0,858 | 5 | 9 | 0,615 |

Alle vier AUC-Werte liegen oberhalb jeder ihrer 4.096 globalen
Herkunftslabelnullen. Die variable endogene Dauer bewahrt somit eine starke
quellgebundene Form zwischen den beiden disjunkten Zieluniversen.

## Anonymer gegenseitiger Graph

Der Graph entsteht wie in 2110 ausschliesslich aus gegenseitiger naechster
Manhattan-Naehe der staerkenormierten Profile. Herkunft, Asset und Jahr werden
erst nach abgeschlossener Kantenbildung gelesen.

| Bestand | gegenseitige Kanten | gleiche Quelle nachtraeglich | Anteil | Nullmittel | Nullmaximum | empirisches p |
|---|---:|---:|---:|---:|---:|---:|
| 2091 | 10 | 5 | 50,0 % | 0,198 | 3 | 0,000244 |
| 2092 | 8 | 3 | 37,5 % | 0,181 | 3 | 0,000732 |

Die Zahl gleichquelliger Kanten ist kleiner als in den guenstigsten festen
1- bis 4-Tick-Profilen aus 2110. Dennoch entsteht sie in beiden Bestaenden klar
ueber der Labelnull, ohne eine Beobachtungsdauer vorzugeben.

Der Verlust an Kanten ist die messbare Folge variabler organischer
Schliessung: Nicht jeder Kontakt endet an derselben Stelle, aber die erhaltene
Form bleibt quellgebunden.

## Befund

Getragen sind:

- Oeffnung durch eine tatsaechliche innere Rangveraenderung,
- endogene Schliessung aller 1.472 Pfade durch erste exakte Rangwiederkehr,
- variable Dauer von 2 bis 13 Ticks ohne Zeitlimit,
- nichttriviale Zyklen und breite intrinsische Uebergangsprofile,
- hohe Quelltrennung zwischen disjunkten Zieluniversen,
- ein anonymer gegenseitiger Graph ueber der Herkunftslabelnull,
- Reproduktion in Entwicklungsbestand und unabhaengigem Holdout.

Nicht getragen sind:

- ein endogen erkannter Kontakt- oder Episodenbeginn,
- eine vollstaendig autonome Segmentierung des fortlaufenden Feldes,
- eine bereits integrierte Formepisode oder Memory,
- eine semantische Identitaet der Rangzyklen,
- Feldrueckwirkung, autonome Aktivitaet oder Handlung.

2111 zeigt, dass das Feld seine intrinsische Form ohne feste Tickzahl an einem
eigenen topologischen Wiederkehrereignis schliessen kann. Die variable
Schliessung bewahrt genug Quellform, um zwischen getrennten Zieluniversen
ueberzufaellige anonyme Nachbarschaften zu bilden.

Damit liegt erstmals ein endogener Abschlusskandidat fuer eine organische
MCM-Formepisode vor. Der Start bleibt jedoch an die von aussen bereitgestellte
Kontaktgrenze gebunden, und MINI_DIO speichert oder liest die Episode noch
nicht.

## Reproduzierbare Ausgaben

- `2111_MCM_ENDOGENE_RANGZYKLUS_SCHLIESSUNG.paths.csv`
- `2111_MCM_ENDOGENE_RANGZYKLUS_SCHLIESSUNG.edges.csv`
- `2111_MCM_ENDOGENE_RANGZYKLUS_SCHLIESSUNG.summary.csv`

Der Runner ist `tools/run_mcm_endogenous_rank_cycle_closure.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
