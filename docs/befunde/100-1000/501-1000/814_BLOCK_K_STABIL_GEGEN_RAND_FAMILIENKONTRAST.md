# 814 - Block-K Familienkontrast: stabil gegen Rand

## Fragestellung

Unterscheiden sich die stabile Traegerfamilie `dio_104t` und die gespannte Randfamilie `dio_1un4` in Feldlage, Sinnesachsen und Feldzeit?

## Auswahl der Randfamilie

`dio_1un4` wurde datengetrieben gewaehlt: ausreichend haeufig, in allen drei Gruppen vorhanden und mit der hoechsten durchschnittlichen MCM-Strain unter ueberwiegend `tragend_unruhig`-Familien.

## Gruppensynthese

| Gruppe | Rolle | Familie | Anteil | Klasse | Innenzustand | Strain | Rekopplung | Carry | Trust | Nachhall | Sehen-Gap | Hoeren-Gap | Hoeren-Stim. | Kontakt | Einbettung |
|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kurz_2k | stable | dio_104t | 0.0656 | stabil | inner_effect_stable | 0.1484 | 0.7196 | 0.5659 | 0.8214 | 0.4167 | 0.2061 | 0.0656 | 0.1440 | 0.0000 | 0.7876 |
| kurz_2k | edge | dio_1un4 | 0.0021 | tragend_unruhig | inner_effect_carried_unrest | 0.2306 | 0.6283 | 0.4291 | 0.4696 | 0.0125 | 0.3493 | 0.2679 | 0.4890 | 0.0000 | 0.5489 |
| asset_mixed_2k | stable | dio_104t | 0.0622 | stabil | inner_effect_stable | 0.1478 | 0.7207 | 0.5639 | 0.8152 | 0.3940 | 0.2060 | 0.0642 | 0.1425 | 0.0000 | 0.7828 |
| asset_mixed_2k | edge | dio_1un4 | 0.0025 | tragend_unruhig | inner_effect_carried_unrest | 0.2307 | 0.6284 | 0.4298 | 0.4566 | 0.0170 | 0.3475 | 0.2672 | 0.4880 | 0.0000 | 0.5390 |
| lang_10k | stable | dio_104t | 0.0673 | stabil | inner_effect_stable | 0.1486 | 0.7233 | 0.5751 | 0.8461 | 0.4340 | 0.2064 | 0.0656 | 0.1437 | 0.0000 | 0.7986 |
| lang_10k | edge | dio_1un4 | 0.0021 | tragend_unruhig | inner_effect_carried_unrest | 0.2230 | 0.6466 | 0.4712 | 0.6533 | 0.0475 | 0.3325 | 0.2652 | 0.4871 | 0.0000 | 0.6535 |

## Befund

`dio_104t` und `dio_1un4` sind nicht dasselbe Feldereignis mit anderem Namen. Der Kontrast ist systematisch sichtbar:

- `dio_104t` bleibt ueberwiegend `stabil` / `inner_effect_stable`.
- `dio_1un4` liegt ueberwiegend in `tragend_unruhig` / `inner_effect_carried_unrest`.
- die Randfamilie traegt deutlich mehr Strain und weniger Feldzeit/Trust.
- die stabile Familie traegt mehr Nachhall und hoehere Feldzeit-Einbettung.
- die Randfamilie zeigt hoehere Sehen-/Hoeren-Gaps und staerkere Hoer-Stimulation.
- der Unterschied liegt damit nicht nur in einem Namen, sondern in gekoppeltem Sinnes-/Feldprofil.

Damit sieht MINI_DIO nicht nur eine generische Bedeutungswolke. Es trennt mindestens eine stabile Traegerfamilie von einer unruhigen Randfamilie innerhalb desselben passiven MCM-Feldes.

## Grenze

Der Befund ist passiv. Er beschreibt Innenfeld- und Bedeutungsprofile, keine Strategie, keine Handlung und keine Richtungsvorhersage.

## Detailauszug

| Rolle | Gruppe | Welt | Anteil | Klasse | Strain | Trust | Nachhall | Einbettung |
|---|---|---|---:|---|---:|---:|---:|---:|
| stable | asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | 0.0737 | stabil | 0.1486 | 0.8270 | 0.4269 | 0.7908 |
| edge | asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | 0.0020 | tragend_unruhig | 0.2296 | 0.4609 | 0.0033 | 0.5444 |
| stable | asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.0557 | stabil | 0.1468 | 0.8088 | 0.3793 | 0.7786 |
| edge | asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.0020 | tragend_unruhig | 0.2349 | 0.4674 | 0.0149 | 0.5463 |
| stable | asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | 0.0627 | stabil | 0.1475 | 0.8151 | 0.3925 | 0.7838 |
| edge | asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | 0.0010 | tragend_unruhig | 0.2307 | 0.3012 | 0.0014 | 0.4404 |
| stable | asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | 0.0567 | stabil | 0.1484 | 0.8097 | 0.3774 | 0.7781 |
| edge | asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | 0.0050 | tragend_unruhig | 0.2278 | 0.5969 | 0.0485 | 0.6250 |
| stable | kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | 0.0667 | stabil | 0.1490 | 0.8290 | 0.4437 | 0.7935 |
| edge | kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | 0.0015 | tragend_unruhig | 0.2353 | 0.4071 | 0.0151 | 0.5099 |
| stable | kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | 0.0832 | stabil | 0.1488 | 0.8412 | 0.4766 | 0.8024 |
| edge | kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | 0.0025 | tragend_unruhig | 0.2276 | 0.5028 | 0.0127 | 0.5700 |
| stable | kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.0557 | stabil | 0.1468 | 0.8088 | 0.3793 | 0.7786 |
| edge | kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | 0.0020 | tragend_unruhig | 0.2349 | 0.4674 | 0.0149 | 0.5463 |
| stable | kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | 0.0567 | stabil | 0.1489 | 0.8067 | 0.3672 | 0.7757 |
| edge | kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | 0.0025 | tragend_unruhig | 0.2247 | 0.5013 | 0.0072 | 0.5695 |
| stable | lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | 0.0695 | stabil | 0.1493 | 0.8474 | 0.4376 | 0.7994 |
| edge | lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | 0.0021 | tragend_unruhig | 0.2215 | 0.6523 | 0.0252 | 0.6514 |
| stable | lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | 0.0602 | stabil | 0.1480 | 0.8429 | 0.4246 | 0.7965 |
| edge | lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | 0.0016 | tragend_unruhig | 0.2255 | 0.6439 | 0.0700 | 0.6507 |
| stable | lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | 0.0727 | stabil | 0.1488 | 0.8489 | 0.4441 | 0.8008 |
| edge | lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | 0.0028 | tragend_unruhig | 0.2223 | 0.6741 | 0.0424 | 0.6625 |
| stable | lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | 0.0665 | stabil | 0.1484 | 0.8453 | 0.4297 | 0.7977 |
| edge | lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | 0.0017 | tragend_unruhig | 0.2227 | 0.6430 | 0.0523 | 0.6496 |

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Randfamilie unter laengerer Folgewelt driftet, stabilisiert oder in eine eigene Bedeutungsinsel ausreift.
