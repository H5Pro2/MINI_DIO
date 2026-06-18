# Sideways 2k-Skalierung Als Feldbefund

Stand: 2026-06-18

## Zweck

Diese Datei dokumentiert die Skalierung der belasteten Seitwaertswelt von 1000 auf 2000 Kerzen.

Geprueft wurde:

```text
data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv
data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv
```

Die Grundfrage war:

```text
Bleibt die belastete Seitwaertslage stabil,
oder entsteht bei laengerer Weltzeit eine neue Feldklasse?
```

## Ergebnis

Die Klasse bleibt erhalten.

```text
sideways_2026_1k -> Stress-Gegenpol
sideways_2026_2k -> Stress-Gegenpol
```

Gleichzeitig veraendert sich die innere Verteilung:

```text
Rekopplung steigt von 0.615214 auf 0.622030.
Tragqualitaet steigt von 0.351964 auf 0.355412.
Memory steigt von 117 auf 175.
Strain/Kippung steigt absolut von 192 auf 271, relativ aber weniger stark.
```

## Vergleich

| Welt | Kerzen | Feldklasse | Rekopplung | Tragqualitaet | Strain/Kippung | Memory | Dominante Wirkung |
|---|---:|---|---:|---:|---:|---:|---|
| sideways_2026_1k | 1000 | Stress-Gegenpol | 0.615214 | 0.351964 | 192 | 117 | tragend_unruhig |
| sideways_2026_2k | 2000 | Stress-Gegenpol | 0.622030 | 0.355412 | 271 | 175 | tragend_unruhig |

## Interpretation

Die 2k-Erweiterung fuehrt nicht zu einem Kollaps.

Sie zeigt eher:

```text
Das Feld bleibt belastet,
aber es organisiert mehr stabile Gegenanteile in die gleiche Welt hinein.
```

Bei 1000 Kerzen war die Welt klar stressnah.

Bei 2000 Kerzen bleibt sie stressnah, aber weniger eng:

```text
stabil: 821
tragend_unruhig: 854
```

Das ist fast eine geteilte Feldlage.

Die belastete Seitwaertswelt wird dadurch nicht widerlegt, sondern differenziert:

```text
Sie ist kein reiner Stressblock.
Sie ist eine lange getragene, aber unruhige Feldspannung.
```

## Feldzeit

Die Feldzeit bleibt ueberwiegend:

```text
temporal_first_contact
```

1k:

```text
temporal_first_contact: 966
temporal_far_return: 27
```

2k:

```text
temporal_first_contact: 1867
temporal_far_return: 126
```

Die Rueckkehranteile wachsen mit der Weltzeit, bleiben aber nicht dominant.

Das bedeutet:

```text
Die Welt bekommt mehr Tiefe,
aber noch keine starke Feldzeitbindung.
```

## Forschungswert

Dieser Lauf zeigt:

```text
Laengere Weltzeit erzeugt nicht automatisch neue Bedeutung.
Sie kann eine vorhandene Bedeutung verbreitern.
```

Die MCM-Feldordnung wirkt dadurch nicht starr.

Sie verhaelt sich eher wie eine Spannungsfamilie:

```text
ein Kern bleibt,
die Randanteile reorganisieren sich.
```

## Wie Es Weitergeht

Als naechstes sollte eine negative Welt auf 2000 Kerzen skaliert werden.

Hierarchie:

1. Grundfrage: Bleibt negative Bewegung auch bei laengerer Weltzeit getragen?
2. Unterpruefung: Waechst dort ebenfalls Feldzeit, ohne dass Stress-Gegenpol entsteht?
3. Folgeschritt: Wenn ja, wird die Unterscheidung staerker: Nicht Richtung, sondern Feldbelastbarkeit ordnet die MCM-Topologie.
