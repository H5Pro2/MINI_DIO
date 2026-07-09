# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_00yl137 | 3 | 3 | 1.3333 | dio_mcm_episode_00er6t0 (1) | dio_mcm_episode_0ultars (1) | zentrum_stabil:2; spannungsrand_kippnaehe:1 | offene_variante:2; zentrum_stabil:1 |
| dio_mcm_episode_0b7nep9 | 70 | 5 | 107.8143 | dio_mcm_episode_0ykar6i (44) | dio_mcm_episode_0ykar6i (44) | zentrum_stabil:60; offene_variante:10 | zentrum_stabil:65; spannungsrand_kippnaehe:4; offene_variante:1 |
| dio_mcm_episode_0e7qvj1 | 90 | 8 | 193.1000 | dio_mcm_episode_0mji3u6 (25) | dio_mcm_episode_18l3thm (30) | zentrum_stabil:84; offene_variante:6 | zentrum_stabil:67; offene_variante:14; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_0hjnwsk | 8 | 4 | 2.6250 | dio_mcm_episode_0aztxel (4) | dio_mcm_episode_18n06fj (8) | offene_variante:6; zentrum_stabil:2 | zentrum_stabil:7; offene_variante:1 |
| dio_mcm_episode_0i7gfxw | 1 | 1 | 3.0000 | dio_mcm_episode_0tf9fq3 (1) | dio_mcm_episode_0hjnwsk (1) | offene_variante:1 | zentrum_stabil:1 |
| dio_mcm_episode_0ifxej6 | 1 | 1 | 1.0000 | dio_mcm_episode_0mm85pw (1) | dio_mcm_episode_0r1o8ja (1) | zentrum_stabil:1 | offene_variante:1 |
| dio_mcm_episode_0jbl5pq | 11 | 6 | 2.5455 | dio_mcm_episode_0lne9ax (6) | dio_mcm_episode_0qzjuvj (9) | zentrum_stabil:8; offene_variante:3 | zentrum_stabil:8; offene_variante:3 |
| dio_mcm_episode_0l3i7ey | 5 | 3 | 1.4000 | dio_mcm_episode_0ldht3x (3) | dio_mcm_episode_0lne9ax (2) | zentrum_stabil:4; offene_variante:1 | zentrum_stabil:4; offene_variante:1 |
| dio_mcm_episode_0mji3u6 | 25 | 6 | 14.0800 | dio_mcm_episode_0e7qvj1 (12) | dio_mcm_episode_0e7qvj1 (25) | zentrum_stabil:18; offene_variante:7 | zentrum_stabil:24; offene_variante:1 |
| dio_mcm_episode_0mvjoir | 3 | 3 | 1.0000 | dio_mcm_episode_0mw7rev (1) | dio_mcm_episode_0n5sqpn (1) | offene_variante:2; zentrum_stabil:1 | offene_variante:2; zentrum_stabil:1 |
| dio_mcm_episode_0om13wf | 6 | 2 | 1.3333 | dio_mcm_episode_0r1o8ja (1) | dio_mcm_episode_0ultars (3) | offene_variante:4; zentrum_stabil:2 | zentrum_stabil:3; offene_variante:3 |
| dio_mcm_episode_0qzjuvj | 9 | 6 | 2.5556 | dio_mcm_episode_0jbl5pq (9) | dio_mcm_episode_0z748ck (6) | offene_variante:5; zentrum_stabil:4 | offene_variante:6; zentrum_stabil:3 |
| dio_mcm_episode_0tf9fq3 | 1 | 1 | 1.0000 | dio_mcm_episode_0oc1i7g (1) | dio_mcm_episode_0i7gfxw (1) | offene_variante:1 | zentrum_stabil:1 |
| dio_mcm_episode_0ultars | 4 | 3 | 1.2500 | dio_mcm_episode_0om13wf (3) | dio_mcm_episode_0aztxel (2) | zentrum_stabil:2; offene_variante:2 | zentrum_stabil:2; offene_variante:1; spannungsrand_kippnaehe:1 |
| dio_mcm_episode_0v5p8er | 16 | 4 | 125.8125 | dio_mcm_episode_14l8khu (11) | dio_mcm_episode_14l8khu (11) | zentrum_stabil:12; offene_variante:3; spannungsrand_kippnaehe:1 | zentrum_stabil:9; offene_variante:7 |
| dio_mcm_episode_0ykar6i | 64 | 4 | 55.5625 | dio_mcm_episode_0b7nep9 (44) | dio_mcm_episode_0b7nep9 (44) | zentrum_stabil:51; offene_variante:11; spannungsrand_kippnaehe:2 | zentrum_stabil:31; offene_variante:27; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_14coypf | 22 | 3 | 128.0909 | dio_mcm_episode_18l3thm (7) | dio_mcm_episode_14l8khu (7) | zentrum_stabil:15; offene_variante:7 | zentrum_stabil:9; offene_variante:7; spannungsrand_kippnaehe:5 |
| dio_mcm_episode_14l8khu | 18 | 3 | 50.3333 | dio_mcm_episode_0v5p8er (11) | dio_mcm_episode_0v5p8er (11) | zentrum_stabil:16; offene_variante:2 | zentrum_stabil:12; offene_variante:6 |
| dio_mcm_episode_18l3thm | 52 | 6 | 14.5962 | dio_mcm_episode_0e7qvj1 (30) | dio_mcm_episode_0e7qvj1 (25) | zentrum_stabil:48; offene_variante:4 | zentrum_stabil:34; offene_variante:16; spannungsrand_kippnaehe:2 |
| dio_mcm_episode_18n06fj | 10 | 5 | 2.7000 | dio_mcm_episode_0hjnwsk (8) | dio_mcm_episode_0mji3u6 (10) | offene_variante:6; zentrum_stabil:4 | zentrum_stabil:6; offene_variante:4 |
| dio_mcm_episode_1al8fjz | 7 | 5 | 1.5714 | dio_mcm_episode_1k0rrn2 (2) | dio_mcm_episode_1y2gc2i (4) | zentrum_stabil:5; offene_variante:2 | zentrum_stabil:6; offene_variante:1 |
| dio_mcm_episode_1hs3jsa | 3 | 2 | 204.0000 | dio_mcm_episode_1q3us3f (2) | dio_mcm_episode_1q3us3f (2) | zentrum_stabil:3 | zentrum_stabil:2; spannungsrand_kippnaehe:1 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_00yl137 | 0.0017 | -0.0020 | 0.0030 | 0.0005 | -0.0083 | -0.1096 | 0.0040 | 0.2251 |
| dio_mcm_episode_0b7nep9 | 0.0602 | 0.0032 | -0.0617 | -0.0068 | -0.2600 | -0.0290 | -0.0996 | -0.0326 |
| dio_mcm_episode_0e7qvj1 | 0.0332 | -0.0103 | -0.0313 | 0.0089 | -0.1538 | 0.0105 | -0.0346 | 0.0104 |
| dio_mcm_episode_0hjnwsk | 0.0117 | 0.0118 | 0.0044 | -0.0298 | 0.0137 | -0.0539 | 0.0707 | -0.1094 |
| dio_mcm_episode_0i7gfxw | 0.0265 | 0.0173 | 0.0156 | -0.0030 | 0.1283 | 0.0522 | 0.0228 | -0.0129 |
| dio_mcm_episode_0ifxej6 | 0.0000 | -0.0368 | 0.0000 | 0.0313 | 0.0000 | -0.3330 | 0.0000 | 0.4615 |
| dio_mcm_episode_0jbl5pq | 0.0062 | -0.0112 | -0.0057 | 0.0140 | -0.0140 | -0.0021 | -0.1015 | 0.0244 |
| dio_mcm_episode_0l3i7ey | 0.0059 | 0.0087 | -0.0014 | -0.0042 | 0.0176 | 0.0468 | 0.0140 | -0.0819 |
| dio_mcm_episode_0mji3u6 | 0.0343 | 0.0140 | -0.0269 | -0.0191 | -0.0529 | -0.0088 | -0.1472 | -0.0431 |
| dio_mcm_episode_0mvjoir | 0.0000 | -0.0264 | 0.0000 | 0.0302 | 0.0000 | -0.0446 | 0.0000 | 0.0665 |
| dio_mcm_episode_0om13wf | -0.0067 | 0.0579 | 0.0101 | -0.0384 | 0.0367 | -0.0013 | 0.0152 | -0.1225 |
| dio_mcm_episode_0qzjuvj | 0.0019 | 0.0023 | 0.0025 | 0.0031 | 0.0130 | 0.0525 | 0.0063 | 0.0104 |
| dio_mcm_episode_0tf9fq3 | 0.0000 | -0.0131 | 0.0000 | -0.0073 | 0.0000 | 0.0847 | 0.0000 | -0.1871 |
| dio_mcm_episode_0ultars | 0.0063 | -0.0267 | -0.0028 | 0.0215 | 0.0157 | 0.0709 | 0.0368 | 0.0072 |
| dio_mcm_episode_0v5p8er | -0.0092 | -0.0054 | 0.0159 | 0.0013 | -0.0303 | -0.0368 | 0.0345 | 0.0649 |
| dio_mcm_episode_0ykar6i | -0.0052 | -0.0294 | 0.0133 | 0.0310 | 0.0642 | 0.1079 | 0.0155 | 0.0413 |
| dio_mcm_episode_14coypf | -0.0044 | -0.0505 | 0.0046 | 0.0573 | 0.0527 | 0.2311 | -0.0300 | 0.0796 |
| dio_mcm_episode_14l8khu | -0.0007 | -0.0221 | -0.0008 | 0.0210 | 0.0377 | 0.0997 | -0.0359 | 0.0455 |
| dio_mcm_episode_18l3thm | 0.0096 | -0.0254 | -0.0064 | 0.0221 | -0.0303 | 0.1058 | -0.0090 | 0.0075 |
| dio_mcm_episode_18n06fj | -0.0146 | -0.0103 | 0.0253 | 0.0025 | 0.0462 | 0.0475 | 0.0845 | 0.0132 |
| dio_mcm_episode_1al8fjz | -0.0047 | 0.0106 | 0.0043 | -0.0150 | 0.0025 | -0.0789 | 0.0524 | 0.0604 |
| dio_mcm_episode_1hs3jsa | -0.0036 | -0.0733 | 0.0114 | 0.0784 | 0.0371 | 0.2563 | 0.0499 | 0.1202 |

## Befund

- `dio_mcm_episode_00yl137`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0ultars`.
- `dio_mcm_episode_0b7nep9`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0ykar6i`.
- `dio_mcm_episode_0e7qvj1`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_18l3thm`.
- `dio_mcm_episode_0hjnwsk`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_18n06fj`.
- `dio_mcm_episode_0i7gfxw`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0hjnwsk`.
- `dio_mcm_episode_0ifxej6`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0r1o8ja`.
- `dio_mcm_episode_0jbl5pq`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0qzjuvj`.
- `dio_mcm_episode_0l3i7ey`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0lne9ax`.
- `dio_mcm_episode_0mji3u6`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_0mvjoir`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0n5sqpn`.
- `dio_mcm_episode_0om13wf`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0ultars`.
- `dio_mcm_episode_0qzjuvj`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0z748ck`.
- `dio_mcm_episode_0tf9fq3`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0i7gfxw`.
- `dio_mcm_episode_0ultars`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0aztxel`.
- `dio_mcm_episode_0v5p8er`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_14l8khu`.
- `dio_mcm_episode_0ykar6i`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0b7nep9`.
- `dio_mcm_episode_14coypf`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_14l8khu`.
- `dio_mcm_episode_14l8khu`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0v5p8er`.
- `dio_mcm_episode_18l3thm`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_18n06fj`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0mji3u6`.
- `dio_mcm_episode_1al8fjz`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_1y2gc2i`.
- `dio_mcm_episode_1hs3jsa`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1q3us3f`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
