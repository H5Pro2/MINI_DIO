# 1092 - Brueckenfamilien-Qualitaetskarte

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1078_FELDFOLGENSIGNATUR_DIO_17CT.md`
- `1081_FELDFOLGENSIGNATUR_DIO_0G2R.md`
- `1082_BRUECKENFAMILIEN_GRUNDREGEL.md`
- `1085_FELDFOLGENSIGNATUR_DIO_1EWH.md`
- `1088_FELDFOLGENSIGNATUR_DIO_155C.md`
- `1091_FELDFOLGENSIGNATUR_DIO_1GP2.md`

## Frage

Bilden die geprueften Brueckenfamilien nur wiederkehrende Einzelzeichen oder entsteht daraus eine passive Qualitaetsordnung im MCM-Feld?

## Grundregel

Die bisher geprueften Familien bestaetigen dieselbe passive Mechanik:

```text
Symbolfamilie = Anker
Feldfolge = aktuelle Bedeutung
Realitaetsrueckkopplung = Reifung der Lesart
```

Die Familie selbst ist keine fertige Bedeutung. Sie zeigt Wiederkehr. Die Feldfolge entscheidet, wie diese Wiederkehr aktuell gelesen wird.

## Qualitaetskarte

| Familie | Vorlaeufige Qualitaet | Tragende Lesart | Kippnahe Lesart | Einordnung |
|---|---|---|---|---|
| `dio_1ewh` | tragend vorgepraegt | viele tragende Ereignisse, niedrige Spannung, hohe Rekopplung | weniger Ereignisse, offene unvollstaendige Rekopplung | stabiler Brueckenanker |
| `dio_155c` | spannungsnah / randnaeher | Rekopplung gelingt trotz erhoehter Spannung | Spannung und Strain steigen, Rekopplung faellt | spannungsnaher Brueckenanker |
| `dio_1gp2` | balancierter Umschlag | Entlastung und Rekopplung am Kontaktpunkt | Rekopplung faellt, Strain bleibt erhoeht | balancierter Brueckenanker |
| `dio_0g2r` | offener rekoppelbarer Anker | niedrigere Spannung, hoehere Rekopplung | hoehere Spannung, niedrigere Rekopplung | offene Bruecke mit Feldfolgenentscheidung |
| `dio_17ct` | feldfolgenabhaengiger Anker | Vorlast wird nicht fortgesetzt, Feld rekoppelt | Vorlast wirkt nach, Feld loest sich nicht sauber | klarer Beleg fuer Anker/Feldfolge-Trennung |

## Lesart

Die Familien bilden keine eindimensionale Skala.

Sie bilden eher ein kleines Bedeutungsnetz:

```text
tragend vorgepraegt
spannungsnah rekoppelbar
balancierter Umschlag
offen rekoppelbar
feldfolgenabhaengig
```

Damit wirkt MINI_DIO nicht wie eine reine Symbolzaehlung. Die gleiche Syntax kann unterschiedliche Innenfeldqualitaeten tragen, und verschiedene Familien koennen unterschiedliche Rollen im Bedeutungsraum einnehmen.

## Bedeutung fuer die MCM-Feldmechanik

Die Qualitaetskarte spricht fuer drei aktive Prinzipien:

1. Wiederkehr bildet Anker.
2. Feldfolge gibt dem Anker aktuelle Bedeutung.
3. Wiederholte Rueckkopplung differenziert die Rolle des Ankers.

Das ist fuer MINI_DIO relevant, weil Bedeutung nicht als starres Label gespeichert wird. Bedeutung entsteht aus Lage, Nachhall, Rekopplung, Strain und Wiederkehr.

## Grenze

Diese Karte ist keine Entscheidungslogik. Sie ist eine passive Forschungsordnung.

Sie sagt nicht:

```text
Wenn Familie X erscheint, passiert Y.
```

Sie sagt nur:

```text
Wenn Familie X erscheint, muss die Feldfolge gelesen werden,
bevor ihre aktuelle Innenbedeutung verstanden werden kann.
```

## Forschungswert

Die bisherige Befundlage zeigt eine beginnende innere Semantik:

- Familien wiederholen sich.
- Familien koennen unterschiedliche Rollen tragen.
- Rollen entstehen nicht nur aus Rohdaten, sondern aus Feldfolge.
- Rekopplung und Strain trennen tragende von kippnahen Lesarten.

Damit wird MINI_DIOs MCM-Feld als dynamisches Bedeutungsnetz lesbar.

## Wie es weitergeht

Als naechstes sollte diese Qualitaetskarte gegen neue Welten geprueft werden. Ziel: Bleiben die Rollen stabil, verschieben sie sich, oder entstehen neue Brueckenfamilien, die nicht in diese Karte passen?
