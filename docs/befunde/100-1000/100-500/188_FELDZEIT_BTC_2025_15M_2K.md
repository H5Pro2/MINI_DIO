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
| btc_2025_15m_2k | 1994 | 0.001435/0.133895 | 0.029200/0.500000 | 0.631429 | 0.363392 | 0.187799 | 124 | 973 | 435 |

## Weltprofile

### btc_2025_15m_2k

- Datenwelt: `data\kontrolliert_btc_2025_15m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2025_15m_2k`
- Zeitstatus: `temporal_first_contact` `1711`, `temporal_far_return` `277`, `temporal_near_return` `4`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `stabil` `1023`, `tragend_unruhig` `782`, `kippend` `92`, `gespannt` `79`, `diffus` `18`

Stärkste Nachhallabschnitte:

- Abschnitt `6` (`995`-`1194`): max_afterimage `0.133895`, avg_recurrence `0.044648`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `2` (`199`-`398`): max_afterimage `0.126000`, avg_recurrence `0.020430`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.116586`, avg_recurrence `0.026908`, dominante Wirkung `tragend_unruhig`, Memory `34`

Stärkste Wiederkehrabschnitte:

- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.055147`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1x99` (`0.015`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.047370`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1yvo` (`0.010`)
- Abschnitt `6` (`995`-`1194`): avg_recurrence `0.044648`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0rqr` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.167`, Rekopplung `0.613542`, Tragqualität `0.350090`, Strain `0.229986`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.080`, Rekopplung `0.629097`, Tragqualität `0.358756`, Strain `0.190723`
- Abschnitt `4` (`597`-`796`): memory_ratio `0.070`, Rekopplung `0.628084`, Tragqualität `0.359117`, Strain `0.192973`

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
