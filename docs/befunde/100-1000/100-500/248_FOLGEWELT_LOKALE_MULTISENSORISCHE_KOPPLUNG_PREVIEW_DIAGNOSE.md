# Lokale multisensorische Kopplung - Diagnose

Stand: 2026-06-19 08:51:11

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
| PREVIEW_EXP_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_NEG_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_REAL2_2023 | 22 | 14 | 0 | 10 |
| PREVIEW_REAL_2023 | 22 | 14 | 0 | 10 |

## Staerkste lokale Kippnaehe

| Welt | Lauf | Ticks | Rolle | Hoerlast | Sehlast | Felddruck | Entlastung | Konflikt | Kippnaehe | Rekopplung |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| PREVIEW_REAL_2023 | 1 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2345 | 0.6803 | 0.2058 | 0.2784 | 0.596159 |
| PREVIEW_REAL_2023 | 2 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2344 | 0.6801 | 0.2057 | 0.2784 | 0.595809 |
| PREVIEW_REAL_2023 | 1 | 721-800 | lokale_multisensorische_kippnaehe | 0.2501 | 0.4094 | 0.2314 | 0.6848 | 0.1991 | 0.2735 | 0.599918 |
| PREVIEW_REAL_2023 | 2 | 721-800 | lokale_multisensorische_kippnaehe | 0.2502 | 0.4094 | 0.2314 | 0.6847 | 0.1990 | 0.2734 | 0.599549 |
| PREVIEW_REAL_2023 | 1 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6859 | 0.1737 | 0.2600 | 0.603969 |
| PREVIEW_REAL_2023 | 2 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6858 | 0.1736 | 0.2599 | 0.603651 |
| PREVIEW_REAL2_2023 | 1 | 41-120 | lokale_multisensorische_kippnaehe | 0.2326 | 0.3839 | 0.2250 | 0.6839 | 0.1648 | 0.2553 | 0.603438 |
| PREVIEW_REAL2_2023 | 2 | 41-120 | lokale_multisensorische_kippnaehe | 0.2327 | 0.3839 | 0.2250 | 0.6838 | 0.1647 | 0.2553 | 0.603151 |
| PREVIEW_REAL_2023 | 1 | 841-920 | lokale_multisensorische_kippnaehe | 0.2129 | 0.3821 | 0.2227 | 0.6901 | 0.1993 | 0.2549 | 0.607073 |
| PREVIEW_REAL_2023 | 2 | 841-920 | lokale_multisensorische_kippnaehe | 0.2130 | 0.3821 | 0.2227 | 0.6900 | 0.1993 | 0.2549 | 0.606749 |
| PREVIEW_REAL2_2023 | 1 | 81-160 | lokale_multisensorische_kippnaehe | 0.2103 | 0.3609 | 0.2199 | 0.6889 | 0.1654 | 0.2427 | 0.607871 |
| PREVIEW_REAL2_2023 | 2 | 81-160 | lokale_multisensorische_kippnaehe | 0.2104 | 0.3609 | 0.2198 | 0.6887 | 0.1654 | 0.2427 | 0.607564 |

## Staerkste lokale Rekopplung / Entlastung

| Welt | Lauf | Ticks | Rolle | Entlastung | Fit | Rekopplung | Feldlast | Nachhall |
|---|---:|---|---|---:|---:|---:|---:|---:|
| PREVIEW_EXP_2023 | 1 | 801-880 | lokal_rekoppelnd | 0.7211 | 0.9972 | 0.645018 | 0.1702 | 0.0012 |
| PREVIEW_EXP_2023 | 2 | 801-880 | lokal_rekoppelnd | 0.7210 | 0.9973 | 0.644663 | 0.1700 | 0.0012 |
| PREVIEW_EXP_2023 | 1 | 841-920 | lokal_rekoppelnd | 0.7172 | 0.9914 | 0.642487 | 0.1704 | 0.0011 |
| PREVIEW_EXP_2023 | 2 | 841-920 | lokal_rekoppelnd | 0.7171 | 0.9913 | 0.642147 | 0.1702 | 0.0011 |
| PREVIEW_EXP_2023 | 1 | 761-840 | lokal_rekoppelnd | 0.7171 | 0.9989 | 0.642047 | 0.1684 | 0.0015 |
| PREVIEW_EXP_2023 | 2 | 761-840 | lokal_rekoppelnd | 0.7169 | 0.9988 | 0.641720 | 0.1682 | 0.0015 |
| PREVIEW_NEG_2023 | 1 | 441-520 | lokal_rekoppelnd | 0.7147 | 0.9855 | 0.638246 | 0.1785 | 0.0021 |
| PREVIEW_NEG_2023 | 2 | 441-520 | lokal_rekoppelnd | 0.7146 | 0.9854 | 0.637905 | 0.1783 | 0.0021 |
| PREVIEW_EXP_2023 | 1 | 201-280 | lokal_rekoppelnd | 0.7136 | 0.9849 | 0.635457 | 0.1889 | 0.0008 |
| PREVIEW_EXP_2023 | 2 | 201-280 | lokal_rekoppelnd | 0.7135 | 0.9848 | 0.635146 | 0.1888 | 0.0008 |
| PREVIEW_NEG_2023 | 1 | 561-640 | lokal_rekoppelnd | 0.7134 | 0.9895 | 0.638176 | 0.1763 | 0.0024 |
| PREVIEW_NEG_2023 | 1 | 321-400 | lokal_rekoppelnd | 0.7133 | 0.9903 | 0.636903 | 0.1815 | 0.0012 |

## Vorlaeufige Lesart

Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.
Eine lokale Kippnaehe ist also kein absoluter Grenzwert, sondern ein Abschnitt, der gegen seine eigene Welt deutlich hervortritt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kippnaehe nur Oberflaechenvarianz ist oder eine wiederkehrende multisensorische Innenfeldinsel bildet.
