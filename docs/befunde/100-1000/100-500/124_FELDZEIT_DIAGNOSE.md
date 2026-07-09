# Feldzeit-Diagnose

Stand: 2026-06-18 17:44:15

## Zweck

Diese Diagnose prüft passiv, ob MINI_DIO zeitliche Tiefe bereits aus dem Feldverhalten bildet.
Es geht nicht um eine externe Uhr und nicht um eine neue Runtime-Regel.

Hierarchie der Prüfung:

1. Grundfrage: Entsteht im MCM-Feld eine eigene zeitliche Tiefe?
2. Unterprüfung: Wo erscheinen Nachhall, Wiederkehr, Drift, Verblassen und Rekopplung über Zeit?
3. Folgeschritt: Prüfen, ob diese Feldzeit bei neuen Welten stabil bleibt oder neue Zeittöne bildet.

## Ergebnisübersicht

| Welt | Episoden | Nachhall avg/max | Wiederkehr avg/max | Rekopplung | Tragqualität | Strain | Episodenmemory | Feldübergänge | Zeitübergänge |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| welt_2023_01 | 994 | 0.000987/0.140818 | 0.010096/0.375000 | 0.623022 | 0.353039 | 0.205616 | 86 | 498 | 91 |
| welt_2024_01 | 994 | 0.000351/0.126000 | 0.005437/0.285714 | 0.622297 | 0.358091 | 0.209955 | 80 | 523 | 58 |
| welt_2025_core_01 | 994 | 0.001361/0.126000 | 0.014893/0.375000 | 0.633885 | 0.361269 | 0.177359 | 24 | 434 | 134 |
| welt_2025_mid_shift_01 | 994 | 0.001230/0.136506 | 0.013849/0.444444 | 0.630490 | 0.359369 | 0.186445 | 56 | 465 | 119 |
| welt_2025_late_shift_01 | 994 | 0.000625/0.062222 | 0.013504/0.375000 | 0.633999 | 0.361895 | 0.178473 | 20 | 461 | 138 |
| welt_2023_stress_01 | 994 | 0.000274/0.048696 | 0.004527/0.166667 | 0.614985 | 0.346134 | 0.222566 | 106 | 515 | 50 |
| welt_2024_bridge3_01 | 994 | 0.000134/0.035000 | 0.003856/0.166667 | 0.616367 | 0.353651 | 0.222512 | 116 | 552 | 44 |

## Weltprofile

### welt_2023_01

- Datenwelt: `data\kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain`
- Zeitstatus: `temporal_first_contact` `942`, `temporal_far_return` `51`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `stabil` `466`, `tragend_unruhig` `388`, `kippend` `69`, `gespannt` `60`, `diffus` `11`

Stärkste Nachhallabschnitte:

- Abschnitt `2` (`99`-`198`): max_afterimage `0.140818`, avg_recurrence `0.015873`, dominante Wirkung `stabil`, Memory `2`
- Abschnitt `8` (`693`-`792`): max_afterimage `0.123018`, avg_recurrence `0.010041`, dominante Wirkung `tragend_unruhig`, Memory `20`
- Abschnitt `4` (`297`-`396`): max_afterimage `0.058947`, avg_recurrence `0.017557`, dominante Wirkung `stabil`, Memory `4`

Stärkste Wiederkehrabschnitte:

- Abschnitt `6` (`495`-`594`): avg_recurrence `0.018038`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0o3d` (`0.020`)
- Abschnitt `4` (`297`-`396`): avg_recurrence `0.017557`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1h70` (`0.020`)
- Abschnitt `2` (`99`-`198`): avg_recurrence `0.015873`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1jnc` (`0.020`)

Stärkste Memoryabschnitte:

- Abschnitt `9` (`792`-`891`): memory_ratio `0.263`, Rekopplung `0.605007`, Tragqualität `0.339262`, Strain `0.246795`
- Abschnitt `8` (`693`-`792`): memory_ratio `0.202`, Rekopplung `0.607938`, Tragqualität `0.351691`, Strain `0.247309`
- Abschnitt `5` (`396`-`495`): memory_ratio `0.081`, Rekopplung `0.625562`, Tragqualität `0.349306`, Strain `0.194934`

### welt_2024_01

- Datenwelt: `data\kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2024_01`
- Zeitstatus: `temporal_first_contact` `963`, `temporal_far_return` `30`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `tragend_unruhig` `453`, `stabil` `400`, `kippend` `68`, `gespannt` `60`, `diffus` `11`, `rekoppelnd` `2`

Stärkste Nachhallabschnitte:

- Abschnitt `8` (`693`-`792`): max_afterimage `0.126000`, avg_recurrence `0.011304`, dominante Wirkung `tragend_unruhig`, Memory `24`
- Abschnitt `4` (`297`-`396`): max_afterimage `0.037333`, avg_recurrence `0.001684`, dominante Wirkung `tragend_unruhig`, Memory `6`
- Abschnitt `7` (`594`-`693`): max_afterimage `0.018983`, avg_recurrence `0.006253`, dominante Wirkung `stabil`, Memory `0`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.012945`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0ngd` (`0.010`)
- Abschnitt `8` (`693`-`792`): avg_recurrence `0.011304`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_00cf` (`0.020`)
- Abschnitt `7` (`594`-`693`): avg_recurrence `0.006253`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_094w` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `8` (`693`-`792`): memory_ratio `0.242`, Rekopplung `0.603452`, Tragqualität `0.354334`, Strain `0.263042`
- Abschnitt `10` (`891`-`994`): memory_ratio `0.136`, Rekopplung `0.624620`, Tragqualität `0.364488`, Strain `0.210615`
- Abschnitt `5` (`396`-`495`): memory_ratio `0.121`, Rekopplung `0.614076`, Tragqualität `0.348864`, Strain `0.222184`

### welt_2025_core_01

- Datenwelt: `data\kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2025_core_01`
- Zeitstatus: `temporal_first_contact` `915`, `temporal_far_return` `74`, `temporal_near_return` `4`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `stabil` `541`, `tragend_unruhig` `417`, `kippend` `17`, `gespannt` `12`, `diffus` `7`

Stärkste Nachhallabschnitte:

- Abschnitt `4` (`297`-`396`): max_afterimage `0.126000`, avg_recurrence `0.021405`, dominante Wirkung `stabil`, Memory `0`
- Abschnitt `3` (`198`-`297`): max_afterimage `0.111109`, avg_recurrence `0.009620`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `6` (`495`-`594`): max_afterimage `0.100451`, avg_recurrence `0.012987`, dominante Wirkung `stabil`, Memory `0`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.032998`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_12em` (`0.019`)
- Abschnitt `9` (`792`-`891`): avg_recurrence `0.026455`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1q02` (`0.020`)
- Abschnitt `4` (`297`-`396`): avg_recurrence `0.021405`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_07y1` (`0.020`)

Stärkste Memoryabschnitte:

- Abschnitt `3` (`198`-`297`): memory_ratio `0.040`, Rekopplung `0.632383`, Tragqualität `0.355826`, Strain `0.176256`
- Abschnitt `5` (`396`-`495`): memory_ratio `0.040`, Rekopplung `0.629354`, Tragqualität `0.352013`, Strain `0.181093`
- Abschnitt `8` (`693`-`792`): memory_ratio `0.040`, Rekopplung `0.631411`, Tragqualität `0.361782`, Strain `0.187181`

### welt_2025_mid_shift_01

- Datenwelt: `data\kontrolliert_2025_mid_shift_test_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2025_mid_shift_01`
- Zeitstatus: `temporal_first_contact` `922`, `temporal_far_return` `70`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `stabil` `510`, `tragend_unruhig` `410`, `gespannt` `32`, `kippend` `30`, `diffus` `11`, `rekoppelnd` `1`

Stärkste Nachhallabschnitte:

- Abschnitt `5` (`396`-`495`): max_afterimage `0.136506`, avg_recurrence `0.013408`, dominante Wirkung `stabil`, Memory `2`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.131473`, avg_recurrence `0.024503`, dominante Wirkung `stabil`, Memory `8`
- Abschnitt `3` (`198`-`297`): max_afterimage `0.126000`, avg_recurrence `0.008418`, dominante Wirkung `stabil`, Memory `8`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`792`-`891`): avg_recurrence `0.033049`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0zrk` (`0.020`)
- Abschnitt `10` (`891`-`994`): avg_recurrence `0.024503`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1wta` (`0.019`)
- Abschnitt `7` (`594`-`693`): avg_recurrence `0.019240`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1np6` (`0.020`)

Stärkste Memoryabschnitte:

- Abschnitt `1` (`0`-`99`): memory_ratio `0.101`, Rekopplung `0.611985`, Tragqualität `0.345758`, Strain `0.228268`
- Abschnitt `3` (`198`-`297`): memory_ratio `0.081`, Rekopplung `0.630674`, Tragqualität `0.356384`, Strain `0.183648`
- Abschnitt `8` (`693`-`792`): memory_ratio `0.081`, Rekopplung `0.631619`, Tragqualität `0.359827`, Strain `0.185141`

### welt_2025_late_shift_01

- Datenwelt: `data\kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2025_late_shift_01`
- Zeitstatus: `temporal_first_contact` `919`, `temporal_far_return` `75`
- Feldwirkung: `stabil` `544`, `tragend_unruhig` `405`, `kippend` `23`, `gespannt` `14`, `diffus` `8`

Stärkste Nachhallabschnitte:

- Abschnitt `3` (`198`-`297`): max_afterimage `0.062222`, avg_recurrence `0.006734`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.041517`, avg_recurrence `0.033056`, dominante Wirkung `stabil`, Memory `0`
- Abschnitt `8` (`693`-`792`): max_afterimage `0.032127`, avg_recurrence `0.020142`, dominante Wirkung `stabil`, Memory `0`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.033056`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0nik` (`0.019`)
- Abschnitt `7` (`594`-`693`): avg_recurrence `0.022607`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_17sh` (`0.020`)
- Abschnitt `8` (`693`-`792`): avg_recurrence `0.020142`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0ht4` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `6` (`495`-`594`): memory_ratio `0.081`, Rekopplung `0.623075`, Tragqualität `0.340555`, Strain `0.192791`
- Abschnitt `1` (`0`-`99`): memory_ratio `0.061`, Rekopplung `0.624929`, Tragqualität `0.351404`, Strain `0.193423`
- Abschnitt `3` (`198`-`297`): memory_ratio `0.040`, Rekopplung `0.632475`, Tragqualität `0.357724`, Strain `0.179313`

### welt_2023_stress_01

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2023_stress_01`
- Zeitstatus: `temporal_first_contact` `967`, `temporal_far_return` `27`
- Feldwirkung: `tragend_unruhig` `436`, `stabil` `348`, `kippend` `102`, `gespannt` `89`, `diffus` `19`

Stärkste Nachhallabschnitte:

- Abschnitt `6` (`495`-`594`): max_afterimage `0.048696`, avg_recurrence `0.011785`, dominante Wirkung `stabil`, Memory `8`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.031111`, avg_recurrence `0.008091`, dominante Wirkung `tragend_unruhig`, Memory `14`
- Abschnitt `2` (`99`-`198`): max_afterimage `0.014737`, avg_recurrence `0.001684`, dominante Wirkung `tragend_unruhig`, Memory `10`

Stärkste Wiederkehrabschnitte:

- Abschnitt `6` (`495`-`594`): avg_recurrence `0.011785`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_15pt` (`0.020`)
- Abschnitt `10` (`891`-`994`): avg_recurrence `0.008091`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1rou` (`0.019`)
- Abschnitt `7` (`594`-`693`): avg_recurrence `0.006734`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_07l4` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `8` (`693`-`792`): memory_ratio `0.232`, Rekopplung `0.601073`, Tragqualität `0.343818`, Strain `0.264755`
- Abschnitt `9` (`792`-`891`): memory_ratio `0.202`, Rekopplung `0.595149`, Tragqualität `0.330807`, Strain `0.267082`
- Abschnitt `10` (`891`-`994`): memory_ratio `0.136`, Rekopplung `0.607389`, Tragqualität `0.345111`, Strain `0.244812`

### welt_2024_bridge3_01

- Datenwelt: `data\kontrolliert_2024_bridge_test3_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_2024_bridge3_01`
- Zeitstatus: `temporal_first_contact` `971`, `temporal_far_return` `23`
- Feldwirkung: `tragend_unruhig` `470`, `stabil` `326`, `kippend` `98`, `gespannt` `79`, `diffus` `21`

Stärkste Nachhallabschnitte:

- Abschnitt `5` (`396`-`495`): max_afterimage `0.035000`, avg_recurrence `0.001684`, dominante Wirkung `tragend_unruhig`, Memory `8`
- Abschnitt `1` (`0`-`99`): max_afterimage `0.020741`, avg_recurrence `0.001684`, dominante Wirkung `tragend_unruhig`, Memory `20`
- Abschnitt `3` (`198`-`297`): max_afterimage `0.008000`, avg_recurrence `0.001684`, dominante Wirkung `tragend_unruhig`, Memory `12`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.011327`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1y5r` (`0.010`)
- Abschnitt `9` (`792`-`891`): avg_recurrence `0.006734`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1vl4` (`0.010`)
- Abschnitt `4` (`297`-`396`): avg_recurrence `0.005051`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_07iv` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `9` (`792`-`891`): memory_ratio `0.283`, Rekopplung `0.597302`, Tragqualität `0.334300`, Strain `0.259585`
- Abschnitt `1` (`0`-`99`): memory_ratio `0.202`, Rekopplung `0.610324`, Tragqualität `0.352399`, Strain `0.236986`
- Abschnitt `6` (`495`-`594`): memory_ratio `0.141`, Rekopplung `0.613978`, Tragqualität `0.356233`, Strain `0.232346`

## Befund

Feldzeit ist in den bisherigen Daten nicht als starke externe Uhr sichtbar.
Sie erscheint eher als innere Zeitspur: Wiederkehr einzelner Formfamilien, kurze Nachhallspitzen, wechselnde Rekopplung und unterschiedlich dichte Episodenmemory.

Wichtig ist die Trennung:

- `mini_afterimage` zeigt Restwirkung einer vorherigen Lage.
- `mini_recurrence_strength` zeigt Wiederkehr oder erneute Nähe.
- `episode_memory_count` zeigt, dass bestimmte Abschnitte mehr innere Verarbeitung tragen.
- `effect_transition_count` zeigt, wie oft die Feldwirkung wechselt.
- `temporal_transition_count` zeigt, ob die Zeitlage selbst wechselt oder weitgehend gleich bleibt.

Damit wirkt Feldzeit aktuell nicht wie programmierte Mehrdimensionalzeit, sondern wie eine passive Tiefe des Feldes: etwas war da, wirkt nach, kehrt wieder oder verliert seine Nähe.

## Interpretation

Das passt zur aktuellen Forschungsrichtung: MINI_DIO muss Zeit nicht als harte Mechanik bekommen, solange das Feld selbst zeitliche Qualitäten lesbar bildet.
Die Diagnose darf aber nicht überdehnt werden. Die meisten Episoden bleiben `temporal_first_contact`; Wiederkehr und Nachhall sind noch dünne, aber messbare Spuren.

## Wie es weitergeht

Als nächstes sollte die Feldzeit gegen die bestehenden Feldklassen gehalten werden.
Konkrete Unterprüfung: Entsteht mehr Nachhall/Wiederkehr in der ruhigen Nähegruppe oder im Stress-Gegenpol?
Erst danach entscheiden wir, ob eine eigene Feldzeit-Karte notwendig ist oder ob die vorhandene Topologie-Karte reicht.
