# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 12:51:04

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\multiworld_axis_map\adaptive_doge_2024_5m_0_to_1000\real_a\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `26`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0127 |
| alignment | 0.0022 |
| strain_relief | 0.0074 |
| sensory | 0.0080 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Adaptiv | Delta | Erfahrung | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 61 | stabil | 0.7514 | 0.0365 | 0.3752 | 0.2973 | 0.2180 | 0.2712 | 0.2136 | 0.1320 |
| field_stabil::dio_0m9z | 35 | stabil | 0.7425 | 0.0370 | 0.3508 | 0.2947 | 0.2187 | 0.2726 | 0.2140 | 0.0104 |
| field_stabil::dio_155c | 34 | stabil | 0.7424 | 0.0359 | 0.4461 | 0.3038 | 0.2189 | 0.2679 | 0.2094 | 0.1257 |
| field_stabil::dio_0h9h | 32 | stabil | 0.7547 | 0.0385 | 0.2552 | 0.2993 | 0.2183 | 0.2694 | 0.2129 | 0.1332 |
| field_stabil::dio_0l7p | 26 | stabil | 0.7564 | 0.0392 | 0.2756 | 0.2978 | 0.2182 | 0.2707 | 0.2133 | 0.1320 |
| field_stabil::dio_0pz6 | 16 | stabil | 0.7622 | 0.0452 | 0.6424 | 0.2931 | 0.2177 | 0.2735 | 0.2157 | 0.0065 |
| field_stabil::dio_00ly | 16 | stabil | 0.7572 | 0.0442 | 0.2500 | 0.2925 | 0.2170 | 0.2739 | 0.2166 | 0.0095 |
| field_tragend_unruhig::dio_00ja | 16 | tragend_unruhig | 0.7287 | 0.0374 | 0.3854 | 0.2949 | 0.2183 | 0.2750 | 0.2118 | 0.0137 |
| field_stabil::dio_09bn | 15 | stabil | 0.7606 | 0.0449 | 0.3630 | 0.2937 | 0.2172 | 0.2728 | 0.2163 | 0.0076 |
| field_tragend_unruhig::dio_0m9z | 14 | tragend_unruhig | 0.7312 | 0.0362 | 0.4286 | 0.2951 | 0.2186 | 0.2724 | 0.2138 | 0.0112 |
| field_stabil::dio_1ewh | 13 | stabil | 0.7396 | 0.0430 | 0.3632 | 0.2918 | 0.2174 | 0.2742 | 0.2166 | 0.0071 |
| field_stabil::dio_1kpz | 12 | stabil | 0.7600 | 0.0459 | 0.3935 | 0.2921 | 0.2168 | 0.2737 | 0.2174 | 0.0041 |
| field_stabil::dio_17ct | 12 | stabil | 0.7487 | 0.0446 | 0.4769 | 0.2933 | 0.2177 | 0.2733 | 0.2157 | 0.0076 |
| field_stabil::dio_0oc3 | 12 | stabil | 0.7294 | 0.0428 | 0.2037 | 0.2936 | 0.2185 | 0.2739 | 0.2139 | 0.0091 |
| field_stabil::dio_0g2r | 11 | stabil | 0.7384 | 0.0439 | 0.1162 | 0.2911 | 0.2180 | 0.2751 | 0.2158 | 0.0110 |
| field_tragend_unruhig::dio_0jkk | 11 | tragend_unruhig | 0.7145 | 0.0397 | 0.1869 | 0.2937 | 0.2190 | 0.2748 | 0.2125 | 0.0102 |
| field_stabil::dio_14wj | 10 | stabil | 0.7565 | 0.0459 | 0.9278 | 0.2919 | 0.2182 | 0.2743 | 0.2156 | 0.0071 |
| field_stabil::dio_1cic | 10 | stabil | 0.7481 | 0.0447 | 0.8111 | 0.2933 | 0.2178 | 0.2742 | 0.2147 | 0.0055 |
| field_tragend_unruhig::dio_05yg | 10 | tragend_unruhig | 0.7103 | 0.0399 | 0.4222 | 0.2934 | 0.2187 | 0.2748 | 0.2131 | 0.0101 |
| field_tragend_unruhig::dio_1v2w | 10 | tragend_unruhig | 0.7096 | 0.0377 | 0.2722 | 0.2959 | 0.2190 | 0.2753 | 0.2098 | 0.0098 |
| field_stabil::dio_06s7 | 9 | stabil | 0.7605 | 0.0470 | 0.7901 | 0.2927 | 0.2179 | 0.2739 | 0.2154 | 0.0049 |
| field_stabil::dio_07uk | 8 | stabil | 0.7588 | 0.0494 | 0.5486 | 0.2913 | 0.2175 | 0.2740 | 0.2172 | 0.0050 |
| field_stabil::dio_1lsu | 8 | stabil | 0.7419 | 0.0465 | 0.3403 | 0.2912 | 0.2177 | 0.2751 | 0.2161 | 0.0049 |
| field_stabil::dio_0fe7 | 8 | stabil | 0.7436 | 0.0458 | 0.2917 | 0.2922 | 0.2171 | 0.2739 | 0.2167 | 0.0035 |
| field_stabil::dio_1u5i | 8 | stabil | 0.7503 | 0.0455 | 0.4306 | 0.2926 | 0.2173 | 0.2743 | 0.2158 | 0.0018 |
| field_stabil::dio_1gp2 | 8 | stabil | 0.7341 | 0.0442 | 0.3611 | 0.2914 | 0.2177 | 0.2745 | 0.2163 | 0.0083 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.

## Wie es weitergeht

Als naechstes sollte die adaptive Erfahrung nicht nur aus Durchschnittswerten, sondern aus Rollenmilieu und Zustandspfad gebildet werden. Dann koennen stabile, randnahe, offene und rekoppelnde Lagen eigene Gewichtungsprofile ausbilden.
