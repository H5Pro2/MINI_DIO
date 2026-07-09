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
| btc_2025_5m_2k | 1994 | 0.005003/0.135274 | 0.072769/0.642857 | 0.638380 | 0.368524 | 0.167311 | 86 | 1011 | 687 |

## Weltprofile

### btc_2025_5m_2k

- Datenwelt: `data\kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv`
- Debug: `debug\research_chain_btc_2025_5m_2k`
- Zeitstatus: `temporal_first_contact` `1429`, `temporal_far_return` `557`, `temporal_near_return` `6`, `temporal_immediate_afterimage` `2`
- Feldwirkung: `stabil` `1139`, `tragend_unruhig` `745`, `kippend` `46`, `gespannt` `44`, `diffus` `20`

Stärkste Nachhallabschnitte:

- Abschnitt `4` (`597`-`796`): max_afterimage `0.135274`, avg_recurrence `0.074339`, dominante Wirkung `stabil`, Memory `6`
- Abschnitt `5` (`796`-`995`): max_afterimage `0.126000`, avg_recurrence `0.072505`, dominante Wirkung `stabil`, Memory `8`
- Abschnitt `6` (`995`-`1194`): max_afterimage `0.126000`, avg_recurrence `0.108090`, dominante Wirkung `stabil`, Memory `6`

Stärkste Wiederkehrabschnitte:

- Abschnitt `7` (`1194`-`1393`): avg_recurrence `0.122746`, max_recurrence `0.615385`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1bfo` (`0.015`)
- Abschnitt `6` (`995`-`1194`): avg_recurrence `0.108090`, max_recurrence `0.500000`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_0e9t` (`0.020`)
- Abschnitt `8` (`1393`-`1592`): avg_recurrence `0.105275`, max_recurrence `0.583333`, dominante Zeitlage `temporal_first_contact`, dominante Formfamilie `dio_1uvm` (`0.015`)

Stärkste Memoryabschnitte:

- Abschnitt `9` (`1592`-`1791`): memory_ratio `0.070`, Rekopplung `0.637785`, Tragqualität `0.364941`, Strain `0.167783`
- Abschnitt `1` (`0`-`199`): memory_ratio `0.060`, Rekopplung `0.629205`, Tragqualität `0.354141`, Strain `0.178299`
- Abschnitt `8` (`1393`-`1592`): memory_ratio `0.050`, Rekopplung `0.641361`, Tragqualität `0.375101`, Strain `0.165452`

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
