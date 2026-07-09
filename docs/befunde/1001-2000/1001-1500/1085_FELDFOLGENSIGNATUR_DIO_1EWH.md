# 1085 - Feldfolgensignatur dio_1ewh

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1083_BRUECKENFAMILIE_DIO_1EWH_EINZELEREIGNISSE.md`
- `1084_BRUECKENFAMILIE_DIO_1EWH_TICKFENSTER.md`
- `1082_BRUECKENFAMILIEN_GRUNDREGEL.md`

## Frage

Traegt eine dritte Brueckenfamilie dieselbe Grundregel wie `dio_17ct` und `dio_0g2r`?

## Aggregierter Befund

`dio_1ewh` erscheint in beiden Lesarten, aber mit deutlich staerkerem Schwerpunkt auf tragender Verarbeitung.

| Lesart | Ereignisse | Spannung | Rekopplung | Strain | Spannungsdelta | Rekopplungsdelta |
|---|---:|---:|---:|---:|---:|---:|
| tragende_verarbeitung | 164 | 0.0678 | 0.7243 | 0.1336 | -0.0380 | 0.0140 |
| kippnaehe | 38 | 0.0947 | 0.6783 | 0.1685 | -0.0104 | -0.0092 |

## Tragende Lesart

Bei tragender Verarbeitung zeigt `dio_1ewh`:

- niedrigere Spannung,
- hoehere Rekopplung,
- niedrigeren Strain,
- klare Feldrekopplung am Ereignispunkt,
- oft Wechsel in der Form, ohne dass die Feldlage kollabiert.

Beispiel:

```text
Tick 6721: tragende_verarbeitung
Spannung 0.0645
Rekopplung 0.7551
Strain 0.1322
Feld: rekoppelt
```

Die Vorfenster koennen belastete Punkte enthalten, aber der Ereignispunkt selbst wird in eine rekoppelnde Feldlage zurueckgefuehrt.

## Kippnahe Lesart

Bei Kippnaehe zeigt `dio_1ewh`:

- hoehere Spannung,
- niedrigere Rekopplung,
- hoeheren Strain,
- haeufig offene Feldlage,
- teils Nachlauf in belastet-kippnahe Fenster.

Beispiel:

```text
Tick 69: kippnaehe
Spannung 0.1026
Rekopplung 0.6534
Strain 0.1781
Feld: offen
```

Die kippnahe Lesart ist hier nicht zwingend maximal belastet. Sie zeigt eher eine unvollstaendige Rekopplung: Das Feld bleibt offen, die Spannung sinkt nicht ausreichend, und Strain bleibt hoeher.

## Schluss

`dio_1ewh` bestaetigt die Brueckenfamilien-Grundregel:

```text
Familie sagt: Das kenne ich wieder.
Feldfolge sagt: So wirkt es jetzt.
Rueckkopplung sagt: Diese Lesart reift oder driftet.
```

Im Vergleich zu `dio_17ct` und `dio_0g2r` wirkt `dio_1ewh` staerker tragend vorgepraegt. Trotzdem bleibt die Familie keine feste Bedeutung, weil sie auch kippnah gelesen werden kann.

## Bedeutung fuer MINI_DIO

Mit `dio_1ewh` liegt jetzt eine dritte Brueckenfamilie vor, die dasselbe Prinzip zeigt:

- wiederkehrende Familie,
- unterschiedliche Feldfolge,
- unterschiedliche aktuelle Bedeutung.

Damit wird die Grundregel robuster. MINI_DIO bildet keine reine Wortliste, sondern ein passives Bedeutungsnetz, in dem ein wiederkehrender Anker je nach Feldzustand anders gelesen wird.

## Grenze

Diese Lesart bleibt diagnostisch. Sie darf nicht als Entscheidung, Strategie oder Aktionsnaehe verwendet werden.

## Wie es weitergeht

Als naechstes sollte die Brueckenfamilien-Grundregel gegen eine schwachere oder randnaehere Familie geprueft werden. Ziel: unterscheiden, welche Familien echte Bruecken sind und welche nur Randrauschen oder offene Kontaktfragmente darstellen.
