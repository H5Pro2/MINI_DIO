# MCM Bewegungsbruch Folgeformen Bewertung

Stand: 2026-07-02

## Grundfrage

Warum fuehrt `bewegungsbruch` meistens zu Entlastung, aber manchmal zu Nachlast oder gebrochener Rekopplung?

## Ergebnis

Die Diagnose `1260_MCM_BEWEGUNGSBRUCH_FOLGEFORMEN` zeigt:

- `811` Fenster: `lastkontakt_entlastet`
- `61` Fenster: `rekopplung_bricht_in_last`
- `21` Fenster: `gemischtes_fenster`
- `9` Fenster: `rekopplung_vor_neuer_last`
- `1` Fenster: `lastkontakt_bleibt`

## Zentrale Trennung

Die Rohweltklasse ist fast gleich:

```text
bewegungsbruch
```

Der Unterschied liegt nicht primaer in der Aussenbewegung, sondern in der Feldfolge danach.

## Hauptform

`lastkontakt_entlastet`:

- Rekopplung steigt im Mittel um `+0.0810`
- Strain faellt im Mittel um `-0.0992`

Lesart:

```text
Das Feld beruehrt Bruch/Rand,
findet danach aber wieder Anschluss.
```

## Gegenformen

### Rekopplung bricht in Last

`rekopplung_bricht_in_last`:

- Rekopplung steigt nur schwach: `+0.0237`
- Strain faellt nur schwach: `-0.0446`

Lesart:

```text
Das Feld entlastet noch,
aber die Rueckbindung ist schwach.
```

Das ist kein voller Kollaps, sondern ein schwaches Entlastungsfenster.

### Gemischtes Fenster

`gemischtes_fenster`:

- Rekopplung faellt leicht: `-0.0140`
- Strain steigt leicht: `+0.0063`

Lesart:

```text
Der Bruch wird nicht integriert.
Das Feld bleibt uneindeutig oder beginnt nachzulasten.
```

### Rekopplung vor neuer Last

`rekopplung_vor_neuer_last`:

- Rekopplung faellt stark: `-0.1148`
- Strain steigt stark: `+0.1257`

Lesart:

```text
Das Feld findet kurz Anschluss,
wird danach aber erneut belastet.
```

Das ist die klarste Gegenform zur Entlastung.

## Bedeutung fuer die MCM-Feldmechanik

Damit wird eine wichtige Trennung sichtbar:

```text
Rohweltbruch ist Ausloeser.
Feldfolge ist Bedeutung.
```

Das Feld reagiert also nicht nur auf den Bruch selbst.

Es bildet eine interne Antwort:

- Anschluss finden,
- Anschluss schwach halten,
- uneindeutig bleiben,
- oder wieder in Last kippen.

## Schluss

Die MCM-Feldreaktion ist nicht nur sensorisch.

Sie ist rekopplungsbezogen:

```text
Nicht: Was passiert draussen?
Sondern: Kann das Feld danach wieder tragend anschliessen?
```

Das ist eine wichtige Stufe fuer die weitere MINI_DIO-Forschung.
