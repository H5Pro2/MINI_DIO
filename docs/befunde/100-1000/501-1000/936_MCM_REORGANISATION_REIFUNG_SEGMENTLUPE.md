# MCM-Token Grenzlupe

## Zweck

Diese Diagnose liest nicht jeden Tick innerhalb eines Tokens, sondern nur die Segmentgrenzen.
Damit wird sichtbar, welches fremde Feldzeichen in einen Token hineinführt und welches wieder herausführt.

## Uebersicht

| Token | Segmente | Welten | Dauer | Hinein von | Heraus zu | Endrolle | Exitrolle |
|---|---:|---:|---:|---|---|---|---|
| dio_mcm_episode_00yl137 | 4 | 3 | 1.5000 | dio_mcm_episode_1iq1hgz (2) | dio_mcm_episode_0ultars (2) | offene_variante:2; zentrum_stabil:2 | zentrum_stabil:3; offene_variante:1 |
| dio_mcm_episode_0om13wf | 11 | 3 | 1.7273 | dio_mcm_episode_1mesbjy (2) | dio_mcm_episode_0ne8zu9 (3) | zentrum_stabil:6; offene_variante:5 | zentrum_stabil:6; offene_variante:5 |
| dio_mcm_episode_0z748ck | 39 | 5 | 2.6154 | dio_mcm_episode_0qzjuvj (30) | dio_mcm_episode_0e7qvj1 (32) | zentrum_stabil:33; offene_variante:6 | zentrum_stabil:31; offene_variante:7; spannungsrand_kippnaehe:1 |
| dio_mcm_episode_1hdpu9s | 114 | 5 | 25.6842 | dio_mcm_episode_0e7qvj1 (72) | dio_mcm_episode_0e7qvj1 (65) | zentrum_stabil:97; offene_variante:16; spannungsrand_kippnaehe:1 | zentrum_stabil:64; offene_variante:38; spannungsrand_kippnaehe:12 |

## Achsbewegung Innerhalb Des Segments Und Beim Austritt

| Token | Rekopplung innen | Rekopplung Exit | Strain innen | Strain Exit | Lautheit innen | Lautheit Exit | Unschaerfe innen | Unschaerfe Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_00yl137 | 0.0293 | -0.0201 | -0.0421 | 0.0015 | -0.1733 | -0.0303 | -0.0510 | 0.1184 |
| dio_mcm_episode_0om13wf | 0.0195 | 0.0076 | -0.0135 | -0.0019 | 0.0090 | 0.0046 | -0.0493 | -0.0530 |
| dio_mcm_episode_0z748ck | 0.0075 | -0.0015 | -0.0059 | 0.0018 | -0.0363 | 0.0104 | -0.0171 | -0.0026 |
| dio_mcm_episode_1hdpu9s | -0.0066 | -0.0313 | 0.0109 | 0.0358 | 0.0396 | 0.1256 | 0.0230 | 0.0397 |

## Befund

- `dio_mcm_episode_00yl137`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0ultars`.
- `dio_mcm_episode_0om13wf`: Austritt wirkt rekoppelnd; dominanter Austritt `dio_mcm_episode_0ne8zu9`.
- `dio_mcm_episode_0z748ck`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0e7qvj1`.
- `dio_mcm_episode_1hdpu9s`: Austritt wirkt oeffnend/belastend; dominanter Austritt `dio_mcm_episode_0e7qvj1`.

## Gesamtlesart

Die Grenzlupe ist die saubere Nachbarschaftspruefung.
Lange Selbstphasen werden nicht mehr als triviale Selbstnachbarschaft gezaehlt, sondern als Segment mit Eintritt und Austritt gelesen.

## Wie es weitergeht

Als naechstes sollten Driftlupe, Segmentlupe und Grenzlupe zu einer Klassifikation verbunden werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
