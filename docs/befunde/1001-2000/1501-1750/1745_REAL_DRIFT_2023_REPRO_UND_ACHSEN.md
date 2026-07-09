# 1745 - Real Drift 2023 Repro Und Achsen

## Zweck

Nach der synthetischen Repro-Prüfung wurde dieselbe Grundfrage auf reale Weltfenster mit stärkerer Milieudrift gelegt.

Geprüft wurden vier SOL-2023-Fenster:

- `REAL_DRIFT_2023_A`,
- `REAL_DRIFT_2023_A_FOLLOW`,
- `REAL_DRIFT_2023_B`,
- `REAL_DRIFT_2023_B_FOLLOW`.

Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bleibt die Topologie auch in realen Driftfenstern stabil?
2. Unterprüfung: Verschiebt sich die lokale Weltfärbung in Zentrum, Offenheit, Randdruck, Rekopplung und Achsenklasse?
3. Folgeschritt: Prüfen, ob dieselbe Driftlogik bei anderen Assets oder anderen Jahren wiederkehrt.

## Topologie

Alle vier realen Driftfenster bleiben `stark_zentriert_wenig_rand`.

| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2023_A | 9994 | 0.9881 | 0.0119 | 0.0000 | 0.2479 | 0.7077 | 0.5524 | 0.1703 | 0.8415 |
| REAL_DRIFT_2023_A_FOLLOW | 9994 | 0.9887 | 0.0113 | 0.0000 | 0.2475 | 0.7067 | 0.5522 | 0.1716 | 0.8391 |
| REAL_DRIFT_2023_B | 9994 | 0.9894 | 0.0106 | 0.0000 | 0.2470 | 0.7070 | 0.5520 | 0.1712 | 0.8397 |
| REAL_DRIFT_2023_B_FOLLOW | 9994 | 0.9895 | 0.0105 | 0.0000 | 0.2474 | 0.7080 | 0.5528 | 0.1701 | 0.8426 |

Die globale Rollenordnung bricht also nicht. Die Drift zeigt sich feiner: im Anteil offener Varianten, in den Symbolfamilien der offenen Variante und in den lokalen Randdruck-Spitzen.

## Randdruck

Die Randdruck-Lupe zeigt ein enges, aber nicht identisches Profil:

| Welt | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2023_A | 0.4258 | 0.1374 | 0.3300 | 0.1069 | 0.1703 | 0.1067 | 0.1778 | 0.1031 |
| REAL_DRIFT_2023_A_FOLLOW | 0.4217 | 0.1383 | 0.3304 | 0.1097 | 0.1716 | 0.1068 | 0.1847 | 0.1032 |
| REAL_DRIFT_2023_B | 0.4221 | 0.1406 | 0.3298 | 0.1076 | 0.1712 | 0.1067 | 0.1832 | 0.1030 |
| REAL_DRIFT_2023_B_FOLLOW | 0.4217 | 0.1392 | 0.3325 | 0.1067 | 0.1701 | 0.1071 | 0.1742 | 0.1041 |

Lesart: Der Randdruck bleibt lokal vorhanden, aber er wird vom Feld rekoppelt. Die reale Drift erzeugt keine harte Randdominanz, sondern eine feinere Umlagerung im zentrumsnahen Rollenraum.

## Achsen

Der Achsenreport liest beide Driftpaare als `mittlere_uebergangsphase`.

| Label | Achsenklasse | Breite | Rollen | Kombinationen | Cross | Same | Rekopplung | Adaptiv | Delta | Erfahrung | Nachhall |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2023_A | mittlere_uebergangsphase | mittel | 4 | 6 | 3 | 3 | 0.7077 | 0.7432 | 0.0356 | 0.7428 | 0.6575 |
| REAL_DRIFT_2023_B | mittlere_uebergangsphase | mittel | 3 | 3 | 2 | 1 | 0.7070 | 0.7413 | 0.0343 | 0.7461 | 0.6601 |

Beide Paare reaktivieren ihre Rollen und Kombinationen vollständig. A ist breiter und stärker vernetzt, B kompakter. Damit entsteht keine starre Kopie, sondern eine stabile Übergangsform mit unterschiedlicher Rollenbreite.

## Lesart

Die realen Driftfenster bestätigen drei Punkte:

1. Die globale Topologie bleibt zentrumsnah rekoppelnd.
2. Die lokale Weltfärbung verändert sich messbar.
3. Reale Drift erscheint eher als Rollenbreiten- und Randdruck-Umlagerung, nicht als Topologiebruch.

Das ist wichtig für die MCM-Lesung: Stabilität bedeutet hier nicht starre Wiederholung. Das Feld hält seine Grundordnung, lässt aber lokale Färbung, offene Varianten und Randdruckspitzen variieren.

## Zugehörige Reports

- [real_drift_2023_topology.md](../../../../reports/real_drift_2023_topology.md)
- [real_drift_2023_randdruck.md](../../../../reports/real_drift_2023_randdruck.md)
- [real_drift_2023_axis_map.md](../../../../reports/real_drift_2023_axis_map.md)

## Grenze

Die Prüfung gilt für diese vier realen SOL-2023-Fenster. Sie zeigt reproduzierbare Rollenkerne und feinere Milieudrift, aber noch keine universelle Aussage über alle Assets oder Jahre.
