# 2098 - Präquentielle Erwartungsprüfung relationaler MCM-Eigenzeit-Gaps

## Zweck

Befund 2097 fand eine überzufällige rückblickende Bündelung gemeinsamer
Relationsereignis-Übergänge und Zweischrittpfade. Daraus folgt noch nicht,
dass diese Topologie vor dem nächsten Ereignis innere Anschlussinformation
besitzt.

2098 prüft deshalb strikt vorwärtsgerichtet: Wenn eine Relation gerade einen
Eigenzeit-Gap abgeschlossen hat, ordnet die bis zu diesem Zeitpunkt gewachsene
Gap-Übergangserfahrung ihren später tatsächlich eintretenden nächsten Gap
besser ein als

- die globale bisherige Gap-Häufigkeit aller Relationen und
- die bisherige Gap-Häufigkeit derselben einzelnen Relation?

Es werden keine Außenwerte, Chartbewegungen oder Handlungsergebnisse gelesen.

## Kausale Vorhersageposition

Für eine Relation mit Ereignisfinalisierungen

```text
t1, t2, t3, ...
```

entstehen die Gaps `g1 = t2 - t1`, `g2 = t3 - t2`, ... . Unmittelbar nach
Ereignis `t2` ist `g1` bekannt und `g2` verborgen. Die Prüfung verwendet zu
diesem Zeitpunkt ausschließlich:

- alle globalen Gaps, deren Endereignis höchstens bei `t2` liegt,
- alle Gap-Übergänge, deren zweiter Gap höchstens bei `t2` abgeschlossen ist,
- alle bisherigen Gaps derselben Relation bis `t2`.

Der tatsächliche nächste Gap wird erst anschließend zur Bewertung geöffnet.
In beiden Beständen gibt es keinen Zukunftszugriff.

## Schwellenfreier Rangscore

Kandidaten sind alle bis zur Vorhersageposition global beobachteten exakten
Gap-Werte. Ist der wirkliche nächste Gap noch unbekannt, wird er als neuer
Kandidat mit Zählung null ergänzt.

Jede der drei Erfahrungsquellen ordnet die Kandidaten nach ihrer bisherigen
Rohhäufigkeit. Gleichstände behalten ihren mittleren Rang. Der Rang wird auf
`0` bis `1` abgebildet:

- `1`: höchster bisheriger Rang,
- `0`: niedrigster bisheriger Rang,
- bei vollständig fehlender konditionierter Historie: ungewichteter Gleichstand.

Es gibt keine Glättung, Pseudohäufigkeit, Mindestunterstützung oder
Gap-Zusammenfassung.

## Präquentieller Gesamtvergleich

| Merkmal | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| Vorhersagepositionen | 6.308 | 4.828 |
| bekannte konditionierte Historie | 6.197 | 4.726 |
| Abdeckung | 98,24 % | 97,89 % |
| konditionierter Übergangsscore | 0,86215 | 0,84150 |
| globaler Gap-Häufigkeitsscore | 0,87703 | 0,86016 |
| relationseigener Häufigkeitsscore | 0,75884 | 0,73151 |
| konditioniert minus global | -0,01489 | -0,01867 |
| konditioniert minus relationseigen | +0,10331 | +0,10999 |
| Zukunftszugriffe | 0 | 0 |

Die Übergangstopologie ordnet den nächsten Gap in beiden Beständen schlechter
ein als die einfache globale bisherige Feldhäufigkeit. Gegenüber der sehr
dünnen Einzelhistorie einer Relation ist sie besser, erreicht aber nicht die
kollektive unkonditionierte Erfahrung.

## Direkte Paarvergleiche

| Vergleich zum globalen Score | 2091-Bestand | 2092-Holdout |
|---|---:|---:|
| konditioniert besser | 762 | 677 |
| gleich | 4.421 | 3.022 |
| konditioniert schlechter | 1.125 | 1.129 |
| Gewinnanteil unter Nichtgleichständen | 40,38 % | 37,49 % |

Der negative Mittelwert entsteht damit nicht nur aus wenigen Ausreißern. Unter
den Positionen, an denen sich die beiden Lesungen unterscheiden, verliert die
konditionierte Topologie häufiger als sie gewinnt.

## Relationseigene Gap-Reihenfolgen-Null

Pro Relation bleiben erstes und letztes Ereignis, Ereigniszahl und die
vollständige Multimenge ihrer Gaps erhalten. Nur deren Reihenfolge wird
200-mal permutiert.

| Bestand | beobachtet: konditioniert minus global | Nullmittel | Nullbereich | einseitiges `p` |
|---|---:|---:|---:|---:|
| 2091 | -0,01489 | -0,01306 | -0,01663 bis -0,01010 | 0,9254 |
| 2092 | -0,01867 | -0,01653 | -0,02010 bis -0,01309 | 0,9303 |

Die wirkliche Gap-Reihenfolge erzeugt keinen positiven konditionierten
Vorsprung und liegt auch nicht über ihrer eigenen Reihenfolgenkontrolle.

## Aktivitätserhaltende Ereignisnull

50 Kontrollen bewahren Ereigniszahl jeder Relation, erstes und letztes
Ereignis, Ereignisaktivität jeder Welt und höchstens ein Relationsereignis pro
Finalisierung. Die geringere Permutationszahl dient hier nur der Begrenzung:
Der reale Hauptvergleich ist bereits negativ.

| Bestand | beobachtet: konditioniert minus global | Nullmittel | Nullbereich | einseitiges `p` |
|---|---:|---:|---:|---:|
| 2091 | -0,01489 | -0,01426 | -0,01712 bis -0,00939 | 0,6275 |
| 2092 | -0,01867 | -0,01740 | -0,02250 bis -0,01457 | 0,8824 |

Auch gegenüber dieser strengeren Kontrolle besitzt die wirkliche
Übergangstopologie keinen besonderen Vorwärtseffekt.

Der positive Abstand zur relationseigenen Historie ist ebenfalls nicht
besonders: Die aktivitätserhaltende Null erwartet `+0,10419` beziehungsweise
`+0,11135`; beobachtet werden `+0,10331` und `+0,10999` (`p = 0,6667` und
`p = 0,7255`). Das Poolen vieler Relationen hilft gegenüber einer dünnen
Einzelhistorie, aber nicht aufgrund der wirklichen Gap-Folge.

## Befund

Getragen sind:

- 11.136 strikt kausale Vorhersagepositionen ohne Zukunftszugriff,
- nahezu vollständige Verfügbarkeit einer konditionierten Gap-Historie,
- bessere Einordnung durch kollektive Erfahrung als durch die dünne Historie
  einer einzelnen Relation,
- die globale bisherige Gap-Häufigkeit als beste der drei geprüften
  inneren Lesungen in beiden Beständen.

Nicht getragen sind:

- präquentielle Anschlussinformation der Gap-Übergangstopologie über die
  globale Feldhäufigkeit hinaus,
- ein besonderer Vorteil der wirklichen Gap-Reihenfolge,
- eine vorhersagende Zustandsübergangs-Memory,
- ein Erwartungswert, Gate oder Handlungssignal,
- eine Rücklesung in Feld, Wahrnehmung oder Handlung.

2098 begrenzt Befund 2097: Die Übergangstopologie ist eine reale retrospektive
Ordnung gemeinsamer Entwicklung, aber noch keine innere Erwartungsbildung.
Die kollektive Gap-Häufigkeit ist ein einfacherer und besserer kausaler
Vergleich, ihre bestandübergreifende Übertragbarkeit ist hier jedoch noch
nicht geprüft. An Runtime und Memory wird nichts geändert.

## Reproduzierbare Ausgaben

- `2098_MCM_RELATIONSGAP_PRAEQUENTIELLE_ERWARTUNG.origins.csv`
- `2098_MCM_RELATIONSGAP_PRAEQUENTIELLE_ERWARTUNG.previous_gaps.csv`
- `2098_MCM_RELATIONSGAP_PRAEQUENTIELLE_ERWARTUNG.null.csv`
- `2098_MCM_RELATIONSGAP_PRAEQUENTIELLE_ERWARTUNG.summary.csv`

Die Auswertung liest ausschließlich die kompakten Archive aus 2089 und 2092.
Sie erzeugt keine Welt-, Debug-, Memory- oder Runtime-Dateien.
