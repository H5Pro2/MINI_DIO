# 2034 - Feldfunktionswechsel Rohweltfenster-Lupe

## Zweck

Diese Diagnose betrachtet konkrete Rohweltfenster vor Feldfunktionswechseln.

Fokus:

- `active_recoupling -> open_surface`: wann rekoppelnde Signaturen öffnen
- `open_surface -> active_recoupling`: wann offene Oberflächen rekoppeln

Die Diagnose bleibt passiv. Sie beschreibt nur Rohwelt, Sinneswerte und MCM-Feldwerte um die Signaturen herum.

## Übersicht

- Rohfenster-Lookback: `96` Ticks
- untersuchte Ereignisse: `304`
- Gruppen: `rekopplung_oeffnet:178, oberflaeche_rekoppelt:80, oberflaeche_rekoppelt_spaet:46`
- Ketten: `long_btc_sol:175, multiasset:129`

## Gruppenzusammenfassung

| Gruppe | Kette | Ereignisse | Fenster | Richtung | Range | Wechsel | Sehen stabil/change | Hören Ton/Shift | MCM carry/strain/rekopplung |
|---|---|---:|---|---|---:|---:|---:|---:|---:|
| `oberflaeche_rekoppelt` | `long_btc_sol` | 41 | `weite_unruhige_fallend:23;weite_unruhige_steigend:18` | `fallend:23;steigend:18` | 6.4240 | 48.05 | 0.267/-0.046 | -0.163/0.330 | 0.410/0.231/0.616 |
| `oberflaeche_rekoppelt` | `multiasset` | 39 | `weite_unruhige_steigend:24;weite_unruhige_fallend:12;weite_gerichtete_fallend:2;weite_unruhige_seitwaerts:1` | `steigend:24;fallend:14;seitwaerts:1` | 6.1288 | 44.13 | 0.194/-0.194 | -0.043/0.253 | 0.425/0.210/0.633 |
| `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | 22 | `weite_unruhige_fallend:9;weite_unruhige_seitwaerts:7;weite_unruhige_steigend:6` | `fallend:9;seitwaerts:7;steigend:6` | 3.6619 | 47.05 | -0.001/-0.544 | 0.474/0.585 | 0.378/0.268/0.590 |
| `oberflaeche_rekoppelt_spaet` | `multiasset` | 24 | `weite_unruhige_fallend:12;weite_unruhige_steigend:6;enge_unruhige_seitwaerts:3;weite_unruhige_seitwaerts:2;enge_unruhige_fallend:1` | `fallend:13;steigend:6;seitwaerts:5` | 5.4713 | 43.33 | 0.059/-0.615 | 0.508/0.576 | 0.375/0.270/0.590 |
| `rekopplung_oeffnet` | `long_btc_sol` | 112 | `weite_unruhige_fallend:56;weite_unruhige_steigend:42;weite_unruhige_seitwaerts:12;enge_unruhige_steigend:1;enge_unruhige_seitwaerts:1` | `fallend:56;steigend:43;seitwaerts:13` | 3.3772 | 47.30 | 0.375/-0.465 | 0.728/0.675 | 0.370/0.286/0.581 |
| `rekopplung_oeffnet` | `multiasset` | 66 | `weite_unruhige_fallend:27;weite_unruhige_steigend:21;enge_unruhige_seitwaerts:8;weite_unruhige_seitwaerts:5;enge_unruhige_steigend:4;enge_unruhige_fallend:1` | `fallend:28;steigend:25;seitwaerts:13` | 4.5873 | 44.20 | 0.447/-0.442 | 0.726/0.677 | 0.367/0.287/0.581 |

## Einzelereignisse

| Signatur | Gruppe | Kette | Welt | Tick | Fenster | Richtung | Range | MCM |
|---|---|---|---|---:|---|---|---:|---:|
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 753 | `weite_unruhige_fallend` | `fallend` | 5.0052 | 0.375/0.271/0.585 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 1043 | `weite_unruhige_fallend` | `fallend` | 4.1648 | 0.388/0.252/0.599 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 1061 | `weite_unruhige_fallend` | `fallend` | 9.2427 | 0.379/0.269/0.586 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 1614 | `weite_unruhige_fallend` | `fallend` | 3.1283 | 0.387/0.255/0.592 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 1898 | `weite_unruhige_steigend` | `steigend` | 3.8998 | 0.379/0.272/0.586 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 2198 | `weite_unruhige_steigend` | `steigend` | 1.6648 | 0.381/0.265/0.592 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 2226 | `weite_unruhige_fallend` | `fallend` | 2.9245 | 0.390/0.253/0.600 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_34K_51K` | 2589 | `weite_unruhige_steigend` | `steigend` | 2.8859 | 0.391/0.254/0.599 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 2595 | `weite_unruhige_fallend` | `fallend` | 4.2777 | 0.388/0.261/0.596 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_34K_51K` | 2751 | `weite_unruhige_steigend` | `steigend` | 3.6909 | 0.383/0.262/0.587 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 2759 | `weite_unruhige_fallend` | `fallend` | 2.7417 | 0.379/0.268/0.588 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_34K_51K` | 2766 | `weite_unruhige_steigend` | `steigend` | 2.4504 | 0.381/0.270/0.588 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 4973 | `weite_unruhige_steigend` | `steigend` | 9.0084 | 0.384/0.255/0.599 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 5336 | `weite_unruhige_steigend` | `steigend` | 3.2902 | 0.384/0.268/0.590 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 5342 | `weite_unruhige_steigend` | `steigend` | 11.2506 | 0.378/0.265/0.588 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 5687 | `weite_unruhige_fallend` | `fallend` | 13.0375 | 0.377/0.269/0.585 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 9613 | `weite_unruhige_fallend` | `fallend` | 12.1509 | 0.376/0.273/0.585 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_34K_51K` | 15738 | `weite_unruhige_fallend` | `fallend` | 4.0508 | 0.385/0.256/0.595 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 15819 | `weite_unruhige_fallend` | `fallend` | 8.7309 | 0.390/0.262/0.593 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 15968 | `weite_unruhige_fallend` | `fallend` | 7.7290 | 0.383/0.271/0.587 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_34K_51K` | 16572 | `weite_unruhige_steigend` | `steigend` | 2.0056 | 0.396/0.251/0.601 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 454 | `weite_unruhige_fallend` | `fallend` | 1.7585 | 0.481/0.157/0.678 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 455 | `weite_unruhige_fallend` | `fallend` | 1.7535 | 0.461/0.192/0.651 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 467 | `weite_unruhige_steigend` | `steigend` | 2.0654 | 0.405/0.230/0.616 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 474 | `weite_unruhige_steigend` | `steigend` | 4.2084 | 0.438/0.171/0.657 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 474 | `weite_unruhige_steigend` | `steigend` | 17.8295 | 0.467/0.123/0.692 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 486 | `weite_unruhige_steigend` | `steigend` | 27.9173 | 0.388/0.254/0.597 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 790 | `weite_unruhige_fallend` | `fallend` | 8.7787 | 0.481/0.162/0.669 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 1726 | `weite_unruhige_fallend` | `fallend` | 5.0906 | 0.403/0.243/0.607 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 1726 | `weite_unruhige_fallend` | `fallend` | 6.3017 | 0.468/0.197/0.647 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 1727 | `weite_unruhige_fallend` | `fallend` | 5.2106 | 0.451/0.149/0.675 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_17K_34K` | 1728 | `weite_unruhige_fallend` | `fallend` | 5.2064 | 0.410/0.235/0.618 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_17K_34K` | 1975 | `weite_unruhige_fallend` | `fallend` | 6.6560 | 0.449/0.216/0.633 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 2157 | `weite_unruhige_fallend` | `fallend` | 2.1505 | 0.407/0.222/0.620 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_0_17K` | 2158 | `weite_unruhige_fallend` | `fallend` | 2.1876 | 0.535/0.203/0.684 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_BTC_34K_51K` | 3437 | `weite_unruhige_steigend` | `steigend` | 1.9153 | 0.417/0.203/0.629 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 4942 | `weite_unruhige_steigend` | `steigend` | 5.6914 | 0.424/0.189/0.644 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 5096 | `weite_unruhige_steigend` | `steigend` | 14.4991 | 0.414/0.222/0.620 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 5097 | `weite_unruhige_steigend` | `steigend` | 14.5229 | 0.448/0.161/0.665 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_0_17K` | 10032 | `weite_unruhige_steigend` | `steigend` | 5.2189 | 0.400/0.243/0.604 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `long_btc_sol` | `FPSIG_LONG_REAL_SOL_34K_51K` | 15701 | `weite_unruhige_fallend` | `fallend` | 7.0923 | 0.420/0.196/0.636 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 188 | `weite_unruhige_steigend` | `steigend` | 1.6666 | 0.390/0.250/0.596 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3363 | `weite_unruhige_steigend` | `steigend` | 2.0113 | 0.376/0.274/0.584 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3439 | `weite_unruhige_steigend` | `steigend` | 3.0537 | 0.385/0.262/0.588 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3487 | `weite_unruhige_steigend` | `steigend` | 3.3170 | 0.383/0.260/0.591 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 3743 | `weite_unruhige_steigend` | `steigend` | 18.3521 | 0.385/0.266/0.591 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 4231 | `weite_unruhige_steigend` | `steigend` | 1.2170 | 0.381/0.263/0.591 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_0_10K` | 4312 | `weite_unruhige_steigend` | `steigend` | 10.6412 | 0.385/0.256/0.595 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 4329 | `weite_unruhige_fallend` | `fallend` | 5.5934 | 0.395/0.252/0.603 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 5670 | `weite_unruhige_fallend` | `fallend` | 6.2141 | 0.390/0.255/0.601 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 9363 | `weite_unruhige_steigend` | `steigend` | 2.0113 | 0.376/0.274/0.585 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 9439 | `weite_unruhige_steigend` | `steigend` | 3.0537 | 0.385/0.262/0.589 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 9487 | `weite_unruhige_steigend` | `steigend` | 3.3170 | 0.382/0.260/0.591 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_0_10K` | 9690 | `weite_unruhige_steigend` | `steigend` | 13.2365 | 0.390/0.257/0.593 |
| `dio_mcm_episode_16yidit` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 9826 | `weite_unruhige_fallend` | `fallend` | 8.4177 | 0.389/0.260/0.597 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 19 | `weite_gerichtete_fallend` | `fallend` | 2.9030 | 0.423/0.190/0.647 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 20 | `weite_gerichtete_fallend` | `fallend` | 2.9030 | 0.431/0.188/0.647 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 296 | `weite_unruhige_steigend` | `steigend` | 6.2551 | 0.405/0.229/0.616 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 297 | `weite_unruhige_steigend` | `steigend` | 6.4479 | 0.546/0.179/0.700 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 324 | `weite_unruhige_steigend` | `steigend` | 5.1144 | 0.423/0.196/0.636 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 325 | `weite_unruhige_fallend` | `fallend` | 5.1082 | 0.445/0.154/0.668 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 326 | `weite_unruhige_fallend` | `fallend` | 5.1031 | 0.407/0.225/0.615 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 582 | `weite_unruhige_steigend` | `steigend` | 4.5522 | 0.482/0.166/0.668 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 2295 | `weite_unruhige_fallend` | `fallend` | 3.4052 | 0.452/0.146/0.677 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_6K_16K` | 2296 | `weite_unruhige_fallend` | `fallend` | 3.4900 | 0.477/0.193/0.658 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 2304 | `weite_unruhige_seitwaerts` | `seitwaerts` | 5.2041 | 0.458/0.141/0.679 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3420 | `weite_unruhige_steigend` | `steigend` | 2.7445 | 0.434/0.174/0.654 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3428 | `weite_unruhige_steigend` | `steigend` | 3.0494 | 0.418/0.212/0.627 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_6K_16K` | 3429 | `weite_unruhige_steigend` | `steigend` | 3.0537 | 0.408/0.211/0.625 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 3520 | `weite_unruhige_fallend` | `fallend` | 19.8930 | 0.453/0.142/0.677 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 3675 | `weite_unruhige_fallend` | `fallend` | 9.4426 | 0.440/0.169/0.657 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_6K_16K` | 3676 | `weite_unruhige_fallend` | `fallend` | 9.4032 | 0.449/0.152/0.671 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_0_10K` | 4170 | `weite_unruhige_fallend` | `fallend` | 6.4839 | 0.521/0.196/0.675 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_XRP_0_10K` | 4230 | `weite_unruhige_steigend` | `steigend` | 11.1783 | 0.504/0.144/0.692 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 5359 | `weite_unruhige_fallend` | `fallend` | 0.8899 | 0.425/0.201/0.637 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 5444 | `weite_unruhige_steigend` | `steigend` | 7.3054 | 0.446/0.153/0.671 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 5445 | `weite_unruhige_steigend` | `steigend` | 7.3151 | 0.484/0.150/0.683 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_DOGE_0_10K` | 5922 | `weite_unruhige_steigend` | `steigend` | 19.5709 | 0.424/0.203/0.643 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 9428 | `weite_unruhige_steigend` | `steigend` | 3.0494 | 0.418/0.212/0.627 |
| `dio_mcm_episode_1y7uo9c` | `oberflaeche_rekoppelt` | `multiasset` | `FPSIG_MULTI_REAL_PAXG_0_10K` | 9429 | `weite_unruhige_steigend` | `steigend` | 3.0537 | 0.408/0.211/0.626 |

## Lesung

Die Rollenwechsel erscheinen nicht als reiner Symbolwechsel.

Sie liegen in konkreten Rohweltfenstern mit unterscheidbaren Richtungs-, Wechsel- und Sinnesprofilen.

`open_surface -> active_recoupling` wird damit als mögliche Rekopplung offener Oberflächen lesbar. `active_recoupling -> open_surface` wirkt dagegen wie ein Öffnen zuvor rekoppelnder Signaturen unter anderer Weltspannung.

## Wie es weitergeht

Als nächstes sollte diese Lupe mit längeren Lookbacks und einem direkten Vergleich der Rohfensterklassen wiederholt werden. Entscheidend ist, ob Öffnung und Rekopplung schon vor dem Signaturauftreten unterschiedliche Weltprofile zeigen.
