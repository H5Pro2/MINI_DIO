# 1377 - Randdruck als passive Feldfunktion

## Fragestellung

Diese Datei verdichtet die Befunde `1360` sowie `1373` bis `1376`.

Geprueft wurde:

```text
Entsteht Randdruck nur durch laute Sinnesaktivierung,
oder braucht er fortgesetzten lauten Feldkontakt plus druckvolle Rohwelt?
```

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Strategie.

## Beobachtete Feldfunktion

Die untersuchte Randlinie lautet:

```text
randnaher_kontaktdruck
```

Sie tritt auf, wenn der Kontakt nicht nur in lautere Feldnaehe uebergeht, sondern dort fortgesetzt bleibt und zugleich eine laute oder druckvolle Rohweltklasse traegt.

Typische Lagefolge:

```text
lauter_feldkontakt -> lauter_feldkontakt
```

Typische Rohweltklasse:

```text
laute_oder_druckvolle_rohwelt
```

Damit ist Randdruck eine gekoppelte Feldfunktion:

```text
fortgesetzter lauter Kontakt + druckvolle Rohwelt + randnahe Entlastungsspur
```

## Positivbefund

Aus `1360`:

- Randnaher Kontaktdruck: `8`
- Preview traegt weiter: `5/8`
- Symbolfamilie traegt weiter: `2/8`
- Rekopplung Delta: `-0.263374`
- Strain Delta: `-0.062453`

Lesung:

```text
Randdruck traegt nicht wie Zentrumskontakt stabil weiter.
Er wirkt eher wie Abfluss, Entladung oder Entlastung einer Randspannung.
```

Das starke Rekopplungsdelta unterscheidet Randdruck deutlich von Bruecke und Zentrumskontakt.

## Negativkontrolle

Aus `1373` bis `1376`:

Es wurden zwei Kontrolltypen gewaehlt:

- gleicher fortgesetzter lauter Kontakt, aber ohne laute/druckvolle Rohweltklasse
- gleiche laute/druckvolle Rohweltklasse, aber ohne fortgesetzten lauten Kontakt

Kontrollgruppe:

- Kontrollfenster: `6`
- Brueckennaehe: `2`
- Randnaehe: `0`
- Zentrumskontakt: `0`
- Hauptrollen: offener lauter Kontakt `4`, Bruecke `2`
- Preview traegt im Folgefenster: `6/6`
- Symbolfamilie traegt im Folgefenster: `1/6`

Lesung:

```text
Wenn eine Randdruck-Komponente fehlt,
traegt der Kontakt weiter,
aber nicht als Randdruck.
```

Die Kontrolle zeigt Nachhall. Dieser Nachhall bleibt jedoch offen oder wird zur Bruecke, statt als randnaher Druck gelesen zu werden.

## Abgrenzung

Randdruck ist zu unterscheiden von:

### Bruecke

Bruecke entsteht beim Uebergang in lauteren Kontakt.

```text
Bruecke = Uebergang
Randdruck = fortgesetzter lauter Druckkontakt
```

### Offener lauter Kontakt

Offener lauter Kontakt kann dieselbe Lagefolge haben, aber ohne druckvolle Rohweltklasse.

```text
lauter Kontakt allein reicht nicht
```

### Zentrumskontakt

Zentrumskontakt kommt aus zentrumsnaher Ruhe.

```text
Zentrumskontakt = Aktivierung aus Ruhe
Randdruck = Randspannung im lauten Kontakt
```

## Schlussfolgerung

Die bisherige Datenlage spricht dafuer:

```text
Randdruck = fortgesetzter lauter Feldkontakt + druckvolle Rohweltklasse + entlastender MCM-Nachhall
```

Nicht ausreichend ist:

```text
nur laut
nur lauter Zielkontakt
nur druckvolle Rohwelt
nur fortgesetzter Kontakt ohne Druckklasse
```

Damit ist Randdruck eine passive Feldfunktion, keine programmierte Handlung und keine Strategie.

## Grenze

Der Befund ist ein Indiz, kein Beweis.

Noch offen:

- Bleibt Randdruck in weiteren Welten als Entlastungsfunktion stabil?
- Gibt es Randdruck bei anderen Rohweltklassen?
- Wie nahe liegt Randdruck an Rand-/Kippbereichen der Topologie?
- Bildet Randdruck eigene Bedeutungsinseln oder bleibt es eine Abflussfunktion?

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier eine dritte unterscheidbare Feldfunktion:

```text
Das Feld kann fortgesetzten lauten Druckkontakt von Bruecke und Zentrumskontakt trennen.
```

Damit entsteht eine kleine passive Funktionskarte:

- Bruecke: Uebergang in lauteren Kontakt
- Zentrumskontakt: aktivierte Zentrumsnaehe
- Randdruck: fortgesetzter lauter Druckkontakt mit Entlastungsspur

## Wie es weitergeht

Als naechstes sollte diese dreiteilige Funktionskarte in einer gemeinsamen Uebersicht zusammengefasst werden. Danach kann gezielt in weiteren Welten geprueft werden, ob Bruecke, Zentrum und Randdruck stabil bleiben oder neue Rollen erzwingen.
