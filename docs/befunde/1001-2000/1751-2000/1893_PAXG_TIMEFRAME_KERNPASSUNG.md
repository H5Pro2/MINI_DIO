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
| PAXG | p25_1h_5000_6000 | 31 | 0.226 | 0.161 | 0.258 | 0.355 | 0.110 | `kern_ausgeblendet` |
| PAXG | p24_1h_4000_5000 | 31 | 0.226 | 0.194 | 0.194 | 0.387 | 0.071 | `kern_ausgeblendet` |
| PAXG | p25_1h_4000_5000 | 31 | 0.194 | 0.097 | 0.258 | 0.452 | 0.005 | `kern_ausgeblendet` |
| PAXG | p24_1h_5000_6000 | 31 | 0.194 | 0.161 | 0.194 | 0.452 | -0.008 | `kern_ausgeblendet` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```
