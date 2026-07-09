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

- `netz_offen_verbunden`: 37
- `netz_rekoppelnd_verbunden`: 32
- `netz_fragmentiert_belastet`: 28
- `netz_driftend_getragen`: 22
- `netz_rekoppelnd_einzeln`: 16
- `netz_zentrum_mit_anschluss`: 8

## Staerkste Knoten

| Symbol | Knoten | Zustand | Rolle | Bewegung | Shift | Stabilitaet | Drift | Nachbarn | Rekopplung | Strain |
|---|---|---|---|---|---|---|---|---:|---:|---:|
| `dio_net_0u7d31q` | `1hdpu9s` | `netz_zentrum_mit_anschluss` | `absteigende_entlastung` | `role_releasing` | `shift_belastete_reifung_zu_zentrum` | `losing_role_weight` | `role_releasing_or_fading` | 1 | 0.050269 | 0.027394 |
| `dio_net_156gakz` | `0e7qvj1` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 17 | -0.047943 | 0.047196 |
| `dio_net_0bqtksx` | `0b7nep9` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 12 | -0.018709 | 0.020149 |
| `dio_net_08aerg3` | `0ykar6i` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | -0.011399 | -0.000302 |
| `dio_net_10tqzxt` | `18l3thm` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 5 | -0.037385 | 0.029754 |
| `dio_net_1g6v5it` | `0mji3u6` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.010964 | 0.000189 |
| `dio_net_0fldgaf` | `1jwnjz4` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.037375 | -0.009866 |
| `dio_net_03pd3je` | `1ahj81f` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_verschwinden_zu_zentrum` | `gaining_weight` | `explicit_role_drift` | 2 | 0.112021 | -0.021697 |
| `dio_net_055gqfg` | `14coypf` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 9 | -0.056852 | 0.054883 |
| `dio_net_0pkatoq` | `1jx2k4i` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | -0.030296 | 0.023696 |
| `dio_net_1bmosds` | `1joiyc3` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 9 | -0.044332 | 0.052125 |
| `dio_net_1ociiic` | `1xx3u1e` | `netz_zentrum_mit_anschluss` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | -0.018136 | 0.017662 |
| `dio_net_0jcuwlt` | `0z748ck` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `shift_bruecke_zu_zentrum_getragen` | `variable_but_carried` | `explicit_role_drift` | 4 | 0.045301 | 0.00868 |
| `dio_net_0rivykr` | `1q3us3f` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 4 | -0.018738 | 0.011784 |
| `dio_net_0qxe252` | `0ybr5e3` | `netz_fragmentiert_belastet` | `rollendrift` | `role_drifting` | `-` | `gaining_weight` | `explicit_role_drift` | 3 | -0.015003 | -9.9e-05 |
| `dio_net_1s4wb86` | `18n06fj` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | -0.019749 | 0.013983 |
| `dio_net_1vmtj6p` | `0jbl5pq` | `netz_fragmentiert_belastet` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 8 | -0.006192 | 0.009415 |
| `dio_net_05ovale` | `0qzjuvj` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `-` | `stable_core` | `low_drift` | 4 | 0.000765 | -0.003036 |
| `dio_net_0e2cww8` | `14l8khu` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 3 | -0.006915 | 0.004938 |
| `dio_net_03ldthk` | `0hjnwsk` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 5 | 0.011896 | -0.02317 |
| `dio_net_1msvd2c` | `1eju9g0` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | 0.022039 | -0.028983 |
| `dio_net_1g5iv0y` | `0v5p8er` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 4 | -0.009443 | 0.006811 |
| `dio_net_1nmik0x` | `0db07p4` | `netz_driftend_getragen` | `kernnah_gehalten` | `role_core_near_retained` | `shift_verschwinden_zu_zentrum` | `stable_core` | `low_drift` | 4 | 0.043612 | 0.000893 |
| `dio_net_17oo6dm` | `0w4x7xs` | `netz_offen_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 2 | -0.010479 | 0.011387 |
| `dio_net_1mypvxu` | `0geqqo3` | `netz_driftend_getragen` | `rollendrift` | `role_drifting` | `-` | `variable_but_carried` | `explicit_role_drift` | 2 | 0.005012 | -0.007119 |
| `dio_net_078wm4q` | `077r0df` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 1 | 0.011433 | -0.016176 |
| `dio_net_0osr8is` | `0om13wf` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `shift_weltabhaengig_zu_rekopplung` | `gaining_weight` | `surface_role_movement` | 8 | 0.062293 | -0.018114 |
| `dio_net_1qizcm6` | `1al8fjz` | `netz_rekoppelnd_verbunden` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `gaining_weight` | `surface_role_movement` | 7 | 0.012339 | -0.019083 |
| `dio_net_01689kl` | `0l3i7ey` | `netz_zentrum_mit_anschluss` | `aufsteigende_verdichtung` | `role_condensing` | `-` | `core_near_retained` | `core_boundary_movement` | 6 | 0.009483 | -0.00449 |
| `dio_net_0ap6ov1` | `0lne9ax` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 2 | 0.020438 | -0.016444 |
| `dio_net_0rotxyl` | `05lquqm` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 9 | 0.008138 | -0.003916 |
| `dio_net_0e5zwxh` | `0aztxel` | `netz_driftend_getragen` | `stabile_rolle` | `role_stable` | `-` | `stable_surface` | `low_drift` | 5 | 0.017652 | -0.022601 |

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