# 1522-1523 - MCM-Mosaik Variantenpruefung

## Zweck

Nach der breiten Mosaik-Welt aus Lauf 1521 war die konkrete Frage:

```text
Bleibt das Mosaik eine stabile Rollenlandschaft,
oder kippt es je nach Sequenzvariante wieder in eine Einzelrolle?
```

Diese Pruefung trennt zwei Unterfaelle:

1. Start-End-Bruecke: Randrollen mit klarer Brueckenstruktur.
2. Verschobener Referenz-Uebergang: Randrollen mit versetzter Uebergangsphase.

Damit wird nicht allgemein "mehr Welt" getestet, sondern gezielt die Form der Mosaik-Kopplung.

## Datenbasis

Geprueft wurden zwei synthetische Mosaikvarianten mit frischer Memory:

```text
1522: data/synthetic_1500_melody_randrollen_start_end_bridge_1200_5m.csv
1523: data/synthetic_1501_melody_randrollen_ref_shifted_transition_1200_5m.csv
```

Beide Welten wurden mit `world_relative` und je zwei Wiederholungen ausgefuehrt.

## Ergebnis

| Lauf | Kerzen | Unique Symbols | Stable Ratio | Carried Unrest | Avg Afterimage | Dominante Rollen |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1522 Lauf 1 | 1200 | 66 | 0.9129 | 0.0871 | 0.3438 | `dio_0l7p` 189, `dio_14wj` 86 |
| 1522 Lauf 2 | 1200 | 66 | 0.9129 | 0.0871 | 0.3438 | `dio_0l7p` 189, `dio_14wj` 86 |
| 1523 Lauf 1 | 1200 | 85 | 0.8626 | 0.1374 | 0.4081 | `dio_1wdi` 176, `dio_0l7p` 70, `dio_1fll` 61 |
| 1523 Lauf 2 | 1200 | 85 | 0.8626 | 0.1374 | 0.4081 | `dio_1wdi` 176, `dio_0l7p` 70, `dio_1fll` 61 |

Die Wiederholungen sind innerhalb der jeweiligen Welt identisch.

## Deutung

1522 bildet keine breite Mosaiklandschaft wie 1521, sondern faellt auf eine stabile Rekopplungs-/Wechselnaehe zurueck:

```text
dio_0l7p dominant
dio_14wj begleitend
dio_1fll nicht aktiv
dio_1wdi nicht aktiv
```

1523 erzeugt dagegen eine andere Rollenverteilung:

```text
dio_1wdi dominant
dio_0l7p begleitend
dio_1fll wieder sichtbar
dio_14wj nicht aktiv
```

Das ist wichtig, weil die Varianten nicht zufaellig dieselben Rollen streuen. Sie sortieren sich reproduzierbar unterschiedlich.

## MCM-Lesung

Der aktuelle Befund spricht dafuer, dass die Mosaik-Wirkung nicht einfach aus der Menge der Reize entsteht, sondern aus der Art der Kopplung:

```text
Start-End-Bruecke
  -> Rekopplungs-/Wechselnaehe
  -> dio_0l7p + dio_14wj

Verschobener Uebergang
  -> nachhallender Randbruch + Randqualitaet
  -> dio_1wdi + dio_0l7p + dio_1fll
```

Damit wird der MCM-Feldraum genauer:

- Zentrum/Bindung kann Bruecken stabilisieren.
- Rand ist kein einzelner Randwert, sondern ein Spannungsraum.
- Bruecken koennen beruhigend oder randnah nachhallend wirken.
- Nebelzonen entstehen dort, wo mehrere Rollen noch keine eindeutige Verdichtung bilden.
- Nachhall entscheidet mit, ob eine Rolle nur kurz auftaucht oder eine Weltphase traegt.

## Grenze

Das ist weiterhin ein passiver Befund.

Er zeigt nicht, dass eine endgueltige Topologie bewiesen ist. Er zeigt aber, dass MINI_DIO unterschiedliche Mosaikstrukturen reproduzierbar in unterschiedliche Rollenlandschaften uebersetzt.
