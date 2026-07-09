# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:12:59

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_long\xrp\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_innerhalb_der_gruppen_noch_flach`
- Gruppen: `56`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0041 |
| alignment | 0.0017 |
| strain_relief | 0.0036 |
| sensory | 0.0053 |
| role_experience | 0.9134 |
| path_experience | 0.4545 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 163 | stabil | milieu_rollennah | 0.7540 | 0.0358 | 0.6936 | 0.7761 | 0.0560 | 0.2979 | 0.2171 | 0.2714 | 0.2136 | 0.0125 |
| field_stabil::dio_155c | 116 | stabil | milieu_rollennah | 0.7497 | 0.0369 | 0.4564 | 0.6588 | 0.0172 | 0.2973 | 0.2170 | 0.2715 | 0.2142 | 0.0161 |
| field_stabil::dio_0h9h | 110 | stabil | milieu_rollennah | 0.7600 | 0.0379 | 0.5323 | 0.7682 | 0.0182 | 0.2979 | 0.2169 | 0.2717 | 0.2135 | 0.0108 |
| field_stabil::dio_0m9z | 109 | stabil | milieu_rollennah | 0.7445 | 0.0352 | 0.5000 | 0.6391 | 0.1101 | 0.2975 | 0.2172 | 0.2714 | 0.2139 | 0.0137 |
| field_stabil::dio_0g2r | 79 | stabil | milieu_rollennah | 0.7479 | 0.0366 | 0.3994 | 0.5675 | 0.0633 | 0.2974 | 0.2171 | 0.2725 | 0.2130 | 0.0111 |
| field_stabil::dio_0l7p | 78 | stabil | milieu_offen | 0.7609 | 0.0383 | 0.2521 | 0.3462 | 0.0609 | 0.2966 | 0.2170 | 0.2723 | 0.2141 | 0.0119 |
| field_stabil::dio_1gp2 | 77 | stabil | milieu_offen | 0.7487 | 0.0363 | 0.3312 | 0.4318 | 0.0779 | 0.2981 | 0.2174 | 0.2726 | 0.2118 | 0.0145 |
| field_tragend_unruhig::dio_00ja | 75 | tragend_unruhig | milieu_offen | 0.7323 | 0.0338 | 0.3689 | 0.1111 | 0.1417 | 0.2973 | 0.2176 | 0.2728 | 0.2124 | 0.0173 |
| field_stabil::dio_00ly | 67 | stabil | milieu_offen | 0.7599 | 0.0396 | 0.3217 | 0.4204 | 0.1082 | 0.2956 | 0.2166 | 0.2727 | 0.2151 | 0.0122 |
| field_stabil::dio_1kpz | 61 | stabil | milieu_offen | 0.7682 | 0.0403 | 0.4007 | 0.5355 | 0.1148 | 0.2964 | 0.2168 | 0.2726 | 0.2142 | 0.0095 |
| field_tragend_unruhig::dio_0jkk | 59 | tragend_unruhig | milieu_offen | 0.7198 | 0.0341 | 0.9284 | 0.3489 | 0.2712 | 0.2963 | 0.2172 | 0.2727 | 0.2137 | 0.0092 |
| field_stabil::dio_06s7 | 56 | stabil | milieu_offen | 0.7684 | 0.0404 | 0.2450 | 0.3586 | 0.0022 | 0.2970 | 0.2169 | 0.2723 | 0.2138 | 0.0108 |
| field_stabil::dio_1ewh | 55 | stabil | milieu_offen | 0.7460 | 0.0380 | 0.2465 | 0.3045 | 0.0568 | 0.2965 | 0.2169 | 0.2725 | 0.2141 | 0.0137 |
| field_tragend_unruhig::dio_0m9z | 51 | tragend_unruhig | milieu_offen | 0.7342 | 0.0332 | 0.4924 | 0.0866 | 0.1765 | 0.2978 | 0.2172 | 0.2713 | 0.2138 | 0.0136 |
| field_tragend_unruhig::dio_1v2w | 46 | tragend_unruhig | milieu_offen | 0.7166 | 0.0335 | 0.8986 | 0.2772 | 0.2908 | 0.2965 | 0.2173 | 0.2728 | 0.2134 | 0.0099 |
| field_stabil::dio_14wj | 43 | stabil | milieu_offen | 0.7645 | 0.0403 | 0.5336 | 0.5562 | 0.3634 | 0.2958 | 0.2169 | 0.2731 | 0.2142 | 0.0078 |
| field_stabil::dio_17ct | 42 | stabil | milieu_offen | 0.7512 | 0.0401 | 0.2077 | 0.2520 | 0.0238 | 0.2960 | 0.2166 | 0.2719 | 0.2155 | 0.0119 |
| field_tragend_unruhig::dio_05yg | 42 | tragend_unruhig | milieu_offen | 0.7194 | 0.0356 | 0.7632 | 0.2381 | 0.1905 | 0.2959 | 0.2174 | 0.2728 | 0.2138 | 0.0116 |
| field_stabil::dio_0nlj | 40 | stabil | milieu_offen | 0.7754 | 0.0433 | 0.3056 | 0.4042 | 0.0813 | 0.2943 | 0.2159 | 0.2727 | 0.2171 | 0.0093 |
| field_stabil::dio_0pz6 | 39 | stabil | milieu_offen | 0.7635 | 0.0407 | 0.1595 | 0.2073 | 0.0160 | 0.2972 | 0.2171 | 0.2706 | 0.2151 | 0.1325 |
| field_stabil::dio_09bn | 37 | stabil | milieu_offen | 0.7642 | 0.0424 | 0.2312 | 0.2725 | 0.0676 | 0.2953 | 0.2165 | 0.2724 | 0.2158 | 0.0118 |
| field_stabil::dio_1lsu | 37 | stabil | milieu_offen | 0.7441 | 0.0396 | 0.4474 | 0.4685 | 0.2061 | 0.2966 | 0.2171 | 0.2721 | 0.2143 | 0.0099 |
| field_stabil::dio_1o4z | 37 | stabil | milieu_offen | 0.7490 | 0.0387 | 0.4264 | 0.4572 | 0.1216 | 0.2962 | 0.2171 | 0.2728 | 0.2140 | 0.0105 |
| field_stabil::dio_1jc2 | 35 | stabil | milieu_offen | 0.7727 | 0.0431 | 0.3730 | 0.5024 | 0.0786 | 0.2949 | 0.2168 | 0.2725 | 0.2158 | 0.0081 |
| field_stabil::dio_0obq | 34 | stabil | milieu_offen | 0.7403 | 0.0403 | 0.4755 | 0.5049 | 0.2243 | 0.2956 | 0.2173 | 0.2721 | 0.2150 | 0.0091 |
| field_stabil::dio_18kx | 33 | stabil | milieu_offen | 0.7629 | 0.0426 | 0.3098 | 0.4343 | 0.0303 | 0.2950 | 0.2163 | 0.2729 | 0.2159 | 0.0067 |
| field_stabil::dio_1oc2 | 32 | stabil | milieu_offen | 0.7477 | 0.0404 | 0.3906 | 0.4297 | 0.0039 | 0.2964 | 0.2168 | 0.2724 | 0.2144 | 0.0068 |
| field_stabil::dio_1u5i | 32 | stabil | milieu_offen | 0.7568 | 0.0403 | 0.4288 | 0.4557 | 0.1641 | 0.2975 | 0.2170 | 0.2725 | 0.2130 | 0.0100 |
| field_stabil::dio_0oc3 | 32 | stabil | milieu_offen | 0.7322 | 0.0396 | 0.3628 | 0.3880 | 0.2383 | 0.2958 | 0.2171 | 0.2725 | 0.2146 | 0.0098 |
| field_tragend_unruhig::dio_19pg | 31 | tragend_unruhig | milieu_offen | 0.7323 | 0.0369 | 0.5699 | 0.1263 | 0.1169 | 0.2968 | 0.2174 | 0.2726 | 0.2133 | 0.0126 |
| field_stabil::dio_1q85 | 30 | stabil | milieu_offen | 0.7434 | 0.0392 | 0.4852 | 0.5111 | 0.2417 | 0.2955 | 0.2168 | 0.2724 | 0.2153 | 0.0078 |
| field_tragend_unruhig::dio_0klp | 30 | tragend_unruhig | milieu_offen | 0.6992 | 0.0333 | 1.0000 | 0.2806 | 0.4042 | 0.2963 | 0.2170 | 0.2725 | 0.2142 | 0.0086 |
| field_stabil::dio_0kx9 | 29 | stabil | milieu_offen | 0.7734 | 0.0439 | 0.2644 | 0.3103 | 0.1379 | 0.2943 | 0.2161 | 0.2735 | 0.2160 | 0.0052 |
| field_stabil::dio_0om4 | 29 | stabil | milieu_offen | 0.7613 | 0.0428 | 0.2490 | 0.2874 | 0.0129 | 0.2951 | 0.2165 | 0.2728 | 0.2157 | 0.0075 |
| field_stabil::dio_0ein | 29 | stabil | milieu_offen | 0.7573 | 0.0414 | 0.1877 | 0.2644 | 0.0000 | 0.2950 | 0.2166 | 0.2741 | 0.2143 | 0.0036 |
| field_stabil::dio_0v65 | 29 | stabil | milieu_offen | 0.7557 | 0.0408 | 0.4100 | 0.4569 | 0.2414 | 0.2961 | 0.2173 | 0.2728 | 0.2138 | 0.0092 |
| field_tragend_unruhig::dio_0cky | 29 | tragend_unruhig | milieu_offen | 0.6984 | 0.0345 | 0.9368 | 0.4483 | 0.3103 | 0.2961 | 0.2174 | 0.2729 | 0.2137 | 0.0078 |
| field_tragend_unruhig::dio_13it | 29 | tragend_unruhig | milieu_rollennah | 0.6954 | 0.0313 | 1.0000 | 0.3966 | 0.3103 | 0.2967 | 0.2170 | 0.2725 | 0.2138 | 0.0038 |
| field_stabil::dio_04uf | 26 | stabil | milieu_offen | 0.7400 | 0.0376 | 0.2906 | 0.2853 | 0.0529 | 0.2969 | 0.2174 | 0.2729 | 0.2129 | 0.0051 |
| field_stabil::dio_00pl | 25 | stabil | milieu_offen | 0.7519 | 0.0413 | 0.2067 | 0.2500 | 0.0000 | 0.2953 | 0.2170 | 0.2742 | 0.2135 | 0.0102 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
