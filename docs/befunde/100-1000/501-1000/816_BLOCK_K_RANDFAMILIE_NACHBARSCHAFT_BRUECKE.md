# 816 - Block-K Randfamilie Nachbarschaft/Bruecke: dio_1un4

## Fragestellung

Ist `dio_1un4` ein isolierter Randpunkt, eine Bruecke zu stabilen Bedeutungsraeumen oder der Anfang einer Unterfamilie?

## Zielzustand der Randfamilie

| Familie | Ticks | Klasse | Strain | Trust | Einbettung | Nachbar-Hits |
|---|---:|---|---:|---:|---:|---:|
| dio_1un4 | 119 | tragend_unruhig | 0.2250 | 0.6067 | 0.6499 | 238 |

## Haeufigste Nachbarfamilien

| Familie | Rolle | Hits | Vorher | Nachher | Gruppen | Klasse | Stabil | Unruhe | Strain | Trust | Nachhall | Einbettung |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| dio_155c | stabile_bruecke | 14 | 8 | 6 | 3 | stabil | 0.9809 | 0.0191 | 0.1554 | 0.8172 | 0.3592 | 0.7780 |
| dio_0l7p | stabiler_nachbar | 13 | 13 | 0 | 3 | stabil | 1.0000 | 0.0000 | 0.1356 | 0.8156 | 0.3549 | 0.7823 |
| dio_104t | stabiler_nachbar | 13 | 13 | 0 | 1 | stabil | 0.9854 | 0.0146 | 0.1485 | 0.8391 | 0.4279 | 0.7961 |
| dio_0m9z | stabile_bruecke | 12 | 9 | 3 | 3 | stabil | 0.7430 | 0.2570 | 0.1639 | 0.8098 | 0.3375 | 0.7702 |
| dio_04uf | unbestimmt | 10 | 1 | 9 | 3 | tragend_unruhig | 0.4535 | 0.5465 | 0.1655 | 0.7184 | 0.1431 | 0.7149 |
| dio_17ct | stabile_bruecke | 10 | 1 | 9 | 3 | stabil | 1.0000 | 0.0000 | 0.1467 | 0.7576 | 0.2095 | 0.7419 |
| dio_14wj | stabiler_nachbar | 8 | 8 | 0 | 3 | stabil | 1.0000 | 0.0000 | 0.1254 | 0.7937 | 0.2989 | 0.7708 |
| dio_0h9h | stabile_bruecke | 7 | 5 | 2 | 3 | stabil | 1.0000 | 0.0000 | 0.1382 | 0.7938 | 0.2878 | 0.7656 |
| dio_1mwv | stabile_bruecke | 5 | 1 | 4 | 2 | stabil | 1.0000 | 0.0000 | 0.1378 | 0.6662 | 0.0853 | 0.7001 |
| dio_0obq | stabile_bruecke | 5 | 3 | 2 | 1 | stabil | 0.9930 | 0.0070 | 0.1554 | 0.7414 | 0.1571 | 0.7264 |
| dio_0u2x | unbestimmt | 5 | 0 | 5 | 2 | stabil | 0.5507 | 0.4493 | 0.1753 | 0.5603 | 0.0136 | 0.6475 |
| dio_05yg | randnahe_unruhe | 5 | 0 | 5 | 3 | tragend_unruhig | 0.0084 | 0.9916 | 0.1760 | 0.7195 | 0.1381 | 0.7113 |

## Befund

`dio_1un4` ist kein isolierter Randpunkt. Die haeufigsten Nachbarn beruehren mehrere Gruppen und liegen ueberwiegend in stabilen oder teilstabilen Bedeutungsraeumen.

- stabile Bruecken im Top-N-Feld: 6
- randnahe Unruhe-Nachbarn im Top-N-Feld: 1
- viele Nachbarn treten vor und nach der Randfamilie auf; das spricht fuer Kontaktzone statt Einbahn-Uebergang,
- die Randfamilie bleibt selbst strain-nah, aber ihre Umgebung ist deutlich tragender als sie selbst.

Lesung: `dio_1un4` wirkt wie eine randnahe Kontakt-/Brueckenfamilie. Sie entsteht an Spannungsuebergaengen und koppelt an stabilere Bedeutungsraeume, ohne selbst zur stabilen Mitte zu werden.

## Grenze

Der Befund ist eine passive Nachbarschaftsdiagnose. Er beschreibt keine Handlung, keine Richtung und keine Strategie.

## Wie es weitergeht

Als naechstes sollte eine der stabilen Brueckenfamilien neben `dio_1un4` genauer gelesen werden. Dann sehen wir, ob die Bruecke nur Nachbarschaft ist oder eine echte semantische Uebergangsstruktur bildet.
