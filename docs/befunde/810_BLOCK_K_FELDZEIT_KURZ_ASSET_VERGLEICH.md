# 810 - Block-K Feldzeit Kurz/Asset-Vergleich

## Fragestellung

Reift Feldzeit primaer durch Dauer, durch Stress-/Regime-Art oder durch Asset-/Sinnesachsen-Mischung?

## Gruppensynthese

| Gruppe | Laeufe | Ticks | Max-Dauer | lange Segmente | gespannte Segmente | Carry-Anteil | Carry | Rekopplung | Strain | Nachhall | Feldzeit/Trust | dominantes Muster |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| kurz_normal | 4 Welten / 4 Rohlaeufe | 1994.0000 | 1271.5000 | 0.7500 | 1.0000 | 0.9995 | 0.5107 | 0.6949 | 0.1557 | 0.1387 | 0.5918 | kurz_getragen -> spannungsbruch -> lang_getragen |
| kurz_stress | 4 Welten / 4 Rohlaeufe | 1494.0000 | 1338.7500 | 0.5000 | 1.2500 | 0.9987 | 0.5051 | 0.6929 | 0.1563 | 0.1333 | 0.5620 | lang_getragen |
| asset_mixed_2k | 4 Welten / 12 Rohlaeufe | 1994.0000 | 861.2500 | 0.2500 | 5.0000 | 0.9974 | 0.5097 | 0.6928 | 0.1603 | 0.1488 | 0.5938 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| lang_10k | 4 Welten / 4 Rohlaeufe | 9994.0000 | 4558.2500 | 3.2500 | 3.5000 | 0.9996 | 0.5371 | 0.7057 | 0.1526 | 0.1730 | 0.7045 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |

## Befund

Die kurze Normal- und Stressgruppe bleibt getragen, zeigt aber deutlich weniger Feldzeit-Tiefe als die 10k-Gruppe. Die asset-gemischte 2k-Gruppe liegt zwischen kurzer Welt und langer 10k-Welt: sie ist nicht kollabiert, bildet aber keine durchgehend tiefe Feldzeit wie die langen Welten.

Lesart:

- Dauer wirkt stark auf Feldzeit/Trust und Nachhall.
- Stress-/Regime-Art veraendert Segmentmuster und Bruchhaeufigkeit, zerlegt die Grundordnung aber nicht automatisch.
- Asset-/Sinnesachsen-Mischung erzeugt Varianz, bleibt aber bei sauberer Rezeptoraufnahme feldtragend.
- 10k zeigt die tiefste Integrationsqualitaet, nicht nur mehr Rohdaten.

## Detailauszug

| Gruppe | Welt | Max-Dauer | Nachhall | Feldzeit/Trust | Muster |
|---|---|---:|---:|---:|---|
| asset_mixed_2k | BTC_2025_1H_2000 | 516.0000 | 0.1688 | 0.6037 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| asset_mixed_2k | KAS_2024_1H_2000 | 1348.0000 | 0.1525 | 0.5919 | kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| asset_mixed_2k | KAS_2024_5M_2000 | 836.0000 | 0.1420 | 0.5931 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| asset_mixed_2k | SOL_2025_5M_2000 | 745.0000 | 0.1320 | 0.5864 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| kurz_normal | kontrolliert_2026_sideways_test1_2000_5m_solusdt | 1145.0000 | 0.1381 | 0.5877 | kurz_getragen -> spannungsbruch -> lang_getragen |
| kurz_normal | kontrolliert_btc_2025_1h_test1_2000_btcusdt | 854.0000 | 0.1632 | 0.6049 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| kurz_normal | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 1994.0000 | 0.1310 | 0.5892 | lang_getragen |
| kurz_normal | kontrolliert_sol_2025_5m_test1_2000_solusdt | 1093.0000 | 0.1224 | 0.5855 | kurz_getragen -> spannungsbruch -> lang_getragen |
| kurz_stress | kontrolliert_2023_extreme_expansion_test1_1000_5m_solusdt | 373.0000 | 0.1272 | 0.5197 | kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen |
| kurz_stress | kontrolliert_2023_negative_stress_test1_1000_5m_solusdt | 994.0000 | 0.1301 | 0.5397 | kurz_getragen |
| kurz_stress | kontrolliert_2024_positive_stress_test1_2000_5m_solusdt | 1994.0000 | 0.1448 | 0.5958 | lang_getragen |
| kurz_stress | kontrolliert_2025_late_negative_test1_2000_5m_solusdt | 1994.0000 | 0.1310 | 0.5926 | lang_getragen |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | 5176.0000 | 0.1768 | 0.7068 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | 4514.0000 | 0.1707 | 0.7020 | lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | 5929.0000 | 0.1727 | 0.7067 | kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> kurz_getragen |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | 2614.0000 | 0.1720 | 0.7023 | lang_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> kurz_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen -> spannungsbruch -> lang_getragen |

## Grenze

Die Gruppen nutzen vorhandene Debuglaeufe. Das ist eine robuste Gegenprobe fuer die aktuelle Datenlage, aber noch kein vollstaendig neu generiertes Experiment mit exakt gleicher Laufzahl je Gruppe.

## Wie es weitergeht

Als naechstes sollte ein kontrollierter Neu-Lauf mit gleicher Gruppengroesse gebaut werden: je vier 2k-Welten, vier 10k-Welten und vier Asset-Mischwelten. Dann koennen Dauer- und Asset-Effekt sauberer getrennt werden.
