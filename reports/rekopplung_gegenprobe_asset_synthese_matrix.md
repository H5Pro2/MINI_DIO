# Rekopplung: Gegenprobe Asset und synthetische Kontrolle

## Matrix

| Quelle | Gruppe | Klassen | n | Rollen | Komb. | Rekopplung | Erfahrung | Nachhall | Lesung |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| btc_paxg_signatur | BTC_2025_verteilt_rekoppelnd | verteilt_rekoppelnd | 3.0 | 5.3333 | 11.6667 | 0.695374 | 0.4344 | 0.3456 | rekoppelnder_referenzpol |
| btc_paxg_signatur | PAXG_5m_verteilt_rekoppelnd | verteilt_rekoppelnd | 4.0 | 7.2500 | 17.5000 | 0.704916 | 0.2515 | 0.3757 | rekoppelnder_referenzpol |
| btc_paxg_signatur | PAXG_offene_Breite | verteilt_offen | 11.0 | 6.8182 | 17.9091 | 0.691200 | 0.4680 | 0.3045 | offene_breite_gegenfolie |
| btc_doge_xrp_2025_late_5m | BTC | verteilt_offen, mittlere_uebergangsphase, verteilt_offen, verteilt_offen | 4.0 | 5.0000 | 10.2500 | 0.686322 | 0.5285 | 0.2694 | keine_rekopplung_trotz_breite |
| btc_doge_xrp_2025_late_5m | DOGE | verteilt_offen, mittlere_uebergangsphase, verteilt_offen, verteilt_offen | 4.0 | 5.5000 | 13.5000 | 0.686778 | 0.5094 | 0.2853 | keine_rekopplung_trotz_breite |
| btc_doge_xrp_2025_late_5m | XRP | verteilt_offen, verteilt_offen, verteilt_offen, verteilt_offen | 4.0 | 8.0000 | 21.2500 | 0.687166 | 0.4964 | 0.2908 | keine_rekopplung_trotz_breite |
| btc_doge_xrp_2025_1h | BTC | mittlere_uebergangsphase, verteilt_offen, verteilt_rekoppelnd, mittlere_uebergangsphase | 4.0 | 4.5000 | 8.5000 | 0.694570 | 0.5052 | 0.3403 | rekopplung_lokal |
| btc_doge_xrp_2025_1h | DOGE | mittlere_uebergangsphase, verteilt_offen, mittlere_uebergangsphase, kompakt_nachhallend | 4.0 | 3.2500 | 4.7500 | 0.693247 | 0.5434 | 0.3347 | keine_rekopplung_trotz_breite |
| btc_doge_xrp_2025_1h | XRP | verteilt_offen, mittlere_uebergangsphase, verteilt_offen, kompakt_nachhallend | 4.0 | 4.5000 | 9.0000 | 0.692689 | 0.5842 | 0.3355 | keine_rekopplung_trotz_breite |
| synthetische_kontrolle | synthetische_randrollen_kontrolle | kompakt_nachhallend | 6 | 1.5000 | 0.5000 | 0.722506 | 0.0040 | 0.5649 | kompakt_nachhallend_keine_rekopplung |

## Kurzlesung

- DOGE und XRP bilden in den geprüften Fenstern Rollenbreite, aber keine stabile `verteilt_rekoppelnd`-Klasse.
- BTC bildet Rekopplung nur lokal im 1h-/Zeitmaßbereich, nicht durchgehend.
- PAXG bildet die stärkste breite Rekopplung in den vorhandenen Vergleichsdaten.
- Die synthetische Randrollen- und Nullkontrolle bleibt kompakt nachhallend. Sie erzeugt keine rekoppelnde Breite.
- Damit wirkt `verteilt_rekoppelnd` nicht wie ein automatisches Nebenprodukt von Breite oder Rauschen, sondern wie eine selektive Feldfunktion unter bestimmten Weltspannungen.

## Grenze

Die Matrix ist eine passive Zusammenführung vorhandener Reports. Sie ist kein Beweis für eine allgemeine Gesetzmäßigkeit. Sie zeigt aber, dass Rekopplung in den bisherigen Daten selektiv auftritt und gegen offene Breite sowie synthetische Kompaktheit unterscheidbar bleibt.
