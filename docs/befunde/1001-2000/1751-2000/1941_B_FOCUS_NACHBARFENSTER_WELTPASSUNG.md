# 1941 - B-Fokus Nachbarfenster: Weltpassungs-Metrik

## Grundfrage

Ist die Restkopplung bei `3000_4500` nur ein punktueller Treffer, oder liegt dort ein breiterer Weltform-Bereich, der den SOL- und BTC-Hartkern teilweise tragen kann?

## Methode

Verglichen wurden drei gleich lange B-Fokusfenster:

- `2800_4300`
- `3000_4500`
- `3200_4700`

Gelesen wurde nur der harte Kern von SOL und BTC. Die Metrik ist passiv: keine Handlung, kein Gate, keine Richtung.

## Ergebnis

| Asset | Weltlage | Kernpaare | getragen | geöffnet | verschoben | ausgeblendet | Score | Lesung |
|---|---|---:|---:|---:|---:|---:|---:|---|
| BTC | `btc_b_focus_2800_4300` | 27 | 0.111 | 0.074 | 0.037 | 0.778 | -0.370 | `kern_ausgeblendet` mit stärkster Restkopplung |
| BTC | `btc_b_focus_3000_4500` | 27 | 0.111 | 0.037 | 0.037 | 0.815 | -0.400 | `kern_ausgeblendet` mit Restkopplung |
| SOL | `sol_b_focus_3000_4500` | 27 | 0.111 | 0.037 | 0.037 | 0.815 | -0.400 | `kern_ausgeblendet` mit Restkopplung |
| SOL | `sol_b_focus_2800_4300` | 27 | 0.074 | 0.000 | 0.074 | 0.852 | -0.454 | `kern_ausgeblendet` mit verschobener Restkopplung |
| BTC | `btc_b_focus_3200_4700` | 27 | 0.111 | 0.000 | 0.000 | 0.889 | -0.467 | `kern_ausgeblendet` mit schmaler Nullnähe |
| SOL | `sol_b_focus_3200_4700` | 27 | 0.111 | 0.000 | 0.000 | 0.889 | -0.467 | `kern_ausgeblendet` mit schmaler Nullnähe |

## Lesung

`3000_4500` ist kein isolierter Einzelpunkt. Es liegt in einem Restkopplungsband.

Die Nachbarn zeigen aber unterschiedliche Qualität:

- Links (`2800_4300`) koppelt BTC stärker und offener. SOL koppelt schwächer, aber nicht leer.
- Mitte (`3000_4500`) koppeln SOL und BTC symmetrisch: 3 getragen, 1 geöffnet, 1 verschoben.
- Rechts (`3200_4700`) bleibt bei beiden nur eine schmalere Nullnähe-Reproduktion ohne Öffnung oder Verschiebung.

Damit entsteht keine harte Punktlogik, sondern eine Feldzone:

```text
linke Zone  -> offener / asset-spezifischer
Mitte       -> gemeinsame SOL/BTC-Restkopplung
rechte Zone -> schmaler, nullnäher, weniger offen
```

## Bedeutung für MINI_DIO

Der Befund hilft DIO, weil Weltpassung als Bereich gelesen werden kann, nicht als einzelnes Signal.

Für die MCM-Mechanik heißt das:

- Restkopplung kann zonal auftreten.
- Innerhalb derselben Zone verändern sich Rollen: offen, getragen, verschoben, ausgeblendet.
- Weltpassung ist keine binäre Entscheidung, sondern ein Feldverlauf.
- Die passive Memory kann solche Zonen als Erfahrungsqualität speichern, ohne daraus Handlung abzuleiten.

## Methodische Grenze

Alle Ergebnisse bleiben passive Feldlesung. Die Metrik beschreibt nur, wie stark eine Weltlage einen bestehenden Hartkern sichtbar hält.

## Wie es weitergeht

Als nächstes sollte geprüft werden, welche Familien über alle drei Nachbarfenster stabil bleiben. Das zeigt, ob die Zone aus denselben Trägern besteht oder ob jede Teilzone andere Familien aktiviert.
