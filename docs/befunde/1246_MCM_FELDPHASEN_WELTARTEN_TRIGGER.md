# MCM-Feldphasen Weltarten-Trigger

Stand: 2026-07-02

## Grundfrage

Welche konkreten Weltarten loesen die weltgebundenen, lokalen, jungen oder grenznahen Feldphasen aus?

## Eingabe

- `docs\befunde\1245_MCM_FELDPHASEN_KLASSEN.csv`

## Profil

- untersuchte Phasen: `10`
- Klassen: `{'weltgebundene_feldphase': 5, 'grenzphase_mit_entlastung': 3, 'lokale_oder_driftende_phase': 1, 'junge_phasenspur': 1}`
- Weltarten in diesen Phasen: `{'stress_oder_negative_welt': 834, 'ruhige_oder_seitwaerts_welt': 760, 'alt_asset_welt': 303, 'synthetische_sinneswelt': 247, 'expansive_oder_positive_welt': 142, 'rand_bruch_welt': 103, 'sol_welt': 74, 'btc_welt': 74, 'paxg_welt': 74, 'zeit_oder_sequenz_welt': 44}`

## Phasenruecklesung

| Phase | Klasse | Anzahl | Welten | Wirkung | Weltarten | Top-Welten | Lesung |
|---|---|---:|---:|---|---|---|---|
| offene_variante->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | 1341 | 29 | rand_entlastet_in_offenheit | stress_oder_negative_welt:564; ruhige_oder_seitwaerts_welt:509; alt_asset_welt:104; expansive_oder_positive_welt:46; sol_welt:39; btc_welt:33; rand_bruch_welt:25; paxg_welt:16; synthetische_sinneswelt:4; zeit_oder_sequenz_welt:1 | BTC_STRESS_2024_5M:212; SOL_STRESS_2024_5M:203; SOL_QUIET_2024_5M:200; BTC_QUIET_2024_5M:192; DOGE_5M_10K:50; POS_EXPANSION_10K:46; NEG_STRESS_10K:43; SIDEWAYS_10K:41 | Grenzimpuls mit Entlastung; Feld kehrt ueber Offenheit zur Ordnung zurueck |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | 772 | 35 | zentrumsbruch_in_offenheit | stress_oder_negative_welt:172; ruhige_oder_seitwaerts_welt:156; alt_asset_welt:135; expansive_oder_positive_welt:68; rand_bruch_welt:56; synthetische_sinneswelt:54; zeit_oder_sequenz_welt:41; paxg_welt:40; btc_welt:27; sol_welt:23 | XRP_5M_10K:73; POS_EXPANSION_10K:68; NEG_STRESS_10K:64; SIDEWAYS_10K:51; DOGE_5M_10K:50; PAXG_5M_10K:40; SOL_STRESS_1H:35; BTC_QUIET_1H:30 | Grenzimpuls mit Entlastung; Feld kehrt ueber Offenheit zur Ordnung zurueck |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | 212 | 29 | rand_entlastet_in_offenheit | ruhige_oder_seitwaerts_welt:60; stress_oder_negative_welt:59; alt_asset_welt:30; rand_bruch_welt:18; expansive_oder_positive_welt:17; btc_welt:9; sol_welt:8; paxg_welt:6; synthetische_sinneswelt:5 | XRP_5M_10K:17; POS_EXPANSION_10K:17; SOL_QUIET_1H:16; SOL_STRESS_CURRENT:14; BTC_QUIET_CURRENT:11; BTC_STRESS_1H:11; SIDEWAYS_10K:10; SOL_STRESS_1H:10 | Grenzimpuls mit Entlastung; Feld kehrt ueber Offenheit zur Ordnung zurueck |
| spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | lokale_oder_driftende_phase | 181 | 6 | phase_offen | synthetische_sinneswelt:174; alt_asset_welt:4; expansive_oder_positive_welt:2; stress_oder_negative_welt:1 | SYNTH_DESYNC_AXES:100; SYNTH_VISUAL_STABLE_HEARING_CHAOTIC:74; DOGE_5M_10K:2; XRP_5M_10K:2; POS_EXPANSION_10K:2; NEG_STRESS_10K:1 | lokale Rand-Zentrum-Schleife; Driftverdacht statt Grundordnung |
| spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | weltgebundene_feldphase | 43 | 16 | zentrum_oeffnet_rekopplung | alt_asset_welt:12; ruhige_oder_seitwaerts_welt:11; stress_oder_negative_welt:8; synthetische_sinneswelt:4; paxg_welt:3; expansive_oder_positive_welt:3; btc_welt:1; rand_bruch_welt:1 | DOGE_5M_10K:6; XRP_5M_10K:6; BTC_QUIET_CURRENT:4; BTC_QUIET_1H:4; PAXG_5M_10K:3; NEG_STRESS_10K:3; POS_EXPANSION_10K:3; SYNTH_DESYNC_AXES:3 | randgebundene situative Phase; haeufigster Weltkontext: alt_asset_welt |
| offene_variante->spannungsrand_kippnaehe->rekopplungsnaehe | weltgebundene_feldphase | 32 | 17 | offenheit_geraet_in_kippnaehe | stress_oder_negative_welt:9; ruhige_oder_seitwaerts_welt:7; paxg_welt:5; alt_asset_welt:4; expansive_oder_positive_welt:3; btc_welt:2; sol_welt:1; rand_bruch_welt:1 | PAXG_5M_10K:5; BTC_QUIET_CURRENT:4; POS_EXPANSION_10K:3; SOL_STRESS_CURRENT:3; XRP_5M_10K:2; NEG_STRESS_10K:2; SIDEWAYS_10K:2; BTC_STRESS_CURRENT:2 | situative Phase; haeufigster Weltkontext: stress_oder_negative_welt |
| offene_variante->spannungsrand_kippnaehe->zentrum_stabil | weltgebundene_feldphase | 32 | 20 | offenheit_geraet_in_kippnaehe | stress_oder_negative_welt:11; ruhige_oder_seitwaerts_welt:6; alt_asset_welt:4; paxg_welt:2; btc_welt:2; synthetische_sinneswelt:2; sol_welt:2; zeit_oder_sequenz_welt:2; rand_bruch_welt:1 | NEG_STRESS_10K:3; PAXG_5M_10K:2; DOGE_5M_10K:2; BTC_1H_2K:2; SOL_STRESS_CURRENT:2; BTC_QUIET_CURRENT:2; BTC_STRESS_CURRENT:2; SOL_STRESS_1H:2 | situative Phase; haeufigster Weltkontext: stress_oder_negative_welt |
| rekopplungsnaehe->spannungsrand_kippnaehe->rekopplungsnaehe | weltgebundene_feldphase | 23 | 11 | phase_offen | alt_asset_welt:5; ruhige_oder_seitwaerts_welt:5; stress_oder_negative_welt:5; synthetische_sinneswelt:4; paxg_welt:2; sol_welt:1; expansive_oder_positive_welt:1 | XRP_5M_10K:4; SIDEWAYS_10K:4; SYNTH_DESYNC_AXES:4; BTC_STRESS_1H:3; PAXG_5M_10K:2; SOL_5M_2K:1; DOGE_5M_10K:1; NEG_STRESS_10K:1 | randgebundene situative Phase; haeufigster Weltkontext: alt_asset_welt |
| rekopplungsnaehe->spannungsrand_kippnaehe->zentrum_stabil | weltgebundene_feldphase | 18 | 11 | phase_offen | ruhige_oder_seitwaerts_welt:6; alt_asset_welt:5; stress_oder_negative_welt:5; expansive_oder_positive_welt:1; rand_bruch_welt:1 | DOGE_5M_10K:3; BTC_STRESS_CURRENT:3; XRP_5M_10K:2; SIDEWAYS_10K:2; BTC_QUIET_1H:2; NEG_STRESS_10K:1; POS_EXPANSION_10K:1; RAND_GEDEHNT:1 | randgebundene situative Phase; haeufigster Weltkontext: ruhige_oder_seitwaerts_welt |
| spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe | junge_phasenspur | 1 | 1 | phase_offen | expansive_oder_positive_welt:1 | POS_EXPANSION_10K:1 | junge Spur; noch keine belastbare Weltartbindung |

## Befund

Die situativen Phasen sind nicht zufaellig verteilt.

Sie liegen ueberwiegend dort, wo Rand/Kipp mit Zentrum, Rekopplung oder Offenheit gekoppelt wird.

Damit bestaetigt sich die Arbeitshierarchie:

```text
allgemeine Feldphasen = Grundordnung
weltgebundene Feldphasen = situative Reaktion
junge Phasenspuren = noch nicht gereifte Randbeobachtung
```

## Bedeutung

MINI_DIO bekommt dadurch keine neue Aktion. Es bekommt eine bessere Unterscheidung zwischen stabiler Innenordnung und situativer Weltwirkung.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese situativen Randphasen in der Rohwelt eher durch Bewegungsbruch, Lautheitslast, Zeitrahmen oder Assetcharakter entstehen.
