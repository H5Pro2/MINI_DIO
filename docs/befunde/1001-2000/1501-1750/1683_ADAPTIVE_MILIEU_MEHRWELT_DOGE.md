# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:00:32

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_worlds\doge\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `26`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0127 |
| alignment | 0.0025 |
| strain_relief | 0.0074 |
| sensory | 0.0081 |
| role_experience | 0.7917 |
| path_experience | 0.9250 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 61 | stabil | milieu_rollennah | 0.7514 | 0.0365 | 0.3752 | 0.5328 | 0.0246 | 0.2973 | 0.2180 | 0.2712 | 0.2136 | 0.1321 |
| field_stabil::dio_0m9z | 35 | stabil | milieu_pfadnah | 0.7425 | 0.0370 | 0.3508 | 0.2024 | 0.4143 | 0.2947 | 0.2187 | 0.2726 | 0.2140 | 0.0104 |
| field_stabil::dio_155c | 34 | stabil | milieu_offen | 0.7424 | 0.0359 | 0.4461 | 0.4730 | 0.1875 | 0.3037 | 0.2189 | 0.2679 | 0.2095 | 0.1257 |
| field_stabil::dio_0h9h | 32 | stabil | milieu_offen | 0.7547 | 0.0385 | 0.2552 | 0.3828 | 0.0000 | 0.2993 | 0.2183 | 0.2694 | 0.2129 | 0.1332 |
| field_stabil::dio_0l7p | 26 | stabil | milieu_offen | 0.7564 | 0.0393 | 0.2756 | 0.2788 | 0.2019 | 0.2978 | 0.2181 | 0.2707 | 0.2134 | 0.1321 |
| field_stabil::dio_0pz6 | 16 | stabil | milieu_rolle_und_pfad_getragen | 0.7622 | 0.0452 | 0.6424 | 0.6406 | 0.6172 | 0.2931 | 0.2176 | 0.2735 | 0.2158 | 0.0066 |
| field_stabil::dio_00ly | 16 | stabil | milieu_offen | 0.7572 | 0.0442 | 0.2500 | 0.2344 | 0.1406 | 0.2925 | 0.2169 | 0.2739 | 0.2167 | 0.0096 |
| field_tragend_unruhig::dio_00ja | 16 | tragend_unruhig | milieu_offen | 0.7287 | 0.0373 | 0.3854 | 0.4844 | 0.0312 | 0.2950 | 0.2184 | 0.2750 | 0.2117 | 0.0137 |
| field_stabil::dio_09bn | 15 | stabil | milieu_offen | 0.7607 | 0.0449 | 0.3630 | 0.3222 | 0.2000 | 0.2936 | 0.2171 | 0.2728 | 0.2165 | 0.0076 |
| field_tragend_unruhig::dio_0m9z | 14 | tragend_unruhig | milieu_offen | 0.7311 | 0.0362 | 0.4286 | 0.3869 | 0.1161 | 0.2953 | 0.2187 | 0.2724 | 0.2136 | 0.0118 |
| field_stabil::dio_1ewh | 13 | stabil | milieu_offen | 0.7396 | 0.0430 | 0.3632 | 0.4167 | 0.1538 | 0.2917 | 0.2173 | 0.2742 | 0.2167 | 0.0072 |
| field_stabil::dio_1kpz | 12 | stabil | milieu_offen | 0.7600 | 0.0460 | 0.3935 | 0.4028 | 0.2500 | 0.2921 | 0.2167 | 0.2737 | 0.2176 | 0.0042 |
| field_stabil::dio_17ct | 12 | stabil | milieu_offen | 0.7487 | 0.0446 | 0.4769 | 0.4861 | 0.3542 | 0.2932 | 0.2175 | 0.2733 | 0.2159 | 0.0077 |
| field_stabil::dio_0oc3 | 12 | stabil | milieu_offen | 0.7294 | 0.0428 | 0.2037 | 0.1250 | 0.2083 | 0.2936 | 0.2185 | 0.2739 | 0.2140 | 0.0091 |
| field_stabil::dio_0g2r | 11 | stabil | milieu_offen | 0.7384 | 0.0439 | 0.1162 | 0.1364 | 0.0227 | 0.2911 | 0.2180 | 0.2751 | 0.2158 | 0.0109 |
| field_tragend_unruhig::dio_0jkk | 11 | tragend_unruhig | milieu_offen | 0.7145 | 0.0397 | 0.1869 | 0.2348 | 0.0000 | 0.2937 | 0.2191 | 0.2748 | 0.2125 | 0.0102 |
| field_stabil::dio_14wj | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7565 | 0.0459 | 0.9278 | 0.9167 | 0.9250 | 0.2919 | 0.2180 | 0.2743 | 0.2158 | 0.0077 |
| field_stabil::dio_1cic | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7481 | 0.0447 | 0.8111 | 0.8167 | 0.7000 | 0.2933 | 0.2177 | 0.2742 | 0.2149 | 0.0056 |
| field_tragend_unruhig::dio_05yg | 10 | tragend_unruhig | milieu_offen | 0.7102 | 0.0398 | 0.4222 | 0.4667 | 0.1000 | 0.2937 | 0.2188 | 0.2748 | 0.2127 | 0.0101 |
| field_tragend_unruhig::dio_1v2w | 10 | tragend_unruhig | milieu_offen | 0.7096 | 0.0377 | 0.2722 | 0.3083 | 0.0500 | 0.2960 | 0.2191 | 0.2753 | 0.2095 | 0.0091 |
| field_stabil::dio_06s7 | 9 | stabil | milieu_rolle_und_pfad_getragen | 0.7606 | 0.0470 | 0.7901 | 0.7963 | 0.6667 | 0.2926 | 0.2177 | 0.2739 | 0.2157 | 0.0050 |
| field_stabil::dio_07uk | 8 | stabil | milieu_offen | 0.7588 | 0.0495 | 0.5486 | 0.5521 | 0.3750 | 0.2913 | 0.2173 | 0.2740 | 0.2174 | 0.0051 |
| field_stabil::dio_1lsu | 8 | stabil | milieu_offen | 0.7420 | 0.0465 | 0.3403 | 0.3542 | 0.1562 | 0.2911 | 0.2175 | 0.2751 | 0.2162 | 0.0050 |
| field_stabil::dio_0fe7 | 8 | stabil | milieu_offen | 0.7436 | 0.0458 | 0.2917 | 0.3125 | 0.1250 | 0.2921 | 0.2170 | 0.2739 | 0.2169 | 0.0036 |
| field_stabil::dio_1u5i | 8 | stabil | milieu_offen | 0.7504 | 0.0455 | 0.4306 | 0.4583 | 0.3750 | 0.2925 | 0.2172 | 0.2743 | 0.2160 | 0.0018 |
| field_stabil::dio_1gp2 | 8 | stabil | milieu_offen | 0.7341 | 0.0442 | 0.3611 | 0.3646 | 0.2031 | 0.2914 | 0.2176 | 0.2745 | 0.2165 | 0.0083 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
