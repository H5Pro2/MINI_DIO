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

- Knoten: `135`

### Netzwerkzustaende

- `netz_offen_verbunden`: 32
- `netz_fragmentiert_belastet`: 28
- `netz_rekoppelnd_verbunden`: 28
- `netz_driftend_getragen`: 22
- `netz_rekoppelnd_einzeln`: 17
- `netz_zentrum_mit_anschluss`: 8

## Staerkste Knoten

| Symbol | Knoten | Zustand | Rolle | Bewegung | Shift | Stabilitaet | Drift | Nachbarn | Rekopplung | Strain |
|---|---|---|---|---|---|---|---|---:|---:|---:|
| `dio_net_1inbljw` | `1hdpu9s` | `netz_zentrum_mit_anschluss` | `absteigende_entlastung` | `role_releasing` | `shift_belastete_reifung_zu_zentrum` | `losing_role_weight` | `role_releasing_or_fading` | 1 | 0.087958 | 0.034527 |
| `dio_net_1qty2le` | `0e7qvj1` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 17 | -0.047096 | 0.046404 |
| `dio_net_0jei8s8` | `0b7nep9` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 12 | -0.018002 | 0.019335 |
| `dio_net_1ld4xpo` | `0ykar6i` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | -0.010769 | -0.000754 |
| `dio_net_1drs9ec` | `18l3thm` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 5 | -0.037767 | 0.030661 |
| `dio_net_1pxjkxy` | `0mji3u6` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.00838 | -0.002211 |
| `dio_net_03pd3je` | `1ahj81f` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_verschwinden_zu_zentrum` | `gaining_weight` | `explicit_role_drift` | 2 | 0.112021 | -0.021697 |
| `dio_net_0pkatoq` | `1jx2k4i` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | -0.030296 | 0.023696 |
| `dio_net_1bmosds` | `1joiyc3` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 9 | -0.044332 | 0.052125 |
| `dio_net_04m8r5h` | `1jwnjz4` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.038828 | -0.009046 |
| `dio_net_1ociiic` | `1xx3u1e` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | -0.018136 | 0.017662 |
| `dio_net_1tdccpy` | `14coypf` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 9 | -0.057929 | 0.055938 |
| `dio_net_0ypdz0m` | `0z748ck` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_bruecke_zu_zentrum_getragen` | `variable_but_carried` | `explicit_role_drift` | 4 | 0.062197 | 0.010559 |
| `dio_net_1x1awqi` | `0ybr5e3` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 3 | -0.0171 | 0.004285 |
| `dio_net_1vx05tg` | `1q3us3f` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 3 | -0.010811 | 0.002392 |
| `dio_net_0cgecav` | `18n06fj` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.021605 | 0.016558 |
| `dio_net_1nmik0x` | `0db07p4` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `shift_verschwinden_zu_zentrum` | `stable_core` | `low_drift` | 4 | 0.043612 | 0.000893 |
| `dio_net_1p1dr97` | `1eju9g0` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | 0.022509 | -0.029367 |
| `dio_net_09j4rgg` | `0jbl5pq` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 8 | -0.006813 | 0.010451 |
| `dio_net_04cwyql` | `0qzjuvj` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | 0.000347 | -0.002087 |
| `dio_net_1q0u4sz` | `0hjnwsk` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | 0.011086 | -0.022607 |
| `dio_net_14t7pnn` | `14l8khu` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | 0.004184 | -0.00604 |
| `dio_net_078wm4q` | `077r0df` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 1 | 0.011433 | -0.016176 |
| `dio_net_159ijnl` | `0w4x7xs` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.013073 | 0.013784 |
| `dio_net_0xx81gf` | `0v5p8er` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 4 | -0.007885 | 0.006784 |
| `dio_net_0z792ns` | `0geqqo3` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `-` | `variable_but_carried` | `explicit_role_drift` | 2 | 0.006507 | -0.009738 |
| `dio_net_1o0frfa` | `1al8fjz` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 7 | 0.012339 | -0.019083 |
| `dio_net_1o9qxwq` | `0om13wf` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `shift_weltabhaengig_zu_rekopplung` | `gaining_weight` | `surface_role_movement` | 8 | 0.101591 | -0.014785 |
| `dio_net_0rotxyl` | `05lquqm` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 9 | 0.008138 | -0.003916 |
| `dio_net_01y55vp` | `02ujuqf` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 4 | -0.009544 | 0.012344 |
| `dio_net_1u0kgz0` | `0wjn8vm` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 4 | -0.006324 | 0.004409 |
| `dio_net_0dhexgc` | `0lne9ax` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 2 | 0.011995 | -0.00823 |

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