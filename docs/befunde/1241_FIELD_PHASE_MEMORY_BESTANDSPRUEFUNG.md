# Befund 1241 - Field Phase Memory Bestandspruefung

Stand: 2026-07-01

## Grundfrage

Gibt es in MINI_DIO bereits eine eigene `field_phase_memory`, oder liegen Feldphasen nur verteilt in anderen Speichern?

## Ergebnis

Eine eigene, klar abgegrenzte `field_phase_memory` ist derzeit nicht vorhanden.

Es gibt bereits mehrere nahe Speicherformen:

- `episode_memory`
- `mcm_field_episode_memory`
- `temporal_families`
- `passive_inner_field_maps`
- `passive_inner_field_archetypes`
- `passive_mcm_role_movement_memory`
- `passive_mcm_role_shift_memory`
- `mcm_field_movement_memory`

Diese Speicher tragen wichtige Teilinformationen. Sie speichern Episoden, Feldkarten, Archetypen, Rollenbewegungen, Rollenwechsel und Feldbewegung. Sie speichern aber noch nicht sauber als eigene Struktur:

```text
vorherige Feldrolle -> aktuelle Feldrolle -> nachfolgende Feldrolle
```

mit Ursache, Dauer, Nachwirkung und Sinnesprofil.

## Wichtige Unterscheidung

Die vorhandenen `fieldphase_*_memory.json` Dateien sind SemanticMemory-Dateien mit einem Phasen-Namen im Dateinamen. Sie sind keine eigene `field_phase_memory`-Struktur.

Sie enthalten unter anderem:

- Symbole,
- Familien,
- Episoden,
- MCM-Feldepisoden,
- temporale Familien,
- passive Innenfeldkarten,
- passive Archetypen.

Damit kann Feldphasenverhalten analysiert werden. Es wird aber noch nicht als eigener reifender Phasenspeicher getragen.

## Was fehlt

Eine echte passive Feldphasen-Erinnerung sollte pro wiederkehrender Feldbewegung speichern:

- `previous_role`
- `current_role`
- `next_role`
- `movement_class`
- `sensory_cause_signature`
- `duration`
- `share`
- `field_before`
- `field_after`
- `aftereffect`
- `world_context`
- `repetition_count`
- `stability_quality`
- `drift_quality`

Beispiel:

```text
zentrum_stabil -> spannungsrand_kippnaehe -> offene_variante
```

Diese Sequenz wurde in den Befunden 1237 bis 1240 wiederholt sichtbar. Aktuell wird sie diagnostisch gelesen, aber noch nicht als eigener Gedaechtnistyp verdichtet.

## Fachliche Bedeutung

Eine `field_phase_memory` waere keine Handlungslogik.

Sie waere:

```text
passive Erinnerung an Feldbewegung ueber Zeit
```

Sie wuerde MINI_DIO mehr Tiefe geben, weil das System nicht nur einzelne Feldlagen, sondern wiederkehrende Phasenbewegungen als innere Erfahrung tragen koennte.

## Grenze

Aus dieser Pruefung folgt nicht:

- kein Gate,
- keine Handlung,
- kein Entry-System,
- keine Strategie,
- keine harte Regel.

Die Feldphasen-Erinnerung darf nur passiv speichern, wie Feldrollen ueber Weltkontakt ineinander uebergehen.

## Schlussfolgerung

Der aktuelle Stand ist fachlich gut vorbereitet, aber noch nicht vollstaendig.

MINI_DIO besitzt bereits:

```text
Feldrollen + Feldbewegung + Episoden + temporale Familien
```

Was als naechste Tiefenschicht fehlt:

```text
Feldphasen-Gedaechtnis als eigener passiver Speicher.
```

## Naechster Schritt

Als naechstes sollte eine kleine, passive `MCMFieldPhaseMemory` entworfen werden.

Sie sollte zuerst nur aus bestehenden Diagnose-CSV-Dateien lernen und nicht in den laufenden Organismus eingreifen.

Erst wenn diese Struktur reproduzierbar sinnvolle Phasenfamilien bildet, kann sie als passive Gedaechtnisschicht in `SemanticMemory` integriert werden.
