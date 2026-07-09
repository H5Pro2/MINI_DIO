# MCM Asset-Feldantwort Balanced Erweitert Bewertung

Stand: 2026-07-02

## Grundfrage

Bleibt die MCM-Grundform auch bei mehr Rohweltfenstern pro Asset erhalten?

## Ergebnis

Die erweiterte Rohwelt-Fensterlupe koppelte `903` Rohfenster.

Die balancierte Assetpruefung nutzte daraus:

```text
6 Assets
36 Fenster pro Asset
216 balancierte Fenster
```

Alle sechs Assetgruppen bleiben in derselben Antwortklasse:

```text
entlastender_bruchkontakt
```

## Bewegungsform

In der balancierten Auswertung gilt fuer alle Assets:

```text
bewegungsbruch
lastkontakt_entlastet
```

Das bestaetigt die bisherige Grundform:

```text
Rohweltbruch -> Randkontakt -> Entlastung
```

## Assetfaerbung

Die Assetfaerbung bleibt messbar verschieden:

| Asset | Lesart |
|---|---|
| SOL | lauteste und staerkste Feldantwort im Sample |
| XRP | starke Entlastung, mittlere bis hohe Lautheit |
| DOGE | hoehere Richtungsunruhe, trotzdem gleiche Entlastung |
| BTC | solide Entlastung bei geringerer Lautheit |
| PAXG | hoechste Expansion, aber nicht staerkste Lautheit |
| KAS | leiseste und schwachste Entlastung, aber gleiche Grundklasse |

## Nebenbefund

Die erweiterte Rohlupe zeigt neben der Hauptform auch kleinere Gegenformen:

- `803` Fenster: `lastkontakt_entlastet + bewegungsbruch`
- `61` Fenster: `rekopplung_bricht_in_last + bewegungsbruch`
- `21` Fenster: `gemischtes_fenster + bewegungsbruch`
- `9` Fenster: `rekopplung_vor_neuer_last + bewegungsbruch`

Das ist wichtig:

```text
Bewegungsbruch fuehrt nicht automatisch zu Entlastung.
Entlastung ist die dominante, aber nicht einzige Feldfolge.
```

## Bedeutung fuer MINI_DIO

Die MCM-Feldantwort wirkt robuster als zuvor:

```text
gleiche Grundform ueber Assets,
aber unterschiedliche innere Faerbung.
```

Damit ist die Topologie nicht einfach assetblind.

Sie liest eine gemeinsame Weltbewegung und bildet gleichzeitig assetbezogene Intensitaet, Lautheit und Entlastungsstaerke aus.

## Grenze

Die Rohweltkopplung verwendet weiterhin nur eindeutig zuordenbare CSV-Welten.

Synthetische und unklare Weltlabels sind nicht in diese Bewertung eingeflossen.

## Schluss

Die erweiterte Pruefung stuetzt die bisherige MCM-Lesung deutlich:

```text
Das Feld reagiert auf Umordnung.
Die Antwort bleibt topologisch stabil.
Die Weltqualitaet faerbt die Feldstaerke.
```

## Wie es weitergeht

Als naechstes sollten die kleineren Gegenformen untersucht werden: Wann wird aus `bewegungsbruch` keine Entlastung, sondern `rekopplung_bricht_in_last` oder `rekopplung_vor_neuer_last`?
