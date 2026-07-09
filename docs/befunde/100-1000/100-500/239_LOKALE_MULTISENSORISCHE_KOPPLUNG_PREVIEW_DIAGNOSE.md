# Lokale multisensorische Kopplung - Diagnose

Stand: 2026-06-19 07:41:53

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
| PREVIEW_2023 | 22 | 14 | 0 | 10 |

## Staerkste lokale Kippnaehe

| Welt | Lauf | Ticks | Rolle | Hoerlast | Sehlast | Felddruck | Entlastung | Konflikt | Kippnaehe | Rekopplung |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| PREVIEW_2023 | 1 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2345 | 0.6803 | 0.2058 | 0.2784 | 0.596159 |
| PREVIEW_2023 | 2 | 761-840 | lokale_multisensorische_kippnaehe | 0.2477 | 0.4235 | 0.2344 | 0.6801 | 0.2057 | 0.2784 | 0.595809 |
| PREVIEW_2023 | 1 | 721-800 | lokale_multisensorische_kippnaehe | 0.2501 | 0.4094 | 0.2314 | 0.6848 | 0.1991 | 0.2735 | 0.599918 |
| PREVIEW_2023 | 2 | 721-800 | lokale_multisensorische_kippnaehe | 0.2502 | 0.4094 | 0.2314 | 0.6847 | 0.1990 | 0.2734 | 0.599549 |
| PREVIEW_2023 | 1 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6859 | 0.1737 | 0.2600 | 0.603969 |
| PREVIEW_2023 | 2 | 801-880 | lokale_multisensorische_kippnaehe | 0.2385 | 0.3906 | 0.2255 | 0.6858 | 0.1736 | 0.2599 | 0.603651 |
| PREVIEW_2023 | 1 | 841-920 | lokale_multisensorische_kippnaehe | 0.2129 | 0.3821 | 0.2227 | 0.6901 | 0.1993 | 0.2549 | 0.607073 |
| PREVIEW_2023 | 2 | 841-920 | lokale_multisensorische_kippnaehe | 0.2130 | 0.3821 | 0.2227 | 0.6900 | 0.1993 | 0.2549 | 0.606749 |
| PREVIEW_2023 | 1 | 881-960 | lokale_multisensorische_kippnaehe | 0.2052 | 0.3425 | 0.2144 | 0.7010 | 0.1596 | 0.2341 | 0.616102 |
| PREVIEW_2023 | 2 | 881-960 | lokale_multisensorische_kippnaehe | 0.2053 | 0.3425 | 0.2143 | 0.7009 | 0.1595 | 0.2341 | 0.615735 |
| PREVIEW_2023 | 1 | 361-440 | lokal_offen | 0.2297 | 0.3091 | 0.2099 | 0.7004 | 0.0874 | 0.2189 | 0.619053 |
| PREVIEW_2023 | 2 | 361-440 | lokal_offen | 0.2298 | 0.3091 | 0.2099 | 0.7003 | 0.0873 | 0.2189 | 0.618711 |

## Staerkste lokale Rekopplung / Entlastung

| Welt | Lauf | Ticks | Rolle | Entlastung | Fit | Rekopplung | Feldlast | Nachhall |
|---|---:|---|---|---:|---:|---:|---:|---:|
| PREVIEW_2023 | 1 | 561-640 | lokal_rekoppelnd | 0.7127 | 0.9805 | 0.634331 | 0.1941 | 0.0003 |
| PREVIEW_2023 | 2 | 561-640 | lokal_rekoppelnd | 0.7126 | 0.9804 | 0.634014 | 0.1939 | 0.0003 |
| PREVIEW_2023 | 1 | 41-120 | lokal_rekoppelnd | 0.7119 | 0.9973 | 0.635840 | 0.1794 | 0.0005 |
| PREVIEW_2023 | 2 | 41-120 | lokal_rekoppelnd | 0.7118 | 0.9972 | 0.635528 | 0.1792 | 0.0005 |
| PREVIEW_2023 | 1 | 81-160 | lokal_rekoppelnd | 0.7106 | 0.9924 | 0.636213 | 0.1754 | 0.0032 |
| PREVIEW_2023 | 2 | 81-160 | lokal_rekoppelnd | 0.7104 | 0.9924 | 0.635890 | 0.1753 | 0.0032 |
| PREVIEW_2023 | 1 | 281-360 | lokal_rekoppelnd | 0.7083 | 0.9933 | 0.634414 | 0.1748 | 0.0021 |
| PREVIEW_2023 | 1 | 161-240 | lokal_rekoppelnd | 0.7083 | 0.9985 | 0.632779 | 0.1782 | 0.0014 |
| PREVIEW_2023 | 2 | 281-360 | lokal_rekoppelnd | 0.7082 | 0.9932 | 0.634111 | 0.1747 | 0.0021 |
| PREVIEW_2023 | 2 | 161-240 | lokal_rekoppelnd | 0.7082 | 0.9986 | 0.632460 | 0.1780 | 0.0014 |
| PREVIEW_2023 | 1 | 201-280 | lokal_rekoppelnd | 0.7071 | 0.9936 | 0.632629 | 0.1767 | 0.0013 |
| PREVIEW_2023 | 2 | 201-280 | lokal_rekoppelnd | 0.7070 | 0.9935 | 0.632311 | 0.1766 | 0.0013 |

## Vorlaeufige Lesart

Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.
Eine lokale Kippnaehe ist also kein absoluter Grenzwert, sondern ein Abschnitt, der gegen seine eigene Welt deutlich hervortritt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kippnaehe nur Oberflaechenvarianz ist oder eine wiederkehrende multisensorische Innenfeldinsel bildet.
