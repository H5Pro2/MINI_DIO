# Feldzeit Gegen Feldklassen

Stand: 2026-06-18 18:26:00

## Zweck

Diese Diagnose prüft, ob Feldzeit-Spuren je nach Feldklasse unterschiedlich auftreten.
Sie verbindet die Feldklassen-Diagnose mit der Feldzeit-Diagnose.
Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

Hierarchie der Prüfung:

1. Grundfrage: Hängt Feldzeit mit der Feldklasse zusammen?
2. Unterprüfung: Welche Klassen tragen mehr Nachhall, Wiederkehr, Memorylast oder Übergänge?
3. Folgeschritt: Prüfen, ob neue Welten dieselbe Kopplung zeigen oder eine neue Klasse bilden.

## Klassenvergleich

| Feldklasse | Welten | Nachhall avg/max | Wiederkehr avg/max | Return-Quote | Memory-Quote | Feldwechsel/Episode | Zeitwechsel/Episode | Rekopplung | Tragqualität | Strain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Stress-Gegenpol | 7 | 0.000220/0.062222 | 0.002483/0.285714 | 0.0246 | 0.1193 | 0.5223 | 0.0457 | 0.613985 | 0.347384 | 0.225046 |
| angespannte Übergangsgruppe | 2 | 0.000669/0.140818 | 0.007767/0.375000 | 0.0407 | 0.0835 | 0.5136 | 0.0749 | 0.622659 | 0.355565 | 0.207785 |
| ruhige Nähegruppe | 5 | 0.001189/0.137834 | 0.015793/0.444444 | 0.0835 | 0.0358 | 0.4549 | 0.1443 | 0.633312 | 0.362069 | 0.180232 |

## Einzelwelten

| Welt | Feldklasse | Nachhall avg/max | Wiederkehr avg/max | Memory | Feldwechsel | Zeitwechsel | Rekopplung | Tragqualität | Strain |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| welt_2023_01 | angespannte Übergangsgruppe | 0.000987/0.140818 | 0.010096/0.375000 | 86 | 498 | 91 | 0.623022 | 0.353039 | 0.205616 |
| welt_2024_01 | angespannte Übergangsgruppe | 0.000351/0.126000 | 0.005437/0.285714 | 80 | 523 | 58 | 0.622297 | 0.358091 | 0.209955 |
| welt_2025_core_01 | ruhige Nähegruppe | 0.001361/0.126000 | 0.014893/0.375000 | 24 | 434 | 134 | 0.633885 | 0.361269 | 0.177359 |
| welt_2025_mid_shift_01 | ruhige Nähegruppe | 0.001230/0.136506 | 0.013849/0.444444 | 56 | 465 | 119 | 0.630490 | 0.359369 | 0.186445 |
| welt_2025_late_shift_01 | ruhige Nähegruppe | 0.000625/0.062222 | 0.013504/0.375000 | 20 | 461 | 138 | 0.633999 | 0.361895 | 0.178473 |
| welt_2023_stress_01 | Stress-Gegenpol | 0.000274/0.048696 | 0.004527/0.166667 | 106 | 515 | 50 | 0.614985 | 0.346134 | 0.222566 |
| welt_2024_bridge3_01 | Stress-Gegenpol | 0.000134/0.035000 | 0.003856/0.166667 | 116 | 552 | 44 | 0.616367 | 0.353651 | 0.222512 |
| welt_2026_anchor_followup1_01 | ruhige Nähegruppe | 0.001606/0.137834 | 0.023313/0.375000 | 46 | 428 | 196 | 0.636513 | 0.366169 | 0.173652 |
| welt_2024_negative_stress_test1_01 | ruhige Nähegruppe | 0.001123/0.129211 | 0.013408/0.375000 | 32 | 473 | 130 | 0.631676 | 0.361644 | 0.185230 |
| welt_auto_stress_extreme_expansion_test1_01 | Stress-Gegenpol | 0.000278/0.058947 | 0.005485/0.285714 | 102 | 501 | 60 | 0.618465 | 0.350669 | 0.216865 |
| welt_auto_stress_segment5_01 | Stress-Gegenpol | 0.000000/0.000000 | 0.000000/0.000000 | 20 | 45 | 0 | 0.607085 | 0.351929 | 0.250055 |
| welt_auto_stress_segment6_01 | Stress-Gegenpol | 0.000000/0.000000 | 0.000000/0.000000 | 22 | 50 | 0 | 0.606419 | 0.339007 | 0.241203 |
| welt_auto_stress_segment5_6_01 | Stress-Gegenpol | 0.000194/0.020364 | 0.001736/0.166667 | 44 | 100 | 2 | 0.606201 | 0.345029 | 0.246979 |
| welt_quiet_segment_2025_core_01 | Stress-Gegenpol | 0.000662/0.062222 | 0.001773/0.166667 | 2 | 41 | 2 | 0.628376 | 0.345272 | 0.175145 |

## Befund

Feldzeit ist nicht gleichmäßig über alle Feldklassen verteilt.
Die ruhige Nähegruppe zeigt in den bisherigen Welten die stärkste Wiederkehr und die niedrigste Memorylast.
Der Stress-Gegenpol zeigt dagegen weniger Wiederkehr, niedrigere Rekopplung, höhere Memorylast und höhere Strain-Werte.

Das ist fachlich wichtig: Feldzeit wirkt nicht isoliert. Sie hängt mit der Qualität der Innenfeldlage zusammen.
Eine Lage kann also zeitliche Tiefe bilden, ohne dass sie automatisch tragend wird.

Der lokale Ruhetest zeigt eine methodische Grenze der bisherigen Feldklassen-Auswertung:

- `welt_quiet_segment_2025_core_01` wird formal als Stress-Gegenpol einsortiert.
- Die Einzelwerte sprechen aber nicht für Stresslast: Memory liegt bei 2, Strain bei 0.175145 und Rekopplung bei 0.628376.
- Das unterscheidet die Ruheinsel deutlich von den lokalen Stresssegmenten, die Memory 20/22/44, Strain 0.241-0.250 und Rekopplung 0.606-0.607 zeigen.

Damit darf die Klassenbezeichnung bei kurzen Segmenten nicht isoliert gelesen werden.
Für Kurzabschnitte sind Memorylast, Strain und Rekopplung belastbarer als der globale Klassenname.

## Interpretation

Die bisherigen Daten sprechen dafür, dass MINI_DIO Feldzeit als Rekopplungsqualität trägt.
In ruhiger Nähe kann Wiederkehr entstehen, ohne viel Memorylast zu erzeugen.
Im Stress-Gegenpol wird weniger Wiederkehr sichtbar, während mehr Episodenmemory geschrieben wird. Das wirkt wie Verarbeitungslast statt ruhiger zeitlicher Tiefe.

Damit wird Feldzeit als organische MCM-Eigenschaft plausibler: Zeit ist nicht nur Reihenfolge, sondern gewirkte Feldnähe, Nachhall und Rekopplung.

Die lokale Ruheinsel bestätigt die Gegenseite der Stressinsel:

1. Stresssegmente: hohe lokale Last, schwächere Rekopplung, hohe Memory-Schreibung.
2. Ruhesegment: niedrige Memory-Schreibung, bessere Rekopplung, niedriger Strain.

Der Unterschied entsteht also nicht nur durch Rohwelt-Stress, sondern durch die Art, wie MINI_DIO diese Weltlage im Innenfeld verarbeitet.
Das stärkt die Arbeitsthese, dass das Feld keine bloße Messwertliste ist, sondern eine passive Innenfeldreaktion bildet.

## Begrenzung

Der Befund ist noch kein Beweis für eine allgemeine MCM-Topologie.
Er ist ein reproduzierbarer Arbeitsbefund innerhalb der bisher getesteten MINI_DIO-Welten.
Neue Welten können diese Kopplung bestätigen, erweitern oder brechen.

## Wie es weitergeht

Als nächstes sollte das Feldklassen-Werkzeug für Kurzsegmente erweitert werden.
Konkrete Frage: Brauchen lokale Segmente eine eigene Kurzsegment-Klasse, die Memorylast, Strain und Rekopplung stärker gewichtet als Wiederkehr und Nachhall?
Danach kann eine zweite ruhige Insel aus einer anderen ruhigen Welt gegengeprüft werden.
