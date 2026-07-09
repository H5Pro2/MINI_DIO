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
| btc_2024_5m_2k | 1994 | 0.002684/0.126851 | 0.047686/0.615385 | 0.636577 | 0.366108 | 0.172431 | 62 | 937 | 598 |

## Weltprofile

### btc_2024_5m_2k

- Datenwelt: `data\kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2024_5m_2k`
- Zeitstatus: `temporal_first_contact` `1569`, `temporal_far_return` `417`, `temporal_near_return` `6`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `stabil` `1130`, `tragend_unruhig` `750`, `kippend` `48`, `gespannt` `42`, `diffus` `24`

Stärkste Nachhallabschnitte:

- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.126851`, avg_recurrence `0.095457`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `2` (`199`-`398`): max_afterimage `0.126000`, avg_recurrence `0.013400`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `8` (`1393`-`1592`): max_afterimage `0.111710`, avg_recurrence `0.083493`, dominante Wirkung `stabil`, Memory `4`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.112676`, max_recurrence `0.615385`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0zrk` (`0.015`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.095457`, max_recurrence `0.583333`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_11c4` (`0.010`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.083493`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_03a3` (`0.015`)

Stärkste Memoryabschnitte:

- Abschnitt `4` (`597`-`796`): memory_ratio `0.090`, Rekopplung `0.628028`, Tragqualität `0.358228`, Strain `0.191380`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.060`, Rekopplung `0.636091`, Tragqualität `0.366380`, Strain `0.174797`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.030`, Rekopplung `0.636402`, Tragqualität `0.368731`, Strain `0.177466`

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
