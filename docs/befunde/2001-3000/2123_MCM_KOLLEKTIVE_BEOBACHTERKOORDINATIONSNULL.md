# 2123 - Kollektive Beobachterkoordinationsnull

## Fragestellung

2122 fand reproduzierbare gemeinsame Schliessungszeiten zwischen der relativen
Aktivierungsstuetze und der relativen Nachhallstuetze. Dieser Befund kann zwei
verschiedene Ursachen haben:

1. Jedes Neuron traegt fuer sich bereits eine lokale Aktivierungs-Nachhall-
   Kopplung, deren blosse Addition den Gesamteffekt erzeugt.
2. Die zeitliche Abstimmung mehrerer Neuronen traegt einen zusaetzlichen
   kollektiven Anteil.

2123 trennt diese Moeglichkeiten mit einer strengeren passiven Null.

## Erhaltene lokale Spur

Fuer jeden der 1.472 fortgefuehrten Feldpfade wird die Zielwelt einmal durch
das unveraenderte MCM-Feld erzeugt. Anschliessend wird pro Neuron die gesamte
lokale Zeitfolge zirkulaer verschoben. Aktivierung und Nachhall desselben
Neurons erhalten immer exakt denselben Versatz.

Damit bleiben fuer jedes einzelne Neuron vollstaendig erhalten:

- alle Aktivierungswerte,
- alle Nachhallwerte,
- jede lokale Aktivierungs-Nachhall-Paarung,
- die komplette lokale zeitliche Reihenfolge bis auf ihren zyklischen
  Startpunkt,
- Zielweltlaenge und Anzahl der Neuronen.

Zwischen verschiedenen Neuronen werden unabhaengige Versatzwerte gezogen. Nur
ihre kollektive Gleichzeitigkeit wird geloest. Die Null wird ausschliesslich
auf der eingefrorenen Zielspur gebildet und schreibt weder in das Feld noch in
eine Memory zurueck.

## Vergleichsgroesse

Die Null kann die Anzahl der aus der Gesamtpopulation gelesenen
Stuetzmengenereignisse veraendern. Deshalb wird nicht die rohe Gleichzeitigkeit
allein verglichen. Fuer Beobachtung und jede Null wird zuerst die jeweils
eigene Erwartung unter einer nicht-nulligen zirkulaeren Verschiebung ihrer
beiden Ereignisfolgen abgezogen:

`Synchronitaetsueberschuss = Gleichzeitigkeit - eigene Kadenz-Erwartung`

Erst dieser normierte Ueberschuss wird zwischen realer Kollektivspur und
neuronlokal erhaltener Null verglichen. Pro Pfad werden 32 deterministische
Kollektivnullen erzeugt.

## Rueckwirkungs-Audit

| Pruefung | Ergebnis |
| --- | ---: |
| fortgefuehrte Feldpfade | 1.472 |
| Zielspur nach allen Nullbildungen identisch | 1.472 / 1.472 |
| Feldendzustand nach allen Nullbildungen identisch | 1.472 / 1.472 |
| lokale Aktivierungs-Nachhall-Paarung erhalten | 1.472 / 1.472 |
| Kollektivnullen je Pfad | 32 |
| Memory-, Viranz- oder Handlungseinfluss | 0 |

## Ergebnis

| Bestand | Universum | beobachteter Ueberschuss | Nullmittel | Nullmaximum | Differenz zum Nullmittel | Quellen + / - | p |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2091 | A | 3.987,34 | 3.098,09 | 3.304,06 | +889,25 | 48 / 0 | 0,030303 |
| 2091 | B | 5.101,62 | 3.358,26 | 3.529,63 | +1.743,36 | 48 / 0 | 0,030303 |
| 2091 | gesamt | 9.088,96 | 6.456,35 | 6.715,47 | +2.632,61 | 48 / 0 | 0,030303 |
| 2092 | A | 4.234,14 | 3.169,60 | 3.337,23 | +1.064,54 | 44 / 0 | 0,030303 |
| 2092 | B | 3.865,59 | 2.839,89 | 3.063,12 | +1.025,70 | 44 / 0 | 0,030303 |
| 2092 | gesamt | 8.099,74 | 6.009,49 | 6.264,16 | +2.090,24 | 44 / 0 | 0,030303 |

Der beobachtete Synchronitaetsueberschuss liegt in jedem Bestand und jedem
getrennten Zieluniversum oberhalb aller 32 Kollektivnullen. Auch quellenweise
ist die Richtung vollstaendig: 48 von 48 Entwicklungsquellen und 44 von 44
Holdoutquellen liegen ueber ihrem jeweiligen Nullmittel.

Der empirische Wert `0,030303` ist die kleinste mit 32 Nullwiederholungen
aufloesbare obere Wahrscheinlichkeit `(0 + 1) / (32 + 1)`. Das gepruefte
Stuetzmengenpaar wurde wegen seines starken 2122-Befunds vor dieser Gegenprobe
festgelegt. 2123 ist deshalb eine mechanische Zerlegung desselben Befunds und
kein neuer blinder Daten-Holdout.

Auf der feineren Pfadebene sind 594 von 768 Entwicklungspfaden und 532 von 704
Holdoutpfaden positiv. Die Ordnung ist damit breit, aber nicht als starres
Gesetz in jedem einzelnen Kontakt vorhanden.

## Einordnung

Der starke 2122-Befund laesst sich nicht allein durch voneinander unabhaengige
lokale Aktivierungs-Nachhall-Spuren erklaeren. Die zeitliche Abstimmung der
Neuronen traegt einen zusaetzlichen reproduzierbaren Anteil. Er bleibt sichtbar
ueber:

- zwei vollstaendig getrennte Datenbestaende,
- beide disjunkten Zieluniversen,
- alle 92 Quellen,
- eine Null, die jede lokale Aktivierungs-Nachhall-Paarung erhaelt.

Damit wird die Mehrprojektionsspur aus 2122 zu einem Kandidaten fuer
kollektive MCM-Feldzeitkoordination. Der Begriff `kollektiv` bezeichnet hier
jedoch noch die gesamte gleichzeitige Population. Die aktuelle Null trennt
nicht, ob der Zusatzanteil aus gemeinsamer rezeptorischer Aussenanregung, aus
der internen neuronalen Nachbarschaftskopplung oder aus ihrem Zusammenspiel
entsteht.

2123 weist weder Quantenverhalten noch Bewusstsein, Viranz oder ein
unsichtbares Objekt nach. Es begrenzt enger: Die beobachterstabile Ordnung ist
nicht rein lokal und nicht nur ein Auswertungsartefakt. Eine Memory,
Bedeutungsbindung oder Handlung wird daraus nicht abgeleitet.

## Reproduzierbarkeit

Ausgaben:

- `2123_MCM_KOLLEKTIVE_BEOBACHTERKOORDINATIONSNULL.paths.csv`
- `2123_MCM_KOLLEKTIVE_BEOBACHTERKOORDINATIONSNULL.sources.csv`
- `2123_MCM_KOLLEKTIVE_BEOBACHTERKOORDINATIONSNULL.summary.csv`

SHA-256:

- `paths`: `8782137AB2E050FA5AA227EC58F982B443C5B961109169C1794E2E79A3B21578`
- `sources`: `C2832521A2311A02DAF6EC7B237DD2C8DE3F485526438099EE8A6A7B650887E7`
- `summary`: `3A8ACEC4BD3730EAFAB18E725E430FA774A600F9320D1CC10EC765000B4964DA`

Runner: `tools/run_mcm_collective_observer_coordination_null.py`

Test: `tests/test_mcm_collective_observer_coordination_null.py`
