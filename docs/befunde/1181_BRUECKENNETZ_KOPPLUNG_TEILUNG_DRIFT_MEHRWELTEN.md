# 1181 - Brueckennetz: Kopplung, Teilung oder Drift in weiteren Welten

## Grundfrage

Verhalten sich die gefundenen Brueckenachsen in weiteren Welten als:

- Kopplung eines gemeinsamen Raums,
- Teilung in getrennte Inseln,
- oder Drift mit verschobener Gewichtung?

Geprueft wurden zehn weitere Asset-/Zeitwelten:

- PAXG, DOGE, XRP, BTC, SOL auf 5m
- PAXG, DOGE, XRP, BTC, SOL auf 1h

Die Pruefung bleibt passiv. Keine Handlung, kein Gate, keine Strategie.

## Ergebnis

In allen zehn geprueften Welten wurde das Brueckennetz als `kopplung_geteilter_raum` gelesen.

| Welt | Paare | `dio_00ly -> dio_104t` | `dio_104t -> dio_00ly` | Cosinus | Jaccard | Lesung |
|---|---:|---:|---:|---:|---:|---|
| PAXG 2024 5m | 384 | 196 | 188 | 0.9480 | 0.6753 | Kopplung |
| DOGE 2024 5m | 518 | 236 | 282 | 0.9825 | 0.6698 | Kopplung |
| XRP 2024 5m | 488 | 176 | 312 | 0.9651 | 0.6524 | Kopplung |
| BTC 2024 5m | 98 | 36 | 62 | 0.9364 | 0.5802 | Kopplung |
| SOL 2024 5m | 84 | 32 | 52 | 0.8662 | 0.3922 | Kopplung |
| PAXG 2024 1h | 506 | 224 | 282 | 0.9688 | 0.6141 | Kopplung |
| DOGE 2024 1h | 464 | 202 | 262 | 0.9859 | 0.5765 | Kopplung |
| XRP 2024 1h | 462 | 192 | 270 | 0.9809 | 0.6167 | Kopplung |
| BTC 2024 1h | 130 | 48 | 82 | 0.9513 | 0.5806 | Kopplung |
| SOL 2024 1h | 80 | 40 | 40 | 0.8887 | 0.3776 | Kopplung |

## Lesart

Die Brueckenachsen teilen sich ueber weitere Welten hinweg einen gemeinsamen Bedeutungsraum.

Es gibt keine saubere Teilung in zwei getrennte Inseln.

Gleichzeitig gibt es Drift:

- manche Welten haben mehr `dio_104t -> dio_00ly`,
- manche sind fast balanciert,
- die Nachbarschaftsgewichte verschieben sich,
- aber der gemeinsame Raum bleibt erhalten.

Das ist wichtig: MINI_DIO bildet hier kein starres Symbolpaar, sondern ein Netz.

## Normalisierte Kandidatengewichtung

Die rohen Kandidatenzahlen waren verzerrt, weil manche Welten mehr Paare in einer Richtung hatten. Deshalb wurde pro Paar normalisiert.

Nach Normalisierung zeigen sich leichte Biasgruppen:

Staerker bei `dio_104t -> dio_00ly`:

- `dio_1kpz`
- `dio_0tay`
- `dio_0oc3`

Staerker bei `dio_00ly -> dio_104t`:

- `dio_1uof`
- `dio_06s7`
- `dio_1lsu`
- `dio_17ct`
- `dio_1r55`
- `dio_00ja`

Diese Biaswerte sind keine fertigen Bedeutungen. Sie zeigen lokale Gewichtung innerhalb eines gemeinsamen Brueckennetzes.

## MCM-Deutung

Der Befund passt zu einer evolutionsaehnlichen Feldorganisation:

- Aehnliche Innenlagen koppeln.
- Wiederkehrende Nachbarschaften verdichten.
- Richtungen driften je nach Weltspannung.
- Der gemeinsame Raum bleibt tragend, statt sofort in getrennte Klassen zu zerfallen.

Das sieht eher nach lebender Feldorganisation als nach fester Symboltabelle aus.

## Grenze

Die Pruefung zeigt Kopplung und Drift im Nachbarschaftsraum.

Sie beweist noch nicht:

- dass MINI_DIO diese Biasfamilien als eigene Bedeutung kennt,
- dass daraus eine autonome Regulation entsteht,
- oder dass die Richtung eine Ursache-Folge-Beziehung ist.

Die sauberste naechste Pruefung ist daher:

Sind die Biasfamilien selbst feldrollengebunden?

Also:

- Liegt `dio_1kpz` wirklich naeher an Stabilisierung/Rueckbindung?
- Liegt `dio_1uof` wirklich naeher an Uebergang/Oeffnung?
- Oder sind diese Familien nur Oberflaechen-Nachbarn?

## Kurzfazit

Die weiteren Welten bestaetigen Kopplung, nicht Teilung.

MINI_DIO zeigt ein gemeinsames Brueckennetz mit richtungsabhaengiger Drift. Das ist fachlich staerker als eine einzelne Symbolueberlappung, aber noch vorsichtiger zu lesen als eine gereifte, getrennte Bedeutung.

