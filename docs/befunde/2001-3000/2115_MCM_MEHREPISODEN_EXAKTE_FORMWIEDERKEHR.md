# 2115 - Exakte Formwiederkehr ueber viele MCM-Episoden

## Zweck

Befund 2114 trennt den Rangzyklus als Eigenzeittraeger von der noch offenen
Frage, welche vieler selbst entstandener Formen fuer eine wachsende Topologie
relevant werden kann.

2115 prueft den strengsten Wiederkehrkandidaten: Eine Episodenform darf erst
nach einer zweiten exakt proportionalen Beobachtung als wiederkehrend gelten.
Es gibt keine Aehnlichkeitsschwelle, kein Clustering und keine vorgegebenen
Formfamilien.

## Kanonische Episodenform

Jede geschlossene Rangzyklus-Episode besitzt ein ganzzahliges Profil der
gerichteten Wechsel aller 66 Neuronenrelationen. Eine gemeinsame ganzzahlige
Staerke wird durch den groessten gemeinsamen Teiler entfernt:

```text
(2, 4, 0, ...) -> (1, 2, 0, ...)
```

Nur exakt gleiche kanonische Vektoren gelten als dieselbe Form. Nahe, aber
nicht identische Formen bleiben getrennt.

## Wiederkehr statt Erstbeobachtung

Pro kontinuierlichem Vorwelt-Zielwelt-Strom werden alle vollstaendig nach dem
verdeckten Kontakt selbst geoeffneten und geschlossenen Episoden gelesen.

Die erste Beobachtung einer kanonischen Form erzeugt keine Wiederkehr. Jede
weitere exakte Beobachtung traegt einmal zum Wiederkehrprofil bei:

```text
erste Form A   -> noch keine Wiederkehr
zweite Form A  -> eine Wiederkehr
dritte Form A  -> zwei Wiederkehrbeobachtungen
```

Die Kontaktgrenze wird nur nachtraeglich verwendet, um die in allen
Zielzweigen identische Vorweltphase nicht in die Profile zu kopieren. Feld und
Segmentierer erhalten diese Grenze nicht.

## Direkte Kontrolle

Zwei Lesungen derselben Episoden werden verglichen:

- `all_episode_forms`: jede kanonische Episode traegt,
- `exact_recurrence_forms`: nur Beobachtungen nach dem ersten Auftreten einer
  exakt gleichen Form tragen.

Je Quelle werden die acht Zielstroeme eines Universums addiert und danach
staerkenormiert. Die beiden disjunkten Zieluniversen aus 2109 bis 2113 bleiben
vollstaendig getrennt.

## Wiederkehrdichte

| Bestand | Stroeme | mit Wiederkehr | Minimum | Median | Maximum | mittlerer Episodenanteil |
|---|---:|---:|---:|---:|---:|---:|
| 2091-Bestand | 768 | 768 | 2 | 7 | 18 | 3,91 % |
| 2092-Holdout | 704 | 704 | 1 | 7 | 26 | 4,58 % |

Exakte proportionale Formwiederkehr tritt in jedem einzelnen Strom auf. Eine
fehlende Mehrfachbeobachtung kann den weiteren Befund daher nicht erklaeren.

Die typische Vielfalt bleibt hoch:

| Bestand | Episoden Median | verschiedene kanonische Formen Median | wiederkehrende Formklassen Median |
|---|---:|---:|---:|
| 2091 | 183 | 177 | 6 |
| 2092 | 186 | 178 | 5 |

Das Feld bildet somit viele Einzelvarianten und eine kleine, aber durchgehend
vorhandene exakte Wiederkehrschicht.

## All-Episoden-Kontrolle

| Bestand | Richtung | AUC | gegenseitige Kanten | gleiche Quelle nachtraeglich |
|---|---|---:|---:|---:|
| 2091 | A nach B | 0,544 | 2 | 0 |
| 2091 | B nach A | 0,552 | 2 | 0 |
| 2092 | A nach B | 0,503 | 1 | 0 |
| 2092 | B nach A | 0,498 | 1 | 0 |

Die All-Episoden-Lesung reproduziert die vollstaendige Lesung aus 2112. Der
Entwicklungsbestand behaelt eine kleine verteilte Restinformation, aber kein
lokales gleichquelliges Nachbarschaftsnetz. Der Holdout liegt bei Zufallsnaehe.

Damit ist die neue Pipeline an der bestehenden Begrenzung angeschlossen.

## Exakte Wiederkehrprofile

| Bestand | Richtung | AUC | hoechste Labelnull-AUC | p |
|---|---|---:|---:|---:|
| 2091 | A nach B | 0,500 | 0,503 | 0,762 |
| 2091 | B nach A | 0,504 | 0,516 | 0,160 |
| 2092 | A nach B | 0,500 | 0,500 | 1,0 |
| 2092 | B nach A | 0,500 | 0,501 | 0,748 |

Alle Wiederkehrprofile der Quelluniversen sind gefuellt. Dennoch liegt keine
der vier Leserichtungen oberhalb ihrer formerhaltenden Quellenlabelnull.

Die kleine Resttrennung der All-Episoden-Lesung wird durch exakte Wiederkehr
nicht verdichtet, sondern verschwindet.

## Anonymer gegenseitiger Graph

| Bestand | Profil | gegenseitige Kanten | gleiche Quelle nachtraeglich | Labelnull-p |
|---|---|---:|---:|---:|
| 2091 | alle Episoden | 2 | 0 | 1,0 |
| 2091 | exakte Wiederkehr | 2 | 0 | 1,0 |
| 2092 | alle Episoden | 1 | 0 | 1,0 |
| 2092 | exakte Wiederkehr | 1 | 0 | 1,0 |

Der Graph entsteht global aus gegenseitiger naechster Manhattan-Naehe der
staerkenormierten Quellenprofile. Herkunft, Asset und Jahr werden erst nach
der Kantenbildung gelesen. Exakte Distanzgleichstaende bleiben erhalten.

In keinem Bestand und keiner Lesung verbindet eine anonyme Kante dieselbe
Quelle zwischen den disjunkten Zieluniversen.

## Interpretation

Exakte Wiederkehr ist eine reale Eigenschaft der selbstsegmentierten
Rangzyklusformen. Sie ist jedoch nicht individuell quelltragend. Die erneut
auftretenden Formen bilden offenbar eine allgemeine Schicht der Felddynamik,
nicht die gesuchte organische Relevanz der jeweiligen Feldgeschichte.

Das Ergebnis trennt zwei Begriffe:

```text
Eine Form kommt erneut vor.          getragen
Ihre Wiederkehr macht sie relevant.  nicht getragen
```

Wiederholung allein darf daher nicht als semantische Verdichtung, Erfahrung
oder Wachstumsrecht einer Memory gelesen werden.

## Befund

Getragen sind:

- exakte staerkenormierte Formwiederkehr in allen 1.472 Stroemen,
- median sieben Wiederkehrbeobachtungen pro Strom,
- eine kleine wiederkehrende Schicht innerhalb hoher Formenvielfalt,
- eine schwellenfreie Kanonisierung ohne Aehnlichkeitsfamilien,
- gefuellte Wiederkehrprofile in allen Quelluniversen,
- direkte Reproduktion der All-Episoden-Begrenzung aus 2112.

Nicht getragen sind:

- universumsuebergreifende Quelltrennung durch exakte Wiederkehr,
- gleichquellige anonyme Nachbarschaften,
- ein Vorteil gegenueber der All-Episoden-Lesung,
- exakte Wiederkehr als organische Relevanz- oder Wachstumsbedingung,
- eine neue Rangzyklus-Memory,
- Semantik, Rueckwirkung oder Handlung.

2115 zeigt, dass Mehrfachbeobachtung allein den offenen Engpass aus 2114 nicht
schliesst. Exakte Episodenformwiederkehr ist vorhanden, aber sie bewahrt nicht
die individuelle relationale Feldgeschichte zwischen getrennten
Zieluniversen.

Damit ist einfache Wiederkehr ebenso wenig als semantische Wachstumsregel
fundiert wie Schliessung oder Neuheitsstaerke.

## Reproduzierbare Ausgaben

- `2115_MCM_MEHREPISODEN_EXAKTE_FORMWIEDERKEHR.paths.csv`
- `2115_MCM_MEHREPISODEN_EXAKTE_FORMWIEDERKEHR.edges.csv`
- `2115_MCM_MEHREPISODEN_EXAKTE_FORMWIEDERKEHR.summary.csv`

Der Runner ist `tools/run_mcm_multi_episode_exact_recurrence.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
