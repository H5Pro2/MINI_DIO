# Feldzeit-Diagnose

Stand: 2026-06-18 22:56:10

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
| btc_2024_15m_2k | 1994 | 0.001242/0.078606 | 0.030761/0.500000 | 0.631196 | 0.362364 | 0.187788 | 104 | 934 | 431 |

## Weltprofile

### btc_2024_15m_2k

- Datenwelt: `data\kontrolliert_btc_2024_15m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2024_15m_2k`
- Zeitstatus: `temporal_first_contact` `1705`, `temporal_far_return` `286`, `temporal_near_return` `3`
- Feldwirkung: `stabil` `1011`, `tragend_unruhig` `792`, `kippend` `93`, `gespannt` `83`, `diffus` `15`

Stärkste Nachhallabschnitte:

- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.078606`, avg_recurrence `0.063521`, dominante Wirkung `stabil`, Memory `2`
- Abschnitt `3` (`398`-`597`): max_afterimage `0.065046`, avg_recurrence `0.017947`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `4` (`597`-`796`): max_afterimage `0.053218`, avg_recurrence `0.020310`, dominante Wirkung `stabil`, Memory `14`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.063521`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0chk` (`0.020`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.057739`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0j9a` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.049912`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0ksn` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `6` (`995`-`1194`): memory_ratio `0.121`, Rekopplung `0.623176`, Tragqualität `0.361143`, Strain `0.211415`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.101`, Rekopplung `0.622262`, Tragqualität `0.352802`, Strain `0.208448`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.070`, Rekopplung `0.618446`, Tragqualität `0.343594`, Strain `0.207841`

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
