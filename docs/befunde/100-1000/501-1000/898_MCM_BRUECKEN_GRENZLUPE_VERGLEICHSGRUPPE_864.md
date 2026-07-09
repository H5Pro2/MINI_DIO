# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_02ujuqf | 3 | 3 | 3.0000 | dio_mcm_episode_0jwgafx (1) | dio_mcm_episode_1xx3u1e (3) | zentrum_stabil:3 | zentrum_stabil:3 |
| dio_mcm_episode_05lquqm | 5 | 5 | 1.2000 | dio_mcm_episode_0ag2osp (1) | dio_mcm_episode_079228h (1) | zentrum_stabil:4; offene_variante:1 | zentrum_stabil:3; offene_variante:2 |
| dio_mcm_episode_0b7nep9 | 70 | 5 | 107.8143 | dio_mcm_episode_0ykar6i (44) | dio_mcm_episode_0ykar6i (44) | zentrum_stabil:60; offene_variante:10 | zentrum_stabil:65; spannungsrand_kippnaehe:4; offene_variante:1 |
| dio_mcm_episode_0db07p4 | 7 | 3 | 10.5714 | dio_mcm_episode_1joiyc3 (3) | dio_mcm_episode_1joiyc3 (6) | zentrum_stabil:5; offene_variante:2 | zentrum_stabil:7 |
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.1000 | dio_mcm_episode_0mji3u6 (25) | dio_mcm_episode_18l3thm (30) | zentrum_stabil:84; offene_variante:6 | zentrum_stabil:67; offene_variante:14; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.5455 | dio_mcm_episode_0lne9ax (6) | dio_mcm_episode_0qzjuvj (9) | zentrum_stabil:8; offene_variante:3 | zentrum_stabil:8; offene_variante:3 |
| dio_mcm_episode_0mji3u6 | 25 | 6 | 14.0800 | dio_mcm_episode_0e7qvj1 (12) | dio_mcm_episode_0e7qvj1 (25) | zentrum_stabil:18; offene_variante:7 | zentrum_stabil:24; offene_variante:1 |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.5556 | dio_mcm_episode_0jbl5pq (9) | dio_mcm_episode_0z748ck (6) | offene_variante:5; zentrum_stabil:4 | offene_variante:6; zentrum_stabil:3 |
| dio_mcm_episode_0wjn8vm | 7 | 2 | 310.2857 | dio_mcm_episode_1engxbn (4) | dio_mcm_episode_1engxbn (5) | zentrum_stabil:7 | zentrum_stabil:6; offene_variante:1 |
| dio_mcm_episode_0ykar6i | 64 | 4 | 55.5625 | dio_mcm_episode_0b7nep9 (44) | dio_mcm_episode_0b7nep9 (44) | zentrum_stabil:51; offene_variante:11; spannungsrand_kippnaehe:2 | zentrum_stabil:31; offene_variante:27; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_0z748ck | 7 | 5 | 2.8571 | dio_mcm_episode_0qzjuvj (6) | dio_mcm_episode_0e7qvj1 (6) | zentrum_stabil:6; offene_variante:1 | zentrum_stabil:6; offene_variante:1 |
| dio_mcm_episode_14coypf | 22 | 3 | 128.0909 | dio_mcm_episode_18l3thm (7) | dio_mcm_episode_14l8khu (7) | zentrum_stabil:15; offene_variante:7 | zentrum_stabil:9; offene_variante:7; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_18l3thm | 52 | 6 | 14.5962 | dio_mcm_episode_0e7qvj1 (30) | dio_mcm_episode_0e7qvj1 (25) | zentrum_stabil:48; offene_variante:4 | zentrum_stabil:34; offene_variante:16; spannungsrand_kippnaehe:2 |
| dio_mcm_episode_18n06fj | 10 | 5 | 2.7000 | dio_mcm_episode_0hjnwsk (8) | dio_mcm_episode_0mji3u6 (10) | offene_variante:6; zentrum_stabil:4 | zentrum_stabil:6; offene_variante:4 |
| dio_mcm_episode_1al8fjz | 7 | 5 | 1.5714 | dio_mcm_episode_1k0rrn2 (2) | dio_mcm_episode_1y2gc2i (4) | zentrum_stabil:5; offene_variante:2 | zentrum_stabil:6; offene_variante:1 |
| dio_mcm_episode_1joiyc3 | 29 | 8 | 266.6207 | dio_mcm_episode_1jx2k4i (19) | dio_mcm_episode_1jx2k4i (16) | zentrum_stabil:23; offene_variante:5; spannungsrand_kippnaehe:1 | zentrum_stabil:21; spannungsrand_kippnaehe:5; offene_variante:2 |
| dio_mcm_episode_1jx2k4i | 40 | 6 | 25.5250 | dio_mcm_episode_1joiyc3 (16) | dio_mcm_episode_1joiyc3 (19) | zentrum_stabil:34; offene_variante:5; spannungsrand_kippnaehe:1 | zentrum_stabil:23; offene_variante:13; spannungsrand_kippnaehe:4 |
| dio_mcm_episode_1xx3u1e | 23 | 4 | 133.0435 | dio_mcm_episode_0ybr5e3 (10) | dio_mcm_episode_0ybr5e3 (11) | zentrum_stabil:16; offene_variante:7 | zentrum_stabil:14; offene_variante:8; spannungsrand_kippnaehe:1 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_02ujuqf | -0.0002 | -0.0023 | -0.0041 | 0.0046 | 0.0758 | -0.0223 | -0.0476 | 0.0180 |
| dio_mcm_episode_05lquqm | 0.0036 | 0.0081 | 0.0007 | -0.0039 | -0.0377 | -0.1250 | 0.0206 | 0.1380 |
| dio_mcm_episode_0b7nep9 | 0.0602 | 0.0032 | -0.0617 | -0.0068 | -0.2600 | -0.0290 | -0.0996 | -0.0326 |
| dio_mcm_episode_0db07p4 | 0.0211 | 0.0357 | -0.0226 | -0.0396 | -0.0420 | -0.0903 | -0.0400 | -0.0410 |
| dio_mcm_episode_0e7qvj1 | 0.0332 | -0.0103 | -0.0313 | 0.0089 | -0.1538 | 0.0105 | -0.0346 | 0.0104 |
| dio_mcm_episode_0jbl5pq | 0.0062 | -0.0112 | -0.0057 | 0.0140 | -0.0140 | -0.0021 | -0.1015 | 0.0244 |
| dio_mcm_episode_0mji3u6 | 0.0343 | 0.0140 | -0.0269 | -0.0191 | -0.0529 | -0.0088 | -0.1472 | -0.0431 |
| dio_mcm_episode_0qzjuvj | 0.0019 | 0.0023 | 0.0025 | 0.0031 | 0.0130 | 0.0525 | 0.0063 | 0.0104 |
| dio_mcm_episode_0wjn8vm | 0.0103 | -0.0058 | -0.0027 | 0.0054 | -0.0354 | 0.0336 | 0.0143 | 0.0558 |
| dio_mcm_episode_0ykar6i | -0.0052 | -0.0294 | 0.0133 | 0.0310 | 0.0642 | 0.1079 | 0.0155 | 0.0413 |
| dio_mcm_episode_0z748ck | 0.0168 | -0.0077 | -0.0295 | -0.0063 | -0.1122 | -0.0397 | -0.0816 | 0.0484 |
| dio_mcm_episode_14coypf | -0.0044 | -0.0505 | 0.0046 | 0.0573 | 0.0527 | 0.2311 | -0.0300 | 0.0796 |
| dio_mcm_episode_18l3thm | 0.0096 | -0.0254 | -0.0064 | 0.0221 | -0.0303 | 0.1058 | -0.0090 | 0.0075 |
| dio_mcm_episode_18n06fj | -0.0146 | -0.0103 | 0.0253 | 0.0025 | 0.0462 | 0.0475 | 0.0845 | 0.0132 |
| dio_mcm_episode_1al8fjz | -0.0047 | 0.0106 | 0.0043 | -0.0150 | 0.0025 | -0.0789 | 0.0524 | 0.0604 |
| dio_mcm_episode_1joiyc3 | 0.0346 | -0.0218 | -0.0367 | 0.0221 | -0.1153 | 0.1023 | -0.0679 | -0.0437 |
| dio_mcm_episode_1jx2k4i | -0.0021 | -0.0220 | 0.0002 | 0.0270 | 0.0361 | 0.0798 | -0.0146 | 0.0467 |
| dio_mcm_episode_1xx3u1e | -0.0159 | -0.0176 | 0.0113 | 0.0166 | 0.0976 | 0.0726 | 0.0141 | 0.0091 |

## Befund

- `dio_mcm_episode_02ujuqf`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1xx3u1e`.
- `dio_mcm_episode_05lquqm`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_079228h`.
- `dio_mcm_episode_0b7nep9`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0ykar6i`.
- `dio_mcm_episode_0db07p4`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_1joiyc3`.
- `dio_mcm_episode_0e7qvj1`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_18l3thm`.
- `dio_mcm_episode_0jbl5pq`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0qzjuvj`.
- `dio_mcm_episode_0mji3u6`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_0qzjuvj`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0z748ck`.
- `dio_mcm_episode_0wjn8vm`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1engxbn`.
- `dio_mcm_episode_0ykar6i`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0b7nep9`.
- `dio_mcm_episode_0z748ck`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_14coypf`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_14l8khu`.
- `dio_mcm_episode_18l3thm`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_18n06fj`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0mji3u6`.
- `dio_mcm_episode_1al8fjz`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_1y2gc2i`.
- `dio_mcm_episode_1joiyc3`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1jx2k4i`.
- `dio_mcm_episode_1jx2k4i`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1joiyc3`.
- `dio_mcm_episode_1xx3u1e`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0ybr5e3`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
