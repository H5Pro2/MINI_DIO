# 1791 - `dio_104t` und `dio_14wj`, Kandidatenlupe

## Grundfrage

1790 zeigte, dass reale rekoppelnde Fenster nicht nur mehr Familien tragen, sondern wiederkehrende Kernfamilien besitzen.

Die nächste Frage ist:

```text
Sind `dio_104t` und `dio_14wj` nur häufige Familien,
oder tragen sie unterschiedliche Feldrollen?
```

## Datenbasis

Die Lupe nutzt die in 1790 erzeugten Profile:

- `reports/rekopplung_core_family_roles.csv`
- `reports/rekopplung_core_family_roles_summary.csv`

Verglichen wurden reale BTC-/PAXG-Rekopplungsfenster und synthetische 1787-/1788-Kompaktwelten.

## `dio_104t`

| Quelle | aktive Fenster | Count | Rollenprofil | Dominante Achsen |
|---|---:|---:|---|---|
| BTC real | 3 | 451 | `hoeren_kohaerenz_getragen` | MCM-Kohärenz, Sehen, Hören, Feldaufnahme |
| PAXG real | 3 | 451 | `hoeren_kohaerenz_getragen` | MCM-Kohärenz, Sehen, Hören, Feldaufnahme |
| synthetisch | 0 | 0 | - | - |

### Lesung

`dio_104t` ist in den realen BTC- und PAXG-Rekopplungsfenstern gleich stark vertreten, fehlt aber in den synthetischen Kompaktwelten.

Das spricht dafür, `dio_104t` vorläufig als reale Koherenz-/Anschlussfamilie zu lesen:

```text
dio_104t
  -> realweltlich rekoppelnd
  -> BTC und PAXG gemeinsam
  -> nicht durch synthetische Nachhallstärke allein erzeugt
```

## `dio_14wj`

| Quelle | aktive Fenster | Count | Rollenprofil | Dominante Achsen |
|---|---:|---:|---|---|
| BTC real | 3 | 150 | `hoeren_kohaerenz_getragen` | MCM-Kohärenz, Sehen, schwächeres Hören |
| PAXG real | 3 | 477 | `sehen_kohaerenz_getragen` | MCM-Kohärenz, Sehen, geringe Feldspannung |
| synthetisch | 2 | 227 | `sehen_kohaerenz_getragen` | MCM-Kohärenz, Sehen, geringe Feldspannung |

### Lesung

`dio_14wj` ist deutlich PAXG-näher als BTC-nah. Es erscheint auch synthetisch, aber dort eingebettet in einen engen Familienraum.

Damit ist `dio_14wj` nicht einfach PAXG-exklusiv. Der Unterschied liegt in der Umgebung:

```text
PAXG real:
  dio_14wj + viele Nachbarfamilien + rekoppelnde Breite

synthetisch:
  dio_14wj vorhanden, aber wenige Familien dominieren
```

Vorläufige Lesung:

```text
dio_14wj
  -> ruhige sehende Kohärenzfamilie
  -> PAXG-nah
  -> synthetisch reproduzierbar, aber ohne breiten Kontext nicht rekoppelnd verteilt
```

## Gemeinsame Interpretation

Der Unterschied zwischen beiden Kandidaten ist wichtig:

```text
dio_104t:
  wirkt wie reale Anschluss-/Koherenzfamilie
  fehlt in synthetischer Kompaktbindung

dio_14wj:
  wirkt wie ruhige sehende Kohärenzfamilie
  erscheint real und synthetisch
  braucht aber realen Nachbarschaftsraum, um rekoppelnde Breite zu tragen
```

Damit wird die bisherige MCM-Lesung präziser:

```text
Eine Familie trägt Bedeutung nicht allein.
Bedeutung entsteht aus Familie + Feldprofil + Nachbarschaft + Weltphase.
```

## Grenze

Das ist eine passive Diagnose. Die Namen `dio_104t` und `dio_14wj` werden nicht als feste semantische Wörter gesetzt. Sie sind beobachtete Innenfeld-Familien, deren Bedeutung erst aus Wiederkehr und Kontext gelesen wird.
