# 1878 - Weltpassungs-Metrik

Diese Diagnose liest, wie gut eine Weltlage den harten Kern der lokalen Reifegruppe trägt.
Die Metrik ist passiv: Sie erzeugt keine Handlung, kein Gate und keine Richtung.

## Zustände

- `getragen`: dieselbe lokale Qualität wird reproduziert.
- `geöffnet`: der Kern bleibt sichtbar, verliert aber Schärfe.
- `verschoben`: der Kern bleibt anschlussfähig, wechselt aber in Kernnähe, Nachhall, Nullnähe oder Drift.
- `ausgeblendet`: das Kernpaar fehlt im Folgefenster.

## Ergebnis

| Asset | Weltlage | Kernpaare | getragen | geöffnet | verschoben | ausgeblendet | Score | Lesung |
|---|---|---:|---:|---:|---:|---:|---:|---|
| BTC | stress | 27 | 0.704 | 0.074 | 0.222 | 0.000 | 0.793 | `kern_getragen` |
| SOL | stress | 27 | 0.741 | 0.111 | 0.111 | 0.037 | 0.772 | `kern_getragen` |
| XRP | real2024 | 28 | 0.679 | 0.107 | 0.179 | 0.036 | 0.734 | `kern_getragen` |
| SOL | expansion | 27 | 0.667 | 0.111 | 0.111 | 0.111 | 0.650 | `kern_getragen` |
| BTC | ruhig | 27 | 0.593 | 0.111 | 0.222 | 0.074 | 0.639 | `kern_getragen` |
| SOL | ruhig | 27 | 0.667 | 0.148 | 0.037 | 0.148 | 0.606 | `kern_getragen` |
| DOGE | follow5000_6000 | 34 | 0.529 | 0.176 | 0.206 | 0.088 | 0.571 | `kern_getragen` |
| DOGE | real2024 | 34 | 0.471 | 0.235 | 0.206 | 0.088 | 0.521 | `kern_getragen` |
| BTC | follow5000_6000 | 27 | 0.444 | 0.296 | 0.185 | 0.074 | 0.506 | `kern_getragen` |
| XRP | follow5000_6000 | 28 | 0.464 | 0.179 | 0.179 | 0.179 | 0.438 | `kern_getragen` |
| PAXG | real2025_5m | 31 | 0.387 | 0.161 | 0.290 | 0.161 | 0.408 | `kern_getragen` |
| PAXG | real2025_1h | 31 | 0.452 | 0.097 | 0.161 | 0.290 | 0.334 | `kern_getragen` |
| PAXG | follow5000_6000 | 31 | 0.323 | 0.097 | 0.323 | 0.258 | 0.282 | `kern_verschoben` |
| PAXG | shift2024_5m | 31 | 0.387 | 0.065 | 0.161 | 0.387 | 0.202 | `kern_ausgeblendet` |
| PAXG | real2024_1h | 31 | 0.387 | 0.097 | 0.097 | 0.419 | 0.163 | `kern_ausgeblendet` |
| PAXG | real2024_5m | 31 | 0.129 | 0.161 | 0.194 | 0.516 | -0.115 | `kern_ausgeblendet` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```

## Wie es weitergeht

Als nächstes sollte diese Weltpassung in die passive Feldrollen-Memory übernommen werden. Nicht als Steuerung, sondern als Erfahrungsqualität: welche Weltlagen tragen welchen Kern, und welche lösen Randdrift aus?
