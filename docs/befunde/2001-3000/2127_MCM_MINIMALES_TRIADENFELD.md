# 2127 - Minimales MCM-Triadenfeld

## Zweck

2127 prueft die kleinste Mehrfeldform der Arbeitshypothese, dass mehrere
MCM-Mikrofelder gemeinsam mehr Varianz und relationale Ordnung tragen koennten
als ein einzelnes Feld. Der Versuch verwendet drei baugleiche Mikrofelder mit
je zwoelf Neuronen. Jedes Mikrofeld erhaelt zuerst eine andere reale
Vorgeschichte; danach erleben alle drei dieselbe Zielwelt.

Verglichen werden zwei Diagnosebedingungen:

- isoliert: Die drei Mikrofelder laufen ohne Informationsuebergang.
- verbunden: Jedes Mikrofeld erhaelt die mittlere Gesamtsignatur der beiden
  anderen Felder aus dem vorherigen Tick als aeusseres Grenzsignal.

Die Verbindung ist kausal und symmetrisch. Sie besitzt kein Zentralfeld, keine
semantischen Rollen und keine bevorzugte Mikrofeldidentitaet. Der vorhandene
Kopplungsfaktor der einzelnen Neuronen wird unveraendert wiederverwendet.

## Pruefgrenze

Die gemeinsame Zustandsfolge wird ohne Feldnamen gelesen. Fuer jedes
Mikrofeld werden nur drei relationale Groessen verwendet:

1. Aktivierungen ueber dem feldinternen Mittel,
2. Nachhallwerte ueber dem feldinternen Mittel,
3. Rangabweichungen zwischen Aktivierung und Nachhall.

Eine zeitverschobene Null erhaelt jede lokale Feldfolge vollstaendig und loest
nur ihr Timing gegen die beiden anderen Felder. Dadurch wird gemeinsame
Triadenordnung nicht mit der Ordnung einzelner Mikrofelder verwechselt.

Ein moeglicher Mittelpunkt wird ausschliesslich nachgelagert als
tickweiser Rangmedoid gelesen. Er wirkt nicht auf den Lauf zurueck.

## Umfang

- Entwicklungsbestand: 16 Quelltriaden, 256 Triade-Ziel-Pfade.
- Unabhaengiger Holdout: 15 Quelltriaden, 240 Triade-Ziel-Pfade.
- Je Pfad: verbundene und isolierte Bedingung sowie 32 Zeitnullen.
- Alle 48 beziehungsweise 44 Quellwelten gehen mindestens einmal ein.
- Der Produktionskern bleibt auf allen 496 Pfaden unveraendert.

## Ergebnis

Beide Bedingungen besitzen gegen ihre jeweilige Zeitnull starke
wiederkehrende gemeinsame Uebergangsordnung. Die symmetrische Verbindung
erhoeht diese Ordnung jedoch nicht:

| Bestand | Verbundener Ueberschuss | Isolierter Ueberschuss | Differenz |
| --- | ---: | ---: | ---: |
| 2091 Basis | 1.136.152,66 | 1.153.617,00 | -17.464,34 |
| 2092 Holdout | 1.138.322,75 | 1.153.298,94 | -14.976,19 |

Im Entwicklungsbestand besitzt die Verbindung nur auf `1 von 256` Pfaden
mehr Ueberschuss als die Isolation. Im Holdout sind es `49 von 240` Pfaden.
Auch die getrennten Zieluniversen A und B tragen jeweils dieselbe negative
Gesamtrichtung.

Die mittlere paarweise Zustandsabweichung sinkt leicht von `0,010835` auf
`0,010643` beziehungsweise von `0,010414` auf `0,010101`. Signatur- und
Nachhallvarianz bleiben praktisch unveraendert. Der mediane dauerhafte
Konvergenzzeitpunkt bleibt in der Basis bei Tick 29 und verschiebt sich im
Holdout nur von Tick 28 auf Tick 27.

Ein beweglicher diagnostischer Mittelpunkt erscheint auf 131 von 256
beziehungsweise 116 von 240 verbundenen Pfaden. Er ist damit nicht fest einem
Mikrofeld zugeordnet, bildet aber auch keine durchgehend vorhandene neue
Triadeninstanz.

## Einordnung

Der Lauf widerlegt nicht, dass mehrere Mikrofelder eine tragfaehige
Gesamtorganisation bilden koennen. Er begrenzt die hier gepruefte Form:

> Der symmetrische Austausch globaler mittlerer Feldsignaturen erzeugt keine
> zusaetzliche triadische Ordnung. Er wirkt eher als schwache Angleichung.

Eine Dreierform darf deshalb nicht allein aufgrund ihrer geometrischen
Plausibilitaet oder eines beweglichen diagnostischen Zentrums integriert
werden. Die Zahl drei, die drei Feldplaetze und ihre Verbindung bleiben in
2127 eine transparente Versuchsarchitektur, keine organisch gewachsene
Topologie.

## Architekturentscheidung

- keine Aenderung an `MiniMCMField` oder `MiniMCMNeuron`,
- keine Integration einer Mehrfeld-Runtime,
- kein Triaden-Memory und keine semantische Feldrolle,
- keine Verstaerkung der Kopplung nach Ergebnis,
- kein Handlungsdurchgriff und kein Viranzparameter.

## Reproduzierbarkeit

Ausgaben:

- `2127_MCM_MINIMALES_TRIADENFELD.paths.csv`
- `2127_MCM_MINIMALES_TRIADENFELD.triads.csv`
- `2127_MCM_MINIMALES_TRIADENFELD.summary.csv`

SHA-256:

- `paths`: `6B78477E8E648302F0E6C5281E698C675342D92EB91AD748A2E418268D3D0AA6`
- `triads`: `8B889849F0AEF041522B560AF218CF89B1F04A0434A9A77FB4C719E6162527B0`
- `summary`: `0810529769872A9DB1EC7487633B106B4909DEB588578E5F0FBF9ADBFC63A4AA`

Runner: `tools/run_mcm_minimal_triad_field.py`

Test: `tests/test_mcm_minimal_triad_field.py`
