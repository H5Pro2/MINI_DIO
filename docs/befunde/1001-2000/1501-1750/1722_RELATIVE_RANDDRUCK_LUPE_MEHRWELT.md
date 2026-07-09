# 1722 - Relative Randdruck-Lupe Mehrwelt

## Frage

Die vorherige Topologie-Matrix zeigte in mehreren Welten eine starke
Zentrumsnaehe. Daraus entstand die methodische Frage:

```text
Ist Randdruck wirklich weg,
oder wird er im Gesamtfeld nur rekoppelt und lokal ueberdeckt?
```

## Methode

Die passive Randdruck-Lupe liest relative Druckprofile innerhalb jeder Welt.
Sie erzeugt keine Runtime-Mechanik und kein Gate.

Gelesen wurden:

- ruhige SOL-Welt,
- stressige SOL-Welt,
- ruhige BTC-Welt,
- stressige BTC-Welt,
- synthetische Rekopplungs-Randwelt,
- synthetisch verschobene Randwelt.

Der vollstaendige Laufbericht liegt unter:

```text
reports/relative_rand_pressure_loupe_probe2.md
```

## Kurzbefund

| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung |
|---|---:|---:|---:|---:|---:|
| SOL ruhig 4000 | 3994 | 0.4046 | 0.1670 | 0.2994 | 0.1289 |
| SOL Stress 4000 | 3994 | 0.4044 | 0.1547 | 0.3082 | 0.1327 |
| BTC ruhig 4000 | 3994 | 0.4069 | 0.1545 | 0.3112 | 0.1274 |
| BTC Stress 4000 | 3994 | 0.4106 | 0.1567 | 0.3087 | 0.1239 |
| Synth Rekopplung 8000 | 7994 | 0.4400 | 0.0962 | 0.4067 | 0.0572 |
| Synth verschoben 8000 | 7994 | 0.4386 | 0.0993 | 0.4046 | 0.0575 |

## Interpretation

Die Realwelten liegen nahe beieinander. Ruhige und stressige Fenster erzeugen
lokal Randdruck, aber keine harte Randdominanz im Gesamtfeld.

Die synthetischen Randwelten zeigen mehr Randdruck und deutlich mehr
Rekopplung. Gleichzeitig sinkt die offene Variante. Das ist wichtig:

```text
Randdruck wird nicht einfach zu Randrolle.
Randdruck kann rekoppeln.
```

Damit trennt sich die Lesung in zwei Ebenen:

```text
Gesamt-Topologie:
  Das Feld bleibt zentrumsnah.

Lokale Randdruck-Lupe:
  Innerhalb dieser zentrumsnahen Ordnung entstehen Randdruckzonen.
```

## Bedeutung fuer MINI_DIO

Der Rand ist nicht verschwunden. Er erscheint nur nicht immer als eigene
dominante Rolle. In der aktuellen Feldorganisation wirkt Rand eher als lokale
Druckzone, die je nach Welt rekoppelt, offen bleibt oder gedaempft wird.

Das spricht gegen eine simple Einteilung:

```text
Zentrum gut, Rand schlecht.
```

Stattdessen entsteht eine differenziertere MCM-Lesung:

```text
Zentrum = Bindung / Gravitation
Rand = lokaler Druckraum
Bruecke = Uebergang und Rekopplung
Offenheit = noch nicht voll verdichtete Variante
Daempfung = reduzierte Aufnahme / stabile Kopplung
```

## Schlussfolgerung

Die Topologie ist nicht nur eine starre Klassentabelle. Sie muss als
Schichtung gelesen werden:

```text
globale Feldrolle
lokaler Druck
Rekopplungsqualitaet
Nachhall
Weltmilieu
```

Das ist fuer die weitere Forschung zentral, weil MINI_DIO dadurch nicht nur
fragt, welche Rolle dominiert, sondern wo innerhalb einer stabilen Rolle
lokaler Druck entsteht.

## Reproduzierbarkeit mit frischer Memory

Zwei Kontrollfaelle wurden mit frischer Memory erneut ausgefuehrt:

- SOL Stress 4000,
- synthetische Rekopplungs-Randwelt 8000.

Der Repro-Bericht liegt unter:

```text
reports/relative_rand_pressure_repro.md
```

Die Kurzprofile waren identisch:

| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung |
|---|---:|---:|---:|---:|---:|
| SOL Stress 4000 Erstlauf | 3994 | 0.4044 | 0.1547 | 0.3082 | 0.1327 |
| SOL Stress 4000 Repro | 3994 | 0.4044 | 0.1547 | 0.3082 | 0.1327 |
| Synth Rekopplung 8000 Erstlauf | 7994 | 0.4400 | 0.0962 | 0.4067 | 0.0572 |
| Synth Rekopplung 8000 Repro | 7994 | 0.4400 | 0.0962 | 0.4067 | 0.0572 |

Auch die Randdruck-Spitzen erschienen an denselben Ticks.

Das bedeutet vorsichtig:

```text
Die lokale Randdruck-Lesung ist in diesen geprueften Welten reproduzierbar.
Sie ist nicht nur eine nachtraegliche Einzelinterpretation eines einmaligen Laufs.
```

Die Aussage bleibt begrenzt auf diese Welten und diese Diagnose.
Sie beweist keine allgemeine Topologie, aber sie staerkt die Methode.
