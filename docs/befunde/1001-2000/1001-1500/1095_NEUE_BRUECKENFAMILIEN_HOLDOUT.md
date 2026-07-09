# 1095 - Neue Brueckenfamilien im Holdout

Diese Diagnose ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Entstehen in den Holdout-Welten Brueckenfamilien, die nicht in der bisherigen Qualitaetskarte liegen?

## Gesamtbefund

- Familien mit beiden Lesarten: `66`
- Bekannte Familien aus 1092: `5`
- Neue starke Kandidaten: `2`
- Neue lokale Kandidaten: `10`

## Staerkste neuen Kandidaten

| Familie | Klasse | Tragend | Kippnah | Welten T/K | Rekopplung Gap | Strain Gap | Tension Gap | Gruppen |
|---|---|---:|---:|---|---:|---:|---:|---|
| `dio_00ly` | neuer_starker_brueckenkandidat | 474 | 12 | 11/6 | 0.0578 | 0.0343 | 0.0204 | feld_5m;zeit_1h |
| `dio_0pq6` | neuer_starker_brueckenkandidat | 10 | 24 | 4/6 | 0.0498 | 0.0509 | 0.0257 | feld_5m;zeit_1h |
| `dio_104t` | neuer_lokaler_brueckenkandidat | 342 | 6 | 11/2 | 0.0376 | 0.0342 | 0.0331 | feld_5m;zeit_1h |
| `dio_1xrt` | neuer_lokaler_brueckenkandidat | 50 | 6 | 7/3 | 0.0516 | 0.0392 | -0.0002 | feld_5m;zeit_1h |
| `dio_161t` | neuer_lokaler_brueckenkandidat | 8 | 20 | 4/8 | 0.0299 | 0.0317 | 0.0132 | feld_5m;sonstige;zeit_1h |
| `dio_1sa0` | neuer_lokaler_brueckenkandidat | 6 | 20 | 2/5 | 0.0367 | 0.0358 | 0.0350 | feld_5m;zeit_1h |
| `dio_0z9t` | neuer_lokaler_brueckenkandidat | 6 | 19 | 3/6 | 0.0525 | 0.0319 | 0.0300 | feld_5m;zeit_1h |
| `dio_07uk` | neuer_lokaler_brueckenkandidat | 8 | 12 | 3/6 | 0.0630 | 0.0417 | 0.0380 | feld_5m;zeit_1h |
| `dio_1o4z` | neuer_lokaler_brueckenkandidat | 5 | 15 | 3/7 | 0.0419 | 0.0390 | 0.0185 | feld_5m;zeit_1h |
| `dio_0obq` | neuer_lokaler_brueckenkandidat | 10 | 10 | 4/4 | 0.0205 | 0.0252 | 0.0216 | feld_5m;zeit_1h |
| `dio_0jqc` | neuer_lokaler_brueckenkandidat | 8 | 8 | 3/5 | 0.0609 | 0.0316 | 0.0219 | feld_5m;zeit_1h |
| `dio_0h6t` | neuer_lokaler_brueckenkandidat | 8 | 6 | 3/3 | 0.0568 | 0.0364 | 0.0275 | feld_5m;zeit_1h |
| `dio_03uk` | schwacher_kontakt | 413 | 2 | 8/1 | 0.1777 | 0.2227 | 0.4497 | feld_5m;zeit_1h |
| `dio_0n0i` | schwacher_kontakt | 324 | 2 | 11/2 | 0.1347 | 0.1822 | 0.4125 | feld_5m;sonstige;zeit_1h |
| `dio_0dd2` | schwacher_kontakt | 271 | 2 | 11/1 | 0.0553 | 0.0267 | 0.0168 | feld_5m;zeit_1h |
| `dio_00ja` | schwacher_kontakt | 3 | 229 | 1/9 | 0.0220 | 0.0262 | 0.0222 | feld_5m;zeit_1h |
| `dio_0pxr` | schwacher_kontakt | 2 | 202 | 1/10 | 0.0352 | 0.0351 | 0.0189 | feld_5m;zeit_1h |
| `dio_1lsu` | schwacher_kontakt | 4 | 151 | 2/9 | 0.0310 | 0.0329 | 0.0396 | feld_5m;zeit_1h |
| `dio_0fe7` | schwacher_kontakt | 67 | 4 | 9/2 | 0.0593 | 0.0364 | 0.0345 | feld_5m;zeit_1h |
| `dio_0tay` | schwacher_kontakt | 66 | 1 | 10/1 | 0.0589 | 0.0356 | 0.0240 | feld_5m;zeit_1h |

## Bekannte Kartenfamilien im Holdout

| Familie | Tragend | Kippnah | Rekopplung Gap | Strain Gap | Tension Gap |
|---|---:|---:|---:|---:|---:|
| `dio_1ewh` | 112 | 22 | 0.0337 | 0.0297 | 0.0228 |
| `dio_17ct` | 52 | 26 | 0.0282 | 0.0315 | 0.0372 |
| `dio_0g2r` | 38 | 38 | 0.0367 | 0.0337 | 0.0204 |
| `dio_155c` | 35 | 28 | 0.0279 | 0.0377 | 0.0276 |
| `dio_1gp2` | 27 | 26 | 0.0255 | 0.0324 | 0.0261 |

## Lesart

Ein neuer Kandidat ist nur dann interessant, wenn er in beiden Lesarten vorkommt und diese Lesarten durch Rekopplung und Strain unterscheidbar bleiben.
Damit wird keine neue Bedeutung gesetzt. Es wird nur markiert, wo das Bedeutungsnetz moeglicherweise neue Knoten ausbildet.

## Wie es weitergeht

Als naechstes sollten die staerksten neuen Kandidaten einzeln mit Tickfenstern gelesen werden. Erst dann kann entschieden werden, ob sie echte neue Brueckenanker oder nur lokale Kontaktfragmente sind.
