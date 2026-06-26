# 812 - Block-K semantische Verdichtung und Feldzeit

## Fragestellung

Vertieft laengere Feldzeit auch die semantische Bedeutungsverdichtung, oder werden `dio_*`-Inseln nur laenger getragen?

## Gruppensynthese

| Gruppe | Ticks | Symbol-Dichte | Semantik-Reuse | Familien-Dichte | Familien-Reuse | Top5-Familien | Wiederholte Familien | Feldzeit/Trust | Nachhall | Verdichtung | Top-Familie |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| kurz_2k | 1994.0000 | 0.1752 | 0.8248 | 0.1740 | 0.8260 | 0.2146 | 0.6472 | 0.5918 | 0.1387 | 0.6414 | dio_104t |
| asset_mixed_2k | 1994.0000 | 0.1718 | 0.8282 | 0.1709 | 0.8291 | 0.2133 | 0.6649 | 0.5954 | 0.1388 | 0.6460 | dio_104t |
| lang_10k | 9994.0000 | 0.0653 | 0.9347 | 0.0650 | 0.9350 | 0.2255 | 0.8715 | 0.7045 | 0.1730 | 0.7489 | dio_104t |

## Befund

Die 10k-Gruppe bildet nicht einfach eine groessere dominante Einzelinsel. Der Top-Familien-Anteil bleibt in einer aehnlichen Groessenordnung wie bei kurzen Welten. Der entscheidende Unterschied liegt in der Dichte:

- deutlich niedrigere Symbol- und Familien-Dichte,
- deutlich hoehere Wiederverwendung der eigenen Syntax,
- hoehere Feldzeit/Trust- und Nachhallwerte,
- stabile Top-Familie ueber alle Gruppen hinweg.

Damit wirkt 10k nicht wie `mehr neue Worte`, sondern wie tiefere Wiederverwendung vorhandener Bedeutungsfamilien. Die Bedeutungsinseln werden also nicht nur laenger getragen; sie werden effizienter in der laufenden Welt wiederverwendet.

## Detailauszug

| Gruppe | Welt | Symbol-Dichte | Semantik-Reuse | Top5-Familien | Feldzeit/Trust | Nachhall | Top-Familie |
|---|---|---:|---:|---:|---:|---:|---|
| asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | 0.1705 | 0.8295 | 0.2292 | 0.5978 | 0.1422 | dio_104t |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.1755 | 0.8245 | 0.1921 | 0.5892 | 0.1310 | dio_104t |
| asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | 0.1650 | 0.8350 | 0.2156 | 0.6042 | 0.1493 | dio_104t |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | 0.1760 | 0.8240 | 0.2161 | 0.5903 | 0.1327 | dio_104t |
| kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | 0.1785 | 0.8215 | 0.2161 | 0.5877 | 0.1381 | dio_104t |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | 0.1705 | 0.8295 | 0.2538 | 0.6049 | 0.1632 | dio_104t |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.1755 | 0.8245 | 0.1921 | 0.5892 | 0.1310 | dio_104t |
| kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | 0.1760 | 0.8240 | 0.1966 | 0.5855 | 0.1224 | dio_104t |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | 0.0641 | 0.9359 | 0.2355 | 0.7068 | 0.1768 | dio_104t |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | 0.0668 | 0.9332 | 0.2136 | 0.7020 | 0.1707 | dio_104t |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | 0.0624 | 0.9376 | 0.2293 | 0.7067 | 0.1727 | dio_104t |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | 0.0677 | 0.9323 | 0.2236 | 0.7023 | 0.1720 | dio_104t |

## Grenze

`Verdichtung` ist hier eine diagnostische Zusammenschau aus Reuse, Familienbindung, Wiederkehr und Feldzeit. Sie ist kein Gate, kein Zielwert und keine Handlungsvorschrift.

## Wie es weitergeht

Als naechstes sollte die stabile Top-Familie `dio_104t` selbst mit der Lupe gelesen werden: welche Feldlage, Sinnesachsen und Weltkontakte tragen diese Familie in 2k und 10k jeweils mit?
