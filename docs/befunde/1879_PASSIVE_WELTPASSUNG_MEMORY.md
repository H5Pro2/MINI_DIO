# 1879 - Passive Weltpassung in der Feldrollen-Memory

## Grundfrage

Kann die Weltpassungs-Metrik als passive Erfahrungsqualität in die Feldrollen-Memory übernommen werden?

## Umsetzung

Die Feldrollen-Memory wurde um `world_fit_quality` erweitert.

Diese Struktur speichert pro Weltlage:

- Asset
- Weltlage / Bedingung
- Anzahl der Kernpaare
- getragene Kernpaare
- geöffnete Kernpaare
- verschobene Kernpaare
- ausgeblendete Kernpaare
- Weltpassungs-Score
- passive Lesung der Weltpassung

## Ergebnis

Aktueller Zähler:

```text
kern_getragen: 9
kern_ausgeblendet: 3
```

## Lesung

Die Erweiterung bleibt vollständig passiv.
Sie entscheidet keine Handlung, keine Richtung und kein Gate.

Ihre Funktion ist Erfahrung:

```text
Welche Weltlagen tragen den harten Kern?
Welche Weltlagen öffnen ihn?
Welche Weltlagen verschieben ihn?
Welche Weltlagen blenden ihn aus?
```

Damit wird Reife als Beziehung zwischen Innenkern und Außenwelt speicherbar.
Das ist fachlich wichtig, weil der Hartkern nicht als absolute Tabelle behandelt wird.
Eine Weltlage kann denselben Kern tragen, öffnen, verschieben oder ausblenden.

## Mechanische Bedeutung

MINI_DIO erhält damit keine neue Steuerung, sondern eine tiefere passive Innenkarte:

```text
Feldrolle
  -> Familien-Anschlussqualität
  -> lokale Phasenreife
  -> harter Kern
  -> Weltpassung
```

Die Weltpassung ist die erste explizite Speicherform für die Frage:

```text
Passt diese Außenwelt zu meinem gereiften Innenkern?
```

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Weltpassungs-Memory über neue Weltfenster stabil mitwächst oder ob sie neue Weltlagen als eigene Passungsgruppen bildet.
