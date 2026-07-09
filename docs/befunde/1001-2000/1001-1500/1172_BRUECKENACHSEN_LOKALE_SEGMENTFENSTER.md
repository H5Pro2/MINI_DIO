# 1172 - Lokale Segmentfenster der Brueckenachsen

## Grundfrage

Bleibt der Befund aus 1169 auch in konkreten lokalen Segmentfenstern sichtbar?

Geprueft wurden einzelne Paarereignisse der stabilen Richtungsfaelle:

- `KAS 2024 5m`: `dio_00ly -> dio_104t`
- `Negative Stress 2024`: `dio_00ly -> dio_104t`
- `BTC 2024 Quiet 5m`: `dio_104t -> dio_00ly`

Die Pruefung bleibt passiv. Keine Handlung, kein Gate, keine Strategie.

## Methode

Fuer jedes Paar wurde ein lokales Fenster gelesen:

- 6 Ticks vor der Quelle,
- Quelle,
- Zwischenraum,
- Ziel,
- 6 Ticks nach dem Ziel.

Die Segmente wurden nach grober lokaler Welt-/Feldlage klassifiziert:

- `ruhige_rekopplung`
- `tonaler_wechsel_in_stabilitaet`
- `form_ton_wechsel`
- `tieferer_tonraum`
- `hellerer_tonraum`
- `hoehere_feldspannung`
- `offene_stabile_lage`

Diese Klassen sind Diagnoseetiketten, keine MINI_DIO-Handlungslogik.

## Ergebnisuebersicht

| Welt | Richtung | Paare | Quelle dominant | Ziel dominant | Ton-Delta | Shift-Delta | Rekopplung-Delta | Spannung-Delta |
|---|---|---:|---|---|---:|---:|---:|---:|
| KAS 2024 5m | `dio_00ly -> dio_104t` | 44 | `tonaler_wechsel_in_stabilitaet` | `tonaler_wechsel_in_stabilitaet` / `ruhige_rekopplung` | -0.1546 | -0.1002 | 0.0021 | -0.0027 |
| Negative Stress 2024 | `dio_00ly -> dio_104t` | 18 | `tonaler_wechsel_in_stabilitaet` | `form_ton_wechsel` / `tonaler_wechsel_in_stabilitaet` | -0.0975 | -0.1929 | -0.0001 | 0.0073 |
| BTC 2024 Quiet 5m | `dio_104t -> dio_00ly` | 80 | `tonaler_wechsel_in_stabilitaet` / `ruhige_rekopplung` | `tonaler_wechsel_in_stabilitaet` | 0.1548 | 0.1794 | 0.0014 | -0.0011 |

## Lesart

Die lokale Segmentebene bestaetigt die Aggregation aus 1169.

Bei `dio_00ly -> dio_104t` faellt der Ton:

- KAS: deutlicher Abfall des Energie-/Tonwerts.
- Negative Stress: ebenfalls Abfall, dazu mehr Form-/Tonwechsel am Ziel.

Bei `dio_104t -> dio_00ly` steigt der Ton:

- BTC Quiet: deutlicher Anstieg des Energie-/Tonwerts.

Die Rekopplung bleibt praktisch stabil. Die Feldspannung kippt nicht stark.

Damit ist die Brueckenrichtung nicht einfach ein Stresssignal. Sie sieht eher aus wie eine tonale Modulation innerhalb eines stabilen MCM-Feldbereichs.

## Bedeutung fuer die MCM-Mechanik

Diese Befunde stuetzen die aktuelle Sinnestrennung:

- Hoeren traegt Energiebewegung.
- Sehen liefert Form-/Wechselanteile.
- Rezeptoren begrenzen die Aufnahme.
- Das MCM-Feld bildet daraus stabile Brueckennaehe.

Wichtig ist: Hoeren wirkt hier nicht als direkte Entscheidung, sondern als Unterschied in der Feldlesung.

Das ist methodisch sauberer als eine harte Regel. MINI_DIO zeigt, dass dieselben Brueckenfamilien je nach lokaler Energiebewegung unterschiedlich gerichtet erscheinen koennen.

## Grenze

Die Segmentklassen sind Auswertungsklassen. Sie wurden nicht als innere MINI_DIO-Syntax gelernt.

Noch offen:

- ob MINI_DIO diese lokalen Segmentunterschiede spaeter selbst als eigene Bedeutungsinseln verdichtet,
- ob dieselbe Tonrichtung auch in anderen Weltklassen wiederkehrt,
- ob visuelle Formwechsel die Tonrichtung nur begleiten oder aktiv mittragen.

## Kurzfazit

Die lokale Pruefung bestaetigt: `dio_00ly` und `dio_104t` bilden eine stabile Brueckennaehe, deren Richtung wesentlich durch lokale Energie-/Tonbewegung moduliert wird.

Das Feld bleibt dabei tragend. Die Richtung entsteht also nicht aus Kollaps, sondern aus differenzierter Innenfeldbewegung.

