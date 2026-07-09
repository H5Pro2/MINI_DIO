# Feldzeit-Diagnose

Stand: 2026-06-18 21:45:23

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
| sideways_2024 | 994 | 0.000749/0.126000 | 0.014987/0.500000 | 0.630554 | 0.359280 | 0.185652 | 42 | 449 | 132 |

## Weltprofile

### sideways_2024

- Datenwelt: `data\kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_sideways_2024_test1`
- Zeitstatus: `temporal_first_contact` `919`, `temporal_far_return` `74`, `temporal_immediate_afterimage` `1`
- Feldwirkung: `stabil` `515`, `tragend_unruhig` `415`, `kippend` `28`, `gespannt` `24`, `diffus` `11`, `rekoppelnd` `1`

Stärkste Nachhallabschnitte:

- Abschnitt `9` (`792`-`891`): max_afterimage `0.126000`, avg_recurrence `0.034031`, dominante Wirkung `stabil`, Memory `2`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.031111`, avg_recurrence `0.019822`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `8` (`693`-`792`): max_afterimage `0.029173`, avg_recurrence `0.028299`, dominante Wirkung `stabil`, Memory `0`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`792`-`891`): avg_recurrence `0.034031`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1pcw` (`0.020`)
- Abschnitt `8` (`693`-`792`): avg_recurrence `0.028299`, max_recurrence `0.444444`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0f2k` (`0.010`)
- Abschnitt `10` (`891`-`994`): avg_recurrence `0.019822`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1pnw` (`0.019`)

Stärkste Memoryabschnitte:

- Abschnitt `7` (`594`-`693`): memory_ratio `0.081`, Rekopplung `0.625662`, Tragqualität `0.360298`, Strain `0.205001`
- Abschnitt `2` (`99`-`198`): memory_ratio `0.071`, Rekopplung `0.628734`, Tragqualität `0.346727`, Strain `0.175602`
- Abschnitt `4` (`297`-`396`): memory_ratio `0.061`, Rekopplung `0.628761`, Tragqualität `0.355558`, Strain `0.189667`

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
