# 818 - Block-K Brueckentypen-Vergleich zu dio_1un4

## Fragestellung

Bilden die stabilen Nachbarfamilien von `dio_1un4` einen gemeinsamen Brueckentyp oder mehrere unterschiedliche Uebergangsarten?

## Vergleich

| Familie | Brueckentyp | Gesamt | Near | Vorher | Nachher | Stabil all | Stabil near | Strain Delta | Trust Delta | Einbettung Delta |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_155c | balancierte_bruecke | 2612 | 14 | 8 | 6 | 0.9809 | 1.0000 | -0.0059 | 0.0053 | -0.0157 |
| dio_0m9z | instabile_kontaktzone | 2327 | 12 | 9 | 3 | 0.7430 | 0.5000 | 0.0036 | -0.0059 | -0.0275 |
| dio_17ct | balancierte_bruecke | 817 | 10 | 1 | 9 | 1.0000 | 1.0000 | 0.0005 | 0.0285 | -0.0101 |
| dio_0h9h | balancierte_bruecke | 1623 | 7 | 5 | 2 | 1.0000 | 1.0000 | 0.0010 | 0.0142 | -0.0295 |
| dio_1mwv | balancierte_bruecke | 223 | 5 | 1 | 4 | 1.0000 | 1.0000 | 0.0003 | 0.0430 | -0.0359 |
| dio_0obq | balancierte_bruecke | 712 | 5 | 3 | 2 | 0.9930 | 1.0000 | -0.0014 | 0.0419 | -0.0334 |

## Befund

Die Brueckenfamilien um `dio_1un4` bilden keinen komplett einheitlichen Typ, aber sie teilen einen Kern: Randnaehe fuehrt nicht automatisch zu Kollaps.

- balancierte_bruecke: 5
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
