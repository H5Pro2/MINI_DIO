# Feldzeit-Diagnose

Stand: 2026-06-18 23:14:19

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
| sol_2025_15m_2k | 1994 | 0.000499/0.112000 | 0.010763/0.444444 | 0.615512 | 0.351537 | 0.222780 | 246 | 989 | 212 |

## Weltprofile

### sol_2025_15m_2k

- Datenwelt: `data\kontrolliert_sol_2025_15m_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2025_15m_2k`
- Zeitstatus: `temporal_first_contact` `1876`, `temporal_far_return` `115`, `temporal_near_return` `3`
- Feldwirkung: `tragend_unruhig` `862`, `stabil` `676`, `gespannt` `218`, `kippend` `202`, `diffus` `36`

Stärkste Nachhallabschnitte:

- Abschnitt `4` (`597`-`796`): max_afterimage `0.112000`, avg_recurrence `0.007538`, dominante Wirkung `tragend_unruhig`, Memory `22`
- Abschnitt `8` (`1393`-`1592`): max_afterimage `0.084000`, avg_recurrence `0.020180`, dominante Wirkung `tragend_unruhig`, Memory `20`
- Abschnitt `2` (`199`-`398`): max_afterimage `0.056000`, avg_recurrence `0.003948`, dominante Wirkung `stabil`, Memory `10`

Stärkste Wiederkehrabschnitte:

- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.020180`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_09ir` (`0.010`)
- Abschnitt `6` (`995`-`1194`): avg_recurrence `0.018755`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0f2w` (`0.010`)
- Abschnitt `5` (`796`-`995`): avg_recurrence `0.013999`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_06hu` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.345`, Rekopplung `0.582792`, Tragqualität `0.327275`, Strain `0.293065`
- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.291`, Rekopplung `0.590895`, Tragqualität `0.341020`, Strain `0.284342`
- Abschnitt `4` (`597`-`796`): memory_ratio `0.111`, Rekopplung `0.616315`, Tragqualität `0.346126`, Strain `0.215074`

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
