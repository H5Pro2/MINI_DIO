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
| DOGE | syn_zwischenwelt_b_0_3000 | 34 | 0.147 | 0.000 | 0.000 | 0.853 | -0.407 | `kern_ausgeblendet` |
| DOGE | syn_role_mosaic_afterimage_follow | 34 | 0.088 | 0.059 | 0.029 | 0.824 | -0.428 | `kern_ausgeblendet` |
| DOGE | syn_breadth_afterimage_follow | 34 | 0.000 | 0.000 | 0.000 | 1.000 | -0.650 | `kern_ausgeblendet` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```

## Wie es weitergeht

Als nächstes sollte diese Weltpassung in die passive Feldrollen-Memory übernommen werden. Nicht als Steuerung, sondern als Erfahrungsqualität: welche Weltlagen tragen welchen Kern, und welche lösen Randdrift aus?
