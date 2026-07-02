# MCM-Feldphasen Fensterlupe

Stand: 2026-07-02

## Grundfrage

Was passiert direkt vor, waehrend und nach situativen Rand-/Kipp-Phasen?

## Unterpruefung

Diese Diagnose liest vorhandene Feldphasen-Segmente als Dreifenster:

```text
vorherige Feldrolle -> aktuelle Feldrolle -> folgende Feldrolle
```

Sie prueft nicht Handlung und nicht Strategie. Sie prueft nur Feldbewegung.

## Eingaben

- Zielphasen: `docs\befunde\1248_MCM_FELDPHASEN_ROHFELD_KOPPLUNG.csv`
- Segmentquellen: `docs/befunde/*FELDPHASEN*SEGMENTE.csv`

## Profil

- gefundene Fenster: `2655`
- untersuchte Phasenfamilien: `10`
- Fensterlesarten: `{'lastkontakt_entlastet': 2077, 'rekopplung_vor_neuer_last': 184, 'rekopplung_bricht_in_last': 168, 'gemischtes_fenster': 145, 'rekopplung_nimmt_zu': 78, 'lastkontakt_bleibt': 3}`
- Phasenklassen: `{'grenzphase_mit_entlastung': 2325, 'lokale_oder_driftende_phase': 181, 'weltgebundene_feldphase': 148, 'junge_phasenspur': 1}`
- Weltarten: `{'ruhige_oder_seitwaerts_welt': 1350, 'unbekannte_welt': 452, 'stress_oder_negative_welt': 372, 'synthetische_sinneswelt': 155, 'expansive_oder_positive_welt': 142, 'btc_welt': 74, 'paxg_welt': 74, 'kas_welt': 36}`

## Phasenuebersicht

| Phase | Fenster | Lesart | Weltart | Rekopplung | Strain | Delta Rekopplung | Delta Strain | Signal |
|---|---:|---|---|---:|---:|---:|---:|---:|
| offene_variante->spannungsrand_kippnaehe->offene_variante | 1341 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5910 | 0.2819 | 0.0609 | -0.0942 | 9.5839 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | 772 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5901 | 0.2808 | 0.0738 | -0.0961 | 15.0000 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | 212 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5892 | 0.2790 | 0.0734 | -0.0962 | 14.4057 |
| spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 181 | rekopplung_vor_neuer_last | stress_oder_negative_welt | 0.7391 | 0.1409 | -0.1116 | 0.1343 | 15.0000 |
| spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 43 | gemischtes_fenster | ruhige_oder_seitwaerts_welt | 0.7173 | 0.1454 | -0.0121 | 0.0001 | 15.0000 |
| offene_variante->spannungsrand_kippnaehe->rekopplungsnaehe | 32 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5919 | 0.2719 | 0.1131 | -0.1211 | 15.0000 |
| offene_variante->spannungsrand_kippnaehe->zentrum_stabil | 32 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5983 | 0.2653 | 0.1219 | -0.1238 | 15.0000 |
| rekopplungsnaehe->spannungsrand_kippnaehe->rekopplungsnaehe | 23 | lastkontakt_entlastet | unbekannte_welt | 0.5989 | 0.2715 | 0.1046 | -0.1167 | 15.0000 |
| rekopplungsnaehe->spannungsrand_kippnaehe->zentrum_stabil | 18 | lastkontakt_entlastet | ruhige_oder_seitwaerts_welt | 0.5989 | 0.2628 | 0.1205 | -0.1186 | 15.0000 |
| spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe | 1 | rekopplung_vor_neuer_last | expansive_oder_positive_welt | 0.7049 | 0.1368 | -0.1045 | 0.1186 | 15.0000 |

## Beispiel-Fenster

| Phase | Welt | Ticks | Lesart | Intake | Loudness | Sharpness | Rekopplung | Strain | Folge-Delta |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | SOL_QUIET_CURRENT | 1692-1695 | lastkontakt_entlastet | 0.5010 | 0.8775 | 0.2808 | 0.5283 | 0.3504 | reko 0.1412, strain -0.1631 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | SIDEWAYS_10K | 4231-4235 | lastkontakt_entlastet | 0.5454 | 0.9519 | 0.6279 | 0.5359 | 0.3461 | reko 0.1129, strain -0.1367 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | NEG_STRESS_10K | 8954-8957 | lastkontakt_entlastet | 0.5156 | 0.9045 | 0.5780 | 0.5380 | 0.3389 | reko 0.1427, strain -0.1672 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 8808-8812 | lastkontakt_entlastet | 0.5432 | 0.9603 | 0.6558 | 0.5408 | 0.3382 | reko 0.1025, strain -0.1287 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | BTC_STRESS_1H | 697-699 | lastkontakt_entlastet | 0.4972 | 0.8779 | 0.5060 | 0.5391 | 0.3379 | reko 0.1157, strain -0.1482 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | RAND_GEDEHNT | 650-1203 | lastkontakt_entlastet | 0.5811 | 0.9794 | 0.7151 | 0.5730 | 0.3368 | reko 0.0838, strain -0.1498 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | BTC_STRESS_CURRENT | 3603-3625 | lastkontakt_entlastet | 0.5513 | 0.9709 | 0.6044 | 0.5489 | 0.3364 | reko 0.0948, strain -0.1288 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | SIDEWAYS_10K | 546-556 | lastkontakt_entlastet | 0.4777 | 0.8642 | 0.3751 | 0.5376 | 0.3359 | reko 0.1135, strain -0.1432 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | BTC_QUIET_1H | 2444-2452 | lastkontakt_entlastet | 0.4898 | 0.8670 | 0.4974 | 0.5413 | 0.3357 | reko 0.1107, strain -0.1466 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 1927-1930 | lastkontakt_entlastet | 0.5288 | 0.9265 | 0.6644 | 0.5436 | 0.3356 | reko 0.0796, strain -0.1023 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 2313-2316 | lastkontakt_entlastet | 0.5505 | 0.9628 | 0.6355 | 0.5486 | 0.3356 | reko 0.1090, strain -0.1534 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | RAND_KOMPAKT | 154-303 | lastkontakt_entlastet | 0.5720 | 0.9634 | 0.7211 | 0.5737 | 0.3355 | reko 0.0886, strain -0.1578 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | SOL_QUIET_1H | 2749-2760 | lastkontakt_entlastet | 0.5073 | 0.8932 | 0.5796 | 0.5427 | 0.3352 | reko 0.1258, strain -0.1598 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | BTC_QUIET_1H | 3004-3011 | lastkontakt_entlastet | 0.4975 | 0.8808 | 0.5333 | 0.5425 | 0.3347 | reko 0.1216, strain -0.1503 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | DOGE_5M_10K | 6405-6409 | lastkontakt_entlastet | 0.5167 | 0.9013 | 0.6469 | 0.5449 | 0.3347 | reko 0.1356, strain -0.1605 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | SOL_QUIET_CURRENT | 2663-2665 | lastkontakt_entlastet | 0.5131 | 0.9003 | 0.4954 | 0.5410 | 0.3345 | reko 0.1154, strain -0.1430 |

## Befund

Die Fensterlupe bestaetigt die vorherige Rohfeld-Kopplung genauer: Viele Rand-/Kippkontakte wirken nicht als dauerhafter Kollaps, sondern als kurzer Lastkontakt mit anschliessender Entlastung.

Der wichtige Punkt ist die Folgebewegung:

```text
Rand/Kipp wird kritisch, wenn Strain bleibt oder Rekopplung weiter faellt.
Rand/Kipp wird tragbar, wenn danach Rekopplung steigt und Strain faellt.
```

## Grenze

Diese Lupe nutzt Feldphasen-Segmente. Sie ist noch keine Kerzen-/OHLCV-Lupe auf Rohchart-Ebene.

## Wie es weitergeht

Als naechstes sollte die gleiche Lupe mit konkreten Rohweltfenstern gekoppelt werden: Phase, Kerzenbereich, Tonprofil, Rezeptorprofil und Feldfolge in einer Zeile.
