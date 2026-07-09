# MCM-Rollenbewegungs-Memory Lesung

## Zweck

Diese Diagnose liest passive Rollenbewegungs-Memory aus `915_training_894_901` gegen die Folgelandschaft `923_fourth_adapted`.
Geprueft wird, ob `dio_role_*` stabil bleibt, weiter verdichtet, entlastet oder driftet.

## Profil

- Gelesene Rollen-Symbole: `112`

### Lesestatus

| Status | Anzahl |
|---|---:|
| verdichtung_gehalten | 48 |
| nicht_wiedergefunden | 28 |
| stabil_bestaetigt | 22 |
| kernnaehe_gehalten | 7 |
| verdichtung_entlastet_oder_driftet | 3 |
| entlastung_bestaetigt | 2 |
| kernnaehe_verloren | 1 |
| stabilitaet_gebrochen | 1 |

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
| `dio_role_0xuioc1` | `0b7nep9` | role_condensing / core_near_retained | brueckenkern | verdichtung_gehalten | 0 |
| `dio_role_1dhtnye` | `0ykar6i` | role_condensing / core_near_retained | brueckenkern | verdichtung_gehalten | 0 |
| `dio_role_15x5igq` | `18l3thm` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_1hxibov` | `0mji3u6` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_152ljbs` | `1jwnjz4` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0ivr2vw` | `14coypf` | role_condensing / core_near_retained | brueckenkern | verdichtung_gehalten | 0 |
| `dio_role_04fwtzx` | `1joiyc3` | role_core_near_retained / stable_core | starker_anschlussanker | kernnaehe_gehalten | -1 |
| `dio_role_143lfe3` | `1xx3u1e` | role_condensing / core_near_retained | brueckenkern | verdichtung_gehalten | 0 |
| `dio_role_0krdv3d` | `0ybr5e3` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0kj7nsa` | `1q3us3f` | role_condensing / gaining_weight | starker_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0bx4b71` | `18n06fj` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_117fbbv` | `0jbl5pq` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_0k5tt9o` | `0qzjuvj` | role_core_near_retained / stable_core | brueckenkern | kernnaehe_gehalten | 0 |
| `dio_role_063jbt5` | `0geqqo3` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_1hd22yj` | `1eju9g0` | role_condensing / gaining_weight | schwacher_anschluss | verdichtung_gehalten | 0 |
| `dio_role_0yamhec` | `0w4x7xs` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |
| `dio_role_0ivla1n` | `077r0df` | role_condensing / gaining_weight | lokaler_anschlussanker | verdichtung_gehalten | 0 |

## Befund

Die Rollenbewegungs-Memory kann gegen eine Folgelandschaft gelesen werden, ohne daraus Handlung abzuleiten.
Relevant ist nicht, ob ein Token dieselbe Klasse behaelt, sondern ob die gespeicherte Bewegungsqualitaet getragen bleibt.

## Wie es weitergeht

Als naechstes sollte die Lesung mit einer wirklich neuen vierten Landschaft wiederholt werden. Dann kann geprueft werden, ob `dio_role_*` generalisiert oder nur die bisherige Weltfolge beschreibt.