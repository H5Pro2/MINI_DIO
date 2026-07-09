# WORLD_RELATIVE Endrand-Methodengrenze

## Fragestellung

Die Schwellenzone `1650-1700` zeigte:

- Die Rohdaten bis `1650` sind zwischen `start250_size1650` und `start250_size1700` identisch.
- Trotzdem verändert sich bei Tick `1150` ein dünner Strain-/Übergangsmarker.
- Im `world_relative`-Modus rekoppelt `start250_size1700` selektiv.

Die methodische Frage lautet:

Entsteht die Selektivität aus anderer Rohwelt an der Rolle selbst, oder aus der weltrelativen Sinnesaufnahme des längeren Gesamtfensters?

## Prüfung

### Rohdaten-Identität

Die ersten `1650` Zeilen von `start250_size1650` und `start250_size1700` sind byte-identisch.

Damit ist die konkrete Rohwelt um Tick `1150` in beiden Fenstern gleich.

### Unterschied im Sinnesprofil

| Fenster | change_scale | direction_scale | energy_shift_scale | sample_count |
| --- | ---: | ---: | ---: | ---: |
| `start250_size1650` | 0.014480 | 0.023433 | 0.595275 | 1649 |
| `start250_size1700` | 0.014549 | 0.024531 | 0.619330 | 1699 |

Die verlängerte Welt verändert also das Rezeptorprofil. Das ist erwartbar, weil `world_relative` die Sinnesaufnahme relativ zur betrachteten Gesamtwelt skaliert.

### Marker bei Tick 1150

| Modus | Fenster | Marker | Rekopplung |
| --- | --- | --- | --- |
| `world_relative` | `1650` | `dio_mcm_episode_0qvqqtg` | reaktiviert |
| `world_relative` | `1700` | `dio_mcm_episode_0eghs1d` | unverändert |
| `fixed` | `1650` | 5/5 Rollen | vollständig reaktiviert |
| `fixed` | `1700` | 5/5 Rollen | vollständig reaktiviert |

Im festen Sinnesmodus bleibt die Offline-Rekopplung bei beiden Fensterlängen vollständig.

## Befund

Die beobachtete selektive Rekopplung im `1700`er-Fenster ist kein reiner Rohdatenbruch an Tick `1150`.

Sie entsteht aus dem Zusammenspiel:

- identischer lokaler Rohwelt,
- längerer Endrand-Welt,
- verändertem `world_relative`-Sinnesprofil,
- dünnem Strain-/Übergangsmarker,
- Offline-Rekopplung.

## Methodische Einordnung

Das ist kein direkter Fehler, aber eine klare Grenze der aktuellen Forschungsläufe:

`world_relative` liest eine Welt als Gesamtmilieu. Dadurch kann eine spätere Randphase die Wahrnehmungsskala früherer Weltpunkte verändern.

Fachlich passt das zu der Idee einer milieubezogenen Rezeptorschicht. Methodisch bedeutet es aber:

- Für passive Weltmilieu-Forschung ist `world_relative` sinnvoll.
- Für streng kausale Tick-für-Tick-Deutung reicht `world_relative` allein nicht.
- Wenn lokale Ursache geprüft werden soll, braucht es zusätzlich eine kausale oder rollierende Rezeptor-Normierung.

## Konsequenz für MINI_DIO

MINI_DIO sollte beide Lesarten trennen:

- **Milieu-Lesung:** Eine Welt wird als Ganzes aufgenommen. Spätere Randphasen können die Gesamtwahrnehmung modulieren.
- **Laufende Außenwelt-Lesung:** Wahrnehmung darf nur aus bisher erlebter Welt entstehen. Spätere Abschnitte dürfen frühere Wahrnehmung nicht nachträglich skalieren.

Für die aktuelle Forschung bleibt der Befund gültig als Milieu-Befund. Für spätere organische Laufzeitmechanik sollte eine rollierende, erfahrungsbasierte Rezeptorschicht ergänzt werden.

## Status

Status: passiver Methodenbefund.

Keine Handlungslogik, keine Strategie, kein Gate.
