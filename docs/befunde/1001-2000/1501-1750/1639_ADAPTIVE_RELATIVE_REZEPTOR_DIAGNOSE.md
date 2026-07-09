# ADAPTIVE_RELATIVE Rezeptor-Diagnose

## Fragestellung

Nach der `rolling_relative`-Gegenprobe wurde eine Zwischenform ergänzt:

`adaptive_relative`

Der Modus soll nicht die vollständige Gesamtwelt wie `world_relative` lesen und nicht bei jedem Tick rein lokal neu normieren wie `rolling_relative`. Stattdessen wird ein Profil aus begrenzter Vergangenheit gebildet und langsam weitergetragen.

Die Grundfrage:

Kann eine kausalere Rezeptorschicht die Rollenbreite erhalten, ohne auf vollständige Gesamtwelt-Skalierung zurückzugreifen?

## Umsetzung

Ergänzt wurde:

- `mini_dio.run_mini --sense-mode adaptive_relative`
- `tools/run_real_sleep_real_chain.py --sense-mode adaptive_relative`
- `Config.DIO_MINI_ADAPTIVE_PROFILE_HORIZON = 512`
- `Config.DIO_MINI_ADAPTIVE_PROFILE_ALPHA = 0.04`

Der Modus ist passiv und diagnostisch:

- keine Handlung,
- kein Gate,
- keine Richtungsvorgabe,
- keine Veränderung der MCM-Feldmechanik.

## Gegenprobe

Geprüft wurden dieselben Schwellenfenster:

- `start250_size1650`
- `start250_size1700`

jeweils als Real-Sleep-Real-Kette.

| Fenster | Sinnesmodus | Rollen | Feldrollen | Rekopplung | Kombinationen |
| --- | --- | ---: | --- | --- | ---: |
| `1650` | `world_relative` | 5 | 3 carried / 2 strained | vollständig | 10 |
| `1700` | `world_relative` | 5 | 3 carried / 2 strained | selektiv | 10 |
| `1650` | `rolling_relative` | 1 | 1 carried | vollständig | 0 |
| `1700` | `rolling_relative` | 1 | 1 carried | vollständig | 0 |
| `1650` | `adaptive_relative` | 1 | 1 carried | vollständig | 0 |
| `1700` | `adaptive_relative` | 1 | 1 carried | vollständig | 0 |

## Befund

Der erste adaptive Ansatz erhält lokale Kausalität, aber nicht die Rollenbreite.

Damit bestätigt sich:

- Die 5-Rollen-Struktur ist an eine Milieu-Lesung gekoppelt.
- Reine oder stark kausalisierte Rezeptorprofile glätten die gespannte Rollenstruktur.
- Die dünnen Strain-/Übergangsmarker verschwinden zuerst.

## Interpretation

Die adaptive Rezeptorschicht ist im aktuellen Stand zu dämpfend.

Sie erzeugt ein stabiles, vollständig rekoppelbares Feld, aber dieses Feld ist semantisch zu breit zusammengezogen: Es bildet eine tragende Grundrolle statt differenzierter Rollenlandschaft.

Das ist methodisch wichtig:

Ein organisches Rezeptorsystem darf Weltspannung nicht einfach beruhigen. Es muss tragfähige Spannung erhalten können. Sonst verliert MINI_DIO genau jene Rand-, Kipp- und Übergangsrollen, die für MCM-Topologie relevant sind.

## Konsequenz

Der nächste Rezeptoransatz sollte nicht nur glätten, sondern Spannung selektiv erhalten:

- stabile Grundlage tragen,
- dünne Rand-/Kippmarker nicht wegdämpfen,
- lokale Kausalität wahren,
- Milieu-Tiefe als Gedächtnis/Nachhall halten.

Die passendere Forschungsrichtung ist daher nicht `adaptive_relative` als einfache Dämpfung, sondern ein **phasengebundener Rezeptor-Nachhall**:

- aktuelle Wahrnehmung bleibt kausal,
- vergangene Feldphasen bleiben als Nachhall verfügbar,
- Strain-/Kippmarker werden nicht durch Normalisierung gelöscht,
- Milieu entsteht aus erlebter Feldgeschichte, nicht aus vollständiger Vorab-Gesamtwelt.

## Status

Status: passiver Methodenbefund.

Keine Handlungslogik, keine Strategie, kein Gate.
