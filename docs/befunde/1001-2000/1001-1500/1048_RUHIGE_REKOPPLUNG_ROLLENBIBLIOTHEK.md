# 1048 - Rollenbibliothek ruhige Rekopplung

## Grundfrage

Ist `ruhige_rekopplung` eine einzelne syntaktische Familie oder eine übergeordnete MCM-Feldrolle, die von mehreren Familien getragen werden kann?

## Unterprüfung

Aus der Kandidatenmatrix `1047_RUHIGE_REKOPPLUNGSROLLEN_ASSET_KANDIDATEN.csv` wurden alle Familien nach Weltenhäufigkeit, Rekopplungsqualität, Nachhall, Kontaktlast, Hör-/Feldabstand und Ruhescore aggregiert.

Die daraus erzeugte Tabelle liegt hier:

- `1048_RUHIGE_REKOPPLUNG_ROLLENBIBLIOTHEK.csv`

## Ergebnis

`ruhige_rekopplung` ist keine Einzelfamilie.

Die Rolle erscheint als wiederkehrende Feldfunktion, die über mehrere syntaktische Familien getragen werden kann. Damit verschiebt sich die Lesart:

```text
Nicht: dieses Wort ist die Bedeutung.
Sondern: mehrere Worte können dieselbe Feldrolle tragen.
```

Das ist wichtig für MINI_DIO, weil Bedeutung damit nicht nur als Token, sondern als wiederkehrende Feldfunktion gelesen werden muss.

## Wichtigste Rollenträger

| Familie | Welten | Gesamtzahl | mittlerer Ruhescore | Nachhall | Zeitvertrauen | Deutung |
|---|---:|---:|---:|---:|---:|---|
| `dio_1fll` | 4 | 634 | 0.8112 | 0.3026 | 0.7618 | scharfer, sehr stabiler Rollenträger |
| `dio_06er` | 6 | 456 | 0.7959 | 0.1799 | 0.7111 | breit weltübergreifend getragen |
| `dio_0kx9` | 6 | 268 | 0.7956 | 0.1257 | 0.6931 | breit, aber weniger nachhallstark |
| `dio_1jc2` | 5 | 283 | 0.7966 | 0.1485 | 0.7063 | stabiler Mehrwelt-Träger |
| `dio_1492` | 5 | 143 | 0.7958 | 0.1347 | 0.6884 | stabil, eher schmaler |
| `dio_14wj` | 5 | 939 | 0.7938 | 0.3294 | 0.7829 | besonders breit und nachhallstark |

## Deutung

`dio_1fll` wirkt wie ein klarer Kernträger der Rolle: hohe Qualität, niedrige Kontaktlast und in den geprüften Welten durchgehend starke Platzierung.

`dio_14wj` wirkt anders: nicht maximal scharf, aber deutlich breiter, häufiger und nachhallstärker. Das spricht für eine tragende, länger im Feld bleibende Rekopplungsrolle.

`dio_06er`, `dio_0kx9`, `dio_1jc2` und `dio_1492` zeigen, dass die Rolle nicht an ein einzelnes Zeichen gebunden ist. MINI_DIO bildet also eher eine Rollenfamilie als ein Einzelwort.

## Forschungswert

Der Befund spricht für eine semantische Schichtung:

```text
Syntaxfamilie -> Feldrolle -> Bedeutungsraum
```

Eine Familie kann lokal wichtig sein, ohne die Rolle allein zu definieren. Eine Rolle kann stabil bleiben, obwohl ihre sprachliche Oberfläche zwischen Welten variiert.

Damit wird MINI_DIOs Gedächtnis nicht als reine Wortliste gelesen, sondern als beginnende Rollenbibliothek des MCM-Feldes.

## Grenze

Die Rollenbibliothek ist noch passiv. Sie beschreibt keine Handlung und keine Strategie.

Sie zeigt nur:

- welche Familien ähnliche Feldfunktionen tragen,
- welche Rollen über mehrere Welten wiederkehren,
- welche Träger scharf, breit, nachhallstark oder lokal sind.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, ob eine andere Rolle ebenfalls rollenförmig getragen wird. Geeignet wäre eine belastete Randrolle oder eine offene Brückenrolle.

Damit wird sichtbar, ob die Rollenbildung nur bei ruhiger Rekopplung erscheint oder ob MINI_DIO generell Feldfunktionen über mehrere Syntaxfamilien organisiert.
