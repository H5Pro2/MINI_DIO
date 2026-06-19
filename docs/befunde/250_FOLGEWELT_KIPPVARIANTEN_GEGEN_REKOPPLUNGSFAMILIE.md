# Preview-Kippvarianten gegen Rekopplungsfamilie

Stand: 2026-06-19 08:51:52

## Zweck

Diese Diagnose vergleicht seltenere Kippvarianten mit der haeufigeren Rekopplungsfamilie.
Sie prueft, ob Rand-/Spannungssymbole eine eigene passive Familie bilden oder nur schwache Varianten der Rekopplungsnaehe sind.

Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.

## Symbolgruppen

- Rekopplungsfamilie: `dio_mcm_episode_02xikfk`, `dio_mcm_episode_1t5bcxp`, `dio_mcm_episode_1r7e52w`
- Kippvarianten: `dio_mcm_episode_037i64j`, `dio_mcm_episode_0e9ekzq`, `dio_mcm_episode_0eje6op`, `dio_mcm_episode_182yyt2`

## Gruppenvergleich

| Gruppe | Fenster | Welten | Rolle | Effekt | Awareness | Rekopplung | Entlastung | Kipp | Felddruck | Symbolanteil |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|
| rekopplungsfamilie | 72 | `PREVIEW_EXP_2023`, `PREVIEW_NEG_2023`, `PREVIEW_REAL2_2023`, `PREVIEW_REAL_2023` | lokal_rekoppelnd (54/72) | stabil (62/72) | inner_effect_stable (62/72) | 0.6324 | 0.7088 | 0.1792 | 0.1931 | 0.4863 |
| kippvarianten | 10 | `PREVIEW_REAL2_2023`, `PREVIEW_REAL_2023` | lokale_multisensorische_kippnaehe (10/10) | tragend_unruhig (10/10) | inner_effect_carried_unrest (10/10) | 0.6052 | 0.6882 | 0.2565 | 0.2244 | 0.1650 |

## Kippvarianten im Detail

| Symbol | Fenster | Welten | Ticks | Anteil | Kipp | Entlastung | Rekopplung | Felddruck |
|---|---:|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_037i64j | 2 | PREVIEW_REAL_2023 | 1:881-960, 2:881-960 | 0.4625 | 0.2341 | 0.7009 | 0.6159 | 0.2144 |
| dio_mcm_episode_0e9ekzq | 2 | PREVIEW_REAL_2023 | 1:761-840, 2:761-840 | 0.0500 | 0.2784 | 0.6802 | 0.5960 | 0.2345 |
| dio_mcm_episode_0eje6op | 2 | PREVIEW_REAL_2023 | 1:801-880, 2:801-880 | 0.0875 | 0.2599 | 0.6859 | 0.6038 | 0.2255 |
| dio_mcm_episode_182yyt2 | 4 | PREVIEW_REAL2_2023, PREVIEW_REAL_2023 | 1:41-120, 2:41-120, 1:841-920, 2:841-920 | 0.1125 | 0.2551 | 0.6869 | 0.6051 | 0.2238 |

## Lesart

Die Kippvarianten bilden weiterhin eine erkennbare Rand-/Spannungsgruppe. Mindestens ein Symbol tritt nun ueber mehrere Welten auf; damit entsteht eine erste Folgewelt-Stuetze, aber noch keine breit mehrweltstabile Familie.

Kippvarianten-Welten: `PREVIEW_REAL2_2023`, `PREVIEW_REAL_2023`
Weltuebergreifend wiederkehrende Kippzeichen: `dio_mcm_episode_182yyt2`

Gegenueber der Rekopplungsfamilie zeigen sie:

- weniger Fenster,
- staerkere lokale Kippnaehe,
- hoeheren Felddruck,
- geringere Rekopplung und Entlastung,
- eindeutige Kopplung an `tragend_unruhig` / `inner_effect_carried_unrest`.

Damit sind sie fachlich eher Rand-/Spannungsvarianten als reine Abschwaechungen der Rekopplung.
Die Grenze bleibt aber wichtig: Eine einzelne Folgewelt-Stuetze reicht noch nicht fuer eine stabile MCM-Familie.

## Wie es weitergeht

Als naechstes sollte genau das wiederkehrende Kippzeichen gegen weitere Real- und Stresswelten gelegt werden. Grundfrage: bleibt es Randspannung, oder wird daraus eine stabile Spannungsfamilie?
