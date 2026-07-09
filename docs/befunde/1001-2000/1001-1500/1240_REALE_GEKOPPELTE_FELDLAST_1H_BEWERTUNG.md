# Reale gekoppelte Feldlast 1h Bewertung

Stand: 2026-07-01

## Grundfrage

Bleibt die Rollenfolge realer `gekoppelte_feldlast` auch in groberer Weltzeit erhalten?

Nach aktueller 1h-Pruefung: ja. Die Struktur aus 5m bleibt fast deckungsgleich sichtbar.

## Grundlage

Die Auswertung liegt in:

- `docs/befunde/1001-2000/1001-1500/1239_REALE_GEKOPPELTE_FELDLAST_ROHWELTFENSTER_1H.md`
- `docs/befunde/1001-2000/1001-1500/1239_REALE_GEKOPPELTE_FELDLAST_ROHWELTFENSTER_1H.csv`

Ausgewertet wurden die 80 lautesten 1h-Rand/Kipp-Segmente aus den aktuellen SOL/BTC Stress-/Quiet-Welten.

## Hauptbefund

Bewegungsart:

```text
bewegungsbruch: 80 von 80
```

Vorherige Rolle:

```text
zentrum_stabil: 45
rekopplungsnaehe: 19
offene_variante: 16
```

Naechste Rolle:

```text
offene_variante: 73
rekopplungsnaehe: 5
zentrum_stabil: 2
```

Haeufigste Sequenz:

```text
zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante: 39
```

## Vergleich zu 5m

Der 5m-Befund lautete:

```text
bewegungsbruch: 80 von 80
zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante: 38
nach Rand/Kipp meist offene_variante: 71 von 80
```

Der 1h-Befund lautet:

```text
bewegungsbruch: 80 von 80
zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante: 39
nach Rand/Kipp meist offene_variante: 73 von 80
```

Damit ist die Rollenfolge nicht nur ein 5m-Artefakt.

## Bedeutung

Die reale gekoppelte Feldlast wirkt in beiden Weltzeiten als kurzer Bewegungsbruch zwischen Ordnung und Neuordnung:

```text
zentrumsnahe oder rekoppelnde Ordnung
-> Rand/Kipp als Bruchpunkt
-> offene Variante als Entlastungs- und Neuordnungsraum
```

Das ist ein starker Hinweis, dass MINI_DIO hier eine wiederkehrende Feldphasenmechanik liest und nicht nur einzelne Rohkerzen.

## Grenze

Die Pruefung umfasst SOL/BTC Stress-/Quiet-Welten in 5m und 1h.

Sie sagt noch nicht, ob dieselbe Sequenz bei PAXG, KAS, DOGE, XRP oder synthetischen Extremwelten gleich bleibt.
