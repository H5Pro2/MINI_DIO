# 807 - Block-K Stress-Feldepisoden-Zeitreihe

## Fragestellung

Wie sieht die Feldepisoden-Zeitreihe einer kurzen Stresswelt im Vergleich zur 10k-Integration aus?

Quelle:

- `debug\block_k_stress_multiworld\kontrolliert_2023_negative_stress_test1_1000_5m_solusdt\dio_mini_lauf_1\episodes.csv`
- Segmentierung: `state`

## Segmentuebersicht

- Segmente: `1`
- durchschnittliche Segmentdauer: `994.00` Ticks
- lange Segmente ab 1000 Ticks: `0`
- nicht getragene/gespannte Segmente: `0`
- wiederkehrende Feldepisoden-Symbole: `0`

Lange Segmente:

- Carry: `0.0000`
- Rekopplung: `0.0000`
- Strain: `0.0000`

## Zeitreihe

| Segment | Ticks | Dauer | Feldepisode | Zustand | Klasse | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | Transition |
|---:|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | 1-994 | 994 | dio_mcm_episode_1joiyc3 | field_carried | stabil | 0.5009 | 0.6916 | 0.1565 | 0.1301 | 0.5397 | start->dio_mcm_episode_1joiyc3->end |

## Befund

Die Welt zeigt eine kurze, durchgehend getragene Feldphase ohne langen Integrationsabschnitt nach der 1000-Tick-Leseschwelle.

Lesart:

- Der Feldzustand bleibt stabil getragen.
- Es entstehen keine langen Integrationssegmente.
- Nachhall und temporales Trust-Signal bleiben niedriger als in der 10k-Langphase.
- Es gibt hier keinen sichtbaren Bruch, aber auch keine lange Feldzeit zur Reifung.

Damit eignet sich diese Welt als Gegenpol zur 10k-Zeitreihe: stabiler Zustand ja, laengere Feldintegration nein.

## Grenze

Diese Zeitreihe ist eine Segmentierung nach Feldphase. Sie ist keine Handlungsauswertung und keine kausale Beweisfuehrung.

## Wie es weitergeht

Als naechstes sollten 806 und 807 direkt verglichen werden: lange 10k-Integration gegen kurze Stress-Phasenstruktur.
