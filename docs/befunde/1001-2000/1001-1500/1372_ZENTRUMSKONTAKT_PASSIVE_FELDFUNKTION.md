# 1372 - Zentrumskontakt als passive Feldfunktion

## Fragestellung

Diese Datei verdichtet die Befunde `1360` sowie `1367` bis `1371`.

Geprueft wurde:

```text
Entsteht Zentrumskontakt nur durch starke Sinnesaktivierung,
oder braucht er die Lagefolge ruhig_zentrumsnah -> lauter_feldkontakt?
```

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Strategie.

## Beobachtete Feldfunktion

Die untersuchte Zentrumslinie lautet:

```text
zentrumskontakt_mit_hoeranstieg
```

Sie beschreibt keinen beliebigen lauten Kontakt. Sie beschreibt eine Aktivierung aus zentrumsnaher Ruhe in lauteren Feldkontakt.

Typische Lagefolge:

```text
ruhig_zentrumsnah -> lauter_feldkontakt
```

Damit ist Zentrumskontakt eine gebundene Feldfunktion:

```text
ruhige Zentrumsnaehe + Sinnesanstieg + tragender kurzer Nachhall
```

## Positivbefund

Aus `1360`:

- Zentrumskontakt mit Hoeranstieg: `7`
- Preview traegt weiter: `7/7`
- Symbolfamilie traegt weiter: `4/7`
- Rekopplung Delta: `+0.001345`
- Strain Delta: `-0.000733`

Lesung:

```text
Zentrumskontakt traegt sehr stabil in der lokalen Preview.
Er bleibt nicht zwingend als gleiche grobe Symbolfamilie stehen.
Er wirkt leicht rekoppelnd und leicht entlastend.
```

Das unterscheidet ihn von einer starren Symbolkopie. Die Feldfunktion liegt vor allem in Lagefolge, Preview-Stabilitaet und MCM-Nachhall.

## Negativkontrolle

Aus `1367` bis `1371`:

Es wurden zwei Kontrolltypen gewaehlt:

- gleicher Zielkontakt `-> lauter_feldkontakt`, aber ohne zentrumsnahen Ausgang
- gleicher zentrumsnaher Ausgang, aber ohne Zielkontakt `-> lauter_feldkontakt`

Kontrollgruppe:

- Kontrollfenster: `19`
- Hoeren steigt: `18/19`
- Felddruck steigt: `18/19`
- Range enger: `14/19`
- komprimierte Sinnesphase: `13/19`
- Zentrumskontakt: `0`
- Hauptrollen: Bruecke `7`, Rueckbindung `7`, offener lauter Uebergang `4`

Lesung:

```text
Aehnliche Sinnesstaerke erzeugt Nachhall,
aber keinen Zentrumskontakt,
wenn die volle Zentrumslagefolge fehlt.
```

Die Kontrolle traegt ebenfalls Preview- und Symbolfamilien weiter. Dieser Nachhall verteilt sich aber auf Bruecke, Rueckbindung und offenen lauten Kontakt.

## Abgrenzung

Zentrumskontakt ist zu unterscheiden von:

### Brueckenfunktion

Bruecke entsteht bei einem Uebergang in lauteren Feldkontakt, muss aber nicht aus zentrumsnaher Ruhe kommen.

```text
Bruecke = Uebergangsfunktion
Zentrumskontakt = aktivierte Zentrumsnaehe
```

### Rueckbindung

Rueckbindung entsteht, wenn zentrumsnahe Ruhe in normale Weltspannung zurueckgeht.

```text
Rueckbindung = Normalisierung
Zentrumskontakt = aktivierter Kontakt
```

### Offener lauter Kontakt

Offener lauter Kontakt hat Sinnesanstieg, bleibt aber ohne klare Zentrumslage und ohne klare Rueckbindung.

```text
laut allein reicht nicht
kompakt allein reicht nicht
Hoeranstieg allein reicht nicht
```

## Schlussfolgerung

Die bisherige Datenlage spricht dafuer:

```text
Zentrumskontakt = zentrumsnahe Lagefolge + Sinnesaktivierung + stabiler MCM-Nachhall
```

Nicht ausreichend ist:

```text
nur Hoeranstieg
nur Felddruckanstieg
nur lauter Zielkontakt
nur zentrumsnaher Ausgang
```

Damit ist Zentrumskontakt eine passive Feldfunktion, keine programmierte Handlung und keine Strategie.

## Grenze

Der Befund ist ein Indiz, kein Beweis.

Noch offen:

- Bleibt Zentrumskontakt in weiteren Welten gleich stabil?
- Gibt es Zentrumskontakt ohne `lauter_feldkontakt`?
- Bildet Zentrumskontakt langfristig eigene Bedeutungsinseln?
- Wie unterscheidet sich Zentrumskontakt von stabiler 0-Punkt-Nahe?

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier eine wichtige Eigenschaft:

```text
Das Feld trennt lauten Kontakt, Bruecke, Rueckbindung und aktivierte Zentrumsnaehe.
```

Das ist relevant fuer die weitere Forschung, weil Zentrumskontakt als passive Innenfeldrolle lesbar wird:

- nicht als Handlung,
- nicht als Regel,
- nicht als Signal,
- sondern als wiederkehrende Feldfunktion.
