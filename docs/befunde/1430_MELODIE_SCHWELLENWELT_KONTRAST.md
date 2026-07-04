# 1430 - Melodie Schwellenwelt Kontrast

## Zweck

Diese Pruefung baut eine Zwischenwelt zwischen `1427` und `1428`.

Grundfrage:

Wo liegt die Schwelle, an der `dio_1fll` seine Dominanz verliert und `dio_0ein` uebernimmt?

## Aufbau

`1427`:

`rest -> block -> wave_down -> irregular -> wave_up -> rest`

`1430`:

`rest -> block -> wave_down -> irregular -> regular -> rest`

`1428`:

`block -> irregular -> regular -> wave_down -> irregular -> block`

`1430` bleibt eine Zwischenwelt:

- Ruhe am Anfang und Ende bleibt erhalten.
- `wave_up` wird durch `regular` ersetzt.
- keine doppelte Irregularitaet.
- keine Blockrahmung ohne Ruhe.

## Rohwelt

| Welt | Richtungswechsel | avg_abs_return | avg_range | Drift | Max DD | Quiet Score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1430 | 361 | 0.000693 | 0.004149 | -0.050794 | 0.070719 | 0.729838 |

Damit liegt `1430` deutlich ueber `1427` im Bruchgrad, aber noch unter `1428`.

## Gesamtvergleich

| Welt | Symbole | stabil | tragend_unruhig | dominant | Carry | Rekopplung | Strain | Kopplung | Nachhall | Fokus | Beobachtung |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1427_REORDERED | 55 | 1147 | 47 | `dio_1fllaqz` | 0.583858 | 0.741103 | 0.121816 | 0.897276 | 0.607947 | 693 | 501 |
| 1430_THRESHOLD_MID | 48 | 1139 | 55 | `dio_1fllaqz` | 0.581064 | 0.736879 | 0.126924 | 0.884080 | 0.606884 | 761 | 433 |
| 1428_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |
| 1429_REPRO_STRONGLY_BROKEN | 47 | 1102 | 92 | `dio_0eindxe` | 0.572284 | 0.729330 | 0.130062 | 0.867700 | 0.518075 | 1079 | 115 |

## Befund

`1430` kippt noch nicht.

Die Hauptfamilie bleibt `dio_1fllaqz`, aber der Abstand zu `dio_0eindxe` wird kleiner:

- `1427`: `dio_1fllaqz:499`, `dio_0eindxe:66`
- `1430`: `dio_1fllaqz:421`, `dio_0eindxe:145`
- `1428`: `dio_0eindxe:197`, `dio_1fllaqz:84`

Das ist eine klare Annäherung an den Kipppunkt, aber noch keine Uebernahme.

## Lesung

Die Schwelle liegt nicht allein bei mehr Richtungswechseln.

`1430` hat bereits deutlich mehr Richtungswechsel als `1427`, bleibt aber feldseitig noch in der `dio_1fll`-Dominanz.

Der eigentliche Kipppunkt scheint an einer Kombination zu haengen:

- keine Ruhephase am Anfang und Ende,
- doppelte Irregularitaet,
- Blockrahmung,
- sinkender Nachhall,
- steigender Fokus bei fallender Beobachtung.

## Schlussfolgerung

Mini-DIO liest Melodiebruch abgestuft.

Moderater Bruch erzeugt Nachbarschaft und Naeherung. Erst staerkerer Bruch verschiebt die dominante Bedeutungsfamilie.

Das ist wichtig, weil die Feldordnung nicht sofort bei jeder Veraenderung springt. Sie bleibt eine Zeit lang in der alten Ordnung tragfaehig und kippt erst bei bestimmter Strukturspannung.

## Grenze

Die Schwelle ist noch nicht exakt lokalisiert.

`1430` zeigt nur, dass der Kippbereich naeher an `1428` liegt als an `1427`. Weitere Zwischenwelten muessen pruefen, welcher Anteil den Wechsel ausloest: fehlende Ruhe, doppelte Irregularitaet oder Blockrahmung.

## Wie es weitergeht

Als naechstes sollte genau ein Faktor aus `1428` isoliert werden. Erste sinnvolle Unterpruefung: Ruhe entfernen, aber keine doppelte Irregularitaet. So sehen wir, ob der Verlust der Ruhe allein die Dominanzverschiebung ausloest.
