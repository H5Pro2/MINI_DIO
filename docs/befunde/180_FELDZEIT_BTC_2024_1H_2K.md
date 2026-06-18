# Feldzeit-Diagnose

Stand: 2026-06-18 22:34:07

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
| btc_2024_1h_2k | 1994 | 0.000421/0.086304 | 0.009253/0.500000 | 0.610376 | 0.345005 | 0.234259 | 328 | 1082 | 170 |

## Weltprofile

### btc_2024_1h_2k

- Datenwelt: `data\kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2024_1h_2k`
- Zeitstatus: `temporal_first_contact` `1895`, `temporal_far_return` `99`
- Feldwirkung: `tragend_unruhig` `839`, `stabil` `584`, `gespannt` `271`, `kippend` `246`, `diffus` `48`, `rekoppelnd` `6`

Stärkste Nachhallabschnitte:

- Abschnitt `8` (`1393`-`1592`): max_afterimage `0.086304`, avg_recurrence `0.013719`, dominante Wirkung `tragend_unruhig`, Memory `50`
- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.078005`, avg_recurrence `0.018396`, dominante Wirkung `tragend_unruhig`, Memory `34`
- Abschnitt `7` (`1194`-`1393`): max_afterimage `0.066082`, avg_recurrence `0.015644`, dominante Wirkung `tragend_unruhig`, Memory `20`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.018396`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0dhp` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.015644`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0qgi` (`0.010`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.013719`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1kwc` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.296`, Rekopplung `0.591675`, Tragqualität `0.335706`, Strain `0.274782`
- Abschnitt `8` (`1393`-`1592`): memory_ratio `0.251`, Rekopplung `0.600318`, Tragqualität `0.340127`, Strain `0.259868`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.181`, Rekopplung `0.606453`, Tragqualität `0.334689`, Strain `0.240529`

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
