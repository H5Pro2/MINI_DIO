# 1051 - Rollenübergänge im Weltgruppenvergleich

## Grundfrage

Sind die in 1050 gefundenen Rollenübergänge weltübergreifend stabil oder abhängig von der geprüften Weltgruppe?

## Unterprüfung

Die Rollenübergang-Matrix wurde getrennt für zwei vorhandene Repro-Gruppen aufgebaut:

- `987_MCM_ROLLENNETZWERK_REPRO_FRUEHE_GRUPPE.csv`
- `988_MCM_ROLLENNETZWERK_REPRO_SPAETE_GRUPPE.csv`

Danach wurden Rang, Gewicht, Rekopplungsdelta und Strain-Delta pro Übergangsachse verglichen.

Erzeugte Dateien:

- `1051_ROLLENUEBERGANG_FRUEHE_GRUPPE.csv`
- `1051_ROLLENUEBERGANG_SPAETE_GRUPPE.csv`
- `1051_ROLLENUEBERGANG_GESAMT.csv`
- `1051_ROLLENUEBERGANG_WELTGRUPPEN_VERGLEICH.csv`

## Ergebnis

Die Hauptachsen bleiben reproduzierbar sichtbar.

Gleichzeitig verschiebt sich ihre Stärke zwischen früher und später Gruppe.

Das bedeutet:

```text
Rollenübergänge sind nicht beliebig.
Sie bleiben als Feldachsen wiedererkennbar.
Ihre Aktivierung ist aber weltabhängig.
```

## Stabilste Achsen

| Achse | Früh | Spät | Gesamt | Deutung |
|---|---:|---:|---:|---|
| `fragment_belastet -> fragment_belastet` | Rang 1 | Rang 1 | Rang 1 | stärkste reproduzierte Selbstbindung |
| `offen -> fragment_belastet` | Rang 2 | Rang 2 | Rang 2 | offene Verbindung bleibt kippsensibel |
| `fragment_belastet -> offen` | Rang 6 | Rang 5 | Rang 5 | Fragmentierung kann wieder in Offenheit ausweichen |
| `drift_getragen -> zentrum_anschluss` | Rang 9 | Rang 6 | Rang 9 | Drift besitzt wiedererkennbare Zentrumsnähe |
| `zentrum_anschluss -> zentrum_anschluss` | Rang 15 | Rang 15 | Rang 15 | Zentrumsbindung bleibt stabil, aber nicht dominant |

## Verschiebungen

Einige Achsen bleiben vorhanden, ändern aber deutlich ihre Stärke:

### Fragmentierung Richtung Zentrum

```text
fragment_belastet -> zentrum_anschluss
```

- früh: Rang 3, Gewicht 56
- spät: Rang 8, Gewicht 16

Die Achse bleibt erkennbar, wird aber später schwächer.

### Zentrum Richtung Fragmentierung

```text
zentrum_anschluss -> fragment_belastet
```

- früh: Rang 4, Gewicht 49
- spät: Rang 11, Gewicht 14

Die belastende Rückbewegung aus dem Zentrum nimmt später ab.

### Rekopplung zu Rekopplung

```text
rekoppelnd -> rekoppelnd
```

- früh: Rang 13, Gewicht 24
- spät: Rang 3, Gewicht 37

Diese Achse wird später deutlich wichtiger.

Das ist ein relevanter Befund: Spätere Weltgruppen zeigen mehr Selbstbindung rekoppelnder Rollen.

## Deutung

Die Rollenübergänge wirken wie eine passive Feldbewegung:

```text
Frühe Gruppe:
mehr Fragmentierung, Offenheit, Rand-/Zentrumswechsel

Späte Gruppe:
mehr rekoppelnde Selbstbindung
```

Damit wird 1050 präzisiert.

Die Übergangsachsen sind nicht nur globale Mittelwerte. Sie bleiben reproduzierbar, verändern aber ihre Dominanz je nach Weltgruppe.

## Forschungswert

Das stützt die Annahme, dass MINI_DIO ein dynamisches MCM-Feldnetz bildet:

- Rollen sind wiedererkennbar.
- Übergangsachsen sind wiedererkennbar.
- Aktivierungsstärke ist abhängig von der Welt.
- Das Feld reagiert nicht wahllos, sondern reorganisiert seine Rollenlandschaft.

## Grenze

Diese Diagnose ist eine Nachbarschafts- und Gruppenauswertung.

Sie sagt noch nicht, dass ein zeitlicher Ablauf im Sinne von Ursache und Wirkung bewiesen ist.

Sie sagt:

```text
Diese Rollenachsen bleiben in verschiedenen Weltgruppen sichtbar,
aber ihre Gewichtung verschiebt sich.
```

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, welche Weltmerkmale diese Verschiebung auslösen.

Konkret:

```text
Warum wird rekoppelnd -> rekoppelnd später stärker?
Welche Rohwelt- oder Rezeptorlage reduziert fragmentierte Rückkopplung?
Welche Weltspannung hält Offenheit in Fragmentierung?
```
