# 811 - Block-K Feldzeit kontrollierter Neulauf

## Fragestellung

Bleibt der Feldzeit-Befund bestehen, wenn jede Gruppe frisch, mit gleicher Gruppengroesse und eigener Memory gelesen wird?

## Kontrollaufbau

- `kurz_2k`: vier kurze Welten
- `lang_10k`: vier lange Welten
- `asset_mixed_2k`: vier asset-gemischte kurze Welten
- alle Laeufe mit frischer Memory und `sense-mode=world_relative`

## Gruppensynthese

| Gruppe | Welten | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | dominantes Muster |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| kurz_2k | 4 | 1994.0000 | 1271.5000 | 0.7500 | 1.0000 | 0.9995 | 0.5107 | 0.6949 | 0.1557 | 0.1387 | 0.5918 | kurz_getragen -> spannungsbruch -> lang_getragen |
| asset_mixed_2k | 4 | 1994.0000 | 1340.2500 | 1.0000 | 1.0000 | 0.9995 | 0.5113 | 0.6967 | 0.1551 | 0.1388 | 0.5954 | lang_getragen -> spannungsbruch -> kurz_getragen |
| lang_10k | 4 | 9994.0000 | 4558.2500 | 3.2500 | 3.5000 | 0.9996 | 0.5371 | 0.7057 | 0.1526 | 0.1730 | 0.7045 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |

## Befund

Der kontrollierte Neulauf bestaetigt den Feldzeit-Befund: die lange 10k-Gruppe bildet deutlich tiefere Feldzeit/Trust- und Nachhallwerte als die kurzen Gruppen. Die asset-gemischte 2k-Gruppe bleibt feldtragend, zeigt aber mehr Segmentwechsel und erreicht nicht die Feldzeit-Tiefe der 10k-Welten.

Lesart:

- Dauer bleibt der staerkste Treiber fuer Feldzeit-Tiefe.
- Asset-Mischung erzeugt zusaetzliche Varianz, aber keinen Feldkollaps.
- Weltrelative Sinnesaufnahme haelt die Gruppen vergleichbar.
- Feldzeit erscheint weiterhin als gewachsene Integrationsqualitaet, nicht als programmierte Zeitachse.

## Detailauszug

| Gruppe | Welt | Max-Dauer | Nachhall | Feldzeit/Trust | Muster |
|---|---|---:|---:|---:|---|
| kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | 1093 | 0.1224 | 0.5855 | kurz_getragen -> spannungsbruch -> lang_getragen |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | 854 | 0.1632 | 0.6049 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 1994 | 0.1310 | 0.5892 | lang_getragen |
| kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | 1145 | 0.1381 | 0.5877 | kurz_getragen -> spannungsbruch -> lang_getragen |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | 5176 | 0.1768 | 0.7068 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | 4514 | 0.1707 | 0.7020 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | 5929 | 0.1727 | 0.7067 | kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> kurz_getragen |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | 2614 | 0.1720 | 0.7023 | lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | 1172 | 0.1327 | 0.5903 | lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | 1172 | 0.1422 | 0.5978 | lang_getragen -> spannungsbruch -> kurz_getragen |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 1994 | 0.1310 | 0.5892 | lang_getragen |
| asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | 1023 | 0.1493 | 0.6042 | lang_getragen -> spannungsbruch -> kurz_getragen |

## Grenze

Der Befund bleibt ein passiver Diagnosebefund. Er sagt etwas ueber Feldzeit-Integration, nicht ueber Handlung oder Strategie.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob die laengere Feldzeit auch die semantische Bedeutungsverdichtung vertieft: bleiben die `dio_*`-Bedeutungsinseln in 10k stabiler, oder werden sie nur laenger getragen?
