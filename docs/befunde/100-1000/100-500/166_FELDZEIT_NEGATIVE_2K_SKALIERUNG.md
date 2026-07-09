# Feldzeit-Diagnose

Stand: 2026-06-18 22:05:48

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
| negative_moderate_1k | 994 | 0.000627/0.074969 | 0.012162/0.375000 | 0.631065 | 0.362044 | 0.188110 | 44 | 473 | 122 |
| negative_moderate_2k | 1994 | 0.000567/0.074969 | 0.018025/0.444444 | 0.629660 | 0.360479 | 0.191097 | 104 | 986 | 321 |

## Weltprofile

### negative_moderate_1k

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

### negative_moderate_2k

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_2000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_negative_2023_moderate_2k`
- Zeitstatus: `temporal_first_contact` `1804`, `temporal_far_return` `190`
- Feldwirkung: `stabil` `1067`, `tragend_unruhig` `766`, `kippend` `75`, `gespannt` `67`, `diffus` `19`

Stärkste Nachhallabschnitte:

- Abschnitt `1` (`0`-`199`): max_afterimage `0.074969`, avg_recurrence `0.005623`, dominante Wirkung `stabil`, Memory `8`
- Abschnitt `5` (`796`-`995`): max_afterimage `0.066051`, avg_recurrence `0.022105`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.057795`, avg_recurrence `0.033701`, dominante Wirkung `stabil`, Memory `16`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.033701`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_03t5` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.029553`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_00fj` (`0.010`)
- Abschnitt `5` (`796`-`995`): avg_recurrence `0.022105`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_165g` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.079`, Rekopplung `0.625670`, Tragqualität `0.351529`, Strain `0.195788`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.070`, Rekopplung `0.625947`, Tragqualität `0.361388`, Strain `0.205093`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.060`, Rekopplung `0.632782`, Tragqualität `0.356876`, Strain `0.177827`

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
