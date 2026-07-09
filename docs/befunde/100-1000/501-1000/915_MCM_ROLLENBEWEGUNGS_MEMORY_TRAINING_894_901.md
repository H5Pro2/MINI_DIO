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

- Records: `112`

### Bewegungsqualitaet
- role_condensing: `59`
- role_stable: `26`
- role_releasing: `19`
- role_core_near_retained: `8`

### Stabilitaetsqualitaet
- gaining_weight: `52`
- stable_surface: `26`
- losing_role_weight: `19`
- stable_core: `8`
- core_near_retained: `7`

### Driftqualitaet
- surface_role_movement: `52`
- low_drift: `34`
- role_releasing_or_fading: `19`
- core_boundary_movement: `7`

## Beispielhafte Records

| Symbol | Token | Bewegung | Stabilitaet | Drift | Klassenfolge |
|---|---|---|---|---|---|
| `dio_role_19qvilb` | `02ujuqf` | role_condensing | core_near_retained | core_boundary_movement | - -> brueckenkern |
| `dio_role_0xuioc1` | `0b7nep9` | role_condensing | core_near_retained | core_boundary_movement | starker_anschlussanker -> brueckenkern |
| `dio_role_1dhtnye` | `0ykar6i` | role_condensing | core_near_retained | core_boundary_movement | schwacher_anschluss -> brueckenkern |
| `dio_role_006s4ho` | `0z748ck` | role_condensing | core_near_retained | core_boundary_movement | lokaler_anschlussanker -> brueckenkern |
| `dio_role_0ivr2vw` | `14coypf` | role_condensing | core_near_retained | core_boundary_movement | - -> brueckenkern |
| `dio_role_0qnck5t` | `1jx2k4i` | role_condensing | core_near_retained | core_boundary_movement | starker_anschlussanker -> brueckenkern |
| `dio_role_143lfe3` | `1xx3u1e` | role_condensing | core_near_retained | core_boundary_movement | lokaler_anschlussanker -> brueckenkern |
| `dio_role_0krdv3d` | `0ybr5e3` | role_condensing | gaining_weight | surface_role_movement | - -> starker_anschlussanker |
| `dio_role_185g3ba` | `1ahj81f` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> starker_anschlussanker |
| `dio_role_152ljbs` | `1jwnjz4` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> starker_anschlussanker |
| `dio_role_0kj7nsa` | `1q3us3f` | role_condensing | gaining_weight | surface_role_movement | lokaler_anschlussanker -> starker_anschlussanker |
| `dio_role_0ivla1n` | `077r0df` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker |
| `dio_role_063jbt5` | `0geqqo3` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker |
| `dio_role_0yamhec` | `0w4x7xs` | role_condensing | gaining_weight | surface_role_movement | schwacher_anschluss -> lokaler_anschlussanker |
| `dio_role_1rkdnd8` | `0wjn8vm` | role_condensing | gaining_weight | surface_role_movement | - -> lokaler_anschlussanker |
| `dio_role_1lq0sw2` | `14l8khu` | role_condensing | gaining_weight | surface_role_movement | - -> lokaler_anschlussanker |

## Befund

Die Rollenfolge kann als semantische Bewegung gespeichert werden, ohne das Feld starr zu klassifizieren.
Damit wird Mini-DIOs Memory naeher an der aktuellen MCM-Lesung gehalten:

```text
Nicht: dieses Zeichen ist immer X.
Sondern: dieses Zeichen bewegte sich zwischen Rollen und trug dabei diese Stabilitaets- oder Driftqualitaet.
```

## Wie es weitergeht

Als naechstes sollte diese passive Rollenbewegungs-Memory gegen neue Welten gelesen werden: bleibt ein role_symbol stabil, verdichtet es weiter, oder driftet es?