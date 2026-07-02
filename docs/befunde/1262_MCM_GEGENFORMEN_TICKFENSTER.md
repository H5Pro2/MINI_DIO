# MCM Gegenformen Tickfenster

Stand: 2026-07-02

## Grundfrage

Welche konkreten Tickfenster zeigen, dass Bewegungsbruch nicht in Entlastung, sondern in Nachlast oder gebrochene Rekopplung geht?

## Unterpruefung

Diese Diagnose isoliert Gegenformen aus der erweiterten Rohwelt-Fensterlupe.

## Eingabe

- `docs\befunde\1257_MCM_FELDPHASEN_ROHWELT_FENSTERLUPE_ERWEITERT.csv`

## Profil

- markierte Gegenform-Fenster: `92`
- Gegenformarten: `{'schwache_entlastung_gebrochene_rekopplung': 61, 'aktive_nachlast': 14, 'rueckfall_nach_kurzer_rekopplung': 9, 'gemischte_gegenform': 7, 'last_bleibt': 1}`
- Fensterlesarten: `{'rekopplung_bricht_in_last': 61, 'gemischtes_fenster': 21, 'rekopplung_vor_neuer_last': 9, 'lastkontakt_bleibt': 1}`
- Welten: `{'XRP_5M_10K': 19, 'NEG_STRESS_10K': 15, 'DOGE_5M_10K': 13, 'POS_EXPANSION_10K': 13, 'PAXG_5M_10K': 12, 'SIDEWAYS_10K': 11, 'BTC_5M_2K': 3, 'BTC_1H_2K': 2, 'SOL_1H_2K': 2, 'SOL_5M_2K': 1, 'KAS_5M_2K': 1}`

## Dominante Phasen

- `zentrum_stabil->spannungsrand_kippnaehe->offene_variante`: `33`
- `spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe`: `22`
- `offene_variante->spannungsrand_kippnaehe->offene_variante`: `21`
- `rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante`: `8`
- `spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe`: `7`
- `spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe`: `1`

## Staerkste Gegenfenster

| Art | Lesart | Welt | Tick | Phase | Loudness | Strain | Delta Rekopplung | Delta Strain | Expansion | Richtung | Severity |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | XRP_5M_10K | 7274 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1742 | 0.1363 | -0.1482 | 0.1586 | 4.2718 | 0.0312 | 0.5102 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | NEG_STRESS_10K | 7850 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.2859 | 0.1432 | -0.1468 | 0.1532 | 3.1028 | 0.0690 | 0.5001 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | DOGE_5M_10K | 4479 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1792 | 0.1473 | -0.1396 | 0.1501 | 3.2104 | 0.0154 | 0.4845 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | XRP_5M_10K | 4068 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1462 | 0.1362 | -0.1322 | 0.1364 | 3.2663 | 0.0746 | 0.4529 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | DOGE_5M_10K | 4430 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1991 | 0.1366 | -0.1167 | 0.1226 | 8.4723 | 0.1642 | 0.4089 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | POS_EXPANSION_10K | 9730 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1898 | 0.1329 | -0.1075 | 0.1252 | 2.6512 | 0.0294 | 0.3990 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | POS_EXPANSION_10K | 5732 | spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 0.1723 | 0.1478 | -0.1091 | 0.1235 | 2.8796 | 0.0588 | 0.3989 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | POS_EXPANSION_10K | 6522 | spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe | 0.1820 | 0.1368 | -0.1045 | 0.1186 | 4.0291 | 0.0769 | 0.3846 |
| aktive_nachlast | gemischtes_fenster | PAXG_5M_10K | 9221 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1212 | 0.1434 | -0.0558 | 0.0398 | 4.4375 | 0.0909 | 0.1935 |
| rueckfall_nach_kurzer_rekopplung | rekopplung_vor_neuer_last | NEG_STRESS_10K | 4456 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1586 | 0.1330 | -0.0285 | 0.0426 | 2.5768 | 0.0154 | 0.1566 |
| aktive_nachlast | gemischtes_fenster | PAXG_5M_10K | 9538 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1661 | 0.1412 | -0.0265 | 0.0380 | 5.7126 | 0.1282 | 0.1467 |
| aktive_nachlast | gemischtes_fenster | POS_EXPANSION_10K | 8690 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2190 | 0.1339 | -0.0258 | 0.0344 | 2.8222 | 0.0286 | 0.1404 |
| aktive_nachlast | gemischtes_fenster | DOGE_5M_10K | 5350 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1234 | 0.1368 | -0.0186 | 0.0356 | 3.5119 | 0.0588 | 0.1313 |
| aktive_nachlast | gemischtes_fenster | POS_EXPANSION_10K | 9805 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2219 | 0.1389 | -0.0230 | 0.0301 | 3.2805 | 0.0769 | 0.1296 |
| aktive_nachlast | gemischtes_fenster | XRP_5M_10K | 8740 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1900 | 0.1400 | -0.0186 | 0.0274 | 2.5652 | 0.0606 | 0.1189 |
| aktive_nachlast | gemischtes_fenster | XRP_5M_10K | 4222 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2761 | 0.1497 | -0.0194 | 0.0192 | 2.9478 | 0.1642 | 0.1078 |
| aktive_nachlast | gemischtes_fenster | XRP_5M_10K | 8582 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1984 | 0.1430 | -0.0142 | 0.0241 | 3.2644 | 0.0000 | 0.1074 |
| aktive_nachlast | gemischtes_fenster | DOGE_5M_10K | 5426 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1759 | 0.1387 | -0.0228 | 0.0096 | 3.7507 | 0.0448 | 0.0986 |
| aktive_nachlast | gemischtes_fenster | DOGE_5M_10K | 6140 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2423 | 0.1411 | -0.0084 | 0.0208 | 3.3927 | 0.0435 | 0.0937 |
| aktive_nachlast | gemischtes_fenster | NEG_STRESS_10K | 6408 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2465 | 0.1382 | -0.0137 | 0.0144 | 2.4683 | 0.0508 | 0.0921 |
| aktive_nachlast | gemischtes_fenster | PAXG_5M_10K | 4109 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2674 | 0.1403 | -0.0085 | 0.0191 | 5.9167 | 0.0526 | 0.0914 |
| gemischte_gegenform | gemischtes_fenster | XRP_5M_10K | 1698 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.1451 | 0.1372 | -0.0211 | -0.0045 | 2.6073 | 0.1212 | 0.0794 |
| schwache_entlastung_gebrochene_rekopplung | rekopplung_bricht_in_last | PAXG_5M_10K | 2558 | zentrum_stabil->spannungsrand_kippnaehe->offene_variante | 0.6677 | 0.2706 | -0.0224 | -0.0214 | 3.3333 | 0.0196 | 0.0729 |
| aktive_nachlast | gemischtes_fenster | XRP_5M_10K | 6140 | spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 0.2909 | 0.1517 | -0.0055 | 0.0096 | 3.4836 | 0.0625 | 0.0726 |

## Befund

Die Gegenformen entstehen nicht aus einer anderen Rohweltklasse. Sie bleiben ueberwiegend `bewegungsbruch`.

Der Unterschied liegt in der Folge:

```text
Entlastung: Rekopplung steigt, Strain faellt.
Gegenform: Rekopplung steigt zu schwach, faellt, oder Strain steigt erneut.
```

## Wie es weitergeht

Als naechstes sollte diese Gegenform-Liste mit den direkten vorherigen Rollen gekoppelt werden, um zu sehen, ob bestimmte Vorrollen Nachlast beguenstigen.
