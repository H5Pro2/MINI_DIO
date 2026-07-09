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
| dio_mcm_episode_1rj8742 | breite_grundrolle | 17014 | 37 | REAL_FOLLOW_BTC_6000 | 0.932 | 0.573 | 0.173 | 0.000 |
| dio_mcm_episode_0icnf2v | breite_grundrolle | 90718 | 36 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.900 | 0.341 | 0.185 | 0.000 |
| dio_mcm_episode_1qlxgj7 | breite_grundrolle | 10973 | 38 | FOLLOW_DOGE_2024_5M_2000 | 0.881 | 0.368 | 0.173 | 0.000 |
| dio_mcm_episode_0wo0tz1 | breite_grundrolle | 4661 | 27 | BTC_FIELD_QUIET_03 | 0.811 | 0.768 | 0.128 | 0.071 |
| dio_mcm_episode_12tgchq | breite_grundrolle | 21382 | 23 | SOL_10K_A | 0.748 | 0.230 | 0.325 | 0.033 |
| dio_mcm_episode_0iwh9d2 | breite_grundrolle | 11006 | 20 | REAL_FOLLOW_PAXG_6000 | 0.664 | 0.155 | 0.403 | 0.047 |
| dio_mcm_episode_0tfzgic | breite_grundrolle | 7966 | 27 | REAL_TIME_2024_SOL_ALTSEQ_A | 0.645 | 0.157 | 0.445 | 0.033 |
| dio_mcm_episode_0nu3wih | breite_grundrolle | 2911 | 19 | QUIET_NEAR_PAXG2025_1H | 0.595 | 0.281 | 0.293 | 0.140 |
| dio_mcm_episode_1eav7xq | breite_grundrolle | 304 | 36 | FOLLOW_XRP_2024_5M_2000 | 0.577 | 0.265 | 0.110 | 0.247 |
| dio_mcm_episode_0vcr3lw | breite_grundrolle | 263 | 35 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.573 | 0.264 | 0.092 | 0.257 |
| dio_mcm_episode_0bsaqu1 | breite_grundrolle | 284 | 37 | SOL_10K_A | 0.565 | 0.289 | 0.091 | 0.251 |
| dio_mcm_episode_1yxc2ug | breite_grundrolle | 958 | 21 | REAL_FOLLOW_XRP_6000 | 0.559 | 0.151 | 0.161 | 0.208 |
| dio_mcm_episode_0vig3jz | breite_grundrolle | 12113 | 9 | REAL_TIME_2024_PAXG | 0.532 | 0.134 | 0.448 | 0.128 |
| dio_mcm_episode_08g1nk4 | breite_grundrolle | 225 | 32 | FOLLOW_XRP_2024_5M_2000 | 0.527 | 0.221 | 0.110 | 0.268 |
| dio_mcm_episode_0hvxln3 | breite_grundrolle | 197 | 34 | REAL_TIME_2023_SOL_ALTSEQ_A | 0.526 | 0.194 | 0.114 | 0.277 |
| dio_mcm_episode_14sn1ov | breite_grundrolle | 234 | 28 | BTC_10K_A | 0.513 | 0.212 | 0.120 | 0.278 |
| dio_mcm_episode_1aejc9m | breite_grundrolle | 255 | 20 | SOL_10K_A | 0.467 | 0.283 | 0.138 | 0.306 |
| dio_mcm_episode_0b8eoy2 | breite_grundrolle | 199 | 24 | FOLLOW_DOGE_2024_5M_2000 | 0.456 | 0.190 | 0.120 | 0.305 |
| dio_mcm_episode_1fdlu6e | breite_grundrolle | 2542 | 11 | REAL_TIME_2024_BTC_5M | 0.431 | 0.107 | 0.368 | 0.204 |
| dio_mcm_episode_0ca57t8 | uebergangsrolle | 411 | 12 | REAL_FOLLOW_PAXG_6000 | 0.425 | 0.431 | 0.123 | 0.324 |
| dio_mcm_episode_15z3zml | breite_grundrolle | 168 | 21 | SOL_10K_A | 0.422 | 0.212 | 0.147 | 0.331 |
| dio_mcm_episode_16bqw8k | breite_grundrolle | 75 | 25 | FOLLOW_XRP_2024_5M_2000 | 0.395 | 0.208 | 0.099 | 0.370 |
| dio_mcm_episode_0m8cxz1 | milieurolle | 1016 | 20 | BTC_LONG_2025_5M_QUIET | 0.383 | 0.171 | 0.508 | 0.209 |
| dio_mcm_episode_14pd6eb | breite_grundrolle | 122 | 17 | FOLLOW_XRP_2024_5M_2000 | 0.382 | 0.163 | 0.133 | 0.375 |
| dio_mcm_episode_0rbjarj | milieurolle | 1923 | 9 | REAL_FOLLOW_PAXG_6000 | 0.371 | 0.084 | 0.398 | 0.244 |

## Wie es weitergeht

Als nächstes diese Rollenbreiten gegen neue Welten aktualisieren und prüfen, ob Rollen nur breiter werden oder ob sich wirklich neue Milieus abspalten.
