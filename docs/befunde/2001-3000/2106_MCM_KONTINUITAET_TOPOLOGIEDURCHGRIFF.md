# 2106 - Durchgriff der MCM-Feldkontinuitaet auf innere Topologie

## Zweck

Befund 2105 zeigt eine reale, selbstbegrenzte Innenzustandsspur derselben
MCM-Feldinstanz. 2106 prueft, ob diese Spur unter identischen Folgereizen nur
numerische Feldwerte verschiebt oder auch die entstehende innere Ordnung
veraendert.

Verglichen werden erneut:

```text
Resetpfad:
neues Feld -> Folgewelt

Kontinuitaetspfad:
Kontaktwelt -> reizfreie Luecke -> dieselbe Feldinstanz -> Folgewelt
```

Es gibt kein Feldlernen, keine Handlung, keine Memory-Ruecklesung und keine
vorgegebene Bedeutung. Der einzige Unterschied ist der Vorzustand des Feldes.

## Zwei getrennte Beobachtungsebenen

### Bestehende DIO-Syntax

Die vorhandene Funktion `make_syntax_symbol` bildet aus demselben Sinnesvektor
und der aktuellen mittleren Feldsignatur ein `dio_*`-Wort. Aufeinanderfolgende
gleiche Woerter werden als eine Episode gelesen; jeder tatsaechliche Wechsel
bildet eine gerichtete Kante.

Diese Ebene ist bereits Teil der bestehenden Architektur. 2106 veraendert
weder ihre Aufloesung noch ihre Bucketbildung.

### Schwellenfreie neuronale Rangtopologie

Zusaetzlich wird pro Tick die exakte Rangordnung der zwoelf
Neuronenaktivierungen gelesen. Exakt gleiche Aktivierungen bleiben in derselben
Rangschicht. Es gibt kein Epsilon, keine Abstandsschwelle und keine benannte
Rolle.

Auch hier werden nur direkt aufeinanderfolgende gleiche Rangzustaende zu einer
Episode zusammengefasst. Gerichtete Kanten entstehen ausschliesslich aus der
tatsaechlichen Folge verschiedener Rangzustaende.

Diese Rangtopologie ist eine Forschungslesung der inneren Feldgeometrie. Sie
ist keine neue Runtime-Topologie und wird von MINI_DIO nicht zurueckgelesen.

## Pruefbestand

Die Gegenprobe verwendet exakt dieselben realen Kontaktpaare wie 2105:

- 120 gerichtete Paare aus BTC und SOL 2024/2025 auf `30m`,
- 108 gerichtete Paare aus DOGE, PAXG und XRP 2024/2025 auf `5m`,
- acht reizfreie Luecken von 0 bis 64 Ticks,
- insgesamt 1.824 Einzelvergleiche.

Vorwaerts- und Rueckwaertskontakte werden getrennt erhalten. Asset, Preis,
Richtung und Volumen werden nicht als Bedeutung oder Ziel ausgewertet.

## Bestehende Syntax bleibt vollstaendig gleich

In keinem der 1.824 Vergleiche aendert die fortgefuehrte Feldinstanz auch nur
einen `dio_*`-Syntaxzustand.

| Bestand | Vergleiche | abweichende Syntaxpfade | abweichende Syntaxticks | abweichende Syntaxknoten | abweichende Syntaxkanten |
|---|---:|---:|---:|---:|---:|
| 2091-Bestand | 960 | 0 | 0 | 0 | 0 |
| 2092-Holdout | 864 | 0 | 0 | 0 | 0 |

Damit entstehen auf der vorhandenen Wortebene weder andere Episoden noch
andere gerichtete Uebergaenge. Die in 2105 gemessene Feldspur erreicht die
aktuelle Syntaxbildung nicht.

Der Grund ist architektonisch sichtbar: Die Wortbildung erhaelt vom MCM-Feld
nur dessen mittlere Signatur und verdichtet sie zusammen mit den Sinneswerten
in diskrete Buckets. Die innere Verteilung der Neuronenaktivierungen ist dort
nicht enthalten.

## Kurze Veraenderung der inneren Feldgeometrie

Unter derselben unveraenderten Syntax veraendert Kontinuitaet dennoch kurz die
exakte neuronale Rangordnung:

| Leerticks | veraenderte Paare 2091 | Median Rangticks 2091 | veraenderte Paare 2092 | Median Rangticks 2092 |
|---:|---:|---:|---:|---:|
| 0 | 120/120 | 7 | 108/108 | 7 |
| 1 | 120/120 | 7 | 108/108 | 7 |
| 2 | 120/120 | 6 | 108/108 | 6 |
| 4 | 119/120 | 5 | 108/108 | 5 |
| 8 | 114/120 | 4 | 105/108 | 4 |
| 16 | 93/120 | 2 | 88/108 | 2 |
| 32 | 26/120 | 0 | 27/108 | 0 |
| 64 | 0/120 | 0 | 0/108 | 0 |

Ohne Leerluecke unterscheiden sich im 2091-Bestand je Paar ein bis 14
Rangticks, im Holdout zwei bis 13. Der letzte abweichende Rangtick liegt im
Median bei Tick 21 beziehungsweise 22; die spaetesten Einzelfaelle liegen bei
Tick 73 und 55.

Die bitgenaue neuronale Zustandsspur aus 2105 dauert damit erheblich laenger
als ihre Wirkung auf die Aktivierungsordnung. Nach 64 Leerticks bleibt zwar
noch eine sehr kleine numerische Feldspur, aber keine Rang-, Knoten- oder
Kantenabweichung.

## Lokale statt breite Rangverschiebung

Die Rangveraenderung ist klein innerhalb des Feldes. Bei zwoelf Neuronen gibt
es 66 paarweise Ordnungsbeziehungen. Ohne Leerluecke unterscheiden sich pro
veraendertem Tick im Paarmittel nur rund 1,27 Beziehungen. Das beobachtete
Maximum liegt in beiden Bestaenden bei fuenf von 66 Beziehungen.

Kontinuitaet wirft die Feldordnung daher nicht vollstaendig um. Sie verschiebt
kurz einzelne Nachbarschaften innerhalb einer ansonsten weitgehend gleichen
Geometrie.

## Wirkung auf den Rangpfad

Die lokalen Verschiebungen reichen aus, um andere unbenannte Knoten und
gerichtete Uebergaenge im Rangpfad zu erzeugen:

| Bestand, Luecke 0 | Grenzunterschiede | Knotenmengen-Unterschiede | Kantenmengen-Unterschiede |
|---|---:|---:|---:|
| 2091-Bestand | 129 | 183 | 1.317 |
| 2092-Holdout | 94 | 140 | 1.223 |

Mit wachsender Leerluecke fallen diese Unterschiede gemeinsam ab. Nach 32
Ticks bleiben noch 66 und 71 Kantenmengen-Unterschiede; nach 64 Ticks sind
Grenzen, Knoten und Kanten in beiden Bestaenden vollstaendig identisch.

Vorwaerts- und Rueckwaertslauf zeigen dieselbe Form. Ohne Luecke liegen die
mittleren abweichenden Rangticks im 2091-Bestand bei 7,15 und 7,10, im Holdout
bei 7,20 und 7,56. Eine besondere natuerliche Kontaktrichtung wird nicht
getragen.

## Signaturstaerke erklaert die Rangdauer nicht

Die Korrelation zwischen erster Signaturdifferenz und Zahl abweichender
Rangticks liegt ueber die Lueckenskala nahe null. Bei Luecke null betraegt sie
-0,006 im 2091-Bestand und -0,084 im Holdout.

Eine groessere mittlere Feldabweichung bedeutet somit nicht automatisch eine
laengere Veraenderung der inneren Ordnung. Entscheidend ist, ob lokale
Neuronenbeziehungen ihre Reihenfolge wechseln.

## Befund

Getragen sind:

- ein reproduzierbarer Durchgriff des Feldvorzustands auf die innere
  Aktivierungsgeometrie,
- Rangveraenderungen in allen 228 gerichteten Folgepfaden ohne Leerluecke,
- dieselbe qualitative Abschwaechung in Entwicklungsbestand und Holdout,
- lokale Aenderungen unbenannter Knoten und gerichteter Ranguebergaenge,
- vollstaendiges Verschwinden dieser topologischen Wirkung bis 64 Leerticks,
- nahezu gleiche Form in Vorwaerts- und Rueckwaertskontakten.

Nicht getragen sind:

- ein anderes bestehendes `dio_*`-Wort,
- eine andere vorhandene Syntaxepisode oder Syntaxkante,
- dauerhafte topologische Abweichung,
- semantische Bedeutung der Rangzustaende,
- quellenspezifische Information oder Wiedererkennung,
- Memory-Bildung, Feldlernen, Handlung oder autonome Aktivitaet.

2106 zeigt erstmals direkt eine Luecke zwischen innerem Feld und aktueller
Selbstbeschreibung: Das MCM-Feld besitzt eine kurz geschichtsabhaengige
Mikrotopologie, waehrend DIOs heutige Syntax diese Geometrie vollstaendig
gleich liest.

Das rechtfertigt weder eine fest programmierte Rangsemantik noch die sofortige
Integration einer dauerhaften Feldinstanz. Getragen ist zunaechst nur, dass
die innere Feldordnung mehr zeitliche Form bewahrt als das bestehende
Syntaxwort ausdrueckt.

## Reproduzierbare Ausgaben

- `2106_MCM_KONTINUITAET_TOPOLOGIEDURCHGRIFF.pairs.csv`
- `2106_MCM_KONTINUITAET_TOPOLOGIEDURCHGRIFF.summary.csv`

Der Runner ist `tools/run_mcm_continuity_topology_transfer.py`. Er erzeugt
keine Welt-, Runtime-, Memory- oder Debugdateien.
