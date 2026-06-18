# Kurzsegment-Leser

Stand: 2026-06-18 21:15:19

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
| expansion_positive | ruhig_feldzeitnah | 994 | 40 (0.040) | 0.178293 | 0.633577 | 0.357946 | 0.435 | 0.016612 | 0.001280 | 0.167 | 0.778 | 1.000 |
| expansion_extreme | last_feldzeitnah | 994 | 86 (0.087) | 0.205616 | 0.623022 | 0.353039 | 0.501 | 0.010096 | 0.000987 | 0.750 | 0.333 | 0.833 |
| quiet_2025_core | ruhenah | 94 | 2 (0.021) | 0.175145 | 0.628376 | 0.345272 | 0.436 | 0.001773 | 0.000662 | 0.167 | 0.889 | 0.667 |
| stress_2025 | lastnah | 94 | 20 (0.213) | 0.262183 | 0.594327 | 0.329181 | 0.447 | 0.000000 | 0.000000 | 0.917 | 0.000 | 0.000 |

## Befund

Die lokalen Stresssegmente werden lastnah gelesen.
Das ruhige Vergleichssegment wird ruhenah gelesen, obwohl ein globaler Feldklassenname es zuvor grob in den Stress-Gegenpol einsortierte.

Das bestätigt die methodische Trennung:

- Vollwelten zeigen Feldklassen über längere Einbettung.
- Kurzsegmente zeigen lokale Feldreaktion.
- Lokale Feldreaktion darf nicht blind wie eine volle Weltklasse gelesen werden.

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

Als nächstes sollte eine zweite ruhige Insel aus einer anderen ruhigen Welt isoliert werden.
Wenn sie wieder ruhenah gelesen wird, wird die Kurzsegment-Lesung belastbarer.
Danach kann geprüft werden, ob Lastnähe und Ruhenähe sich über mehrere Jahre/Welten ähnlich trennen.
