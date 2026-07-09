# Kalibrierte Rezeptoraufnahme Diagnose

Stand: 2026-07-06

## Fragestellung

Nach `rolling_relative`, `adaptive_relative` und `phase_afterimage_relative` blieb die Frage offen:

```text
Kann eine begrenzte Anfangskalibrierung Rollenbreite erhalten,
ohne das vollstaendige Zukunftsprofil von world_relative zu benutzen?
```

## Umsetzung

Ergaenzt wurde der Sinnesmodus:

```text
calibrated_relative
```

Mechanik:

- MINI_DIO bildet aus einer begrenzten Anfangswelt ein Rezeptorprofil,
- dieses Profil wird als gelebter Rezeptorrahmen fuer den weiteren Lauf genutzt,
- es wird nicht aus der gesamten Welt berechnet,
- es ersetzt keine MCM-Feldregel und erzeugt keine Handlung.

Aktueller Kalibrierhorizont:

```text
DIO_MINI_CALIBRATION_PROFILE_HORIZON = 512
```

## Gepruefte Welten

```text
data/scan_synth-rand-kipp-start0_start250_size1650.csv
data/scan_synth-rand-kipp-start0_start250_size1700.csv
```

## Ergebnis

Beide kalibrierten Laeufe bleiben in der Offline-Rollenbildung bei einer einzigen Rolle:

```text
field_roles = { field_carried: 1 }
sleep_roles_fully_reactivated = 1 / 1
Sleep-Kombinationen = 0
Top-Syntax-Ueberlappung = 1.0
Top-Familien-Ueberlappung = 1.0
```

Gleichzeitig steigt die Oberflaechen-/Syntaxdifferenzierung gegenueber `phase_afterimage_relative`:

```text
1650 calibrated: unique_symbols = 186
1700 calibrated: unique_symbols = 193
```

und es erscheinen lokale Effektklassen:

```text
1650: kippend = 42, tragend_unruhig = 345
1700: kippend = 45, tragend_unruhig = 380
```

## Interpretation

Die kalibrierte Rezeptoraufnahme ist besser als reine Glattung, weil sie wieder mehr Oberflaechenvarianz sichtbar macht.

Sie loest aber das eigentliche Topologieproblem noch nicht:

```text
Syntax und Effektklasse differenzieren,
aber die Offline-Rollenbildung bleibt auf eine Grundrolle verdichtet.
```

Damit entsteht ein klarerer Befund:

```text
Das Problem liegt wahrscheinlich nicht nur in der Sinnesaufnahme,
sondern auch in der Art, wie MCM-Feldepisoden zu Sleep-Rollen verdichtet werden.
```

Moegliche Lesart:

- `world_relative` erzeugt breite Milieu-Rollen, aber mit Ganzweltprofil.
- `fixed`, `rolling`, `adaptive`, `phase_afterimage` und `calibrated` bleiben methodisch sauberer, verdichten aber fuer Sleep zu stark.
- Die Rezeptoraufnahme kann lokale Kippnaehe zeigen, aber die Rollenverdichtung erkennt daraus noch keine getrennten Offline-Rollen.

## Konsequenz

Die naechste Pruefung sollte nicht nur an der Rezeptoraufnahme drehen.

Stattdessen muss die Rollenverdichtung selbst betrachtet werden:

```text
Welche Merkmale machen aus einer MCM-Feldepisode eine eigene Rolle?
```

Wenn `field_carried` zu breit ist, verschluckt es lokale Kipp- und Uebergangszonen. Dann sieht MINI_DIO zwar Unterschiede in Syntax und Effektklasse, aber Sleep/Offline kann sie nicht als getrennte Rollen beruehren.

## Wie es weitergeht

Als naechstes sollte die MCM-Feldepisoden-Verdichtung untersucht werden: `field_carried` muss gegen lokale Kippnaehe, Strain, Nachhall und Rekopplungsqualitaet aufgeteilt werden, ohne daraus harte Regeln oder Handlungsgates zu machen.
