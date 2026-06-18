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
| sol_2024_5m_2k | 1994 | 0.000490/0.126000 | 0.011627/0.375000 | 0.622777 | 0.358038 | 0.208681 | 148 | 1056 | 226 |

## Weltprofile

### sol_2024_5m_2k

- Datenwelt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2024_5m_2k`
- Zeitstatus: `temporal_first_contact` `1869`, `temporal_far_return` `123`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `tragend_unruhig` `918`, `stabil` `811`, `kippend` `137`, `gespannt` `102`, `diffus` `23`, `rekoppelnd` `3`

Stärkste Nachhallabschnitte:

- Abschnitt `4` (`597`-`796`): max_afterimage `0.126000`, avg_recurrence `0.008734`, dominante Wirkung `tragend_unruhig`, Memory `24`
- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.126000`, avg_recurrence `0.023223`, dominante Wirkung `tragend_unruhig`, Memory `14`
- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.050909`, avg_recurrence `0.019592`, dominante Wirkung `tragend_unruhig`, Memory `18`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.023223`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0wsj` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.021656`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0id0` (`0.015`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.019592`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1ttr` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `4` (`597`-`796`): memory_ratio `0.121`, Rekopplung `0.617478`, Tragqualität `0.361737`, Strain `0.227698`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.090`, Rekopplung `0.622829`, Tragqualität `0.363033`, Strain `0.213426`
- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.090`, Rekopplung `0.622545`, Tragqualität `0.358747`, Strain `0.211349`

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
