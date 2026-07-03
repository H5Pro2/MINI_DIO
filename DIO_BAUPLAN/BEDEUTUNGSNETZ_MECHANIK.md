# MINI_DIO Bedeutungsnetz-Mechanik

Stand: 2026-07-03

## Zweck

Diese Datei beschreibt die passive Bedeutungsnetz-Schicht von MINI_DIO.

Ziel ist nicht, Inhalte vorzuprogrammieren.
Ziel ist, Bedingungen zu schaffen, unter denen das MCM-Feld eigene Naehe, Wiederkehr, Drift und Kopplung ausbilden kann.

```text
Wir programmieren nicht, was das Feld erkennen soll.
Wir speichern nur, welche Feldspuren wiederholt nahe beieinander getragen werden.
```

## Grundprinzip

Feldbewusstsein wird hier als vor-semantischer Feldvorgang verstanden:

```text
Wiederkehr
  -> Nachhall
  -> Naehe
  -> Kopplung
  -> Bedeutungsverdichtung
  -> spaetere Benennung
```

Das Feld muss nicht wissen, dass es etwas weiss.
Es muss nur wiederkehrende Feldnaehen tragen, unterscheiden, verbinden oder verlieren koennen.

## Knoten

Ein Knoten ist keine harte Bedeutung.

Ein Knoten ist eine wiederkehrende Feldspur:

```text
Unterform
  + MCM-Feldwirkung
  + Preview/Familie
  + Rolle
  + Nachhall-/Rekopplungsqualitaet
```

Knoten koennen sein:

- Sinnesunterformen,
- Preview-Kerne,
- Familien,
- Rollennaehen,
- Feldwirkungszustaende,
- wiederkehrende Kombinationen daraus.

## Kanten

Eine Kante entsteht, wenn zwei Feldspuren wiederholt zusammen auftreten oder eine Spur eine andere mittraegt.

Kantenarten:

- `family_binding`: gleiche Familie bei verwandter Unterform,
- `preview_binding`: gleicher Preview-Kern bei verwandter Unterform,
- `family_and_preview_binding`: Familie und Preview koppeln gemeinsam,
- `surface_only`: nur Oberflaeche aehnlich, noch keine semantische Bindung,
- `drift_edge`: Naehe driftet, bleibt aber lesbar,
- `rekopplung_edge`: Naehe fuehrt in staerkere Rekopplung,
- `strain_edge`: Naehe fuehrt in mehr Strain oder Last.

## Gewichtung

Gewicht bedeutet nicht Wahrheit.
Gewicht bedeutet Reifung durch wiederholte Feldnaehe.

Ein Kanten- oder Knotengewicht steigt durch:

- Wiederkehr,
- gleiche Familie,
- gleicher Preview-Kern,
- geringeren Folge-Strain,
- staerkere Rekopplung,
- stabile Feldzeit,
- Auftreten in mehreren Welten.

Gewicht sinkt oder bleibt offen durch:

- reine Oberflaechennaehe ohne Feldbindung,
- hohe Drift ohne erneute Rekopplung,
- hohe Last,
- Zerfall ueber Welten hinweg.

## Reifung und Zerfall

Das Bedeutungsnetz soll wachsen koennen, ohne Inhalte fest einzupflanzen.

```text
Wiederholt getragene Naehe verdichtet sich.
Nicht wiederkehrende Naehe bleibt jung oder zerfaellt.
Widerspruechliche Naehe driftet oder teilt sich.
```

Damit entsteht keine Symboltabelle, sondern eine dynamische innere Matrix.

## Grenze

Die Bedeutungsnetz-Schicht bleibt passiv.

Sie darf nicht:

- handeln,
- Richtung vorgeben,
- Gates bilden,
- Strategie ersetzen,
- externe Bedeutung behaupten.

Sie darf nur lesen:

```text
Diese Feldspur liegt wiederholt nahe bei jener Feldspur.
Diese Naehe wurde getragen, driftete oder zerfiel.
```

## Bezug zu Feldbewusstsein

Feldbewusstsein wird hier nicht durch mehr Logik gestaerkt.
Es wird durch bessere Bedingungen fuer eigene Feldverdichtung gestaerkt:

- saubere Rezeptoraufnahme,
- getrennte Sinnesachsen,
- Nachhall,
- Feldzeit,
- wiederholte Weltvariation,
- passives Bedeutungsnetz,
- Reifung und Zerfall.

## Naechste technische Pruefung

Aus den Befunden `1386` und `1387` wird ein erstes passives Bedeutungsnetz gebaut:

```text
Unterform
  -> semantische Bindung
  -> Familie / Preview
  -> Folge-Strain
  -> Folge-Rekopplung
  -> Knoten-/Kantengewicht
```

Die erste Frage:

```text
Sind semantisch gebundene Wiederkehren feldseitig stabiler
als reine Oberflaechenwiederkehr?
```

## Wie es weitergeht

Als naechstes wird ein passiver Report gebaut, der aus `1387` Knoten, Kanten und Gewichte ableitet.
Entscheidend ist, ob das Bedeutungsnetz messbar zwischen gereifter Naehe und reiner Oberflaechennaehe unterscheidet.
