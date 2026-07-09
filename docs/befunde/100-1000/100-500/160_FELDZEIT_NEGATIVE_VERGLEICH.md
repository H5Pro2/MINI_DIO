# Feldzeit-Diagnose

Stand: 2026-06-18 21:49:48

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
| negative_moderate | 994 | 0.000627/0.074969 | 0.012162/0.375000 | 0.631065 | 0.362044 | 0.188110 | 44 | 473 | 122 |
| negative_stress | 994 | 0.001214/0.126000 | 0.012707/0.375000 | 0.630398 | 0.356899 | 0.186196 | 58 | 426 | 127 |

## Weltprofile

### negative_moderate

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_negative_2023_moderate_test1`
- Zeitstatus: `temporal_first_contact` `927`, `temporal_far_return` `67`
- Feldwirkung: `stabil` `553`, `tragend_unruhig` `369`, `kippend` `39`, `gespannt` `26`, `diffus` `7`

Stärkste Nachhallabschnitte:

- Abschnitt `2` (`99`-`198`): max_afterimage `0.074969`, avg_recurrence `0.007937`, dominante Wirkung `stabil`, Memory `2`
- Abschnitt `9` (`792`-`891`): max_afterimage `0.066051`, avg_recurrence `0.020142`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.046667`, avg_recurrence `0.023347`, dominante Wirkung `stabil`, Memory `2`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.023347`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1ldk` (`0.019`)
- Abschnitt `5` (`396`-`495`): avg_recurrence `0.021405`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0g5y` (`0.020`)
- Abschnitt `9` (`792`-`891`): avg_recurrence `0.020142`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_05kd` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `3` (`198`-`297`): memory_ratio `0.081`, Rekopplung `0.629999`, Tragqualität `0.354467`, Strain `0.185923`
- Abschnitt `5` (`396`-`495`): memory_ratio `0.081`, Rekopplung `0.627785`, Tragqualität `0.358226`, Strain `0.197240`
- Abschnitt `1` (`0`-`99`): memory_ratio `0.061`, Rekopplung `0.630652`, Tragqualität `0.358371`, Strain `0.183180`

### negative_stress

- Datenwelt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_negative_2023_stress_test1`
- Zeitstatus: `temporal_first_contact` `925`, `temporal_far_return` `66`, `temporal_immediate_afterimage` `2`, `temporal_near_return` `1`
- Feldwirkung: `stabil` `550`, `tragend_unruhig` `373`, `kippend` `36`, `gespannt` `30`, `diffus` `5`

Stärkste Nachhallabschnitte:

- Abschnitt `1` (`0`-`99`): max_afterimage `0.126000`, avg_recurrence `0.003367`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `6` (`495`-`594`): max_afterimage `0.126000`, avg_recurrence `0.015091`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `5` (`396`-`495`): max_afterimage `0.111363`, avg_recurrence `0.017076`, dominante Wirkung `stabil`, Memory `4`

Stärkste Wiederkehrabschnitte:

- Abschnitt `8` (`693`-`792`): avg_recurrence `0.026936`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0t1i` (`0.020`)
- Abschnitt `9` (`792`-`891`): avg_recurrence `0.018939`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1sme` (`0.020`)
- Abschnitt `5` (`396`-`495`): avg_recurrence `0.017076`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1f08` (`0.020`)

Stärkste Memoryabschnitte:

- Abschnitt `3` (`198`-`297`): memory_ratio `0.121`, Rekopplung `0.619546`, Tragqualität `0.344560`, Strain `0.206498`
- Abschnitt `9` (`792`-`891`): memory_ratio `0.121`, Rekopplung `0.624183`, Tragqualität `0.355147`, Strain `0.201280`
- Abschnitt `1` (`0`-`99`): memory_ratio `0.061`, Rekopplung `0.630421`, Tragqualität `0.351895`, Strain `0.179469`

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
