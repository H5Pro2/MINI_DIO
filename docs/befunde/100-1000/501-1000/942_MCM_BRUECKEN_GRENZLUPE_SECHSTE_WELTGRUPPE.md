# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.1000 | dio_mcm_episode_0mji3u6 (25) | dio_mcm_episode_18l3thm (30) | zentrum_stabil:84; offene_variante:6 | zentrum_stabil:67; offene_variante:14; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_0hjnwsk | 8 | 4 | 2.6250 | dio_mcm_episode_0aztxel (4) | dio_mcm_episode_18n06fj (8) | offene_variante:6; zentrum_stabil:2 | zentrum_stabil:7; offene_variante:1 |
| dio_mcm_episode_0ifxej6 | 1 | 1 | 1.0000 | dio_mcm_episode_0mm85pw (1) | dio_mcm_episode_0r1o8ja (1) | zentrum_stabil:1 | offene_variante:1 |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.5455 | dio_mcm_episode_0lne9ax (6) | dio_mcm_episode_0qzjuvj (9) | zentrum_stabil:8; offene_variante:3 | zentrum_stabil:8; offene_variante:3 |
| dio_mcm_episode_0l3i7ey | 5 | 3 | 1.4000 | dio_mcm_episode_0ldht3x (3) | dio_mcm_episode_0lne9ax (2) | zentrum_stabil:4; offene_variante:1 | zentrum_stabil:4; offene_variante:1 |
| dio_mcm_episode_0q7j4gf | 1 | 1 | 1.0000 | dio_mcm_episode_0qhiq5e (1) | dio_mcm_episode_0ldenly (1) | zentrum_stabil:1 | zentrum_stabil:1 |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.5556 | dio_mcm_episode_0jbl5pq (9) | dio_mcm_episode_0z748ck (6) | offene_variante:5; zentrum_stabil:4 | offene_variante:6; zentrum_stabil:3 |
| dio_mcm_episode_0y1i8dq | 1 | 1 | 1.0000 | dio_mcm_episode_0om13wf (1) | dio_mcm_episode_0om13wf (1) | offene_variante:1 | offene_variante:1 |
| dio_mcm_episode_1hs3jsa | 3 | 2 | 204.0000 | dio_mcm_episode_1q3us3f (2) | dio_mcm_episode_1q3us3f (2) | zentrum_stabil:3 | zentrum_stabil:2; spannungsrand_kippnaehe:1 |
| dio_mcm_episode_1i31hl0 | 1 | 1 | 2.0000 | dio_mcm_episode_1mesbjy (1) | dio_mcm_episode_0om13wf (1) | offene_variante:1 | zentrum_stabil:1 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0e7qvj1 | 0.0332 | -0.0103 | -0.0313 | 0.0089 | -0.1538 | 0.0105 | -0.0346 | 0.0104 |
| dio_mcm_episode_0hjnwsk | 0.0117 | 0.0118 | 0.0044 | -0.0298 | 0.0137 | -0.0539 | 0.0707 | -0.1094 |
| dio_mcm_episode_0ifxej6 | 0.0000 | -0.0368 | 0.0000 | 0.0313 | 0.0000 | -0.3330 | 0.0000 | 0.4615 |
| dio_mcm_episode_0jbl5pq | 0.0062 | -0.0112 | -0.0057 | 0.0140 | -0.0140 | -0.0021 | -0.1015 | 0.0244 |
| dio_mcm_episode_0l3i7ey | 0.0059 | 0.0087 | -0.0014 | -0.0042 | 0.0176 | 0.0468 | 0.0140 | -0.0819 |
| dio_mcm_episode_0q7j4gf | 0.0000 | 0.0775 | 0.0000 | -0.0629 | 0.0000 | -0.2076 | 0.0000 | -0.0275 |
| dio_mcm_episode_0qzjuvj | 0.0019 | 0.0023 | 0.0025 | 0.0031 | 0.0130 | 0.0525 | 0.0063 | 0.0104 |
| dio_mcm_episode_0y1i8dq | 0.0000 | -0.0876 | 0.0000 | 0.0603 | 0.0000 | 0.1083 | 0.0000 | 0.0967 |
| dio_mcm_episode_1hs3jsa | -0.0036 | -0.0733 | 0.0114 | 0.0784 | 0.0371 | 0.2563 | 0.0499 | 0.1202 |
| dio_mcm_episode_1i31hl0 | -0.0091 | 0.0158 | 0.0467 | -0.0537 | 0.3132 | -0.3151 | -0.0844 | 0.0255 |

## Befund

- `dio_mcm_episode_0e7qvj1`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_18l3thm`.
- `dio_mcm_episode_0hjnwsk`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_18n06fj`.
- `dio_mcm_episode_0ifxej6`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0r1o8ja`.
- `dio_mcm_episode_0jbl5pq`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0qzjuvj`.
- `dio_mcm_episode_0l3i7ey`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0lne9ax`.
- `dio_mcm_episode_0q7j4gf`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0ldenly`.
- `dio_mcm_episode_0qzjuvj`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0z748ck`.
- `dio_mcm_episode_0y1i8dq`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0om13wf`.
- `dio_mcm_episode_1hs3jsa`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1q3us3f`.
- `dio_mcm_episode_1i31hl0`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0om13wf`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
