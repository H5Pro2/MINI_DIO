# Bewertung 1277 - Achsenspezifische Rezeptorpraeferenz

## Ergebnis

Die Sinnesaufnahme-Memory erzeugt jetzt pro Signatur eine getrennte Rezeptorpraeferenz fuer:

- Hoeren
- Sehen
- Fuehlen

Damit ist Regulation nicht mehr global gedacht.

## Mechanik

Die Praeferenz entsteht aus:

```text
Sinnes-Signatur
-> Feldrolle
-> Tragqualitaet
-> Strain / Rohfeldkontakt
-> achsenspezifische Rezeptorpraeferenz
```

Beispiele aus der aktuellen Memory:

```text
leise_scharf_feldduenn_getragen
-> zentrum_stabil
-> Hoeren hold, Sehen hold, Fuehlen hold
```

```text
laut_unscharf_feldmittel_offen
-> offene_variante
-> Hoeren down, Sehen up, Fuehlen hold
```

```text
laut_unscharf_feldstark_angespannt
-> spannungsrand_kippnaehe
-> Hoeren down, Sehen up, Fuehlen down
```

```text
laut_scharf_feldstark_angespannt
-> spannungsrand_kippnaehe
-> Hoeren down, Sehen soften, Fuehlen down
```

## Fachliche Bedeutung

Mini-DIO bekommt damit kein globales Regulationssignal.

Er bekommt eine getrennte Sinneshaltung:

- Hoeren kann leiser werden, waehrend Sehen schaerfer wird.
- Fuehlen kann Abstand nehmen, waehrend Hoeren unveraendert bleibt.
- Tragende Sinneslagen koennen stabil gehalten werden.

Das verhindert den alten Fehler eines Wahrnehmungsbreis.

## Grenze

Diese Schicht steuert noch nicht aktiv den naechsten Durchlauf.

Sie speichert zunaechst nur eine passive Praeferenz. Der naechste Schritt waere, diese Praeferenz in einem separaten Testlauf als sanfte Rezeptorhaltung vor der Feldaufnahme zu verwenden.

Wichtig:

- keine Handlung
- kein Gate
- keine Richtung
- keine direkte Feldsteuerung

## Schluss

Die Regulation ist jetzt als gelernte Anpassung vorbereitet:

```text
zu hohe Last -> passende Sinnesachse herunterregeln
zu duenne Wahrnehmung -> passende Sinnesachse hochregeln
tragende Wahrnehmung -> Sinneshaltung halten
```

Der entscheidende Punkt ist die Achsentrennung. Mini-DIO lernt nicht "alles runter" oder "alles hoch", sondern welche Sinnesachse bei welcher Feldkonsequenz anders aufgenommen werden sollte.

Wie es weitergeht: Als naechstes sollte diese Rezeptorpraeferenz ueber neue Welten reproduziert und danach in einem isolierten A/B-Lauf als sanfte Rezeptorhaltung getestet werden.
