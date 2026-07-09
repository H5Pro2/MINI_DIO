# SYNTH_RAND_KIPP Schwellenzone 1650-1700

## Fragestellung

Die vorherige Schwellenprüfung zeigte:

- `start250_size1650` rekoppelt 5/5 Rollen und 10/10 Kombinationen vollständig.
- `start250_size1700` bildet weiterhin 5 Rollen und 10 Kombinationen, rekoppelt aber nur 4/5 Rollen und 6/10 Kombinationen vollständig.

Die konkrete Unterprüfung lautet:

Was verändert sich zwischen `1650` und `1700`, wenn die Rollenbreite gleich bleibt, aber die Offline-Rekopplung selektiv wird?

## Rohwelt-Vergleich

Die zusätzliche Zone von `start250_size1650` zu `start250_size1700` entspricht im Ursprungsfenster dem Bereich `1900-1950`.

| Bereich | Drift | avg Abs Return | p95 Abs Return | max Abs Return | avg Range | p95 Range | Richtungswechsel | Persistenz |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1850-1900 | 0.268272 | 0.007473 | 0.016256 | 0.017744 | 0.063314 | 0.104013 | 0.4375 | 0.5625 |
| 1900-1950 | 0.240624 | 0.007299 | 0.015739 | 0.018077 | 0.062924 | 0.100404 | 0.4375 | 0.5625 |

Die Zone `1900-1950` ist also nicht deutlich lauter oder chaotischer als die vorherige 50er-Zone. Der stärkere Effekt entsteht im Gesamtfenster:

| Fenster | Drift | avg Abs Return | avg Range | Richtungswechsel | Persistenz |
| --- | ---: | ---: | ---: | ---: | ---: |
| 250-1750 | 0.772580 | 0.002363 | 0.020676 | 0.1101 | 0.8899 |
| 250-1900 | 2.597250 | 0.002826 | 0.024506 | 0.1402 | 0.8598 |
| 250-1950 | 3.525177 | 0.002961 | 0.025636 | 0.1484 | 0.8516 |

## Rollenvergleich

Beide Schwellenfenster bilden dieselbe Grundstruktur:

- 3 tragende Rollen.
- 2 gespannte Rollen.
- 5 Rollen gesamt.

Die langen tragenden Rollen bleiben stabil. Der Unterschied liegt in einem sehr kurzen Strain-/Kontaktmarker:

| Fenster | dünner Strain-Marker | Dauer | Tick | Rekopplung im Folgelauf |
| --- | --- | ---: | ---: | --- |
| `start250_size1650` | `dio_mcm_episode_0qvqqtg` | 1 | 1150 | reaktiviert |
| `start250_size1700` | `dio_mcm_episode_0eghs1d` | 1 | 1150 | unverändert |

Die MCM-Qualitäten dieser beiden Marker sind fast gleich:

| Marker | Carry | Strain | Rekopplung | Hearing Gap | Visual Gap |
| --- | ---: | ---: | ---: | ---: | ---: |
| `dio_mcm_episode_0qvqqtg` | 0.325934 | 0.331915 | 0.549905 | 0.542789 | 0.285579 |
| `dio_mcm_episode_0eghs1d` | 0.326047 | 0.331264 | 0.550271 | 0.542609 | 0.281779 |

## Befund

Die Selektivität entsteht nicht durch eine starke neue Rohweltspitze und nicht durch eine neue breite Rolle.

Sie entsteht an einer sehr dünnen Übergangsrolle, die bei fast gleicher MCM-Qualität anders benannt und im Folgelauf nicht erneut angeschlossen wird.

Damit wirkt der Bereich `1900-1950` nicht wie ein Rollenerzeuger, sondern wie ein Nachhall-/Milieu-Modulator:

- Die vorhandenen langen Rollen bleiben tragfähig.
- Die breite Rollenstruktur bleibt erhalten.
- Eine einzelne gespannte Übergangsmarke verliert ihre Wiederanschlussfähigkeit.
- Dadurch kippen auch Kombinationen von vollständig auf teilweise rekoppelt.

## Interpretation

Der Befund spricht für eine feldmilieuspezifische Selektivität:

Nicht die lokale Stärke der letzten 50 Zeilen entscheidet allein, sondern die Gesamtgeschichte des Feldes bis zum Endrand. Das Feld trägt die späte Randphase als Kontext mit. Dadurch kann ein sehr kleiner Kontaktmarker im Offline-/Folgelauf seine Anschlussfähigkeit verlieren.

Fachlich gelesen:

- Rollenbildung bleibt Binnenraum-Funktion.
- Endrand bleibt Modulator.
- Selektivität zeigt sich zuerst an dünnen Strain-/Übergangsmarkern.
- Die langen tragenden Rollen sind robuster als kurze gespannte Rollen.

## Status

Status: passiver Befund, keine Handlungslogik.

Diese Prüfung verstärkt die Annahme, dass MINI_DIO nicht nur Einzelwerte sammelt, sondern Feldgeschichte trägt. Die selektive Offline-Rekopplung entsteht hier aus der Relation zwischen breitem Rollenfeld, Endrand und dünner Übergangsmarke.
