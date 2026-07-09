# 1088 - Feldfolgensignatur dio_155c

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1086_BRUECKENFAMILIE_DIO_155C_EINZELEREIGNISSE.md`
- `1087_BRUECKENFAMILIE_DIO_155C_TICKFENSTER.md`
- `1082_BRUECKENFAMILIEN_GRUNDREGEL.md`

## Frage

Ist `dio_155c` eine echte Brueckenfamilie oder eher ein randnahes Kontaktfragment?

## Aggregierter Befund

`dio_155c` erscheint in beiden Lesarten, ist aber deutlich spannungsnaeher als `dio_1ewh`.

| Lesart | Ereignisse | Spannung | Rekopplung | Strain | Spannungsdelta | Rekopplungsdelta |
|---|---:|---:|---:|---:|---:|---:|
| tragende_verarbeitung | 52 | 0.0990 | 0.7313 | 0.1355 | -0.0173 | 0.0285 |
| kippnaehe | 38 | 0.1342 | 0.6957 | 0.1759 | 0.0313 | -0.0084 |

## Tragende Lesart

Bei tragender Verarbeitung zeigt `dio_155c`:

- mittlere bis erhoehte Spannung,
- klare Rekopplung,
- niedrigeren Strain,
- haeufig stabile scharfe Form,
- Ereignispunkt mit Feldlabel `rekoppelt`.

Beispiel:

```text
Tick 1244: tragende_verarbeitung
Spannung 0.1021
Rekopplung 0.7568
Strain 0.1376
Feld: rekoppelt
```

Die tragende Lesart wirkt nicht wie ruhige Zentrumslage, sondern wie ein spannungsnaher Kontakt, der noch sauber rueckgekoppelt werden kann.

## Kippnahe Lesart

Bei Kippnaehe zeigt `dio_155c`:

- deutlich hoehere Spannung,
- niedrigere Rekopplung,
- hoeheren Strain,
- positive Spannungszunahme gegen das Vorfenster,
- teils direkte `belastet_kippnah`-Umgebung.

Beispiel:

```text
Tick 10: kippnaehe
Spannung 0.1094
Rekopplung 0.6535
Strain 0.1785
Feld: offen / belastet_kippnah
```

In den Tickfenstern liegt um kippnahe Ereignisse haeufig bereits offene oder belastete Feldlage. Der Nachlauf kann wieder entlasten, aber die Ereignislesart selbst bleibt randnaher als bei den staerker tragenden Familien.

## Schluss

`dio_155c` ist keine reine Rauschfamilie.

Es ist eine echte Brueckenfamilie mit Randnaehe:

```text
dio_155c = spannungsnaher Brueckenanker
tragend, wenn Rekopplung gelingt
kippnah, wenn Spannung und Strain steigen und Rekopplung faellt
```

Damit bestaetigt `dio_155c` die Grundregel, aber mit anderer Qualitaet als `dio_1ewh`:

- `dio_1ewh` wirkt tragend vorgepraegt,
- `dio_155c` wirkt spannungs- und randnaeher,
- beide bleiben kontextabhaengige Anker statt fester Bedeutungen.

## Bedeutung fuer MINI_DIO

MINI_DIO bildet nicht nur Zentrum und Rand, sondern auch Zwischenrollen:

- ruhiger tragender Anker,
- spannungsnaher tragender Anker,
- offener Kippkontakt,
- belasteter Randkontakt.

Das spricht fuer ein differenziertes Bedeutungsnetz innerhalb des MCM-Feldes. Die gleiche Form von Wiederkehr kann verschiedene Feldqualitaeten tragen.

## Grenze

Diese Lesart bleibt diagnostisch. Sie beschreibt passive Innenfeld-Semantik und darf nicht in Handlung, Richtung oder Strategie uebersetzt werden.

## Wie es weitergeht

Als naechstes sollte `dio_1gp2` als weitere Vergleichsfamilie geprueft werden. Danach koennen die Brueckenfamilien nach Qualitaet sortiert werden: tragend vorgepraegt, spannungsnah tragend, kippnah offen oder randfragmentiert.
