# Adaptierte Feldkopplung - Umsetzung

## Anlass

Die Befundlage zur Rezeptoradaptation zeigte fachlich:

```text
Rohfeldaufnahme bleibt Diagnose.
Adaptierte Feldaufnahme ist die eigentliche Aufnahmegrenze vor dem MCM-Feld.
```

Bei der Codepruefung wurde eine Inkonsistenz gefunden:

```text
mcm_feldwirkung.mcm_tension
```

war noch an die rohe Feldaufnahme gekoppelt.

## Korrektur

In `mini_dio/mini_world.py` wurde die Feldkopplung korrigiert:

```text
field_intake_pressure = adapted_field_intake_pressure
```

Damit gilt jetzt:

- `perception_raw_field_intake_pressure` bleibt sichtbare Rohaufnahme.
- `perception_adapted_field_intake_pressure` beschreibt die adaptierte Aufnahme.
- `mcm_feldwirkung.mcm_tension` liest die adaptierte Aufnahme.
- Topologie-/Rollenberichte sollen MCM-Spannung oder adaptierte Aufnahme lesen, nicht Rohaufnahme.

## Nachlauf

BTC/SOL/KAS wurden als 2k-5m-Welten mit aktuellem Stand erneut ausgefuehrt.

Ergebnis:

- Top-Syntax/Familien reproduzieren weiter exakt.
- `field_strained` nimmt gegenueber dem direkten Rohkopplungsstand ab.
- Die MCM-Feldwirkung bleibt lesbar.
- Hochlastfenster bleiben offen/randnaeher, aber ohne Feldkollaps.

## Bedeutung

Das ist eine fachliche Schaerfung der MCM-Mechanik:

```text
Weltspannung darf sichtbar bleiben.
Aber sie darf nicht ungefiltert als Feldspannung gesetzt werden.
```

Damit passt Code und Bauplan besser zusammen.

## Grenze

Aeltere Befunde vor dieser Korrektur bleiben historisch wertvoll, muessen aber bei Feldspannungsfragen vorsichtig gelesen werden, wenn sie Rohfeldaufnahme und MCM-Spannung noch nicht sauber getrennt haben.

Wie es weitergeht: Als naechstes sollten die synthetischen Kontrollwelten mit adaptierter Feldkopplung erneut laufen, damit Harmonie, Bruch/Rand und Randdominanz auf dem korrigierten Mechanikstand verglichen werden.
