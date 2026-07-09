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
| DOGE | d25_1h_3000_4000 | 34 | 0.500 | 0.118 | 0.147 | 0.235 | 0.416 | `kern_getragen` |
| DOGE | d25_1h_0_1000 | 34 | 0.353 | 0.176 | 0.265 | 0.206 | 0.338 | `kern_getragen` |
| DOGE | d25_1h_2000_3000 | 34 | 0.471 | 0.118 | 0.118 | 0.294 | 0.338 | `kern_getragen` |
| DOGE | d25_1h_1000_2000 | 34 | 0.235 | 0.382 | 0.147 | 0.235 | 0.191 | `kern_geoeffnet` |
| DOGE | d25_1h_4000_5000 | 34 | 0.176 | 0.235 | 0.324 | 0.265 | 0.153 | `kern_verschoben` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```
