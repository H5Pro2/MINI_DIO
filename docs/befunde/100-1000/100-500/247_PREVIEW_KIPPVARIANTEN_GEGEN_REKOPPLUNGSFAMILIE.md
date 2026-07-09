# Preview-Kippvarianten gegen Rekopplungsfamilie

Stand: 2026-06-19 08:23:23

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
| rekopplungsfamilie | 58 | `PREVIEW_EXP_2023`, `PREVIEW_NEG_2023`, `PREVIEW_REAL_2023` | lokal_rekoppelnd (40/58) | stabil (48/58) | inner_effect_stable (48/58) | 0.6315 | 0.7083 | 0.1814 | 0.1942 | 0.4912 |
| kippvarianten | 8 | `PREVIEW_REAL_2023` | lokale_multisensorische_kippnaehe (8/8) | tragend_unruhig (8/8) | inner_effect_carried_unrest (8/8) | 0.6057 | 0.6892 | 0.2568 | 0.2243 | 0.1719 |

## Kippvarianten im Detail

| Symbol | Fenster | Welten | Ticks | Anteil | Kipp | Entlastung | Rekopplung | Felddruck |
|---|---:|---|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_037i64j | 2 | PREVIEW_REAL_2023 | 1:881-960, 2:881-960 | 0.4625 | 0.2341 | 0.7009 | 0.6159 | 0.2144 |
| dio_mcm_episode_0e9ekzq | 2 | PREVIEW_REAL_2023 | 1:761-840, 2:761-840 | 0.0500 | 0.2784 | 0.6802 | 0.5960 | 0.2345 |
| dio_mcm_episode_0eje6op | 2 | PREVIEW_REAL_2023 | 1:801-880, 2:801-880 | 0.0875 | 0.2599 | 0.6859 | 0.6038 | 0.2255 |
| dio_mcm_episode_182yyt2 | 2 | PREVIEW_REAL_2023 | 1:841-920, 2:841-920 | 0.0875 | 0.2549 | 0.6900 | 0.6069 | 0.2227 |

## Lesart

Die Kippvarianten bilden bisher eine erkennbare Rand-/Spannungsgruppe, aber noch keine mehrweltstabile Familie.
Sie erscheinen aktuell in `PREVIEW_REAL_2023` und reproduzieren sich dort sauber ueber Lauf 1 und Lauf 2.

Gegenueber der Rekopplungsfamilie zeigen sie:

- weniger Fenster,
- staerkere lokale Kippnaehe,
- hoeheren Felddruck,
- geringere Rekopplung und Entlastung,
- eindeutige Kopplung an `tragend_unruhig` / `inner_effect_carried_unrest`.

Damit sind sie fachlich eher Rand-/Spannungsvarianten als reine Abschwaechungen der Rekopplung.
Die Grenze bleibt aber wichtig: mit nur einer Weltbasis sind sie noch nicht als stabile MCM-Familie zu benennen.

## Wie es weitergeht

Als naechstes braucht diese Rand-/Spannungsgruppe eine Folgewelt.
Grundfrage: tauchen dieselben Kippvarianten in weiteren Real- oder Stresswelten wieder auf, oder bleiben sie situative Realwelt-Randzeichen?
