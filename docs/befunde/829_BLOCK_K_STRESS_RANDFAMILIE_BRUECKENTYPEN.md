# 818 - Block-K Brueckentypen-Vergleich zu dio_0jkk

## Fragestellung

Bilden die stabilen Nachbarfamilien von `dio_0jkk` einen gemeinsamen Brueckentyp oder mehrere unterschiedliche Uebergangsarten?

## Vergleich

| Familie | Brueckentyp | Gesamt | Near | Vorher | Nachher | Stabil all | Stabil near | Strain Delta | Trust Delta | Einbettung Delta |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_155c | balancierte_bruecke | 472 | 13 | 6 | 7 | 0.9852 | 0.9231 | -0.0021 | -0.0076 | -0.0246 |
| dio_104t | offene_bruecke | 721 | 8 | 5 | 3 | 0.9931 | 0.8750 | 0.0036 | -0.0071 | -0.0375 |
| dio_0oc3 | offene_bruecke | 174 | 8 | 3 | 5 | 0.9368 | 0.7500 | 0.0049 | -0.0064 | -0.0336 |
| dio_0m9z | instabile_kontaktzone | 404 | 7 | 2 | 5 | 0.7277 | 0.5714 | 0.0057 | 0.0030 | -0.0360 |
| dio_1gp2 | balancierte_bruecke | 86 | 5 | 1 | 4 | 0.8605 | 1.0000 | -0.0078 | 0.0293 | -0.0321 |
| dio_0h9h | balancierte_bruecke | 310 | 4 | 2 | 2 | 1.0000 | 1.0000 | 0.0016 | 0.0115 | -0.0552 |
| dio_00ly | balancierte_bruecke | 149 | 4 | 2 | 2 | 1.0000 | 1.0000 | 0.0090 | 0.0003 | -0.0677 |
| dio_0h6t | vorfeld_anker | 19 | 3 | 3 | 0 | 1.0000 | 1.0000 | 0.0028 | -0.2450 | -0.1338 |

## Befund

Die Brueckenfamilien um `dio_0jkk` bilden keinen komplett einheitlichen Typ, aber sie teilen einen Kern: Randnaehe fuehrt nicht automatisch zu Kollaps.

- balancierte_bruecke: 4
- offene_bruecke: 2
- instabile_kontaktzone: 1
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
