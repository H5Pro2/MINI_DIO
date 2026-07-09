# Synthetische Binnenvarianz: Grenze der Rekopplungsbreite

Stand: 2026-07-08

## Grundfrage

Die Fokusphase aus Befund 1765 zeigte eine reproduzierbare Vorform rekoppelnder Breite:

```text
3 Rollen
3 Kombinationen
erhöhte adaptive Rekopplung
mittlere Übergangsphase
```

Die nächste Frage war:

```text
Wird daraus verteilte Rekopplungsbreite,
wenn die Zone intern variabler gemacht wird?
```

## Umsetzung

Der synthetische Welt-Builder wurde um das Preset `rekopplungsbreite` erweitert.

Dieses Preset enthält:

- mehrere benannte Öffnungsphasen,
- mehrere benannte Rekopplungsphasen,
- einen weichen Gegenpol,
- einen kurzen Randimpuls,
- eine Nachhallphase.

Wichtig:

```text
Das ist nur eine neue synthetische Außenwelt.
Die Feldlogik von MINI_DIO wurde dadurch nicht verändert.
```

## Ergebnis

Die neuen Binnenvarianz-Welten erzeugten keine `verteilt_rekoppelnd`-Klasse.

Sie erzeugten auch keine stabile mittlere Übergangsphase wie die Fokuszone aus 1765.

Alle geprüften 1000er- und 1500er-Anschlüsse blieben:

```text
kompakt_nachhallend
```

## Rohwelt-Rücklesung

Die Rücklesung zeigt:

- sehr kleine Energieänderung,
- fallende Drift,
- nahezu unveränderte Range,
- hohe Rekopplung,
- hoher Nachhall,
- keine adaptive Erfahrungskopplung.

Kurz:

```text
Die neue Binnenvarianz wurde vom Feld als zu gleichmäßig gebunden gelesen.
```

## Deutung

Der negative Befund ist wichtig.

Mehr interne Unterphasen erzeugen nicht automatisch mehr Rollenbreite.

In dieser Form wurde die Welt nicht breiter, sondern glatter:

```text
mehr Struktur,
aber zu wenig wirksamer Kontrast.
```

Damit wird die erfolgreiche Zone aus 1765 genauer eingegrenzt:

- Sie braucht nicht nur mehrere Öffnungs-/Rekopplungsnamen.
- Sie braucht wirksamen Kontrast zwischen Öffnung und Rückbindung.
- Dieser Kontrast darf aber nicht in harte Randlast kippen.

## Bedeutung für MINI_DIO

MINI_DIO reagiert hier nicht auf formale Benennung der Phasen.

Es reagiert auf die tatsächliche Weltwirkung:

```text
Energie,
Drift,
Range,
Nachhall,
Rekopplung,
lokale Übergangsspannung.
```

Das ist methodisch gut, weil es gegen eine rein symbolische Scheinerklärung spricht.

## Grenze

Diese Prüfung ist ein negativer Zwischenbefund.

Sie zeigt nicht, dass synthetische Rekopplungsbreite unmöglich ist.

Sie zeigt:

```text
Zu gleichmäßig modulierte Binnenvarianz bleibt kompakt.
```
