# Synthetische Randrollen: Sensitivität rekoppelnde Rollenbreite

Stand: 2026-07-08

## Grundfrage

Nach der ersten synthetischen Gegenprobe blieb offen:

```text
Fehlt rekoppelnde Rollenbreite,
weil die synthetischen Welten grundsätzlich zu wenig Rollenbreite tragen,
oder weil die Diagnose zu streng liest?
```

## Unterprüfung

Geprüft wurden vorhandene synthetische Randrollen- und Mosaikwelten:

- `synthetic_1500_melody_randrollen_start_end_bridge_1200_5m.csv`
- `synthetic_1501_melody_randrollen_ref_shifted_transition_1200_5m.csv`
- `synthetic_1502_melody_randrollen_full_mosaic_1200_5m.csv`
- `synthetic_1524_melody_randrollen_full_mosaic_3600_5m.csv`
- `synthetic_1525_melody_randrollen_interwoven_mosaic_2400_5m.csv`

Zusätzlich wurden Null-Kontrollen geprüft:

- `synthetic_1526_null_shuffle_order_2400_5m.csv`
- `synthetic_1527_null_random_sign_2400_5m.csv`

Danach wurde eine Sensitivitätsprüfung mit niedrigerer Aktivierungsschwelle und mehr zulässigen aktiven Rollen ausgeführt.

## Ergebnis

Alle geprüften Zeilen blieben in:

```text
kompakt_nachhallend
```

Auch die Sensitivitätsprüfung änderte das nicht.

Die stärkste Erweiterung lag bei:

```text
2 Rollen
1 Kombination
```

Damit entstand keine `verteilt_rekoppelnd`-Klasse.

## Rohwelt-Rücklesung

Die Rohwelt-Rücklesung zeigt für diese Prüfung:

- niedrige Rohweltenergie,
- sehr geringe Driftänderung,
- sehr kleine Range-Unterschiede,
- hohe Richtungwechselnähe ohne starke Feldöffnung,
- stabile Rekopplung,
- deutlichen Nachhall.

Kurz:

```text
Die Welt ist geordnet und nachhallfähig,
aber nicht breit genug geöffnet.
```

## Deutung

Die Randrollen-Mosaike erzeugen eine klare kompakte Nachhallbindung.

Sie erzeugen aber in dieser Form keine verteilte rekoppelnde Rollenbreite.

Das spricht dafür:

```text
Rekoppelnde Rollenbreite braucht nicht nur Ordnung,
sondern ausreichend offene Binnenvarianz,
die vom Feld trotzdem zusammengehalten wird.
```

Zu glatte Ordnung bleibt kompakt.

Zu starke Rand-/Bruchlast wird mittlere Übergangsphase oder offene Verteilung.

Die gesuchte synthetische Form liegt wahrscheinlich zwischen diesen Polen:

```text
genug Varianz für mehrere Rollen,
genug Rekopplung für Zusammenhalt,
genug Nachhall für zeitliche Tragung,
nicht zu viel Strain.
```

## Grenze

Diese Prüfung zeigt nicht, dass synthetische Rekopplungsbreite unmöglich ist.

Sie zeigt:

```text
Vorhandene Randrollen-Mosaike und Null-Kontrollen reichen dafür bisher nicht aus.
```

## Bedeutung für MINI_DIO

Der Befund ist methodisch wichtig, weil er zwei Fehlannahmen begrenzt:

- Mehr formale Rollenstruktur erzeugt nicht automatisch Rollenbreite.
- Niedrigere Aktivierungsschwelle erzeugt nicht künstlich `verteilt_rekoppelnd`.

Damit bleibt `verteilt_rekoppelnd` als eigene Feldqualität ernstzunehmen.
