# ROLLING_RELATIVE Rezeptor-Diagnose

## Fragestellung

Nach der `WORLD_RELATIVE`-Methodengrenze wurde ein zusätzlicher Diagnosemodus ergänzt:

`rolling_relative`

Dieser Modus nutzt dieselbe rezeptorische Übersetzung wie `world_relative`, baut das Sinnesprofil aber pro Tick nur aus Vergangenheit und Gegenwart. Spätere Weltabschnitte dürfen frühere Wahrnehmung nicht mehr nachträglich skalieren.

Die Grundfrage:

Bleibt die in `world_relative` beobachtete 5-Rollen-Struktur mit selektiver Endrand-Rekopplung bestehen, wenn die Sinnesaufnahme kausal rollierend gelesen wird?

## Umsetzung

Ergänzt wurde:

- `mini_dio.run_mini --sense-mode rolling_relative`
- `tools/run_real_sleep_real_chain.py --sense-mode rolling_relative`

Der Modus ist passiv und diagnostisch. Er verändert keine Feldmechanik, keine Handlung, keine Rolle und keine Offline-Reorganisation. Er ändert nur, wie das Rezeptorprofil pro Tick gebildet wird.

## Gegenprobe

Geprüft wurden dieselben Schwellenfenster:

- `start250_size1650`
- `start250_size1700`

jeweils als Real-Sleep-Real-Kette mit `rolling_relative`.

| Fenster | Sinnesmodus | Rollen | Feldrollen | Rekopplung | Kombinationen |
| --- | --- | ---: | --- | --- | ---: |
| `1650` | `world_relative` | 5 | 3 carried / 2 strained | vollständig | 10 |
| `1700` | `world_relative` | 5 | 3 carried / 2 strained | selektiv | 10 |
| `1650` | `rolling_relative` | 1 | 1 carried | vollständig | 0 |
| `1700` | `rolling_relative` | 1 | 1 carried | vollständig | 0 |

## Befund

Die rollierende Rezeptor-Normierung beseitigt die selektive Endrand-Kippung, aber sie beseitigt auch die breite Rollenstruktur.

Damit ist die Diagnose zweischneidig:

- `rolling_relative` ist methodisch kausaler.
- `rolling_relative` ist im aktuellen Stand zu grob für die 5-Rollen-Topologie.
- `world_relative` liest das Gesamtmilieu besser, ist aber nicht streng lokal-kausal.

## Interpretation

Die bisherige 5-Rollen-Struktur entsteht offenbar nicht allein aus lokaler Tick-Reaktion. Sie benötigt eine weltbezogene Rezeptor-Skalierung, die das Feldmilieu als Ganzes lesbar macht.

Das ist fachlich wichtig:

MINI_DIO bildet Rollen nicht nur aus Einzelpunkten, sondern aus einem Milieu-Verhältnis. Wird dieses Verhältnis rein rollierend und lokal gebildet, verdichtet das Feld im aktuellen Stand zu einer einzigen tragenden Grundrolle.

## Methodische Konsequenz

Es braucht wahrscheinlich eine Zwischenform:

- nicht vollständig global wie `world_relative`,
- nicht vollständig lokal/rollierend wie `rolling_relative`,
- sondern ein organisches Rezeptorprofil mit Gedächtnis, Adaptation und begrenzter Vergangenheit.

Arbeitshypothese:

Eine kausal tragfähige Rezeptorschicht sollte mit gleitender Feldzeit arbeiten, nicht mit vollständiger Gesamtwelt und nicht mit reinem Tickfenster.

## Status

Status: passiver Methodenbefund.

Keine Handlungslogik, keine Strategie, kein Gate.
