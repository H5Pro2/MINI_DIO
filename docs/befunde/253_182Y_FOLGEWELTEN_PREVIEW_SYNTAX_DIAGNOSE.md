# Lokale multisensorische Syntax - Diagnose

Stand: 2026-06-19 08:59:49

## Zweck

Diese Diagnose legt lokale multisensorische Kipp- und Rekopplungsfenster gegen MINI_DIOs eigene Syntax.
Sie prueft, ob lokale Sinnesinnenlagen wiederkehrende Zeichen, Familien oder Feld-Episodensymbole tragen.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Werden lokale multisensorische Innenlagen semantisch wiedererkannt?
2. Unterpruefung: Top-Kippfenster und Top-Rekopplungsfenster gegen Symbol, Symbolfamilie und MCM-Feldsymbol legen.
3. Folgeschritt: Nur bei wiederkehrender Syntax von lokalen Bedeutungsinseln sprechen.

## Rollen und dominante Familien

- `lokal_rekoppelnd` Familien: `dio_0rkf` (4), `dio_0epw` (4), `dio_1f08` (4), `dio_01uf` (4), `dio_01ov` (2), `dio_1b04` (2)
- `lokal_rekoppelnd` Feldsymbole: `dio_mcm_episode_02xikfk` (64), `dio_mcm_episode_1t5bcxp` (10), `dio_mcm_episode_1eik02d` (6), `dio_mcm_episode_1r7e52w` (4)
- `lokale_multisensorische_kippnaehe` Familien: `dio_0ry1` (4), `dio_1jd5` (4), `dio_02xt` (2), `dio_02o7` (2), `dio_0w2x` (2), `dio_0tbo` (2)
- `lokale_multisensorische_kippnaehe` Feldsymbole: `dio_mcm_episode_02xikfk` (28), `dio_mcm_episode_1eik02d` (18), `dio_mcm_episode_037i64j` (6), `dio_mcm_episode_182yyt2` (4), `dio_mcm_episode_0e9ekzq` (2), `dio_mcm_episode_0eje6op` (2)

## Staerkste Syntax-Konzentration

| Welt | Lauf | Ticks | Rolle | Familie | Anteil | Feldsymbol | Anteil | Effekt | Awareness | Syntaxkonz. | Kipp | Entlastung |
|---|---:|---|---|---|---:|---|---:|---|---|---:|---:|---:|
| PREVIEW_NEG_2023 | 1 | 441-520 | lokal_rekoppelnd | dio_1f08 | 0.0125 | dio_mcm_episode_02xikfk | 0.9750 | stabil | inner_effect_stable | 0.4125 | 0.1666 | 0.7147 |
| PREVIEW_NEG_2023 | 2 | 441-520 | lokal_rekoppelnd | dio_1f08 | 0.0125 | dio_mcm_episode_02xikfk | 0.9750 | stabil | inner_effect_stable | 0.4125 | 0.1666 | 0.7146 |
| PREVIEW_MODNEG_2023 | 1 | 721-800 | lokal_rekoppelnd | dio_1nky | 0.0125 | dio_mcm_episode_02xikfk | 0.9750 | stabil | inner_effect_stable | 0.4060 | 0.1645 | 0.7136 |
| PREVIEW_MODNEG_2023 | 2 | 721-800 | lokal_rekoppelnd | dio_1nky | 0.0125 | dio_mcm_episode_02xikfk | 0.9750 | stabil | inner_effect_stable | 0.4060 | 0.1645 | 0.7135 |
| PREVIEW_MODNEG_2023 | 1 | 561-640 | lokal_rekoppelnd | dio_1o05 | 0.0125 | dio_mcm_episode_02xikfk | 1.0000 | stabil | inner_effect_stable | 0.3957 | 0.1839 | 0.7093 |
| PREVIEW_EXP_2023 | 2 | 761-840 | lokal_rekoppelnd | dio_1s8v | 0.0125 | dio_mcm_episode_02xikfk | 0.8250 | stabil | inner_effect_stable | 0.3830 | 0.1613 | 0.7169 |
| PREVIEW_EXP_2023 | 1 | 761-840 | lokal_rekoppelnd | dio_1s8v | 0.0125 | dio_mcm_episode_02xikfk | 0.8125 | stabil | inner_effect_stable | 0.3800 | 0.1613 | 0.7171 |
| PREVIEW_EXP_2023 | 1 | 841-920 | lokal_rekoppelnd | dio_0epw | 0.0250 | dio_mcm_episode_1t5bcxp | 0.8250 | stabil | inner_effect_stable | 0.3795 | 0.1613 | 0.7172 |
| PREVIEW_REAL2_2023 | 2 | 881-960 | lokal_rekoppelnd | dio_0vcp | 0.0375 | dio_mcm_episode_02xikfk | 0.7750 | stabil | inner_effect_stable | 0.3770 | 0.1589 | 0.7115 |
| PREVIEW_REAL_2023 | 2 | 561-640 | lokal_rekoppelnd | dio_1j5i | 0.0125 | dio_mcm_episode_02xikfk | 0.8500 | stabil | inner_effect_stable | 0.3760 | 0.1833 | 0.7126 |
| PREVIEW_REAL_2023 | 1 | 561-640 | lokal_rekoppelnd | dio_1j5i | 0.0125 | dio_mcm_episode_02xikfk | 0.8375 | stabil | inner_effect_stable | 0.3730 | 0.1833 | 0.7127 |
| PREVIEW_MODNEG_2023 | 2 | 881-960 | lokal_rekoppelnd | dio_1ldk | 0.0250 | dio_mcm_episode_02xikfk | 0.8750 | stabil | inner_effect_stable | 0.3720 | 0.1744 | 0.7108 |
| PREVIEW_MODNEG_2023 | 1 | 881-960 | lokal_rekoppelnd | dio_1ldk | 0.0250 | dio_mcm_episode_02xikfk | 0.8625 | stabil | inner_effect_stable | 0.3690 | 0.1744 | 0.7109 |
| PREVIEW_EXP_2023 | 2 | 841-920 | lokal_rekoppelnd | dio_0epw | 0.0250 | dio_mcm_episode_1t5bcxp | 0.7750 | stabil | inner_effect_stable | 0.3675 | 0.1612 | 0.7171 |
| PREVIEW_REAL2_2023 | 1 | 881-960 | lokal_rekoppelnd | dio_0vcp | 0.0375 | dio_mcm_episode_02xikfk | 0.7125 | stabil | inner_effect_stable | 0.3620 | 0.1590 | 0.7117 |
| PREVIEW_MODNEG_2023 | 1 | 681-760 | lokal_rekoppelnd | dio_0ooz | 0.0125 | dio_mcm_episode_02xikfk | 0.7875 | stabil | inner_effect_stable | 0.3448 | 0.1717 | 0.7171 |

## Welt-/Rollenverteilung

- `lokal_rekoppelnd`: `PREVIEW_EXP_2023` (14), `PREVIEW_MODNEG_2023` (14), `PREVIEW_NEG_2023` (14), `PREVIEW_REAL2_2023` (14), `PREVIEW_REAL3_2023` (14), `PREVIEW_REAL_2023` (14)
- `lokale_multisensorische_kippnaehe`: `PREVIEW_EXP_2023` (10), `PREVIEW_MODNEG_2023` (10), `PREVIEW_NEG_2023` (10), `PREVIEW_REAL2_2023` (10), `PREVIEW_REAL3_2023` (10), `PREVIEW_REAL_2023` (10)

## Vorlaeufige Lesart

Eine lokale multisensorische Innenlage wird erst dann als Bedeutungsinsel interessant, wenn sie nicht nur hohe Kipp- oder Rekopplungswerte zeigt, sondern auch eigene wiederkehrende Syntax traegt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kipp- und Rekopplungsfenster semantisch getrennte Innenfeldinseln bilden oder nur dieselbe allgemeine Feldsprache wiederholen.
