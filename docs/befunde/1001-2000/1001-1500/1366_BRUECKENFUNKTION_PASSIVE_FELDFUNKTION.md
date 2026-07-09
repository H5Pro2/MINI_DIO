# 1366 - Brueckenfunktion als passive Feldfunktion

## Fragestellung

Diese Datei verdichtet die Befunde `1357` bis `1365`.

Geprueft wurde:

```text
Entsteht die Brueckenfunktion nur durch starke Sinnesaktivierung,
oder braucht sie eine bestimmte Lagefolge im MCM-Feld?
```

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Strategie.

## Beobachtete Feldfunktion

Die untersuchte Brueckenlinie lautet:

```text
brueckenuebergang_zum_lauten_kontakt
```

Sie tritt auf, wenn eine Weltlage nicht einfach laut oder druckvoll ist, sondern aus einer vorherigen Lage in lauteren Feldkontakt uebergeht.

Typische Lagefolgen:

```text
normale_weltspannung -> lauter_feldkontakt
offen_suchend -> lauter_feldkontakt
randlastige_sinneslage -> lauter_feldkontakt
```

Damit ist die Bruecke keine reine Messgroesse. Sie beschreibt eine Uebergangsfunktion im Feld.

## Positivbefund

Aus `1360`:

- Brueckenfenster: `10`
- Preview traegt weiter: `8/10`
- Symbolfamilie traegt weiter: `4/10`
- Rekopplung Delta: `+0.001448`
- Strain Delta: `-0.001295`

Lesung:

```text
Die Bruecke traegt als kurze Nachhallspur weiter.
Sie stabilisiert leicht und entlastet leicht.
Sie kopiert nicht starr die Symbolfamilie.
```

Das ist wichtig: Die grobe `dio_*`-Familie muss nicht identisch bleiben, damit die Feldfunktion weitertraegt. Das stabilere Signal liegt in der MCM-Preview- und Rollenfolge.

## Negativkontrolle

Aus `1361` bis `1365`:

Es wurden Kontrollfenster mit aehnlicher Hoer-/Druckstaerke gewaehlt, aber ohne Lagefolge `-> lauter_feldkontakt`.

Kontrollgruppe:

- Kontrollfenster: `20`
- Hoeren steigt: `16/20`
- Felddruck steigt: `16/20`
- Range enger: `15/20`
- Brueckennaehe: `0`
- Hauptrolle: `rueckbindung_in_normale_weltspannung` mit `17/20`

Lesung:

```text
Starke Sinnesaktivierung allein erzeugt Nachhall,
aber keine Brueckenfunktion.
```

Die Kontrolle zeigt ebenfalls Preview- und Familiennachhall. Dieser Nachhall bleibt aber an Rueckbindung in normale Weltspannung gebunden, nicht an Bruecke.

## Abgrenzung

Die Brueckenfunktion ist zu unterscheiden von:

### Randdruck

Aus `1360`:

- Randnaher Kontaktdruck: `8`
- Rekopplung Delta: `-0.263374`
- Strain Delta: `-0.062453`

Lesung:

```text
Randdruck wirkt eher wie Abfluss oder Entlastung,
nicht wie tragende Bruecke.
```

### Zentrumskontakt

Aus `1360`:

- Zentrumskontakt mit Hoeranstieg: `7`
- Preview weiter: `7/7`
- Rekopplung Delta: `+0.001345`
- Strain Delta: `-0.000733`

Lesung:

```text
Zentrumskontakt traegt stabil,
aber nicht als Uebergangsbruecke,
sondern als ruhiger aktivierter Kontakt.
```

## Schlussfolgerung

Die bisherige Datenlage spricht dafuer:

```text
Brueckenfunktion = Lagefolge + Sinnesaktivierung + kurzer MCM-Nachhall
```

Nicht ausreichend ist:

```text
nur laut
nur druckvoll
nur kompakt
```

Damit ist die Brueckenfunktion eine passive Feldfunktion, keine programmierte Handlung und keine Strategie.

## Grenze

Der Befund ist ein Indiz, kein Beweis.

Noch offen:

- Wie stabil bleibt die Brueckenfunktion in weiteren Welten?
- Gibt es andere Brueckenarten ohne `lauter_feldkontakt`?
- Bleibt die MCM-Preview wichtiger als die grobe `dio_*`-Familie?
- Bildet die Brueckenfunktion langfristig eigene Bedeutungsinseln?

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier eine wichtige Eigenschaft:

```text
Das Feld unterscheidet nicht nur Reizstaerke,
sondern auch Lagefolge und Feldfunktion.
```

Das ist relevant fuer die weitere Forschung, weil es eine sauberere Trennung ermoeglicht:

- Sinnesstaerke,
- Feldrolle,
- Nachhall,
- Rueckbindung,
- Bruecke,
- Entlastung,
- Zentrumskontakt.
