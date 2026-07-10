# 2110 - Intrinsische Selbstlesbarkeit der MCM-Form

## Zweck

Die Befunde 2107 bis 2109 zeigen eine robuste quellgebundene Form der
Feldkontinuitaet. Diese Form wurde jedoch als Differenz zwischen einem
kontinuierlichen Feld und einem parallel berechneten Resetfeld gemessen.

Das ist eine saubere Forschungsgegenprobe, aber keine organisch zugaengliche
Eigenwahrnehmung:

```text
DIO besitzt im laufenden Feld
keine parallel erzeugte Gegenwelt ohne Vergangenheit.
```

2110 entfernt deshalb das Resetfeld vollstaendig. Geprueft wird, ob dieselbe
Quellform allein aus den tatsaechlich aufeinanderfolgenden inneren Zustaenden
der kontinuierlichen Feldinstanz lesbar bleibt.

## Intrinsisches Formprofil

Pro Quell-Ziel-Pfad wird nur verglichen:

```text
eigene neuronale Rangordnung im vorherigen Tick
gegen
eigene neuronale Rangordnung im aktuellen Tick
```

Bei zwoelf Neuronen bestehen 66 paarweise Rangbeziehungen. Jede tatsaechliche
Aenderung wird als eine von sechs gerichteten Formen zwischen `kleiner`,
`gleich` und `groesser` gezaehlt. Exakte Gleichstaende bleiben erhalten.

Das Profil verwendet nicht:

- ein Reset- oder Nullfeld,
- Herkunftslabel oder Weltname,
- Asset oder Jahr,
- Preis, Richtung oder Volumenbedeutung,
- Feldlernen oder Memory,
- Handlung oder Rueckwirkung.

Damit besteht das Forschungsprofil ausschliesslich aus Informationen, die im
laufenden MCM-Feld selbst vorhanden sind.

## Praefixskala statt fester Laufzeit

Es wird keine einzelne Beobachtungsdauer als Organismusregel gewaehlt. Die
intrinsischen Rangwechsel werden kumulativ ueber die Skala

```text
1, 2, 4, 8, 16, 32 und 64 Kontaktticks
```

gelesen. Jeder groessere Punkt enthaelt alle vorherigen Beobachtungen. Die
Skala dient nur dazu, sichtbar zu machen, wann Quellform gegen neue
Kontakterfahrung traegt oder zerfaellt.

## Getrennte Zieluniversen

Die Pruefung verwendet dieselben disjunkten Zieluniversen aus Befund 2109:

- 48 Vorweltfelder und zweimal acht Zielwelten im 2091-Bestand,
- 44 Vorweltfelder und zweimal acht Zielwelten im 2092-Holdout,
- insgesamt 1.472 kontinuierliche Quell-Ziel-Pfade.

Fuer jede Vorwelt werden die intrinsischen Profile innerhalb jedes Universums
addiert und durch ihre gesamte Wechselzahl geteilt. Verglichen wird nur die
relative Form, nicht die Menge der inneren Bewegung.

Kein Profil ist leer. Bereits bei Tick 1 reicht die aggregierte Wechselmenge
je Quelle im 2091-Bestand von 20 bis 91 und im Holdout von 13 bis 88. Eine
gleiche Gesamtmasse kann den Befund daher nicht erklaeren.

## Verteilungsweite Quelltrennung

| Bestand | Ticks | AUC A nach B | AUC B nach A |
|---|---:|---:|---:|
| 2091 | 1 | 0,976 | 0,975 |
| 2091 | 2 | 0,976 | 0,966 |
| 2091 | 4 | 0,966 | 0,959 |
| 2091 | 8 | 0,805 | 0,730 |
| 2091 | 16 | 0,807 | 0,654 |
| 2091 | 32 | 0,648 | 0,583 |
| 2091 | 64 | 0,522 | 0,518 |
| 2092 | 1 | 0,976 | 0,975 |
| 2092 | 2 | 0,967 | 0,968 |
| 2092 | 4 | 0,958 | 0,953 |
| 2092 | 8 | 0,904 | 0,925 |
| 2092 | 16 | 0,821 | 0,785 |
| 2092 | 32 | 0,707 | 0,747 |
| 2092 | 64 | 0,798 | 0,835 |

Alle 28 gerichteten AUC-Werte liegen oberhalb jeder ihrer 4.096 globalen
Herkunftslabelnullen. Auch der kleine Basisrest bei Tick 64 bleibt formal
getrennt: AUC 0,522 liegt dort ueber der hoechsten Null von 0,515.

Diese AUC beschreibt eine verteilungsweite Restordnung. Sie ist noch kein
selbstorganisierter Nachbarschaftsgraph.

## Anonymer gegenseitiger Nachbarschaftsgraph

Fuer jeden Skalenpunkt werden alle Profile aus Universum A und B global
verglichen. Ein Knoten aus A und ein Knoten aus B erhalten nur dann eine Kante,
wenn beide einander bei ungewichteter Manhattan-Distanz gegenseitig am
naechsten sind. Exakte Ties bleiben als mehrere Kanten erhalten.

Der Graph verwendet weder Herkunftslabel noch Asset-/Jahresgruppen. Erst nach
seiner Fertigstellung wird geprueft, welche Kanten zwei Profile derselben
Vorwelt verbinden.

### 2091-Bestand

| Ticks | gegenseitige Kanten | gleiche Quelle nachtraeglich | Anteil | Labelnull-p |
|---:|---:|---:|---:|---:|
| 1 | 32 | 20 | 62,5 % | 0,000244 |
| 2 | 31 | 20 | 64,5 % | 0,000244 |
| 4 | 17 | 12 | 70,6 % | 0,000244 |
| 8 | 4 | 1 | 25,0 % | 0,0757 |
| 16 | 2 | 0 | 0 % | 1,0 |
| 32 | 1 | 0 | 0 % | 1,0 |
| 64 | 1 | 0 | 0 % | 1,0 |

### 2092-Holdout

| Ticks | gegenseitige Kanten | gleiche Quelle nachtraeglich | Anteil | Labelnull-p |
|---:|---:|---:|---:|---:|
| 1 | 32 | 15 | 46,9 % | 0,000244 |
| 2 | 24 | 15 | 62,5 % | 0,000244 |
| 4 | 18 | 14 | 77,8 % | 0,000244 |
| 8 | 10 | 3 | 30,0 % | 0,00122 |
| 16 | 3 | 3 | 100 % | 0,000244 |
| 32 | 2 | 2 | 100 % | 0,000976 |
| 64 | 4 | 2 | 50,0 % | 0,00513 |

Der robuste gemeinsame Kern beider Datenbestaende liegt bei 1 bis 4 Ticks. In
diesem Bereich entstehen ohne Label, Reset oder Marktgruppe jeweils 12 bis 20
beziehungsweise 14 bis 15 gleichquellige gegenseitige Kanten. Jede Zahl liegt
oberhalb aller 4.096 Labelnullen.

Ab Tick 8 zerfaellt diese Topologie im 2091-Bestand. Der Holdout behaelt
wenige, teils reine Kanten bis Tick 64. Die spaete Holdoutform ist jedoch sehr
schmal und kein gleich breiter Ersatz fuer den fruehen gemeinsamen Kern.

## AUC und Topologie sind zu trennen

Die verteilungsweite AUC bleibt laenger ueber ihrer Null als der anonyme
gegenseitige Graph. Das bedeutet:

- schwache Quellinformation kann noch ueber viele Profile verteilt sein,
- ohne dass daraus stabile lokale gegenseitige Nachbarschaften entstehen.

Fuer eine organische Topologie ist deshalb nicht jede statistisch messbare
Restinformation ausreichend. Der belastbarere Traeger ist die tatsaechlich
entstehende gegenseitige Naehe.

## Befund

Getragen sind:

- resetfreie Quellinformation aus aufeinanderfolgenden eigenen Feldzustaenden,
- sehr hohe universumsuebergreifende Trennung bei 1 bis 4 Kontaktticks,
- ein globaler anonymer gegenseitiger Nachbarschaftsgraph,
- 12 bis 20 und 14 bis 15 gleichquellige Kanten im gemeinsamen Fruehbereich,
- Reproduktion in Entwicklungsbestand und unabhaengigem Holdout,
- Zerfall oder starke Ausduennung unter wachsender neuer Erfahrung.

Nicht getragen sind:

- bereits implementierte Selbstbeobachtung durch MINI_DIO,
- eine endogen bestimmte Start- oder Abschlussgrenze des Formprofils,
- eine feste Vier-Tick-Regel,
- dauerhafte Identitaet jeder Vorwelt,
- ein bereits wachsendes intrinsisches Memory,
- Semantik, autonome Aktivitaet oder Handlung.

2110 schliesst die wichtigste organische Luecke der vorherigen Befunde: Die
quellgebundene Form ist nicht nur durch eine aeussere Resetgegenprobe messbar.
Sie kann aus der tatsaechlichen inneren Bewegung des kontinuierlichen Feldes
selbst rekonstruiert werden.

Damit liegt erstmals ein mechanisch selbstlesbarer Traeger fuer organisch
entstehende Innenidentitaet vor. MINI_DIO nutzt diesen Traeger noch nicht. Es
fehlt insbesondere eine feldinterne, nicht hart gesetzte Grenze dafuer, wann
eine solche Formbeobachtung als eigene Episode geschlossen wird.

## Reproduzierbare Ausgaben

- `2110_MCM_INTRINSISCHE_FORM_SELBSTLESBARKEIT.edges.csv`
- `2110_MCM_INTRINSISCHE_FORM_SELBSTLESBARKEIT.summary.csv`

Der Runner ist `tools/run_mcm_intrinsic_form_self_readability.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
