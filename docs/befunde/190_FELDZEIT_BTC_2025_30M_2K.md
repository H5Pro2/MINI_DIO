# Feldzeit-Diagnose

Stand: 2026-06-18 22:56:11

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
| btc_2025_30m_2k | 1994 | 0.000689/0.126000 | 0.015062/0.444444 | 0.623087 | 0.355382 | 0.205899 | 166 | 994 | 262 |

## Weltprofile

### btc_2025_30m_2k

- Datenwelt: `data\kontrolliert_btc_2025_30m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2025_30m_2k`
- Zeitstatus: `temporal_first_contact` `1836`, `temporal_far_return` `154`, `temporal_near_return` `3`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `stabil` `845`, `tragend_unruhig` `841`, `kippend` `144`, `gespannt` `131`, `diffus` `32`, `rekoppelnd` `1`

Stärkste Nachhallabschnitte:

- Abschnitt `1` (`0`-`199`): max_afterimage `0.126000`, avg_recurrence `0.001675`, dominante Wirkung `tragend_unruhig`, Memory `12`
- Abschnitt `6` (`995`-`1194`): max_afterimage `0.084957`, avg_recurrence `0.017558`, dominante Wirkung `tragend_unruhig`, Memory `14`
- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.061736`, avg_recurrence `0.031990`, dominante Wirkung `stabil`, Memory `6`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.031990`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0uy5` (`0.010`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.030211`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_12dz` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.020818`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1tqe` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `5` (`796`-`995`): memory_ratio `0.131`, Rekopplung `0.610631`, Tragqualität `0.348550`, Strain `0.236011`
- Abschnitt `4` (`597`-`796`): memory_ratio `0.111`, Rekopplung `0.618866`, Tragqualität `0.345783`, Strain `0.212482`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.101`, Rekopplung `0.623338`, Tragqualität `0.356661`, Strain `0.205385`

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
