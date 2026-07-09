# 1431 - Melodie Ruheverlust Isolation

## Zweck

Diese Pruefung isoliert einen Faktor aus dem `1428`-Kipppunkt:

Verlust von Ruhe.

Grundfrage:

Reicht das Entfernen der Ruhephasen allein, damit `dio_0ein` die Dominanz von `dio_1fll` uebernimmt?

## Aufbau

`1430`:

`rest -> block -> wave_down -> irregular -> regular -> rest`

`1431`:

`block -> wave_up -> block -> wave_down -> irregular -> regular`

`1428`:

`block -> irregular -> regular -> wave_down -> irregular -> block`

`1431` entfernt Ruhephasen, aber hat nur eine Irregularitaet.

## Rohwelt

| Welt | Richtungswechsel | avg_abs_return | avg_range | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1431 | 383 | 0.000910 | 0.004366 | 0.026240 | 0.072463 | 0.709154 |

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | zweites Symbol | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1430_THRESHOLD_MID | 48 | 1139 | 55 | `dio_1fllaqz` | `dio_0eindxe` | 0.581064 | 0.736879 | 0.126924 | 0.884080 | 0.606884 | 761 | 433 |
| 1431_NO_REST_SINGLE_IRREGULAR | 53 | 1118 | 76 | `dio_1fllaqz` | `dio_0eindxe` | 0.573338 | 0.732059 | 0.126514 | 0.878326 | 0.517223 | 1013 | 181 |
| 1428_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | `dio_0v65ujo` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Befund

Ruheverlust allein reicht noch nicht fuer den Dominanzwechsel.

`1431` bleibt formal bei `dio_1fllaqz`, aber der Abstand zu `dio_0eindxe` wird sehr klein:

- `1430`: `dio_1fllaqz:421`, `dio_0eindxe:145`
- `1431`: `dio_1fllaqz:176`, `dio_0eindxe:143`
- `1428`: `dio_0eindxe:197`, `dio_1fllaqz:84`

Das ist fachlich wichtig:

Der Verlust von Ruhe bringt das Feld sehr nahe an den Kipppunkt, aber die Uebernahme entsteht erst in Kombination mit weiterer Strukturspannung.

## Lesung

`1431` zeigt fast dieselbe Nachhallabsenkung wie `1428`:

- `1430`: Nachhall 0.606884
- `1431`: Nachhall 0.517223
- `1428`: Nachhall 0.518075

Trotzdem kippt `1431` nicht vollstaendig.

Das spricht dafuer:

Nachhallverlust ist notwendig oder stark beteiligt, aber nicht allein ausreichend.

Die doppelte Irregularitaet und/oder die konkrete Blockrahmung aus `1428` sind wahrscheinlich zusaetzliche Kipptreiber.

## Schlussfolgerung

Mini-DIO liest Ruheverlust als starke Feldveraenderung.

Die Bedeutungsdominanz wird komprimiert und beinahe verschoben. Der eigentliche Kippmoment braucht aber mehr als nur fehlende Ruhe.

Das bestaetigt die hierarchische Pruefung:

1. Grundfrage: Was loest den Melodie-Kipppunkt aus?
2. Unterpruefung: Reicht Ruheverlust allein?
3. Ergebnis: Nein, aber Ruheverlust bringt das Feld nahe an die Schwelle.

## Grenze

Diese Aussage gilt fuer die synthetische Melodiereihe.

Die exakte Schwelle ist noch nicht vollstaendig bestimmt.
