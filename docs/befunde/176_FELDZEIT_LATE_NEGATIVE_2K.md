# Feldzeit-Diagnose

Stand: 2026-06-18 22:19:09

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
| late_negative_2k | 1994 | 0.000530/0.056000 | 0.017424/0.375000 | 0.630192 | 0.363286 | 0.191589 | 116 | 971 | 326 |

## Weltprofile

### late_negative_2k

- Datenwelt: `data\kontrolliert_2025_late_negative_test1_2000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_late_negative_2025_2k`
- Zeitstatus: `temporal_first_contact` `1805`, `temporal_far_return` `187`, `temporal_near_return` `2`
- Feldwirkung: `stabil` `1013`, `tragend_unruhig` `816`, `kippend` `69`, `gespannt` `68`, `diffus` `28`

Stärkste Nachhallabschnitte:

- Abschnitt `9` (`1592`-`1791`): max_afterimage `0.056000`, avg_recurrence `0.039453`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `5` (`796`-`995`): max_afterimage `0.044800`, avg_recurrence `0.013999`, dominante Wirkung `stabil`, Memory `10`
- Abschnitt `2` (`199`-`398`): max_afterimage `0.041481`, avg_recurrence `0.007538`, dominante Wirkung `stabil`, Memory `10`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.039453`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0h0v` (`0.010`)
- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.029293`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0ke1` (`0.010`)
- Abschnitt `6` (`995`-`1194`): avg_recurrence `0.024019`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1lb5` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `3` (`398`-`597`): memory_ratio `0.101`, Rekopplung `0.624707`, Tragqualität `0.355651`, Strain `0.199330`
- Abschnitt `8` (`1393`-`1592`): memory_ratio `0.101`, Rekopplung `0.624208`, Tragqualität `0.369720`, Strain `0.215992`
- Abschnitt `7` (`1194`-`1393`): memory_ratio `0.090`, Rekopplung `0.624174`, Tragqualität `0.358335`, Strain `0.205055`

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
