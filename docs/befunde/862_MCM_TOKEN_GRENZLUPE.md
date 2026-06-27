# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_0v5p8er | 16 | 4 | 125.8125 | dio_mcm_episode_14l8khu (11) | dio_mcm_episode_14l8khu (11) | zentrum_stabil:12; offene_variante:3; spannungsrand_kippnaehe:1 | zentrum_stabil:9; offene_variante:7 |
| dio_mcm_episode_14l8khu | 18 | 3 | 50.3333 | dio_mcm_episode_0v5p8er (11) | dio_mcm_episode_0v5p8er (11) | zentrum_stabil:16; offene_variante:2 | zentrum_stabil:12; offene_variante:6 |
| dio_mcm_episode_1q3us3f | 26 | 6 | 67.8077 | dio_mcm_episode_18l3thm (19) | dio_mcm_episode_18l3thm (16) | zentrum_stabil:23; offene_variante:3 | offene_variante:13; zentrum_stabil:12; spannungsrand_kippnaehe:1 |
| dio_mcm_episode_1xx3u1e | 23 | 4 | 133.0435 | dio_mcm_episode_0ybr5e3 (10) | dio_mcm_episode_0ybr5e3 (11) | zentrum_stabil:16; offene_variante:7 | zentrum_stabil:14; offene_variante:8; spannungsrand_kippnaehe:1 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0v5p8er | -0.0092 | -0.0054 | 0.0159 | 0.0013 | -0.0303 | -0.0368 | 0.0345 | 0.0649 |
| dio_mcm_episode_14l8khu | -0.0007 | -0.0221 | -0.0008 | 0.0210 | 0.0377 | 0.0997 | -0.0359 | 0.0455 |
| dio_mcm_episode_1q3us3f | -0.0073 | -0.0243 | 0.0136 | 0.0332 | 0.0517 | 0.1310 | 0.0440 | 0.0241 |
| dio_mcm_episode_1xx3u1e | -0.0159 | -0.0176 | 0.0113 | 0.0166 | 0.0976 | 0.0726 | 0.0141 | 0.0091 |

## Befund

- `dio_mcm_episode_0v5p8er`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_14l8khu`.
- `dio_mcm_episode_14l8khu`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0v5p8er`.
- `dio_mcm_episode_1q3us3f`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_18l3thm`.
- `dio_mcm_episode_1xx3u1e`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0ybr5e3`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
