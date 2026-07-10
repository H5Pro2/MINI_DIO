# 2093 - Exakte Gelegenheit und Herkunftsbalance des MCM-Relationslebenslaufs

## Zweck

Befunde 2091 und 2092 verglichen, ob bereits getragene Relationskanten beim
nächsten Eigenalter häufiger fortbestehen als neue Kontakte. Als
fortsetzungsfähig galt bisher jede Kante, deren beide Relationen irgendwann
das nächste Alter erreichten.

Diese Bedingung ist notwendig, aber nicht hinreichend. Eine Relation kann das
nächste Alter bereits wieder verlassen haben, bevor die zweite Relation es
erreicht. Beide besitzen dann nie gleichzeitig das zu vergleichende Alter;
eine fehlende Kante ist in diesem Fall keine ausgebliebene Fortsetzung.

2093 rekonstruiert deshalb die exakte gemeinsame Gelegenheit und ordnet sie
der Welt zu, in der die zweite Relation das nächste Alter erreicht. Die
Herkunft dient ausschließlich als Kontrollschicht. Chartwerte,
Außenentwicklungen und Handlungsergebnisse werden nicht untersucht.

## Exakte Gelegenheit

Für eine Kante bei Relationsalter `a` gilt eine Fortsetzungsgelegenheit bei
`a + 1` nur, wenn:

1. beide Relationen ein Ereignis `a + 1` besitzen,
2. die früher dort angekommene Relation dieses Alter noch nicht verlassen
   hat, wenn die zweite eintrifft,
3. beide Relationen somit bei derselben Weltfinalisierung gleichzeitig
   Alter `a + 1` besitzen.

Jede tatsächlich beobachtete Fortsetzung erfüllt diese Bedingung. Entfernt
werden ausschließlich bisher als Nichtfortsetzung gezählte Kanten ohne
gleichzeitige Gelegenheit.

## Korrektur der beiden Bestände

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| bisher angenäherte Gelegenheiten | 21.114 | 14.089 |
| nicht gleichzeitige Gelegenheiten | 9.625 | 6.015 |
| exakte gemeinsame Gelegenheiten | 11.489 | 8.074 |
| Anteil entfernter Schein-Gelegenheiten | 45,58 % | 42,69 % |

Im Entwicklungsbestand waren 4.769 getragene und 4.856 neue angenäherte
Gelegenheiten nicht gleichzeitig. Im unabhängigen Holdout waren es 2.822
getragene und 3.193 neue. Diese ungleiche Verteilung konnte die bisherigen
Fortsetzungsraten verzerren.

## Korrigierter Gesamtvergleich

| Bestand | getragen | neu | Abstand | Verhältnis |
|---|---:|---:|---:|---:|
| 2091: BTC/SOL `30m` | 0,6625 | 0,6483 | +0,0141 | 1,0218 |
| 2092: DOGE/PAXG/XRP `5m` | 0,6223 | 0,6320 | -0,0098 | 0,9845 |

Der ursprüngliche Bestand behält nach der Korrektur einen kleinen Vorsprung
von 1,41 Prozentpunkten. Im unabhängigen Bestand kehrt sich die Richtung um:
Getragene Kanten setzen sich 0,98 Prozentpunkte seltener fort als neue.

## Herkunftsstratifizierte Kontrolle

Die Gelegenheiten werden innerhalb jeder Kombination aus Relationsalter und
Datenherkunft verglichen. Eine Kantenlabel-Null erhält pro Schicht die Zahl
der getragenen Kanten und die Zahl der Fortsetzungen und verteilt nur die
Label 2.000-mal neu.

| Bestand | informative Herkunft-Alter-Schichten | gemeinsamer Odds-Faktor | analytisches `p` | empirisches `p` |
|---|---:|---:|---:|---:|
| 2091 | 110 | 1,0627 | 0,0670 | 0,0685 |
| 2092 | 94 | 0,9209 | 0,9591 | 0,9585 |

Der kleine positive Abstand im 2091-Bestand erreicht nach Kontrolle der
Herkunft die Grenze von 0,05 nicht. Der unabhängige Holdout liefert keine
positive Evidenz. Die frühere graphstrukturerhaltende Null beantwortet diese
korrigierte Frage nicht, weil sie die fehlende Gleichzeitigkeit nicht
modellierte.

## Herkunftsbalance

Im 2091-Bestand zeigen drei von vier Herkunftsgruppen eine positive und eine
eine negative Rohdifferenz. Der positive Anteil liegt vor allem in den beiden
SOL-Gruppen; BTC 2024 ist negativ und BTC 2025 nahezu neutral. Alle vier
Leave-one-source-out-Vergleiche bleiben positiv, aber zwischen 0,29 und 2,40
Prozentpunkten.

Im unabhängigen 2092-Bestand zeigen drei von sechs Gruppen eine positive und
drei eine negative Richtung. Beim Weglassen jeweils einer Herkunft bleiben
fünf von sechs Vergleichen negativ. Nur ohne XRP 2024 entsteht ein kleiner
positiver Abstand. Eine herkunftsübergreifend gleichgerichtete Ordnung liegt
damit nicht vor.

## Befund

Getragen sind:

- die exakte Rekonstruktion gemeinsamer Fortsetzungsgelegenheiten aus den
  archivierten Relationsereignissen,
- ein kleiner positiver Rest im 2091-Entwicklungsbestand,
- deutlich unterschiedliche Fortsetzungsrichtungen zwischen den
  Herkunftsgruppen,
- eine negative Gesamtrichtung im unabhängigen 2092-Holdout.

Nicht getragen sind:

- der bisher angenommene gleichberechtigte Fortsetzungsvergleich allein über
  das spätere Maximalalter,
- eine belastbare herkunftsübergreifende Eigenstabilität getragener Kanten,
- eine Übertragung des positiven 2091-Rests auf den unabhängigen Holdout,
- ein Stabilitätsmarker, Reifealter oder eine Gewichtungsregel,
- eine Rücklesung in Feld, Wahrnehmung oder Handlung.

2093 korrigiert die Interpretation von 2091 und 2092. Der passive
Relationslebenslauf bleibt als exaktes Archiv organischer Umbildung erhalten,
aber seine bisher behauptete Fortsetzungsneigung ist nicht belastbar. An der
Runtime wird nichts geändert.

## Reproduzierbare Ausgaben

- `2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.source_age.csv`
- `2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.sources.csv`
- `2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.leave_one_source_out.csv`
- `2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.null.csv`
- `2093_MCM_RELATIONSLEBENSLAUF_EXAKTE_GELEGENHEIT_HERKUNFTSBALANCE.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089, 2090 und
2092. Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien und wird
von MINI_DIO nicht zurückgelesen.
