# Stress-Gegenpol-Diagnose

Stand: 2026-06-18 18:18:45

## Zweck

Diese Diagnose untersucht, welche Rohwelt- und Innenfeldmerkmale den Stress-Gegenpol begleiten.
Sie ist passiv: Sie erzeugt keine Handlung, kein Gate und keine Regel.

Hierarchie der Prüfung:

1. Grundfrage: Warum kippt eine Welt in stärkere innere Verarbeitungslast?
2. Unterprüfung: Welche Abschnitte tragen erhöhte Spannung, Kippnähe und Episodenmemory?
3. Folgeschritt: Prüfen, ob diese Merkmale bei neuen Stresswelten wiederkehren.

## Ergebnisübersicht

### welt_auto_stress_extreme_expansion_test1_01

- Datenwelt: `data\kontrolliert_auto_stress_extreme_expansion_test1_1000_5m_SOLUSDT.csv`
- Debug: `debug\research_chain_auto_stress_extreme_expansion_test1_01`

Top-Stressabschnitte:

- Abschnitt `5` (`396`-`495`): stress_score `0.6161`, stress_ratio `0.343`, tragend_unruhig `0.384`, Rekopplung `0.605`, avg_abs_return `0.0049`, avg_range `0.0094`, Episodenmemory `22`
- Abschnitt `6` (`495`-`594`): stress_score `0.5338`, stress_ratio `0.273`, tragend_unruhig `0.485`, Rekopplung `0.606`, avg_abs_return `0.0039`, avg_range `0.0079`, Episodenmemory `24`
- Abschnitt `1` (`0`-`99`): stress_score `0.4479`, stress_ratio `0.131`, tragend_unruhig `0.364`, Rekopplung `0.626`, avg_abs_return `0.0050`, avg_range `0.0074`, Episodenmemory `2`

## Abschnittsdetails

### welt_auto_stress_extreme_expansion_test1_01

| Abschnitt | Stress | Tragend unruhig | Stabil | Rekopplung | Tragqualität | Roh-Bewegung | Range | Drift | Memory |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.131 | 0.364 | 0.495 | 0.626 | 0.357 | 0.0050 | 0.0074 | 0.114 | 2 |
| 2 | 0.051 | 0.394 | 0.545 | 0.627 | 0.349 | 0.0020 | 0.0045 | 0.005 | 8 |
| 3 | 0.071 | 0.384 | 0.535 | 0.626 | 0.347 | 0.0018 | 0.0040 | 0.003 | 4 |
| 4 | 0.121 | 0.364 | 0.505 | 0.626 | 0.363 | 0.0025 | 0.0056 | 0.066 | 8 |
| 5 | 0.343 | 0.384 | 0.253 | 0.605 | 0.347 | 0.0049 | 0.0094 | 0.075 | 22 |
| 6 | 0.273 | 0.485 | 0.222 | 0.606 | 0.340 | 0.0039 | 0.0079 | 0.081 | 24 |
| 7 | 0.192 | 0.455 | 0.333 | 0.616 | 0.361 | 0.0034 | 0.0072 | -0.014 | 8 |
| 8 | 0.192 | 0.424 | 0.374 | 0.614 | 0.345 | 0.0030 | 0.0060 | -0.013 | 9 |
| 9 | 0.162 | 0.545 | 0.253 | 0.609 | 0.337 | 0.0034 | 0.0064 | -0.007 | 13 |
| 10 | 0.058 | 0.379 | 0.553 | 0.629 | 0.360 | 0.0019 | 0.0044 | 0.000 | 4 |

## Befund

Der Stress-Gegenpol entsteht in den bisherigen Läufen nicht durch ein einzelnes Merkmal.
Er zeigt eine Kopplung aus höherer Rohweltbewegung, größerer Range, erhöhter Kipp-/Spannungswirkung, niedrigerer Rekopplung und mehr Episodenmemory.

Im automatisch extrahierten Stressfenster ist die Belastung nicht gleichmäßig verteilt.
Die stärksten Stressabschnitte liegen in Abschnitt `5` und `6`.
Dort fallen niedrige Rekopplung, hohe Spannung, starke Hearing-/Visual-Gaps, mehr Episodenmemory und weniger stabile Feldwirkung zusammen.
Abschnitt `1` enthält zwar den stärksten Rohweltimpuls, erzeugt aber noch nicht die höchste Innenfeldlast.
Das spricht dafür, dass MINI_DIO Stress nicht nur als Einzelreiz liest, sondern als aufbauende Feldbelastung über Weltkontakt.

Fachlich gelesen heißt das: MINI_DIO reagiert nicht nur auf Bewegung, sondern auf eine Belastungskombination aus Weltunruhe und Innenfeld-Rekopplungsverlust.

Die Diagnose bleibt passiv. Sie beschreibt, welche Abschnitte Last tragen; sie entscheidet nicht, was MINI_DIO tun soll.

## Wie es weitergeht

Als nächstes sollte eine neue Stresswelt gegen diese Abschnittsmerkmale geprüft werden. Entscheidend ist, ob der Stress-Gegenpol wieder aus derselben Kombination entsteht oder ob ein anderer Belastungstyp sichtbar wird.
