# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 12:55:20

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_check\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_beginnen_zu_differenzieren`
- Gruppen: `27`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0120 |
| alignment | 0.0035 |
| strain_relief | 0.0057 |
| sensory | 0.0109 |
| role_experience | 0.7372 |
| path_experience | 0.9375 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 55 | stabil | milieu_offen | 0.7525 | 0.0385 | 0.3980 | 0.5576 | 0.0500 | 0.2919 | 0.2173 | 0.2738 | 0.2170 | 0.0099 |
| field_stabil::dio_155c | 42 | stabil | milieu_rollennah | 0.7470 | 0.0396 | 0.3360 | 0.5000 | 0.0060 | 0.2932 | 0.2171 | 0.2733 | 0.2164 | 0.0099 |
| field_stabil::dio_0l7p | 28 | stabil | milieu_rolle_und_pfad_getragen | 0.7593 | 0.0417 | 0.7579 | 0.7470 | 0.7321 | 0.2926 | 0.2177 | 0.2739 | 0.2158 | 0.0100 |
| field_stabil::dio_0m9z | 21 | stabil | milieu_offen | 0.7381 | 0.0369 | 0.4339 | 0.3413 | 0.4226 | 0.3017 | 0.2192 | 0.2694 | 0.2097 | 0.1335 |
| field_stabil::dio_1gp2 | 20 | stabil | milieu_offen | 0.7415 | 0.0392 | 0.4139 | 0.3958 | 0.1875 | 0.2952 | 0.2178 | 0.2739 | 0.2130 | 0.0052 |
| field_tragend_unruhig::dio_00ja | 18 | tragend_unruhig | milieu_offen | 0.7237 | 0.0356 | 0.2500 | 0.3333 | 0.0208 | 0.3008 | 0.2198 | 0.2709 | 0.2085 | 0.1323 |
| field_stabil::dio_14wj | 17 | stabil | milieu_rolle_und_pfad_getragen | 0.7622 | 0.0444 | 0.7876 | 0.7941 | 0.7721 | 0.2914 | 0.2177 | 0.2744 | 0.2165 | 0.0095 |
| field_stabil::dio_0h9h | 17 | stabil | milieu_offen | 0.7544 | 0.0444 | 0.3758 | 0.4265 | 0.1985 | 0.2917 | 0.2170 | 0.2742 | 0.2171 | 0.0059 |
| field_stabil::dio_00ly | 17 | stabil | milieu_offen | 0.7561 | 0.0440 | 0.2876 | 0.3039 | 0.1691 | 0.2918 | 0.2173 | 0.2745 | 0.2164 | 0.0077 |
| field_stabil::dio_1ewh | 17 | stabil | milieu_offen | 0.7421 | 0.0414 | 0.2190 | 0.2696 | 0.0368 | 0.2934 | 0.2179 | 0.2750 | 0.2138 | 0.0108 |
| field_stabil::dio_0obq | 16 | stabil | milieu_offen | 0.7386 | 0.0436 | 0.1528 | 0.2135 | 0.0000 | 0.2908 | 0.2170 | 0.2748 | 0.2173 | 0.0080 |
| field_stabil::dio_0pz6 | 15 | stabil | milieu_offen | 0.7608 | 0.0457 | 0.2111 | 0.2444 | 0.0500 | 0.2913 | 0.2175 | 0.2741 | 0.2171 | 0.0054 |
| field_stabil::dio_1lsu | 15 | stabil | milieu_offen | 0.7449 | 0.0444 | 0.2407 | 0.2722 | 0.0583 | 0.2910 | 0.2172 | 0.2744 | 0.2174 | 0.0036 |
| field_stabil::dio_0g2r | 15 | stabil | milieu_offen | 0.7418 | 0.0420 | 0.2704 | 0.2833 | 0.1417 | 0.2938 | 0.2177 | 0.2750 | 0.2136 | 0.0110 |
| field_stabil::dio_0oc3 | 14 | stabil | milieu_rolle_und_pfad_getragen | 0.7298 | 0.0430 | 0.8254 | 0.7976 | 0.6786 | 0.2918 | 0.2180 | 0.2741 | 0.2161 | 0.0106 |
| field_stabil::dio_17ct | 13 | stabil | milieu_offen | 0.7512 | 0.0460 | 0.1410 | 0.1795 | 0.0192 | 0.2897 | 0.2168 | 0.2741 | 0.2194 | 0.0050 |
| field_tragend_unruhig::dio_0m9z | 13 | tragend_unruhig | milieu_offen | 0.7299 | 0.0351 | 0.5342 | 0.4231 | 0.0769 | 0.2974 | 0.2183 | 0.2721 | 0.2122 | 0.0102 |
| field_stabil::dio_06s7 | 11 | stabil | milieu_offen | 0.7610 | 0.0463 | 0.2576 | 0.2955 | 0.0909 | 0.2929 | 0.2170 | 0.2738 | 0.2163 | 0.0043 |
| field_tragend_unruhig::dio_05yg | 11 | tragend_unruhig | milieu_offen | 0.7114 | 0.0389 | 0.4293 | 0.4621 | 0.1818 | 0.2953 | 0.2188 | 0.2742 | 0.2118 | 0.0105 |
| field_stabil::dio_1u5i | 10 | stabil | milieu_offen | 0.7533 | 0.0450 | 0.3389 | 0.3583 | 0.3000 | 0.2915 | 0.2173 | 0.2743 | 0.2168 | 0.0035 |
| field_tragend_unruhig::dio_0jkk | 10 | tragend_unruhig | milieu_offen | 0.7086 | 0.0395 | 0.5000 | 0.5500 | 0.1000 | 0.2938 | 0.2188 | 0.2751 | 0.2123 | 0.0084 |
| field_stabil::dio_1kpz | 9 | stabil | milieu_rolle_und_pfad_getragen | 0.7642 | 0.0481 | 0.6852 | 0.6481 | 0.5556 | 0.2912 | 0.2173 | 0.2743 | 0.2172 | 0.0049 |
| field_stabil::dio_09bn | 9 | stabil | milieu_offen | 0.7566 | 0.0474 | 0.3272 | 0.3796 | 0.1111 | 0.2911 | 0.2163 | 0.2742 | 0.2184 | 0.0046 |
| field_stabil::dio_1q85 | 9 | stabil | milieu_offen | 0.7386 | 0.0448 | 0.5556 | 0.4907 | 0.4167 | 0.2920 | 0.2180 | 0.2741 | 0.2159 | 0.0113 |
| field_stabil::dio_06er | 8 | stabil | milieu_rolle_und_pfad_getragen | 0.7644 | 0.0489 | 0.9375 | 0.9167 | 0.9375 | 0.2909 | 0.2180 | 0.2747 | 0.2164 | 0.0061 |
| field_stabil::dio_1cic | 8 | stabil | milieu_rolle_und_pfad_getragen | 0.7486 | 0.0465 | 0.8125 | 0.7604 | 0.8125 | 0.2907 | 0.2180 | 0.2747 | 0.2166 | 0.0084 |
| field_stabil::dio_04uf | 8 | stabil | milieu_offen | 0.7366 | 0.0421 | 0.3472 | 0.3542 | 0.0625 | 0.2924 | 0.2172 | 0.2741 | 0.2163 | 0.0072 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.
