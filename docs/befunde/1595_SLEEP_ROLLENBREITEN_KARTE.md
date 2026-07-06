# Sleep-Rollenbreiten-Karte

Stand: 2026-07-06 10:17:28

## Grundfrage

Wo kippt Offline-Feld-Reorganisation von voller fokussierter Rekopplung in selektive Reorganisation?

## Unterpruefung

Verglichen werden Real-Sleep-Real-Laeufe mit 2000er-Fenstern. Die Diagnose ist passiv: Sie liest Rollenanzahl, Kombinationen, Strain-Anteil und Sleep-Reaktivierung.

## Rollenbreiten-Karte

| Label | Klasse | Rollen | Kombinationen | Rollen reaktiviert | Kombis voll | Kombis teilweise | Strain-Rollen | Afterimage | Rekopplung | Carry | Strain |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| synth_rand_kipp_2000_start0_multirole_repro | selektiv_breit | 5 | 10 | 4 (0.8000) | 6 (0.6000) | 4 (0.4000) | 2 (0.4000) | 0.6412 | 0.7346 | 0.5809 | 0.1353 |
| synth_bruch_rand_a_2000_start0_high_afterimage_repro | voll_fokussiert | 3 | 3 | 3 (1.0000) | 3 (1.0000) | 0 (0.0000) | 1 (0.3333) | 0.7645 | 0.7509 | 0.6048 | 0.1218 |
| synth_rand_dominanz_gedaempft_2000_start0_role5_repro | voll_fokussiert | 5 | 10 | 5 (1.0000) | 10 (1.0000) | 0 (0.0000) | 2 (0.4000) | 0.5175 | 0.7279 | 0.5647 | 0.1351 |
| ruhig_sideways_2000_start6000_transition_repro | voll_fokussiert | 3 | 3 | 3 (1.0000) | 3 (1.0000) | 0 (0.0000) | 1 (0.3333) | 0.1481 | 0.6948 | 0.5120 | 0.1569 |
| expansion_positiv_2000_start2000_transition_repro | voll_fokussiert | 3 | 3 | 3 (1.0000) | 3 (1.0000) | 0 (0.0000) | 1 (0.3333) | 0.1440 | 0.6958 | 0.5111 | 0.1553 |
| xrp2024_2000_start2000_role4_repro | voll_fokussiert | 4 | 6 | 4 (1.0000) | 6 (1.0000) | 0 (0.0000) | 1 (0.2500) | 0.1433 | 0.6954 | 0.5110 | 0.1553 |
| xrp2024_2000_start0_role5_repro | voll_fokussiert | 5 | 10 | 5 (1.0000) | 10 (1.0000) | 0 (0.0000) | 2 (0.4000) | 0.1458 | 0.6955 | 0.5117 | 0.1556 |
| doge2024_2000_start0_role5_repro | voll_fokussiert | 5 | 10 | 5 (1.0000) | 10 (1.0000) | 0 (0.0000) | 2 (0.4000) | 0.1432 | 0.6944 | 0.5111 | 0.1566 |
| doge2024_2000_start8000_role5_repro | voll_fokussiert | 5 | 10 | 5 (1.0000) | 10 (1.0000) | 0 (0.0000) | 2 (0.4000) | 0.1407 | 0.6956 | 0.5111 | 0.1548 |

## Befund

- Voll fokussierte Rekopplung: `8` Fenster.
- Selektiv breite Reorganisation: `1` Fenster.

Die aktuelle Stichprobe zeigt keine lineare Regel nach Fensterlaenge. Rollenbreite allein erklaert die Reaktivierung ebenfalls nicht vollstaendig:

```text
3 Rollen / 3 Kombinationen, 4 Rollen / 6 Kombinationen, 5 Rollen / 10 Kombinationen -> voll fokussierte Rekopplung.
5 Rollen / 10 Kombinationen -> selektive breite Reorganisation.
```

Wichtig ist: 5 Rollen / 10 Kombinationen koennen in realen Fenstern voll rekoppeln. Auch ein synthetisch gedaempftes Randdominanz-Fenster mit 5 Rollen / 10 Kombinationen rekoppelt voll. Das urspruengliche synthetische Rand-/Kippfenster bleibt dagegen bei derselben Rollenbreite selektiv.

Der sichtbare Unterschied liegt daher nicht in Rollenbreite allein und auch nicht in Nachhall allein, sondern im Feldmilieu: Rand-/Kippnaehe, Nachhallstaerke, Co-Touch-Qualitaet und Strain-Verteilung muessen gemeinsam gelesen werden.

## Grenze

Das ist eine kleine Diagnosekarte, kein Beweis. Sie definiert aber eine pruefbare Achse: Weitere Fenster koennen auf Rollenbreite, Strain-Anteil und Reaktivierungsklasse eingetragen werden.

## Wie es weitergeht

Als naechstes sollte die selektive Rand-/Kippwelt gezielt variiert werden: gleiche Rollenbreite, aber veraenderte Randphase, veraenderte Co-Touch-Qualitaet oder veraenderte Strain-Verteilung. Ziel ist zu isolieren, welche Feldmilieu-Komponente die selektive Offline-Reorganisation ausloest.
