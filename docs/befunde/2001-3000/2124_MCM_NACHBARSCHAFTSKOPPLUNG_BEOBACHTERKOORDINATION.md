# 2124 - Nachbarschaftskopplung und Beobachterkoordination

## Fragestellung

2123 zeigte, dass die gemeinsame Ereigniszeit von relativer Aktivierungs- und
Nachhallstuetze nicht als Summe voneinander unabhaengiger lokaler
Neuronenspuren erklaert werden kann. Offen blieb, ob der kollektive Anteil aus
der gemeinsamen Aussenanregung oder aus der internen Nachbarschaftsweitergabe
des aktuellen MCM-Feldes entsteht.

2124 bildet deshalb fuer jeden Feldpfad ein diagnostisches Paar:

1. das unveraenderte gekoppelte MCM-Feld,
2. ein Kontrollfeld mit identischer Aussenwelt, identischen Gewichten und
   identischer Nachhallmechanik, aber ohne Signalweitergabe zwischen Neuronen.

Die Kontrolle ist nur ein Forschungsinstrument. Der produktive Feldkern wird
nicht veraendert.

## Isolierter Mechanismus

Im bestehenden `MiniMCMField` wird jedes Neuron sequenziell verarbeitet. Das
erste Neuron erhaelt den Nachbarschaftswert `0`; jedes folgende Neuron erhaelt
die aktuelle Aktivierung seines direkten Vorgaengers. In `MCMNeuron.step`
wirkt dieses Signal mit dem fest vorgegebenen Faktor `0,12`.

Die diagnostische Kontrolle setzt ausschliesslich den uebergebenen
Nachbarschaftswert fuer alle Neuronen auf `0`. Erhalten bleiben:

- dieselben weltrelativen Sinneswerte an jedem Tick,
- dieselben drei Feldmerkmale,
- dieselben neuronalen Eingangs- und Handlungsgewichte,
- dieselbe Aktivierungsfunktion,
- dieselbe Nachhallgleichung,
- dieselbe Neuronenzahl,
- dieselbe kontinuierliche Vorwelt-Zielwelt-Grenze.

Da Neuron `0` auch im Originalfeld kein Vorgaengersignal erhaelt, muss seine
vollstaendige Aktivierungs-Nachhall-Spur in beiden Instanzen exakt gleich
bleiben. Erst die nachfolgenden Neuronen duerfen auseinanderlaufen.

## Messung

Beide Instanzen werden getrennt durch die in 2122 und 2123 getragene
Stuetzmengenprojektion gelesen. Fuer jede Instanz wird der eigene
Synchronitaetsueberschuss berechnet:

`Gleichzeitigkeit - eigene nicht-nullige Kadenz-Erwartung`

Damit wird nicht vorausgesetzt, dass gekoppelte und entkoppelte Felder gleich
viele Aktivierungs- oder Nachhallereignisse erzeugen.

## Kontrollaudit

| Pruefung | Ergebnis |
| --- | ---: |
| gepaarte Feldpfade | 1.472 |
| identische Ausgangsgewichte | 1.472 / 1.472 |
| Neuron 0 in der Vorwelt exakt gleich | 1.472 / 1.472 |
| Neuron 0 in der Zielwelt exakt gleich | 1.472 / 1.472 |
| gekoppelte Spur nach Beobachtung unveraendert | 1.472 / 1.472 |
| Kontrollspur nach Beobachtung unveraendert | 1.472 / 1.472 |
| produktiver Feldkern unveraendert | 1.472 / 1.472 |
| Memory-, Viranz- oder Handlungseinfluss | 0 |

Der gekoppelte Ueberschuss stimmt in beiden Bestaenden exakt mit dem
beobachteten 2123-Ueberschuss ueberein. Die neue Paarmessung rekonstruiert den
Ausgangsbefund daher ohne Messdrift.

## Ergebnis

| Bestand | Universum | gekoppelt | ohne Nachbarschaft | Differenz | Quellen + / - | Pfade + / - | Vorzeichentest p |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2091 | A | 3.987,34 | 24,31 | +3.963,03 | 48 / 0 | 384 / 0 | 3,553 * 10^-15 |
| 2091 | B | 5.101,62 | -27,38 | +5.129,01 | 48 / 0 | 384 / 0 | 3,553 * 10^-15 |
| 2091 | gesamt | 9.088,96 | -3,08 | +9.092,04 | 48 / 0 | 768 / 0 | 3,553 * 10^-15 |
| 2092 | A | 4.234,14 | 720,39 | +3.513,75 | 44 / 0 | 352 / 0 | 5,684 * 10^-14 |
| 2092 | B | 3.865,59 | 521,99 | +3.343,60 | 44 / 0 | 281 / 71 | 5,684 * 10^-14 |
| 2092 | gesamt | 8.099,74 | 1.242,38 | +6.857,35 | 44 / 0 | 633 / 71 | 5,684 * 10^-14 |

Im Entwicklungsbestand faellt der Synchronitaetsueberschuss ohne interne
Weitergabe insgesamt auf praktisch null. Im unabhaengigen Holdout bleibt ein
positiver Rest von `1.242,38` gegenueber `8.099,74` im gekoppelten Feld. Die
Kontrolle traegt dort damit etwa `15,34 %` des gekoppelten Ueberschusses; rund
`84,66 %` der Differenz erscheinen erst mit der internen Weitergabe.

Alle 48 Entwicklungsquellen und alle 44 Holdoutquellen tragen dieselbe
gerichtete Paardifferenz. Auf Pfadebene ist die Richtung im Entwicklungsbestand
vollstaendig und im Holdout in 633 von 704 Pfaden positiv.

## Einordnung

2124 trennt die in 2123 noch gemeinsame kollektive Ursache:

- Gemeinsame Aussenanregung kann im Holdout einen kleineren eigenen
  Synchronitaetsueberschuss tragen.
- Der dominante und vollstaendig quellenstabile Zusatzanteil entsteht im
  aktuellen Modell durch die interne Nachbarschaftsweitergabe.
- Der 2122-Befund ist damit weder blosses Beobachtungsartefakt noch nur
  gemeinsame Aussenreaktion.

Diese Ursachenzuordnung ist fuer das Ziel der organischen Feldentwicklung
zugleich eine klare Grenze. Die aktuelle Nachbarschaft ist eine im Code
festgelegte gerichtete Kette, und ihre Staerke `0,12` ist ebenfalls vorgegeben.
2124 belegt deshalb die Wirkung der bestehenden Kopplungsarchitektur, nicht das
organische Entstehen einer Topologie und nicht Feldintelligenz.

Aus dem starken Effekt darf weder ein Memory-Eintrag noch eine semantische
Bindung oder Handlung abgeleitet werden. Vor einer organischen Nutzung muss
geprueft werden, ob die Koordination an genau dieser willkuerlichen
Indexreihenfolge haengt oder eine allgemeinere Eigenschaft interner Kopplung
ist.

## Reproduzierbarkeit

Ausgaben:

- `2124_MCM_NACHBARSCHAFTSKOPPLUNG_BEOBACHTERKOORDINATION.paths.csv`
- `2124_MCM_NACHBARSCHAFTSKOPPLUNG_BEOBACHTERKOORDINATION.sources.csv`
- `2124_MCM_NACHBARSCHAFTSKOPPLUNG_BEOBACHTERKOORDINATION.summary.csv`

SHA-256:

- `paths`: `B61A1967D8EB6D16F6DD7C4321EC502CEB082AEFF6BA3D09F0D06088822220C1`
- `sources`: `FC106B19ACD45F5903D3CF0B795A0E836E548070D98B5E2D29E564DEDCB60D0D`
- `summary`: `38ABE7B07C6E0CCAD017953A0B17BC1C61A981AEC39DB53F0969038131AF26D6`

Runner: `tools/run_mcm_neighbor_coupling_observer_coordination.py`

Test: `tests/test_mcm_neighbor_coupling_observer_coordination.py`
