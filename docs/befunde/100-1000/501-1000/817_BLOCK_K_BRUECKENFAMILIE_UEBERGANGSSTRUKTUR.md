# 817 - Block-K Brueckenfamilie/Uebergangsstruktur: dio_155c

## Fragestellung

Ist `dio_155c` nur ein stabiler Nachbar von `dio_1un4`, oder veraendert sich sein Feldprofil in direkter Randnaehe?

## Kontextvergleich

| Gruppe | Kontext | Ticks | Klasse | Stabil | Unruhe | Strain | Trust | Nachhall | Rekopplung | Hoeren-Stim. | Einbettung |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL | normal | 2598 | stabil | 0.9808 | 0.0192 | 0.1555 | 0.8172 | 0.3592 | 0.7161 | 0.2433 | 0.7780 |
| ALL | near_edge | 14 | stabil | 1.0000 | 0.0000 | 0.1495 | 0.8226 | 0.3528 | 0.7202 | 0.2376 | 0.7623 |
| ALL | before_edge | 8 | stabil | 1.0000 | 0.0000 | 0.1540 | 0.8227 | 0.3597 | 0.7176 | 0.2445 | 0.7488 |
| ALL | after_edge | 6 | stabil | 1.0000 | 0.0000 | 0.1436 | 0.8223 | 0.3435 | 0.7236 | 0.2283 | 0.7386 |
| kurz_2k | normal | 344 | stabil | 0.9797 | 0.0203 | 0.1547 | 0.7878 | 0.3241 | 0.7122 | 0.2434 | 0.7641 |
| kurz_2k | near_edge | 2 | stabil | 1.0000 | 0.0000 | 0.1518 | 0.8124 | 0.3383 | 0.7178 | 0.2227 | 0.6496 |
| kurz_2k | before_edge | 2 | stabil | 1.0000 | 0.0000 | 0.1518 | 0.8124 | 0.3383 | 0.7178 | 0.2227 | 0.6496 |
| kurz_2k | after_edge | 0 | - | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4000 |
| asset_mixed_2k | normal | 309 | stabil | 0.9838 | 0.0162 | 0.1543 | 0.7816 | 0.3106 | 0.7126 | 0.2396 | 0.7606 |
| asset_mixed_2k | near_edge | 3 | stabil | 1.0000 | 0.0000 | 0.1534 | 0.8061 | 0.3376 | 0.7156 | 0.2660 | 0.6889 |
| asset_mixed_2k | before_edge | 2 | stabil | 1.0000 | 0.0000 | 0.1583 | 0.8026 | 0.3186 | 0.7125 | 0.2722 | 0.6422 |
| asset_mixed_2k | after_edge | 1 | stabil | 1.0000 | 0.0000 | 0.1437 | 0.8132 | 0.3755 | 0.7217 | 0.2535 | 0.5324 |
| lang_10k | normal | 1945 | stabil | 0.9805 | 0.0195 | 0.1558 | 0.8281 | 0.3731 | 0.7173 | 0.2439 | 0.7830 |
| lang_10k | near_edge | 9 | stabil | 1.0000 | 0.0000 | 0.1477 | 0.8303 | 0.3610 | 0.7223 | 0.2314 | 0.7562 |
| lang_10k | before_edge | 4 | stabil | 1.0000 | 0.0000 | 0.1530 | 0.8380 | 0.3910 | 0.7201 | 0.2414 | 0.7267 |
| lang_10k | after_edge | 5 | stabil | 1.0000 | 0.0000 | 0.1436 | 0.8241 | 0.3371 | 0.7240 | 0.2233 | 0.7299 |

## Befund

`dio_155c` bleibt auch in direkter Naehe zu `dio_1un4` ueberwiegend stabil. Die Randnaehe veraendert aber das Profil:

- Strain-Delta near_edge gegen normal: -0.0059
- Trust-Delta near_edge gegen normal: 0.0053
- near_edge ist selten, aber nicht leer; die Bruecke ist also messbar, nicht nur theoretisch,
- die Stabilitaet bleibt in Randnaehe voll erhalten,
- Trust faellt nicht ab; die Bruecke kollabiert also nicht in Randbelastung,
- die Feldzeit-Einbettung ist in Randnaehe niedriger, weil diese Kontakte selten und lokal begrenzt sind.

Lesung: Die Brueckenfamilie wird nicht zur Randfamilie, sondern bleibt stabil und beruehrt die Randspannung ohne Vertrauensverlust. Das ist naeher an einer semantischen Uebergangsstruktur als an zufaelliger Nachbarschaft.

## Welt-Detail

| Gruppe | Welt | Kontext | Ticks | Strain | Trust | Einbettung |
|---|---|---|---:|---:|---:|---:|
| asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | normal | 93 | 0.1537 | 0.7936 | 0.7659 |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | normal | 73 | 0.1538 | 0.7757 | 0.7542 |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | before_edge | 1 | 0.1522 | 0.7977 | 0.5107 |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | near_edge | 1 | 0.1522 | 0.7977 | 0.5107 |
| asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | normal | 51 | 0.1527 | 0.7484 | 0.7376 |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | normal | 92 | 0.1563 | 0.7925 | 0.7648 |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | before_edge | 1 | 0.1643 | 0.8075 | 0.5237 |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | after_edge | 1 | 0.1437 | 0.8132 | 0.5324 |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | near_edge | 2 | 0.1540 | 0.8103 | 0.6531 |
| kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | normal | 100 | 0.1554 | 0.7962 | 0.7675 |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | normal | 96 | 0.1543 | 0.7967 | 0.7679 |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | before_edge | 1 | 0.1514 | 0.8271 | 0.5386 |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | near_edge | 1 | 0.1514 | 0.8271 | 0.5386 |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | normal | 73 | 0.1538 | 0.7757 | 0.7542 |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | before_edge | 1 | 0.1522 | 0.7977 | 0.5107 |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | near_edge | 1 | 0.1522 | 0.7977 | 0.5107 |
| kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | normal | 75 | 0.1550 | 0.7770 | 0.7541 |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | normal | 508 | 0.1559 | 0.8295 | 0.7837 |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | before_edge | 1 | 0.1623 | 0.8368 | 0.5381 |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | after_edge | 1 | 0.1525 | 0.8200 | 0.5343 |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | near_edge | 2 | 0.1574 | 0.8284 | 0.6612 |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | normal | 464 | 0.1556 | 0.8259 | 0.7811 |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | after_edge | 2 | 0.1379 | 0.8159 | 0.6444 |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | near_edge | 2 | 0.1379 | 0.8159 | 0.6444 |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | normal | 469 | 0.1556 | 0.8254 | 0.7802 |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | before_edge | 2 | 0.1475 | 0.8407 | 0.6686 |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | after_edge | 1 | 0.1415 | 0.8390 | 0.5422 |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | near_edge | 3 | 0.1455 | 0.8401 | 0.7098 |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | normal | 504 | 0.1560 | 0.8312 | 0.7850 |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | before_edge | 1 | 0.1546 | 0.8339 | 0.5316 |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | after_edge | 1 | 0.1480 | 0.8299 | 0.5341 |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | near_edge | 2 | 0.1513 | 0.8319 | 0.6578 |

## Grenze

Der Befund beschreibt passive Feldnaehe. Er ist keine Handlungsauswertung und keine Aussage ueber Richtung.

## Wie es weitergeht

Als naechstes sollte die Bruecke `dio_155c` mit einer zweiten Brueckenfamilie verglichen werden. Dann sehen wir, ob es einen gemeinsamen Brueckentyp gibt oder mehrere unterschiedliche Uebergangsarten.
