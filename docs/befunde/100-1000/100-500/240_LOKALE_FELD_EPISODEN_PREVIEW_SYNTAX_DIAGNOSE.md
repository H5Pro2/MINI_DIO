# Lokale multisensorische Syntax - Diagnose

Stand: 2026-06-19 07:41:54

## Zweck

Diese Diagnose legt lokale multisensorische Kipp- und Rekopplungsfenster gegen MINI_DIOs eigene Syntax.
Sie prueft, ob lokale Sinnesinnenlagen wiederkehrende Zeichen, Familien oder Feld-Episodensymbole tragen.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Werden lokale multisensorische Innenlagen semantisch wiedererkannt?
2. Unterpruefung: Top-Kippfenster und Top-Rekopplungsfenster gegen Symbol, Symbolfamilie und MCM-Feldsymbol legen.
3. Folgeschritt: Nur bei wiederkehrender Syntax von lokalen Bedeutungsinseln sprechen.

## Rollen und dominante Familien

- `lokal_rekoppelnd` Familien: `dio_01x2` (2), `dio_0f10` (2), `dio_1enk` (2), `dio_1vn6` (2), `dio_1pmi` (2), `dio_1j5i` (2)
- `lokal_rekoppelnd` Feldsymbole: `dio_mcm_episode_02xikfk` (9), `dio_mcm_episode_1r7e52w` (4), `dio_mcm_episode_1eik02d` (1)
- `lokale_multisensorische_kippnaehe` Familien: `dio_0vbe` (2), `dio_0eu7` (2), `dio_0otp` (2), `dio_0p0s` (2), `dio_1d0u` (2)
- `lokale_multisensorische_kippnaehe` Feldsymbole: `dio_mcm_episode_02xikfk` (2), `dio_mcm_episode_0e9ekzq` (2), `dio_mcm_episode_0eje6op` (2), `dio_mcm_episode_182yyt2` (2), `dio_mcm_episode_037i64j` (2)

## Staerkste Syntax-Konzentration

| Welt | Lauf | Ticks | Rolle | Familie | Anteil | Feldsymbol | Anteil | Effekt | Awareness | Syntaxkonz. | Kipp | Entlastung |
|---|---:|---|---|---|---:|---|---:|---|---|---:|---:|---:|
| PREVIEW_2023 | 2 | 561-640 | lokal_rekoppelnd | dio_1j5i | 0.0125 | dio_mcm_episode_02xikfk | 0.8500 | stabil | inner_effect_stable | 0.3760 | 0.1833 | 0.7126 |
| PREVIEW_2023 | 1 | 561-640 | lokal_rekoppelnd | dio_1j5i | 0.0125 | dio_mcm_episode_02xikfk | 0.8375 | stabil | inner_effect_stable | 0.3730 | 0.1833 | 0.7127 |
| PREVIEW_2023 | 2 | 281-360 | lokal_rekoppelnd | dio_1pmi | 0.0250 | dio_mcm_episode_02xikfk | 0.5750 | stabil | inner_effect_stable | 0.3098 | 0.1738 | 0.7082 |
| PREVIEW_2023 | 1 | 281-360 | lokal_rekoppelnd | dio_1pmi | 0.0250 | dio_mcm_episode_02xikfk | 0.5250 | stabil | inner_effect_stable | 0.2978 | 0.1738 | 0.7083 |
| PREVIEW_2023 | 2 | 201-280 | lokal_rekoppelnd | dio_1vn6 | 0.0250 | dio_mcm_episode_02xikfk | 0.4625 | stabil | inner_effect_stable | 0.2795 | 0.1711 | 0.7070 |
| PREVIEW_2023 | 1 | 201-280 | lokal_rekoppelnd | dio_1vn6 | 0.0250 | dio_mcm_episode_1eik02d | 0.4375 | stabil | inner_effect_stable | 0.2735 | 0.1711 | 0.7071 |
| PREVIEW_2023 | 2 | 601-680 | lokal_rekoppelnd | dio_08b7 | 0.0125 | dio_mcm_episode_02xikfk | 0.5625 | stabil | inner_effect_stable | 0.2712 | 0.2060 | 0.7063 |
| PREVIEW_2023 | 1 | 601-680 | lokal_rekoppelnd | dio_08b7 | 0.0125 | dio_mcm_episode_02xikfk | 0.5500 | stabil | inner_effect_stable | 0.2682 | 0.2060 | 0.7064 |
| PREVIEW_2023 | 1 | 161-240 | lokal_rekoppelnd | dio_1enk | 0.0125 | dio_mcm_episode_02xikfk | 0.4000 | stabil | inner_effect_stable | 0.2680 | 0.1720 | 0.7083 |
| PREVIEW_2023 | 2 | 161-240 | lokal_rekoppelnd | dio_1enk | 0.0125 | dio_mcm_episode_02xikfk | 0.4000 | stabil | inner_effect_stable | 0.2680 | 0.1720 | 0.7082 |
| PREVIEW_2023 | 1 | 81-160 | lokal_rekoppelnd | dio_0f10 | 0.0250 | dio_mcm_episode_1r7e52w | 0.3875 | stabil | inner_effect_stable | 0.2648 | 0.1665 | 0.7106 |
| PREVIEW_2023 | 2 | 81-160 | lokal_rekoppelnd | dio_0f10 | 0.0250 | dio_mcm_episode_1r7e52w | 0.3875 | stabil | inner_effect_stable | 0.2648 | 0.1665 | 0.7104 |
| PREVIEW_2023 | 1 | 881-960 | lokale_multisensorische_kippnaehe | dio_1d0u | 0.0250 | dio_mcm_episode_037i64j | 0.4625 | tragend_unruhig | inner_effect_carried_unrest | 0.2438 | 0.2341 | 0.7010 |
| PREVIEW_2023 | 2 | 881-960 | lokale_multisensorische_kippnaehe | dio_1d0u | 0.0250 | dio_mcm_episode_037i64j | 0.4625 | tragend_unruhig | inner_effect_carried_unrest | 0.2438 | 0.2341 | 0.7009 |
| PREVIEW_2023 | 1 | 41-120 | lokal_rekoppelnd | dio_01x2 | 0.0250 | dio_mcm_episode_1r7e52w | 0.2375 | stabil | inner_effect_stable | 0.2418 | 0.1664 | 0.7119 |
| PREVIEW_2023 | 2 | 41-120 | lokal_rekoppelnd | dio_01x2 | 0.0250 | dio_mcm_episode_1r7e52w | 0.2375 | stabil | inner_effect_stable | 0.2418 | 0.1664 | 0.7118 |

## Welt-/Rollenverteilung

- `lokal_rekoppelnd`: `PREVIEW_2023` (14)
- `lokale_multisensorische_kippnaehe`: `PREVIEW_2023` (10)

## Vorlaeufige Lesart

Eine lokale multisensorische Innenlage wird erst dann als Bedeutungsinsel interessant, wenn sie nicht nur hohe Kipp- oder Rekopplungswerte zeigt, sondern auch eigene wiederkehrende Syntax traegt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kipp- und Rekopplungsfenster semantisch getrennte Innenfeldinseln bilden oder nur dieselbe allgemeine Feldsprache wiederholen.
