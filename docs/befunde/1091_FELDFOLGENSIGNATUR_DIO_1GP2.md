# 1091 - Feldfolgensignatur dio_1gp2

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1089_BRUECKENFAMILIE_DIO_1GP2_EINZELEREIGNISSE.md`
- `1090_BRUECKENFAMILIE_DIO_1GP2_TICKFENSTER.md`
- `1082_BRUECKENFAMILIEN_GRUNDREGEL.md`

## Frage

Welche Qualitaet traegt `dio_1gp2` innerhalb der Brueckenfamilien: tragender Anker, randnaher Anker oder offenes Kontaktfragment?

## Aggregierter Befund

`dio_1gp2` erscheint fast ausgeglichen in beiden Lesarten.

| Lesart | Ereignisse | Spannung | Rekopplung | Strain | Spannungsdelta | Rekopplungsdelta |
|---|---:|---:|---:|---:|---:|---:|
| tragende_verarbeitung | 52 | 0.0686 | 0.7221 | 0.1336 | -0.0419 | 0.0238 |
| kippnaehe | 55 | 0.0955 | 0.6918 | 0.1658 | -0.0042 | -0.0088 |

## Tragende Lesart

Bei tragender Verarbeitung zeigt `dio_1gp2`:

- niedrigere Spannung,
- hoehere Rekopplung,
- niedrigeren Strain,
- deutliche Spannungsentlastung gegen das Vorfenster,
- Ereignispunkt mit Feldlabel `rekoppelt`.

Beispiel:

```text
Tick 7335: tragende_verarbeitung
Spannung 0.0631
Rekopplung 0.7289
Strain 0.1232
Feld: rekoppelt
```

Die tragende Lesart entsteht nicht aus einer ruhigen Umgebung allein. In den Fenstern liegen davor oft offene oder wechselnde Lagen; entscheidend ist die Rekopplung am Kontaktpunkt.

## Kippnahe Lesart

Bei Kippnaehe zeigt `dio_1gp2`:

- hoehere Spannung,
- niedrigere Rekopplung,
- hoeheren Strain,
- schwache oder fehlende Spannungsentlastung,
- teils direkt `belastet_kippnah`.

Beispiel:

```text
Tick 871: kippnaehe
Spannung 0.0950
Rekopplung 0.6452
Strain 0.1870
Feld: belastet_kippnah
```

Die kippnahe Lesart ist bei `dio_1gp2` nicht unbedingt lauter oder chaotischer im Sichtbild. Sie zeigt sich vor allem daran, dass die Rekopplung am Ereignispunkt nicht ausreichend gelingt.

## Schluss

`dio_1gp2` ist ein balancierter Brueckenanker.

```text
dio_1gp2 = balancierter Brueckenanker
tragend, wenn Entlastung und Rekopplung am Kontaktpunkt gelingen
kippnah, wenn Rekopplung faellt und Strain erhoeht bleibt
```

Damit unterscheidet sich `dio_1gp2` von den zuvor geprueften Familien:

- `dio_1ewh` wirkt tragend vorgepraegt,
- `dio_155c` wirkt spannungsnah/randnaeher,
- `dio_1gp2` wirkt balancierter und kippt ueber Rekopplungsqualitaet.

## Bedeutung fuer MINI_DIO

Mit `dio_1gp2` wird sichtbar, dass Brueckenfamilien nicht nur entlang einer Achse `gut` gegen `schlecht` liegen. Sie koennen eigene Rollenqualitaeten tragen:

- tragende Vorpraegung,
- spannungsnahe Rekopplung,
- balancierter Umschlag,
- offene oder belastete Kippnaehe.

Das spricht fuer ein Bedeutungsnetz mit mehreren Qualitaetsrichtungen, nicht fuer eine einfache Klassenliste.

## Grenze

Diese Lesart bleibt diagnostisch. Sie beschreibt passive Innenfeld-Semantik und darf nicht in Handlung, Richtung oder Strategie uebersetzt werden.

## Wie es weitergeht

Als naechstes sollten die geprueften Brueckenfamilien gemeinsam sortiert werden. Ziel ist eine passive Qualitaetskarte: welche Familien sind tragend vorgepraegt, spannungsnah, balanciert oder randfragmentiert?
