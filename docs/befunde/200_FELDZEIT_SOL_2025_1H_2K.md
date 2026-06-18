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
| sol_2025_1h_2k | 1994 | 0.000652/0.084000 | 0.014472/0.545455 | 0.589067 | 0.335489 | 0.283691 | 590 | 1142 | 243 |

## Weltprofile

### sol_2025_1h_2k

- Datenwelt: `data\kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv`
- Debug: `debug\research_chain_sol_2025_1h_2k`
- Zeitstatus: `temporal_first_contact` `1849`, `temporal_far_return` `144`, `temporal_near_return` `1`
- Feldwirkung: `tragend_unruhig` `630`, `gespannt` `584`, `kippend` `466`, `stabil` `235`, `diffus` `76`, `rekoppelnd` `3`

Stärkste Nachhallabschnitte:

- Abschnitt `5` (`796`-`995`): max_afterimage `0.084000`, avg_recurrence `0.015793`, dominante Wirkung `gespannt`, Memory `83`
- Abschnitt `3` (`398`-`597`): max_afterimage `0.047449`, avg_recurrence `0.008136`, dominante Wirkung `gespannt`, Memory `71`
- Abschnitt `4` (`597`-`796`): max_afterimage `0.046667`, avg_recurrence `0.013161`, dominante Wirkung `gespannt`, Memory `59`

Stärkste Wiederkehrabschnitte:

- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.030420`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_11cy` (`0.010`)
- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.025404`, max_recurrence `0.545455`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_12rx` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.020988`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1e2d` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `5` (`796`-`995`): memory_ratio `0.417`, Rekopplung `0.582771`, Tragqualität `0.332733`, Strain `0.298998`
- Abschnitt `8` (`1393`-`1592`): memory_ratio `0.397`, Rekopplung `0.581740`, Tragqualität `0.337629`, Strain `0.308955`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.357`, Rekopplung `0.575305`, Tragqualität `0.319799`, Strain `0.310849`

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
