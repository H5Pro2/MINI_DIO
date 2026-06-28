# MCM-Rollenbewegungs-Memory Lesung

## Zweck

Diese Diagnose liest passive Rollenbewegungs-Memory aus `915_training_894_901` gegen die Folgelandschaft `911_followup_868`.
Geprueft wird, ob `dio_role_*` stabil bleibt, weiter verdichtet, entlastet oder driftet.

## Profil

- Gelesene Rollen-Symbole: `112`

### Lesestatus

| Status | Anzahl |
|---|---:|
| verdichtung_gehalten | 37 |
| nicht_wiedergefunden | 29 |
| stabil_bestaetigt | 23 |
| verdichtung_entlastet_oder_driftet | 10 |
| kernnaehe_gehalten | 8 |
| stabilitaet_gebrochen | 3 |
| entlastung_bestaetigt | 2 |

### Memory-Trends

| Trend | Anzahl |
|---|---:|
| role_condensing | 59 |
| role_stable | 26 |
| role_releasing | 19 |
| role_core_near_retained | 8 |

## Starke Bestaetigungen / Bewegungen

| Symbol | Token | Memory | Aktuell | Lesung | Rangdelta |
|---|---|---|---|---|---:|
| `dio_role_0c7nggw` | `0e7qvj1` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_15x5igq` | `18l3thm` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_0xuioc1` | `0b7nep9` | role_condensing / core_near_retained | brueckenkern | verdichtung_gehalten | 0 |
| `dio_role_1hxibov` | `0mji3u6` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_04fwtzx` | `1joiyc3` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_152ljbs` | `1jwnjz4` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0kj7nsa` | `1q3us3f` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0bx4b71` | `18n06fj` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_117fbbv` | `0jbl5pq` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_0zpfrqb` | `0v5p8er` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 2 |
| `dio_role_0k5tt9o` | `0qzjuvj` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_1hd22yj` | `1eju9g0` | role_condensing / gaining_weight | schwacher_anschluss | verdichtung_gehalten | 0 |
| `dio_role_04lwhlp` | `0db07p4` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_1lq0sw2` | `14l8khu` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0yamhec` | `0w4x7xs` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0ivla1n` | `077r0df` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_015c6f2` | `1al8fjz` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_07r8ira` | `05lquqm` | role_stable / stable_surface | schwacher_anschluss | stabil_bestaetigt | 0 |

## Befund

Die Rollenbewegungs-Memory kann gegen eine Folgelandschaft gelesen werden, ohne daraus Handlung abzuleiten.
Relevant ist nicht, ob ein Token dieselbe Klasse behaelt, sondern ob die gespeicherte Bewegungsqualitaet getragen bleibt.

## Wie es weitergeht

Als naechstes sollte die Lesung mit einer wirklich neuen vierten Landschaft wiederholt werden. Dann kann geprueft werden, ob `dio_role_*` generalisiert oder nur die bisherige Weltfolge beschreibt.