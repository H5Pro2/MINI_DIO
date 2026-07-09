# 1081 - Feldfolgensignatur dio_0g2r

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1079_BRUECKENFAMILIE_DIO_0G2R_EINZELEREIGNISSE.md`
- `1080_BRUECKENFAMILIE_DIO_0G2R_TICKFENSTER.md`

## Frage

Wiederholt sich das Prinzip aus `dio_17ct`: Familie als Anker, Feldfolge als Bedeutungsentscheidung?

## Aggregierter Befund

`dio_0g2r` erscheint ebenfalls in beiden Lesarten.

| Lesart | Ereignisse | Spannung | Rekopplung | Strain | Spannungsdelta | Rekopplungsdelta |
|---|---:|---:|---:|---:|---:|---:|
| tragende_verarbeitung | 64 | 0.0683 | 0.7217 | 0.1326 | -0.0402 | 0.0229 |
| kippnaehe | 47 | 0.0929 | 0.6893 | 0.1642 | -0.0115 | 0.0114 |

## Tragende Lesart

Bei tragender Verarbeitung zeigt `dio_0g2r`:

- deutlich niedrigere Spannung,
- hoehere Rekopplung,
- niedrigeren Strain,
- Feldlabel `rekoppelt`,
- meist geordnetes Hinhoeren,
- oft offene oder wechselnde Form, aber ohne Feldkollaps.

Beispiel:

```text
Tick 9155: tragende_verarbeitung
Spannung 0.0640
Rekopplung 0.7287
Strain 0.1284
Feld: rekoppelt
```

## Kippnahe Lesart

Bei Kippnaehe zeigt `dio_0g2r`:

- hoehere Spannung,
- niedrigere Rekopplung,
- hoeheren Strain,
- teils direkt `belastet_kippnah`,
- teils Vorlauf mit lauterem Wechsel oder belasteter Feldlage.

Beispiel:

```text
Tick 7: kippnaehe
Spannung 0.1045
Rekopplung 0.6458
Strain 0.1852
Feld: belastet_kippnah
```

## Schluss

`dio_0g2r` bestaetigt das Prinzip aus `dio_17ct`.

```text
Symbolfamilie = Anker
Feldfolge = aktuelle Bedeutung
Realitaetsrueckkopplung = Reifung der Lesart
```

Die Familie ist nicht falsch, wenn sie in beiden Rollen erscheint. Sie ist ein wiederkehrender Kontaktbereich, dessen Bedeutung durch die aktuelle Welt- und Feldlage entschieden wird.

## Bedeutung fuer MINI_DIO

Damit wird die dynamische Innenfeld-Semantik robuster:

- gleiche Familie,
- unterschiedliche Feldfolge,
- unterschiedliche Bedeutung.

Das ist keine starre Klassifikation. Es ist eine passive Bedeutungsbildung ueber Kontext.

## Wie es weitergeht

Als naechstes sollte die gemeinsame Mechanik aus `dio_17ct` und `dio_0g2r` als allgemeine Regel fuer Brueckenfamilien formuliert werden: Familie als Anker, Feldfolge als Bedeutungsentscheidung, Wiederkehr als Reifung.
