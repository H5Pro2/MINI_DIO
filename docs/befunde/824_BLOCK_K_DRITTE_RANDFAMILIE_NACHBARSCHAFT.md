# 816 - Block-K Randfamilie Nachbarschaft/Bruecke: dio_1v2w

## Fragestellung

Ist `dio_1v2w` ein isolierter Randpunkt, eine Bruecke zu stabilen Bedeutungsraeumen oder der Anfang einer Unterfamilie?

## Zielzustand der Randfamilie

| Familie | Ticks | Klasse | Strain | Trust | Einbettung | Nachbar-Hits |
|---|---:|---|---:|---:|---:|---:|
| dio_1v2w | 295 | tragend_unruhig | 0.1763 | 0.6893 | 0.6975 | 590 |

## Haeufigste Nachbarfamilien

| Familie | Rolle | Hits | Vorher | Nachher | Gruppen | Klasse | Stabil | Unruhe | Strain | Trust | Nachhall | Einbettung |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| dio_155c | stabile_bruecke | 27 | 5 | 22 | 3 | stabil | 0.9809 | 0.0191 | 0.1554 | 0.8172 | 0.3592 | 0.7780 |
| dio_0m9z | stabile_bruecke | 23 | 7 | 16 | 3 | stabil | 0.7430 | 0.2570 | 0.1639 | 0.8098 | 0.3375 | 0.7702 |
| dio_0jkk | randnahe_unruhe | 16 | 11 | 5 | 3 | tragend_unruhig | 0.0103 | 0.9897 | 0.1792 | 0.7210 | 0.1395 | 0.7107 |
| dio_05yg | randnahe_unruhe | 14 | 5 | 9 | 3 | tragend_unruhig | 0.0084 | 0.9916 | 0.1760 | 0.7195 | 0.1381 | 0.7113 |
| dio_00ja | randnahe_unruhe | 14 | 3 | 11 | 3 | tragend_unruhig | 0.2791 | 0.7209 | 0.1614 | 0.7578 | 0.2146 | 0.7373 |
| dio_0g2r | stabile_bruecke | 13 | 4 | 9 | 3 | stabil | 0.9061 | 0.0939 | 0.1470 | 0.7319 | 0.1578 | 0.7257 |
| dio_0h9h | stabile_bruecke | 13 | 5 | 8 | 3 | stabil | 1.0000 | 0.0000 | 0.1382 | 0.7938 | 0.2878 | 0.7656 |
| dio_0pxr | unbestimmt | 13 | 11 | 2 | 3 | stabil | 0.5147 | 0.4853 | 0.1629 | 0.6524 | 0.0677 | 0.6846 |
| dio_00ly | stabile_bruecke | 11 | 4 | 7 | 3 | stabil | 1.0000 | 0.0000 | 0.1358 | 0.7626 | 0.2078 | 0.7456 |
| dio_1gp2 | stabile_bruecke | 11 | 4 | 7 | 3 | stabil | 0.8636 | 0.1364 | 0.1493 | 0.7424 | 0.1960 | 0.7336 |
| dio_0pq6 | stabile_bruecke | 10 | 5 | 5 | 1 | stabil | 0.7719 | 0.2281 | 0.1484 | 0.6743 | 0.0895 | 0.6983 |
| dio_104t | stabile_bruecke | 9 | 1 | 8 | 2 | stabil | 0.9854 | 0.0146 | 0.1485 | 0.8391 | 0.4279 | 0.7961 |

## Befund

`dio_1v2w` ist kein isolierter Randpunkt. Die haeufigsten Nachbarn beruehren mehrere Gruppen und liegen ueberwiegend in stabilen oder teilstabilen Bedeutungsraeumen.

- stabile Bruecken im Top-N-Feld: 8
- randnahe Unruhe-Nachbarn im Top-N-Feld: 3
- viele Nachbarn treten vor und nach der Randfamilie auf; das spricht fuer Kontaktzone statt Einbahn-Uebergang,
- die Randfamilie bleibt selbst strain-nah, aber ihre Umgebung ist deutlich tragender als sie selbst.

Lesung: `dio_1un4` wirkt wie eine randnahe Kontakt-/Brueckenfamilie. Sie entsteht an Spannungsuebergaengen und koppelt an stabilere Bedeutungsraeume, ohne selbst zur stabilen Mitte zu werden.

## Grenze

Der Befund ist eine passive Nachbarschaftsdiagnose. Er beschreibt keine Handlung, keine Richtung und keine Strategie.

## Wie es weitergeht

Als naechstes sollte eine der stabilen Brueckenfamilien neben `dio_1v2w` genauer gelesen werden. Dann sehen wir, ob die Bruecke nur Nachbarschaft ist oder eine echte semantische Uebergangsstruktur bildet.
