# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:00:32

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_worlds\paxg\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `66`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0363 |
| alignment | 0.0068 |
| strain_relief | 0.0226 |
| sensory | 0.0232 |
| role_experience | 0.9167 |
| path_experience | 1.0000 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 125 | stabil | milieu_rollennah | 0.7631 | 0.0372 | 0.7516 | 0.8193 | 0.0500 | 0.2946 | 0.2175 | 0.2722 | 0.2157 | 0.0098 |
| field_stabil::dio_14wj | 102 | stabil | milieu_rollennah | 0.7776 | 0.0388 | 0.5038 | 0.6405 | 0.0172 | 0.2927 | 0.2183 | 0.2718 | 0.2172 | 0.0099 |
| field_stabil::dio_155c | 63 | stabil | milieu_offen | 0.7552 | 0.0384 | 0.4700 | 0.5675 | 0.1806 | 0.2964 | 0.2180 | 0.2713 | 0.2144 | 0.0135 |
| field_stabil::dio_0l7p | 62 | stabil | milieu_offen | 0.7677 | 0.0398 | 0.2616 | 0.3495 | 0.0726 | 0.2931 | 0.2176 | 0.2726 | 0.2166 | 0.0106 |
| field_stabil::dio_0m9z | 55 | stabil | milieu_offen | 0.7510 | 0.0371 | 0.4465 | 0.3545 | 0.3795 | 0.2962 | 0.2189 | 0.2709 | 0.2140 | 0.0113 |
| field_stabil::dio_0h9h | 52 | stabil | milieu_offen | 0.7628 | 0.0391 | 0.2938 | 0.4215 | 0.0192 | 0.2965 | 0.2181 | 0.2711 | 0.2142 | 0.1330 |
| field_stabil::dio_1lsu | 37 | stabil | milieu_offen | 0.7535 | 0.0406 | 0.2793 | 0.3626 | 0.0777 | 0.2941 | 0.2174 | 0.2727 | 0.2158 | 0.0096 |
| field_stabil::dio_1u5i | 37 | stabil | milieu_offen | 0.7636 | 0.0403 | 0.3393 | 0.4009 | 0.2162 | 0.2947 | 0.2175 | 0.2728 | 0.2149 | 0.0078 |
| field_stabil::dio_06er | 34 | stabil | milieu_rolle_und_pfad_getragen | 0.7801 | 0.0432 | 0.9248 | 0.8775 | 0.8713 | 0.2933 | 0.2183 | 0.2729 | 0.2156 | 0.0098 |
| field_stabil::dio_0z9t | 34 | stabil | milieu_offen | 0.7576 | 0.0412 | 0.2647 | 0.3603 | 0.0331 | 0.2933 | 0.2176 | 0.2718 | 0.2174 | 0.0100 |
| field_stabil::dio_00ly | 32 | stabil | milieu_offen | 0.7620 | 0.0414 | 0.3281 | 0.4062 | 0.1484 | 0.2947 | 0.2178 | 0.2722 | 0.2153 | 0.0100 |
| field_stabil::dio_1fll | 27 | stabil | milieu_offen | 0.7878 | 0.0445 | 0.4959 | 0.5093 | 0.4537 | 0.2937 | 0.2179 | 0.2724 | 0.2160 | 0.0084 |
| field_stabil::dio_0dd2 | 25 | stabil | milieu_rolle_und_pfad_getragen | 0.7694 | 0.0436 | 0.6044 | 0.6033 | 0.5850 | 0.2932 | 0.2179 | 0.2731 | 0.2158 | 0.0090 |
| field_stabil::dio_06s7 | 24 | stabil | milieu_offen | 0.7655 | 0.0429 | 0.2593 | 0.3056 | 0.1667 | 0.2936 | 0.2176 | 0.2734 | 0.2154 | 0.0081 |
| field_stabil::dio_0obq | 23 | stabil | milieu_offen | 0.7457 | 0.0425 | 0.1715 | 0.2428 | 0.0109 | 0.2918 | 0.2176 | 0.2733 | 0.2173 | 0.0095 |
| field_stabil::dio_0g2r | 22 | stabil | milieu_offen | 0.7498 | 0.0408 | 0.3409 | 0.3674 | 0.2273 | 0.2942 | 0.2179 | 0.2741 | 0.2138 | 0.0104 |
| field_tragend_unruhig::dio_0m9z | 21 | tragend_unruhig | milieu_offen | 0.7419 | 0.0341 | 0.4153 | 0.2937 | 0.2202 | 0.2973 | 0.2188 | 0.2705 | 0.2133 | 0.0085 |
| field_stabil::dio_1ewh | 20 | stabil | milieu_offen | 0.7468 | 0.0412 | 0.2528 | 0.2958 | 0.1437 | 0.2937 | 0.2178 | 0.2738 | 0.2147 | 0.0122 |
| field_stabil::dio_1jc2 | 19 | stabil | milieu_offen | 0.7722 | 0.0447 | 0.3801 | 0.4123 | 0.2632 | 0.2938 | 0.2170 | 0.2736 | 0.2156 | 0.0071 |
| field_stabil::dio_07o8 | 19 | stabil | milieu_rolle_und_pfad_getragen | 0.7530 | 0.0435 | 0.8596 | 0.8246 | 0.7961 | 0.2925 | 0.2183 | 0.2732 | 0.2160 | 0.0095 |
| field_tragend_unruhig::dio_00ja | 19 | tragend_unruhig | milieu_offen | 0.7331 | 0.0365 | 0.3099 | 0.3377 | 0.0789 | 0.2949 | 0.2187 | 0.2738 | 0.2126 | 0.0119 |
| field_stabil::dio_1q85 | 18 | stabil | milieu_offen | 0.7510 | 0.0423 | 0.1790 | 0.0926 | 0.2778 | 0.2913 | 0.2202 | 0.2722 | 0.2163 | 0.0067 |
| field_stabil::dio_1gp2 | 17 | stabil | milieu_offen | 0.7452 | 0.0410 | 0.3922 | 0.3873 | 0.3015 | 0.2955 | 0.2180 | 0.2732 | 0.2133 | 0.0096 |
| field_stabil::dio_00ja | 17 | stabil | milieu_pfadnah | 0.7451 | 0.0376 | 0.2843 | 0.0833 | 0.5000 | 0.2953 | 0.2186 | 0.2738 | 0.2123 | 0.0084 |
| field_stabil::dio_0kx9 | 16 | stabil | milieu_rolle_und_pfad_getragen | 0.7713 | 0.0444 | 0.9410 | 0.9427 | 0.8594 | 0.2958 | 0.2181 | 0.2719 | 0.2142 | 0.0067 |
| field_stabil::dio_0pz6 | 15 | stabil | milieu_rolle_und_pfad_getragen | 0.7658 | 0.0454 | 0.6889 | 0.7000 | 0.5333 | 0.2926 | 0.2177 | 0.2732 | 0.2165 | 0.0047 |
| field_stabil::dio_1kpz | 15 | stabil | milieu_rolle_und_pfad_getragen | 0.7682 | 0.0450 | 1.0000 | 0.9944 | 0.9167 | 0.2932 | 0.2182 | 0.2732 | 0.2154 | 0.0086 |
| field_stabil::dio_0fe7 | 15 | stabil | milieu_rolle_und_pfad_getragen | 0.7553 | 0.0439 | 0.9333 | 0.9167 | 0.8167 | 0.2939 | 0.2182 | 0.2726 | 0.2153 | 0.0096 |
| field_stabil::dio_1uof | 15 | stabil | milieu_offen | 0.7445 | 0.0410 | 0.5741 | 0.5500 | 0.5167 | 0.2935 | 0.2182 | 0.2734 | 0.2148 | 0.0106 |
| field_stabil::dio_0oc3 | 15 | stabil | milieu_rolle_und_pfad_getragen | 0.7298 | 0.0405 | 1.0000 | 1.0000 | 0.8333 | 0.2952 | 0.2181 | 0.2721 | 0.2146 | 0.0060 |
| field_stabil::dio_10dv | 14 | stabil | milieu_offen | 0.7661 | 0.0478 | 0.1706 | 0.1845 | 0.1071 | 0.2896 | 0.2177 | 0.2732 | 0.2195 | 0.0080 |
| field_stabil::dio_0jqc | 14 | stabil | milieu_offen | 0.7617 | 0.0472 | 0.2778 | 0.2500 | 0.2500 | 0.2900 | 0.2172 | 0.2735 | 0.2193 | 0.0044 |
| field_stabil::dio_18po | 13 | stabil | milieu_rolle_und_pfad_getragen | 0.7298 | 0.0437 | 0.6239 | 0.6218 | 0.4519 | 0.2940 | 0.2182 | 0.2726 | 0.2153 | 0.0111 |
| field_stabil::dio_1pij | 13 | stabil | milieu_offen | 0.7392 | 0.0420 | 0.5043 | 0.5064 | 0.4135 | 0.2955 | 0.2183 | 0.2715 | 0.2146 | 0.0104 |
| field_tragend_unruhig::dio_05yg | 13 | tragend_unruhig | milieu_offen | 0.7216 | 0.0397 | 0.4744 | 0.4808 | 0.0000 | 0.2934 | 0.2191 | 0.2738 | 0.2137 | 0.0088 |
| field_stabil::dio_1350 | 12 | stabil | milieu_rolle_und_pfad_getragen | 0.7660 | 0.0456 | 0.9907 | 0.9722 | 0.9688 | 0.2937 | 0.2183 | 0.2727 | 0.2153 | 0.0098 |
| field_tragend_unruhig::dio_0cky | 12 | tragend_unruhig | milieu_offen | 0.7003 | 0.0379 | 0.5648 | 0.3958 | 0.0833 | 0.2941 | 0.2197 | 0.2728 | 0.2133 | 0.0116 |
| field_stabil::dio_1492 | 11 | stabil | milieu_rolle_und_pfad_getragen | 0.7706 | 0.0471 | 1.0000 | 1.0000 | 1.0000 | 0.2946 | 0.2182 | 0.2726 | 0.2147 | 0.0088 |
| field_stabil::dio_1oye | 11 | stabil | milieu_rolle_und_pfad_getragen | 0.7351 | 0.0430 | 0.8283 | 0.8182 | 0.5568 | 0.2947 | 0.2182 | 0.2725 | 0.2146 | 0.0071 |
| field_stabil::dio_0g3b | 11 | stabil | milieu_offen | 0.7721 | 0.0393 | 0.3030 | 0.3182 | 0.1932 | 0.3147 | 0.2209 | 0.2602 | 0.2041 | 0.1334 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.

## Wie es weitergeht

Als naechstes sollte die adaptive Erfahrung nicht nur aus Durchschnittswerten, sondern aus Rollenmilieu und Zustandspfad gebildet werden. Dann koennen stabile, randnahe, offene und rekoppelnde Lagen eigene Gewichtungsprofile ausbilden.
