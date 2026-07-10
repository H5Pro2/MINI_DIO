# 2107 - Quellgebundene Form in der MCM-Feldkontinuitaet

## Zweck

Befund 2106 zeigt, dass eine fortgefuehrte MCM-Feldinstanz kurz die exakte
Rangtopologie ihrer Neuronen veraendert, obwohl DIOs bestehende Syntax gleich
bleibt. 2107 prueft, ob diese Mikrotopologie nur allgemeiner Nachhall ist oder
Information ueber den konkreten vorherigen Feldzustand traegt.

Die Frage lautet:

```text
Erzeugen verschiedene Vorwelten
unter denselben Zielreizen
unterscheidbare innere Formspuren?
```

Weltname, Asset, Jahr und Fensterstart werden dem Feld nicht gegeben. Sie
dienen erst nach dem Lauf als Prueflabel. Es gibt kein Feldlernen, keine
Memory-Ruecklesung und keine Handlung.

## Datenblinde Trennung

Jeder der beiden unabhaengigen Bestaende wird getrennt behandelt. Die Welten
werden ausschliesslich nach dem SHA-256 ihres vorhandenen Weltenschluessels
geordnet. Die ersten acht bilden Zielwelten, alle uebrigen die zu pruefenden
Vorweltidentitaeten:

| Bestand | Zielwelten | Vorwelten |
|---|---:|---:|
| 2091-Bestand | 8 | 56 |
| 2092-Holdout | 8 | 52 |

Die acht Zielwelten werden ohne Ergebniswissen in zwei disjunkte Vierergruppen
A und B geteilt. Keine Zielwelt ist zugleich eine Vorweltidentitaet.

Jede Vorwelt wird als fertiger Feldzustand auf alle acht frischen Zielwelten
gefuehrt. Geprueft wird nur die staerkste in 2106 getragene Bedingung ohne
reizfreie Luecke. Daraus entstehen 448 Quell-Ziel-Pfade im 2091-Bestand und
416 im Holdout.

## Schwellenfreies Formprofil

Bei zwoelf Neuronen bestehen 66 paarweise Rangbeziehungen. Fuer jeden Tick
wird exakt gelesen, welche Beziehung im kontinuierlichen Feld anders liegt als
im Resetfeld. Eine Beziehung kann in sechs gerichteten Formen zwischen
`kleiner`, `gleich` und `groesser` wechseln.

Damit entsteht pro Quell-Ziel-Pfad ein 396-dimensionales Zaehlerprofil:

```text
66 Neuronenpaare
x 6 moegliche gerichtete Rangwechsel
= 396 beobachtbare Formstellen
```

Es gibt keine Epsilon-, Reife- oder Bedeutungsgrenze. Exakte Gleichstaende
bleiben erhalten. Die vier Profile einer Zielgruppe werden je Vorwelt nur
addiert.

## Getrennte Staerke- und Formpruefung

Zwei Lesungen werden getrennt:

- `raw`: Anzahl und Lage aller Rangwechsel; Staerke und Form bleiben erhalten.
- `shape`: Jede Kohorte wird durch ihre gesamte Wechselzahl geteilt; nur die
  relative Verteilung der Rangwechsel bleibt erhalten.

Die Formlesung verhindert, dass eine Vorwelt allein durch mehr oder weniger
Nachhall wiedererkannt wird.

Die Profile aus A und B werden mit ungewichteter Manhattan-Distanz verglichen.
Die Identitaets-AUC gibt an, wie oft das Profil derselben Vorwelt naeher liegt
als ein fremdes Profil. Exakte Distanzgleichstaende zaehlen halb. Eine
ungebundene Zuordnung liegt bei AUC 0,5.

## Globale Quelltrennung

Die staerkenormierte Form liest dieselbe Vorwelt ueber die beiden disjunkten
Zielgruppen in beiden Richtungen besser als Fremdvorwelten:

| Bestand | Richtung | Kandidaten | Median Identitaetsrang | mittlere AUC | eindeutig naechste Identitaet |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 56 | 15 | 0,620 | 4 |
| 2091 | B nach A | 56 | 11 | 0,737 | 4 |
| 2092 | A nach B | 52 | 4 | 0,874 | 9 |
| 2092 | B nach A | 52 | 3 | 0,891 | 10 |

Die gleiche qualitative Richtung erscheint bereits in den rohen Profilen.
Dass sie nach der Staerkenormierung bestehen bleibt, zeigt eine Verteilung der
Rangwechsel und nicht nur eine unterschiedliche Nachhallmenge.

## Kontrolle innerhalb desselben Assets und Jahres

Eine globale Trennung koennte nur grobe Asset- oder Jahresfamilien
wiederfinden. Deshalb wird jede Vorwelt zusaetzlich ausschliesslich gegen
andere Fenster desselben Assets und Jahres geprueft.

| Bestand | Richtung | Kandidaten je Gruppe | Median Identitaetsrang | mittlere Form-AUC | eindeutig naechste Identitaet |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 13 bis 15 | 5 | 0,627 | 12/56 |
| 2091 | B nach A | 13 bis 15 | 3 | 0,754 | 14/56 |
| 2092 | A nach B | 7 bis 10 | 1 | 0,885 | 27/52 |
| 2092 | B nach A | 7 bis 10 | 1 | 0,902 | 32/52 |

Die individuelle Fensterherkunft bleibt damit auch erhalten, wenn Asset und
Jahr fuer alle Kandidaten gleich sind. Der Effekt ist im Holdout staerker,
aber in beiden Bestaenden und beiden Leserichtungen gleichgerichtet.

## Gruppeninterne Labelnull

Fuer jede Daten-, Profil-, Richtungs- und Vergleichskombination werden die
Herkunftslabels 4.096-mal zwischen unveraenderten Profilen vertauscht. In der
strengen Kontrolle geschieht das nur innerhalb desselben Assets und Jahres.

Alle beobachteten mittleren AUC-Werte liegen oberhalb jeder zugehoerigen
Labelnull. Fuer jede der 16 Auswertungen ergibt sich damit die kleinste
aufloesbare empirische Wahrscheinlichkeit:

```text
p = 1 / 4097 = 0,000244
```

In der staerkenormierten gruppeninternen Kontrolle erreicht die hoechste Null
im 2091-Bestand AUC 0,589 und 0,615 gegen beobachtete 0,627 und 0,754. Im
Holdout erreicht sie 0,643 und 0,634 gegen beobachtete 0,885 und 0,902.

## Selbstbegrenzung bleibt erhalten

Alle 864 Quell-Ziel-Pfade konvergieren innerhalb der Zielwelt bitgenau zum
jeweiligen Resetfeld. Der spaeteste Konvergenztick liegt bei 305 im
2091-Bestand und 314 im Holdout.

447 von 448 Pfaden im 2091-Bestand und alle 416 Holdoutpfade veraendern
mindestens eine Rangbeziehung. Keine der Vierergruppen bildet ein leeres
Formprofil.

Die Quellinformation ist damit eine voruebergehende Form des laufenden Feldes,
kein dauerhaft abweichender Zustand.

## Eindeutigkeit und Grenze

Die mittlere Herkunftstrennung ist robust, aber nicht mit eindeutiger
Wiedererkennung aller Vorwelten gleichzusetzen. Global ist dieselbe Vorwelt
nur in 4 von 56 beziehungsweise 9 bis 10 von 52 Faellen der eindeutig naechste
Formnachbar. Auch innerhalb gleicher Assets und Jahre bleiben im
2091-Bestand viele Identitaeten verteilt.

Getragen ist daher:

- ein quellabhaengiges Muster lokaler Rangwechsel,
- Wiedererkennbarkeit ueber zwei getrennte Gruppen fremder Zielreize,
- Erhalt der Trennung nach Entfernung der gesamten Wechselstaerke,
- Erhalt innerhalb desselben Assets und Jahres,
- Reproduktion in einem unabhaengigen Datenbestand,
- vollstaendige spaetere Konvergenz aller Feldpfade.

Nicht getragen sind:

- ein fertiges Identitaetssymbol,
- eindeutige Wiedererkennung jeder Vorwelt,
- bereits entstandene Semantik oder Bedeutung,
- eine gespeicherte episodische Erinnerung,
- ein autonomer Vergleich eigener Feldzustaende,
- Memory-, Feld- oder Handlungsrueckwirkung.

2107 zeigt eine quellgebundene Formkontinuitaet: Der neuronale Nachhall traegt
nicht nur Staerke, sondern auch eine relationale innere Verteilung des
vorherigen Feldzustands in neue Kontakte. Diese Form ist kurzlebig, kontextuell
und noch nicht Teil von DIOs eigener Syntax.

Der Befund rechtfertigt keine fest programmierte Rangidentitaet. Er belegt
zunaechst, dass das kontinuierliche MCM-Feld eine mechanische Grundlage fuer
organisch entstehende Innenidentitaet besitzt, ohne dass eine solche Identitaet
bereits als Memory oder Bedeutung realisiert waere.

## Reproduzierbare Ausgaben

- `2107_MCM_KONTINUITAET_QUELLIDENTITAET.sources.csv`
- `2107_MCM_KONTINUITAET_QUELLIDENTITAET.summary.csv`

Der Runner ist `tools/run_mcm_continuity_source_identity.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
