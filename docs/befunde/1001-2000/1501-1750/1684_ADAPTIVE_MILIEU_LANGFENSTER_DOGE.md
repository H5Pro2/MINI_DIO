# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:12:58

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_long\doge\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_innerhalb_der_gruppen_noch_flach`
- Gruppen: `58`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0072 |
| alignment | 0.0018 |
| strain_relief | 0.0045 |
| sensory | 0.0061 |
| role_experience | 0.9464 |
| path_experience | 0.4500 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 267 | stabil | milieu_rollennah | 0.7554 | 0.0345 | 0.8483 | 0.8933 | 0.0056 | 0.2987 | 0.2173 | 0.2706 | 0.2133 | 0.1321 |
| field_stabil::dio_155c | 148 | stabil | milieu_rollennah | 0.7489 | 0.0354 | 0.6577 | 0.8440 | 0.0456 | 0.3001 | 0.2175 | 0.2696 | 0.2128 | 0.1257 |
| field_stabil::dio_0h9h | 134 | stabil | milieu_rollennah | 0.7607 | 0.0369 | 0.5925 | 0.8240 | 0.0000 | 0.2992 | 0.2173 | 0.2704 | 0.2131 | 0.1332 |
| field_stabil::dio_0l7p | 122 | stabil | milieu_offen | 0.7619 | 0.0367 | 0.3311 | 0.4679 | 0.0430 | 0.2986 | 0.2173 | 0.2710 | 0.2131 | 0.1321 |
| field_stabil::dio_0m9z | 110 | stabil | milieu_offen | 0.7452 | 0.0350 | 0.3677 | 0.3970 | 0.1795 | 0.2982 | 0.2179 | 0.2710 | 0.2130 | 0.0129 |
| field_tragend_unruhig::dio_00ja | 84 | tragend_unruhig | milieu_offen | 0.7317 | 0.0327 | 0.5992 | 0.2629 | 0.1161 | 0.2990 | 0.2177 | 0.2721 | 0.2111 | 0.0185 |
| field_stabil::dio_00ly | 76 | stabil | milieu_offen | 0.7603 | 0.0389 | 0.2712 | 0.3772 | 0.0296 | 0.2971 | 0.2169 | 0.2719 | 0.2141 | 0.0114 |
| field_stabil::dio_14wj | 71 | stabil | milieu_offen | 0.7664 | 0.0392 | 0.2660 | 0.3110 | 0.1585 | 0.2969 | 0.2168 | 0.2720 | 0.2143 | 0.0108 |
| field_stabil::dio_1ewh | 68 | stabil | milieu_offen | 0.7468 | 0.0372 | 0.3382 | 0.4828 | 0.0294 | 0.2973 | 0.2171 | 0.2723 | 0.2133 | 0.0117 |
| field_stabil::dio_1kpz | 67 | stabil | milieu_offen | 0.7689 | 0.0404 | 0.3217 | 0.4490 | 0.0448 | 0.2960 | 0.2164 | 0.2722 | 0.2154 | 0.0097 |
| field_stabil::dio_06s7 | 66 | stabil | milieu_offen | 0.7692 | 0.0399 | 0.4663 | 0.6174 | 0.0909 | 0.2980 | 0.2169 | 0.2716 | 0.2135 | 0.0092 |
| field_tragend_unruhig::dio_0jkk | 65 | tragend_unruhig | milieu_offen | 0.7213 | 0.0339 | 0.8479 | 0.2154 | 0.2923 | 0.2972 | 0.2173 | 0.2721 | 0.2134 | 0.0106 |
| field_stabil::dio_0g2r | 60 | stabil | milieu_offen | 0.7466 | 0.0369 | 0.2028 | 0.2708 | 0.0063 | 0.2974 | 0.2173 | 0.2726 | 0.2128 | 0.0151 |
| field_stabil::dio_1gp2 | 55 | stabil | milieu_offen | 0.7471 | 0.0370 | 0.1333 | 0.1682 | 0.0386 | 0.2982 | 0.2173 | 0.2722 | 0.2123 | 0.0132 |
| field_stabil::dio_0pz6 | 53 | stabil | milieu_offen | 0.7655 | 0.0412 | 0.4948 | 0.5126 | 0.1863 | 0.2959 | 0.2170 | 0.2720 | 0.2151 | 0.0107 |
| field_stabil::dio_09bn | 52 | stabil | milieu_offen | 0.7674 | 0.0412 | 0.1902 | 0.2212 | 0.0577 | 0.2963 | 0.2166 | 0.2716 | 0.2155 | 0.0107 |
| field_tragend_unruhig::dio_0m9z | 52 | tragend_unruhig | milieu_offen | 0.7328 | 0.0334 | 0.4038 | 0.1554 | 0.1370 | 0.2987 | 0.2178 | 0.2707 | 0.2127 | 0.0138 |
| field_tragend_unruhig::dio_1v2w | 50 | tragend_unruhig | milieu_offen | 0.7168 | 0.0328 | 0.8544 | 0.2033 | 0.4300 | 0.2975 | 0.2173 | 0.2723 | 0.2129 | 0.0094 |
| field_tragend_unruhig::dio_05yg | 49 | tragend_unruhig | milieu_offen | 0.7207 | 0.0348 | 0.8639 | 0.1803 | 0.2449 | 0.2971 | 0.2173 | 0.2722 | 0.2135 | 0.0107 |
| field_stabil::dio_1lsu | 47 | stabil | milieu_offen | 0.7470 | 0.0392 | 0.2045 | 0.2376 | 0.0266 | 0.2965 | 0.2168 | 0.2725 | 0.2142 | 0.0111 |
| field_stabil::dio_0kx9 | 44 | stabil | milieu_offen | 0.7718 | 0.0401 | 0.2790 | 0.3277 | 0.1818 | 0.2999 | 0.2174 | 0.2709 | 0.2118 | 0.1303 |
| field_stabil::dio_0oc3 | 44 | stabil | milieu_offen | 0.7339 | 0.0385 | 0.4015 | 0.3939 | 0.0568 | 0.2971 | 0.2173 | 0.2718 | 0.2138 | 0.0114 |
| field_stabil::dio_1u5i | 43 | stabil | milieu_offen | 0.7591 | 0.0399 | 0.1938 | 0.2558 | 0.0698 | 0.2964 | 0.2168 | 0.2727 | 0.2141 | 0.0077 |
| field_stabil::dio_0om4 | 40 | stabil | milieu_rollennah | 0.7635 | 0.0420 | 0.4847 | 0.6833 | 0.0500 | 0.2947 | 0.2161 | 0.2732 | 0.2160 | 0.0063 |
| field_stabil::dio_1o4z | 40 | stabil | milieu_offen | 0.7487 | 0.0379 | 0.1181 | 0.1646 | 0.0000 | 0.2974 | 0.2168 | 0.2722 | 0.2136 | 0.0090 |
| field_tragend_unruhig::dio_19pg | 40 | tragend_unruhig | milieu_offen | 0.7328 | 0.0362 | 0.5028 | 0.0417 | 0.1812 | 0.2959 | 0.2170 | 0.2728 | 0.2143 | 0.0105 |
| field_stabil::dio_0nlj | 39 | stabil | milieu_offen | 0.7744 | 0.0436 | 0.1695 | 0.2073 | 0.0449 | 0.2941 | 0.2161 | 0.2730 | 0.2169 | 0.0086 |
| field_stabil::dio_1492 | 39 | stabil | milieu_offen | 0.7733 | 0.0424 | 0.3590 | 0.4188 | 0.1282 | 0.2960 | 0.2164 | 0.2718 | 0.2159 | 0.0116 |
| field_stabil::dio_17ct | 39 | stabil | milieu_rollennah | 0.7542 | 0.0407 | 0.6595 | 0.6752 | 0.1378 | 0.2962 | 0.2173 | 0.2717 | 0.2149 | 0.0107 |
| field_stabil::dio_0obq | 39 | stabil | milieu_offen | 0.7399 | 0.0392 | 0.2080 | 0.2479 | 0.0256 | 0.2966 | 0.2174 | 0.2714 | 0.2146 | 0.0081 |
| field_stabil::dio_1jc2 | 38 | stabil | milieu_offen | 0.7734 | 0.0427 | 0.3231 | 0.3465 | 0.0855 | 0.2957 | 0.2167 | 0.2726 | 0.2150 | 0.0132 |
| field_stabil::dio_1cic | 32 | stabil | milieu_offen | 0.7535 | 0.0406 | 0.3299 | 0.3698 | 0.2188 | 0.2961 | 0.2172 | 0.2733 | 0.2134 | 0.0092 |
| field_stabil::dio_1q85 | 32 | stabil | milieu_rollennah | 0.7476 | 0.0389 | 0.6372 | 0.6042 | 0.1680 | 0.2960 | 0.2173 | 0.2720 | 0.2147 | 0.0109 |
| field_stabil::dio_14d9 | 31 | stabil | milieu_offen | 0.7462 | 0.0412 | 0.2115 | 0.2527 | 0.0323 | 0.2957 | 0.2166 | 0.2727 | 0.2150 | 0.0088 |
| field_stabil::dio_1oc2 | 30 | stabil | milieu_rollennah | 0.7464 | 0.0408 | 0.6556 | 0.6667 | 0.0125 | 0.2962 | 0.2167 | 0.2722 | 0.2148 | 0.0128 |
| field_stabil::dio_0pq6 | 30 | stabil | milieu_offen | 0.7484 | 0.0386 | 0.2222 | 0.2667 | 0.0083 | 0.2968 | 0.2168 | 0.2722 | 0.2142 | 0.0079 |
| field_stabil::dio_07uk | 29 | stabil | milieu_offen | 0.7599 | 0.0440 | 0.2605 | 0.3161 | 0.1034 | 0.2942 | 0.2164 | 0.2726 | 0.2169 | 0.0098 |
| field_tragend_unruhig::dio_12fw | 29 | tragend_unruhig | milieu_offen | 0.7216 | 0.0360 | 0.7261 | 0.1724 | 0.2672 | 0.2961 | 0.2173 | 0.2729 | 0.2137 | 0.0111 |
| field_tragend_unruhig::dio_13it | 27 | tragend_unruhig | milieu_offen | 0.6932 | 0.0312 | 1.0000 | 0.3704 | 0.3333 | 0.2972 | 0.2172 | 0.2721 | 0.2136 | 0.0072 |
| field_stabil::dio_0v65 | 26 | stabil | milieu_rollennah | 0.7521 | 0.0408 | 0.7137 | 0.7244 | 0.0769 | 0.2961 | 0.2169 | 0.2728 | 0.2142 | 0.0079 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
