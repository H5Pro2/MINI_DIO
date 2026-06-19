# Lokale multisensorische Kopplung - Diagnose

Stand: 2026-06-19 09:11:13

## Zweck

Diese Diagnose liest kurze Abschnitte innerhalb einer Welt.
Sie prueft, ob Hoeren, Sehen und Fuehlen lokal gemeinsam kippen oder rekoppeln.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Gibt es gemeinsame Sinnesinnenlagen innerhalb einer Welt?
2. Unterpruefung: Wo steigen Hoerlast, Sehlast und Felddruck lokal gemeinsam?
3. Folgeschritt: Pruefen, ob lokale Kippnaehe nur kurz aufflammt oder wiederkehrende Innenfeldinseln bildet.

## Rollen nach Welt

| Welt | lokal offen | lokal rekoppelnd | Sinnesreiben | Kippnaehe |
|---|---:|---:|---:|---:|
| PREVIEW_2024_REAL1 | 22 | 14 | 0 | 10 |
| PREVIEW_EXP_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_MODNEG_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_NEG_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_REAL2_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_REAL3_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_REAL_2023 | 22 | 14 | 0 | 10 |

## Staerkste lokale Kippnaehe

| Welt | Lauf | Ticks | Rolle | Hoerlast | Sehlast | Felddruck | Entlastung | Konflikt | Kippnaehe | Rekopplung |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| PREVIEW_REAL_2023 | 1 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2345 | 0.6803 | 0.2058 | 0.2784 | 0.596159 |
| PREVIEW_REAL_2023 | 2 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2344 | 0.6801 | 0.2057 | 0.2784 | 0.595809 |
| PREVIEW_REAL_2023 | 1 | 721-800 | lokale_multisensorische_kippnaehe | 0.2501 | 0.4094 | 0.2314 | 0.6848 | 0.1991 | 0.2735 | 0.599918 |
| PREVIEW_REAL_2023 | 2 | 721-800 | lokale_multisensorische_kippnaehe | 0.2502 | 0.4094 | 0.2314 | 0.6847 | 0.1990 | 0.2734 | 0.599549 |
| PREVIEW_2024_REAL1 | 1 | 721-800 | lokale_multisensorische_kippnaehe | 0.2291 | 0.4059 | 0.2262 | 0.6902 | 0.2145 | 0.2681 | 0.605009 |
| PREVIEW_2024_REAL1 | 2 | 721-800 | lokale_multisensorische_kippnaehe | 0.2292 | 0.4059 | 0.2262 | 0.6901 | 0.2144 | 0.2681 | 0.604680 |
| PREVIEW_REAL3_2023 | 1 | 321-400 | lokale_multisensorische_kippnaehe | 0.2604 | 0.3995 | 0.2305 | 0.6825 | 0.1618 | 0.2673 | 0.599833 |
| PREVIEW_REAL3_2023 | 2 | 321-400 | lokale_multisensorische_kippnaehe | 0.2605 | 0.3995 | 0.2305 | 0.6824 | 0.1617 | 0.2673 | 0.599533 |
| PREVIEW_REAL3_2023 | 1 | 281-360 | lokale_multisensorische_kippnaehe | 0.2387 | 0.3984 | 0.2266 | 0.6895 | 0.1901 | 0.2649 | 0.605467 |
| PREVIEW_REAL3_2023 | 2 | 281-360 | lokale_multisensorische_kippnaehe | 0.2387 | 0.3984 | 0.2266 | 0.6894 | 0.1900 | 0.2649 | 0.605158 |
| PREVIEW_REAL_2023 | 1 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6859 | 0.1737 | 0.2600 | 0.603969 |
| PREVIEW_REAL_2023 | 2 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6858 | 0.1736 | 0.2599 | 0.603651 |

## Staerkste lokale Rekopplung / Entlastung

| Welt | Lauf | Ticks | Rolle | Entlastung | Fit | Rekopplung | Feldlast | Nachhall |
|---|---:|---|---|---:|---:|---:|---:|---:|
| PREVIEW_EXP_2023 | 1 | 801-880 | lokal_rekoppelnd | 0.7211 | 0.9972 | 0.645018 | 0.1702 | 0.0012 |
| PREVIEW_EXP_2023 | 2 | 801-880 | lokal_rekoppelnd | 0.7210 | 0.9973 | 0.644663 | 0.1700 | 0.0012 |
| PREVIEW_EXP_2023 | 1 | 841-920 | lokal_rekoppelnd | 0.7172 | 0.9914 | 0.642487 | 0.1704 | 0.0011 |
| PREVIEW_EXP_2023 | 2 | 841-920 | lokal_rekoppelnd | 0.7171 | 0.9913 | 0.642147 | 0.1702 | 0.0011 |
| PREVIEW_MODNEG_2023 | 1 | 681-760 | lokal_rekoppelnd | 0.7171 | 0.9822 | 0.639078 | 0.1841 | 0.0003 |
| PREVIEW_EXP_2023 | 1 | 761-840 | lokal_rekoppelnd | 0.7171 | 0.9989 | 0.642047 | 0.1684 | 0.0015 |
| PREVIEW_MODNEG_2023 | 2 | 681-760 | lokal_rekoppelnd | 0.7170 | 0.9821 | 0.638737 | 0.1839 | 0.0003 |
| PREVIEW_EXP_2023 | 2 | 761-840 | lokal_rekoppelnd | 0.7169 | 0.9988 | 0.641720 | 0.1682 | 0.0015 |
| PREVIEW_NEG_2023 | 1 | 441-520 | lokal_rekoppelnd | 0.7147 | 0.9855 | 0.638246 | 0.1785 | 0.0021 |
| PREVIEW_NEG_2023 | 2 | 441-520 | lokal_rekoppelnd | 0.7146 | 0.9854 | 0.637905 | 0.1783 | 0.0021 |
| PREVIEW_EXP_2023 | 1 | 201-280 | lokal_rekoppelnd | 0.7136 | 0.9849 | 0.635457 | 0.1889 | 0.0008 |
| PREVIEW_MODNEG_2023 | 1 | 721-800 | lokal_rekoppelnd | 0.7136 | 0.9868 | 0.637802 | 0.1735 | 0.0001 |

## Vorlaeufige Lesart

Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.
Eine lokale Kippnaehe ist also kein absoluter Grenzwert, sondern ein Abschnitt, der gegen seine eigene Welt deutlich hervortritt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kippnaehe nur Oberflaechenvarianz ist oder eine wiederkehrende multisensorische Innenfeldinsel bildet.
