# 1378 - Passive MCM-Feldfunktionskarte

## Zweck

Diese Datei fasst die isolierten Befunde zu Bruecke, Zentrumskontakt und Randdruck zusammen.

Sie ist keine neue Mechanik. Sie ist eine passive Karte der bisher beobachteten Feldfunktionen.

## Grundfrage

```text
Unterscheidet MINI_DIO nur Reizstaerke,
oder bildet das MCM-Feld unterschiedliche passive Feldfunktionen?
```

Die bisherigen Pruefungen sprechen dafuer, dass nicht nur Lautstaerke, Druck oder Kompaktheit gelesen werden, sondern Lagefolge, Sinnesaktivierung und Nachhall zusammenwirken.

## Feldfunktionen

| Feldfunktion | Kernausloeser | Nachhallbild | Kontrollbefund | Lesung |
|---|---|---|---|---|
| Bruecke | Uebergang in lauteren Feldkontakt | kurzer tragender Uebergang | aehnliche Sinnesstaerke ohne Zielkontakt erzeugt `0` Brueckenfaelle | Uebergangsfunktion |
| Zentrumskontakt | `ruhig_zentrumsnah -> lauter_feldkontakt` | sehr stabile lokale Preview | aehnliche Sinnesstaerke ohne volle Zentrumslagefolge erzeugt `0` Zentrumskontakt | aktivierte Zentrumsnaehe |
| Randdruck | `lauter_feldkontakt -> lauter_feldkontakt` plus druckvolle Rohwelt | Entladung / Abfluss / Entlastung | fehlende Teilkomponente erzeugt `0` Randdruck | fortgesetzter Druckkontakt |

## Wichtigster Befund

```text
Reizstaerke allein reicht nicht.
```

In allen drei Linien zeigen die Gegenproben, dass aehnliche Sinnesaktivierung nicht automatisch dieselbe Feldfunktion erzeugt.

Entscheidend ist die Kopplung:

```text
Lagefolge + Sinnesaktivierung + MCM-Nachhall
```

## Rolle des Nachhalls

Nachhall erscheint in allen Kontrollgruppen.

Das ist wichtig:

```text
Nachhall ist nicht automatisch Bedeutungsgleichheit.
```

Ein Kontakt kann weitertragen, aber als andere Feldfunktion:

- Bruecke statt Randdruck,
- Rueckbindung statt Zentrumskontakt,
- offener lauter Kontakt statt Randdruck.

Damit ist Nachhall eine zeitliche Feldspur, aber die Feldrolle entscheidet, wie diese Spur gelesen wird.

## Bedeutung fuer das MCM-Feld

Die bisherige Karte zeigt drei verschiedene Arten von passiver Feldorganisation:

### Uebergang

```text
Bruecke
```

Das Feld erkennt, dass eine Lage in eine andere Kontaktnaehe uebergeht.

### Aktivierte Naehe

```text
Zentrumskontakt
```

Das Feld erkennt, dass eine ruhige zentrumsnahe Lage aktiviert wird und lokal stabil weitertraegt.

### Entlastende Randspannung

```text
Randdruck
```

Das Feld erkennt fortgesetzten lauten Druckkontakt, der eher entlaedt als stabil bindet.

## Abgrenzung

Diese Karte bedeutet nicht:

- MINI_DIO handelt,
- MINI_DIO entscheidet,
- MINI_DIO verfolgt eine Strategie,
- die Topologie sei bewiesen.

Sie bedeutet:

```text
MINI_DIO zeigt passive Feldrollen,
die durch kontrollierte Gegenproben unterscheidbar werden.
```

## Forschungswert

Die Karte ist ein wichtiger Zwischenschritt, weil sie eine methodische Ordnung schafft:

```text
nicht einzelne Koerner suchen,
sondern Feldfunktionen isolieren und gegeneinander pruefen.
```

Damit koennen weitere Welten gezielter gelesen werden:

- bleibt Bruecke Bruecke?
- bleibt Zentrumskontakt zentrumsnah?
- bleibt Randdruck eine Entlastungsspur?
- entstehen neue Rollen?
- kippt eine Rolle unter anderer Weltspannung?

## Grenze

Der Befund ist ein Indiz.

Stabiler wird er erst, wenn diese drei Rollen in weiteren Welten erneut unterscheidbar bleiben.
