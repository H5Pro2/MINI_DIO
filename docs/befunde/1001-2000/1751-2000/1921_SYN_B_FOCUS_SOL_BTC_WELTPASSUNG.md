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
| BTC | syn_b_focus_2400_3900 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |
| BTC | syn_b_focus_3000_4500 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |
| BTC | syn_b_focus_3200_5200 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |
| SOL | syn_b_focus_2400_3900 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |
| SOL | syn_b_focus_3000_4500 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |
| SOL | syn_b_focus_3200_5200 | 27 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```
