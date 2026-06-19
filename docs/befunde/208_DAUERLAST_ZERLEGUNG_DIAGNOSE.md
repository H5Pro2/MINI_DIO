# Dauerlast-Zerlegung - Diagnose

Stand: 2026-06-19 04:40:11

## Zweck

Diese Diagnose zerlegt Dauerlast in mehrere passive Quellen.
Sie prueft nicht, ob gehandelt werden soll.

Hierarchie der Pruefung:

1. Grundfrage: Woher kommt Dauerlast im MCM-Feld?
2. Unterpruefung: Sensorik, Nachhall, Memory, Rekopplung und Distanzierung getrennt lesen.
3. Folgeschritt: Entscheiden, ob eine Distanzierungs-Vorstufe notwendig ist.

## Einzelwerte

| Welt | sensorische Last | Persistenz | Nachhall | Aufmerksamkeit | Adaptionskapazitaet | Distanzbedarf | Distanzluecke | Feldlast | Memorylast | Rekopplungsverlust | Dauerlast gesamt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_15m | 0.2038 | 0.2621 | 0.1718 | 0.3555 | 0.6889 | 0.5778 | 0.0000 | 0.0416 | 0.0527 | 0.0088 | 0.0532 |
| BTC_2024_1h | 0.2249 | 0.2886 | 0.1959 | 0.3742 | 0.6495 | 0.6423 | 0.0000 | 0.1389 | 0.1650 | 0.0296 | 0.1223 |
| BTC_2024_30m | 0.2123 | 0.2846 | 0.1770 | 0.3526 | 0.6895 | 0.5986 | 0.0000 | 0.0647 | 0.0898 | 0.0138 | 0.0720 |
| BTC_2024_5m | 0.2221 | 0.3042 | 0.1980 | 0.4110 | 0.6109 | 0.6674 | 0.0565 | 0.0211 | 0.0316 | 0.0034 | 0.0434 |
| BTC_2025_15m | 0.2135 | 0.2751 | 0.1785 | 0.3776 | 0.6674 | 0.6048 | 0.0000 | 0.0396 | 0.0627 | 0.0086 | 0.0558 |
| BTC_2025_1h | 0.2199 | 0.3002 | 0.1900 | 0.3666 | 0.6741 | 0.6354 | 0.0000 | 0.1414 | 0.1740 | 0.0288 | 0.1242 |
| BTC_2025_30m | 0.2055 | 0.2701 | 0.1695 | 0.3502 | 0.6967 | 0.5762 | 0.0000 | 0.0662 | 0.0838 | 0.0169 | 0.0709 |
| BTC_2025_5m | 0.2325 | 0.2751 | 0.2149 | 0.4473 | 0.5831 | 0.6948 | 0.1117 | 0.0221 | 0.0436 | 0.0016 | 0.0485 |
| SOL_2024_15m | 0.1922 | 0.2866 | 0.1570 | 0.3502 | 0.6699 | 0.5628 | 0.0000 | 0.1334 | 0.1550 | 0.0335 | 0.1135 |
| SOL_2024_1h | 0.1912 | 0.3122 | 0.1614 | 0.3538 | 0.6526 | 0.5861 | 0.0000 | 0.3159 | 0.3225 | 0.0530 | 0.2213 |
| SOL_2024_30m | 0.1893 | 0.3072 | 0.1565 | 0.3520 | 0.6615 | 0.5738 | 0.0000 | 0.1830 | 0.2212 | 0.0398 | 0.1477 |
| SOL_2024_5m | 0.2047 | 0.3122 | 0.1706 | 0.3743 | 0.6390 | 0.6097 | 0.0000 | 0.0527 | 0.0747 | 0.0172 | 0.0642 |
| SOL_2025_15m | 0.1921 | 0.3052 | 0.1563 | 0.3512 | 0.6754 | 0.5721 | 0.0000 | 0.1093 | 0.1239 | 0.0245 | 0.0953 |
| SOL_2025_1h | 0.1999 | 0.3007 | 0.1707 | 0.3532 | 0.6717 | 0.5962 | 0.0000 | 0.2944 | 0.2964 | 0.0509 | 0.2084 |
| SOL_2025_30m | 0.1899 | 0.3002 | 0.1573 | 0.3449 | 0.6744 | 0.5690 | 0.0000 | 0.2016 | 0.2177 | 0.0391 | 0.1530 |
| SOL_2025_5m | 0.2004 | 0.3032 | 0.1712 | 0.3821 | 0.6291 | 0.6087 | 0.0000 | 0.0140 | 0.0276 | 0.0035 | 0.0364 |

## Staerkste Dauerlast

- `SOL_2024_1h`: Dauerlast `0.2213`, Feldlast `0.3159`, Memorylast `0.3225`, Rekopplungsverlust `0.0530`
- `SOL_2025_1h`: Dauerlast `0.2084`, Feldlast `0.2944`, Memorylast `0.2964`, Rekopplungsverlust `0.0509`
- `SOL_2025_30m`: Dauerlast `0.1530`, Feldlast `0.2016`, Memorylast `0.2177`, Rekopplungsverlust `0.0391`
- `SOL_2024_30m`: Dauerlast `0.1477`, Feldlast `0.1830`, Memorylast `0.2212`, Rekopplungsverlust `0.0398`

## Staerkste Distanzluecke

- `BTC_2025_5m`: Distanzluecke `0.1117`, Distanzbedarf `0.6948`, Adaptionskapazitaet `0.5831`
- `BTC_2024_5m`: Distanzluecke `0.0565`, Distanzbedarf `0.6674`, Adaptionskapazitaet `0.6109`
- `BTC_2024_15m`: Distanzluecke `0.0000`, Distanzbedarf `0.5778`, Adaptionskapazitaet `0.6889`
- `BTC_2024_1h`: Distanzluecke `0.0000`, Distanzbedarf `0.6423`, Adaptionskapazitaet `0.6495`

## Lesart

- `sensorische Last`: akute Reizueberschreitung gegen lokale Basis.
- `Persistenz`: Anteil der Ticks, in denen die adaptierte Last ueber dem Arbeitsbereich bleibt.
- `Nachhall`: Restspur wiederholter Last nach Adaptation.
- `Adaptionskapazitaet`: Gewoehnung minus Sensitivierung, auf einen tragbaren Bereich bezogen.
- `Distanzluecke`: wenn Distanzbedarf groesser ist als Adaptionskapazitaet.
- `Dauerlast gesamt`: passive Zusammenfassung aus Feldlast, Memorylast, Rekopplungsverlust und Nachhall.

## Befund

Dauerlast ist nicht identisch mit akuter Lautstaerke.
Sie entsteht, wenn Last ueber Zeit im Feld bleibt, Memoryspuren erzeugt und die Rekopplung sinkt.

Die Distanzierungsfrage ist damit fachlich berechtigt:
Wenn Distanzbedarf und Nachhall steigen, aber Adaptionskapazitaet nicht mitkommt, wird Weltspannung zu Innenfeldlast.

## Wie es weitergeht

Als naechstes sollte aus dieser Diagnose ein Befund geschrieben werden.
Darin wird festgehalten, ob SOL 1h eher durch Sensorik, durch Nachhall oder durch Rekopplungsverlust zur Dauerlast wird.
