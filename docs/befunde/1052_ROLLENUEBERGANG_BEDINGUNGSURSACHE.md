# 1052 - Bedingungsursache der Rollenübergänge

## Grundfrage

Welche Bedingungsverschiebung erklärt, warum in 1051 die späte Gruppe weniger fragmentierend und stärker rekoppelnd wirkt?

## Unterprüfung

Verglichen wurden:

- `989_MCM_ROLLENNETZWERK_BEDINGUNG_FRUEHE_GRUPPE.csv`
- `990_MCM_ROLLENNETZWERK_BEDINGUNG_SPAETE_GRUPPE.csv`
- `1051_ROLLENUEBERGANG_WELTGRUPPEN_VERGLEICH.csv`

Erzeugte Datei:

- `1052_ROLLENUEBERGANG_BEDINGUNGSURSACHE.csv`

## Ergebnis

Die späte Gruppe zeigt keine völlig neue Feldlogik.

Sie zeigt eine andere Aktivierungsverteilung:

```text
weniger fragmentierte Gesamtaktivität
weniger zentrumsnahe Rückkippung in Fragmentierung
mehr relative Selbstbindung rekoppelnder Rollen
mehr einzelne rekoppelnde Entlastungsformen
```

## Zentrale Unterschiede

| Zustand | Früh | Spät | Veränderung | Deutung |
|---|---:|---:|---:|---|
| `netz_fragmentiert_belastet` Beobachtungen | 3123 | 1627 | -1496 | fragmentierte Belastung wird stark weniger aktiviert |
| `netz_zentrum_mit_anschluss` Beobachtungen | 6819 | 5634 | -1185 | Zentrum bleibt aktiv, aber weniger stark überladen |
| `netz_rekoppelnd_verbunden` Beobachtungen | 499 | 299 | -200 | Gesamtmenge sinkt, aber Selbstbindung steigt |
| `netz_driftend_getragen` Knoten | 22 | 33 | +11 | Drift verteilt sich breiter |
| `netz_rekoppelnd_einzeln` Knoten | 17 | 26 | +9 | kleine Entlastungsformen nehmen zu |
| `netz_zentrum_getragen` Knoten | 0 | 2 | +2 | neue getragene Zentrumsspur erscheint |

## Wichtigste Achsen aus 1051

### Fragmentierung bleibt die stärkste Selbstbindung

```text
fragment_belastet -> fragment_belastet
```

- früh: Rang 1, Gewicht 172
- spät: Rang 1, Gewicht 70

Die Achse bleibt Rang 1, aber ihr Gewicht sinkt deutlich.

Das heißt: Fragmentierung bleibt strukturell vorhanden, aber sie dominiert weniger stark.

### Offene Verbindung bleibt kippsensibel

```text
offen -> fragment_belastet
```

- früh: Rang 2, Gewicht 69
- spät: Rang 2, Gewicht 41

Offenheit bleibt mit Fragmentierung verbunden. Auch diese Achse wird schwächer, bleibt aber stabil sichtbar.

### Rekopplung bindet sich später stärker an sich selbst

```text
rekoppelnd -> rekoppelnd
```

- früh: Rang 13, Gewicht 24
- spät: Rang 3, Gewicht 37

Das ist der wichtigste positive Befund.

Später wird Rekopplung weniger als einzelne Erscheinung gelesen, sondern stärker als eigener zusammenhängender Rollenraum.

## Deutung

Die späte Gruppe wirkt nicht einfach ruhiger.

Sie wirkt reorganisierter:

```text
Fragmentierung bleibt vorhanden,
aber ihre Dominanz sinkt.

Rekopplung wird nicht nur punktuell,
sondern bildet mehr Selbstbindung.
```

Das passt zur Idee einer passiven MCM-Eigenregulation:

- Belastung wird nicht gelöscht.
- Belastung bleibt als Rolle lesbar.
- Das Feld verschiebt aber Gewicht Richtung rekoppelnde und getragenere Nachbarschaften.

## Forschungswert

1052 liefert eine erste Bedingungslesung für Feldreifung:

```text
Feldreifung heißt nicht:
Problemzustand verschwindet.

Feldreifung heißt:
Problemzustand verliert Dominanz,
während Rekopplung und tragende Nachbarschaft stärker organisiert werden.
```

Das ist wichtig für MINI_DIO, weil organische Regulation nicht als harte Korrektur erscheinen sollte, sondern als veränderte Feldverteilung.

## Grenze

Die Auswertung erklärt nicht vollständig, welche Rohweltmerkmale diese Verschiebung auslösen.

Sie zeigt nur die interne Feldseite:

```text
Welche Rollen werden weniger aktiv?
Welche Rollen binden sich stärker?
Welche Rollen erscheinen neu?
```

Der direkte Rohweltvergleich bleibt ein eigener Schritt.

## Nächster Prüfpunkt

Als nächstes sollte die Rohwelt-/Rezeptorseite der beiden Gruppen verglichen werden:

```text
Welche äußere Weltspannung lag bei früher Gruppe vor?
Welche Rezeptorlage lag bei später Gruppe vor?
Warum konnte rekoppelnde Selbstbindung später stärker werden?
```

Das trennt sauber:

```text
Innenfeld-Verschiebung wurde jetzt gelesen.
Welt-/Rezeptorursache muss danach geprüft werden.
```
