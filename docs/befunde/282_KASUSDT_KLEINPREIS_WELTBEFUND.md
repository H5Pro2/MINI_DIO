# Befund: KASUSDT als Kleinpreis-Welt

Stand: 2026-06-19

## Zweck

Diese Datei haelt den ersten KASUSDT-Test fest.

KASUSDT wurde aufgenommen, weil der Preisbereich deutlich kleiner ist als bei SOL oder BTC.
Damit prueft KAS, ob die weltrelative Sinnesaufnahme wirklich preisniveauunabhaengiger arbeitet.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Datenbau

KASUSDT war ueber Binance Spot fuer 2024 in der verwendeten Monatsdatenquelle nicht verfuegbar.
Darum wurde der Data-Builder um Binance Futures-UM erweitert.

Erzeugt wurden:

| Datei | Markt | Zeitebene | Kerzen | Preisbereich |
|---|---|---|---:|---|
| kontrolliert_kas_2024_5m_test1_2000_KASUSDT.csv | futures_um | 5m | 2000 | 0.07594 bis 0.12430 |
| kontrolliert_kas_2024_1h_test1_2000_KASUSDT.csv | futures_um | 1h | 2000 | 0.07594 bis 0.19026 |

## Topologiebefund

Beide KAS-Welten bleiben im gleichen Topologiezustand:

```text
zentrum_mit_rand_und_uebergang
```

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| KAS_2024_5M_2K | 0.8004 | 0.1575 | 0.0421 | 0.6451 | 0.3963 | 0.1869 | 0.8645 |
| KAS_2024_1H_2K | 0.7984 | 0.1560 | 0.0456 | 0.6445 | 0.3940 | 0.1865 | 0.8639 |

## Interpretation

KAS verschiebt die Rollenanteile leicht:

- etwas weniger Zentrum als BTC 2025,
- etwas mehr offene Variante,
- Rand/Kipp bleibt klein,
- Sinnes-MCM-Kopplung bleibt nahe bei SOL/BTC.

Das ist relevant, weil KAS auf absolutem Preisniveau deutlich anders liegt.

Die aktuelle Lesart:

```text
world_relative verhindert, dass der kleine Preisbereich die MCM-Lesung zerlegt.
```

Damit wird die Annahme staerker, dass MINI_DIO nicht nur absolute Preisgroesse liest, sondern Weltspannung relativ zur jeweiligen Welt aufnehmen kann.

## Grenze

Der Test ist noch klein:

- nur 2024,
- je 2000 Kerzen,
- Futures-UM statt Spot,
- noch keine Reproduktion,
- noch keine 15m/30m-Zwischenebenen.

## Wie es weitergeht

Als naechstes sollte KAS reproduziert werden:

1. KAS 5m und KAS 1h erneut mit frischem Memory laufen lassen,
2. Delta gegen `281` berechnen,
3. danach KAS 15m/30m pruefen.

Wenn KAS ebenfalls exakt oder sehr nah reproduziert, ist das ein wichtiger Befund fuer preisniveauunabhaengige MCM-Feldaufnahme.
