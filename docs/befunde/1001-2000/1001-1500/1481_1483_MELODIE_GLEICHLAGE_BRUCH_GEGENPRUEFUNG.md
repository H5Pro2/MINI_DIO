# 1481-1483 - Melodie-Gleichlage Bruch-Gegenpruefung

## Zweck

Diese Pruefung ist eine staerkere Gegenstruktur zur Schwellenkarte `1477`.

Die konkrete Frage war:

Bleibt das Gleichlagenplateau zwischen `dio_0ein` und `dio_1fll` auch bei strukturellem Bruch bestehen, oder bildet MINI_DIO einen anderen Hauptanker?

## Aufbau

Gebaut wurde eine gebrochene Melodiewelt:

`block -> irregular -> regular -> wave_down -> irregular -> block`

Konstant gehalten:

- `block_size 13`,
- Amplitudenreihe `0.00110`, `0.00112`, `0.00114`,
- `world_relative`,
- frischer Speicher.

Bewusst veraendert:

- mittlere Phasen werden durch `irregular` gestoert,
- Richtungswechsel sinken auf `417-419`,
- Welt bleibt driftkontrolliert.

## Ergebnis

| Welt | Amp | Hauptanker | `dio_0ein` | `dio_1fll` | Differenz | Paarlage | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1481 | 0.00110 | `dio_0v65` 148 | 134 | 134 | 0 | gleich | 53 | 1118 | 76 | 0.730917 | 0.526082 |
| 1482 | 0.00112 | `dio_0v65` 148 | 134 | 133 | 1 | `dio_0ein`-nah | 55 | 1117 | 77 | 0.730629 | 0.524131 |
| 1483 | 0.00114 | `dio_0v65` 149 | 135 | 134 | 1 | `dio_0ein`-nah | 55 | 1117 | 77 | 0.730480 | 0.524123 |

## Befund

Der strukturelle Bruch zerlegt die bisherige Hauptdominanz.

`dio_0ein` und `dio_1fll` bleiben als Paar eng beieinander, aber sie bilden nicht mehr den Hauptanker.

Stattdessen uebernimmt `dio_0v65`.

Das ist der entscheidende Unterschied zur Spiegel-Gegenpruefung:

- Spiegelung: Gleichlagenplateau bleibt als Hauptstruktur sichtbar.
- Bruch: altes Paar bleibt nahe, aber ein anderer Anker wird zentral.

## Lesung

MINI_DIO reagiert nicht nur auf Lautstaerke.

Bei gebrochener Struktur verschiebt sich der Bedeutungsraum:

- Nachhall sinkt deutlich,
- tragende Unruhe steigt,
- Fokus-Ton steigt,
- `dio_0v65` wird dominanter.

Das spricht dafuer, dass das Feld strukturelle Unordnung nicht einfach als gleiche Lautstaerkevariante liest.

## Schlussfolgerung

Das Gleichlagenplateau aus `1477` ist robust gegen Spiegelung, aber nicht unveraendert robust gegen strukturellen Bruch.

Bei Bruch bleibt eine Restnaehe zwischen `dio_0ein` und `dio_1fll`, aber die zentrale Feldrolle verschiebt sich zu `dio_0v65`.

Fachlich:

Das Feld bewahrt alte Nachbarschaft, bildet aber bei Bruch einen neuen Hauptanker.

## Grenze

Diese Pruefung nutzt eine konstruierte Bruchwelt.

Sie zeigt eine klare Verschiebung, aber noch nicht, ob `dio_0v65` allgemein fuer gebrochene Melodie steht oder nur fuer diese konkrete Bruchform.

## Wie es weitergeht

Als naechstes sollte `dio_0v65` als Bruchanker isoliert werden: gleiche Bruchstruktur bei mehreren Lautstaerken oder anderer Irregularitaetsform. Ziel ist zu pruefen, ob `dio_0v65` stabil die Rolle `gebrochene Feldnaehe` traegt.
