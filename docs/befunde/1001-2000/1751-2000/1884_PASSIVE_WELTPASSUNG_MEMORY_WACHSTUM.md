# 1884 - Passive Weltpassung: Memory-Wachstum über Folgefenster

## Grundfrage

Wächst die passive Weltpassungs-Memory über neue Weltfenster stabil mit, oder ersetzt sie nur eine alte Einzelmessung?

## Umsetzung

Die Weltpassungs-Memory liest jetzt mehrere Messreihen:

- `1878_WELTPASSUNG_METRIK.csv`
- `1883_WELTPASSUNG_MEMORY_WACHSTUM_FOLGEFENSTER.csv`

Die Zeilen werden nach Asset, Bedingung und Zeilentyp dedupliziert. Dadurch bleibt die Memory wachsend, ohne dieselbe Weltlage doppelt zu zählen.

## Ergebnis

Nach der Aktualisierung enthält `world_fit_quality`:

```text
kern_getragen: 12
kern_ausgeblendet: 3
kern_verschoben: 1
```

Vorher enthielt die Memory:

```text
kern_getragen: 9
kern_ausgeblendet: 3
```

## Lesung

Die neue Folgeprüfung bestätigt keine starre Tabelle, sondern eine wachsende Passungskarte:

- BTC, DOGE und XRP bleiben im Folgefenster tragend, aber mit schwächerer Passung als die stärksten Stressfenster.
- PAXG bleibt nicht einfach ausgeblendet, sondern bildet im neuen Folgefenster `kern_verschoben`.
- Damit erscheint eine Zwischenqualität zwischen tragender Weltlage und ausgeblendeter Weltlage.

Das ist wichtig, weil `kern_verschoben` methodisch eine Driftform beschreibt:

```text
Der harte Kern ist nicht weg.
Er wird aber von dieser Weltlage anders getragen.
```

## Mechanische Bedeutung

Die Feldrollen-Memory erhält dadurch keine Steuerung und kein Gate.
Sie erhält eine passivere Erfahrungsschicht:

```text
Welche Weltlagen tragen den Kern?
Welche Weltlagen blenden ihn aus?
Welche Weltlagen verschieben ihn?
```

Damit wird Weltpassung als wachsende Beziehung zwischen Innenkern und Außenwelt gespeichert.
Die Bedeutung liegt nicht im Symbol allein, sondern in der Passung zwischen gereifter Innenordnung und neuer Weltlage.

## Befund

Die Weltpassungs-Memory wächst stabil mit.
Sie erzeugt keine neue harte Regel, sondern erweitert die bisherige Topologie um eine feinere Driftqualität.

Die bisherige Lesung bleibt:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```

Neu ist, dass `verschoben` nun als gespeicherte passive Erfahrung im Memory sichtbar wird.
