# 1078 - Feldfolgensignatur dio_17ct

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1075_BRUECKENFAMILIEN_ROHWELTFENSTER.md`
- `1076_BRUECKENFAMILIE_DIO_17CT_EINZELEREIGNISSE.md`
- `1077_BRUECKENFAMILIE_DIO_17CT_TICKFENSTER.md`

## Frage

Welche Vorlauf- und Feldfolgen-Merkmale unterscheiden `dio_17ct` als tragende Verarbeitung von `dio_17ct` als Kippnaehe?

## Befund

`dio_17ct` erscheint in beiden Lesarten:

```text
tragende_verarbeitung
kippnaehe
```

Die Familie selbst entscheidet die Lesart nicht. Entscheidend ist die Feldfolge.

## Tragende Lesart

In den extrahierten tragenden Fenstern zeigt der Ereignispunkt:

- niedrigere Spannung als belastete Vorfenster,
- hoehere Rekopplung,
- niedrigeren Strain,
- Feldlabel `rekoppelt`,
- stabile oder scharfe Formaufnahme,
- geordnetes Hinhoeren.

Beispiel:

```text
Tick 9309: belastet_kippnah
Spannung 0.2175, Rekopplung 0.6694, Strain 0.1910

Tick 9310: tragende_verarbeitung
Spannung 0.0971, Rekopplung 0.7403, Strain 0.1215
```

Lesart:

```text
Vorlast wird nicht fortgesetzt.
Das Feld rekoppelt.
Die gleiche Familie wird tragend gelesen.
```

## Kippnahe Lesart

In den kippnahen Fenstern liegt vor dem Ereignis oft bereits ein belasteter Kontakt:

```text
Tick 65: belastet_kippnah
Spannung 0.2032, Rekopplung 0.6236, Strain 0.2243

Tick 66: kippnaehe
Spannung 0.1298, Rekopplung 0.6613, Strain 0.1747
```

Das Ereignis selbst ist teils nicht maximal belastet, bleibt aber in einer niedrigeren Rekopplung und hoeheren Strain-Lage als die tragende Lesart.

Lesart:

```text
Die Vorlast wirkt nach.
Das Feld loest sich nicht sauber in Rekopplung.
Die gleiche Familie wird kippnah gelesen.
```

## Schluss

`dio_17ct` ist keine feste Bedeutung.

`dio_17ct` ist eine wiederkehrende Familie, deren aktuelle Bedeutung aus der Kopplung von:

- Vorfenster,
- Tonlage,
- visueller Formaufnahme,
- Rezeptoraufnahme,
- Spannung,
- Rekopplung,
- Strain

entsteht.

Das bestaetigt die Arbeitsregel aus 1074:

```text
Innere Familie allein reicht nicht.
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Bedeutung fuer MINI_DIO

Damit wird die praebewusste Ergaenzung konkret:

```text
Mini-DIO darf eine Familie wiedererkennen.
Aber die Familie ist nur ein Anker.
Die Feldfolge entscheidet, ob der Anker tragend oder kippnah ist.
```

Das ist ein wichtiger Schritt weg von starrer Symbolik und hin zu dynamischer Innenfeld-Semantik.

## Wie es weitergeht

Als naechstes sollte dieselbe Feldfolgenanalyse mit einer zweiten Brueckenfamilie wiederholt werden. Wenn sich das Prinzip wiederholt, wird daraus eine robuste Mechanik: Familie als Anker, Feldfolge als Bedeutungsentscheidung.
