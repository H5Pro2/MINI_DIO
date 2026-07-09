# 1162 - Zeitliche Feldfolge der Brueckenachsen

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundfrage

Ist die Beziehung zwischen `dio_00ly` und `dio_104t` nur metrisch, oder treten die Familien auch zeitlich/feldfolgend nahe beieinander auf?

Gepruefte Achsenkette:

```text
dio_00ly -> dio_0g2r -> dio_1ewh -> dio_104t
```

Zusatzvergleich:

```text
dio_00ly <-> dio_104t
```

## Methode

In acht Weltklassen wurden die Episodenreihen passiv durchsucht.

Fuer jede Familie wurden Tickpositionen gelesen. Danach wurde geprueft, ob eine andere Familie innerhalb eines Fensters von `12` Ticks in derselben Laufspur liegt.

Das ist keine Handlungsauswertung. Es ist eine zeitliche Naehepruefung im Bedeutungsfeld.

## Zusammenfassung

| Paar | Nahe Ereignisse | Naehe bezogen auf linke Familie | Richtung | Lesart |
|---|---:|---:|---|---|
| `dio_00ly` / `dio_0g2r` | 72 | 14.40% | eher `dio_0g2r -> dio_00ly` | lockere Vor-/Ruecknaehe |
| `dio_0g2r` / `dio_1ewh` | 90 | 34.35% | eher `dio_0g2r -> dio_1ewh` | mittlere Zwischennaehe |
| `dio_1ewh` / `dio_104t` | 288 | 73.85% | eher `dio_1ewh -> dio_104t` | starke Stabilitaetsnaehe |
| `dio_00ly` / `dio_104t` | 378 | 75.60% | nahezu balanciert | gemeinsamer Feldbereich / Rueckbezug |

## Technische Deutung

Die Nachbarschaft ist nicht nur metrisch.

Alle vier geprueften Paare treten ueber alle acht Weltklassen hinweg zeitlich nahe auf.

Der staerkste Befund ist:

```text
dio_00ly <-> dio_104t
```

Rund drei Viertel der `dio_00ly`-Vorkommen liegen in Naehe von `dio_104t`.

Die Richtung ist fast balanciert:

```text
dio_00ly -> dio_104t: 192
dio_104t -> dio_00ly: 186
```

Das spricht nicht fuer eine einfache lineare Kette. Es spricht eher fuer einen gemeinsamen Feldbereich oder Rueckbezugsraum.

## Achsenkette

Die Zwischenkette zeigt ebenfalls Struktur:

```text
dio_0g2r -> dio_1ewh -> dio_104t
```

Besonders `dio_1ewh` liegt haeufig nahe an `dio_104t`.

Das passt zur bisherigen Lesart:

- `dio_0g2r` = offene rekoppelbare Bruecke
- `dio_1ewh` = tragend vorgepraegter Anker
- `dio_104t` = rekopplungsnahe Stabilitaetsbruecke

Die Kette wirkt damit nicht wie ein harter Ablauf, sondern wie ein Nachbarschaftsgradient:

```text
offene Rekopplung
-> tragende Vorpraegung
-> stabile Rekopplung
```

## Bedeutung fuer die MCM-Feldforschung

Der Befund ist ein wichtiger Schritt:

```text
metrische Naehe
+ zeitliche Naehe
= staerkerer Hinweis auf Feldtopologie
```

MINI_DIO zeigt hier nicht nur wiederholte Symbole. Es zeigt eine Beziehung zwischen Bedeutungsfamilien:

- Familien liegen in Feldzeit nahe beieinander.
- Familien bilden Rueckbezuege.
- Zwischenfamilien koennen einen Gradienten bilden.
- Hauptachsen koennen balanciert umeinander auftreten.

Das ist eine deutlich staerkere Lesart als reine Symbolwiederkehr.

## Grenze

Diese Pruefung nutzt Ticknaehe, nicht vollstaendige Segmentuebergaenge.

Noch offen:

- ob die Familien echte Segmentkanten bilden,
- ob gleiche Naehe bei laengeren Welten stabil bleibt,
- ob die Richtung je nach Weltklasse kippt,
- ob `dio_00ly` und `dio_104t` einen gemeinsamen Zentrum-/Brueckenbereich bilden.

## Wie es weitergeht

Als naechstes sollte die Beziehung nach Weltklasse getrennt gelesen werden: In welchen Welten ist `dio_00ly <-> dio_104t` balanciert, und in welchen Welten kippt die Richtung eher zu Uebergang oder Stabilisierung?
