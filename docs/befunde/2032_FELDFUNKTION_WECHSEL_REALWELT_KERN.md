# 2032_FELDFUNKTION_WECHSEL_REALWELT_KERN - Feldfunktionswechsel im Realwelt-Kern

## Zweck

Dieser Bericht vergleicht dieselben Feldphasen-Signaturen über mehrere reale Weltketten.

Geprüft wird nicht, ob eine Signatur nur wiederkehrt, sondern ob sie ihre Feldfunktion hält oder je nach Weltkörper eine andere Rolle annimmt.

Verglichene Ketten:

- `old_real`
- `long_btc_sol`
- `multiasset`

## Übersicht

- gemeinsamer Realwelt-Kern: `50` Signaturen
- Signaturen mit Feldfunktionswechsel: `11`
- Signaturen mit Zustandswechsel: `31`

### Wechselklassen

- `zustand_reift_oder_kippt`: `25`
- `funktion_stabil`: `7`
- `zustand_und_funktion_verschoben`: `6`
- `variante_verschoben`: `6`
- `funktion_verschoben`: `5`
- `tiefe_deutlich_bewegt`: `1`

### Häufigste Feldfunktionspfade

- `active_recoupling -> active_recoupling -> active_recoupling`: `24`
- `milieu_island -> milieu_island -> milieu_island`: `15`
- `active_recoupling -> milieu_island -> active_recoupling`: `2`
- `open_surface -> active_recoupling -> active_recoupling`: `2`
- `active_recoupling -> open_surface -> open_surface`: `2`
- `milieu_island -> active_recoupling -> active_recoupling`: `1`
- `milieu_island -> active_recoupling -> milieu_island`: `1`
- `active_recoupling -> active_recoupling -> milieu_island`: `1`
- `milieu_island -> milieu_island -> active_recoupling`: `1`
- `open_surface -> open_surface -> active_recoupling`: `1`

### Häufigste Zustandspfade

- `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase`: `20`
- `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase`: `11`
- `positive_recoupling_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase`: `8`
- `young_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase`: `5`
- `young_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase`: `3`
- `young_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase`: `1`
- `positive_recoupling_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase`: `1`
- `stable_crossworld_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase`: `1`

### Häufigste Herkunftspfade

- `realwelt_getragen -> realwelt_getragen -> realwelt_getragen`: `50`

## Feldfunktionswechsel

| Signatur | Klasse | Zustandspfad | Funktionspfad | Tiefe | Drift |
|---|---|---|---|---:|---:|
| `dio_mcm_episode_1qlxgj7` | `funktion_verschoben` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> milieu_island` | `0.843927 -> 0.827115 -> 0.829085` | `0.046201 -> 0.055660 -> 0.055576` |
| `dio_mcm_episode_1yxc2ug` | `zustand_und_funktion_verschoben` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> milieu_island -> active_recoupling` | `0.812387 -> 0.825856 -> 0.821316` | `0.044964 -> 0.062273 -> 0.065375` |
| `dio_mcm_episode_16hqn22` | `zustand_und_funktion_verschoben` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> active_recoupling -> active_recoupling` | `0.595121 -> 0.790683 -> 0.788673` | `0.039466 -> 0.057422 -> 0.051995` |
| `dio_mcm_episode_0wyfujk` | `zustand_und_funktion_verschoben` | `young_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `active_recoupling -> milieu_island -> active_recoupling` | `0.555413 -> 0.774429 -> 0.772823` | `0.057824 -> 0.054758 -> 0.055763` |
| `dio_mcm_episode_0bb4ews` | `zustand_und_funktion_verschoben` | `young_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase` | `milieu_island -> active_recoupling -> milieu_island` | `0.553812 -> 0.749969 -> 0.692311` | `0.030479 -> 0.030705 -> 0.034463` |
| `dio_mcm_episode_16bqw8k` | `funktion_verschoben` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> open_surface -> open_surface` | `0.701787 -> 0.729200 -> 0.714535` | `0.017946 -> 0.050709 -> 0.054522` |
| `dio_mcm_episode_0xg0gjh` | `funktion_verschoben` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> open_surface -> open_surface` | `0.661977 -> 0.723947 -> 0.701940` | `0.015504 -> 0.029970 -> 0.026436` |
| `dio_mcm_episode_1y7uo9c` | `zustand_und_funktion_verschoben` | `young_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `open_surface -> active_recoupling -> active_recoupling` | `0.552232 -> 0.707892 -> 0.723190` | `0.040074 -> 0.072607 -> 0.071341` |
| `dio_mcm_episode_0he6atw` | `funktion_verschoben` | `positive_recoupling_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> active_recoupling` | `0.673306 -> 0.714234 -> 0.718205` | `0.038126 -> 0.037301 -> 0.058134` |
| `dio_mcm_episode_0x60uui` | `funktion_verschoben` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `open_surface -> open_surface -> active_recoupling` | `0.628007 -> 0.697173 -> 0.702399` | `0.024571 -> 0.038710 -> 0.029672` |
| `dio_mcm_episode_16yidit` | `zustand_und_funktion_verschoben` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `open_surface -> active_recoupling -> active_recoupling` | `0.601437 -> 0.700000 -> 0.678722` | `0.013690 -> 0.024435 -> 0.027417` |

## Zustandswechsel

| Signatur | Klasse | Zustandspfad | Funktionspfad | Tiefe | Drift |
|---|---|---|---|---:|---:|
| `dio_mcm_episode_0iwh9d2` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.764748 -> 0.848824 -> 0.847396` | `0.038802 -> 0.046974 -> 0.047807` |
| `dio_mcm_episode_12tgchq` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.824693 -> 0.847418 -> 0.845983` | `0.043521 -> 0.050915 -> 0.049008` |
| `dio_mcm_episode_0bygq81` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.723534 -> 0.846386 -> 0.835857` | `0.040288 -> 0.045483 -> 0.046175` |
| `dio_mcm_episode_05upp98` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.742449 -> 0.845502 -> 0.840732` | `0.039827 -> 0.046662 -> 0.044604` |
| `dio_mcm_episode_1qv5i56` | `zustand_reift_oder_kippt` | `young_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.613271 -> 0.844299 -> 0.818386` | `0.019322 -> 0.044280 -> 0.043338` |
| `dio_mcm_episode_14pd6eb` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.769585 -> 0.843894 -> 0.840914` | `0.039865 -> 0.050213 -> 0.045380` |
| `dio_mcm_episode_1c8zokt` | `zustand_reift_oder_kippt` | `young_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.555881 -> 0.840598 -> 0.768189` | `0.015674 -> 0.051379 -> 0.046290` |
| `dio_mcm_episode_1rf1k15` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.627397 -> 0.833067 -> 0.810019` | `0.027330 -> 0.043228 -> 0.036714` |
| `dio_mcm_episode_1i3ov0z` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.729424 -> 0.828846 -> 0.832871` | `0.042217 -> 0.050874 -> 0.048320` |
| `dio_mcm_episode_1yxc2ug` | `zustand_und_funktion_verschoben` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> milieu_island -> active_recoupling` | `0.812387 -> 0.825856 -> 0.821316` | `0.044964 -> 0.062273 -> 0.065375` |
| `dio_mcm_episode_06eyd53` | `zustand_reift_oder_kippt` | `young_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.584029 -> 0.822560 -> 0.744522` | `0.024957 -> 0.041983 -> 0.047504` |
| `dio_mcm_episode_14sn1ov` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.778156 -> 0.816514 -> 0.814710` | `0.055294 -> 0.062725 -> 0.062214` |
| `dio_mcm_episode_0b8eoy2` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.770080 -> 0.815665 -> 0.811240` | `0.066194 -> 0.065464 -> 0.064538` |
| `dio_mcm_episode_0vidg3n` | `zustand_reift_oder_kippt` | `young_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.542113 -> 0.814902 -> 0.726521` | `0.000000 -> 0.046869 -> 0.062422` |
| `dio_mcm_episode_15z3zml` | `zustand_reift_oder_kippt` | `positive_recoupling_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.765175 -> 0.814881 -> 0.807733` | `0.053892 -> 0.064174 -> 0.064338` |
| `dio_mcm_episode_0nu3wih` | `zustand_reift_oder_kippt` | `stable_crossworld_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.814007 -> 0.719018 -> 0.683691` | `0.049324 -> 0.050188 -> 0.044312` |

## Stabile Kernsignaturen

| Signatur | Klasse | Zustandspfad | Funktionspfad | Tiefe | Drift |
|---|---|---|---|---:|---:|
| `dio_mcm_episode_0icnf2v` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `milieu_island -> milieu_island -> milieu_island` | `0.847206 -> 0.847505 -> 0.848468` | `0.042285 -> 0.046268 -> 0.048092` |
| `dio_mcm_episode_1rj8742` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.842520 -> 0.825458 -> 0.830190` | `0.045490 -> 0.049337 -> 0.048249` |
| `dio_mcm_episode_0bsaqu1` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.809338 -> 0.821206 -> 0.817310` | `0.041893 -> 0.060607 -> 0.060942` |
| `dio_mcm_episode_0vcr3lw` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.811692 -> 0.817113 -> 0.819619` | `0.047498 -> 0.063823 -> 0.057735` |
| `dio_mcm_episode_0hvxln3` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.800860 -> 0.817478 -> 0.817481` | `0.051182 -> 0.060294 -> 0.056324` |
| `dio_mcm_episode_08g1nk4` | `funktion_stabil` | `stable_crossworld_field_phase -> stable_crossworld_field_phase -> stable_crossworld_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.784989 -> 0.816539 -> 0.814029` | `0.057141 -> 0.060768 -> 0.059046` |
| `dio_mcm_episode_1f9nms9` | `funktion_stabil` | `positive_recoupling_field_phase -> positive_recoupling_field_phase -> positive_recoupling_field_phase` | `active_recoupling -> active_recoupling -> active_recoupling` | `0.660881 -> 0.698252 -> 0.679626` | `0.028542 -> 0.065588 -> 0.059190` |

## Lesung

Der gemeinsame Realwelt-Kern bleibt nicht nur als Symbolmenge interessant. Entscheidend ist, ob eine Signatur über verschiedene Weltkörper dieselbe Feldrolle trägt oder ihre Rolle verschiebt.

Ein stabiler Funktionspfad spricht für eine robuste Kernrolle. Ein Feldfunktionswechsel spricht dagegen für eine Signatur, die nicht verschwindet, sondern je nach Weltspannung anders eingebunden wird.

Damit wird die Topologie nicht als starre Karte gelesen, sondern als dynamisches Bedeutungsnetz: gleiche Signatur, mögliche andere Rolle.

## Wie es weitergeht

Als nächstes sollte geprüft werden, welche konkreten Weltmerkmale die Feldfunktionswechsel auslösen. Relevant sind besonders Signaturen, die zwischen `active_recoupling`, `milieu_island` und `open_surface` wechseln.
