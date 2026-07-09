# 1018 - Abverkauf/Rekopplung-Familie

Passive Familienlesung fuer Abverkauf, Bruch, Rekopplung und Nach-Abverkauf-Erholung.

## Kurzbefund

- Familienfenster gesamt: 15
- Modi: 3
- Phasenhinweise: 4

## Modi

| Modus | Anzahl | Welten | Bewegung | Phasenhinweise | Return % | Range % | Vorher % | Nachher % | Druck | Rekopplung |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| abverkauf_mit_rekopplung | 7 | LONG2024_5M_SOL_STRESS_4000:2 <br> LONG2025_15M_BTC_QUIET_4000:1 <br> LONG2025_15M_BTC_STRESS_4000:1 <br> LONG2025_15M_SOL_STRESS_4000:1 <br> LONG2025_5M_BTC_STRESS_4000:1 <br> LONG2025_SOL_STRESS_4000:1 | rekopplungs_uebergang:7 | fallende_rekopplung:7 | -16.343053 | 26.165717 | 0.287663 | -0.604939 | 0.051619 | 0.019111 |
| abverkauf_mit_bruch | 4 | SOL_2024_30M:2 <br> LONG2025_15M_SOL_STRESS_4000:1 <br> LONG2025_5M_SOL_STRESS_4000:1 | offene_uebergangszone:2 <br> bewegungsbruch_zone:2 | offenes_familienfenster:2 <br> fallender_bruch:2 | -15.55323 | 21.204778 | -0.346737 | -2.108212 | 0.063828 | 0.019154 |
| rekopplung_nach_abverkauf | 4 | BTC_2024_1H:2 <br> KAS2024_1H_ASSET_PROBE:2 | druck_uebergang:1 <br> offene_uebergangszone:1 <br> bewegungsbruch_zone:1 <br> rekopplungs_uebergang:1 | erholung_nach_abverkauf:4 | 59.870493 | 91.03631 | -4.787495 | -1.875831 | 0.091296 | 0.02023 |

## Phasenhinweise

| Phase | Anzahl | Modi | Return % | Range % | Vorher % | Nachher % | Druck | Rekopplung |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| fallende_rekopplung | 7 | abverkauf_mit_rekopplung:7 | -16.343053 | 26.165717 | 0.287663 | -0.604939 | 0.051619 | 0.019111 |
| erholung_nach_abverkauf | 4 | rekopplung_nach_abverkauf:4 | 59.870493 | 91.03631 | -4.787495 | -1.875831 | 0.091296 | 0.02023 |
| fallender_bruch | 2 | abverkauf_mit_bruch:2 | -26.952207 | 36.754031 | -0.232524 | -4.59471 | 0.064318 | 0.021888 |
| offenes_familienfenster | 2 | abverkauf_mit_bruch:2 | -4.154253 | 5.655525 | -0.46095 | 0.378286 | 0.063338 | 0.01642 |

## Einzelzuordnung

| Modus | Phase | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Return % | Range % |
|---|---|---|---|---|---|---|---|---:|---:|
| abverkauf_mit_bruch | fallender_bruch | LONG_ISOLATION | LONG2025_15M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 134-3979 | `abverkauf_getragen` | `bewegungsbruch_zone` | -36.805556 | 42.974387 |
| abverkauf_mit_bruch | fallender_bruch | LONG_ISOLATION | LONG2025_5M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 473-3976 | `abverkauf_getragen` | `bewegungsbruch_zone` | -17.098858 | 30.533676 |
| abverkauf_mit_bruch | offenes_familienfenster | ASSET_ZEIT | SOL_2024_30M | `183drjy->1t5bcxp` | 1603-1721 | `abverkauf_getragen` | `offene_uebergangszone` | -3.229713 | 5.308841 |
| abverkauf_mit_bruch | offenes_familienfenster | ASSET_ZEIT | SOL_2024_30M | `1t5bcxp->183drjy` | 1594-1724 | `abverkauf_getragen` | `offene_uebergangszone` | -5.078792 | 6.002208 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2024_5M_SOL_STRESS_4000 | `183drjy->1t5bcxp` | 2406-3426 | `abverkauf_getragen` | `rekopplungs_uebergang` | -9.208984 | 15.273437 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2024_5M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 2404-3477 | `abverkauf_getragen` | `rekopplungs_uebergang` | -10.795233 | 19.851504 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2025_15M_BTC_QUIET_4000 | `1t5bcxp->183drjy` | 723-3816 | `abverkauf_getragen` | `rekopplungs_uebergang` | -3.810866 | 10.623678 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2025_15M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 894-3647 | `abverkauf_getragen` | `rekopplungs_uebergang` | -10.193232 | 22.125853 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2025_15M_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 132-3955 | `abverkauf_getragen` | `rekopplungs_uebergang` | -36.414755 | 42.869996 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2025_5M_BTC_STRESS_4000 | `1t5bcxp->183drjy` | 2125-3952 | `abverkauf_getragen` | `rekopplungs_uebergang` | -6.169117 | 10.763185 |
| abverkauf_mit_rekopplung | fallende_rekopplung | LONG_ISOLATION | LONG2025_SOL_STRESS_4000 | `1t5bcxp->183drjy` | 322-2431 | `abverkauf_getragen` | `rekopplungs_uebergang` | -37.809187 | 61.652364 |
| rekopplung_nach_abverkauf | erholung_nach_abverkauf | ASSET_ZEIT | BTC_2024_1H | `183drjy->1t5bcxp` | 446-1767 | `rekopplung_nach_abverkauf` | `druck_uebergang` | 71.149405 | 85.091518 |
| rekopplung_nach_abverkauf | erholung_nach_abverkauf | ASSET_ZEIT | BTC_2024_1H | `1t5bcxp->183drjy` | 442-1766 | `rekopplung_nach_abverkauf` | `offene_uebergangszone` | 73.171069 | 85.080644 |
| rekopplung_nach_abverkauf | erholung_nach_abverkauf | KAS_GEGENPROBE | KAS2024_1H_ASSET_PROBE | `183drjy->1t5bcxp` | 447-1665 | `rekopplung_nach_abverkauf` | `bewegungsbruch_zone` | 48.426102 | 97.841511 |
| rekopplung_nach_abverkauf | erholung_nach_abverkauf | KAS_GEGENPROBE | KAS2024_1H_ASSET_PROBE | `1t5bcxp->183drjy` | 444-1656 | `rekopplung_nach_abverkauf` | `rekopplungs_uebergang` | 46.735395 | 96.131566 |

## Interpretation

Die Familie zerfaellt in drei lesbare Formen: fallender Bruch, fallende Rekopplung und Erholung nach vorherigem Abverkauf.

`abverkauf_mit_rekopplung` ist derzeit die stabilere Familie als `rekopplung_nach_abverkauf`. Letztere wirkt eher wie eine grossraeumige Erholungsform nach vorherigem Druck.

Fachlich bedeutet das: Das MCM-Feld liest nicht nur Preisrichtung. Es unterscheidet, ob ein fallendes Fenster bricht, rekoppelt oder nach vorheriger Belastung wieder Anschluss findet.

## Wie es weitergeht

Als naechstes sollte die Familie `abverkauf + rekopplung` gegen lokale Weltmerkmale gelesen werden: Lautstaerke/Energie, Rezeptorlast, Druckwechsel und Topologie-Rolle im gleichen Tickfenster.
