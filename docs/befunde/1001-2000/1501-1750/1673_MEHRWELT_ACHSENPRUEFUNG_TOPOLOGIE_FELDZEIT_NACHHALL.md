# Mehrwelt-Achsenprüfung: Topologie, Feldzeit, Nachhall und Rollenbreite

Stand: 2026-07-07

## Zweck

Diese Prüfung führt die bisher getrennten Achsen zusammen:

```text
Topologie
Feldzeit
Nachhall
Rollenbreite
```

Die Grundfrage:

```text
Tragen diese Achsen gemeinsam,
oder wirken sie nur einzeln stabil?
```

Die Prüfung nutzt die bereits erzeugten 2000er-Segmente aus drei realen 10k-Welten:

- `negative_stress_2023_10k`
- `positive_expansion_2023_10k`
- `sideways_2026_10k`

Sinnesmodus:

```text
calibrated_relative
```

## Gemeinsame Achsentabelle

| Welt | Start | Rollen | Kombis | Syntax | Stabil | Unruhig | Kippend | Gespannt | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| negative_stress | 0 | 2/2 | 1/1 | 383 | 1472 | 504 | 18 | 0 | 0.692433 | 0.126551 |
| negative_stress | 2000 | 4/4 | 6/6 | 314 | 1681 | 303 | 9 | 1 | 0.700541 | 0.159969 |
| negative_stress | 4000 | 2/2 | 1/1 | 274 | 1703 | 276 | 15 | 0 | 0.702411 | 0.181988 |
| negative_stress | 6000 | 3/3 | 3/3 | 330 | 1560 | 422 | 11 | 1 | 0.696504 | 0.138270 |
| negative_stress | 8000 | 4/4 | 6/6 | 441 | 1437 | 528 | 28 | 1 | 0.689311 | 0.109644 |
| positive_expansion | 0 | 4/4 | 6/6 | 312 | 1605 | 371 | 18 | 0 | 0.698394 | 0.148830 |
| positive_expansion | 2000 | 3/3 | 3/3 | 437 | 1433 | 532 | 28 | 1 | 0.688532 | 0.107891 |
| positive_expansion | 4000 | 5/5 | 10/10 | 394 | 1393 | 580 | 20 | 1 | 0.689427 | 0.100488 |
| positive_expansion | 6000 | 5/5 | 10/10 | 415 | 1472 | 498 | 24 | 0 | 0.689402 | 0.118277 |
| positive_expansion | 8000 | 3/3 | 3/3 | 304 | 1633 | 346 | 15 | 0 | 0.697626 | 0.155083 |
| sideways | 0 | 7/7 | 19/19 | 274 | 1745 | 240 | 8 | 1 | 0.702821 | 0.174799 |
| sideways | 2000 | 5/5 | 10/10 | 330 | 1555 | 425 | 14 | 0 | 0.694790 | 0.139279 |
| sideways | 4000 | 2/2 | 1/1 | 348 | 1604 | 376 | 14 | 0 | 0.695582 | 0.138300 |
| sideways | 6000 | 3/3 | 3/3 | 335 | 1510 | 467 | 16 | 1 | 0.694012 | 0.139838 |
| sideways | 8000 | 6/6 | 14/14 | 331 | 1616 | 361 | 16 | 1 | 0.696020 | 0.145656 |

## Befund 1: Die Achsen Tragen Gemeinsam

Die Achsen wirken nicht isoliert.

Rollenbreite, Nachhall und Rekopplung verändern sich gemeinsam mit der Feldrollenlage:

```text
enge Kopplung
  -> wenige Rollen / wenige Kombinationen

verteilte Feldlage
  -> mehr Rollen / mehr Kombinationen

höherer Nachhall
  -> nicht automatisch mehr Rollen
  -> oft stärkere Integration oder Fokussierung
```

Damit ist Rollenbreite nicht einfach ein Rohweltwert.
Sie ist eine Binnenfeld-Eigenschaft.

## Befund 2: Nachhall Ist Nicht Gleich Breite

Der stärkste Gegenpunkt gegen eine einfache Deutung:

```text
negative_stress Start 4000:
Rollen 2/2, Kombinationen 1/1, Nachhall 0.181988
```

Das ist hoher Nachhall bei enger Bindung.

Im Gegensatz dazu:

```text
positive_expansion Start 4000:
Rollen 5/5, Kombinationen 10/10, Nachhall 0.100488
```

Das ist breite Rollenöffnung bei niedrigerem Nachhall.

Schluss:

```text
Nachhall misst nicht einfach Menge oder Breite.
Nachhall misst eher zeitliche Integrationsspur.
```

## Befund 3: Topologie Ist Nicht Nur Stabilität

`sideways Start 0` zeigt:

```text
Rollen 7/7
Kombinationen 19/19
Stabil 1745
Unruhig 240
Rekopplung 0.702821
Nachhall 0.174799
```

Das ist breite Rollenöffnung trotz hoher Stabilität.

Topologie bedeutet daher nicht:

```text
stabil = eng
unruhig = breit
```

Sondern:

```text
Topologie = Feldordnung aus Stabilität, Nachhall, Rekopplung und Rollenanschluss.
```

## Befund 4: Weltklassen Sind Nicht Starr

Jede Welt zeigt Binnenphasen:

- Stress kann eng sein oder mittlere Rollenbreite öffnen.
- Expansion kann breit werden oder wieder fokussieren.
- Seitwärts kann sehr breit beginnen, enger werden und später wieder öffnen.

Damit ist die relevante Ebene nicht nur:

```text
Welche Weltklasse ist das?
```

Sondern:

```text
Welche Feldphase wirkt innerhalb dieser Welt?
```

## Wissenschaftliche Anschlussstelle

Diese Achsenprüfung stützt die Priorisierung aus `1672`:

1. **Feldzeit / Nachhall** ist methodisch stark, weil es Struktur, Nullwelt und Stress unterscheiden kann.
2. **Topologie** ist breit bestätigt, weil Rollenordnungen über Welten wiederkehren.
3. **Verteilte Rollennetze** erklären, warum Bedeutung als Beziehungsmuster reifen kann.
4. **Offline-Feld-Reorganisation** kann später auf diesen gemeinsamen Achsen geprüft werden.

## MCM-Lesung

MINI_DIO zeigt hier keine simple Symboltabelle.

Das Feld verhält sich eher wie ein dynamischer Ordnungsraum:

```text
Weltkontakt
  -> Feldrollen
  -> Nachhall
  -> Rekopplung
  -> Rollenbreite
  -> Bedeutungsraum
```

Der zentrale Befund:

```text
MCM-Feldordnung ist mehrdimensional.
Keine einzelne Achse erklärt das Verhalten allein.
```

## Grenze

Diese Prüfung bleibt passiv.

Sie zeigt:

- keine Handlung,
- keine Strategie,
- kein aktives Entscheiden,
- keine bewusste Auswahl.

Sie zeigt aber, dass mehrere passive Achsen gemeinsam lesbare Feldordnung bilden.

## Wie es weitergeht

Als nächstes sollte ein kompakter Mehrwelt-Report automatisiert werden, der diese vier Achsen pro Welt direkt aus neuen Läufen ausgibt. Dadurch können spätere Welten schneller gegen Topologie, Feldzeit, Nachhall und Rollenbreite geprüft werden.
