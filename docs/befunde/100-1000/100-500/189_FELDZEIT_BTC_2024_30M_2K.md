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
| btc_2024_30m_2k | 1994 | 0.000900/0.115907 | 0.019469/0.375000 | 0.626156 | 0.359372 | 0.201056 | 178 | 991 | 325 |

## Weltprofile

### btc_2024_30m_2k

- Datenwelt: `data\kontrolliert_btc_2024_30m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2024_30m_2k`
- Zeitstatus: `temporal_first_contact` `1790`, `temporal_far_return` `200`, `temporal_near_return` `4`
- Feldwirkung: `stabil` `928`, `tragend_unruhig` `785`, `gespannt` `125`, `kippend` `123`, `diffus` `29`, `rekoppelnd` `4`

Stärkste Nachhallabschnitte:

- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.115907`, avg_recurrence `0.040992`, dominante Wirkung `stabil`, Memory `16`
- Abschnitt `1` (`0`-`199`): max_afterimage `0.112000`, avg_recurrence `0.001675`, dominante Wirkung `stabil`, Memory `32`
- Abschnitt `3` (`398`-`597`): max_afterimage `0.098755`, avg_recurrence `0.008973`, dominante Wirkung `tragend_unruhig`, Memory `44`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.040992`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1v8e` (`0.015`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.031646`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1g35` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.028565`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_01zv` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `3` (`398`-`597`): memory_ratio `0.221`, Rekopplung `0.608792`, Tragqualität `0.341157`, Strain `0.238550`
- Abschnitt `1` (`0`-`199`): memory_ratio `0.161`, Rekopplung `0.618883`, Tragqualität `0.356736`, Strain `0.220536`
- Abschnitt `6` (`995`-`1194`): memory_ratio `0.101`, Rekopplung `0.622380`, Tragqualität `0.354201`, Strain `0.206256`

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
