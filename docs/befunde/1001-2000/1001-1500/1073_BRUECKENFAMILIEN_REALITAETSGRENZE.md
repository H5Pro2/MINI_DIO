# 1073 - Brueckenfamilien Realitaetsgrenze

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1070_REZEPTORHALTUNG_STABILITAET_WELTGRUPPEN.md`
- `1071_REZEPTORHALTUNG_SEMANTISCHE_BINDUNG.md`
- `1072_REZEPTORHALTUNG_FAMILIENUEBERLAPPUNG.md`

## Frage

Sind geteilte Symbolfamilien zwischen `tragende_verarbeitung` und `kippnaehe` echte starke Bruecken, oder nur schwache Uebergangsstellen im Feldnetz?

## Befund

Die Weltgruppen zeigen zwei unterschiedliche Formen von Brueckenbildung:

| Weltgruppe | Geteilte Familien | Familien gesamt | Jaccard | Staerkste Brueckenfamilie | Brueckenwert |
|---|---:|---:|---:|---|---:|
| feld_5m | 28 | 681 | 0.0411 | dio_17ct | 0.0018 |
| real_segment | 7 | 304 | 0.0230 | dio_0g2r | 0.0036 |
| regime | 19 | 680 | 0.0279 | dio_17ct | 0.0015 |
| synthetisch | 4 | 281 | 0.0142 | dio_1fll | 0.0483 |
| zeit_1h | 25 | 707 | 0.0354 | dio_1ewh | 0.0017 |

## Lesart

Die synthetische Weltgruppe zeigt eine auffaellige dominante Bruecke:

```text
dio_1fll
tragend Anteil: 0.9722
kipp Anteil: 0.0483
```

Das ist keine gleichgewichtige Doppelbedeutung. `dio_1fll` ist primär tragend, erscheint aber in einem kleineren Anteil auch kippnah.

In den realen Weltgruppen ist das anders:

- Es gibt mehr geteilte Familien.
- Die einzelne Brueckenstaerke ist deutlich kleiner.
- Die Uebergaenge wirken verteilter und weniger dominant.

## Schluss

Mini-DIO zeigt kein einfaches Umschalten zwischen zwei festen Klassen.

Die bisherige Lesung ist:

```text
tragende Verarbeitung und Kippnaehe bleiben unterscheidbar,
aber das Feld besitzt schwache Uebergangsstellen.
```

Diese Uebergangsstellen sind wichtig, weil sie eine moegliche Feldnetz-Struktur anzeigen. Sie duerfen aber nicht als fertige Bedeutung oder starke Bruecke ueberinterpretiert werden.

## Wissenschaftliche Grenze

Der Befund zeigt eine passive Struktur im aktuellen Datenmaterial. Er beweist noch nicht, dass Mini-DIO eine stabile semantische Brueckenmechanik besitzt.

Stabiler waere der Befund erst, wenn dieselben Brueckenfamilien:

- ueber weitere frische Welten wiederkehren,
- nicht nur synthetisch, sondern realweltlich deutlicher auftreten,
- und gegen Rohweltfenster nachvollziehbar zeigen, wann eine Familie tragend oder kippnah gelesen wird.

## Wie es weitergeht

Als naechstes sollte eine reale Brueckenfamilie, zum Beispiel `dio_17ct` oder `dio_0g2r`, gegen Rohweltfenster gelesen werden. Ziel: verstehen, welche Weltabschnitte dieselbe Familie einmal tragend und einmal kippnah erscheinen lassen.
