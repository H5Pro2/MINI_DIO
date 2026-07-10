# 2092 - Unabhängiger Holdout des MCM-Relationslebenslaufs

> **Methodischer Nachtrag 2093:** Die damalige Fortsetzungsfähigkeit über das
> spätere Maximalalter schloss Kanten ohne gleichzeitig erreichtes nächstes
> Relationsalter ein. Nach exakter Korrektur setzen sich getragene Kanten zu
> 62,23 Prozent und neue zu 63,20 Prozent fort; die Richtung ist damit leicht
> negativ. Die Teilreplikation ist nicht bestätigt. Siehe
> [Befund 2093](2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.md).

## Zweck

Befund 2091 fand im passiven Relationslebenslauf einen kleinen inneren
Fortsetzungsvorteil: Bereits getragene Kanten setzten sich beim nächsten
Relationsalter häufiger fort als neue Kontakte. Diese Prüfung beruhte jedoch
auf demselben Weltbestand wie die Entwicklung des Lebenslaufs.

2092 prüft dieselbe vorab festgelegte Vergleichslogik in neuen realen Welten.
Außenwerte, Chartmuster und Handlungsergebnisse sind keine Zielgrößen. Gemessen
wird ausschließlich, wie sich die aus dem MCM-Feld entstandenen
Relationsnachbarschaften in ihrer eigenen Ereigniszeit fortsetzen.

## Unabhängiger Weltblock

Der Holdout besteht aus 60 nicht überlappenden realen `5m`-Welten:

| Merkmal | Umfang |
|---|---:|
| Assets | DOGE, PAXG, XRP |
| Jahre | 2024, 2025 |
| Quelldateien | 6 |
| Fenster je Quelle | 10 |
| Zeilen je Welt | 1.000 |
| Gesamtwelten | 60 |

Diese Daten wurden in der Befundkette 2085 bis 2091 nicht verwendet. Die
Weltreihenfolge wurde deterministisch aus einem festen Holdout-Schlüssel
gebildet. Es gibt keine synthetischen Welten und keine Auswahl anhand des
Ergebnisses.

## Exakte Lebenslaufprüfung

Der Feldlauf erzeugt 1.932 Relationen und 7.807 Relationsereignisse. Aus 1.046
Relationen mit auswertbarer Eigenzeit entstehen 159.199
Lebenslaufbeobachtungen auf 137.353 unterschiedlichen Kanten.

Die archivierten Relationsereignisse stimmen vollständig mit der laufenden
Memory überein. Auch alle Lebenslaufbeobachtungen lassen sich exakt aus den
Relationsereignissen rekonstruieren:

| Integritätsmerkmal | Ergebnis |
|---|---:|
| erwartete Lebenslaufbeobachtungen | 159.199 |
| gespeicherte Lebenslaufbeobachtungen | 159.199 |
| fehlende Beobachtungen | 0 |
| unerwartete Beobachtungen | 0 |
| Ereignisse vor ihrem Weltbeginn | 0 |

## Unabhängiger Primärvergleich

34 Altersübergänge von Alter 3 bis 38 enthalten gleichzeitig getragene und
neue fortsetzungsfähige Kanten.

| Merkmal | getragen | neu |
|---|---:|---:|
| fortsetzungsfähige Kanten | 6.904 | 7.168 |
| beim nächsten Alter fortgesetzt | 2.535 | 2.512 |
| Fortsetzungsrate | 0,3672 | 0,3504 |

Der absolute Abstand beträgt `0,0167` oder 1,67 Prozentpunkte. Getragene
Kanten setzen sich relativ `1,0477`-mal so häufig fort. Der gemeinsame
Mantel-Haenszel-Odds-Faktor über die Altersschichten beträgt `1,0543`.

Die Richtung aus 2091 erscheint damit erneut, der Effekt ist aber deutlich
kleiner:

| Merkmal | 2091: BTC/SOL `30m` | 2092: DOGE/PAXG/XRP `5m` |
|---|---:|---:|
| Fortsetzungsrate getragen | 0,3712 | 0,3672 |
| Fortsetzungsrate neu | 0,3409 | 0,3504 |
| absoluter Abstand | 0,0303 | 0,0167 |
| relatives Verhältnis | 1,0887 | 1,0477 |
| gemeinsamer Odds-Faktor | 1,1499 | 1,0543 |

## Nullkontrollen

### Altersstratifizierte Kantenlabel

Die Null erhält pro Alter die aktuellen Kanten, die Zahl der getragenen
Kanten und die Zahl der späteren Fortsetzungen. Nur die Label `getragen` und
`neu` werden innerhalb derselben Altersschicht 2.000-mal neu verteilt.

Erwartet werden 2.492,80 fortgesetzte getragene Kanten bei einer
Standardabweichung von 28,22; beobachtet werden 2.535. Der analytische
einseitige Wert beträgt `p = 0,0674`, der empirische Wert
`p = 128/2001 = 0,0640`. Diese Primärkontrolle überschreitet damit knapp die
vorher festgelegte Grenze von 0,05.

### Relationsidentität des Zukunftsgraphen

Die zweite Null erhält je Alter den vollständigen Zukunftsgraphen mit seiner
Kantenzahl und Gradstruktur, permutiert aber seine Relationsidentitäten. Unter
1.000 Permutationen beträgt die mittlere Ratendifferenz `0,00115`; die
beobachtete Differenz von `0,01673` wird nur dreimal erreicht oder
überschritten. Mit Korrektur ergibt sich `p = 4/1001 = 0,003996`.

Die konkrete relationale Identität enthält somit auch im unabhängigen Block
mehr Fortsetzungsinformation als die bloße Form des Zukunftsgraphen. Das
reicht jedoch nicht aus, um die knapp verfehlte primäre Labelkontrolle als
vollständig repliziert zu behandeln.

## Sekundäre Alterssensitivität

| Altersbereich | getragen | neu | relatives Verhältnis | einseitiges `p` |
|---|---:|---:|---:|---:|
| 3 bis 4 | 0,3586 | 0,3526 | 1,0171 | 0,2664 |
| 5 bis 9 | 0,4386 | 0,3526 | 1,2438 | 0,0313 |
| 10 bis 20 | 0,4211 | 0,2833 | 1,4861 | 0,0033 |
| 21 bis 38 | 0,4848 | 0,4111 | 1,1794 | 0,7417 |

Ab Alter 5 ist der beobachtete Unterschied größer. Diese Aufteilung ist eine
nachgelagerte Sensitivität mit schnell kleiner werdenden Mengen. Sie begründet
weder ein festes Reifealter noch eine Auswahl-, Gewichtungs- oder
Verstärkungsregel.

## Zusammenhängende Altersläufe

18.602 Kanten werden bei mehr als einem Relationsalter beobachtet. Davon
besitzen 17.681 oder `95,05 %` mindestens einen unmittelbar
aufeinanderfolgenden Alterskontakt; 921 kehren ausschließlich mit Lücken
zurück. Die längste zusammenhängende Folge umfasst 12 Relationsalter. Lange
Folgen bleiben selten.

## Befund

Getragen sind:

- dieselbe Richtung des kleinen Fortsetzungsvorteils wie in 2091,
- exakte Bildung und Rekonstruktion des Lebenslaufs in einem unabhängigen
  realen Weltbestand,
- Fortsetzungsinformation der konkreten Relationsidentität über die reine
  Graphform hinaus,
- überwiegend direkt aufeinanderfolgende statt nur lückenhafte Wiederkehr.

Nicht getragen sind:

- eine vollständige Replikation der primären Kantenlabel-Evidenz,
- ein gleich starker Effekt wie im Entwicklungsbestand,
- ein festes Reifealter oder dauerhaft stabile Relationsmitglieder,
- eine Rücklesung, Selbstverstärkung oder semantische Entscheidung,
- Feld-, Wahrnehmungs- oder Handlungswirkung.

2092 ist damit eine Teilreplikation. Der Lebenslauf bewahrt eine schwache
eigene Fortsetzungsordnung, deren Stärke zwischen unabhängigen Weltbeständen
variiert. Für einen passiven Stabilitätsmarker oder eine Rückwirkung in das
Feld ist die Evidenz noch nicht robust genug. An der Runtime wird nichts
geändert.

## Reproduzierbare Ausgaben

- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.order.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.integrity.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.transitions.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.sensitivity.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.null.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.runs.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.comparison.csv`
- `2092_MCM_RELATIONSLEBENSLAUF_UNABHAENGIGER_HOLDOUT.summary.csv`
- `data/2092_mcm_lifecycle_holdout_events.zip`

Das ZIP enthält ausschließlich die kompakte Holdout-Reihenfolge, die
Relationsereignisse und die rekonstruierten Lebenslaufbeobachtungen. Entpackte
Welt-, Debug- und Memory-Dateien werden nach dem Lauf entfernt und nicht
versioniert. MINI_DIO liest die Auswertung nicht zurück.
