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
| sol_2025_5m_2k | 1994 | 0.001903/0.126000 | 0.035818/0.500000 | 0.636504 | 0.365647 | 0.173548 | 54 | 916 | 493 |

## Weltprofile

### sol_2025_5m_2k

- Datenwelt: `data\kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2025_5m_2k`
- Zeitstatus: `temporal_first_contact` `1659`, `temporal_far_return` `327`, `temporal_near_return` `6`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `stabil` `1145`, `tragend_unruhig` `767`, `kippend` `35`, `gespannt` `28`, `diffus` `19`

Stärkste Nachhallabschnitte:

- Abschnitt `2` (`199`-`398`): max_afterimage `0.126000`, avg_recurrence `0.015434`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.126000`, avg_recurrence `0.062565`, dominante Wirkung `stabil`, Memory `10`
- Abschnitt `8` (`1393`-`1592`): max_afterimage `0.112000`, avg_recurrence `0.045585`, dominante Wirkung `stabil`, Memory `6`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.069845`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0zxj` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.062565`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0wwh` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.052744`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1hh7` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.050`, Rekopplung `0.635531`, Tragqualität `0.363423`, Strain `0.173967`
- Abschnitt `5` (`796`-`995`): memory_ratio `0.040`, Rekopplung `0.635146`, Tragqualität `0.357612`, Strain `0.168722`
- Abschnitt `4` (`597`-`796`): memory_ratio `0.030`, Rekopplung `0.635256`, Tragqualität `0.369532`, Strain `0.182511`

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
