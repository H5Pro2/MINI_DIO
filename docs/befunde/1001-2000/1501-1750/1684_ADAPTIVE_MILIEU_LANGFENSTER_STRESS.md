# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:12:58

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_long\stress\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_innerhalb_der_gruppen_noch_flach`
- Gruppen: `20`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0048 |
| alignment | 0.0020 |
| strain_relief | 0.0032 |
| sensory | 0.0063 |
| role_experience | 0.6811 |
| path_experience | 0.8038 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 94 | stabil | milieu_rollennah | 0.7545 | 0.0365 | 0.4545 | 0.6241 | 0.0505 | 0.2955 | 0.2176 | 0.2725 | 0.2144 | 0.1310 |
| field_stabil::dio_155c | 65 | stabil | milieu_rollennah | 0.7479 | 0.0383 | 0.4718 | 0.6218 | 0.1269 | 0.2948 | 0.2173 | 0.2724 | 0.2156 | 0.0121 |
| field_stabil::dio_0h9h | 55 | stabil | milieu_rollennah | 0.7611 | 0.0399 | 0.5424 | 0.7076 | 0.0295 | 0.2950 | 0.2168 | 0.2726 | 0.2156 | 0.0108 |
| field_stabil::dio_0l7p | 43 | stabil | milieu_offen | 0.7610 | 0.0405 | 0.4574 | 0.4574 | 0.3634 | 0.2943 | 0.2175 | 0.2735 | 0.2147 | 0.0126 |
| field_stabil::dio_0m9z | 42 | stabil | milieu_offen | 0.7421 | 0.0365 | 0.3161 | 0.2540 | 0.2649 | 0.2977 | 0.2179 | 0.2721 | 0.2123 | 0.0148 |
| field_stabil::dio_00ly | 37 | stabil | milieu_rollennah | 0.7547 | 0.0396 | 0.4565 | 0.5946 | 0.1419 | 0.2983 | 0.2177 | 0.2713 | 0.2128 | 0.1327 |
| field_tragend_unruhig::dio_00ja | 36 | tragend_unruhig | milieu_offen | 0.7302 | 0.0345 | 0.4583 | 0.5139 | 0.0764 | 0.2982 | 0.2183 | 0.2731 | 0.2104 | 0.0117 |
| field_stabil::dio_1gp2 | 32 | stabil | milieu_offen | 0.7435 | 0.0372 | 0.2656 | 0.2891 | 0.1406 | 0.2981 | 0.2177 | 0.2728 | 0.2113 | 0.0127 |
| field_tragend_unruhig::dio_0jkk | 32 | tragend_unruhig | milieu_offen | 0.7167 | 0.0349 | 0.4861 | 0.3516 | 0.1641 | 0.2972 | 0.2186 | 0.2728 | 0.2113 | 0.0159 |
| field_stabil::dio_14wj | 30 | stabil | milieu_rolle_und_pfad_getragen | 0.7661 | 0.0421 | 0.8981 | 0.8944 | 0.8333 | 0.2935 | 0.2175 | 0.2738 | 0.2152 | 0.0110 |
| field_stabil::dio_0oc3 | 28 | stabil | milieu_offen | 0.7308 | 0.0395 | 0.2381 | 0.2708 | 0.1250 | 0.2959 | 0.2177 | 0.2724 | 0.2140 | 0.0118 |
| field_stabil::dio_0g2r | 26 | stabil | milieu_offen | 0.7436 | 0.0400 | 0.3547 | 0.4295 | 0.1538 | 0.2947 | 0.2174 | 0.2737 | 0.2142 | 0.0108 |
| field_tragend_unruhig::dio_0m9z | 25 | tragend_unruhig | milieu_offen | 0.7317 | 0.0346 | 0.3178 | 0.2133 | 0.1000 | 0.2980 | 0.2179 | 0.2718 | 0.2123 | 0.0141 |
| field_stabil::dio_17ct | 24 | stabil | milieu_offen | 0.7512 | 0.0426 | 0.2731 | 0.3472 | 0.0833 | 0.2936 | 0.2167 | 0.2731 | 0.2165 | 0.0077 |
| field_stabil::dio_1ewh | 22 | stabil | milieu_offen | 0.7420 | 0.0405 | 0.2828 | 0.3333 | 0.1364 | 0.2945 | 0.2174 | 0.2737 | 0.2145 | 0.0098 |
| field_tragend_unruhig::dio_05yg | 22 | tragend_unruhig | milieu_offen | 0.7180 | 0.0367 | 0.7879 | 0.5417 | 0.4545 | 0.2961 | 0.2178 | 0.2730 | 0.2131 | 0.0114 |
| field_stabil::dio_0pz6 | 21 | stabil | milieu_offen | 0.7624 | 0.0435 | 0.5979 | 0.6190 | 0.4583 | 0.2945 | 0.2174 | 0.2728 | 0.2153 | 0.0126 |
| field_stabil::dio_0nlj | 20 | stabil | milieu_offen | 0.7704 | 0.0454 | 0.5056 | 0.5333 | 0.4000 | 0.2935 | 0.2166 | 0.2732 | 0.2167 | 0.0087 |
| field_stabil::dio_0obq | 20 | stabil | milieu_offen | 0.7395 | 0.0422 | 0.3972 | 0.4417 | 0.1688 | 0.2936 | 0.2172 | 0.2733 | 0.2159 | 0.0080 |
| field_tragend_unruhig::dio_1v2w | 20 | tragend_unruhig | milieu_offen | 0.7136 | 0.0359 | 0.5028 | 0.3375 | 0.1000 | 0.2957 | 0.2185 | 0.2744 | 0.2114 | 0.0138 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.

## Wie es weitergeht

Als naechstes sollte die adaptive Erfahrung nicht nur aus Durchschnittswerten, sondern aus Rollenmilieu und Zustandspfad gebildet werden. Dann koennen stabile, randnahe, offene und rekoppelnde Lagen eigene Gewichtungsprofile ausbilden.
