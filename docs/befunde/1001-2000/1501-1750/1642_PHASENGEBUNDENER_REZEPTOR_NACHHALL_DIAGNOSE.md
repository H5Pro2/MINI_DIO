# Phasengebundener Rezeptor-Nachhall Diagnose

Stand: 2026-07-06

## Fragestellung

Nach der Rand-Kipp-Pruefung entstand ein Methodenproblem:

```text
world_relative liest die Rollenbreite gut,
ist aber nicht streng kausal.

fixed, rolling_relative und adaptive_relative sind kausaler,
verlieren aber die Rollenbreite.
```

Die naechste Pruefung war deshalb:

```text
Kann ein phasengebundener Rezeptor-Nachhall
kausal bleiben und trotzdem Rollenbreite erhalten?
```

## Umsetzung

Ergaenzt wurde der neue Sinnesmodus:

```text
phase_afterimage_relative
```

Mechanik:

- aktuelle Sinnesaufnahme bleibt kausal,
- die adaptive Rezeptor-Skalierung nutzt nur vergangene und aktuelle Daten,
- fruehere Sinnesphasen werden als schwacher Nachhall auf `sehen` und `hoeren` gemischt,
- danach wird die MCM-Feldwirkung neu aus den gemischten Sinnesachsen berechnet,
- der Nachhall steuert keine Handlung, kein Gate und keine Richtung.

Die MCM-Feldregeln selbst wurden nicht veraendert.

## Gepruefte Welten

```text
data/scan_synth-rand-kipp-start0_start250_size1650.csv
data/scan_synth-rand-kipp-start0_start250_size1700.csv
```

Beide wurden als Real-Sleep-Real-Kette mit gleicher Follow-Welt geprueft.

## Ergebnis

Beide Laeufe kollabierten auf eine einzige Feldrolle:

```text
field_roles = { field_carried: 1 }
sleep_roles_fully_reactivated = 1 / 1
Sleep-Kombinationen = 0
Top-Syntax-Ueberlappung = 1.0
Top-Familien-Ueberlappung = 1.0
```

Der Nachhall erzeugt also stabile Wiederholung, aber keine Rollenbreite.

## Interpretation

Der Test ist fachlich negativ fuer die eigentliche Zielannahme:

```text
Phasennachhall allein stellt die Topologie nicht wieder her.
```

Die Ursache liegt wahrscheinlich nicht im Fehlen von Nachhall, sondern davor:

```text
Die kausale Rezeptor-Normierung glaettet die Welt so stark,
dass die Rand-/Bruecken-/Zentrumsrollen nicht mehr getrennt sichtbar werden.
```

Damit ist der Befund wichtig:

- Nachhall kann vorhandene Sinnesphasen forttragen.
- Er kann aber keine Topologie retten, wenn die Rezeptoraufnahme vorher zu einheitlich wird.
- Die MCM-Topologie braucht offenbar nicht nur Zeitrest, sondern ausreichende rezeptorische Kontrastbildung.

## Konsequenz

Die naechste sinnvolle Richtung ist keine staerkere Nachhall-Mischung, sondern eine sauberere Rezeptor-Kalibrierung:

```text
lokal kausal genug,
aber nicht so stark geglaettet,
dass alle Rollen zu field_carried werden.
```

Moegliche naechste Pruefung:

```text
calibrated_relative
```

Dabei wuerde MINI_DIO eine Anfangsphase als eigene Weltkalibrierung nutzen und danach mit dieser gelebten Kalibrierung weiter lesen. Das waere kausaler als `world_relative`, aber weniger kurzatmig als `rolling_relative` oder `adaptive_relative`.

## Forschungsgrenze

Dieser Befund beweist nicht, dass `world_relative` falsch ist. Er zeigt nur:

```text
world_relative ist fuer Topologie-Lesung stark,
aber methodisch wegen Ganzwelt-Profil nicht streng kausal.

phase_afterimage_relative ist kausaler,
aber fuer Rollenbreite derzeit zu glatt.
```

## Wie es weitergeht

Als naechstes sollte eine kalibrierte Rezeptoraufnahme geprueft werden: MINI_DIO liest eine begrenzte Anfangswelt als Kalibrierung und nutzt diese danach als gelebten Rezeptorrahmen. Ziel ist Rollenbreite ohne Ganzwelt-Zukunftsblick.
