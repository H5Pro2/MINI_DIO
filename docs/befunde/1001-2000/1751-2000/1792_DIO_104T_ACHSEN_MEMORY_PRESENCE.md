# 1792 - `dio_104t` über Achsen-Memories

## Grundfrage

Die Prüfung liest, ob `dio_104t` nur in den rekoppelnden BTC/PAXG-Fenstern stark ist oder breiter in vorhandenen Achsen-Memories auftritt.

Die Diagnose bleibt passiv und verändert keine Laufmechanik.

## Kurzbefund

- geprüfte Memories: `395`
- aktive Memories mit `dio_104t`: `163`
- Quellenprofil: `btc:46; sonstige:32; doge:26; paxg:25; xrp:24; stress:3; sideways:3; expansion:3; synth:1`

## Stärkste Vorkommen

| Memory | Quelle | Count | Symbolcount | Dominante Achsen | Feldprofil |
|---|---|---:|---:|---|---|
| `axis_btc_2024_10k_self` | btc | 1316 | 1 | `mcm_kohaerenz:0.6136;sehen_form_salience:0.2365;hoeren_stimulation:0.1449;feldaufnahme_druck:0.0785` | `inner_effect_stable:0.7758;inner_effect_carried_unrest:0.2170;inner_effect_tipping:0.0064;inner_effect_strained:0.0008` |
| `REAL_DRIFT_2023_A` | sonstige | 1301 | 1 | `mcm_kohaerenz:0.6128;sehen_form_salience:0.2373;hoeren_stimulation:0.1441;feldaufnahme_druck:0.0785` | `inner_effect_stable:0.9884;inner_effect_carried_unrest:0.0116` |
| `REAL_DRIFT_2023_B` | sonstige | 1288 | 1 | `mcm_kohaerenz:0.6127;sehen_form_salience:0.2368;hoeren_stimulation:0.1452;feldaufnahme_druck:0.0788` | `inner_effect_stable:0.9895;inner_effect_carried_unrest:0.0105` |
| `REAL_DRIFT_2024_A` | sonstige | 1278 | 1 | `mcm_kohaerenz:0.6116;sehen_form_salience:0.2382;hoeren_stimulation:0.1436;feldaufnahme_druck:0.0781` | `inner_effect_stable:0.9926;inner_effect_carried_unrest:0.0074` |
| `REAL_DRIFT_2025_A` | sonstige | 1243 | 1 | `mcm_kohaerenz:0.6125;sehen_form_salience:0.2410;hoeren_stimulation:0.1445;feldaufnahme_druck:0.0785` | `inner_effect_stable:0.9922;inner_effect_carried_unrest:0.0078` |
| `axis_doge_2024_10k_self` | doge | 1186 | 1 | `mcm_kohaerenz:0.6109;sehen_form_salience:0.2425;hoeren_stimulation:0.1443;feldaufnahme_druck:0.0787` | `inner_effect_stable:0.7448;inner_effect_carried_unrest:0.2486;inner_effect_tipping:0.0063;inner_effect_strained:0.0003` |
| `REAL_DRIFT_DOGE_2024_A` | doge | 697 | 1 | `mcm_kohaerenz:0.6131;sehen_form_salience:0.2371;hoeren_stimulation:0.1444;feldaufnahme_druck:0.0786` | `inner_effect_stable:0.9893;inner_effect_carried_unrest:0.0107` |
| `REAL_DRIFT_DOGE_2025_A` | doge | 683 | 1 | `mcm_kohaerenz:0.6164;sehen_form_salience:0.2342;hoeren_stimulation:0.1440;feldaufnahme_druck:0.0780` | `inner_effect_stable:0.9898;inner_effect_carried_unrest:0.0102` |
| `axis_doge_2024_5000_halves` | doge | 671 | 1 | `mcm_kohaerenz:0.6125;sehen_form_salience:0.2383;hoeren_stimulation:0.1432;feldaufnahme_druck:0.0780` | `inner_effect_stable:0.7685;inner_effect_carried_unrest:0.2248;inner_effect_tipping:0.0065;inner_effect_strained:0.0002` |
| `REAL_DRIFT_XRP_2025_A` | xrp | 661 | 1 | `mcm_kohaerenz:0.6149;sehen_form_salience:0.2322;hoeren_stimulation:0.1429;feldaufnahme_druck:0.0779` | `inner_effect_stable:0.9890;inner_effect_carried_unrest:0.0110` |
| `axis_btc_2024_5000_halves` | btc | 660 | 1 | `mcm_kohaerenz:0.6130;sehen_form_salience:0.2344;hoeren_stimulation:0.1446;feldaufnahme_druck:0.0785` | `inner_effect_stable:0.7851;inner_effect_carried_unrest:0.2064;inner_effect_tipping:0.0075;inner_effect_strained:0.0009` |
| `REAL_DRIFT_XRP_2024_A` | xrp | 657 | 1 | `mcm_kohaerenz:0.6128;sehen_form_salience:0.2390;hoeren_stimulation:0.1449;feldaufnahme_druck:0.0788` | `inner_effect_stable:0.9861;inner_effect_carried_unrest:0.0139` |
| `axis_xrp_2024_5000_halves` | xrp | 524 | 1 | `mcm_kohaerenz:0.6129;sehen_form_salience:0.2363;hoeren_stimulation:0.1420;feldaufnahme_druck:0.0775` | `inner_effect_stable:0.7503;inner_effect_carried_unrest:0.2400;inner_effect_tipping:0.0092;inner_effect_strained:0.0005` |
| `axis_paxg_2024_5000_halves` | paxg | 515 | 1 | `mcm_kohaerenz:0.6030;sehen_form_salience:0.2300;hoeren_stimulation:0.1341;feldaufnahme_druck:0.0777` | `inner_effect_stable:0.8017;inner_effect_carried_unrest:0.1927;inner_effect_tipping:0.0053;inner_effect_strained:0.0003` |
| `axis_btc_2024_4000_a` | btc | 511 | 1 | `mcm_kohaerenz:0.6132;sehen_form_salience:0.2375;hoeren_stimulation:0.1428;feldaufnahme_druck:0.0780` | `inner_effect_stable:0.7710;inner_effect_carried_unrest:0.2208;inner_effect_tipping:0.0073;inner_effect_strained:0.0009` |
| `axis_doge_2024_4000_a` | doge | 403 | 1 | `mcm_kohaerenz:0.6117;sehen_form_salience:0.2437;hoeren_stimulation:0.1464;feldaufnahme_druck:0.0794` | `inner_effect_stable:0.7118;inner_effect_carried_unrest:0.2793;inner_effect_tipping:0.0088;inner_effect_strained:0.0001` |
| `axis_assets_doge_2024_6000_to_8000` | doge | 353 | 1 | `mcm_kohaerenz:0.6145;sehen_form_salience:0.2311;hoeren_stimulation:0.1442;feldaufnahme_druck:0.0785` | `inner_effect_stable:0.8681;inner_effect_carried_unrest:0.1256;inner_effect_tipping:0.0060;inner_effect_strained:0.0003` |
| `adaptive_stress_2000_to_4000` | stress | 340 | 1 | `mcm_kohaerenz:0.6147;sehen_form_salience:0.2364;hoeren_stimulation:0.1445;feldaufnahme_druck:0.0787` | `inner_effect_stable:0.8485;inner_effect_carried_unrest:0.1452;inner_effect_tipping:0.0060;inner_effect_strained:0.0003` |
| `multi_axis_stress_2000_to_4000` | stress | 340 | 1 | `mcm_kohaerenz:0.6147;sehen_form_salience:0.2364;hoeren_stimulation:0.1445;feldaufnahme_druck:0.0787` | `inner_effect_stable:0.8485;inner_effect_carried_unrest:0.1452;inner_effect_tipping:0.0060;inner_effect_strained:0.0003` |
| `multi_axis_stress_4000_to_6000` | stress | 316 | 1 | `mcm_kohaerenz:0.6115;sehen_form_salience:0.2382;hoeren_stimulation:0.1447;feldaufnahme_druck:0.0786` | `inner_effect_stable:0.8182;inner_effect_carried_unrest:0.1750;inner_effect_tipping:0.0065;inner_effect_strained:0.0003` |
| `adaptive_sideways_0_to_2000` | sideways | 306 | 1 | `mcm_kohaerenz:0.6144;sehen_form_salience:0.2329;hoeren_stimulation:0.1440;feldaufnahme_druck:0.0784` | `inner_effect_stable:0.8275;inner_effect_carried_unrest:0.1668;inner_effect_tipping:0.0055;inner_effect_strained:0.0003` |
| `multi_axis_sideways_0_to_2000` | sideways | 306 | 1 | `mcm_kohaerenz:0.6144;sehen_form_salience:0.2329;hoeren_stimulation:0.1440;feldaufnahme_druck:0.0784` | `inner_effect_stable:0.8275;inner_effect_carried_unrest:0.1668;inner_effect_tipping:0.0055;inner_effect_strained:0.0003` |
| `axis_assets_btc_2024_4000_to_6000` | btc | 303 | 1 | `mcm_kohaerenz:0.6120;sehen_form_salience:0.2335;hoeren_stimulation:0.1409;feldaufnahme_druck:0.0776` | `inner_effect_stable:0.8322;inner_effect_carried_unrest:0.1635;inner_effect_tipping:0.0043` |
| `axis_assets_doge_2024_4000_to_6000` | doge | 294 | 1 | `mcm_kohaerenz:0.6181;sehen_form_salience:0.2322;hoeren_stimulation:0.1438;feldaufnahme_druck:0.0777` | `inner_effect_stable:0.8004;inner_effect_carried_unrest:0.1926;inner_effect_tipping:0.0070` |
| `SYN_NULL_RANDOM_TO_SHUFFLE` | sonstige | 288 | 1 | `mcm_kohaerenz:0.6155;sehen_form_salience:0.2403;hoeren_stimulation:0.1424;feldaufnahme_druck:0.0760` | `inner_effect_stable:1.0000` |
| `SYN_NULL_SHUFFLE_TO_RANDOM` | sonstige | 288 | 1 | `mcm_kohaerenz:0.6089;sehen_form_salience:0.2430;hoeren_stimulation:0.1340;feldaufnahme_druck:0.0739` | `inner_effect_stable:1.0000` |
| `SYN_NULL_SHUFFLE_TO_RANDOM_SENS` | sonstige | 288 | 1 | `mcm_kohaerenz:0.6089;sehen_form_salience:0.2430;hoeren_stimulation:0.1340;feldaufnahme_druck:0.0739` | `inner_effect_stable:1.0000` |
| `axis_assets_xrp_2024_6000_to_8000` | xrp | 285 | 1 | `mcm_kohaerenz:0.6118;sehen_form_salience:0.2422;hoeren_stimulation:0.1436;feldaufnahme_druck:0.0784` | `inner_effect_stable:0.8187;inner_effect_carried_unrest:0.1723;inner_effect_tipping:0.0080;inner_effect_strained:0.0010` |
| `axis_assets_btc_2024_6000_to_8000` | btc | 281 | 1 | `mcm_kohaerenz:0.6131;sehen_form_salience:0.2328;hoeren_stimulation:0.1464;feldaufnahme_druck:0.0794` | `inner_effect_stable:0.8024;inner_effect_carried_unrest:0.1903;inner_effect_tipping:0.0070;inner_effect_strained:0.0003` |
| `axis_assets_btc_2024_2000_to_4000` | btc | 267 | 1 | `mcm_kohaerenz:0.6147;sehen_form_salience:0.2334;hoeren_stimulation:0.1421;feldaufnahme_druck:0.0775` | `inner_effect_stable:0.8054;inner_effect_carried_unrest:0.1873;inner_effect_tipping:0.0058;inner_effect_strained:0.0015` |

## Interpretation

`dio_104t` ist dann fachlich interessant, wenn es nicht nur häufig erscheint, sondern in verschiedenen Weltmilieus eine ähnliche Achsenmischung hält.

Wichtig bleibt:

```text
Familie allein ist kein Bedeutungsbeweis.
Erst Wiederkehr + Achsenprofil + Feldprofil + Nachbarschaft machen sie lesbar.
```
