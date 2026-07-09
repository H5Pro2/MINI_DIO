# 1981 - Rollenbreite mit gleichlangen 10k-Folgewelten

## Grundfrage

War der starke Rollenzuwachs aus 1980 teilweise durch gemischte Fensterlängen verzerrt, oder bleibt die Verbreiterung auch bei gleichlangen Folge-Welten sichtbar?

## Unterprüfung

Ausgehend von der 1980-Memory wurde eine Kopie mit drei gleichlangen 10k-Welten fortgeschrieben:

- PAXG 2024 5m, `10000` Kerzen
- DOGE 2024 5m, `10000` Kerzen
- XRP 2024 5m, `10000` Kerzen

KAS wurde hier bewusst ausgelassen, weil aktuell nur ein 2k-Fenster vorliegt. Dadurch bleibt diese Gegenprobe längengleich.

## Rollenklassen

| Lesart | 1980 | 1981 | Delta |
|---|---:|---:|---:|
| `breite_grundrolle` | 22 | 26 | 4 |
| `milieurolle` | 5 | 4 | -1 |
| `nebenrolle` | 72 | 89 | 17 |
| `uebergangsrolle` | 1 | 1 | 0 |

## Größte Zuwächse

| Symbol | Rolle 1980 | Rolle 1981 | Count Delta | Weltbreite Delta | Top-Welt |
|---|---|---|---:|---:|---|
| `dio_mcm_episode_12tgchq` | `breite_grundrolle` | `breite_grundrolle` | 11567 | 3 | `FOLLOW_EQ10K_DOGE_2024_5M` |
| `dio_mcm_episode_1qlxgj7` | `breite_grundrolle` | `breite_grundrolle` | 5911 | 3 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_0icnf2v` | `breite_grundrolle` | `breite_grundrolle` | 3663 | 3 | `REAL_TIME_2023_SOL_ALTSEQ_A` |
| `dio_mcm_episode_0iwh9d2` | `breite_grundrolle` | `breite_grundrolle` | 3298 | 3 | `REAL_FOLLOW_PAXG_6000` |
| `dio_mcm_episode_1rj8742` | `breite_grundrolle` | `breite_grundrolle` | 1007 | 3 | `REAL_FOLLOW_BTC_6000` |
| `dio_mcm_episode_1yxc2ug` | `breite_grundrolle` | `breite_grundrolle` | 506 | 3 | `FOLLOW_EQ10K_DOGE_2024_5M` |
| `dio_mcm_episode_1b57ksv` | `neu` | `nebenrolle` | 406 | 4 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_1eav7xq` | `breite_grundrolle` | `breite_grundrolle` | 197 | 3 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_0m8cxz1` | `milieurolle` | `breite_grundrolle` | 182 | 2 | `BTC_LONG_2025_5M_QUIET` |
| `dio_mcm_episode_0bsaqu1` | `breite_grundrolle` | `breite_grundrolle` | 171 | 3 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_1i3ov0z` | `milieurolle` | `milieurolle` | 168 | 3 | `BTC_FIELD_QUIET_03` |
| `dio_mcm_episode_0vcr3lw` | `breite_grundrolle` | `breite_grundrolle` | 164 | 3 | `FOLLOW_EQ10K_XRP_2024_5M` |

## Rollenwechsel

| Symbol | 1980 | 1981 | Count Delta | Weltbreite Delta |
|---|---|---|---:|---:|
| `dio_mcm_episode_0m8cxz1` | `milieurolle` | `breite_grundrolle` | 182 | 2 |
| `dio_mcm_episode_05upp98` | `nebenrolle` | `breite_grundrolle` | 77 | 3 |
| `dio_mcm_episode_16hqn22` | `nebenrolle` | `breite_grundrolle` | 28 | 3 |
| `dio_mcm_episode_0xg0gjh` | `nebenrolle` | `breite_grundrolle` | 17 | 3 |

## Neue Symbole in der Top-Metrik

| Symbol | Lesart | Count | Welten | Top-Welt |
|---|---|---:|---:|---|
| `dio_mcm_episode_1b57ksv` | `nebenrolle` | 406 | 4 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_010cqn6` | `nebenrolle` | 115 | 6 | `FOLLOW_EQ10K_PAXG_2024_5M` |
| `dio_mcm_episode_0hlxzy4` | `nebenrolle` | 49 | 10 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_16rn392` | `nebenrolle` | 34 | 9 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_0ws9wvs` | `nebenrolle` | 33 | 10 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_08q1993` | `nebenrolle` | 33 | 9 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_0a6jsal` | `nebenrolle` | 26 | 8 | `FOLLOW_EQ10K_PAXG_2024_5M` |
| `dio_mcm_episode_0wyfujk` | `nebenrolle` | 24 | 9 | `FOLLOW_EQ10K_PAXG_2024_5M` |
| `dio_mcm_episode_0imu3z8` | `nebenrolle` | 19 | 11 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_01h2hhh` | `nebenrolle` | 19 | 7 | `FOLLOW_EQ10K_DOGE_2024_5M` |

## Befund

Die gleichlange Gegenprobe bestätigt die Richtung aus 1980, aber schärfer: Neue Weltinformation wird weiterhin stark von vorhandenen Grundrollen aufgenommen. Die Anzahl der Milieurollen steigt nicht explosionsartig; die auffälligste Bewegung ist Rollenverbreiterung und Rollenreifung.

Auffällig ist `dio_mcm_episode_0icnf2v`: Die Rolle wächst weiter deutlich und bleibt breit. Das spricht gegen einen reinen Längeneffekt der vorherigen DOGE-/XRP-Läufe. Gleichzeitig entstehen neue Symbole in der Top-Metrik überwiegend als breite oder nebenläufige Kandidaten, nicht sofort als feste neue Milieus.

Damit bleibt die Arbeitshypothese stabil: MINI_DIO speichert neue Weltkontakte nicht primär als isolierte neue Rohsymbole, sondern koppelt sie zuerst an bestehende Bedeutungsräume. Erst wiederholte Eigenlast könnte später eine neue Milieurolle bilden.

## Artefakte

- Metrik: [1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_METRIK.csv](1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_METRIK.csv)
- Metrikbericht: [1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_METRIK.md](1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_METRIK.md)
- Delta: [1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_DELTA.csv](1981_MCM_ROLLENBREITEN_GLEICHLANG_10K_DELTA.csv)
- Memory: `memory/preview_depth_role_breadth_equal10k_probe.json`
- Debug: `debug/1981_equal10k_follow_eq10k_*`
