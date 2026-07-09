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
| BTC | btc_b_focus_3000_4500 | 27 | 0.111 | 0.037 | 0.037 | 0.815 | -0.400 | `kern_ausgeblendet` |
| SOL | sol_b_focus_3000_4500 | 27 | 0.111 | 0.037 | 0.037 | 0.815 | -0.400 | `kern_ausgeblendet` |
| SOL | sol_b_focus_2400_3900 | 27 | 0.037 | 0.037 | 0.074 | 0.852 | -0.485 | `kern_ausgeblendet` |
| BTC | btc_b_focus_2400_3900 | 27 | 0.074 | 0.037 | 0.000 | 0.889 | -0.498 | `kern_ausgeblendet` |
| BTC | btc_b_focus_3200_5200 | 27 | 0.037 | 0.000 | 0.037 | 0.926 | -0.552 | `kern_ausgeblendet` |
| DOGE | syn_b_focus_3200_5200 | 34 | 0.029 | 0.000 | 0.029 | 0.941 | -0.572 | `kern_ausgeblendet` |
| DOGE | syn_b_focus_2400_3900 | 34 | 0.000 | 0.059 | 0.029 | 0.912 | -0.574 | `kern_ausgeblendet` |
| SOL | sol_b_focus_3200_5200 | 27 | 0.037 | 0.000 | 0.000 | 0.963 | -0.589 | `kern_ausgeblendet` |
| DOGE | syn_b_focus_3000_4500 | 34 | 0.000 | 0.029 | 0.000 | 0.971 | -0.626 | `kern_ausgeblendet` |

## Lesung

Die stärksten Weltpassungen entstehen dort, wo der harte Kern überwiegend getragen bleibt und nur wenig ausgeblendet wird.
Schwache Weltpassung bedeutet nicht, dass das Feld leer ist. Es bedeutet, dass diese Weltlage den bisherigen Kern nicht sauber trägt und ihn eher öffnet, verschiebt oder ausblendet.

Damit wird Reife als Beziehung lesbar:

```text
Hartkern + Weltlage -> getragen / geöffnet / verschoben / ausgeblendet
```

## Wie es weitergeht

Als nächstes sollte diese Weltpassung in die passive Feldrollen-Memory übernommen werden. Nicht als Steuerung, sondern als Erfahrungsqualität: welche Weltlagen tragen welchen Kern, und welche lösen Randdrift aus?
