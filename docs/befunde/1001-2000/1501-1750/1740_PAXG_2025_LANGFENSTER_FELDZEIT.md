# 1740 - PAXG 2025 Langfenster Und Feldzeit

## Fragestellung

Die vorherige Prüfung zeigte im verschobenen PAXG-2025-Folgefenster mehr Dämpfung und etwas weniger Rekopplung.

Die neue Frage:

```text
Ist diese Dämpfung eine längere PAXG-2025-Tendenz
oder nur eine lokale Phase innerhalb einer größeren Feldbewegung?
```

## Datengrundlage

Geprüft wurden längere PAXG-2025-Fenster:

- 5m mit 9994 Episoden,
- 15m mit 3327 Episoden,
- 1h mit 8754 Episoden.

Die 15m-Welt wurde aus dem 5m-10k-Fenster aggregiert.

## Kernergebnis

Alle drei Langfenster bleiben:

```text
stark_zentriert_wenig_rand
```

Damit bleibt die Topologie auch bei längerer Feldzeit stabil.

## Neue Qualität

Im längeren Fenster werden offene Varianten stärker sichtbar:

| Zeitachse | Zentrum | Offen | Rand/Kipp | Rekopplung |
|---|---:|---:|---:|---:|
| 5m | 0.8725 | 0.1202 | 0.0073 | 0.7144 |
| 15m | 0.9922 | 0.0078 | 0.0000 | 0.7025 |
| 1h | 0.8098 | 0.1857 | 0.0045 | 0.7061 |

Das ist wichtig: Längere Feldzeit macht Offenheit und kleine Kippanteile sichtbar, ohne dass daraus Randdominanz entsteht.

## Interpretation

Die SHIFT1-Dämpfung war keine einfache Gesamttendenz. Im Langfenster zeigt PAXG 2025 weiter starke Rekopplung und gleichzeitig mehr offene Variante.

Die bessere Lesart:

```text
PAXG 2025 enthält lokale Dämpfungsphasen.
Über längere Feldzeit bleibt die Rekopplungsstruktur aber stark.
Offene Varianten werden sichtbarer, ohne die Topologie zu brechen.
```

Damit wird Feldzeit als Tiefenachse konkreter: kurze Fenster lesen Momentfärbung, längere Fenster zeigen mehr Rollenbreite.

## Bedeutung Für MINI_DIO

Der Befund stützt die bisherige MCM-Lesart:

- Topologie ist stabiler als lokale Feldfärbung.
- Feldzeit bringt zusätzliche Tiefe.
- Offenheit ist nicht automatisch Störung.
- Kleine Kippnähe kann als Randdruck sichtbar werden, ohne das Zentrum zu verlieren.

## Grenze

Der 15m-Lauf ist aggregiert und kürzer als 5m/1h. Für eine vollständig symmetrische Prüfung wäre eine echte 15m-10k-Welt sinnvoll, falls Rohdaten verfügbar werden.

## Referenzen

- [paxg_2025_long_window_summary.md](../../../../reports/paxg_2025_long_window_summary.md)
- [paxg_2025_long_window_topology.md](../../../../reports/paxg_2025_long_window_topology.md)
- [paxg_2025_long_window_randdruck.md](../../../../reports/paxg_2025_long_window_randdruck.md)

## Wie es weitergeht

Als nächstes sollte eine andere Welt mit vergleichbarer Länge geprüft werden. KAS oder BTC wären sinnvoll, weil wir damit trennen können, ob lange Feldzeit allgemein offene Varianten verstärkt oder ob PAXG hier besonders reagiert.
