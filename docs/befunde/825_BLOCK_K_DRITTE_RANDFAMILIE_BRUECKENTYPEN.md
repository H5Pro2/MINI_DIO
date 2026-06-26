# 818 - Block-K Brueckentypen-Vergleich zu dio_1v2w

## Fragestellung

Bilden die stabilen Nachbarfamilien von `dio_1v2w` einen gemeinsamen Brueckentyp oder mehrere unterschiedliche Uebergangsarten?

## Vergleich

| Familie | Brueckentyp | Gesamt | Near | Vorher | Nachher | Stabil all | Stabil near | Strain Delta | Trust Delta | Einbettung Delta |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_155c | balancierte_bruecke | 2612 | 27 | 5 | 22 | 0.9809 | 0.9630 | 0.0000 | 0.0071 | -0.0059 |
| dio_0m9z | instabile_kontaktzone | 2327 | 23 | 7 | 16 | 0.7430 | 0.4783 | 0.0064 | 0.0019 | -0.0141 |
| dio_0g2r | offene_bruecke | 543 | 13 | 4 | 9 | 0.9061 | 0.7692 | 0.0015 | 0.0356 | -0.0028 |
| dio_0h9h | balancierte_bruecke | 1623 | 13 | 5 | 8 | 1.0000 | 1.0000 | 0.0005 | -0.0144 | -0.0284 |
| dio_00ly | balancierte_bruecke | 968 | 11 | 4 | 7 | 1.0000 | 1.0000 | 0.0028 | 0.0002 | -0.0219 |
| dio_1gp2 | offene_bruecke | 579 | 11 | 4 | 7 | 0.8636 | 0.8182 | -0.0016 | -0.0040 | -0.0244 |
| dio_0pq6 | offene_bruecke | 263 | 10 | 5 | 5 | 0.7719 | 0.7000 | -0.0024 | 0.0686 | 0.0016 |
| dio_104t | balancierte_bruecke | 3708 | 9 | 1 | 8 | 0.9854 | 1.0000 | 0.0064 | 0.0027 | -0.0310 |

## Befund

Die Brueckenfamilien um `dio_1v2w` bilden keinen komplett einheitlichen Typ, aber sie teilen einen Kern: Randnaehe fuehrt nicht automatisch zu Kollaps.

- balancierte_bruecke: 4
- offene_bruecke: 3
- instabile_kontaktzone: 1

Gemeinsame Lesung:

- stabile Bruecken behalten in Randnaehe ueberwiegend ihre Stabilitaet,
- Vorher-/Nachher-Verteilung unterscheidet die Rolle: manche wirken als Vorfeldanker, andere als Nachfeldanker, einige als echte beidseitige Bruecke,
- Trust-Delta und Strain-Delta zeigen, ob Randnaehe belastet, neutral bleibt oder entlastet,
- damit wirkt die MCM-Topologie nicht wie eine einzelne Linie, sondern wie mehrere Uebergangsarten zwischen Randspannung und stabileren Bedeutungsraeumen.

## Grenze

Der Befund ist passiv. Er beschreibt Brueckentypen im Innenfeld, keine Handlung und keine Richtung.

## Wie es weitergeht

Als naechstes sollte aus diesen Brueckentypen eine kompakte MCM-Uebergangskarte gebaut werden: Randfamilie, Vorfeldanker, beidseitige Bruecke, Nachfeldanker, stabile Mitte.
