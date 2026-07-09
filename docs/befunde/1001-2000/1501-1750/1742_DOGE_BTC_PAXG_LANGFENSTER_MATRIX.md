# 1742 DOGE/BTC/PAXG Langfenster-Matrix

Stand: 2026-07-08

## Grundfrage

Bleibt die robuste MCM-Topologie auch dann erhalten, wenn neben PAXG und BTC eine weitere längere Gegenwelt geprüft wird?

## Unterprüfung

Geprüft wurden lange Weltfenster über drei Milieus:

- PAXG 2025: 5m 10k, 15m 3333, 1h 10k
- BTC 2025: 5m 10k, 15m 3333, 1h full
- DOGE 2024/2025: 5m 10k, 15m 3333, 1h 10k

Die DOGE-15m-Welten wurden aus den vorhandenen DOGE-5m-10k-Welten aggregiert.

Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Befund

Alle zwölf geprüften Welten bleiben in der Topologieklasse `stark_zentriert_wenig_rand`.

Damit wird die bisherige Grundlinie bestätigt:

```text
Die Topologie bleibt robust.
Die lokale Feldfärbung wandert.
```

DOGE verhält sich in dieser Langfenster-Matrix sehr nah an BTC. Beide zeigen eine enge Zentrumslage mit sehr geringer offener Variante und ohne sichtbaren globalen Rand-/Kippanteil. PAXG bleibt dagegen der offenere Pol, besonders in 5m und 1h.

## Kurzmatrix

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| PAXG 2025 5m | 0.8725 | 0.1202 | 0.0073 | 0.7144 | 0.5410 | 0.1517 | 0.8561 |
| PAXG 2025 15m | 0.9922 | 0.0078 | 0.0000 | 0.7025 | 0.5305 | 0.1652 | 0.8449 |
| PAXG 2025 1h | 0.8098 | 0.1857 | 0.0045 | 0.7061 | 0.5357 | 0.1519 | 0.8437 |
| BTC 2025 5m | 0.9902 | 0.0098 | 0.0000 | 0.7075 | 0.5529 | 0.1698 | 0.8424 |
| BTC 2025 15m | 0.9856 | 0.0144 | 0.0000 | 0.7007 | 0.5328 | 0.1668 | 0.8418 |
| BTC 2025 1h | 0.9897 | 0.0103 | 0.0000 | 0.7083 | 0.5532 | 0.1691 | 0.8429 |
| DOGE 2024 5m | 0.9897 | 0.0103 | 0.0000 | 0.7070 | 0.5527 | 0.1707 | 0.8408 |
| DOGE 2024 15m | 0.9856 | 0.0144 | 0.0000 | 0.7001 | 0.5328 | 0.1677 | 0.8398 |
| DOGE 2024 1h | 0.9903 | 0.0097 | 0.0000 | 0.7069 | 0.5516 | 0.1701 | 0.8411 |
| DOGE 2025 5m | 0.9911 | 0.0089 | 0.0000 | 0.7069 | 0.5526 | 0.1706 | 0.8413 |
| DOGE 2025 15m | 0.9841 | 0.0159 | 0.0000 | 0.7003 | 0.5330 | 0.1674 | 0.8408 |
| DOGE 2025 1h | 0.9894 | 0.0106 | 0.0000 | 0.7065 | 0.5516 | 0.1708 | 0.8400 |

## Lesart

Die MCM-Topologie wirkt in diesen Welten nicht wie eine starre Ausgabeform, sondern wie eine robuste Feldordnung mit lokaler Milieu-Färbung.

PAXG zeigt:

- mehr offene Variante,
- niedrigeren Strain,
- stärkere Sinneskopplung,
- mehr phasenartige Öffnung in 5m und 1h.

BTC und DOGE zeigen:

- engere Zentrumslage,
- sehr kleine offene Variante,
- höhere Strain-Werte,
- geringere Sinneskopplung als PAXG,
- sehr ähnliche lokale Feldfärbung zueinander.

Damit entsteht vorläufig eine Dreiteilung:

```text
PAXG = offener, rekopplungsstärker, phasenreicher
BTC  = kompakt zentrumsstabil
DOGE = kompakt zentrumsstabil, nahe BTC
```

## Folgeschluss

Die Topologie ist nach dieser Prüfung stabiler als die einzelnen Asset-Milieus.

Das ist relevant für die MCM-Forschung, weil es zwei Ebenen trennt:

```text
Feldordnung       = wiederkehrende Grundstruktur
Weltfärbung       = lokale Ausprägung durch Asset, Zeitmaß und Sinnesaufnahme
```

Damit wird MINI_DIO nicht nur als Symbolzählung lesbar, sondern als Feldsystem, das ähnliche Grundordnung unter verschiedenen Weltmilieus hält und zugleich Unterschiede in Offenheit, Dämpfung, Strain und Rekopplung ausdrückt.

## Verweise

- [doge_btc_paxg_long_topology.md](../../../../reports/doge_btc_paxg_long_topology.md)
- [doge_btc_paxg_long_randdruck.md](../../../../reports/doge_btc_paxg_long_randdruck.md)
- [1741_BTC_PAXG_2025_LANGFENSTER_VERGLEICH.md](1741_BTC_PAXG_2025_LANGFENSTER_VERGLEICH.md)

## Wie es weitergeht

Als nächstes sollte die robuste Topologie gegen eine Welt geprüft werden, die nicht nur ein anderes Asset, sondern eine andere Strukturqualität trägt: KAS mit längerem Fenster, sobald verfügbar, oder eine gezielt synthetisch erzeugte Außenwelt mit kontrolliertem Bruch, Ruhe und Expansion.
