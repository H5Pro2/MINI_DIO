# Reale gekoppelte Feldlast Rollenfolge Bewertung

Stand: 2026-07-01

## Grundfrage

Welche Feldrolle liegt vor und nach realer `gekoppelte_feldlast` beziehungsweise `spannungsrand_kippnaehe`?

Nach aktueller Auswertung: Die staerksten realen Rand/Kipp-Fenster sind fast durchgehend `bewegungsbruch` und laufen danach ueberwiegend in `offene_variante`.

## Grundlage

Die Auswertung liegt in:

- `docs/befunde/1001-2000/1001-1500/1237_REALE_GEKOPPELTE_FELDLAST_ROHWELTFENSTER_5M.md`
- `docs/befunde/1001-2000/1001-1500/1237_REALE_GEKOPPELTE_FELDLAST_ROHWELTFENSTER_5M.csv`

Ausgewertet wurden die 80 lautesten realen Rand/Kipp-Segmente aus den aktuellen 5m Stress-/Quiet-Welten.

## Hauptbefund

Bewegungsart:

```text
bewegungsbruch: 80 von 80
```

Vorherige Rolle:

```text
zentrum_stabil: 43
offene_variante: 21
rekopplungsnaehe: 16
```

Naechste Rolle:

```text
offene_variante: 71
zentrum_stabil: 5
rekopplungsnaehe: 4
```

Haeufigste Sequenz:

```text
zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante: 38
```

## Bedeutung

Reale gekoppelte Feldlast wirkt in diesen Laeufen nicht wie ein langer Dauerdruck.

Sie erscheint eher als kurzer Bruchzustand:

```text
stabile Feldnaehe
-> ploetzlicher Bewegungs-/Energiebruch
-> offener Entlastungs- oder Neuordnungsraum
```

Das passt zur bisherigen MCM-Feldphasenlesung:

- Zentrum ist kein starres Stillstehen.
- Rand/Kipp ist kurz und hoch belastet.
- Offenheit ist haeufig die direkte Nachphase, in der das Feld wieder Bewegungsraum bekommt.

## Fachliche Grenze

Diese Diagnose beschreibt keine Handlung und keine Strategie.

Sie beschreibt nur, wie MINI_DIO im passiven Feldlesen reale Hochlastfenster als Rollenfolge ordnet.

## Schlussfolgerung

Die reale Rand/Kipp-Rolle ist in der aktuellen Rezeptorschicht keine isolierte Einzelachse. Sie ist ein gekoppelter Bruchpunkt zwischen zentrumsnaher Ordnung und offener Neuordnung.

Das ist fuer MINI_DIO relevant, weil daraus eine bessere passive Innenfeldmechanik entsteht:

```text
Feldlast wird nicht nur gemessen.
Sie wird in einer zeitlichen Rollenfolge gelesen.
```

## Wie es weitergeht

Als naechstes sollte dieselbe Rollenfolge auf 1h-Welten geprueft werden. Ziel ist zu sehen, ob `zentrum -> Rand/Kipp -> Offenheit` nur auf 5m sichtbar ist oder auch in groberer Weltzeit erhalten bleibt.
