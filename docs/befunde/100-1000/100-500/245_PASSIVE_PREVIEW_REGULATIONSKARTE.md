# Passive Preview-Regulationskarte

Stand: 2026-06-19 07:57:43

## Zweck

Diese Diagnose liest die lokalen Feld-Episoden-Vorschau-Symbole als passive Regulationskarte.
Sie fragt nicht, was MINI_DIO tun soll, sondern welche Vorschau-Feldlagen mit Stabilisierung, Unruhe, Kippnaehe oder Rekopplung gekoppelt sind.

Wichtig: Das ist keine Handlung, kein Gate, kein Entry-Signal und keine Runtime-Regel.

Hierarchie der Pruefung:

1. Grundfrage: Welche Feldsymbole tragen regulative Innenfeldwirkung?
2. Unterpruefung: Feldsymbol gegen lokale Rolle, Effektklasse, Awareness, Rekopplung, Entlastung und Kippnaehe legen.
3. Folgeschritt: Wiederkehrende Feldsymbole spaeter gegen weitere Welten pruefen.

## Datenbasis

- Fenster gesamt: `72`
- Feldsymbole: `8`
- Rollen: `lokal_rekoppelnd` (42), `lokale_multisensorische_kippnaehe` (30)
- Regulationslesarten: `tragend_unruhig` (4), `rekoppelnd_stabilisierend` (3), `kippnah_variant` (1)

## Staerkste Feldsymbole

| Feldsymbol | Fenster | Welten | Rolle | Effekt | Awareness | Rekopplung | Entlastung | Kipp | Felddruck | Lesart |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| dio_mcm_episode_02xikfk | 48 | PREVIEW_EXP_2023, PREVIEW_NEG_2023, PREVIEW_REAL_2023 | lokal_rekoppelnd (30/48) | stabil (38/48) | inner_effect_stable (38/48) | 0.6303 | 0.7074 | 0.1843 | 0.1956 | rekoppelnd_stabilisierend |
| dio_mcm_episode_1t5bcxp | 6 | PREVIEW_EXP_2023, PREVIEW_NEG_2023 | lokal_rekoppelnd (6/6) | stabil (6/6) | inner_effect_stable (6/6) | 0.6386 | 0.7140 | 0.1677 | 0.1865 | rekoppelnd_stabilisierend |
| dio_mcm_episode_1eik02d | 6 | PREVIEW_EXP_2023, PREVIEW_REAL_2023 | lokale_multisensorische_kippnaehe (4/6) | tragend_unruhig (4/6) | inner_effect_carried_unrest (4/6) | 0.6285 | 0.7025 | 0.1795 | 0.1951 | kippnah_variant |
| dio_mcm_episode_1r7e52w | 4 | PREVIEW_REAL_2023 | lokal_rekoppelnd (4/4) | stabil (4/4) | inner_effect_stable (4/4) | 0.6359 | 0.7112 | 0.1664 | 0.1890 | rekoppelnd_stabilisierend |
| dio_mcm_episode_037i64j | 2 | PREVIEW_REAL_2023 | lokale_multisensorische_kippnaehe (2/2) | tragend_unruhig (2/2) | inner_effect_carried_unrest (2/2) | 0.6159 | 0.7009 | 0.2341 | 0.2144 | tragend_unruhig |
| dio_mcm_episode_0eje6op | 2 | PREVIEW_REAL_2023 | lokale_multisensorische_kippnaehe (2/2) | tragend_unruhig (2/2) | inner_effect_carried_unrest (2/2) | 0.6038 | 0.6859 | 0.2599 | 0.2255 | tragend_unruhig |
| dio_mcm_episode_182yyt2 | 2 | PREVIEW_REAL_2023 | lokale_multisensorische_kippnaehe (2/2) | tragend_unruhig (2/2) | inner_effect_carried_unrest (2/2) | 0.6069 | 0.6900 | 0.2549 | 0.2227 | tragend_unruhig |
| dio_mcm_episode_0e9ekzq | 2 | PREVIEW_REAL_2023 | lokale_multisensorische_kippnaehe (2/2) | tragend_unruhig (2/2) | inner_effect_carried_unrest (2/2) | 0.5960 | 0.6802 | 0.2784 | 0.2345 | tragend_unruhig |

## Vorlaeufige Lesart

`dio_mcm_episode_02xikfk` ist derzeit die wichtigste gemeinsame Vorschau-Feldlage.
Sie tritt in mehreren Welten und besonders in lokalen Rekopplungsfenstern auf.
Das spricht fuer eine passive rekoppelnd-stabilisierende Innenfeldnaehe.

Kippnahe und weltbezogene Varianten bleiben beweglicher.
Dort ist nicht allein das Feldsymbol entscheidend, sondern seine Kopplung an Rolle, Weltspannung und aktuelle Innenfeldwirkung.

## Grenze

Diese Karte beschreibt Regulation nur als beobachtete Feldorganisation.
Sie darf nicht als aktives Kontrollsystem, Handlungsvorgabe oder Beweis fuer eine fertige Bedeutungsstruktur gelesen werden.

## Wie es weitergeht

Als naechstes wird `dio_mcm_episode_02xikfk` isoliert.
Dabei werden Rekopplungsfenster mit diesem Symbol gegen Kippfenster mit demselben Symbol verglichen.
Ziel ist zu pruefen, ob dasselbe Feldsymbol je nach Rolle eine andere Innenfeldwirkung traegt.
