# Stress-/Quiet-Feldphasen Bewertung

Stand: 2026-07-01

## Grundfrage

Die Grundfrage dieser Pruefung war:

```text
Bleibt die MCM-Feldphasenordnung erhalten,
wenn ruhige und belastete 5m-Weltfenster direkt gegeneinander gelesen werden?
```

Die Unterpruefung nutzte:

- `SOL_QUIET_2024_5M`
- `SOL_STRESS_2024_5M`
- `BTC_QUIET_2024_5M`
- `BTC_STRESS_2024_5M`

## Technische Grenze

Diese Debuglaeufe sind aeltere 4000er Laeufe. Die aktuellen Rezeptorachsen fuer rohe Feldaufnahme und Lautheit sind dort nicht vollstaendig vorhanden. Deshalb sind `avg_raw_field_intake` und `avg_auditory_loudness` in dieser Pruefung nicht als Ursache zu lesen.

Diese Pruefung bewertet daher vor allem:

```text
Feldrollenfolge,
Phasendauer,
Rekopplung,
Strain,
Offen-Rand-Pendelung.
```

## Ergebnis

Die Feldphasenordnung bleibt erhalten.

Direkte Uebergaenge:

```text
Offen -> Rand/Kipp: 807
Rand/Kipp -> Offen: 821
```

Die vier Welten zeigen damit kein neues Rollenmodell. Stattdessen wird die bekannte Pendelbewegung sichtbar:

```text
Offenheit haelt Bewegung.
Rand/Kipp ist kurz.
Rand/Kipp kehrt fast sofort wieder in Offenheit zurueck.
```

## Lesart

In diesen Stress-/Quiet-Fenstern wirkt `offene_variante` nicht wie ein schwacher Zustand, sondern wie ein aktiver Bewegungsraum.

Der Rand ist hier nicht dauerhaft. Er erscheint in kurzen Impulsen und wird wieder in Offenheit zurueckgefuehrt.

Das stuetzt die bisherige Mechanik:

```text
Das MCM-Feld verliert bei Belastung nicht einfach Ordnung.
Es pendelt zwischen Bewegungsraum und Grenzimpuls.
```

## Stress gegen Quiet

Der Unterschied zwischen ruhigen und belasteten Fenstern erzeugt keine neue Feldrolle.

BTC-Stress zeigt etwas mehr Segmentierung und kuerzere Offen-Dauer vor Rand/Kipp. Das spricht fuer staerkere innere Beweglichkeit oder hoehere Fragmentierung, aber nicht fuer Topologiebruch.

SOL-Stress bleibt im Vergleich zu SOL-Quiet sehr nah. Dort veraendert Stress die Phasenordnung weniger stark.

## Bedeutung fuer MINI_DIO

Diese Pruefung ist wichtig, weil sie zeigt:

```text
Die Feldphasenordnung ist nicht nur ein Effekt synthetischer Welten.
Sie bleibt auch bei realen ruhigen und belasteten Weltfenstern sichtbar.
```

Die Topologie wird dadurch nicht als abgeschlossen bewiesen, aber weiter gestuetzt.

## Naechster Schritt

Als naechstes sollten neue Laeufe mit aktueller Rezeptorschicht fuer genau diese Stress-/Quiet-Welten erzeugt werden. Dann kann dieselbe Phasenordnung mit vollstaendiger Rohaufnahme, Hoeren, Sehen und Rezeptorwirkung gelesen werden.

