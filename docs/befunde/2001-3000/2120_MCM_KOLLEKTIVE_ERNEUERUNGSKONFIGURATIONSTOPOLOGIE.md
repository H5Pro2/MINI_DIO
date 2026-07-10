# 2120 - Kollektive Topologie der MCM-Erneuerungskonfigurationen

## Zweck

Befund 2119 zeigt, dass lokale Ablosungskanten innerhalb eines
Neuronenpaares vollstaendig durch ihre jeweilige Kandidatengeometrie erzwungen
sind. Auf lokaler Ebene entsteht deshalb kein zusaetzlicher Nachfolgergraph.

Eine organische Feldordnung koennte stattdessen kollektiv auftreten: Mehrere
Neuronenpaare koennten am selben endogenen Ranguebergang gemeinsam erneuern.

2120 prueft deshalb:

```text
Bilden gleichzeitig erneuernde Neuronenpaare wiederkehrende kollektive
Konfigurationen oder Kopplungen, die ueber Paarhaeufigkeit und Momentbreite
hinausgehen?
```

## Kollektiver Erneuerungsmoment

Die lokale Erneuerung bleibt exakt wie in 2117 und 2119 definiert. Innerhalb
desselben Neuronenpaares und derselben bisherigen Slothaeufigkeit endet eine
mitgetragene Form, waehrend eine aktuell neue Form in der Folgeepisode
fortbesteht.

Pro aktuelle Rangepisode werden nur die Identitaeten der Neuronenpaare
gesammelt, die gleichzeitig mindestens eine solche Erneuerung zeigen. Jedes
Paar zaehlt an diesem Zeitpunkt hoechstens einmal.

Eine kollektive Konfiguration besitzt mindestens zwei verschiedene
Neuronenpaare. Einzelpaarmomente bleiben fuer Abdeckung und Graderhaltung
sichtbar, zaehlen aber nicht als kollektive Topologie.

## Strominterne Gradnull

Die Null arbeitet fuer jeden der 1.472 Feldstroeme getrennt. Binaere
Paarmitgliedschaften werden nur durch gueltige Zwei-mal-zwei-Swaps zwischen
zwei Erneuerungsmomenten desselben Stroms vertauscht.

Dadurch bleiben exakt erhalten:

- Anzahl der Erneuerungsmomente pro Strom,
- Breite jedes einzelnen Moments,
- gesamte Erneuerungshaeufigkeit jedes Neuronenpaares im Strom,
- alle Strom-, Quellen- und Universengrenzen.

Die Null veraendert nur, welche gleich haeufigen Paarmitgliedschaften am
selben Moment zusammenkommen. Es gibt keine feste Konfigurationsklasse und
keinen Supportschwellwert.

## Abdeckung

| Bestand | Stroeme mit Erneuerung | Erneuerungsmomente | mehrpaarige Momente | maximale Breite | tauschbare Stroeme |
|---|---:|---:|---:|---:|---:|
| 2091-Bestand | 673 / 768 | 1.580 | 285 | 4 | 439 |
| 2092-Holdout | 599 / 704 | 1.292 | 187 | 6 | 286 |

Beide Bestaende enthalten damit reale kombinatorische Freiheit. Anders als
bei den lokalen Kanten aus 2119 kann die Null tausende gueltige
Identitaetsswaps pro Ziehung ausfuehren.

## Kollektive Konfigurationsbuendelung

Die erste Metrik zaehlt Kollisionspaare identischer mehrpaariger
Konfigurationen. Jeder zweite und weitere gleiche Moment traegt ohne
Supportschwelle bei.

| Bestand | Universum | beobachtete Kollision | Nullmittel | empirisches p |
|---|---|---:|---:|---:|
| 2091 | alle | 4.914 | 2.150,6 | 0,0033 |
| 2091 | A | 2.414 | 1.360,1 | 0,0033 |
| 2091 | B | 2.500 | 652,6 | 0,0033 |
| 2092 | alle | 5.711 | 1.551,9 | 0,0033 |
| 2092 | A | 1.428 | 341,6 | 0,0033 |
| 2092 | B | 2.027 | 803,5 | 0,0033 |

In jedem Bestand und jedem Zieluniversum wiederholen sich ganze kollektive
Konfigurationen staerker, als ihre einzelnen Paarhaeufigkeiten und
Momentbreiten erwarten lassen.

## Kopplung einzelner Neuronenpaar-Paare

Die zweite Metrik zerlegt jeden mehrpaarigen Moment in alle ungeordneten
Paar-Kopplungen und prueft deren wiederholte gemeinsame Erneuerung.

| Bestand | Universum | beobachtete Kollision | Nullmittel | empirisches p |
|---|---|---:|---:|---:|
| 2091 | alle | 12.379 | 6.445,0 | 0,0033 |
| 2091 | A | 2.414 | 1.360,1 | 0,0033 |
| 2091 | B | 7.901 | 3.756,5 | 0,0033 |
| 2092 | alle | 8.395 | 2.802,4 | 0,0033 |
| 2092 | A | 2.220 | 969,2 | 0,0033 |
| 2092 | B | 3.919 | 1.322,9 | 0,0033 |

Damit liegt auf Populationsebene eine reale kollektive Erneuerungskoordination
vor. Sie ist nicht durch die Aktivitaet einzelner Paare oder durch besonders
breite Rangmomente erklaert.

## Uebertragung ganzer Konfigurationen

Die konkrete Identitaet mehrpaariger Konfigurationen wird zwischen den
getrennten Zieluniversen A und B verglichen.

| Bestand | gleiche A/B-Instanzpaare | Nullmittel | empirisches p | Quellen ueber / unter / gleich Null |
|---|---:|---:|---:|---:|
| 2091 | 0 | 137,3 | 1,000 | 0 / 38 / 10 |
| 2092 | 2.256 | 408,5 | 0,0033 | 24 / 11 / 9 |

Die Richtung reproduziert nicht. Im Entwicklungsbestand teilen A und B keine
einzige mehrpaarige Konfiguration, obwohl die graderhaltende Null im Mittel
137 Treffer erzeugt. Im Holdout uebertragen wenige haeufige Konfigurationen
stark.

Eine feste universenuebergreifende Gesamtgestalt ist damit nicht getragen.

## Uebertragung der Paar-Kopplung

Die kleinere Paar-Kopplung zeigt aggregiert in beiden Bestaenden mehr
A/B-Uebereinstimmung als die Gradnull:

| Bestand | gleiche A/B-Kopplungsinstanzen | Nullmittel | empirisches p | Quellen ueber / unter / gleich Null |
|---|---:|---:|---:|---:|
| 2091 | 2.064 | 1.326,4 | 0,0033 | 40 / 5 / 3 |
| 2092 | 2.256 | 507,5 | 0,0033 | 24 / 16 / 4 |

Der Entwicklungsbestand traegt diese Richtung auch quellenweise. Im Holdout
ist die Quellenrichtung mit `24 / 16 / 4` jedoch nicht signifikant
einheitlich; die zweiseitige Signkontrolle liegt bei `0,268`.

Die aggregierte Kopplung ist deshalb ein realer populationsweiter Befund,
aber noch keine quellenuniverselle feste Kante.

## Interpretation

2120 findet erstmals auf der neuen Erneuerungsebene echte kombinatorische
kollektive Ordnung:

```text
Erneuerung geschieht nicht nur lokal und unabhaengig.
Mehrere Neuronenpaare koordinieren ihre Erneuerungsmomente ueberzufaellig.
```

Diese Ordnung ist jedoch beweglich. Welche vollstaendige Konfiguration traegt,
wechselt zwischen Bestanden und Zieluniversen. Selbst die kleinere
Paar-Kopplung uebertraegt im Holdout nicht quellenweit gleichgerichtet.

Getragen ist daher eine populationale kollektive Koordination. Nicht getragen
ist eine feste semantische Konfiguration, ein universeller Kopplungsgraph oder
eine autonome Auswahlregel.

## Keine Integration

MINI_DIO speichert aus 2120 weder Konfigurationen noch Kopplungskanten. Der
Runner veraendert Feld und Memory nicht und wirkt nicht auf spaetere Episoden
oder Handlungen zurueck.

Quellen-, Asset- und Jahresbezeichnungen dienen nur der nachgelagerten
Reproduktionskontrolle. Die Kandidatenbildung liest keine Folgeepisode; die
Folgeepisode bestimmt ausschliesslich, ob die zuvor gebildete lokale
Erneuerungsgelegenheit realisiert wird.

## Reproduzierbare Ausgaben

- `2120_MCM_KOLLEKTIVE_ERNEUERUNGSKONFIGURATIONSTOPOLOGIE.paths.csv`
- `2120_MCM_KOLLEKTIVE_ERNEUERUNGSKONFIGURATIONSTOPOLOGIE.sources.csv`
- `2120_MCM_KOLLEKTIVE_ERNEUERUNGSKONFIGURATIONSTOPOLOGIE.summary.csv`
- `2120_MCM_KOLLEKTIVE_ERNEUERUNGSKONFIGURATIONSTOPOLOGIE.configurations.csv`

Der Runner ist
`tools/run_mcm_collective_renewal_configuration_topology.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
