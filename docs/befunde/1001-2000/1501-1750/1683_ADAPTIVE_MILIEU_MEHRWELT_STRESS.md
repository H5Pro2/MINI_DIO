# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:00:32

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_worlds\stress\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `30`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0144 |
| alignment | 0.0029 |
| strain_relief | 0.0073 |
| sensory | 0.0099 |
| role_experience | 0.8303 |
| path_experience | 0.8250 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_155c | 52 | stabil | milieu_rollennah | 0.7489 | 0.0396 | 0.4562 | 0.6426 | 0.0168 | 0.2915 | 0.2172 | 0.2738 | 0.2176 | 0.0111 |
| field_stabil::dio_104t | 47 | stabil | milieu_offen | 0.7528 | 0.0388 | 0.3369 | 0.4557 | 0.0745 | 0.2939 | 0.2172 | 0.2736 | 0.2153 | 0.0099 |
| field_stabil::dio_0h9h | 36 | stabil | milieu_offen | 0.7592 | 0.0418 | 0.3040 | 0.4444 | 0.0104 | 0.2910 | 0.2168 | 0.2746 | 0.2176 | 0.0061 |
| field_stabil::dio_0m9z | 28 | stabil | milieu_pfadnah | 0.7401 | 0.0377 | 0.2738 | 0.1726 | 0.2679 | 0.2964 | 0.2181 | 0.2731 | 0.2123 | 0.0093 |
| field_stabil::dio_06s7 | 25 | stabil | milieu_offen | 0.7650 | 0.0427 | 0.2044 | 0.2500 | 0.0450 | 0.2945 | 0.2170 | 0.2739 | 0.2147 | 0.0104 |
| field_stabil::dio_0l7p | 23 | stabil | milieu_offen | 0.7576 | 0.0417 | 0.2560 | 0.2681 | 0.1739 | 0.2945 | 0.2168 | 0.2730 | 0.2157 | 0.0070 |
| field_stabil::dio_14wj | 17 | stabil | milieu_offen | 0.7632 | 0.0449 | 0.1242 | 0.1275 | 0.0588 | 0.2885 | 0.2174 | 0.2748 | 0.2193 | 0.0020 |
| field_stabil::dio_17ct | 17 | stabil | milieu_offen | 0.7483 | 0.0439 | 0.3105 | 0.3922 | 0.0221 | 0.2919 | 0.2171 | 0.2736 | 0.2174 | 0.0064 |
| field_stabil::dio_0pz6 | 16 | stabil | milieu_offen | 0.7649 | 0.0460 | 0.3021 | 0.3490 | 0.2031 | 0.2908 | 0.2170 | 0.2742 | 0.2180 | 0.0055 |
| field_stabil::dio_1gp2 | 15 | stabil | milieu_offen | 0.7418 | 0.0407 | 0.2111 | 0.1556 | 0.2083 | 0.2947 | 0.2180 | 0.2753 | 0.2120 | 0.0088 |
| field_stabil::dio_0oc3 | 14 | stabil | milieu_offen | 0.7271 | 0.0423 | 0.3849 | 0.3690 | 0.3571 | 0.2933 | 0.2183 | 0.2740 | 0.2145 | 0.0096 |
| field_stabil::dio_0g2r | 13 | stabil | milieu_offen | 0.7427 | 0.0431 | 0.4487 | 0.4487 | 0.3365 | 0.2906 | 0.2178 | 0.2747 | 0.2169 | 0.0057 |
| field_stabil::dio_1q85 | 13 | stabil | milieu_rolle_und_pfad_getragen | 0.7333 | 0.0389 | 0.7991 | 0.7949 | 0.7212 | 0.3029 | 0.2195 | 0.2682 | 0.2094 | 0.1328 |
| field_tragend_unruhig::dio_00ja | 12 | tragend_unruhig | milieu_offen | 0.7273 | 0.0364 | 0.2731 | 0.2778 | 0.0208 | 0.2960 | 0.2181 | 0.2748 | 0.2111 | 0.0113 |
| field_stabil::dio_1mwv | 11 | stabil | milieu_offen | 0.7536 | 0.0476 | 0.2172 | 0.2955 | 0.0114 | 0.2902 | 0.2171 | 0.2743 | 0.2183 | 0.0066 |
| field_stabil::dio_00ly | 11 | stabil | milieu_offen | 0.7545 | 0.0469 | 0.1869 | 0.2348 | 0.0000 | 0.2894 | 0.2166 | 0.2753 | 0.2187 | 0.0040 |
| field_stabil::dio_1ewh | 11 | stabil | milieu_offen | 0.7375 | 0.0444 | 0.1970 | 0.2197 | 0.0341 | 0.2891 | 0.2168 | 0.2753 | 0.2188 | 0.0039 |
| field_stabil::dio_00ja | 11 | stabil | milieu_offen | 0.7374 | 0.0404 | 0.1616 | 0.0530 | 0.2045 | 0.2947 | 0.2182 | 0.2755 | 0.2116 | 0.0129 |
| field_tragend_unruhig::dio_0m9z | 11 | tragend_unruhig | milieu_offen | 0.7298 | 0.0363 | 0.3081 | 0.2955 | 0.1364 | 0.2961 | 0.2181 | 0.2732 | 0.2125 | 0.0094 |
| field_stabil::dio_1lsu | 10 | stabil | milieu_offen | 0.7407 | 0.0459 | 0.2222 | 0.2250 | 0.0875 | 0.2904 | 0.2172 | 0.2755 | 0.2169 | 0.0023 |
| field_stabil::dio_0fe7 | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7472 | 0.0452 | 0.9111 | 0.8833 | 0.8250 | 0.2920 | 0.2178 | 0.2745 | 0.2157 | 0.0077 |
| field_tragend_unruhig::dio_05yg | 10 | tragend_unruhig | milieu_offen | 0.7171 | 0.0406 | 0.1944 | 0.2167 | 0.0625 | 0.2912 | 0.2185 | 0.2749 | 0.2154 | 0.0087 |
| field_stabil::dio_0nlj | 9 | stabil | milieu_rolle_und_pfad_getragen | 0.7707 | 0.0482 | 0.6914 | 0.7037 | 0.5556 | 0.2942 | 0.2174 | 0.2733 | 0.2152 | 0.0069 |
| field_stabil::dio_0kx9 | 9 | stabil | milieu_rolle_und_pfad_getragen | 0.7639 | 0.0474 | 0.6235 | 0.5926 | 0.5139 | 0.2924 | 0.2178 | 0.2742 | 0.2156 | 0.0099 |
| field_tragend_unruhig::dio_04uf | 9 | tragend_unruhig | milieu_offen | 0.7226 | 0.0406 | 0.2840 | 0.2500 | 0.2083 | 0.2945 | 0.2179 | 0.2741 | 0.2135 | 0.0076 |
| field_stabil::dio_1jc2 | 8 | stabil | milieu_offen | 0.7661 | 0.0495 | 0.2917 | 0.3125 | 0.1250 | 0.2891 | 0.2171 | 0.2755 | 0.2183 | 0.0020 |
| field_stabil::dio_09bn | 8 | stabil | milieu_offen | 0.7613 | 0.0479 | 0.5208 | 0.5104 | 0.3750 | 0.2919 | 0.2179 | 0.2736 | 0.2166 | 0.0055 |
| field_stabil::dio_1u5i | 8 | stabil | milieu_offen | 0.7495 | 0.0451 | 0.5278 | 0.5417 | 0.3750 | 0.2944 | 0.2178 | 0.2740 | 0.2137 | 0.0074 |
| field_tragend_unruhig::dio_0u1o | 8 | tragend_unruhig | milieu_offen | 0.7090 | 0.0417 | 0.2708 | 0.3125 | 0.0000 | 0.2923 | 0.2188 | 0.2746 | 0.2143 | 0.0081 |
| field_tragend_unruhig::dio_0jkk | 8 | tragend_unruhig | milieu_offen | 0.7025 | 0.0398 | 0.3750 | 0.4375 | 0.2500 | 0.2937 | 0.2193 | 0.2755 | 0.2114 | 0.0076 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
