# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 12:49:03

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\multiworld_axis_map\adaptive_btc_2024_5m_0_to_1000\real_a\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `27`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0120 |
| alignment | 0.0034 |
| strain_relief | 0.0057 |
| sensory | 0.0109 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Adaptiv | Delta | Erfahrung | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 55 | stabil | 0.7525 | 0.0385 | 0.3980 | 0.2919 | 0.2173 | 0.2738 | 0.2170 | 0.0099 |
| field_stabil::dio_155c | 42 | stabil | 0.7470 | 0.0396 | 0.3360 | 0.2932 | 0.2171 | 0.2733 | 0.2164 | 0.0098 |
| field_stabil::dio_0l7p | 28 | stabil | 0.7593 | 0.0417 | 0.7579 | 0.2926 | 0.2178 | 0.2739 | 0.2157 | 0.0099 |
| field_stabil::dio_0m9z | 21 | stabil | 0.7381 | 0.0369 | 0.4339 | 0.3017 | 0.2193 | 0.2694 | 0.2096 | 0.1335 |
| field_stabil::dio_1gp2 | 20 | stabil | 0.7415 | 0.0392 | 0.4139 | 0.2952 | 0.2179 | 0.2740 | 0.2129 | 0.0055 |
| field_tragend_unruhig::dio_00ja | 18 | tragend_unruhig | 0.7237 | 0.0356 | 0.2500 | 0.3008 | 0.2198 | 0.2709 | 0.2085 | 0.1323 |
| field_stabil::dio_14wj | 17 | stabil | 0.7622 | 0.0444 | 0.7876 | 0.2913 | 0.2178 | 0.2744 | 0.2164 | 0.0095 |
| field_stabil::dio_0h9h | 17 | stabil | 0.7544 | 0.0444 | 0.3758 | 0.2917 | 0.2171 | 0.2742 | 0.2170 | 0.0058 |
| field_stabil::dio_00ly | 17 | stabil | 0.7561 | 0.0440 | 0.2876 | 0.2918 | 0.2174 | 0.2745 | 0.2163 | 0.0076 |
| field_stabil::dio_1ewh | 17 | stabil | 0.7421 | 0.0414 | 0.2190 | 0.2934 | 0.2179 | 0.2750 | 0.2138 | 0.0108 |
| field_stabil::dio_0obq | 16 | stabil | 0.7386 | 0.0436 | 0.1528 | 0.2908 | 0.2170 | 0.2748 | 0.2173 | 0.0080 |
| field_stabil::dio_0pz6 | 15 | stabil | 0.7608 | 0.0456 | 0.2111 | 0.2913 | 0.2176 | 0.2740 | 0.2170 | 0.0053 |
| field_stabil::dio_1lsu | 15 | stabil | 0.7449 | 0.0444 | 0.2407 | 0.2910 | 0.2173 | 0.2744 | 0.2173 | 0.0035 |
| field_stabil::dio_0g2r | 15 | stabil | 0.7418 | 0.0420 | 0.2704 | 0.2938 | 0.2178 | 0.2750 | 0.2135 | 0.0110 |
| field_stabil::dio_0oc3 | 14 | stabil | 0.7298 | 0.0430 | 0.8254 | 0.2918 | 0.2181 | 0.2741 | 0.2159 | 0.0105 |
| field_stabil::dio_17ct | 13 | stabil | 0.7512 | 0.0460 | 0.1410 | 0.2898 | 0.2168 | 0.2741 | 0.2193 | 0.0050 |
| field_tragend_unruhig::dio_0m9z | 13 | tragend_unruhig | 0.7300 | 0.0352 | 0.5342 | 0.2972 | 0.2182 | 0.2722 | 0.2125 | 0.0093 |
| field_stabil::dio_06s7 | 11 | stabil | 0.7610 | 0.0463 | 0.2576 | 0.2929 | 0.2170 | 0.2739 | 0.2162 | 0.0043 |
| field_tragend_unruhig::dio_05yg | 11 | tragend_unruhig | 0.7114 | 0.0390 | 0.4293 | 0.2951 | 0.2186 | 0.2741 | 0.2122 | 0.0105 |
| field_stabil::dio_1u5i | 10 | stabil | 0.7533 | 0.0450 | 0.3389 | 0.2915 | 0.2174 | 0.2743 | 0.2168 | 0.0035 |
| field_tragend_unruhig::dio_0jkk | 10 | tragend_unruhig | 0.7087 | 0.0396 | 0.5000 | 0.2935 | 0.2186 | 0.2751 | 0.2128 | 0.0084 |
| field_stabil::dio_1kpz | 9 | stabil | 0.7642 | 0.0480 | 0.6852 | 0.2912 | 0.2175 | 0.2744 | 0.2170 | 0.0049 |
| field_stabil::dio_09bn | 9 | stabil | 0.7565 | 0.0474 | 0.3272 | 0.2911 | 0.2164 | 0.2742 | 0.2183 | 0.0053 |
| field_stabil::dio_1q85 | 9 | stabil | 0.7386 | 0.0448 | 0.5556 | 0.2920 | 0.2181 | 0.2741 | 0.2157 | 0.0113 |
| field_stabil::dio_06er | 8 | stabil | 0.7644 | 0.0489 | 0.9375 | 0.2909 | 0.2181 | 0.2747 | 0.2163 | 0.0059 |
| field_stabil::dio_1cic | 8 | stabil | 0.7486 | 0.0466 | 0.8125 | 0.2906 | 0.2180 | 0.2747 | 0.2166 | 0.0080 |
| field_stabil::dio_04uf | 8 | stabil | 0.7366 | 0.0421 | 0.3472 | 0.2924 | 0.2173 | 0.2741 | 0.2162 | 0.0074 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
