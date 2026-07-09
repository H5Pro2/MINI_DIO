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
| sol_2024_30m_2k | 1994 | 0.000394/0.126000 | 0.008778/0.444444 | 0.600205 | 0.341420 | 0.256735 | 440 | 1193 | 174 |

## Weltprofile

### sol_2024_30m_2k

- Datenwelt: `data\kontrolliert_sol_2024_30m_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2024_30m_2k`
- Zeitstatus: `temporal_first_contact` `1901`, `temporal_far_return` `90`, `temporal_near_return` `2`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `tragend_unruhig` `776`, `kippend` `393`, `stabil` `390`, `gespannt` `362`, `diffus` `70`, `rekoppelnd` `3`

Stärkste Nachhallabschnitte:

- Abschnitt `7` (`1194`-`1393`): max_afterimage `0.126000`, avg_recurrence `0.011247`, dominante Wirkung `tragend_unruhig`, Memory `32`
- Abschnitt `3` (`398`-`597`): max_afterimage `0.089214`, avg_recurrence `0.005384`, dominante Wirkung `tragend_unruhig`, Memory `64`
- Abschnitt `5` (`796`-`995`): max_afterimage `0.056000`, avg_recurrence `0.005025`, dominante Wirkung `tragend_unruhig`, Memory `36`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.019167`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0t27` (`0.010`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.017079`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_18hu` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.012324`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_09l0` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `2` (`199`-`398`): memory_ratio `0.342`, Rekopplung `0.589786`, Tragqualität `0.340224`, Strain `0.284319`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.322`, Rekopplung `0.589434`, Tragqualität `0.333610`, Strain `0.280157`
- Abschnitt `1` (`0`-`199`): memory_ratio `0.281`, Rekopplung `0.591963`, Tragqualität `0.340432`, Strain `0.281037`

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
