# 2023_HERKUNFTSDIAGNOSE_SHUFFLE_NULL_CHAIN - Feldphasen-Herkunftsdiagnose

## Zweck

Diese Diagnose liest die passive Feldphasen-Signatur-Memory und trennt Herkunftsqualität von reiner Wiederkehr.

Sie prüft nicht Handlung, Richtung oder Entry, sondern:

- Realwelt-Anteil
- Null-/Störwelt-Anteil
- Mixed-Binding-Anteil
- Feldfunktion
- Reifetiefe
- Drift

## Übersicht

- Signaturen gesamt: `269`

### Herkunftsqualität

- `realwelt_getragen`: `136`
- `gemischte_bindung`: `82`
- `feldinterne_nullordnung`: `51`

### Phasenzustand

- `young_field_phase`: `149`
- `positive_recoupling_field_phase`: `91`
- `stable_crossworld_field_phase`: `29`

### Dominante Weltbindung

- `realworld_bound`: `217`
- `field_internal_null_order`: `51`
- `mixed_binding`: `1`

### Feldfunktion

- `active_recoupling`: `123`
- `open_surface`: `81`
- `milieu_island`: `65`

## Top-Herkunftssignaturen

| Signatur | Herkunft | Zustand | Funktion | Tiefe | Drift | Real | Null | Mixed | Count/Welten |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| `dio_mcm_episode_0icnf2v` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.870 | 0.043 | 0.441 | 0.559 | 0.162 | 28040/10 |
| `dio_mcm_episode_1rj8742` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.861 | 0.045 | 0.583 | 0.417 | 0.000 | 5924/12 |
| `dio_mcm_episode_12tgchq` | `realwelt_getragen` | `stable_crossworld_field_phase` | `milieu_island` | 0.859 | 0.044 | 0.853 | 0.147 | 0.000 | 2388/8 |
| `dio_mcm_episode_1qlxgj7` | `realwelt_getragen` | `stable_crossworld_field_phase` | `active_recoupling` | 0.859 | 0.047 | 0.761 | 0.239 | 0.000 | 3156/12 |
| `dio_mcm_episode_0vcr3lw` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.840 | 0.047 | 0.640 | 0.360 | 0.000 | 89/12 |
| `dio_mcm_episode_0wo0tz1` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.840 | 0.044 | 0.681 | 0.319 | 0.000 | 2210/9 |
| `dio_mcm_episode_1eav7xq` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.839 | 0.047 | 0.574 | 0.426 | 0.000 | 94/12 |
| `dio_mcm_episode_0bsaqu1` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.838 | 0.045 | 0.625 | 0.375 | 0.000 | 80/12 |
| `dio_mcm_episode_0tfzgic` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.835 | 0.048 | 0.619 | 0.381 | 0.000 | 1343/11 |
| `dio_mcm_episode_0hvxln3` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.833 | 0.049 | 0.644 | 0.356 | 0.000 | 73/12 |
| `dio_mcm_episode_0iwh9d2` | `realwelt_getragen` | `positive_recoupling_field_phase` | `milieu_island` | 0.831 | 0.040 | 0.828 | 0.172 | 0.000 | 395/5 |
| `dio_mcm_episode_08g1nk4` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.830 | 0.053 | 0.607 | 0.393 | 0.000 | 84/10 |
| `dio_mcm_episode_0nu3wih` | `realwelt_getragen` | `stable_crossworld_field_phase` | `active_recoupling` | 0.827 | 0.049 | 0.937 | 0.063 | 0.000 | 414/11 |
| `dio_mcm_episode_14pd6eb` | `gemischte_bindung` | `positive_recoupling_field_phase` | `active_recoupling` | 0.825 | 0.042 | 0.500 | 0.500 | 0.125 | 48/7 |
| `dio_mcm_episode_14sn1ov` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.824 | 0.053 | 0.595 | 0.405 | 0.000 | 79/9 |
| `dio_mcm_episode_05upp98` | `gemischte_bindung` | `positive_recoupling_field_phase` | `milieu_island` | 0.824 | 0.041 | 0.477 | 0.523 | 0.205 | 44/7 |
| `dio_mcm_episode_1yxc2ug` | `realwelt_getragen` | `stable_crossworld_field_phase` | `active_recoupling` | 0.822 | 0.045 | 0.996 | 0.004 | 0.000 | 234/6 |
| `dio_mcm_episode_0b8eoy2` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.810 | 0.062 | 0.627 | 0.373 | 0.000 | 67/8 |
| `dio_mcm_episode_0n6m7si` | `gemischte_bindung` | `positive_recoupling_field_phase` | `active_recoupling` | 0.809 | 0.045 | 0.333 | 0.667 | 0.333 | 33/7 |
| `dio_mcm_episode_0bygq81` | `gemischte_bindung` | `positive_recoupling_field_phase` | `milieu_island` | 0.806 | 0.035 | 0.484 | 0.516 | 0.194 | 31/6 |
| `dio_mcm_episode_15z3zml` | `realwelt_getragen` | `stable_crossworld_field_phase` | `active_recoupling` | 0.796 | 0.053 | 0.838 | 0.162 | 0.000 | 37/8 |
| `dio_mcm_episode_1aejc9m` | `gemischte_bindung` | `stable_crossworld_field_phase` | `active_recoupling` | 0.791 | 0.052 | 0.556 | 0.444 | 0.000 | 117/9 |
| `dio_mcm_episode_0ca57t8` | `gemischte_bindung` | `positive_recoupling_field_phase` | `milieu_island` | 0.780 | 0.033 | 0.422 | 0.578 | 0.281 | 64/3 |
| `dio_mcm_episode_094f7up` | `feldinterne_nullordnung` | `positive_recoupling_field_phase` | `milieu_island` | 0.780 | 0.029 | 0.158 | 0.842 | 0.158 | 19/5 |
| `dio_mcm_episode_171moy1` | `realwelt_getragen` | `stable_crossworld_field_phase` | `active_recoupling` | 0.771 | 0.043 | 0.826 | 0.174 | 0.000 | 23/9 |
| `dio_mcm_episode_0vig3jz` | `realwelt_getragen` | `positive_recoupling_field_phase` | `milieu_island` | 0.771 | 0.042 | 0.926 | 0.074 | 0.000 | 269/2 |
| `dio_mcm_episode_1fdlu6e` | `realwelt_getragen` | `positive_recoupling_field_phase` | `milieu_island` | 0.770 | 0.044 | 0.987 | 0.013 | 0.000 | 537/2 |
| `dio_mcm_episode_0izppf1` | `feldinterne_nullordnung` | `positive_recoupling_field_phase` | `active_recoupling` | 0.770 | 0.058 | 0.217 | 0.783 | 0.217 | 23/6 |
| `dio_mcm_episode_17i3weh` | `gemischte_bindung` | `positive_recoupling_field_phase` | `active_recoupling` | 0.767 | 0.044 | 0.600 | 0.400 | 0.000 | 20/7 |
| `dio_mcm_episode_1i3ov0z` | `realwelt_getragen` | `positive_recoupling_field_phase` | `active_recoupling` | 0.760 | 0.043 | 0.969 | 0.031 | 0.000 | 64/3 |

## Lesung

Eine stabile Feldphase ist erst dann fachlich stark, wenn ihre Herkunft mitgelesen wird.

Eine Signatur kann tief und wiederkehrend sein, aber trotzdem anders zu lesen sein, wenn sie unter Null- oder Random-Sign-Welten stark mitgetragen wird.

Damit wird die Feldmemory genauer: Sie speichert nicht nur, dass eine Phase wiederkehrt, sondern in welcher Herkunftsqualität sie wiederkehrt.
