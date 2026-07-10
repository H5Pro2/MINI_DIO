# 2080 - MCM-Nachbarschaft: Persistenz und Peripherie

## Zweck

Befund 2079 integrierte eine passiv wachsende Nachbarschafts-Memory. Diese Prüfung untersucht, ob sich aus ihrer eigenen Erfahrung ohne feste Reifeschwelle eine belastbare Trennung zwischen dauerhaftem Kern und einmaliger Peripherie bildet.

Untersucht werden ausschließlich innere Beziehungsqualitäten:

- Zahl bestätigender Weltpaare,
- Kontextbreite über Weltläufe,
- Zahl verschiedener Weltabschlüsse mit neuer Bestätigung,
- Tragung in den drei inneren Profilräumen,
- Verhältnis von Bestätigung zu bisherigem Beziehungsalter,
- Dauer seit der letzten Bestätigung.

Die 26 strengen Relationen aus Befund 2078 werden erst nach dem Lauf als Vergleichsgruppe markiert. Sie beeinflussen weder Wachstum noch Speicherung.

## Prüfbasis

Wie in Befund 2079 wachsen zwei getrennte fortlaufende Memories durch dieselben 81 Welten:

```text
forward: W001 -> W002 -> ... -> W081
reverse: W081 -> W080 -> ... -> W001
```

Am Ende enthalten sie 2.046 beziehungsweise 2.085 Relationen. Alle 26 Vergleichsrelationen sind in beiden Memories vorhanden.

## Technische Sicherung der Kontextbreite

Die Herkunftsbreite einer Relation wird nun verlustfrei als Ganzzahl-Bitmaske der Laufnummern gespeichert. Ein zusätzlicher Reload-Test prüft die Bits 1, 60 und 81 über Speichern, Laden und weiteres Wachstum.

Eine erste Auswertung wurde verworfen, weil die Bitmaske fälschlich über Gleitkomma konvertiert worden war und oberhalb von 53 Bits Genauigkeit verlor. Die korrigierte Implementierung verwendet ausschließlich Ganzzahlarithmetik. In den endgültigen 4.131 Relationszeilen liegt keine Paardichte über 1; der Maximalwert beträgt exakt 1.

Die vollständigen lokalen Memories sinken durch die kompaktere Darstellung auf 12,06 MB beziehungsweise 12,12 MB. Das reduziert die Dateigröße, ersetzt aber noch keine organische Verdichtung.

## Kern und Peripherie

| Achse | Median Kern vorwärts/rückwärts | Median Peripherie vorwärts/rückwärts |
|---|---:|---:|
| bestätigende Weltpaare | 391 / 371,5 | 2 / 2 |
| getragene Welten | 45,5 / 46 | 3 / 3 |
| bestätigende Weltabschlüsse | 44 / 41,5 | 2 / 2 |
| Bestätigung im Beziehungsalter | 0,560 / 0,549 | 0,077 / 0,077 |
| Aktualität | 1,000 / 1,000 | 0,091 / 0,091 |

Der Kern liegt auf allen fünf Persistenz- und Breitenachsen deutlich über der typischen Peripherie.

## Trennschärfe

Die AUC misst schwellenfrei, wie häufig eine zufällige Kernrelation auf der jeweiligen Achse über einer zufälligen Peripherierelation liegt.

| Achse | AUC vorwärts | AUC rückwärts |
|---|---:|---:|
| bestätigende Weltpaare | 0,984 | 0,984 |
| getragene Welten | 0,961 | 0,961 |
| bestätigende Weltabschlüsse | 0,975 | 0,973 |
| Bestätigung im Beziehungsalter | 0,930 | 0,935 |
| Aktualität | 0,907 | 0,890 |

Das ist eine starke statistische Schichtung. Dennoch erzeugt keine einzelne Achse eine saubere Grenze: Auf jeder Achse existiert mindestens eine Peripherierelation oberhalb des schwächsten Kernwertes.

Zwei scheinbar naheliegende Größen kehren die Lesung sogar um:

- Der Median der Profilraum-Balance liegt im Kern bei 0,561/0,572, in der Peripherie aber bei 1,000/1,000.
- Der Median der Paardichte liegt im Kern bei 0,365/0,401, in der Peripherie bei 0,667/0,667.

Viele periphere Einmalbeziehungen besitzen perfekte Balance oder Dichte, weil sie nur in sehr wenigen Kontexten beobachtet wurden. Balance und Dichte ohne Breite sind deshalb keine Reife.

## Reihenfolgenstabilität der Achsen

| Achse | Spearman vorwärts zu rückwärts |
|---|---:|
| bestätigende Weltpaare | 0,975 |
| getragene Welten | 0,974 |
| bestätigende Weltabschlüsse | 0,804 |
| Profilraum-Balance | 0,915 |
| Paardichte | 0,966 |
| Bestätigung im Beziehungsalter | 0,341 |
| Aktualität | 0,305 |

Breite und absolute Wiederkehr sind robust. Altersverhältnis und aktuelle Nichtbestätigung hängen deutlich stärker davon ab, welche Welten zuletzt erlebt wurden. Eine direkte Vergessenswirkung aus Aktualität wäre damit stark pfadabhängig.

## Schwellenfreier Pareto-Test

Der Pareto-Test verwendet nur die drei robusten Achsen Weltpaartragung, Weltbreite und bestätigende Weltabschlüsse. Es gibt keine Gewichtung und keinen Grenzwert. Eine Relation dominiert eine andere nur, wenn sie auf allen drei Achsen mindestens gleich und auf einer Achse stärker ist.

- Der mediane Kern dominiert vorwärts 1.986 von 2.020 Peripherierelationen.
- Rückwärts dominiert der mediane Kern 2.022 von 2.059 Peripherierelationen.
- Selbst die schwächste Kernrelation dominiert noch 1.696 beziehungsweise 1.759 Peripherierelationen.
- Der mediane Kern wird zugleich von sechs peripheren Ausreißern dominiert.
- Vier Kernrelationen sind vorwärts und drei rückwärts von keiner Peripherierelation dominiert.
- Drei dieser Pareto-Spitzen sind in beiden Erfahrungsrichtungen identisch.

Es entsteht somit keine binäre Kern-/Restgrenze, sondern eine Schichtung:

```text
kleine stabile Pareto-Spitze
breiter stark getragener Reifebereich
überlappende periphere Ausreißer
große schwach bestätigte Peripherie
```

## Befund

Die passive Nachbarschafts-Memory bildet organisch eine deutliche Reifungsordnung aus. Wiederkehr, Weltbreite und bestätigende Weltabschlüsse tragen diese Ordnung robust und weitgehend reihenfolgenstabil.

Nicht fundiert ist eine harte Reifeklasse oder ein direktes Vergessen:

- Kern und Peripherie überlappen,
- periphere Ausreißer können einzelne oder mehrere Kernrelationen übertreffen,
- Aktualität und Bestätigungsalter sind stark erfahrungsreihenfolgeabhängig,
- hohe Balance oder Dichte kann aus Datenarmut statt Reife entstehen.

Der Lauf verändert deshalb weder Feldwirkung noch aktive Auswahl und entfernt keine Relation. Er belegt eine kontinuierliche, mehrschichtige Reifungstopologie, aber noch keine organisch fundierte Abbauentscheidung.

Reproduzierbare Ausgaben:

- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.relations.csv`
- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.groups.csv`
- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.separation.csv`
- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.order.csv`
- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.pareto.csv`
- `2080_MCM_NACHBARSCHAFT_PERSISTENZ_UND_PERIPHERIE.summary.csv`
