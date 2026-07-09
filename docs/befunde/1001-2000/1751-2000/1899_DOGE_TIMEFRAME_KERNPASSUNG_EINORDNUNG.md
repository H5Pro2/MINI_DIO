# 1899 - DOGE-Timeframe: Einordnung der Kernpassung

## Grundfrage

Taucht `kern_verschoben` auch bei einem anderen fragilen Asset auf, oder zeigt ein anderes Asset eine andere Randpassungsqualität?

## Prüfung

DOGE wurde im 1h-Timeframe über drei 2025-Folgefenster geprüft:

- `0_1000`
- `1000_2000`
- `2000_3000`

Alle Fenster wurden passiv gegen den harten lokalen Reifekern gelesen.

## Ergebnis

```text
d25_1h_0_1000    -> kern_getragen
d25_1h_1000_2000 -> kern_geoeffnet
d25_1h_2000_3000 -> kern_getragen
```

Die passive Weltpassungs-Memory enthält nach der Aktualisierung:

```text
kern_getragen: 15
kern_ausgeblendet: 9
kern_verschoben: 1
kern_geoeffnet: 1
```

## Lesung

DOGE wiederholt nicht die PAXG-Lesung.
Statt `kern_verschoben` entsteht hier einmal `kern_geoeffnet`.

Das bedeutet:

```text
Der Kern bleibt sichtbar.
Er verliert aber lokale Schärfe und öffnet sich stärker.
```

PAXG-1h tendierte stärker zu Ausblendung.
DOGE-1h bleibt dagegen überwiegend tragend und zeigt eine offene Zwischenlage.

## Bedeutung für das MCM-Feld

Damit wird die Weltpassung feiner:

- `kern_getragen`: Kern bleibt in dieser Weltlage tragfähig.
- `kern_geoeffnet`: Kern bleibt sichtbar, verliert aber Schärfe.
- `kern_verschoben`: Kern bleibt anschlussfähig, wird aber anders getragen.
- `kern_ausgeblendet`: Kernpaare verschwinden stark.

Das spricht für Randpassung als mehrstufige Beziehung, nicht als einfache Ja/Nein-Stabilität.

## Befund

`kern_verschoben` bleibt bisher selten.
Die DOGE-Prüfung zeigt aber, dass andere Assets eigene Zwischenqualitäten ausbilden können.

Damit wird die passive Weltpassungs-Memory nicht nur größer, sondern differenzierter.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob `kern_geoeffnet` bei DOGE-Folgefenstern wiederkehrt oder ob es ebenfalls nur eine einzelne Übergangslage war.
