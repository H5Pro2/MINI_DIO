# Kurzsegment-Leser

Stand: 2026-06-18 18:48:14

## Zweck

Diese Diagnose liest kurze lokale Segmente anders als volle 1000-Zeilen-Welten.
Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

Kurzsegmente haben oft zu wenig Kontext für starke Wiederkehr oder Nachhall.
Deshalb werden sie primär über lokale Feldwirkung gelesen: Memorylast, Strain, Rekopplung und Feldwechsel.

## Hierarchie Der Prüfung

1. Grundfrage: Kann MINI_DIO lokale Ruhe- und Stressinseln unterscheiden?
2. Unterprüfung: Welche Kurzsegmente zeigen Lastnähe, Ruhenähe oder Feldzeitnähe?
3. Folgeschritt: Prüfen, ob diese Kurzlesung über weitere lokale Abschnitte stabil bleibt.

## Methode

Die Lesung nutzt keine absoluten Regeln.
Die Segmente werden relativ zueinander verglichen:

- Lastnähe: mehr Memorylast, mehr Strain, schwächere Rekopplung, mehr Feldwechsel.
- Ruhenähe: weniger Memorylast, weniger Strain, stärkere Rekopplung.
- Feldzeitnähe: Wiederkehr und Nachhall treten sichtbar auf.
- Kombinierte Lesung: Feldzeit kann ruhig oder belastet eingebettet sein.

## Segmentvergleich

| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall | Load | Calm | Feldzeit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| stress_segment5 | lastnah | 93 | 20 (0.215) | 0.250055 | 0.607085 | 0.351929 | 0.484 | 0.000000 | 0.000000 | 0.550 | 0.467 | 0.000 |
| stress_segment6 | lastnah | 93 | 22 (0.237) | 0.241203 | 0.606419 | 0.339007 | 0.538 | 0.000000 | 0.000000 | 0.750 | 0.333 | 0.100 |
| stress_segment5_6 | last_feldzeitnah | 192 | 44 (0.229) | 0.246979 | 0.606201 | 0.345029 | 0.521 | 0.001736 | 0.000194 | 0.700 | 0.333 | 0.800 |
| stress_2023_test4 | lastnah | 94 | 22 (0.234) | 0.269079 | 0.596927 | 0.338154 | 0.468 | 0.000000 | 0.000000 | 0.800 | 0.067 | 0.200 |
| quiet_2025_core | ruhig_feldzeitnah | 94 | 2 (0.021) | 0.175145 | 0.628376 | 0.345272 | 0.436 | 0.001773 | 0.000662 | 0.150 | 0.867 | 0.900 |
| quiet_2026_anchor | ruhig_feldzeitnah | 94 | 4 (0.043) | 0.166449 | 0.639974 | 0.370294 | 0.415 | 0.001773 | 0.000518 | 0.050 | 0.933 | 1.000 |

## Befund

Die zweite lokale Stressinsel bestätigt die Lastseite.
`stress_2023_test4` wird klar `lastnah` gelesen und trägt die stärkste Last im aktuellen Vergleich:

- Memory: 22 von 94 Episoden.
- Strain: 0.269079.
- Rekopplung: 0.596927.
- Calm-Score: 0.067.
- Load-Score: 0.800.

Damit stehen jetzt zwei lokale Ruheinseln und mehrere lokale Stressinseln gegenüber:

- Ruheinseln: `quiet_2025_core`, `quiet_2026_anchor`.
- Stressinseln: `stress_segment5`, `stress_segment6`, `stress_2023_test4`.
- Gemischte Einbettung: `stress_segment5_6` als `last_feldzeitnah`.

Das bestätigt die methodische Trennung:

- Vollwelten zeigen Feldklassen über längere Einbettung.
- Kurzsegmente zeigen lokale Feldreaktion.
- Lokale Feldreaktion darf nicht blind wie eine volle Weltklasse gelesen werden.
- Feldzeit kann in Ruhe oder Last eingebettet sein.
- Lastnähe und Ruhenähe trennen sich vor allem über Memorylast, Strain und Rekopplung.

## Interpretation

Innenfeldlast entsteht in MINI_DIO als Feldwirkung.
Sie muss nicht als eigenes Lastmodul modelliert werden.
Für Kurzsegmente reicht es, die entstehende Feldwirkung zu lesen:

- schreibt das Feld viel Memory?
- steigt Strain?
- sinkt Rekopplung?
- bleibt das Segment trotz kurzer Dauer ruhig und getragen?

Damit wird der organische MCM-Ansatz sauberer:

```text
Nicht: Innenfeldlast programmieren.
Sondern: Innenfeldlast als Feldwirkung lesen.
```

## Begrenzung

Die Lesung ist relativ zur geprüften Segmentgruppe.
Sie ist ein Diagnosewerkzeug, keine universelle Klassifikation.
Weitere ruhige und belastete Kurzsegmente müssen gegengeprüft werden.

## Wie es weitergeht

Als nächstes sollte diese Kurzsegment-Lesung wissenschaftlich verdichtet werden:

1. Welche Wertebereiche unterscheiden lokale Last und lokale Ruhe bisher?
2. Welche Rolle spielt Feldzeit, wenn sie ruhig oder belastet eingebettet ist?
3. Welche Polachsen sind über mehrere Kurzsegmente stabil?

Danach kann ein Report entstehen, der Kurzsegment-Lesung als eigene passive Diagnoseebene beschreibt.
