# 806 - Block-K Feldepisoden-Zeitreihe

## Fragestellung

Wann entsteht in einer 10k-Welt Feldintegration, wann bricht sie, und tragen Nachhall/Feldzeit diese Phasen sichtbar mit?

Quelle:

- `debug\block_k_10k_multiworld\kontrolliert_2023_negative_stress_10k_5m_solusdt\dio_mini_lauf_1\episodes.csv`
- Segmentierung: `state`

## Segmentuebersicht

- Segmente: `5`
- durchschnittliche Segmentdauer: `1998.80` Ticks
- lange Segmente ab 1000 Ticks: `3`
- nicht getragene/gespannte Segmente: `2`
- wiederkehrende Feldepisoden-Symbole: `0`

Lange Segmente:

- Carry: `0.5354`
- Rekopplung: `0.7053`
- Strain: `0.1530`

## Zeitreihe

| Segment | Ticks | Dauer | Feldepisode | Zustand | Klasse | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | Transition |
|---:|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | 1-2405 | 2405 | dio_mcm_episode_1joiyc3 | field_carried | stabil | 0.5169 | 0.6983 | 0.1544 | 0.1603 | 0.6161 | start->dio_mcm_episode_1joiyc3->dio_mcm_episode_1gwfnz5 |
| 2 | 2406-2406 | 1 | dio_mcm_episode_1gwfnz5 | field_strained | gespannt | 0.3229 | 0.5363 | 0.3422 | 0.0000 | 0.0000 | dio_mcm_episode_1joiyc3->dio_mcm_episode_1gwfnz5->dio_mcm_episode_0e7qvj1 |
| 3 | 2407-7582 | 5176 | dio_mcm_episode_0e7qvj1 | field_carried | stabil | 0.5429 | 0.7079 | 0.1524 | 0.1815 | 0.7319 | dio_mcm_episode_1gwfnz5->dio_mcm_episode_0e7qvj1->dio_mcm_episode_0d1w2c7 |
| 4 | 7583-7583 | 1 | dio_mcm_episode_0d1w2c7 | field_strained | gespannt | 0.3208 | 0.5379 | 0.3435 | 0.0000 | 0.0000 | dio_mcm_episode_0e7qvj1->dio_mcm_episode_0d1w2c7->dio_mcm_episode_14coypf |
| 5 | 7584-9994 | 2411 | dio_mcm_episode_14coypf | field_carried | stabil | 0.5466 | 0.7096 | 0.1523 | 0.1832 | 0.7442 | dio_mcm_episode_0d1w2c7->dio_mcm_episode_14coypf->end |

## Befund

Die Welt zeigt Feldintegration als Phasenstruktur, nicht nur als Durchschnittswert.

Lesart:

- Lange getragene Feldepisoden bilden den Hauptanteil der Weltzeit.
- Kurze gespannte oder kippende Segmente treten als Bruch- oder Uebergangspunkte auf.
- Feldepisoden-Symbole markieren die jeweilige Feldphase; Wiederkehr zeigt sich hier primaer als wiederholter Wechsel zwischen getragenen Langphasen und kurzen Spannungsbruechen.
- Nachhall und temporales Trust-Signal bleiben in langen Segmenten lesbar und begleiten die Integration.

Damit wird der Befund aus `805` konkretisiert: die hoehere 10k-Stabilisierung ist in einer zeitlichen Segmentordnung sichtbar.

## Grenze

Diese Zeitreihe ist eine Segmentierung nach Feldphase. Sie ist keine Handlungsauswertung und keine kausale Beweisfuehrung.

## Wie es weitergeht

Als naechstes sollte dieselbe Zeitreihen-Lupe fuer eine stressige 1000/2000er Welt laufen. Dann sehen wir, ob kuerzere Stresswelten weniger lange Integrationssegmente und mehr Bruchpunkte bilden.
