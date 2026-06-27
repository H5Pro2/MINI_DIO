# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_05lquqm | 2 | 1 | 2.0000 | dio_mcm_episode_08ubq99 (1) | dio_mcm_episode_0ej0lhx (1) | zentrum_stabil:2 | zentrum_stabil:2 |
| dio_mcm_episode_0b7nep9 | 18 | 3 | 472.3889 | dio_mcm_episode_00nzcuc (8) | dio_mcm_episode_00nzcuc (6) | zentrum_stabil:17; offene_variante:1 | zentrum_stabil:12; spannungsrand_kippnaehe:3; offene_variante:2 |
| dio_mcm_episode_0db07p4 | 15 | 5 | 17.6000 | dio_mcm_episode_1joiyc3 (6) | dio_mcm_episode_1joiyc3 (11) | zentrum_stabil:11; offene_variante:4 | zentrum_stabil:13; offene_variante:2 |
| dio_mcm_episode_0e7qvj1 | 54 | 6 | 259.2963 | dio_mcm_episode_18l3thm (19) | dio_mcm_episode_18l3thm (23) | zentrum_stabil:50; offene_variante:4 | zentrum_stabil:43; offene_variante:6; spannungsrand_kippnaehe:3 |
| dio_mcm_episode_0jbl5pq | 10 | 5 | 2.0000 | dio_mcm_episode_0lne9ax (4) | dio_mcm_episode_0qzjuvj (7) | zentrum_stabil:6; offene_variante:4 | zentrum_stabil:7; offene_variante:3 |
| dio_mcm_episode_0mji3u6 | 11 | 5 | 8.9091 | dio_mcm_episode_0e7qvj1 (6) | dio_mcm_episode_0e7qvj1 (11) | zentrum_stabil:9; offene_variante:2 | zentrum_stabil:11 |
| dio_mcm_episode_0qzjuvj | 10 | 5 | 2.7000 | dio_mcm_episode_0jbl5pq (7) | dio_mcm_episode_0z748ck (9) | zentrum_stabil:8; offene_variante:2 | zentrum_stabil:5; offene_variante:5 |
| dio_mcm_episode_18l3thm | 34 | 5 | 45.2647 | dio_mcm_episode_0e7qvj1 (23) | dio_mcm_episode_0e7qvj1 (19) | zentrum_stabil:28; offene_variante:6 | zentrum_stabil:18; offene_variante:13; spannungsrand_kippnaehe:3 |
| dio_mcm_episode_18n06fj | 6 | 4 | 2.3333 | dio_mcm_episode_0hjnwsk (4) | dio_mcm_episode_0mji3u6 (4) | zentrum_stabil:3; offene_variante:3 | zentrum_stabil:4; offene_variante:2 |
| dio_mcm_episode_1al8fjz | 3 | 2 | 1.6667 | dio_mcm_episode_0dsrwv5 (1) | dio_mcm_episode_1y2gc2i (2) | zentrum_stabil:3 | zentrum_stabil:3 |
| dio_mcm_episode_1joiyc3 | 29 | 7 | 200.8966 | dio_mcm_episode_1jx2k4i (17) | dio_mcm_episode_1jx2k4i (16) | zentrum_stabil:26; offene_variante:3 | zentrum_stabil:19; offene_variante:5; spannungsrand_kippnaehe:4 |
| dio_mcm_episode_1xx3u1e | 6 | 2 | 15.0000 | dio_mcm_episode_0geqqo3 (6) | dio_mcm_episode_0geqqo3 (5) | zentrum_stabil:6 | offene_variante:4; zentrum_stabil:2 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_05lquqm | 0.0155 | -0.0266 | 0.0092 | 0.0216 | -0.0511 | 0.1732 | 0.0162 | 0.0961 |
| dio_mcm_episode_0b7nep9 | 0.0248 | -0.0240 | -0.0244 | 0.0253 | -0.0391 | 0.1059 | -0.0765 | -0.0237 |
| dio_mcm_episode_0db07p4 | 0.0103 | 0.0257 | -0.0135 | -0.0305 | -0.0522 | -0.0701 | -0.0301 | -0.0191 |
| dio_mcm_episode_0e7qvj1 | 0.0410 | -0.0139 | -0.0415 | 0.0122 | -0.1722 | 0.0422 | -0.0690 | 0.0024 |
| dio_mcm_episode_0jbl5pq | -0.0016 | -0.0002 | 0.0092 | -0.0031 | 0.0641 | -0.0571 | -0.0073 | 0.0201 |
| dio_mcm_episode_0mji3u6 | 0.0475 | 0.0025 | -0.0485 | -0.0043 | -0.1504 | 0.0601 | -0.1207 | -0.0652 |
| dio_mcm_episode_0qzjuvj | 0.0069 | -0.0217 | 0.0002 | 0.0204 | 0.0338 | 0.0320 | -0.0115 | 0.0871 |
| dio_mcm_episode_18l3thm | 0.0018 | -0.0277 | 0.0039 | 0.0315 | -0.0037 | 0.1525 | 0.0074 | 0.0045 |
| dio_mcm_episode_18n06fj | -0.0001 | -0.0073 | 0.0013 | 0.0042 | 0.0570 | 0.0154 | -0.0046 | -0.0009 |
| dio_mcm_episode_1al8fjz | -0.0166 | -0.0044 | 0.0212 | 0.0031 | 0.0988 | -0.0606 | 0.0910 | 0.0884 |
| dio_mcm_episode_1joiyc3 | 0.0247 | -0.0254 | -0.0243 | 0.0308 | -0.1138 | 0.1250 | -0.0390 | 0.0069 |
| dio_mcm_episode_1xx3u1e | -0.0046 | -0.0681 | 0.0117 | 0.0638 | 0.0557 | 0.2479 | 0.0416 | 0.0230 |

## Befund

- `dio_mcm_episode_05lquqm`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0ej0lhx`.
- `dio_mcm_episode_0b7nep9`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_00nzcuc`.
- `dio_mcm_episode_0db07p4`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_1joiyc3`.
- `dio_mcm_episode_0e7qvj1`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_18l3thm`.
- `dio_mcm_episode_0jbl5pq`: Austritt wirkt gemischt; dominanter Austritt `dio_mcm_episode_0qzjuvj`.
- `dio_mcm_episode_0mji3u6`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_0qzjuvj`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0z748ck`.
- `dio_mcm_episode_18l3thm`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_18n06fj`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0mji3u6`.
- `dio_mcm_episode_1al8fjz`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1y2gc2i`.
- `dio_mcm_episode_1joiyc3`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_1jx2k4i`.
- `dio_mcm_episode_1xx3u1e`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0geqqo3`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
