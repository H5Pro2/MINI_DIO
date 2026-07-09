# Lokale multisensorische Syntax - Diagnose

Stand: 2026-06-19 07:24:42

## Zweck

Diese Diagnose legt lokale multisensorische Kipp- und Rekopplungsfenster gegen MINI_DIOs eigene Syntax.
Sie prueft, ob lokale Sinnesinnenlagen wiederkehrende Zeichen, Familien oder Feld-Episodensymbole tragen.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Werden lokale multisensorische Innenlagen semantisch wiedererkannt?
2. Unterpruefung: Top-Kippfenster und Top-Rekopplungsfenster gegen Symbol, Symbolfamilie und MCM-Feldsymbol legen.
3. Folgeschritt: Nur bei wiederkehrender Syntax von lokalen Bedeutungsinseln sprechen.

## Rollen und dominante Familien

- `lokal_rekoppelnd` Familien: `dio_054b` (4), `dio_0ti6` (4), `dio_1ttr` (4), `dio_0rkf` (4), `dio_1ril` (4), `dio_1qzl` (2)
- `lokal_rekoppelnd` Feldsymbole: `-` (160)
- `lokale_multisensorische_kippnaehe` Familien: `dio_0wc3` (6), `dio_00cf` (3), `dio_1poi` (2), `dio_1nmf` (2), `dio_1ruk` (2), `dio_0kh1` (2)
- `lokale_multisensorische_kippnaehe` Feldsymbole: `-` (121)

## Staerkste Syntax-Konzentration

| Welt | Lauf | Ticks | Rolle | Familie | Anteil | Feldsymbol | Anteil | Effekt | Awareness | Syntaxkonz. | Kipp | Entlastung |
|---|---:|---|---|---|---:|---|---:|---|---|---:|---:|---:|
| SOL_2025_5M | 1 | 561-640 | lokal_rekoppelnd | dio_04pt | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4410 | 0.1581 | 0.7204 |
| SOL_2025_5M | 2 | 561-640 | lokal_rekoppelnd | dio_04pt | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4410 | 0.1580 | 0.7202 |
| SOL_2025_5M | 1 | 1281-1360 | lokal_rekoppelnd | dio_06wt | 0.0250 | - | 0.9500 | stabil | inner_effect_stable | 0.4323 | 0.1620 | 0.7168 |
| SOL_2025_5M | 2 | 1281-1360 | lokal_rekoppelnd | dio_06wt | 0.0250 | - | 0.9500 | stabil | inner_effect_stable | 0.4290 | 0.1619 | 0.7167 |
| SOL_2025_5M | 1 | 1761-1840 | lokal_rekoppelnd | dio_1ril | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4280 | 0.1607 | 0.7153 |
| SOL_2025_5M | 2 | 1761-1840 | lokal_rekoppelnd | dio_1ril | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4280 | 0.1606 | 0.7151 |
| SOL_2025_5M | 1 | 1481-1560 | lokal_rekoppelnd | dio_0mhv | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4215 | 0.1681 | 0.7181 |
| SOL_2025_5M | 1 | 1801-1880 | lokal_rekoppelnd | dio_1ril | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4215 | 0.1660 | 0.7192 |
| SOL_2025_5M | 2 | 1481-1560 | lokal_rekoppelnd | dio_0mhv | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4215 | 0.1681 | 0.7180 |
| SOL_2025_5M | 2 | 1801-1880 | lokal_rekoppelnd | dio_1ril | 0.0250 | - | 1.0000 | stabil | inner_effect_stable | 0.4215 | 0.1659 | 0.7191 |
| SOL_2025_5M | 1 | 1521-1600 | lokal_rekoppelnd | dio_1xoy | 0.0250 | - | 0.9750 | stabil | inner_effect_stable | 0.4188 | 0.1634 | 0.7214 |
| SOL_2025_5M | 2 | 1521-1600 | lokal_rekoppelnd | dio_1xoy | 0.0250 | - | 0.9750 | stabil | inner_effect_stable | 0.4188 | 0.1633 | 0.7213 |
| SOL_2025_5M | 1 | 961-1040 | lokal_rekoppelnd | dio_0g71 | 0.0125 | - | 0.9750 | stabil | inner_effect_stable | 0.4158 | 0.1574 | 0.7136 |
| SOL_2025_5M | 2 | 961-1040 | lokal_rekoppelnd | dio_0g71 | 0.0125 | - | 0.9750 | stabil | inner_effect_stable | 0.4158 | 0.1574 | 0.7134 |
| SOL_2025_5M | 1 | 1001-1080 | lokal_rekoppelnd | dio_0v26 | 0.0250 | - | 0.9500 | stabil | inner_effect_stable | 0.4128 | 0.1592 | 0.7169 |
| SOL_2025_5M | 2 | 1001-1080 | lokal_rekoppelnd | dio_0v26 | 0.0250 | - | 0.9500 | stabil | inner_effect_stable | 0.4128 | 0.1591 | 0.7168 |

## Welt-/Rollenverteilung

- `lokal_rekoppelnd`: `SOL_2024_30M` (29), `SOL_2024_5M` (29), `SOL_2025_30M` (29), `SOL_2025_5M` (29), `SOL_2025_1H` (26), `SOL_2024_1H` (18)
- `lokale_multisensorische_kippnaehe`: `SOL_2024_1H` (20), `SOL_2024_30M` (20), `SOL_2024_5M` (20), `SOL_2025_1H` (20), `SOL_2025_30M` (20), `SOL_2025_5M` (18), `STRESS_2023_TEST4` (1), `STRESS_2024_REAL` (1), `STRESS_2025_STRESS` (1)

## Vorlaeufige Lesart

Eine lokale multisensorische Innenlage wird erst dann als Bedeutungsinsel interessant, wenn sie nicht nur hohe Kipp- oder Rekopplungswerte zeigt, sondern auch eigene wiederkehrende Syntax traegt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kipp- und Rekopplungsfenster semantisch getrennte Innenfeldinseln bilden oder nur dieselbe allgemeine Feldsprache wiederholen.
