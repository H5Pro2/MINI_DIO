# Feldzeit-Diagnose

Stand: 2026-06-18 22:02:33

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
| sideways_2026_1k | 994 | 0.000261/0.098000 | 0.004815/0.285714 | 0.615214 | 0.351964 | 0.224037 | 116 | 515 | 50 |
| sideways_2026_2k | 1994 | 0.000467/0.098000 | 0.011605/0.444444 | 0.622030 | 0.355412 | 0.207645 | 174 | 1011 | 222 |

## Weltprofile

### sideways_2026_1k

- Datenwelt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_sideways_2026_test1`
- Zeitstatus: `temporal_first_contact` `966`, `temporal_far_return` `27`, `temporal_near_return` `1`
- Feldwirkung: `tragend_unruhig` `459`, `stabil` `317`, `kippend` `108`, `gespannt` `84`, `diffus` `24`, `rekoppelnd` `2`

Stärkste Nachhallabschnitte:

- Abschnitt `6` (`495`-`594`): max_afterimage `0.098000`, avg_recurrence `0.005051`, dominante Wirkung `tragend_unruhig`, Memory `10`
- Abschnitt `10` (`891`-`994`): max_afterimage `0.028718`, avg_recurrence `0.018955`, dominante Wirkung `stabil`, Memory `4`
- Abschnitt `7` (`594`-`693`): max_afterimage `0.010566`, avg_recurrence `0.006734`, dominante Wirkung `stabil`, Memory `4`

Stärkste Wiederkehrabschnitte:

- Abschnitt `10` (`891`-`994`): avg_recurrence `0.018955`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_023a` (`0.019`)
- Abschnitt `8` (`693`-`792`): avg_recurrence `0.008418`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0q71` (`0.010`)
- Abschnitt `7` (`594`-`693`): avg_recurrence `0.006734`, max_recurrence `0.166667`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1l83` (`0.010`)

Stärkste Memoryabschnitte:

- Abschnitt `4` (`297`-`396`): memory_ratio `0.303`, Rekopplung `0.590701`, Tragqualität `0.338782`, Strain `0.283157`
- Abschnitt `2` (`99`-`198`): memory_ratio `0.202`, Rekopplung `0.610163`, Tragqualität `0.335307`, Strain `0.224463`
- Abschnitt `1` (`0`-`99`): memory_ratio `0.182`, Rekopplung `0.609870`, Tragqualität `0.349599`, Strain `0.237776`

### sideways_2026_2k

- Datenwelt: `data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_sideways_2026_2k`
- Zeitstatus: `temporal_first_contact` `1867`, `temporal_far_return` `126`, `temporal_near_return` `1`
- Feldwirkung: `tragend_unruhig` `854`, `stabil` `821`, `kippend` `155`, `gespannt` `116`, `diffus` `44`, `rekoppelnd` `4`

Stärkste Nachhallabschnitte:

- Abschnitt `3` (`398`-`597`): max_afterimage `0.098000`, avg_recurrence `0.004188`, dominante Wirkung `tragend_unruhig`, Memory `16`
- Abschnitt `8` (`1393`-`1592`): max_afterimage `0.074363`, avg_recurrence `0.016232`, dominante Wirkung `stabil`, Memory `10`
- Abschnitt `6` (`995`-`1194`): max_afterimage `0.051134`, avg_recurrence `0.015404`, dominante Wirkung `tragend_unruhig`, Memory `12`

Stärkste Wiederkehrabschnitte:

- Abschnitt `9` (`1592`-`1791`): avg_recurrence `0.022583`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0f10` (`0.010`)
- Abschnitt `10` (`1791`-`1994`): avg_recurrence `0.019235`, max_recurrence `0.285714`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1793` (`0.010`)
- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.018396`, max_recurrence `0.375000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1hmz` (`0.005`)

Stärkste Memoryabschnitte:

- Abschnitt `2` (`199`-`398`): memory_ratio `0.241`, Rekopplung `0.594397`, Tragqualität `0.338376`, Strain `0.271569`
- Abschnitt `1` (`0`-`199`): memory_ratio `0.191`, Rekopplung `0.610171`, Tragqualität `0.342675`, Strain `0.230813`
- Abschnitt `3` (`398`-`597`): memory_ratio `0.080`, Rekopplung `0.613438`, Tragqualität `0.353095`, Strain `0.227255`

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
