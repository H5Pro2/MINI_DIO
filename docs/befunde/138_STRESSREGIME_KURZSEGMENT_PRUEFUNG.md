# Stressregime: Kurzsegment-Prüfung

Stand: 2026-06-18 19:11:05

## Zweck

Diese Diagnose prüft, ob MINI_DIO lokale Last und lokale Ruhe auch innerhalb einer ausdrücklich stressartigen 2025-Welt unterscheiden kann.

Geprüft wurde:

- ein automatisch extrahiertes Stressfenster aus `kontrolliert_2025_stress_10k_5m_SOLUSDT.csv`
- ein automatisch extrahiertes Ruhefenster aus derselben Welt

Die Diagnose ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

## Hierarchie Der Prüfung

1. Grundfrage: Kann MINI_DIO innerhalb einer stressartigen Welt lokale Feldqualitäten trennen?
2. Unterprüfung: Wird das stärkste lokale Stressfenster anders gelesen als das ruhigste lokale Fenster derselben Welt?
3. Folgeschritt: Prüfen, ob diese Trennung auch in weiteren Stress-, Seitwärts- und Expansionswelten erhalten bleibt.

## Rohwelt-Extraktion

Stressfenster:

- Quelle: `kontrolliert_2025_stress_10k_5m_SOLUSDT.csv`
- Bereich: Zeile 7450 bis 7550
- `stress_score`: 2.075993
- `avg_abs_return`: 0.007753
- `avg_range`: 0.013453
- `max_abs_return`: 0.062990
- `max_drawdown`: 0.073845
- `drift`: 0.253191

Ruhefenster:

- Quelle: `kontrolliert_2025_stress_10k_5m_SOLUSDT.csv`
- Bereich: Zeile 3275 bis 3375
- `quiet_score`: 0.335694
- `avg_abs_return`: 0.000981
- `avg_range`: 0.001911
- `max_abs_return`: 0.002670
- `max_drawdown`: 0.018725
- `drift`: -0.004429

## Segmentvergleich

| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| stress_2025_stress | lastnah | 94 | 20 (0.213) | 0.262183 | 0.594327 | 0.329181 | 0.447 | 0.000000 | 0.000000 |
| quiet_2025_stress | ruhenah | 94 | 0 (0.000) | 0.176916 | 0.639352 | 0.378478 | 0.500 | 0.000000 | 0.000000 |

## Befund

MINI_DIO trennt die beiden Fenster derselben Stresswelt deutlich:

- Das Stressfenster wird `lastnah` gelesen.
- Das Ruhefenster wird `ruhenah` gelesen.
- Das Stressfenster schreibt 20 Memory-Episoden.
- Das Ruhefenster schreibt 0 Memory-Episoden.
- Das Stressfenster zeigt höheren Strain und schwächere Rekopplung.
- Das Ruhefenster zeigt niedrigeren Strain, stärkere Rekopplung und höhere Carry-Qualität.

Das ist wichtig, weil beide Segmente aus derselben Oberwelt stammen.
MINI_DIO liest also nicht nur einen globalen Weltcharakter, sondern lokale Feldqualität.

## Interpretation

Die aktuelle Trennung stützt die Annahme:

```text
Innenfeldlast entsteht nicht nur aus der Weltdatei.
Sie entsteht aus lokaler Kopplung zwischen Rohwelt, Sinneswirkung und MCM-Feld.
```

Die stressartige Gesamtwelt enthält lokale Ruhe.
MINI_DIO kann diese Ruhe passiv lesen, ohne sie als Stress-Gegenpol zu behandeln.

Umgekehrt zeigt das Stressfenster keine deutliche Feldzeitspur.
Es ist primär `lastnah`, nicht `last_feldzeitnah`.
Damit bleibt die bisherige Differenzierung erhalten:

- Lastnähe: Belastung ohne starke Wiederkehr/Nachhall-Tiefe.
- Last-Feldzeitnähe: Belastung plus sichtbare Tiefenspur.
- Ruhenähe: niedrige Last, stärkere Rekopplung.
- Ruhig-Feldzeitnähe: Ruhe plus sichtbare Tiefenspur.

## Bedeutung Für MINI_DIO

Für den weiteren Aufbau bedeutet das:

- Feldqualität muss lokal gelesen werden.
- Eine ganze Welt darf nicht pauschal als Stress oder Ruhe behandelt werden.
- Memory-Schreiben ist ein starkes Diagnosezeichen für lokale Last.
- Rekopplung und Strain bleiben zentrale passive Lesesignale.
- Feldzeit muss getrennt von Last/Ruhe gehalten werden.

Das unterstützt die Richtung, MINI_DIO nicht über zusätzliche Lastmodule zu steuern.
Stattdessen wird die Innenfeldreaktion gelesen, verdichtet und später für Regulation nutzbar gemacht.

## Grenze

Diese Diagnose beweist keine universelle Topologie.
Sie zeigt aber, dass innerhalb einer stressartigen Welt lokale Gegenqualitäten lesbar bleiben.

Die Werte sind Arbeitsbefunde, keine Schwellwerte.

## Wie es weitergeht

Als nächstes sollte ein anderes Regime geprüft werden, zum Beispiel Seitwärts- oder Expansionswelt.
Die Hierarchie bleibt:

1. Grundpol: lokale Last, lokale Ruhe oder Mischform?
2. Unterform: mit oder ohne Feldzeitspur?
3. Folgeschritt: bleibt die Trennung bei weiteren Welten stabil oder entsteht eine neue Mischklasse?
