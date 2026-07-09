# Asset-Milieu-Matrix 15m

## Zweck

Diese Matrix prueft, ob 15m zwischen 5m und 1h vermittelt oder eine eigene Milieuschicht erzeugt.

Aktuell liegen im Projekt fuer 15m nur BTC und SOL als Jahresdaten vor.
Deshalb ist dieser Report eine Zeitmass-Gegenprobe, keine vollstaendige Asset-Matrix wie bei 5m/1h.

## Datenbasis

Je Asset wurden vier 15m-Welten gelesen:

- 2024 Start,
- 2024 Folge,
- 2025 Start,
- 2025 Folge.

Alle acht Fenster enthalten 5000 Zeilen.

## Asset-Mittelwerte

| Asset | Welten | Randdruck | Offen | Rekopplung | Daempfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC | 4 | 0.4104 | 0.1530 | 0.3113 | 0.1254 | 0.1683 | 0.1068 | 0.1787 | 0.1036 |
| SOL | 4 | 0.4082 | 0.1550 | 0.3098 | 0.1271 | 0.1693 | 0.1083 | 0.1813 | 0.1057 |

## Topologiebefund

Die 15m-Topologiematrix liest alle acht Welten als:

```text
stark_zentriert_wenig_rand
```

Damit entsteht keine neue Topologieklasse.
15m wirkt in diesen Daten wie ein stabiler Zwischenraum:

```text
mehr Detail als 1h
weniger Milieubreite als 5m
keine lokale Randdominanz
```

## BTC gegen SOL

BTC:

```text
minimal mehr Randdruck
minimal mehr Rekopplung
minimal weniger Daempfung
```

SOL:

```text
minimal mehr offene Variante
minimal mehr Daempfung
minimal hoehere Sinnes-Gaps
```

Die Unterschiede sind klein.
Der wichtigere Befund ist deshalb nicht Assettrennung, sondern Zeitmass-Stabilitaet.

## Bedeutung

15m bestaetigt bisher:

```text
Topologie bleibt erhalten.
Zeitmass faerbt lokal.
Die Grundordnung wird nicht durch mittlere Aufloesung gebrochen.
```

Damit passt 15m zwischen 5m und 1h, ohne eine neue Milieuschicht zu erzwingen.

## Methodische Grenze

Dieser Report umfasst nur BTC und SOL.
PAXG, XRP und DOGE fehlen fuer 15m im aktuellen Datenbestand.

Die Werte sind Diagnoseprofile, keine MCM-Grenzen und keine Vorgaben fuer MINI_DIO.
