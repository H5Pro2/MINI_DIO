# 1982 - Rollenbreite mit KAS 10k als leiser Welt

## Grundfrage

Spaltet eine kleinpreisige/leise Welt wie KAS eigene starke Rollen ab, oder rekoppelt sie zuerst an vorhandene Grundrollen?

## Unterprüfung

Auf Basis der 1981-Memory wurde eine KAS-10k-Welt ergänzt:

- KAS 2024 5m, `10000` Kerzen
- Datenquelle: Binance Futures-UM, weil Spot-Monatsdaten für KAS 2024 nicht verfügbar waren
- Sense-Mode: `world_relative`
- Lauf bleibt passiv, ohne Handlung, Gate oder Motorik

## Rollenklassen

| Lesart | 1981 | 1982 | Delta |
|---|---:|---:|---:|
| `breite_grundrolle` | 26 | 28 | 2 |
| `milieurolle` | 4 | 4 | 0 |
| `nebenrolle` | 89 | 107 | 18 |
| `uebergangsrolle` | 1 | 1 | 0 |

## Größte Zuwächse

| Symbol | Rolle 1981 | Rolle 1982 | Count Delta | Weltbreite Delta | Top-Welt |
|---|---|---|---:|---:|---|
| `dio_mcm_episode_12tgchq` | `breite_grundrolle` | `breite_grundrolle` | 4470 | 1 | `FOLLOW_EQ10K_DOGE_2024_5M` |
| `dio_mcm_episode_1qlxgj7` | `breite_grundrolle` | `breite_grundrolle` | 2466 | 1 | `FOLLOW_EQ10K_KAS_2024_5M` |
| `dio_mcm_episode_0iwh9d2` | `breite_grundrolle` | `breite_grundrolle` | 851 | 1 | `REAL_FOLLOW_PAXG_6000` |
| `dio_mcm_episode_0icnf2v` | `breite_grundrolle` | `breite_grundrolle` | 471 | 1 | `REAL_TIME_2023_SOL_ALTSEQ_A` |
| `dio_mcm_episode_1b57ksv` | `nebenrolle` | `nebenrolle` | 440 | 1 | `FOLLOW_EQ10K_KAS_2024_5M` |
| `dio_mcm_episode_13vl4wk` | `neu` | `nebenrolle` | 224 | 5 | `BTC_STRESS_2024_5M` |
| `dio_mcm_episode_1yxc2ug` | `breite_grundrolle` | `breite_grundrolle` | 172 | 1 | `FOLLOW_EQ10K_DOGE_2024_5M` |

## Rollenwechsel

Zwei Nebenrollen reifen in die breite Grundrolle:

| Symbol | 1981 | 1982 | Count Delta | Weltbreite Delta |
|---|---|---|---:|---:|
| `dio_mcm_episode_0bygq81` | `nebenrolle` | `breite_grundrolle` | 36 | 1 |
| `dio_mcm_episode_171moy1` | `nebenrolle` | `breite_grundrolle` | 14 | 1 |

## Neue Symbole

Neue Top-Metrik-Symbole entstehen, bleiben aber Nebenrollen.

| Symbol | Lesart | Count | Welten | Top-Welt |
|---|---|---:|---:|---|
| `dio_mcm_episode_13vl4wk` | `nebenrolle` | 224 | 5 | `BTC_STRESS_2024_5M` |
| `dio_mcm_episode_0vmqpav` | `nebenrolle` | 44 | 5 | `FOLLOW_EQ10K_XRP_2024_5M` |
| `dio_mcm_episode_0u7qgeu` | `nebenrolle` | 27 | 7 | `FOLLOW_EQ10K_PAXG_2024_5M` |
| `dio_mcm_episode_11w0mrr` | `nebenrolle` | 22 | 9 | `FOLLOW_EQ10K_KAS_2024_5M` |
| `dio_mcm_episode_01116gq` | `nebenrolle` | 22 | 8 | `FOLLOW_EQ10K_KAS_2024_5M` |

## Befund

KAS erzeugt keine starke neue Milieuabspaltung. Die Milieurollen bleiben bei `4`, während Grundrollen und Nebenrollen wachsen.

Das ist fachlich wichtig, weil KAS als kleinpreisige/leise Welt eine gute Gegenprobe ist. Der Lauf zeigt nicht: "neues Asset, neue feste Bedeutung". Er zeigt eher:

- vorhandene Grundrollen nehmen KAS-Anteile auf
- einzelne Nebenrollen werden breiter
- neue KAS-nahe Kandidaten bleiben zunächst Nebenrollen
- das Feld reagiert nicht mit chaotischer Neuspeicherung

Damit bleibt die aktuelle MCM-Lesung stabil: neue Weltkontakte werden zuerst in vorhandene Bedeutungsräume rekoppelt. Erst wenn eine Nebenrolle wiederholt eigenes Gewicht trägt, kann daraus später eine neue Milieu- oder Grundrolle entstehen.

## Grenze

KAS 10k wurde aus Binance Futures-UM gebaut, weil Spot-Monatsdaten für KAS 2024 nicht verfügbar waren. Der Befund ist deshalb ein sauberer KAS-10k-Test, aber nicht direkt identisch mit den Spot-basierten Assets.

## Artefakte

- Welt: [data/kontrolliert_kas_2024_5m_10k_KASUSDT.csv](../../data/kontrolliert_kas_2024_5m_10k_KASUSDT.csv)
- Metrik: [1982_MCM_ROLLENBREITEN_KAS_10K_METRIK.csv](1982_MCM_ROLLENBREITEN_KAS_10K_METRIK.csv)
- Metrikbericht: [1982_MCM_ROLLENBREITEN_KAS_10K_METRIK.md](1982_MCM_ROLLENBREITEN_KAS_10K_METRIK.md)
- Delta: [1982_MCM_ROLLENBREITEN_KAS_10K_DELTA.csv](1982_MCM_ROLLENBREITEN_KAS_10K_DELTA.csv)
- Memory: `memory/preview_depth_role_breadth_equal10k_kas_probe.json`
- Debug: `debug/1982_equal10k_kas_2024_5m`

## Wie es weitergeht

Als nächstes sollte eine zweite leise/kleinpreisige Welt ergänzt werden, idealerweise nicht KAS. Ziel: prüfen, ob die KAS-Rekopplung assettypisch ist oder ob kleinpreisige Welten generell zuerst in vorhandene Grundrollen hineinreifen.
