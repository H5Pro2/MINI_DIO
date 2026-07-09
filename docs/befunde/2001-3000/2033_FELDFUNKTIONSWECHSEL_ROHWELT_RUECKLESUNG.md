# 2033 - Feldfunktionswechsel Rohwelt-Rücklesung

## Zweck

Diese Diagnose liest die Feldfunktionswechsel aus `2032` zurück in die tragenden Weltkörper.

Sie prüft passiv, ob eine gleiche Feldsignatur ihre Rolle abhängig von Asset, Segment oder Weltkörper verschiebt.

## Übersicht

- untersuchte Feldfunktionswechsel: `11`

### Rollenlesung

- `lange_btc_sol_welt_verdichtet_kurz_zu_milieu`: `2`
- `offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd`: `2`
- `lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche`: `2`
- `weltkoerper_wechsel_schiebt_zwischen_milieu_und_rekopplung`: `1`
- `breitere_realwelt_rekoppelt_fruehes_milieu_aktiv`: `1`
- `multiasset_welt_rekoppelt_offene_oberflaeche`: `1`
- `multiasset_welt_aktiviert_milieunahe_phase`: `1`
- `multiasset_welt_bindet_rekopplung_zu_milieu`: `1`

### Feldfunktionspfade

- `active_recoupling -> milieu_island -> active_recoupling`: `2`
- `open_surface -> active_recoupling -> active_recoupling`: `2`
- `active_recoupling -> open_surface -> open_surface`: `2`
- `milieu_island -> active_recoupling -> milieu_island`: `1`
- `milieu_island -> active_recoupling -> active_recoupling`: `1`
- `open_surface -> open_surface -> active_recoupling`: `1`
- `milieu_island -> milieu_island -> active_recoupling`: `1`
- `active_recoupling -> active_recoupling -> milieu_island`: `1`

### Top-Asset-Pfade

- `DOGE -> BTC -> DOGE`: `3`
- `SOL -> BTC -> DOGE`: `3`
- `DOGE -> BTC -> XRP`: `2`
- `DOGE -> SOL -> DOGE`: `1`
- `PAXG -> BTC -> DOGE`: `1`
- `DOGE -> SOL -> PAXG`: `1`

## Einzelrücklesung

| Signatur | Rollenlesung | Funktion | Zustand | Top-Assets | Tiefe |
|---|---|---|---|---|---:|
| `dio_mcm_episode_0wyfujk` | `lange_btc_sol_welt_verdichtet_kurz_zu_milieu` | `active_recoupling -> milieu_island -> active_recoupling` | `young_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `DOGE -> BTC -> DOGE` | `0.555413 -> 0.774429 -> 0.772823` |
| `dio_mcm_episode_0bb4ews` | `weltkoerper_wechsel_schiebt_zwischen_milieu_und_rekopplung` | `milieu_island -> active_recoupling -> milieu_island` | `young_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase` | `DOGE -> SOL -> DOGE` | `0.553812 -> 0.749969 -> 0.692311` |
| `dio_mcm_episode_16hqn22` | `breitere_realwelt_rekoppelt_fruehes_milieu_aktiv` | `milieu_island -> active_recoupling -> active_recoupling` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `SOL -> BTC -> DOGE` | `0.595121 -> 0.790683 -> 0.788673` |
| `dio_mcm_episode_1y7uo9c` | `offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd` | `open_surface -> active_recoupling -> active_recoupling` | `young_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `PAXG -> BTC -> DOGE` | `0.552232 -> 0.707892 -> 0.723190` |
| `dio_mcm_episode_16yidit` | `offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd` | `open_surface -> active_recoupling -> active_recoupling` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `DOGE -> SOL -> PAXG` | `0.601437 -> 0.700000 -> 0.678722` |
| `dio_mcm_episode_0x60uui` | `multiasset_welt_rekoppelt_offene_oberflaeche` | `open_surface -> open_surface -> active_recoupling` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `DOGE -> BTC -> XRP` | `0.628007 -> 0.697173 -> 0.702399` |
| `dio_mcm_episode_0xg0gjh` | `lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche` | `active_recoupling -> open_surface -> open_surface` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `DOGE -> BTC -> DOGE` | `0.661977 -> 0.723947 -> 0.701940` |
| `dio_mcm_episode_0he6atw` | `multiasset_welt_aktiviert_milieunahe_phase` | `milieu_island -> milieu_island -> active_recoupling` | `positive_recoupling_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `SOL -> BTC -> DOGE` | `0.673306 -> 0.714234 -> 0.718205` |
| `dio_mcm_episode_16bqw8k` | `lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche` | `active_recoupling -> open_surface -> open_surface` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `SOL -> BTC -> DOGE` | `0.701787 -> 0.729200 -> 0.714535` |
| `dio_mcm_episode_1qlxgj7` | `multiasset_welt_bindet_rekopplung_zu_milieu` | `active_recoupling -> active_recoupling -> milieu_island` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `DOGE -> BTC -> DOGE` | `0.843927 -> 0.827115 -> 0.829085` |
| `dio_mcm_episode_1yxc2ug` | `lange_btc_sol_welt_verdichtet_kurz_zu_milieu` | `active_recoupling -> milieu_island -> active_recoupling` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `DOGE -> BTC -> XRP` | `0.812387 -> 0.825856 -> 0.821316` |

## Weltkörperdetails


### `dio_mcm_episode_0wyfujk`

- Rollenlesung: `lange_btc_sol_welt_verdichtet_kurz_zu_milieu`
- Funktion: `active_recoupling -> milieu_island -> active_recoupling`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:1;SOL:1`, Segmente `real:1;quiet:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:14;SOL:9`, Segmente `17K:13;34K_51K:5;17K_34K:5`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:11;PAXG:11;XRP:6`, Segmente `6K_16K:21;10K:7`

### `dio_mcm_episode_0bb4ews`

- Rollenlesung: `weltkoerper_wechsel_schiebt_zwischen_milieu_und_rekopplung`
- Funktion: `milieu_island -> active_recoupling -> milieu_island`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:2;BTC:1`, Segmente `real:2;stress:1`
- `long_btc_sol`: Top-Asset `SOL`, Assets `SOL:10;BTC:10`, Segmente `17K:10;34K_51K:6;17K_34K:4`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:5;XRP:3;PAXG:1`, Segmente `6K_16K:5;10K:4`

### `dio_mcm_episode_16hqn22`

- Rollenlesung: `breitere_realwelt_rekoppelt_fruehes_milieu_aktiv`
- Funktion: `milieu_island -> active_recoupling -> active_recoupling`
- `old_real`: Top-Asset `SOL`, Assets `SOL:3;DOGE:1`, Segmente `expansion:3;real:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:42;SOL:32`, Segmente `17K:32;17K_34K:21;34K_51K:21`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:27;XRP:17;PAXG:15`, Segmente `10K:31;6K_16K:28`

### `dio_mcm_episode_1y7uo9c`

- Rollenlesung: `offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd`
- Funktion: `open_surface -> active_recoupling -> active_recoupling`
- `old_real`: Top-Asset `PAXG`, Assets `PAXG:1;SOL:1`, Segmente `1h:1;expansion:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:10;SOL:10`, Segmente `17K_34K:11;17K:7;34K_51K:2`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:13;XRP:6;PAXG:6`, Segmente `6K_16K:15;10K:10`

### `dio_mcm_episode_16yidit`

- Rollenlesung: `offene_oberflaeche_wird_bei_mehr_weltkontakt_rekoppelnd`
- Funktion: `open_surface -> active_recoupling -> active_recoupling`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:3;BTC:1;SOL:1`, Segmente `real:2;1h:1;5m:1;expansion:1`
- `long_btc_sol`: Top-Asset `SOL`, Assets `SOL:12;BTC:9`, Segmente `17K:9;17K_34K:7;34K_51K:5`
- `multiasset`: Top-Asset `PAXG`, Assets `PAXG:7;XRP:4;DOGE:3`, Segmente `6K_16K:8;10K:6`

### `dio_mcm_episode_0x60uui`

- Rollenlesung: `multiasset_welt_rekoppelt_offene_oberflaeche`
- Funktion: `open_surface -> open_surface -> active_recoupling`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:3;SOL:2;BTC:1;PAXG:1`, Segmente `5m:2;expansion:2;1h:2;real:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:13;SOL:9`, Segmente `17K:8;34K_51K:8;17K_34K:6`
- `multiasset`: Top-Asset `XRP`, Assets `XRP:10;PAXG:9;DOGE:5`, Segmente `10K:15;6K_16K:9`

### `dio_mcm_episode_0xg0gjh`

- Rollenlesung: `lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche`
- Funktion: `active_recoupling -> open_surface -> open_surface`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:3;SOL:3;BTC:2;PAXG:1`, Segmente `real:3;1h:2;stress:1;5m:1;expansion:1;quiet:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:27;SOL:16`, Segmente `34K_51K:15;17K_34K:14;17K:14`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:11;PAXG:8;XRP:6`, Segmente `6K_16K:13;10K:12`

### `dio_mcm_episode_0he6atw`

- Rollenlesung: `multiasset_welt_aktiviert_milieunahe_phase`
- Funktion: `milieu_island -> milieu_island -> active_recoupling`
- `old_real`: Top-Asset `SOL`, Assets `SOL:7;DOGE:1`, Segmente `expansion:5;real:3`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:5;SOL:5`, Segmente `17K:7;17K_34K:2;34K_51K:1`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:8;XRP:6;PAXG:4`, Segmente `10K:15;6K_16K:3`

### `dio_mcm_episode_16bqw8k`

- Rollenlesung: `lange_und_multiasset_welt_oeffnen_rekopplung_als_oberflaeche`
- Funktion: `active_recoupling -> open_surface -> open_surface`
- `old_real`: Top-Asset `SOL`, Assets `SOL:9;BTC:6;DOGE:5;PAXG:1`, Segmente `expansion:8;stress:5;real:4;1h:2;5m:1;quiet:1`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:36;SOL:33`, Segmente `17K_34K:27;34K_51K:23;17K:19`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:15;XRP:15;PAXG:11`, Segmente `10K:22;6K_16K:19`

### `dio_mcm_episode_1qlxgj7`

- Rollenlesung: `multiasset_welt_bindet_rekopplung_zu_milieu`
- Funktion: `active_recoupling -> active_recoupling -> milieu_island`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:1409;SOL:674;BTC:255;PAXG:63`, Segmente `real:1091;expansion:534;5m:380;1h:200;stress:118;quiet:78`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:6646;SOL:6535`, Segmente `34K_51K:5251;17K:4254;17K_34K:3676`
- `multiasset`: Top-Asset `DOGE`, Assets `DOGE:4388;XRP:3254;PAXG:2967`, Segmente `10K:5593;6K_16K:5016`

### `dio_mcm_episode_1yxc2ug`

- Rollenlesung: `lange_btc_sol_welt_verdichtet_kurz_zu_milieu`
- Funktion: `active_recoupling -> milieu_island -> active_recoupling`
- `old_real`: Top-Asset `DOGE`, Assets `DOGE:188;SOL:24;BTC:21`, Segmente `real:103;5m:85;expansion:24;1h:14;stress:7`
- `long_btc_sol`: Top-Asset `BTC`, Assets `BTC:1384;SOL:1183`, Segmente `17K_34K:981;17K:858;34K_51K:728`
- `multiasset`: Top-Asset `XRP`, Assets `XRP:825;DOGE:500;PAXG:156`, Segmente `10K:866;6K_16K:615`

## Lesung

Der Feldfunktionswechsel ist kein Verschwinden der Signatur.

Die Signatur bleibt im gemeinsamen Realwelt-Kern erhalten, aber ihre Einbindung verschiebt sich je nach Weltkörper.

Damit wird die MCM-Topologie als dynamisches Bedeutungsnetz lesbar: Der Knoten bleibt, seine Rolle kann sich unter anderer Weltspannung verändern.

## Wie es weitergeht

Als nächstes sollten die stärksten Rollenwechsel mit Rohweltfenstern verglichen werden. Besonders relevant sind `active_recoupling -> open_surface` und `open_surface -> active_recoupling`, weil sie zeigen können, wann Weltkontakt öffnet oder rekoppelt.
