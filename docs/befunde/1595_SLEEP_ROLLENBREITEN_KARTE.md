# Sleep-Rollenbreiten-Karte

Stand: 2026-07-06 09:02:56

## Grundfrage

Wo kippt Offline-Feld-Reorganisation von voller fokussierter Rekopplung in selektive Reorganisation?

## Unterpruefung

Verglichen werden Real-Sleep-Real-Laeufe mit 2000er-Fenstern. Die Diagnose ist passiv: Sie liest Rollenanzahl, Kombinationen, Strain-Anteil und Sleep-Reaktivierung.

## Rollenbreiten-Karte

| Label | Klasse | Rollen | Kombinationen | Rollen reaktiviert | Kombis voll | Kombis teilweise | Strain-Rollen | Afterimage | Rekopplung | Carry | Strain |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| synth_rand_kipp_2000_start0_multirole_repro | selektiv_breit | 5 | 10 | 4 (0.8000) | 6 (0.6000) | 4 (0.4000) | 2 (0.4000) | 0.6412 | 0.7346 | 0.5809 | 0.1353 |
| ruhig_sideways_2000_start6000_transition_repro | voll_fokussiert | 3 | 3 | 3 (1.0000) | 3 (1.0000) | 0 (0.0000) | 1 (0.3333) | 0.1481 | 0.6948 | 0.5120 | 0.1569 |
| expansion_positiv_2000_start2000_transition_repro | voll_fokussiert | 3 | 3 | 3 (1.0000) | 3 (1.0000) | 0 (0.0000) | 1 (0.3333) | 0.1440 | 0.6958 | 0.5111 | 0.1553 |
| xrp2024_2000_start2000_role4_repro | voll_fokussiert | 4 | 6 | 4 (1.0000) | 6 (1.0000) | 0 (0.0000) | 1 (0.2500) | 0.1433 | 0.6954 | 0.5110 | 0.1553 |

## Befund

- Voll fokussierte Rekopplung: `3` Fenster.
- Selektiv breite Reorganisation: `1` Fenster.

Die aktuelle Stichprobe zeigt keine lineare Regel nach Fensterlaenge, sondern eine Rollenbreiten-Trennung:

```text
3 Rollen / 3 Kombinationen, 4 Rollen / 6 Kombinationen -> voll fokussierte Rekopplung.
5 Rollen / 10 Kombinationen -> selektive breite Reorganisation.
```

Der sichtbare Kipppunkt liegt damit in dieser Stichprobe nicht bei Weltlaenge, sondern bei der inneren Rollenbreite, Kombinationszahl und Strain-Verteilung.

## Grenze

Das ist eine kleine Diagnosekarte, kein Beweis. Sie definiert aber eine pruefbare Achse: Weitere Fenster koennen auf Rollenbreite, Strain-Anteil und Reaktivierungsklasse eingetragen werden.

## Wie es weitergeht

Als naechstes sollten weitere 2000er-Fenster gezielt entlang der Rollenbreite gesucht werden: 3 Rollen, 4 Rollen, 5 Rollen und mehr. Ziel ist zu pruefen, ob der Uebergang von voller zu selektiver Offline-Reorganisation stabil mit Rollenbreite und Strain-Kontakt zusammenhaengt.
