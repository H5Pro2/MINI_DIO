# 1904 - DOGE: geöffnet und verschoben als Randpassung

## Grundfrage

Kehrt `kern_geoeffnet` in weiteren DOGE-Fenstern wieder, und bleibt `kern_verschoben` eine PAXG-Speziallage?

## Prüfung

Die DOGE-1h-Serie wurde auf fünf Folgefenster erweitert:

- `0_1000`
- `1000_2000`
- `2000_3000`
- `3000_4000`
- `4000_5000`

## Ergebnis

```text
d25_1h_0_1000    -> kern_getragen
d25_1h_1000_2000 -> kern_geoeffnet
d25_1h_2000_3000 -> kern_getragen
d25_1h_3000_4000 -> kern_getragen
d25_1h_4000_5000 -> kern_verschoben
```

Die passive Weltpassungs-Memory enthält nach der Aktualisierung:

```text
kern_getragen: 16
kern_ausgeblendet: 9
kern_verschoben: 2
kern_geoeffnet: 1
```

## Lesung

`kern_geoeffnet` kehrt in dieser DOGE-Serie nicht direkt wieder.
Stattdessen taucht später `kern_verschoben` auf.

Damit ist `kern_verschoben` nicht mehr nur eine PAXG-5m-Speziallage.
Es erscheint auch bei DOGE-1h, aber als seltene Randpassungsqualität.

## Bedeutung

Die Randpassung wirkt mehrstufig:

```text
getragen -> geöffnet -> getragen -> getragen -> verschoben
```

Das spricht gegen eine starre Klasse.
Es spricht für eine dynamische Passungsbewegung zwischen Innenkern und Weltlage.

## Mechanischer Befund

MINI_DIOs passive Weltpassungs-Memory trägt nun vier Qualitäten:

- `kern_getragen`
- `kern_geoeffnet`
- `kern_verschoben`
- `kern_ausgeblendet`

Diese Qualitäten beschreiben keine Handlung.
Sie beschreiben, wie eine Weltlage den gereiften lokalen Kern behandelt.

## Wie es weitergeht

Als nächstes sollte diese vierstufige Weltpassung als eigener Mechanikabschnitt zusammengefasst werden, damit die Reifungsbahn nicht nur Befunde sammelt, sondern eine klar lesbare MCM-Feldmechanik daraus ableitet.
