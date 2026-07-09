# 1889 - PAXG-Kernverschiebung: Einordnung über Folgefenster

## Grundfrage

War `kern_verschoben` eine stabile neue Weltpassungsgruppe oder eine einzelne Übergangslage?

## Prüfung

Nach dem ersten PAXG-Folgefenster `5000_6000` wurden drei weitere PAXG-Fenster geprüft:

- `6000_7000`
- `7000_8000`
- `8000_9000`

Alle Fenster wurden passiv gegen den harten lokalen Reifekern gelesen.

## Ergebnis

```text
follow5000_6000 -> kern_verschoben
follow6000_7000 -> kern_ausgeblendet
follow7000_8000 -> kern_ausgeblendet
follow8000_9000 -> kern_getragen
```

Die passive Weltpassungs-Memory enthält nach der Erweiterung:

```text
kern_getragen: 13
kern_ausgeblendet: 5
kern_verschoben: 1
```

## Lesung

`kern_verschoben` ist in dieser Prüfung keine stabile neue Hauptklasse.
Es wirkt eher wie eine Übergangslage innerhalb einer PAXG-Randzone:

```text
getragen -> verschoben -> ausgeblendet -> getragen
```

Das ist methodisch wichtig.
Die Weltpassung verhält sich nicht wie eine feste Symboltabelle.
Sie zeigt eine wechselnde Beziehung zwischen Innenkern und Weltlage.

## Bedeutung für das MCM-Feld

PAXG bleibt der aktuell beste Testfall für fragile Weltpassung.
Der Kern ist dort nicht dauerhaft verloren, aber auch nicht dauerhaft sauber getragen.

Damit entsteht eine feinere Lesung:

- `kern_getragen`: Weltlage trägt den lokalen Reifekern.
- `kern_ausgeblendet`: Weltlage lässt viele Kernpaare verschwinden.
- `kern_verschoben`: Kern bleibt teilweise anschlussfähig, wird aber anders getragen.

Diese Zwischenqualität ist passiv.
Sie ist keine Handlung, kein Gate und keine Richtung.

## Befund

Die Erweiterung stärkt die Annahme einer dynamischen Weltpassung:

```text
Innenkern und Außenwelt bilden keine starre Kopie.
Sie bilden eine wechselnde Passungsbeziehung.
```

PAXG zeigt dabei besonders deutlich Randdrift, Ausblendung und erneute Tragfähigkeit.
