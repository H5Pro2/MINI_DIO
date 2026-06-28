# MCM-Rolennetzwerk: passive Feldkarte

## Zweck

Diese Datei haelt eine passive Netzwerkkarte aus Rollenbewegung, Rollenwechsel, Rollenreifung und gelesenen Nachbarschaften fest.
Sie ist keine Handlungsschicht, kein Gate und keine Strategie.

## Sicherheitsgrenze

- passive Lesung
- keine Entry-Wirkung
- keine Richtungsvorgabe
- keine Motorik
- keine harte Regel

## Profil

- Knoten: `143`

### Netzwerkzustaende

- `netz_driftend_getragen`: 33
- `netz_rekoppelnd_verbunden`: 30
- `netz_offen_verbunden`: 29
- `netz_rekoppelnd_einzeln`: 26
- `netz_fragmentiert_belastet`: 17
- `netz_zentrum_mit_anschluss`: 6
- `netz_zentrum_getragen`: 2

## Staerkste Knoten

| Symbol | Knoten | Zustand | Rolle | Bewegung | Shift | Stabilitaet | Drift | Nachbarn | Rekopplung | Strain |
|---|---|---|---|---|---|---|---|---:|---:|---:|
| `dio_net_1kl3e5e` | `1hdpu9s` | `netz_zentrum_mit_anschluss` | `absteigende_entlastung` | `role_releasing` | `shift_belastete_reifung_zu_zentrum` | `losing_role_weight` | `role_releasing_or_fading` | 1 | 0.129416 | 0.042373 |
| `dio_net_03w926c` | `0e7qvj1` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 17 | -0.049344 | 0.048507 |
| `dio_net_1wj0zme` | `0b7nep9` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 12 | -0.020791 | 0.022549 |
| `dio_net_0t6wl85` | `0ykar6i` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | -0.012785 | 0.000694 |
| `dio_net_0p0msro` | `18l3thm` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 5 | -0.036458 | 0.027552 |
| `dio_net_0xu44tf` | `1ahj81f` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_verschwinden_zu_zentrum` | `gaining_weight` | `explicit_role_drift` | 0 | 0.680606 | 0.157897 |
| `dio_net_0cgelup` | `0mji3u6` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.017166 | 0.00595 |
| `dio_net_15twx07` | `1jwnjz4` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.034952 | -0.011233 |
| `dio_net_0vlthk7` | `0z748ck` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_bruecke_zu_zentrum_getragen` | `variable_but_carried` | `explicit_role_drift` | 2 | 0.140283 | 0.033946 |
| `dio_net_0564zr4` | `14coypf` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 9 | -0.054896 | 0.052964 |
| `dio_net_147vvmr` | `14l8khu` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 3 | -0.014315 | 0.012257 |
| `dio_net_0ak8npc` | `0v5p8er` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 4 | -0.011001 | 0.006838 |
| `dio_net_1tbmj5q` | `0ybr5e3` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 2 | -0.006616 | -0.017634 |
| `dio_net_1rspn9j` | `1jx2k4i` | `netz_zentrum_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 0 | 0.0 | 0.0 |
| `dio_net_0satnab` | `1q3us3f` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 4 | -0.028827 | 0.023739 |
| `dio_net_1ar5mof` | `18n06fj` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.01524 | 0.007728 |
| `dio_net_1tzgamp` | `0jbl5pq` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 8 | -0.005315 | 0.007955 |
| `dio_net_084j1zr` | `1xx3u1e` | `netz_zentrum_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 0 | 0.0 | 0.0 |
| `dio_net_1k45bql` | `0hjnwsk` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | 0.012822 | -0.023815 |
| `dio_net_1vrl65p` | `0db07p4` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `shift_verschwinden_zu_zentrum` | `stable_core` | `low_drift` | 0 | 0.666626 | 0.169261 |
| `dio_net_0sopvzv` | `0qzjuvj` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | 0.001393 | -0.004459 |
| `dio_net_1wu9qw7` | `1eju9g0` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 1 | 0.020157 | -0.027447 |
| `dio_net_1ea19ll` | `0om13wf` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `shift_weltabhaengig_zu_rekopplung` | `gaining_weight` | `surface_role_movement` | 8 | 0.070646 | -0.007368 |
| `dio_net_1t2czxs` | `0w4x7xs` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 1 | 0.001197 | 0.000601 |
| `dio_net_0xg0n3a` | `0l3i7ey` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | 0.009759 | -0.00501 |
| `dio_net_18gxihp` | `1al8fjz` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 7 | 0.012339 | -0.019083 |
| `dio_net_0vvge8i` | `0geqqo3` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `variable_but_carried` | `explicit_role_drift` | 1 | -0.002461 | 0.005975 |
| `dio_net_0wnw4ph` | `077r0df` | `netz_rekoppelnd_einzeln` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 0 | 0.0 | 0.0 |
| `dio_net_1tan8c8` | `1joiyc3` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 0 | 0.0 | 0.0 |
| `dio_net_05intwy` | `0lne9ax` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 2 | 0.027474 | -0.02329 |
| `dio_net_1vi8ggh` | `0aztxel` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 5 | 0.0176 | -0.021614 |
| `dio_net_0aheenk` | `1ds636q` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.034331 | 0.03265 |

## Interpretation

Das Rolennetzwerk liest nicht nur, ob ein Zeichen vorkommt.
Es liest, welche Feldrolle ein Zeichen traegt, wie diese Rolle wandert, ob Nachbarschaft entsteht und ob der Knoten rekoppelt, driftet oder fragmentiert.

Damit wird die aktuelle Arbeitsannahme technisch greifbar:

```text
Daten liegen nicht nur im Raum.
Das MCM-Feld bildet ein dynamisches Bedeutungsnetz.
```

## Grenze

Diese Netzwerkkarte darf nicht direkt handeln.
Sie darf spaeter nur als gereifte passive Feldkarte fuer weitere Forschung gelesen werden.

## Wie es weitergeht

Als naechstes sollte geprueft werden, welche Bedingungen dazu fuehren, dass ein Knoten stabil bleibt, seine Rolle wechselt, driftet oder rekoppelt.