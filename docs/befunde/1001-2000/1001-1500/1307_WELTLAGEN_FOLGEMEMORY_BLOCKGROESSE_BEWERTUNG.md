# Bewertung 1307 - Weltlagen-Folgememory Blockgroesse

## Prueffrage

Nach `1302-1304` war offen, ob die gelesenen Lagefolgen stabil bleiben, wenn die Diagnose nicht mit derselben Blockgroesse arbeitet.

Geprueft wurden dieselben Mehrwelten mit:

- Blockgroesse `100`
- Blockgroesse `200`
- Blockgroesse `400`

## Ergebnis

Die Hauptfolgen bleiben ueber die Blockgroessen sichtbar:

- `normale_weltspannung -> normale_weltspannung`
- `ueberstabil_extrem_leise_scharf -> ueberstabil_extrem_leise_scharf`
- `offen_suchend -> offen_suchend`
- `offen_suchend -> normale_weltspannung`
- `normale_weltspannung -> offen_suchend`
- `randlastige_sinneslage -> randlastige_sinneslage`
- `normale_weltspannung -> randlastige_sinneslage`

Die Folgeordnung ist damit nicht nur ein Einzelblock-Artefakt.

## Blockgroesse 100

Bei feinerer Blockung entstehen mehr Einzelvarianten:

- `51` Folgeklassen
- `42` neutral
- `9` beruhigend

Die feine Blockung liest viele kurze Lagebewegungen als neutral, weil die Wirkung noch nicht lange genug getragen ist.

## Blockgroesse 200

Die mittlere Blockung aus `1303` bildet eine Zwischenlage:

- `40` Folgeklassen
- `22` neutral
- `18` beruhigend

Hier werden offene und randnahe Folgen bereits klarer beruhigend, ohne dass ueberstabile Folgen kuenstlich verschoben werden.

## Blockgroesse 400

Bei groberer Blockung wird die Folgequalitaet deutlicher:

- `29` Folgeklassen
- `15` beruhigend
- `14` neutral

Besonders:

- `normale_weltspannung -> normale_weltspannung` wird beruhigend.
- `offen_suchend -> offen_suchend` wird beruhigend.
- `randlastige_sinneslage -> randlastige_sinneslage` bleibt beruhigend.
- `ueberstabil_extrem_leise_scharf -> ueberstabil_extrem_leise_scharf` bleibt neutral.

## Wichtigster Befund

Die Lagefolge bleibt stabil, aber ihre Wirkung ist zeitlich skalenabhaengig.

Kurz gelesen:

```text
fein:
  viele Einzelbewegungen bleiben neutral

mittel:
  offene und randnahe Folgen werden teilweise beruhigend

grob:
  getragene Lagefolgen zeigen deutlicher Beruhigung
```

Das passt zur bisherigen Feldzeit-Lesung:

Eine Weltlage hat nicht nur einen momentanen Zustand.

Sie bekommt Bedeutung ueber Dauer, Folge und getragene Wirkung.

## Bedeutung fuer MINI_DIO

Mini-DIO sollte Lagefolgen nicht nur punktuell speichern.

Wichtig ist die zeitliche Tiefe:

```text
Welche Lage kam vorher?
Welche Lage bleibt?
Wie lange bleibt sie?
Welche Feldwirkung entsteht erst ueber Dauer?
```

Damit wird Rezeptorhaltung nicht als harte Einstellung gelesen, sondern als Aufnahmequalitaet ueber Feldzeit.

## Grenze

Die Blockgroesse ist weiterhin Diagnose.

Sie ist keine interne Regel fuer MINI_DIO.

Die Ergebnisse zeigen nur, dass verschiedene zeitliche Lesetiefen unterschiedliche Aspekte derselben Feldordnung sichtbar machen.

Wie es weitergeht: Als naechstes sollte die Blockgroesse nicht fest gewaehlt, sondern als mehrskalige Diagnose gelesen werden: kurze Lagebewegung, mittlere Lagefolge und laengere Feldphase.
