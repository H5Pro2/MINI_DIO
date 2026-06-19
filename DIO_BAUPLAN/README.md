# DIO Bauplan

Dieser Ordner ist im neuen MINI_DIO-Projekt kein alter Bot-Bauplan mehr.

Er dient nur noch als Theorie- und Abhandlungsbereich fuer die MINI_DIO-Forschung.

## Aktiv

- `abhandlungen/` enthaelt die fachliche Verdichtung der Mini-DIO- und MCM-Erkenntnisse.

## Nicht Teil dieses Projekts

Die alten Bereiche `konstruktion/`, `bausatz/` und `temp_alt/` wurden aus diesem MINI_DIO-Projekt entfernt, weil sie alte DIO-Bot-Mechaniken, Handlungsschichten, Gate-Logik und ueberladene Arbeitsverlaeufe zurueck in die neue Forschung ziehen koennten.

## Arbeitsregel

MINI_DIO bleibt zuerst ein Forschungsprojekt fuer:

- MCM-basierte Innenfeldreaktion,
- rezeptorische Wahrnehmungstrennung,
- emergente Bedeutungsverdichtung,
- passive Semantik,
- Feldtopologie,
- Reproduzierbarkeit,
- Drift, Rekopplung und Eigenregulation.

Handlung, Entry, Gate, Motorik und Trading-Strategie gehoeren nicht in diesen Bauplan, solange sie nicht aus stabilen passiven Befunden begruendet werden.

## Feste Wahrnehmungsarchitektur

Aus den Befunden `303` bis `308` wird die rezeptorische Trennung als Bauplan-Grundsatz uebernommen.

MINI_DIO liest Weltkontakt nicht mehr als direkte Feldwirkung.

Stattdessen gilt:

```text
Aussenwelt
  -> Sehen / Hoeren
  -> Rezeptoren
  -> Fuehlen
  -> MCM-Feld
```

### Bedeutung der Ebenen

- `Sehen` liest Form, Fluss, Stabilitaet und Formwechsel.
- `Hoeren` liest Energie, Ton, Druckwechsel und rhythmische Spannung.
- `Rezeptoren` uebersetzen Sinneskontakt in innere Beruehrung.
- `Fuehlen` meint im aktuellen MINI_DIO-Kontext MCM-Feldwirkung durch Rezeptorkontakt, nicht Hautkontakt.
- `MCM-Feld` bildet daraus passive Ordnung, Zentrum, Rand, Uebergang und Rekopplung.

Im Code wird diese Trennung ab jetzt kompatibel gefuehrt:

```text
mcm_feldwirkung = fachlicher Name
fuehlen = alter Kompatibilitaetsname
```

Neue Kernlogik soll `mcm_feldwirkung` lesen. `fuehlen` bleibt nur erhalten, damit alte Debugs, Reports und Befunde nicht brechen.

Nicht zulaessig als Bauprinzip:

```text
Aussenwelt -> MCM-Feld
```

Das waere fachlich zu roh, weil ein organisches System nicht die ganze Welt direkt fuehlt. Es fuehlt nur das, was ueber seine Rezeptoren als innere Beruehrung ankommt.

Die Sinnesaufnahme nutzt ab Befund `321` standardmaessig den weltrelativen Modus:

```text
DIO_MINI_SENSE_MODE = "world_relative"
```

Damit werden unterschiedliche Welten zuerst gegen ihre eigene Bewegung, Lautstaerke und Formspannung gelesen, bevor daraus Rezeptorkontakt und MCM-Feldwirkung entstehen.

Wichtig:

```text
Sehen + Hoeren ist nicht Fuehlen.
```

Sehen, Hoeren und spaeter Tasten sind getrennte Sinnesachsen. Die aktuelle Feldwirkung aus Sehen und Hoeren darf deshalb nicht als echter Haut- oder Koerperkontakt missverstanden werden.

## Rezeptorische Grundwerte

Die Rezeptorschicht bleibt passiv und darf nicht als Gate, Entry-Signal oder motorische Steuerung verwendet werden.

Sie ist ein fundamentaler Schutz- und Uebersetzungsbaustein vor der MCM-Schicht.

Ihre Kernaufgabe:

```text
Sie schuetzt das MCM-Feld vor Rohdatenueberlagerung.
```

Das Feld bekommt nicht die Aussenwelt selbst, sondern die innere Wirkung von Rezeptorkontakt.

Sie beschreibt deshalb nur die Qualitaet des Kontakts:

- `visual_contact`: wie stark sichtbare Form beruehrt.
- `auditory_contact`: wie stark die energetische Hoerspur beruehrt.
- `contact_pressure`: gesamte Kontaktspannung.
- `contact_alignment`: Passung zwischen visueller und akustischer Beruehrung.
- `contact_asymmetry`: gerichtete Kontaktpraegung.

Die aktuellen Befunde zeigen:

- Oeffnung aus dem Zentrum geht mit mehr `contact_pressure` und weniger `contact_alignment` einher.
- Rekopplung zum Zentrum geht mit weniger `contact_pressure` und besserem `contact_alignment` einher.
- Die bisher beobachtete Zentrum-Rand-Uebergangsordnung bleibt auch nach dieser Trennung erhalten.
- Kontaktinseln verdichten sich auf der MCM-Preview-Ebene in weniger Feld-Episodenfamilien als auf der rohen Symbolseite.

## Rezeptorschicht als Schutzgrenze

Als Bauprinzip gilt:

```text
Nicht alles, was von aussen existiert, darf direkt in das MCM-Feld.
Nur was ueber Rezeptoren als innere Beruehrung getragen wird, darf MCM-Fuehlen erzeugen.
```

Damit ist die Rezeptorschicht die funktionale Grenze zwischen Welt und Innenfeld.

Sie verhindert:

- Ueberlagerung durch zu viele Rohdaten,
- Vermischung von Sehen, Hoeren und Fuehlen,
- direkte Rohweltwirkung auf die MCM-Schicht,
- falsche Deutung von Wahrnehmungsdaten als Feldzustand.

Sie ermoeglicht:

- getrennte Sinnesaufnahme,
- organisierte Kontaktqualitaet,
- saubere MCM-Feldwirkung,
- passive Bedeutungsverdichtung,
- stabilere Rekopplung.

## Getrennte Sinneswahrnehmung

MINI_DIO soll keine ungetrennte Gefuehlsmischung bilden.

Die sinnvolle Grundordnung lautet:

```text
Sehen  -> visuelle Rezeptoren -> visuelle Feldwirkung
Hoeren -> auditive Rezeptoren -> auditive Feldwirkung
Tasten -> taktile Rezeptoren  -> taktile Feldwirkung
```

Tasten ist aktuell noch nicht vorhanden.

Eine spaetere Mousepad- oder Kontaktflaechen-Simulation kann diese Achse kontrolliert ergaenzen:

```text
Kontaktpunkt
+ Druck
+ Bewegung
+ Reibung
+ Stabilitaet
+ Nachhall
= taktile Rezeptorwirkung
```

Dabei bleibt die taktile Simulation passiv. Sie ist kein Steuergeraet und keine Handlungsschicht.

## Innenwahrnehmung

Zusaetzlich muss MINI_DIO zwischen zwei Innenlesungen unterscheiden:

```text
Wie fuehlt sich diese Wahrnehmung an?
Was macht diese Wahrnehmung mit mir?
```

Die erste Frage ist reflektiv:

```text
Ich lese die Wirkung einer Wahrnehmung in mir.
```

Die zweite Frage ist MCM-metaphysisch:

```text
Ich lese, wie diese Wahrnehmung meine Feldordnung veraendert.
```

Damit bleibt klar:

- Sinneswahrnehmung ist der Kanal.
- Reflektive Innenwahrnehmung ist die innere Lesung.
- MCM-Feldwirkung ist die Veraenderung der Feldordnung.

## Bauplan-Grenze

Diese Rezeptorschicht ist keine Handlungslogik.

Sie ist die Grundlage fuer saubere MCM-Wahrnehmung:

```text
Weltkontakt wird beruehrt.
Beruehrung wird gefuehlt.
Fuehlen wirkt auf das MCM-Feld.
Das Feld ordnet passiv.
```

Erst wenn aus dieser passiven Ordnung langfristig stabile Konsequenzkopplung entsteht, darf Handlung spaeter wieder als eigenes Forschungsthema betrachtet werden.
