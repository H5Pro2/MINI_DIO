# Feldzeit Gegen Feldklassen

Stand: 2026-06-18 18:00:31

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
| Stress-Gegenpol | 2 | 0.000204/0.048696 | 0.004192/0.166667 | 0.0252 | 0.1117 | 0.5367 | 0.0473 | 0.615676 | 0.349893 | 0.222539 |
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

## Befund

Feldzeit ist nicht gleichmäßig über alle Feldklassen verteilt.
Die ruhige Nähegruppe zeigt in den bisherigen Welten die stärkste Wiederkehr und die niedrigste Memorylast.
Der Stress-Gegenpol zeigt dagegen weniger Wiederkehr, niedrigere Rekopplung, höhere Memorylast und höhere Strain-Werte.

Die neu geprüfte Welt `welt_2024_negative_stress_test1_01` ist trotz ihres Dateinamens keine Stress-Gegenpol-Welt.
Sie fällt in die ruhige Nähegruppe: hohe Rekopplung, hohe Tragqualität, niedrige Memorylast und deutliche Wiederkehr.
Das ist ein wichtiger Gegenbefund gegen Namens- oder Erwartungslogik. Entscheidend ist nicht, wie eine Welt benannt ist, sondern welche Innenfeldreaktion MINI_DIO passiv bildet.

Das ist fachlich wichtig: Feldzeit wirkt nicht isoliert. Sie hängt mit der Qualität der Innenfeldlage zusammen.
Eine Lage kann also zeitliche Tiefe bilden, ohne dass sie automatisch tragend wird.

## Interpretation

Die bisherigen Daten sprechen dafür, dass MINI_DIO Feldzeit als Rekopplungsqualität trägt.
In ruhiger Nähe kann Wiederkehr entstehen, ohne viel Memorylast zu erzeugen.
Im Stress-Gegenpol wird weniger Wiederkehr sichtbar, während mehr Episodenmemory geschrieben wird. Das wirkt wie Verarbeitungslast statt ruhiger zeitlicher Tiefe.

Damit wird Feldzeit als organische MCM-Eigenschaft plausibler: Zeit ist nicht nur Reihenfolge, sondern gewirkte Feldnähe, Nachhall und Rekopplung.

## Begrenzung

Der Befund ist noch kein Beweis für eine allgemeine MCM-Topologie.
Er ist ein reproduzierbarer Arbeitsbefund innerhalb der bisher getesteten MINI_DIO-Welten.
Neue Welten können diese Kopplung bestätigen, erweitern oder brechen.

## Wie es weitergeht

Als nächstes sollte eine neue Welt gezielt gegen diese Kopplung geprüft werden.
Konkrete Frage: Bleibt die ruhige Nähegruppe wiederkehrstark und memoryarm, während Stresswelten memorylastiger bleiben?
Wenn ja, wird Feldzeit als Feldklassen-Eigenschaft deutlich belastbarer.
