# SYNTH_RAND_KIPP Varianten und Selektivität

Stand: 2026-07-06

## Grundfrage

Ist die selektive Offline-Feld-Reorganisation des ursprünglichen `SYNTH_RAND_KIPP`-Fensters durch Rollenbreite allein erklärbar, oder hängt sie an einem engeren Feldmilieu?

## Unterprüfung

Drei synthetische Varianten wurden erzeugt:

- `RAND_KIPP_SHORT`: kürzere Randphasen.
- `RAND_KIPP_RECOUP`: längere Rekopplungsphasen.
- `RAND_KIPP_SHIFT`: veränderte Phasenordnung.

Alle Varianten wurden passiv über 2000er-Fenster gescannt. Danach wurde der stärkste Übergangskandidat `RAND_KIPP_SHORT start4000` als Real-Sleep-Real-Kette geprüft.

## Befund

Die Varianten erzeugten keine 5-Rollen-Breite mehr. Sie bildeten überwiegend:

- `einzelrekopplung`
- `uebergang_mit_randkontakt`

Der stärkste geprüfte Übergang `RAND_KIPP_SHORT start4000` hatte:

- 3 Rollen
- 3 Sleep-Kombinationen
- 3/3 Rollen reaktiviert
- 3/3 Kombinationen vollständig reaktiviert
- keine selektive Teilreaktivierung

Damit rekoppelt dieser Übergang voll fokussiert.

## Lesung

Die selektive Breite des ursprünglichen `SYNTH_RAND_KIPP start0` ist bisher nicht reproduziert worden, wenn nur Randphasen, Rekopplungslänge oder Phasenordnung grob variiert werden.

Das spricht gegen eine einfache Erklärung:

- nicht nur Rollenbreite
- nicht nur Nachhall
- nicht nur synthetische Herkunft
- nicht nur Randkontakt

Wahrscheinlicher ist eine engere Feldmilieu-Kombination:

- konkrete Rand-/Kippnähe
- Co-Touch-Qualität der Rollen
- Verteilung von `field_carried` und `field_strained`
- Nachhallstärke
- zeitliche Lage der Belastungs- und Rekopplungsphasen

## Grenze

Das ist kein Beweis für eine vollständige Ursache. Es ist aber ein negativer Isolationsbefund: Die bisher getesteten Varianten reichen nicht aus, um die selektive breite Reorganisation des ursprünglichen Fensters nachzubilden.

## Wie es weitergeht

Als nächstes sollte die Originalquelle von `SYNTH_RAND_KIPP start0` feiner zerlegt werden: nicht neue Welten grob bauen, sondern das ursprüngliche 2000er-Fenster segmentweise lesen. Ziel ist zu erkennen, an welcher Binnenstelle die 5-Rollen-Breite und die spätere Selektivität entstehen.
