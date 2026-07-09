# MCM-Rollenbreiten-Metrik

## Zweck

Diese Diagnose liest vorhandene Preview-Anker passiv nach Rollenbreite.
Sie verändert keine Feldmechanik und erzeugt keine Handlungssignale.

## Lesarten

- `breite_grundrolle`: viele Welten, breite Verteilung, hohe Wiederkehr
- `uebergangsrolle`: deutliche Stress-/Shift- oder Milieu-Überbrückung
- `milieurolle`: hohe Spezifität für ein Milieu
- `nebenrolle`: geringe Breite oder geringe Wiederkehr

## Top-Rollen

| Rolle | Lesart | Count | Welten | Top-Welt | Breite | Übergang | Milieu | Neben |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| dio_mcm_episode_1rj8742 | breite_grundrolle | 15161 | 33 | REAL_FOLLOW_BTC_6000 | 0.928 | 0.615 | 0.194 | 0.000 |
| dio_mcm_episode_0icnf2v | breite_grundrolle | 76574 | 32 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.905 | 0.369 | 0.219 | 0.000 |
| dio_mcm_episode_1qlxgj7 | breite_grundrolle | 9019 | 34 | REAL_FOLLOW_SOL_6000 | 0.885 | 0.406 | 0.209 | 0.007 |
| dio_mcm_episode_0wo0tz1 | uebergangsrolle | 4119 | 24 | BTC_FIELD_QUIET_03 | 0.763 | 0.799 | 0.144 | 0.092 |
| dio_mcm_episode_12tgchq | breite_grundrolle | 18497 | 21 | SOL_10K_A | 0.706 | 0.225 | 0.379 | 0.043 |
| dio_mcm_episode_0iwh9d2 | breite_grundrolle | 10296 | 17 | REAL_FOLLOW_PAXG_6000 | 0.636 | 0.153 | 0.429 | 0.064 |
| dio_mcm_episode_0tfzgic | breite_grundrolle | 7708 | 24 | REAL_TIME_2024_SOL_ALTSEQ_A | 0.609 | 0.147 | 0.463 | 0.047 |
| dio_mcm_episode_0bsaqu1 | breite_grundrolle | 247 | 33 | SOL_10K_A | 0.563 | 0.311 | 0.102 | 0.261 |
| dio_mcm_episode_1eav7xq | breite_grundrolle | 261 | 33 | REAL_FOLLOW_DOGE_6000 | 0.562 | 0.279 | 0.097 | 0.257 |
| dio_mcm_episode_0vcr3lw | breite_grundrolle | 226 | 32 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.556 | 0.277 | 0.104 | 0.267 |
| dio_mcm_episode_0vig3jz | breite_grundrolle | 12113 | 9 | REAL_TIME_2024_PAXG | 0.532 | 0.134 | 0.448 | 0.128 |
| dio_mcm_episode_0nu3wih | breite_grundrolle | 2458 | 17 | QUIET_NEAR_PAXG2025_1H | 0.532 | 0.279 | 0.343 | 0.163 |
| dio_mcm_episode_1yxc2ug | breite_grundrolle | 763 | 18 | REAL_FOLLOW_XRP_6000 | 0.514 | 0.147 | 0.196 | 0.240 |
| dio_mcm_episode_08g1nk4 | breite_grundrolle | 187 | 29 | REAL_TIME_2024_XRP | 0.506 | 0.232 | 0.098 | 0.291 |
| dio_mcm_episode_0hvxln3 | breite_grundrolle | 166 | 31 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.496 | 0.194 | 0.131 | 0.292 |
| dio_mcm_episode_14sn1ov | breite_grundrolle | 193 | 26 | BTC_10K_A | 0.480 | 0.217 | 0.132 | 0.300 |
| dio_mcm_episode_1fdlu6e | breite_grundrolle | 2542 | 11 | REAL_TIME_2024_BTC_5M | 0.431 | 0.107 | 0.368 | 0.204 |
| dio_mcm_episode_0ca57t8 | uebergangsrolle | 411 | 12 | REAL_FOLLOW_PAXG_6000 | 0.425 | 0.431 | 0.123 | 0.324 |
| dio_mcm_episode_0b8eoy2 | breite_grundrolle | 162 | 21 | REAL_FOLLOW_XRP_6000 | 0.422 | 0.195 | 0.140 | 0.333 |
| dio_mcm_episode_1aejc9m | breite_grundrolle | 220 | 17 | SOL_10K_A | 0.418 | 0.281 | 0.157 | 0.333 |
| dio_mcm_episode_15z3zml | breite_grundrolle | 142 | 18 | SOL_10K_A | 0.382 | 0.213 | 0.170 | 0.358 |
| dio_mcm_episode_0rbjarj | milieurolle | 1923 | 9 | REAL_FOLLOW_PAXG_6000 | 0.371 | 0.084 | 0.398 | 0.244 |
| dio_mcm_episode_16bqw8k | nebenrolle | 61 | 22 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.367 | 0.217 | 0.088 | 0.398 |
| dio_mcm_episode_0m8cxz1 | milieurolle | 990 | 18 | BTC_LONG_2025_5M_QUIET | 0.353 | 0.160 | 0.524 | 0.221 |
| dio_mcm_episode_14pd6eb | nebenrolle | 94 | 15 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.349 | 0.167 | 0.126 | 0.406 |

## Wie es weitergeht

Als nächstes diese Rollenbreiten gegen neue Welten aktualisieren und prüfen, ob Rollen nur breiter werden oder ob sich wirklich neue Milieus abspalten.
