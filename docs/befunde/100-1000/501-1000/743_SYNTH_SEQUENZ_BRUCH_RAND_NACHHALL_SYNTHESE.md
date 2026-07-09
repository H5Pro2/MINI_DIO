# Synthetische Bruch-Rand-Sequenz Nachhall-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft, ob MINI_DIO nur die Dauer einzelner Phasen liest oder auch Sequenzordnung und Nachhall.

Getestet wurden zwei Welten mit denselben Phasen und denselben Laengen:

- `SEQUENZ_ORIGINAL`
- `SEQUENZ_PERMUTIERT`

In der permutierten Welt wurde `randflackern` vor `bruch_impuls` gesetzt.

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Liest MINI_DIO Sequenzordnung oder nur isolierte Phasenqualitaet?
2. Unterpruefung: Bleibt die globale Topologie trotz Permutation stabil?
3. Unterpruefung: Veraendert sich die lokale Rollenlesung einzelner Phasen?
4. Folgeschritt: Nachhall und Sequenzgedaechtnis genauer pruefen.

## Forschungslaeufe

| Lauf | Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|
| 737 | Bruch/Rand original | 6100 | 6094 | 172 | 0.7461 | 0.5985 | 0.9043 |
| 738 | Bruch/Rand permutiert | 6100 | 6094 | 161 | 0.7462 | 0.5985 | 0.9043 |

Befund:

- Beide Varianten reproduzieren Top-Syntax und Top-Familien mit `1.0` Ueberlappung.
- Rekopplung, Carry und Sinneskopplung bleiben global fast identisch.
- Die permutierte Welt bildet weniger eindeutige Syntaxsymbole (`161` statt `172`).

Das spricht gegen globalen Kollaps durch Permutation.
Die Frage verschiebt sich damit auf die lokale Phasenlesung.

## Globale Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|
| SEQUENZ_ORIGINAL | 0.9539 | 0.0456 | 0.0005 | 0.7461 | 0.5985 | 0.9043 |
| SEQUENZ_PERMUTIERT | 0.9524 | 0.0471 | 0.0005 | 0.7462 | 0.5985 | 0.9043 |

Befund:

- Die globale Rollen-Topologie bleibt stabil.
- Die Permutation veraendert die Gesamtordnung kaum.
- Das Feld haelt dieselbe Grundtopologie, obwohl die Weltfolge geaendert wurde.

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|
| SEQUENZ_ORIGINAL | 0.8904 | 0.0711 | 0.0011 | 0.4508 | 0.0115 |
| SEQUENZ_PERMUTIERT | 0.8884 | 0.0727 | 0.0011 | 0.4787 | 0.0115 |

Befund:

- Die permutierte Welt ist minimal offener.
- Hochlastfenster werden in der permutierten Welt offener gelesen.
- Rand/Kippnaehe bleibt gleich niedrig.

## Lokaler Sequenzbefund

Der entscheidende Unterschied liegt in `randflackern` und `bruch_impuls`.

### Original

| Phase | Zentrum | Offen | Rekopplungsnaehe | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| bruch_impuls | 0.8843 | 0.0529 | 0.0629 | 0.7377 | 0.5807 |
| randflackern | 0.2700 | 0.5186 | 0.2100 | 0.6954 | 0.5151 |

### Permutiert

| Phase | Zentrum | Offen | Rekopplungsnaehe | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| randflackern | 0.1857 | 0.5714 | 0.2429 | 0.6924 | 0.5074 |
| bruch_impuls | 0.9529 | 0.0171 | 0.0286 | 0.7407 | 0.5875 |

## Lesart

Wenn `randflackern` vor `bruch_impuls` erscheint, wird es offener gelesen:

```text
Original randflackern:    Offen 0.5186
Permutiert randflackern: Offen 0.5714
```

Danach wird `bruch_impuls` deutlich zentrumsnaeher gelesen:

```text
Original bruch_impuls:    Zentrum 0.8843
Permutiert bruch_impuls: Zentrum 0.9529
```

Das spricht dafuer, dass MINI_DIO nicht nur die Phase selbst liest.
Die vorherige Feldlage wirkt auf die naechste Phase nach.

Kurz:

```text
Gleiche Phase.
Andere Reihenfolge.
Andere lokale Feldrolle.
```

## MCM-Bedeutung

Dieser Befund passt zur Nachhall-Hypothese:

```text
Eine Weltlage endet nicht einfach.
Sie hinterlaesst eine Feldspur,
die beeinflusst, wie die folgende Weltlage gelesen wird.
```

Damit wird Feldzeit konkreter:

```text
Feldzeit ist nicht nur Dauer.
Feldzeit beinhaltet Sequenzordnung und Nachhall.
```

## Grenze

Die globale Topologie bleibt fast gleich.
Das ist wichtig:

- Die Permutation zerlegt MINI_DIO nicht.
- Die grossen Bedeutungsfamilien bleiben stabil.
- Die lokale Phasenlesung veraendert sich trotzdem.

Damit ist der Befund kein Beweis fuer beliebige Sequenzintelligenz.
Er zeigt eine kontrollierte Spur von sequenzabhaengiger Innenfeldwirkung.

## Bedeutung fuer MINI_DIO

Fuer MINI_DIO bedeutet das:

1. Phasen duerfen nicht nur isoliert gelesen werden.
2. Die vorherige Feldlage ist Teil der aktuellen Wahrnehmung.
3. Nachhall ist eine echte Diagnoseachse.
4. Feldzeit sollte als Sequenz- und Integrationsspur gelesen werden.

Das passt zur bisherigen Richtung:

```text
nicht harte Zeit programmieren,
sondern Nachhall und Feldbewegung aus dem Innenfeld lesen.
```

## Wie es weitergeht

Als naechstes sollte eine zweite Permutation getestet werden, die `rekopplung` vor die Randphase setzt. Ziel: pruefen, ob ein rekoppelter Vorzustand Randoeffnung abfedert oder nur die gleiche lokale Randreaktion verschiebt.
