# Feldzeit-Diagnose

Stand: 2026-06-18 23:14:20

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
| sol_2024_1h_2k | 1994 | 0.000605/0.126000 | 0.015423/0.500000 | 0.587027 | 0.333433 | 0.287549 | 642 | 1190 | 272 |

## Weltprofile

### sol_2024_1h_2k

- Datenwelt: `data\kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2024_1h_2k`
- Zeitstatus: `temporal_first_contact` `1841`, `temporal_far_return` `152`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `gespannt` `625`, `tragend_unruhig` `605`, `kippend` `475`, `stabil` `213`, `diffus` `71`, `rekoppelnd` `5`

Stärkste Nachhallabschnitte:

- Abschnitt `1` (`0`-`199`): max_afterimage `0.126000`, avg_recurrence `0.005025`, dominante Wirkung `gespannt`, Memory `65`
- Abschnitt `10` (`1791`-`1994`): max_afterimage `0.109045`, avg_recurrence `0.038764`, dominante Wirkung `gespannt`, Memory `85`
- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.044800`, avg_recurrence `0.023919`, dominante Wirkung `gespannt`, Memory `78`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.038764`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1fv6` (`0.010`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.028087`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1g8p` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.023919`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_043x` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `10` (`1791`-`1994`): memory_ratio `0.419`, Rekopplung `0.574887`, Tragqualität `0.321717`, Strain `0.306019`
- Abschnitt `2` (`199`-`398`): memory_ratio `0.397`, Rekopplung `0.579856`, Tragqualität `0.323599`, Strain `0.298743`
- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.392`, Rekopplung `0.584477`, Tragqualität `0.332441`, Strain `0.296291`

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
