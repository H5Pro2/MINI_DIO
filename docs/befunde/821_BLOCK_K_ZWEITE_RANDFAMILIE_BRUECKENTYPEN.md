# 818 - Block-K Brueckentypen-Vergleich zu dio_1yoi

## Fragestellung

Bilden die stabilen Nachbarfamilien von `dio_1yoi` einen gemeinsamen Brueckentyp oder mehrere unterschiedliche Uebergangsarten?

## Vergleich

| Familie | Brueckentyp | Gesamt | Near | Vorher | Nachher | Stabil all | Stabil near | Strain Delta | Trust Delta | Einbettung Delta |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_155c | balancierte_bruecke | 2612 | 18 | 13 | 5 | 0.9809 | 1.0000 | -0.0046 | 0.0176 | -0.0010 |
| dio_17ct | balancierte_bruecke | 817 | 14 | 6 | 8 | 1.0000 | 1.0000 | 0.0047 | 0.0175 | -0.0116 |
| dio_104t | balancierte_bruecke | 3708 | 13 | 11 | 2 | 0.9854 | 0.9231 | 0.0040 | 0.0029 | -0.0224 |
| dio_0pz6 | balancierte_bruecke | 771 | 11 | 6 | 5 | 1.0000 | 1.0000 | -0.0009 | -0.0022 | -0.0272 |
| dio_0h9h | offene_bruecke | 1623 | 7 | 4 | 3 | 1.0000 | 1.0000 | -0.0065 | -0.0423 | -0.0595 |
| dio_0f4r | nachfeld_anker | 125 | 9 | 0 | 9 | 1.0000 | 1.0000 | 0.0016 | -0.0114 | -0.0279 |
| dio_0l7p | vorfeld_anker | 2101 | 7 | 7 | 0 | 1.0000 | 1.0000 | 0.0029 | -0.0014 | -0.0354 |

## Befund

Die Brueckenfamilien um `dio_1yoi` bilden keinen komplett einheitlichen Typ, aber sie teilen einen Kern: Randnaehe fuehrt nicht automatisch zu Kollaps.

- balancierte_bruecke: 4
- offene_bruecke: 1
- nachfeld_anker: 1
- vorfeld_anker: 1

Gemeinsame Lesung:

- stabile Bruecken behalten in Randnaehe ueberwiegend ihre Stabilitaet,
- Vorher-/Nachher-Verteilung unterscheidet die Rolle: manche wirken als Vorfeldanker, andere als Nachfeldanker, einige als echte beidseitige Bruecke,
- Trust-Delta und Strain-Delta zeigen, ob Randnaehe belastet, neutral bleibt oder entlastet,
- damit wirkt die MCM-Topologie nicht wie eine einzelne Linie, sondern wie mehrere Uebergangsarten zwischen Randspannung und stabileren Bedeutungsraeumen.

## Grenze

Der Befund ist passiv. Er beschreibt Brueckentypen im Innenfeld, keine Handlung und keine Richtung.

## Wie es weitergeht

Als naechstes sollte aus diesen Brueckentypen eine kompakte MCM-Uebergangskarte gebaut werden: Randfamilie, Vorfeldanker, beidseitige Bruecke, Nachfeldanker, stabile Mitte.
