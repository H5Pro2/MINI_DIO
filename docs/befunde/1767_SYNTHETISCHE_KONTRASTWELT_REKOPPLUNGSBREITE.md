# Synthetische Kontrastwelt: lokale Übergangsbreite und Glättungsgrenze

Stand: 2026-07-08

## Grundfrage

Nach Befund 1766 war klar:

```text
Formale Binnenstruktur reicht nicht aus,
wenn die Weltwirkung zu gleichmäßig bleibt.
```

Die nächste Frage war deshalb:

```text
Erzeugt ein stärkerer realer Feldkontrast zwischen Öffnung,
Nachhall und Rückbindung eine breitere rekoppelnde Rollenbildung?
```

## Umsetzung

Der synthetische Welt-Builder wurde um das Preset `rekopplungsbreite_kontrast` erweitert.

Dieses Preset enthält:

- eine ruhige Startphase,
- eine klare Öffnung,
- eine offenere Varianzphase,
- eine längere Rekopplungsphase,
- einen unruhigen Nachhall,
- eine zweite Rekopplung,
- eine ruhige Rückbindung.

Die Feldlogik von MINI_DIO wurde dadurch nicht verändert. Geändert wurde nur die kontrollierte Außenwelt.

## Ergebnis

Die 1000er-Fenster zeigten in allen drei Varianten A, B und C am Anfang reproduzierbar:

```text
mittlere_uebergangsphase
3 Rollen
3 Kombinationen
2 Cross-State-Kopplungen
erhöhte adaptive Rekopplung
```

Damit ist die Übergangsbreite aus 1764/1765 nicht zufällig verschwunden. Sie lässt sich durch wirksamen Kontrast erneut lokal erzeugen.

Die breiteren 1500er- und 2000er-Fenster glätteten jedoch wieder vollständig zu:

```text
kompakt_nachhallend
```

Es entstand weiterhin keine `verteilt_rekoppelnd`-Klasse.

## Rohwelt-Rücklesung

Die Rücklesung trennt die beiden Klassen deutlich.

Bei `mittlere_uebergangsphase` lag im Mittel:

- Basis-Energie niedriger als bei den kompakten Phasen,
- Folge-Energie deutlich höher,
- Range der Folgewelt deutlich höher,
- Cross-State-Kopplung aktiv,
- adaptive Rekopplung über der statischen Referenz.

Bei `kompakt_nachhallend` lag im Mittel:

- Rollenbreite bei 1,
- keine Kombinationen,
- keine Cross-State-Kopplung,
- keine adaptive Erfahrungsdifferenz,
- eher fallende oder geglättete Folgeenergie.

Kurz:

```text
Übergangsbreite entsteht hier lokal dort,
wo eine ruhigere Basis in eine stärkere Folge-Weltspannung übergeht.
```

## Deutung

Der Befund ist ein Zwischenschritt.

Stärkerer Feldkontrast erzeugt reproduzierbar eine lokale mittlere Übergangsphase. Diese Phase ist breiter als reine kompakte Nachhallbindung, aber noch nicht breit und getragen genug für `verteilt_rekoppelnd`.

Die längeren Fenster zeigen gleichzeitig eine Grenze:

```text
Zu viel Fensterbreite integriert die lokale Öffnung wieder
in kompakte Nachhallbindung.
```

Damit wird die nächste Bedingung genauer:

- Rollenbreite braucht wirksamen Kontrast.
- Der Kontrast muss lokal genug bleiben, damit er nicht geglättet wird.
- Er muss gleichzeitig lang und tragfähig genug sein, damit mehr als 3 Rollen stabil rekoppeln können.

## Bedeutung für MINI_DIO

MINI_DIO reagiert nicht auf den Namen einer Phase, sondern auf die tatsächlich gewirkte Weltlage.

Die aktuelle Lesung lautet:

```text
Nicht formale Struktur erzeugt Rollenbreite,
sondern wirksamer Kontrast aus Energie, Range, Nachhall und Rückbindung.
```

Das stärkt die methodische Trennung zwischen:

- bloßer synthetischer Konstruktion,
- lokaler Übergangsspannung,
- kompakter Nachhallbindung,
- und echter rekoppelnder Rollenbreite.

## Grenze

Diese Prüfung beweist keine allgemeine MCM-Regel.

Sie zeigt für die geprüften synthetischen Welten:

```text
Kontrast kann mittlere Übergangsbreite reproduzieren,
aber verteilte Rekopplung entsteht daraus noch nicht automatisch.
```

## Wie es weitergeht

Als nächstes sollte nicht einfach mehr Struktur eingebaut werden. Sinnvoller ist eine gezielte Welt, die mehrere lokale Kontrastpakete mit genug Abstand enthält. Ziel ist zu prüfen, ob mehrere getrennte mittlere Übergangsphasen sich später zu rekoppelnder Rollenbreite verbinden oder weiterhin lokal bleiben.
