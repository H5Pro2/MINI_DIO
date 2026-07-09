# 1478-1480 - Melodie-Gleichlage Spiegel-Gegenpruefung

## Zweck

Diese Pruefung ist die Gegenpruefung zur Schwellenkarte `1477`.

Die allgemeine Grundfrage war:

Bildet MINI_DIO das Gleichlagenband nur in der urspruenglichen Melodiefamilie, oder entsteht es auch bei veraenderter Phasenordnung?

## Aufbau

Die neue Weltstruktur nutzt eine gespiegelte Phasenordnung:

Original:

`block -> wave_up -> regular -> wave_down -> regular -> block`

Gegenstruktur:

`block -> wave_down -> regular -> wave_up -> regular -> block`

Konstant gehalten:

- `block_size 13`,
- `455` Richtungswechsel,
- gleiche Amplitudenreihe `0.00110`, `0.00112`, `0.00114`,
- `world_relative`,
- frischer Speicher.

## Ergebnis

| Welt | Amp | `dio_0ein` | `dio_1fll` | Differenz | Dominanz | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1478 | 0.00110 | 175 | 173 | 2 | `dio_0ein` | 51 | 1139 | 55 | 0.732594 | 0.571776 |
| 1479 | 0.00112 | 173 | 173 | 0 | gleich | 51 | 1139 | 55 | 0.732426 | 0.570747 |
| 1480 | 0.00114 | 173 | 173 | 0 | gleich | 52 | 1137 | 57 | 0.732233 | 0.570884 |

## Befund

Die gespiegelte Phasenordnung bildet erneut das gleiche lokale Muster:

- bei `0.00110`: `dio_0ein` bleibt knapp vorne,
- bei `0.00112`: Gleichlage,
- bei `0.00114`: Gleichlage.

Damit bleibt das Gleichlagenplateau trotz veraenderter Phasenordnung sichtbar.

## Vergleich Zur Originalstruktur

Die Originalstruktur zeigte:

- `0.00110`: `dio_0ein` knapp vorne,
- `0.00112`: Gleichlage,
- `0.00114`: Gleichlage.

Die Spiegelstruktur zeigt denselben Ablauf.

Die Feldwerte bleiben ebenfalls sehr nahe:

- Rekopplung bleibt um `0.732`,
- Nachhall bleibt um `0.571`,
- stabile Feldwirkung bleibt hoch,
- tragende Unruhe steigt nur leicht.

## Lesung

Der Befund spricht dagegen, dass die beobachtete Gleichlage nur ein Artefakt der konkreten Phasenreihenfolge ist.

Vorsichtige Lesung:

MINI_DIO reagiert hier staerker auf den gekoppelten Feldraum aus Lautstaerke, Blockdauer, Nachhall und Rekopplung als auf die exakte Reihenfolge von `wave_up` und `wave_down`.

Das stuetzt die Idee einer lokalen Bedeutungs-Topologie.

## Schlussfolgerung

Die Schwellenkarte aus `1477` wird durch eine Spiegel-Gegenpruefung gestuetzt.

Die Gleichlage bei `0.00112` bis `0.00114` bleibt auch bei veraenderter Phasenordnung erhalten.

Das ist kein allgemeiner Beweis, aber ein staerkerer Befund als eine reine Einzelwelt-Beobachtung.

## Grenze

Die Gegenpruefung bleibt innerhalb derselben synthetischen Grundfamilie.

Sie veraendert die Phasenordnung, aber nicht alle moeglichen Weltmerkmale.

## Wie es weitergeht

Als naechstes sollte eine staerkere Gegenstruktur laufen: nicht nur Spiegelung, sondern gebrochene Melodie mit erhaltener Lautstaerkenreihe. Ziel ist zu pruefen, ob das Gleichlagenplateau bei strukturellem Bruch bestehen bleibt oder zerfaellt.
