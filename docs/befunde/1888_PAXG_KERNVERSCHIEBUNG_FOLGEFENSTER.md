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
| PAXG | real2025_5m | 31 | 0.387 | 0.161 | 0.290 | 0.161 | 0.408 | `kern_getragen` |
| PAXG | follow8000_9000 | 31 | 0.419 | 0.097 | 0.226 | 0.258 | 0.345 | `kern_getragen` |
| PAXG | real2025_1h | 31 | 0.452 | 0.097 | 0.161 | 0.290 | 0.334 | `kern_getragen` |
| PAXG | follow5000_6000 | 31 | 0.323 | 0.097 | 0.323 | 0.258 | 0.282 | `kern_verschoben` |
| PAXG | shift2024_5m | 31 | 0.387 | 0.065 | 0.161 | 0.387 | 0.202 | `kern_ausgeblendet` |
| PAXG | follow6000_7000 | 31 | 0.323 | 0.129 | 0.194 | 0.355 | 0.179 | `kern_ausgeblendet` |
| PAXG | real2024_1h | 31 | 0.387 | 0.097 | 0.097 | 0.419 | 0.163 | `kern_ausgeblendet` |
| PAXG | follow7000_8000 | 31 | 0.355 | 0.065 | 0.129 | 0.452 | 0.116 | `kern_ausgeblendet` |
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
