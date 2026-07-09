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
| sol_2024_15m_2k | 1994 | 0.000323/0.084000 | 0.008308/0.375000 | 0.606542 | 0.343678 | 0.241083 | 308 | 1075 | 172 |

## Weltprofile

### sol_2024_15m_2k

- Datenwelt: `data\kontrolliert_sol_2024_15m_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2024_15m_2k`
- Zeitstatus: `temporal_first_contact` `1903`, `temporal_far_return` `90`, `temporal_near_return` `1`
- Feldwirkung: `tragend_unruhig` `891`, `stabil` `470`, `kippend` `320`, `gespannt` `263`, `diffus` `47`, `rekoppelnd` `3`

Stärkste Nachhallabschnitte:

- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.084000`, avg_recurrence `0.013161`, dominante Wirkung `tragend_unruhig`, Memory `27`
- Abschnitt `2` (`199`-`398`): max_afterimage `0.036669`, avg_recurrence `0.005623`, dominante Wirkung `tragend_unruhig`, Memory `34`
- Abschnitt `4` (`597`-`796`): max_afterimage `0.034158`, avg_recurrence `0.004397`, dominante Wirkung `tragend_unruhig`, Memory `54`

Stärkste Wiederkehrabschnitte:

- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.013999`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0mp0` (`0.005`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.013520`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0gdw` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.013161`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1u20` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `4` (`597`-`796`): memory_ratio `0.271`, Rekopplung `0.595475`, Tragqualität `0.329551`, Strain `0.259334`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.171`, Rekopplung `0.592910`, Tragqualität `0.331789`, Strain `0.268427`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.171`, Rekopplung `0.596987`, Tragqualität `0.334511`, Strain `0.259185`

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
