# Befund 2012 - Positive Feldphasen-Signatur und Reproduktion

Stand: 2026-07-09

## Frage

Befund 2009 isolierte aus der positiven Mixed-Binding-Reifung eine Feldphasen-Signatur:

```text
hohe Rekopplung,
mittleres Carry,
niedrige Strain-Werte,
niedrige Feldspannung,
niedrige Hörlücke,
stabile Wirkung,
hohe sensorische Kopplung.
```

Diese Prüfung fragt:

```text
Taucht diese Feldphasenqualität auch in anderen Welten wieder auf,
oder war sie nur an die ursprünglichen Symbolnamen gebunden?
```

## Umsetzung

Neu angelegt wurde:

```text
tools/report_mixed_binding_field_phase_signature.py
```

Das Tool berechnet die Signatur aus den tatsächlich getroffenen Rollen aus:

```text
docs/befunde/2001-3000/2009_MIXED_BINDING_POSITIVE_ZIELWELT_RAW_PHASE.csv
```

Danach sucht es passiv nach Feldphasen-Nähe in Debugläufen.

Wichtig:

```text
Das ist keine Handlung.
Das ist kein Gate.
Das ist keine feste Regel.
```

Die Signatur ist eine passive Messform für wiederkehrende Feldqualität.

## Geprüfte Reports

```text
docs/befunde/2001-3000/2010_POSITIVE_MIXED_BINDING_SIGNATURE_TARGET_WORLDS.md
docs/befunde/2001-3000/2011_POSITIVE_MIXED_BINDING_SIGNATURE_COUNTER_WORLDS.md
```

## Ergebnis

In den ursprünglichen Zielwelten:

```text
Episoden mit Signaturnähe: 20976
starke Episoden >=0.90: 9131
sehr starke Episoden >=0.95: 2330
sehr starke Preview-Symbole >=0.95: 36
```

In den getrennten Gegenwelten:

```text
Episoden mit Signaturnähe: 11964
starke Episoden >=0.90: 4784
sehr starke Episoden >=0.95: 1215
sehr starke Preview-Symbole >=0.95: 31
```

Vollständiger Symbolvergleich:

```text
>=0.95:
Zielwelten: 36 Symbole
Gegenwelten: 31 Symbole
gemeinsam: 24 Symbole
Jaccard: 0.5581

>=0.90:
Zielwelten: 69 Symbole
Gegenwelten: 62 Symbole
gemeinsam: 47 Symbole
Jaccard: 0.5595

>=0.85:
Zielwelten: 94 Symbole
Gegenwelten: 78 Symbole
gemeinsam: 60 Symbole
Jaccard: 0.5357
```

## Lesung

Die positive Feldphase ist nicht nur ein einzelner Symbolname.

Sie erscheint als wiedererkennbare Feldqualität:

```text
gleiche Nähequalität,
teilweise andere Symbolträger,
stabile Überschneidung über unterschiedliche Welten.
```

Das erklärt die scheinbare Spannung zwischen Befund 2008 und Befund 2009:

```text
Die alten mixed_binding-Symbole reiften in den Gegenproben nicht erneut.
Aber die zugrunde liegende positive Feldphase tauchte durchaus wieder auf.
```

Damit trennt MINI_DIO zwei Ebenen:

```text
1. Symbolbindung:
   Welche konkrete Rolle wird erneut berührt?

2. Feldphasenbindung:
   Welche innere Qualität taucht unabhängig vom konkreten Symbol wieder auf?
```

## Bedeutung

Das ist wichtig für die weitere Entwicklung, weil MINI_DIO damit nicht nur Namen wiedererkennt.

Das Feld kann eine Qualität wiederfinden, auch wenn sie in anderen Trägerrollen erscheint.

Vorsichtig formuliert:

```text
Das sieht nach Feldphasen-Gedächtnis aus,
nicht nur nach Symbolzählung.
```

## Grenze

Die Signaturnähe ist eine passive Diagnose.

Sie beweist nicht, dass MINI_DIO bewusst versteht. Sie zeigt aber, dass die gemessene Feldqualität in unterschiedlichen Weltlagen wieder auftaucht und strukturiert verglichen werden kann.
