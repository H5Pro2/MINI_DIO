# Unabhängiges Jahr: Kurzsegment-Prüfung

Stand: 2026-06-18 19:01:35

## Zweck

Diese Diagnose prüft, ob der passive Kurzsegment-Leser außerhalb der bisher verwendeten Segmentwelten belastbar bleibt.

Geprüft wurde ein unabhängiger 2024-Ausschnitt:

- lokales Stressfenster aus `kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- lokales Ruhefenster aus derselben Welt

Die Diagnose ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

## Hierarchie Der Prüfung

1. Grundfrage: Trennt MINI_DIO lokale Last und lokale Ruhe auch in einem unabhängigen Jahr?
2. Unterprüfung: Wie lesen sich ein automatisch extrahiertes Stressfenster und ein automatisch extrahiertes Ruhefenster aus 2024?
3. Folgeschritt: Prüfen, ob weitere unabhängige Jahre neue Mischformen erzeugen oder die bisherigen Arbeitsformen stabilisieren.

## Methode

Die Fenster wurden aus der Rohwelt extrahiert:

- Stressfenster: stärkste lokale Rohweltbelastung nach Bewegung, Range, Drawdown, Volatilität und Richtungswechsel.
- Ruhefenster: schwächste lokale Rohweltbelastung nach denselben Merkmalen.

Danach wurde für beide Fenster die passive Forschungskette ausgeführt und mit den bisherigen Kurzsegmenten verglichen.

Der Kurzsegment-Leser nutzt relative Lesung:

- Lastnähe: mehr Memorylast, mehr Strain, schwächere Rekopplung, mehr Feldwechsel.
- Ruhenähe: weniger Memorylast, weniger Strain, stärkere Rekopplung.
- Feldzeitnähe: Wiederkehr und Nachhall treten sichtbar hinzu.

## Segmentvergleich

| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall | Load | Calm | Feldzeit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| stress_segment5 | lastnah | 93 | 20 (0.215) | 0.250055 | 0.607085 | 0.351929 | 0.484 | 0.000000 | 0.000000 | 0.500 | 0.476 | 0.000 |
| stress_segment6 | lastnah | 93 | 22 (0.237) | 0.241203 | 0.606419 | 0.339007 | 0.538 | 0.000000 | 0.000000 | 0.714 | 0.333 | 0.071 |
| stress_segment5_6 | last_feldzeitnah | 192 | 44 (0.229) | 0.246979 | 0.606201 | 0.345029 | 0.521 | 0.001736 | 0.000194 | 0.643 | 0.381 | 0.786 |
| stress_2023_test4 | lastnah | 94 | 22 (0.234) | 0.269079 | 0.596927 | 0.338154 | 0.468 | 0.000000 | 0.000000 | 0.714 | 0.143 | 0.143 |
| stress_2024_real1 | last_feldzeitnah | 94 | 22 (0.234) | 0.270193 | 0.601652 | 0.356035 | 0.617 | 0.003546 | 0.001599 | 0.929 | 0.095 | 1.000 |
| quiet_2025_core | ruhenah | 94 | 2 (0.021) | 0.175145 | 0.628376 | 0.345272 | 0.436 | 0.001773 | 0.000662 | 0.143 | 0.857 | 0.857 |
| quiet_2026_anchor | ruhenah | 94 | 4 (0.043) | 0.166449 | 0.639974 | 0.370294 | 0.415 | 0.001773 | 0.000518 | 0.036 | 0.952 | 0.929 |
| quiet_2024_real1 | ruhenah | 94 | 4 (0.043) | 0.189680 | 0.630744 | 0.362024 | 0.500 | 0.000000 | 0.000000 | 0.321 | 0.762 | 0.214 |

## Befund

Das unabhängige 2024-Jahr bestätigt die Trennung der Kurzsegment-Lesung.

- Das 2024-Stressfenster wird nicht ruhig gelesen, sondern `last_feldzeitnah`.
- Das 2024-Ruhefenster wird ruhenah gelesen.
- Die Stressseite zeigt hohe Memorylast, hohen Strain, schwächere Rekopplung und mehr Feldwechsel.
- Die Ruheseite zeigt niedrige Memorylast, niedrigeren Strain und stärkere Rekopplung.

Der wichtige Punkt ist die Zusatzqualität des 2024-Stressfensters:

```text
stress_2024_real1 ist nicht nur lastnah.
Es trägt zusätzlich Feldzeitspur.
```

Das spricht dafür, dass lokale Last und Feldzeit nicht dasselbe sind.
Ein belasteter Bereich kann bereits Wiederkehr/Nachhall ausbilden, ohne dadurch ruhig zu werden.

## Interpretation

Die bisherige Arbeitsthese wird belastbarer:

```text
Lokale Last ist eine Feldwirkung.
Lokale Ruhe ist eine Feldwirkung.
Feldzeit ist eine zusätzliche Tiefenspur, kein automatisches Ruhesignal.
```

Damit wird die passive MCM-Lesung präziser:

- Kurzsegmente dürfen nicht über einen einzelnen globalen Klassennamen gelesen werden.
- Das Feld zeigt unterschiedliche Qualitäten gleichzeitig.
- Last kann feldzeitnah werden, wenn Wiederkehr und Nachhall sichtbar werden.
- Ruhe kann feldzeitnah werden, wenn niedrige Last mit stabilerer Rekopplung zusammenliegt.

## Grenze

Diese Prüfung ist noch kein Beweis einer universellen MCM-Topologie.
Sie ist aber ein unabhängiger Gegencheck: Die bisherige Kurzsegment-Trennung kollabiert nicht, wenn ein anderes Jahr verwendet wird.

Die Werte sind Arbeitsbefunde, keine Schwellwerte.

## Wie es weitergeht

Als nächstes sollte ein weiteres unabhängiges Jahr oder ein anderes Marktregime geprüft werden.
Ziel ist nicht, immer dieselben Namen zu erzwingen, sondern zu sehen, ob MINI_DIO lokale Last, lokale Ruhe und Feldzeitspur weiter getrennt lesen kann.
Wenn neue Mischformen entstehen, müssen sie hierarchisch eingeordnet werden: Grundpol, Unterform, danach mögliche Folgeschritte.
