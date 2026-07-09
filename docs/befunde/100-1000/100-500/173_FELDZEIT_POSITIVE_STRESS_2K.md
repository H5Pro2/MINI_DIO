# Feldzeit-Diagnose

Stand: 2026-06-18 22:15:54

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
| positive_stress_2k | 1994 | 0.000947/0.126000 | 0.022346/0.444444 | 0.631225 | 0.362635 | 0.187569 | 78 | 949 | 372 |

## Weltprofile

### positive_stress_2k

- Datenwelt: `data\kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_positive_stress_2024_2k`
- Zeitstatus: `temporal_first_contact` `1761`, `temporal_far_return` `230`, `temporal_near_return` `2`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `stabil` `1044`, `tragend_unruhig` `798`, `kippend` `83`, `gespannt` `47`, `diffus` `21`, `rekoppelnd` `1`

Stärkste Nachhallabschnitte:

- Abschnitt `2` (`199`-`398`): max_afterimage `0.126000`, avg_recurrence `0.007538`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `1` (`0`-`199`): max_afterimage `0.098000`, avg_recurrence `0.000838`, dominante Wirkung `stabil`, Memory `8`
- Abschnitt `4` (`597`-`796`): max_afterimage `0.070000`, avg_recurrence `0.024408`, dominante Wirkung `stabil`, Memory `2`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.043003`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_04ks` (`0.010`)
- Abschnitt `6` (`995`-`1194`): avg_recurrence `0.035475`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0s9h` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.033471`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1r0p` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.089`, Rekopplung `0.616685`, Tragqualität `0.361885`, Strain `0.231529`
- Abschnitt `6` (`995`-`1194`): memory_ratio `0.060`, Rekopplung `0.637784`, Tragqualität `0.367270`, Strain `0.174805`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.050`, Rekopplung `0.630412`, Tragqualität `0.362448`, Strain `0.188248`

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
