# 1021 - Bull/Selloff gegen Topologie-Rollen

Passive Gegenlesung der Bull-/Abverkauf-Familien gegen vorhandene MCM-Topologie-Rollen.

## Sicherheitsgrenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie
- keine nachtraegliche Topologie-Vorgabe

## Rollenverdichtung

| Seite | Modus | Count | Return % | Range % | Druck | Rekopplung | Topologie-Lesung | Achsen | Knotenstatus |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| bull | `gerichtete_bewegung_mit_bruch` | 4 | -7.005688 | 27.087858 | 0.063247 | 0.018472 | `zeitachse_mit_angrenzender_rollenbewegung:4` | `183drjy<->1t5bcxp:4` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:4` |
| bull | `gerichtete_bewegung_mit_rekopplung` | 4 | 4.737651 | 12.69461 | 0.052582 | 0.019147 | `zeitachse_mit_angrenzender_rollenbewegung:4` | `183drjy<->1t5bcxp:4` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:4` |
| bull | `getragene_expansion` | 8 | 29.146646 | 40.035995 | 0.074675 | 0.021062 | `zeitachse_mit_angrenzender_rollenbewegung:8` | `183drjy<->1t5bcxp:8` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:8` |
| selloff | `abverkauf_mit_bruch` | 4 | -15.55323 | 21.204778 | 0.063828 | 0.019154 | `zeitachse_mit_angrenzender_rollenbewegung:4` | `183drjy<->1t5bcxp:4` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:4` |
| selloff | `abverkauf_mit_rekopplung` | 7 | -16.343053 | 26.165717 | 0.051619 | 0.019111 | `zeitachse_mit_angrenzender_rollenbewegung:7` | `183drjy<->1t5bcxp:7` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:7` |
| selloff | `rekopplung_nach_abverkauf` | 4 | 59.870493 | 91.03631 | 0.091296 | 0.02023 | `zeitachse_mit_angrenzender_rollenbewegung:4` | `183drjy<->1t5bcxp:4` | `nichtbruecke_rekopplungsfeld<->nichtbruecke_zentrum_schwach:4` |

## Einzelbelege

| Seite | Modus | Welt | Paar | Phase | Bewegung | Return % | Topologie | Knotenrollen |
|---|---|---|---|---|---|---:|---|---|
| bull | `gerichtete_bewegung_mit_bruch` | `LONG2024_15M_SOL_QUIET_4000` | `183drjy->1t5bcxp` | `steigender_bruch` | `bewegungsbruch_zone` | 20.07336 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_bruch` | `LONG2024_5M_BTC_QUIET_4000` | `183drjy->1t5bcxp` | `offenes_bull_fenster` | `bewegungsbruch_zone` | 1.115271 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_bruch` | `LONG2025_5M_BTC_STRESS_4000` | `183drjy->1t5bcxp` | `offenes_bull_fenster` | `bewegungsbruch_zone` | -5.889823 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_bruch` | `LONG2025_SOL_STRESS_4000` | `183drjy->1t5bcxp` | `offenes_bull_fenster` | `bewegungsbruch_zone` | -43.321558 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_rekopplung` | `LONG2024_15M_SOL_QUIET_4000` | `1t5bcxp->183drjy` | `steigende_rekopplung` | `rekopplungs_uebergang` | 19.822883 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_rekopplung` | `LONG2025_15M_BTC_QUIET_4000` | `183drjy->1t5bcxp` | `offenes_bull_fenster` | `rekopplungs_uebergang` | -4.169846 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_rekopplung` | `LONG2025_5M_BTC_QUIET_4000` | `183drjy->1t5bcxp` | `offenes_bull_fenster` | `rekopplungs_uebergang` | 1.593614 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `gerichtete_bewegung_mit_rekopplung` | `LONG2025_5M_BTC_QUIET_4000` | `1t5bcxp->183drjy` | `offenes_bull_fenster` | `rekopplungs_uebergang` | 1.703952 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `KAS_2024_30M` | `183drjy->1t5bcxp` | `steigende_expansion_mit_bruch` | `bewegungsbruch_zone` | 33.575069 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `LONG2024_15M_BTC_STRESS_4000` | `183drjy->1t5bcxp` | `getragene_expansion` | `druck_uebergang` | 30.262088 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `LONG2024_15M_BTC_STRESS_4000` | `1t5bcxp->183drjy` | `steigende_rekopplung_getragen` | `rekopplungs_uebergang` | 31.706961 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `LONG2024_15M_SOL_STRESS_4000` | `1t5bcxp->183drjy` | `steigende_rekopplung_getragen` | `rekopplungs_uebergang` | 13.901137 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `LONG2025_BTC_STRESS_4000` | `183drjy->1t5bcxp` | `steigende_expansion_mit_bruch` | `bewegungsbruch_zone` | 18.94883 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `LONG2025_BTC_STRESS_4000` | `1t5bcxp->183drjy` | `steigende_rekopplung_getragen` | `rekopplungs_uebergang` | 25.458857 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `SOL_2024_1H` | `183drjy->1t5bcxp` | `getragene_expansion` | `offene_uebergangszone` | 40.518749 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| bull | `getragene_expansion` | `SOL_2024_1H` | `1t5bcxp->183drjy` | `getragene_expansion` | `offene_uebergangszone` | 38.801476 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_bruch` | `LONG2025_15M_SOL_STRESS_4000` | `183drjy->1t5bcxp` | `fallender_bruch` | `bewegungsbruch_zone` | -36.805556 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_bruch` | `LONG2025_5M_SOL_STRESS_4000` | `183drjy->1t5bcxp` | `fallender_bruch` | `bewegungsbruch_zone` | -17.098858 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_bruch` | `SOL_2024_30M` | `183drjy->1t5bcxp` | `offenes_familienfenster` | `offene_uebergangszone` | -3.229713 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_bruch` | `SOL_2024_30M` | `1t5bcxp->183drjy` | `offenes_familienfenster` | `offene_uebergangszone` | -5.078792 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2024_5M_SOL_STRESS_4000` | `183drjy->1t5bcxp` | `fallende_rekopplung` | `rekopplungs_uebergang` | -9.208984 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2024_5M_SOL_STRESS_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -10.795233 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2025_15M_BTC_QUIET_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -3.810866 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2025_15M_BTC_STRESS_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -10.193232 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2025_15M_SOL_STRESS_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -36.414755 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2025_5M_BTC_STRESS_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -6.169117 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `abverkauf_mit_rekopplung` | `LONG2025_SOL_STRESS_4000` | `1t5bcxp->183drjy` | `fallende_rekopplung` | `rekopplungs_uebergang` | -37.809187 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `rekopplung_nach_abverkauf` | `BTC_2024_1H` | `183drjy->1t5bcxp` | `erholung_nach_abverkauf` | `druck_uebergang` | 71.149405 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `rekopplung_nach_abverkauf` | `BTC_2024_1H` | `1t5bcxp->183drjy` | `erholung_nach_abverkauf` | `offene_uebergangszone` | 73.171069 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `rekopplung_nach_abverkauf` | `KAS2024_1H_ASSET_PROBE` | `183drjy->1t5bcxp` | `erholung_nach_abverkauf` | `bewegungsbruch_zone` | 48.426102 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |
| selloff | `rekopplung_nach_abverkauf` | `KAS2024_1H_ASSET_PROBE` | `1t5bcxp->183drjy` | `erholung_nach_abverkauf` | `rekopplungs_uebergang` | 46.735395 | `zeitachse_mit_angrenzender_rollenbewegung` | `zentrum_stabil / zentrum_stabil` |

## Befund

- Bull-Modi: 3
- Selloff-Modi: 3
- Gemeinsame Achsen: `183drjy<->1t5bcxp`
- Nur Bull-Achsen: `-`
- Nur Selloff-Achsen: `-`

Die gleiche oder aehnliche Achse kann unterschiedliche Bewegungsqualitaeten tragen.
Damit wirkt die Topologie nicht als starres Richtungsschema, sondern als Feldort,
an dem Bewegung je nach Weltphase anders gelesen wird.

## Schluss

Bull-/Selloff-Asymmetrie liegt nicht nur in der Rohbewegung, sondern in der Kombination aus Achse,
Rollennaehe, Rekopplung, Druck und vorheriger Last. Das passt zur bisherigen Lesung:
MCM-Feldrollen sind Bedeutungsorte, keine fixen Handelsrichtungen.

## Wie es weitergeht

Als naechstes sollte eine einzelne gemeinsame Achse isoliert werden: Wann liest sie Bull-Fortsetzung, wann Selloff-Rekopplung, und welche Weltmerkmale kippen die Rollenqualitaet?
