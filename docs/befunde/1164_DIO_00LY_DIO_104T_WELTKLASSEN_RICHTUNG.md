# 1164 - Weltklassenrichtung zwischen `dio_00ly` und `dio_104t`

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundfrage

In welchen Weltklassen ist die Beziehung `dio_00ly <-> dio_104t` balanciert, und in welchen Weltklassen kippt sie eher zu Uebergang oder Stabilisierung?

## Methode

Grundlage ist die zeitliche Naehepruefung aus `1159-1162`.

Gelesen wurde nur das Paar:

```text
dio_00ly <-> dio_104t
```

Pro Weltklasse wurde gezaehlt:

- wie oft `dio_00ly` und `dio_104t` innerhalb von 12 Ticks nahe beieinander liegen,
- ob `dio_00ly` eher vor `dio_104t` liegt,
- ob `dio_104t` eher vor `dio_00ly` liegt,
- ob die Richtung balanciert bleibt.

## Ergebnis

| Weltklasse | Nahe Ereignisse | Naehe pro `dio_00ly` | Richtung | Lesart |
|---|---:|---:|---|---|
| PAXG 2024 5m | 46 | 74.19% | balanciert | Rueckbezugsraum |
| BTC 2024 1h | 62 | 81.58% | balanciert | Rueckbezugsraum |
| KAS 2024 5m | 66 | 73.33% | `dio_00ly -> dio_104t` | Uebergang zu Stabilisierung |
| Expansion 2023 | 16 | 72.73% | `dio_104t -> dio_00ly` | Stabilisierung zu Uebergang |
| SOL 2026 Seitwaerts | 42 | 80.77% | balanciert | Rueckbezugsraum |
| BTC 2024 quiet | 102 | 75.00% | `dio_104t -> dio_00ly` | Stabilisierung zu Uebergang |
| Negative Stress 2024 | 18 | 64.29% | `dio_00ly -> dio_104t` | Uebergang zu Stabilisierung |
| Positive Recovery 2025 | 26 | 76.47% | balanciert | Rueckbezugsraum |

## Technische Deutung

Die Beziehung ist in allen Weltklassen vorhanden.

Die Richtung ist aber weltabhaengig:

```text
balanciert:
PAXG 5m, BTC 1h, SOL Seitwaerts, Positive Recovery

Uebergang -> Stabilisierung:
KAS 5m, Negative Stress

Stabilisierung -> Uebergang:
Expansion, BTC quiet
```

Damit ist `dio_00ly <-> dio_104t` keine starre Kette.

Die Beziehung wirkt eher wie ein gemeinsamer Feldbereich, dessen Richtung durch Weltspannung moduliert wird.

## MCM-Lesart

`dio_00ly` wurde als Uebergangsbruecke gelesen.

`dio_104t` wurde als rekopplungsnahe Stabilitaetsbruecke gelesen.

Die Weltklassenrichtung zeigt:

```text
Wenn die Welt Druck oder Umordnung erzeugt,
kann Uebergang in Stabilisierung laufen.

Wenn die Welt stabiler oder expansiver wirkt,
kann Stabilisierung wieder Uebergang oeffnen.

Wenn beide Rollen gleich stark miteinander schwingen,
entsteht balancierter Rueckbezug.
```

Das ist fuer die MCM-Feldforschung wichtig, weil es ein dynamisches Netz zeigt:

- gleiche Familien,
- gleiche Naehe,
- unterschiedliche Richtung je nach Weltklasse.

## Grenze

Die Richtung ist eine Ticknaehe-Lesung, keine kausale Aussage.

Noch nicht gesagt ist:

- ob die Richtung bei anderen Tickfensterbreiten gleich bleibt,
- ob Segmentkanten dieselbe Richtung zeigen,
- ob die Balancierung ein stabiler Zentrumseffekt ist.

## Wie es weitergeht

Als naechstes sollte die Fensterbreite geprueft werden: bleibt die Richtung bei 6, 12 und 24 Ticks aehnlich, oder ist die Achsenrichtung nur ein Artefakt des gewaehlten Nahfensters?
