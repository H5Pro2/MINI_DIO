# MCM-Rollenwanderung Kandidaten

## Zweck

Diese Diagnose fasst zusammen, welche Tokens zwischen 894 und 901 ihre topologische Rolle wechseln.
Damit wird geprueft, ob `0b7nep9` ein Einzelphaenomen ist oder Teil einer allgemeinen Rollenwanderung.

## Profil

| Migration | Anzahl |
|---|---:|
| neue_rolle | 47 |
| stabile_rolle | 34 |
| rolle_zerfallen | 17 |
| rolle_verdichtet | 12 |
| rolle_entlastet_oder_driftet | 2 |

## Verdichtende Rollen

| Token | Basisrolle | Vergleichsrolle | Gewicht Delta | Dauer Delta |
|---|---|---|---:|---:|
| `0ykar6i` | schwacher_anschluss | brueckenkern | 212 | -628.65 |
| `0b7nep9` | starker_anschlussanker | brueckenkern | 193 | -385.79 |
| `1jx2k4i` | starker_anschlussanker | brueckenkern | 82 | -66.83 |
| `1jwnjz4` | schwacher_anschluss | starker_anschlussanker | 46 | 74.53 |
| `1xx3u1e` | lokaler_anschlussanker | brueckenkern | 37 | 110.08 |
| `1ahj81f` | schwacher_anschluss | starker_anschlussanker | 29 | -16.93 |
| `077r0df` | schwacher_anschluss | lokaler_anschlussanker | 15 | 7.00 |
| `1q3us3f` | lokaler_anschlussanker | starker_anschlussanker | 13 | 2.32 |
| `0geqqo3` | schwacher_anschluss | lokaler_anschlussanker | 11 | 29.14 |
| `0w4x7xs` | schwacher_anschluss | lokaler_anschlussanker | 9 | -72.83 |
| `1al8fjz` | schwacher_anschluss | lokaler_anschlussanker | 8 | -0.10 |
| `0z748ck` | lokaler_anschlussanker | brueckenkern | 4 | -50.30 |

## Neue Rollen

| Token | Basisrolle | Vergleichsrolle | Gewicht Delta | Dauer Delta |
|---|---|---|---:|---:|
| `14coypf` | - | brueckenkern | 57 | 100.07 |
| `0ybr5e3` | - | starker_anschlussanker | 41 | 112.37 |
| `1eju9g0` | - | schwacher_anschluss | 20 | 42.15 |
| `0wjn8vm` | - | lokaler_anschlussanker | 14 | 310.29 |
| `14l8khu` | - | lokaler_anschlussanker | 13 | 37.46 |
| `0dgle71` | - | schwacher_anschluss | 10 | 60.40 |
| `02ujuqf` | - | brueckenkern | 9 | 139.44 |
| `1engxbn` | - | schwacher_anschluss | 9 | 242.33 |
| `01s42m6` | - | schwacher_anschluss | 4 | 161.75 |
| `1t42af6` | - | schwacher_anschluss | 4 | 312.25 |
| `1ds636q` | - | schwacher_anschluss | 3 | 41.00 |
| `06ccuqv` | - | schwacher_anschluss | 2 | 2.00 |

## Entlastende Oder Driftende Rollen

| Token | Basisrolle | Vergleichsrolle | Gewicht Delta | Dauer Delta |
|---|---|---|---:|---:|
| `1hdpu9s` | lokaler_anschlussanker | schwacher_anschluss | -1 | -1.69 |
| `00nzcuc` | lokaler_anschlussanker | schwacher_anschluss | -13 | 218.93 |

## Zerfallende Rollen

| Token | Basisrolle | Vergleichsrolle | Gewicht Delta | Dauer Delta |
|---|---|---|---:|---:|
| `0h9ka55` | schwacher_anschluss | - | -1 | -733.00 |
| `0jatqr8` | schwacher_anschluss | - | -1 | -2.00 |
| `0jdgxa5` | schwacher_anschluss | - | -1 | -2007.00 |
| `0ldenly` | schwacher_anschluss | - | -1 | -3.00 |
| `0n22aiv` | schwacher_anschluss | - | -1 | -1753.00 |
| `0rz7ra9` | schwacher_anschluss | - | -1 | -2034.00 |
| `0sxikqi` | schwacher_anschluss | - | -1 | -283.00 |
| `0tosxof` | schwacher_anschluss | - | -1 | -1972.00 |
| `0vszw6h` | schwacher_anschluss | - | -1 | -3.00 |
| `1ej5zl7` | schwacher_anschluss | - | -1 | -532.00 |
| `1fej2vb` | schwacher_anschluss | - | -1 | -2034.00 |
| `1q3u8v6` | schwacher_anschluss | - | -1 | -2.00 |

## Befund

Die Rollenwanderung ist kein Einzelereignis. Mehrere Tokens verdichten sich von schwachen oder lokalen Anschlussrollen in starke Anschlussanker oder Brueckenkerne.
Gleichzeitig zerfallen andere Rollen oder entlasten sich. Das passt zu einer dynamischen MCM-Topologie: Rollen werden durch Weltspannung, Nachbarschaft und Feldkopplung getragen, nicht durch eine fixe Token-Eigenschaft.

Besonders relevant:

- `0b7nep9`: starker Anschlussanker -> Brueckenkern.
- `0ykar6i`: schwacher Anschluss -> Brueckenkern.
- `1jx2k4i`: starker Anschlussanker -> Brueckenkern.
- `1xx3u1e`: lokaler Anschlussanker -> Brueckenkern.
- `0z748ck`: lokaler Anschlussanker -> Brueckenkern.

## Wie es weitergeht

Als naechstes sollte eine einzelne zweite Rollenwanderung isoliert werden, vorzugsweise `0ykar6i`, weil es vom schwachen Anschluss zum Kernpartner von `0b7nep9` wird.