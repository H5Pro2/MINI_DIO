# Feldzeit-Diagnose

Stand: 2026-06-18 22:41:38

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
| btc_2025_1h_2k | 1994 | 0.000305/0.046667 | 0.009335/0.375000 | 0.611240 | 0.347018 | 0.233802 | 346 | 1082 | 187 |

## Weltprofile

### btc_2025_1h_2k

- Datenwelt: `data\kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2025_1h_2k`
- Zeitstatus: `temporal_first_contact` `1890`, `temporal_far_return` `102`, `temporal_near_return` `2`
- Feldwirkung: `tragend_unruhig` `845`, `stabil` `578`, `gespannt` `275`, `kippend` `248`, `diffus` `41`, `rekoppelnd` `7`

Stärkste Nachhallabschnitte:

- Abschnitt `7` (`1194`-`1393`): max_afterimage `0.046667`, avg_recurrence `0.012563`, dominante Wirkung `tragend_unruhig`, Memory `37`
- Abschnitt `5` (`796`-`995`): max_afterimage `0.038621`, avg_recurrence `0.005623`, dominante Wirkung `tragend_unruhig`, Memory `25`
- Abschnitt `4` (`597`-`796`): max_afterimage `0.028000`, avg_recurrence `0.008375`, dominante Wirkung `tragend_unruhig`, Memory `33`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.016772`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1lrk` (`0.005`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.016631`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1ldk` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.012563`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_13kr` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `8` (`1393`-`1592`): memory_ratio `0.256`, Rekopplung `0.594710`, Tragqualität `0.341194`, Strain `0.278035`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.226`, Rekopplung `0.606418`, Tragqualität `0.343688`, Strain `0.245612`
- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.196`, Rekopplung `0.607681`, Tragqualität `0.352556`, Strain `0.247846`

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
