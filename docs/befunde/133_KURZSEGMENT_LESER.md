# Kurzsegment-Leser

Stand: 2026-06-18 18:36:00

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

## Segmentvergleich

| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall | Load | Calm | Feldzeit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| stress_segment5 | lastnah | 93 | 20 (0.215) | 0.250055 | 0.607085 | 0.351929 | 0.484 | 0.000000 | 0.000000 | 0.500 | 0.444 | 0.000 |
| stress_segment6 | lastnah | 93 | 22 (0.237) | 0.241203 | 0.606419 | 0.339007 | 0.538 | 0.000000 | 0.000000 | 0.750 | 0.333 | 0.167 |
| stress_segment5_6 | feldzeitnah | 192 | 44 (0.229) | 0.246979 | 0.606201 | 0.345029 | 0.521 | 0.001736 | 0.000194 | 0.750 | 0.222 | 0.833 |
| quiet_2025_core | ruhenah | 94 | 2 (0.021) | 0.175145 | 0.628376 | 0.345272 | 0.436 | 0.001773 | 0.000662 | 0.000 | 1.000 | 1.000 |

## Befund

Die lokalen Stresssegmente werden lastnah gelesen.
Das ruhige Vergleichssegment wird ruhenah gelesen, obwohl ein globaler Feldklassenname es zuvor grob in den Stress-Gegenpol einsortierte.
Das kombinierte Stresssegment 5+6 wird feldzeitnah gelesen, trägt aber weiterhin hohe Last.

Das bestätigt die methodische Trennung:

- Vollwelten zeigen Feldklassen über längere Einbettung.
- Kurzsegmente zeigen lokale Feldreaktion.
- Lokale Feldreaktion darf nicht blind wie eine volle Weltklasse gelesen werden.
- Feldzeitnähe bedeutet nicht automatisch Ruhe; sie kann auch als zeitlich eingebettete Belastung auftreten.

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
