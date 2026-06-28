# MCM-Rollenbewegungs-Memory

## Zweck

Diese Datei uebersetzt die Mehrlandschafts-Rollenfolge aus 912 in eine passive semantische Memory-Struktur.
Gespeichert wird nicht eine harte Klasse, sondern Rollenbewegung, Stabilitaet und Driftqualitaet.

## Grenze

Diese Memory-Schicht ist passiv:

- keine Handlung,
- kein Gate,
- kein Entry-Signal,
- keine Richtungsvorgabe,
- keine motorische Steuerung.

## Profil

- Records: `133`

### Bewegungsqualitaet
- role_condensing: `61`
- role_stable: `23`
- role_drifting: `19`
- role_releasing: `19`
- role_core_near_retained: `11`

### Stabilitaetsqualitaet
- gaining_weight: `62`
- stable_surface: `23`
- losing_role_weight: `19`
- variable_but_carried: `14`
- stable_core: `8`
- core_near_retained: `7`

### Driftqualitaet
- surface_role_movement: `57`
- low_drift: `31`
- explicit_role_drift: `19`
- role_releasing_or_fading: `19`
- core_boundary_movement: `7`

## Beispielhafte Records

| Symbol | Token | Bewegung | Stabilitaet | Drift | Klassenfolge |
|---|---|---|---|---|---|
| `dio_role_07g4e01` | `0b7nep9` | role_condensing | core_near_retained | core_boundary_movement | starker_anschlussanker -> brueckenkern -> brueckenkern |
| `dio_role_1ssut42` | `0hjnwsk` | role_condensing | core_near_retained | core_boundary_movement | schwacher_anschluss -> schwacher_anschluss -> brueckenkern |
| `dio_role_18ig317` | `0l3i7ey` | role_condensing | core_near_retained | core_boundary_movement | schwacher_anschluss -> schwacher_anschluss -> brueckenkern |
| `dio_role_1phr90y` | `17c7qwp` | role_condensing | core_near_retained | core_boundary_movement | schwacher_anschluss -> schwacher_anschluss -> brueckenkern |
| `dio_role_0779ibi` | `0v5p8er` | role_condensing | gaining_weight | surface_role_movement | - -> schwacher_anschluss -> starker_anschlussanker |
| `dio_role_0odq05p` | `1jwnjz4` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> starker_anschlussanker -> starker_anschlussanker |
| `dio_role_12j3rgf` | `1q3us3f` | role_condensing | gaining_weight | surface_role_movement | lokaler_anschlussanker -> starker_anschlussanker -> starker_anschlussanker |
| `dio_role_138u9ng` | `077r0df` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker -> lokaler_anschlussanker |
| `dio_role_0iv22zm` | `0om13wf` | role_condensing | gaining_weight | surface_role_movement | - -> - -> lokaler_anschlussanker |
| `dio_role_1dw8ap1` | `0w4x7xs` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker -> lokaler_anschlussanker |
| `dio_role_0zf74ch` | `14l8khu` | role_condensing | gaining_weight | surface_role_movement | - -> lokaler_anschlussanker -> lokaler_anschlussanker |
| `dio_role_1tn82e3` | `1al8fjz` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker -> lokaler_anschlussanker |
| `dio_role_0j3luhj` | `01s42m6` | role_condensing | gaining_weight | surface_role_movement | - -> schwacher_anschluss -> schwacher_anschluss |
| `dio_role_0bjgvzw` | `06ccuqv` | role_condensing | gaining_weight | surface_role_movement | - -> schwacher_anschluss -> schwacher_anschluss |
| `dio_role_0tftzjf` | `079228h` | role_condensing | gaining_weight | surface_role_movement | - -> schwacher_anschluss -> schwacher_anschluss |
| `dio_role_0ix6dsf` | `080f74u` | role_condensing | gaining_weight | surface_role_movement | - -> schwacher_anschluss -> schwacher_anschluss |

## Befund

Die Rollenfolge kann als semantische Bewegung gespeichert werden, ohne das Feld starr zu klassifizieren.
Damit wird Mini-DIOs Memory naeher an der aktuellen MCM-Lesung gehalten:

```text
Nicht: dieses Zeichen ist immer X.
Sondern: dieses Zeichen bewegte sich zwischen Rollen und trug dabei diese Stabilitaets- oder Driftqualitaet.
```

## Wie es weitergeht

Als naechstes sollte diese passive Rollenbewegungs-Memory gegen neue Welten gelesen werden: bleibt ein role_symbol stabil, verdichtet es weiter, oder driftet es?