# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:12:58

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_long\paxg\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `56`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0136 |
| alignment | 0.0038 |
| strain_relief | 0.0095 |
| sensory | 0.0091 |
| role_experience | 0.8643 |
| path_experience | 0.5250 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 283 | stabil | milieu_rollennah | 0.7632 | 0.0357 | 0.8818 | 0.9202 | 0.0327 | 0.2970 | 0.2177 | 0.2708 | 0.2146 | 0.0126 |
| field_stabil::dio_14wj | 240 | stabil | milieu_rollennah | 0.7793 | 0.0370 | 0.7891 | 0.8472 | 0.0073 | 0.2954 | 0.2181 | 0.2707 | 0.2158 | 0.0111 |
| field_stabil::dio_155c | 164 | stabil | milieu_rollennah | 0.7574 | 0.0366 | 0.5600 | 0.7663 | 0.0694 | 0.2977 | 0.2184 | 0.2696 | 0.2143 | 0.0135 |
| field_stabil::dio_0l7p | 156 | stabil | milieu_offen | 0.7681 | 0.0374 | 0.3672 | 0.5337 | 0.0288 | 0.2965 | 0.2175 | 0.2712 | 0.2148 | 0.0119 |
| field_stabil::dio_0m9z | 126 | stabil | milieu_offen | 0.7507 | 0.0355 | 0.3624 | 0.3988 | 0.1746 | 0.2969 | 0.2183 | 0.2704 | 0.2144 | 0.0115 |
| field_stabil::dio_0h9h | 118 | stabil | milieu_rollennah | 0.7637 | 0.0376 | 0.6304 | 0.7338 | 0.0085 | 0.2978 | 0.2178 | 0.2705 | 0.2140 | 0.1330 |
| field_stabil::dio_1fll | 99 | stabil | milieu_offen | 0.7940 | 0.0403 | 0.3620 | 0.4790 | 0.1237 | 0.2964 | 0.2174 | 0.2709 | 0.2153 | 0.0110 |
| field_stabil::dio_1u5i | 92 | stabil | milieu_offen | 0.7669 | 0.0376 | 0.2083 | 0.2690 | 0.0870 | 0.2967 | 0.2172 | 0.2719 | 0.2142 | 0.0101 |
| field_stabil::dio_00ly | 89 | stabil | milieu_offen | 0.7640 | 0.0386 | 0.3664 | 0.5187 | 0.0534 | 0.2978 | 0.2175 | 0.2709 | 0.2138 | 0.0133 |
| field_stabil::dio_06er | 84 | stabil | milieu_rolle_und_pfad_getragen | 0.7848 | 0.0404 | 0.6792 | 0.6696 | 0.4301 | 0.2966 | 0.2182 | 0.2704 | 0.2148 | 0.0131 |
| field_stabil::dio_1lsu | 70 | stabil | milieu_offen | 0.7566 | 0.0386 | 0.2746 | 0.3393 | 0.0714 | 0.2966 | 0.2180 | 0.2709 | 0.2145 | 0.0136 |
| field_stabil::dio_0z9t | 67 | stabil | milieu_offen | 0.7603 | 0.0395 | 0.3242 | 0.3930 | 0.0578 | 0.2954 | 0.2176 | 0.2707 | 0.2162 | 0.0119 |
| field_stabil::dio_0g2r | 57 | stabil | milieu_offen | 0.7507 | 0.0376 | 0.2096 | 0.2588 | 0.0877 | 0.2968 | 0.2177 | 0.2725 | 0.2130 | 0.0115 |
| field_stabil::dio_1gp2 | 55 | stabil | milieu_offen | 0.7500 | 0.0374 | 0.1980 | 0.2348 | 0.0932 | 0.2975 | 0.2188 | 0.2709 | 0.2128 | 0.0104 |
| field_stabil::dio_1kpz | 53 | stabil | milieu_offen | 0.7700 | 0.0406 | 0.5514 | 0.5896 | 0.3467 | 0.2966 | 0.2174 | 0.2718 | 0.2141 | 0.0106 |
| field_stabil::dio_06s7 | 53 | stabil | milieu_offen | 0.7695 | 0.0405 | 0.2117 | 0.2799 | 0.0755 | 0.2962 | 0.2172 | 0.2720 | 0.2146 | 0.0111 |
| field_stabil::dio_0dd2 | 51 | stabil | milieu_offen | 0.7716 | 0.0415 | 0.3715 | 0.4085 | 0.2868 | 0.2950 | 0.2178 | 0.2718 | 0.2154 | 0.0098 |
| field_stabil::dio_1ewh | 50 | stabil | milieu_offen | 0.7492 | 0.0380 | 0.1411 | 0.1783 | 0.0575 | 0.2973 | 0.2173 | 0.2718 | 0.2137 | 0.0126 |
| field_stabil::dio_1jc2 | 49 | stabil | milieu_offen | 0.7763 | 0.0417 | 0.2336 | 0.2891 | 0.1020 | 0.2953 | 0.2168 | 0.2729 | 0.2150 | 0.0093 |
| field_stabil::dio_0obq | 48 | stabil | milieu_offen | 0.7471 | 0.0400 | 0.1447 | 0.2101 | 0.0052 | 0.2949 | 0.2178 | 0.2717 | 0.2157 | 0.0126 |
| field_stabil::dio_0oc3 | 48 | stabil | milieu_rolle_und_pfad_getragen | 0.7378 | 0.0376 | 0.7292 | 0.7396 | 0.3542 | 0.2977 | 0.2182 | 0.2706 | 0.2134 | 0.0098 |
| field_tragend_unruhig::dio_0m9z | 48 | tragend_unruhig | milieu_offen | 0.7386 | 0.0334 | 0.3681 | 0.1441 | 0.1797 | 0.2975 | 0.2183 | 0.2702 | 0.2140 | 0.0087 |
| field_tragend_unruhig::dio_00ja | 47 | tragend_unruhig | milieu_offen | 0.7343 | 0.0341 | 0.1927 | 0.1365 | 0.0691 | 0.2975 | 0.2183 | 0.2721 | 0.2122 | 0.0145 |
| field_stabil::dio_07o8 | 43 | stabil | milieu_rolle_und_pfad_getragen | 0.7535 | 0.0407 | 0.9380 | 0.9225 | 0.5058 | 0.2955 | 0.2180 | 0.2715 | 0.2150 | 0.0111 |
| field_stabil::dio_0pz6 | 35 | stabil | milieu_offen | 0.7695 | 0.0431 | 0.3333 | 0.3571 | 0.2286 | 0.2929 | 0.2169 | 0.2726 | 0.2176 | 0.0061 |
| field_stabil::dio_1o4z | 35 | stabil | milieu_offen | 0.7530 | 0.0385 | 0.4222 | 0.4357 | 0.2000 | 0.2969 | 0.2177 | 0.2717 | 0.2136 | 0.0117 |
| field_stabil::dio_1uof | 35 | stabil | milieu_offen | 0.7512 | 0.0381 | 0.3381 | 0.3262 | 0.2786 | 0.2955 | 0.2186 | 0.2723 | 0.2137 | 0.0113 |
| field_stabil::dio_00ja | 35 | stabil | milieu_offen | 0.7468 | 0.0361 | 0.2111 | 0.1357 | 0.2429 | 0.2966 | 0.2182 | 0.2726 | 0.2126 | 0.0111 |
| field_stabil::dio_0jqc | 34 | stabil | milieu_rollennah | 0.7696 | 0.0437 | 0.7026 | 0.6912 | 0.2647 | 0.2946 | 0.2176 | 0.2716 | 0.2163 | 0.0111 |
| field_stabil::dio_0kx9 | 34 | stabil | milieu_offen | 0.7739 | 0.0421 | 0.4739 | 0.4902 | 0.4044 | 0.2970 | 0.2173 | 0.2722 | 0.2134 | 0.0069 |
| field_stabil::dio_1q85 | 34 | stabil | milieu_offen | 0.7514 | 0.0400 | 0.3170 | 0.2574 | 0.2022 | 0.2938 | 0.2198 | 0.2710 | 0.2154 | 0.0120 |
| field_tragend_unruhig::dio_05yg | 34 | tragend_unruhig | milieu_offen | 0.7283 | 0.0366 | 0.7435 | 0.3211 | 0.1176 | 0.2959 | 0.2186 | 0.2716 | 0.2139 | 0.0103 |
| field_tragend_unruhig::dio_0jkk | 34 | tragend_unruhig | milieu_offen | 0.7198 | 0.0358 | 0.8611 | 0.3162 | 0.2353 | 0.2958 | 0.2183 | 0.2715 | 0.2145 | 0.0107 |
| field_stabil::dio_1492 | 33 | stabil | milieu_rollennah | 0.7757 | 0.0430 | 1.0000 | 1.0000 | 0.5265 | 0.2964 | 0.2179 | 0.2712 | 0.2144 | 0.0095 |
| field_stabil::dio_0v65 | 30 | stabil | milieu_offen | 0.7595 | 0.0406 | 0.2241 | 0.2528 | 0.1333 | 0.2962 | 0.2170 | 0.2734 | 0.2134 | 0.0092 |
| field_stabil::dio_0fe7 | 29 | stabil | milieu_rolle_und_pfad_getragen | 0.7572 | 0.0417 | 0.9004 | 0.8937 | 0.5302 | 0.2955 | 0.2180 | 0.2718 | 0.2148 | 0.0109 |
| field_stabil::dio_0f8s | 27 | stabil | milieu_rolle_und_pfad_getragen | 0.7474 | 0.0413 | 0.6564 | 0.6636 | 0.4074 | 0.2967 | 0.2179 | 0.2706 | 0.2148 | 0.0105 |
| field_stabil::dio_1xrt | 27 | stabil | milieu_rolle_und_pfad_getragen | 0.7550 | 0.0412 | 0.6687 | 0.6636 | 0.4259 | 0.2961 | 0.2177 | 0.2717 | 0.2145 | 0.0109 |
| field_stabil::dio_1pij | 27 | stabil | milieu_rolle_und_pfad_getragen | 0.7395 | 0.0394 | 0.7613 | 0.7623 | 0.3611 | 0.2967 | 0.2181 | 0.2708 | 0.2144 | 0.0110 |
| field_stabil::dio_1oye | 27 | stabil | milieu_rolle_und_pfad_getragen | 0.7352 | 0.0393 | 0.8951 | 0.8920 | 0.3750 | 0.2965 | 0.2180 | 0.2712 | 0.2143 | 0.0105 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
