# 2039 - Feldfunktionswechsel Vorphasen nach Asset

## Zweck

Diese Diagnose prüft, ob die Vorphasen-Klassen aus `2038` assetübergreifend stabil bleiben oder ob einzelne Weltkörper eigene Vorphasenprofile ausbilden.

## Übersicht

- Asset-Gruppen: `BTC:9, SOL:9, DOGE:9, PAXG:9, XRP:9`

## Asset-Stabilität

| Lookback | Gruppe | Kette | Assets | Feldkontakt | Sinnesphase | Rohphase | MCM carry/strain/rekopplung |
|---|---|---|---|---|---|---|---:|
| `lb144` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_wechselnd_mittel` (1.00) | `weite_unruhige_vorphase_fallend` (0.50) | 0.411/0.231/0.616 |
| `lb144` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE;PAXG;XRP` | `tragende_rekopplung` (0.67) | `sicht_zerfaellt_gedaempft_leise` (0.33) | `weite_unruhige_vorphase_steigend` (0.67) | 0.425/0.210/0.632 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.378/0.268/0.590 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE;PAXG;XRP` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.67) | 0.374/0.270/0.589 |
| `lb144` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC;SOL` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_steigend` (0.50) | 0.370/0.286/0.581 |
| `lb144` | `rekopplung_oeffnet` | `multiasset` | `DOGE;PAXG;XRP` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_steigend` (0.67) | 0.367/0.286/0.581 |
| `lb48` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_wechselnd_mittel` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.411/0.231/0.616 |
| `lb48` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE;PAXG;XRP` | `tragende_rekopplung` (0.67) | `sicht_zerfaellt_gedaempft_leise` (0.33) | `weite_unruhige_vorphase_steigend` (0.33) | 0.425/0.210/0.632 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.378/0.268/0.590 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE;PAXG;XRP` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.67) | 0.374/0.270/0.589 |
| `lb48` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC;SOL` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.370/0.286/0.581 |
| `lb48` | `rekopplung_oeffnet` | `multiasset` | `DOGE;PAXG;XRP` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.67) | 0.367/0.286/0.581 |
| `lb96` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_wechselnd_mittel` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.411/0.231/0.616 |
| `lb96` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE;PAXG;XRP` | `tragende_rekopplung` (0.67) | `sicht_zerfaellt_gedaempft_leise` (0.33) | `weite_unruhige_vorphase_steigend` (0.33) | 0.425/0.210/0.632 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC;SOL` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_fallend` (0.50) | 0.378/0.268/0.590 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE;PAXG;XRP` | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.33) | 0.374/0.270/0.589 |
| `lb96` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC;SOL` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `enge_unruhige_vorphase_steigend` (0.50) | 0.370/0.286/0.581 |
| `lb96` | `rekopplung_oeffnet` | `multiasset` | `DOGE;PAXG;XRP` | `spannungsnahe_oeffnung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.67) | 0.367/0.286/0.581 |

## Asset-Details

| Lookback | Gruppe | Kette | Asset | Ereignisse | Feldkontakt | Sinnesphase | Rohphase | MCM |
|---|---|---|---|---:|---|---|---|---:|
| `lb144` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC` | 19 | `offene_rekopplung` (0.68) | `sicht_zerfaellt_wechselnd_mittel` (0.26) | `weite_unruhige_vorphase_fallend` (0.42) | 0.414/0.229/0.619 |
| `lb144` | `oberflaeche_rekoppelt` | `long_btc_sol` | `SOL` | 22 | `offene_rekopplung` (0.64) | `sicht_zerfaellt_wechselnd_mittel` (0.18) | `weite_unruhige_vorphase_steigend` (0.50) | 0.407/0.233/0.613 |
| `lb144` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE` | 16 | `tragende_rekopplung` (0.69) | `sicht_zerfaellt_gedaempft_leise` (0.19) | `weite_unruhige_vorphase_steigend` (0.50) | 0.438/0.197/0.645 |
| `lb144` | `oberflaeche_rekoppelt` | `multiasset` | `PAXG` | 13 | `offene_rekopplung` (0.54) | `sicht_zerfaellt_wechselnd_mittel` (0.23) | `enge_unruhige_vorphase_steigend` (0.77) | 0.398/0.237/0.609 |
| `lb144` | `oberflaeche_rekoppelt` | `multiasset` | `XRP` | 10 | `tragende_rekopplung` (0.60) | `sicht_stabil_gedaempft_leise` (0.30) | `weite_unruhige_vorphase_steigend` (0.60) | 0.438/0.197/0.643 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC` | 13 | `offene_rekopplung` (0.92) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `enge_unruhige_vorphase_fallend` (0.38) | 0.378/0.269/0.590 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `SOL` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.33) | `weite_unruhige_vorphase_steigend` (0.56) | 0.378/0.266/0.590 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE` | 5 | `offene_rekopplung` (0.60) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.80) | 0.371/0.275/0.585 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `PAXG` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.44) | `enge_unruhige_vorphase_fallend` (0.44) | 0.375/0.268/0.593 |
| `lb144` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `XRP` | 10 | `offene_rekopplung` (0.80) | `sicht_zerfaellt_hoch_schwingend_laut` (0.40) | `weite_unruhige_vorphase_fallend` (0.50) | 0.376/0.268/0.589 |
| `lb144` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC` | 63 | `spannungsnahe_oeffnung` (0.67) | `sicht_zerfaellt_hoch_schwingend_laut` (0.63) | `enge_unruhige_vorphase_steigend` (0.33) | 0.370/0.287/0.582 |
| `lb144` | `rekopplung_oeffnet` | `long_btc_sol` | `SOL` | 49 | `spannungsnahe_oeffnung` (0.71) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `weite_unruhige_vorphase_steigend` (0.29) | 0.370/0.285/0.581 |
| `lb144` | `rekopplung_oeffnet` | `multiasset` | `DOGE` | 26 | `spannungsnahe_oeffnung` (0.77) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `weite_unruhige_vorphase_steigend` (0.38) | 0.371/0.287/0.582 |
| `lb144` | `rekopplung_oeffnet` | `multiasset` | `PAXG` | 19 | `spannungsnahe_oeffnung` (0.68) | `sicht_zerfaellt_hoch_schwingend_laut` (0.84) | `enge_unruhige_vorphase_steigend` (0.47) | 0.364/0.285/0.582 |
| `lb144` | `rekopplung_oeffnet` | `multiasset` | `XRP` | 21 | `spannungsnahe_oeffnung` (0.81) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `weite_unruhige_vorphase_steigend` (0.52) | 0.365/0.287/0.579 |
| `lb48` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC` | 19 | `offene_rekopplung` (0.68) | `sicht_zerfaellt_wechselnd_mittel` (0.26) | `enge_unruhige_vorphase_fallend` (0.47) | 0.414/0.229/0.619 |
| `lb48` | `oberflaeche_rekoppelt` | `long_btc_sol` | `SOL` | 22 | `offene_rekopplung` (0.64) | `sicht_zerfaellt_wechselnd_mittel` (0.18) | `weite_unruhige_vorphase_steigend` (0.32) | 0.407/0.233/0.613 |
| `lb48` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE` | 16 | `tragende_rekopplung` (0.69) | `sicht_zerfaellt_gedaempft_leise` (0.19) | `weite_unruhige_vorphase_steigend` (0.44) | 0.438/0.197/0.645 |
| `lb48` | `oberflaeche_rekoppelt` | `multiasset` | `PAXG` | 13 | `offene_rekopplung` (0.54) | `sicht_zerfaellt_wechselnd_mittel` (0.23) | `enge_unruhige_vorphase_steigend` (0.92) | 0.398/0.237/0.609 |
| `lb48` | `oberflaeche_rekoppelt` | `multiasset` | `XRP` | 10 | `tragende_rekopplung` (0.60) | `sicht_stabil_gedaempft_leise` (0.30) | `weite_unruhige_vorphase_fallend` (0.40) | 0.438/0.197/0.643 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC` | 13 | `offene_rekopplung` (0.92) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `enge_unruhige_vorphase_fallend` (0.38) | 0.378/0.269/0.590 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `SOL` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.33) | `enge_unruhige_vorphase_steigend` (0.44) | 0.378/0.266/0.590 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE` | 5 | `offene_rekopplung` (0.60) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.60) | 0.371/0.275/0.585 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `PAXG` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.44) | `mittlere_vorphase_seitwaerts` (0.33) | 0.375/0.268/0.593 |
| `lb48` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `XRP` | 10 | `offene_rekopplung` (0.80) | `sicht_zerfaellt_hoch_schwingend_laut` (0.40) | `weite_unruhige_vorphase_fallend` (0.50) | 0.376/0.268/0.589 |
| `lb48` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC` | 63 | `spannungsnahe_oeffnung` (0.67) | `sicht_zerfaellt_hoch_schwingend_laut` (0.63) | `enge_unruhige_vorphase_fallend` (0.32) | 0.370/0.287/0.582 |
| `lb48` | `rekopplung_oeffnet` | `long_btc_sol` | `SOL` | 49 | `spannungsnahe_oeffnung` (0.71) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `enge_unruhige_vorphase_steigend` (0.31) | 0.370/0.285/0.581 |
| `lb48` | `rekopplung_oeffnet` | `multiasset` | `DOGE` | 26 | `spannungsnahe_oeffnung` (0.77) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `weite_unruhige_vorphase_fallend` (0.27) | 0.371/0.287/0.582 |
| `lb48` | `rekopplung_oeffnet` | `multiasset` | `PAXG` | 19 | `spannungsnahe_oeffnung` (0.68) | `sicht_zerfaellt_hoch_schwingend_laut` (0.84) | `mittlere_vorphase_seitwaerts` (0.26) | 0.364/0.285/0.582 |
| `lb48` | `rekopplung_oeffnet` | `multiasset` | `XRP` | 21 | `spannungsnahe_oeffnung` (0.81) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `weite_unruhige_vorphase_fallend` (0.48) | 0.365/0.287/0.579 |
| `lb96` | `oberflaeche_rekoppelt` | `long_btc_sol` | `BTC` | 19 | `offene_rekopplung` (0.68) | `sicht_zerfaellt_wechselnd_mittel` (0.26) | `enge_unruhige_vorphase_fallend` (0.37) | 0.414/0.229/0.619 |
| `lb96` | `oberflaeche_rekoppelt` | `long_btc_sol` | `SOL` | 22 | `offene_rekopplung` (0.64) | `sicht_zerfaellt_wechselnd_mittel` (0.18) | `weite_unruhige_vorphase_fallend` (0.41) | 0.407/0.233/0.613 |
| `lb96` | `oberflaeche_rekoppelt` | `multiasset` | `DOGE` | 16 | `tragende_rekopplung` (0.69) | `sicht_zerfaellt_gedaempft_leise` (0.19) | `weite_unruhige_vorphase_steigend` (0.50) | 0.438/0.197/0.645 |
| `lb96` | `oberflaeche_rekoppelt` | `multiasset` | `PAXG` | 13 | `offene_rekopplung` (0.54) | `sicht_zerfaellt_wechselnd_mittel` (0.23) | `enge_unruhige_vorphase_steigend` (0.92) | 0.398/0.237/0.609 |
| `lb96` | `oberflaeche_rekoppelt` | `multiasset` | `XRP` | 10 | `tragende_rekopplung` (0.60) | `sicht_stabil_gedaempft_leise` (0.30) | `weite_unruhige_vorphase_fallend` (0.50) | 0.438/0.197/0.643 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `BTC` | 13 | `offene_rekopplung` (0.92) | `sicht_zerfaellt_hoch_schwingend_laut` (0.62) | `enge_unruhige_vorphase_fallend` (0.46) | 0.378/0.269/0.590 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `SOL` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.33) | `weite_unruhige_vorphase_fallend` (0.22) | 0.378/0.266/0.590 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `DOGE` | 5 | `offene_rekopplung` (0.60) | `sicht_zerfaellt_hoch_schwingend_laut` (1.00) | `weite_unruhige_vorphase_fallend` (0.60) | 0.371/0.275/0.585 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `PAXG` | 9 | `offene_rekopplung` (1.00) | `sicht_zerfaellt_hoch_schwingend_laut` (0.44) | `enge_unruhige_vorphase_seitwaerts` (0.56) | 0.375/0.268/0.593 |
| `lb96` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `XRP` | 10 | `offene_rekopplung` (0.80) | `sicht_zerfaellt_hoch_schwingend_laut` (0.40) | `weite_unruhige_vorphase_steigend` (0.50) | 0.376/0.268/0.589 |
| `lb96` | `rekopplung_oeffnet` | `long_btc_sol` | `BTC` | 63 | `spannungsnahe_oeffnung` (0.67) | `sicht_zerfaellt_hoch_schwingend_laut` (0.63) | `enge_unruhige_vorphase_steigend` (0.37) | 0.370/0.287/0.582 |
| `lb96` | `rekopplung_oeffnet` | `long_btc_sol` | `SOL` | 49 | `spannungsnahe_oeffnung` (0.71) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `enge_unruhige_vorphase_fallend` (0.33) | 0.370/0.285/0.581 |
| `lb96` | `rekopplung_oeffnet` | `multiasset` | `DOGE` | 26 | `spannungsnahe_oeffnung` (0.77) | `sicht_zerfaellt_hoch_schwingend_laut` (0.50) | `weite_unruhige_vorphase_fallend` (0.38) | 0.371/0.287/0.582 |
| `lb96` | `rekopplung_oeffnet` | `multiasset` | `PAXG` | 19 | `spannungsnahe_oeffnung` (0.68) | `sicht_zerfaellt_hoch_schwingend_laut` (0.84) | `enge_unruhige_vorphase_seitwaerts` (0.42) | 0.364/0.285/0.582 |
| `lb96` | `rekopplung_oeffnet` | `multiasset` | `XRP` | 21 | `spannungsnahe_oeffnung` (0.81) | `sicht_zerfaellt_hoch_schwingend_laut` (0.57) | `weite_unruhige_vorphase_fallend` (0.33) | 0.365/0.287/0.579 |

## Lesung

Der Feldkontakt ist stabiler als die Rohbewegung.

Rohphasen wechseln je nach Asset und Segment deutlicher. Der MCM-Feldkontakt bleibt innerhalb der Rollenfamilie konsistenter: Rekopplung bleibt rekoppelnd, Öffnung bleibt spannungsnah.

Das spricht dafür, dass MINI_DIO nicht nur assetbezogene Oberflächen liest, sondern darunter eine wiederkehrende Feldrolle hält.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese assetübergreifenden Feldkontaktklassen als passive Vorwahrnehmungs-Memory gespeichert werden können, ohne daraus Handlung oder harte Regeln abzuleiten.
