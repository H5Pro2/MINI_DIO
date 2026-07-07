# Adaptive Rekopplung nach Rolle und Familie

Stand: 2026-07-07 13:00:32

## Zweck

Diese Diagnose prueft, ob adaptive Rekopplung nur global anhebt oder ob sie nach Feldrolle und Symbolfamilie unterschiedlich gewichtet.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Eingabe

- Quelle: `debug\adaptive_milieu_worlds\xrp\dio_mini_lauf_1\episodes.csv`
- Gruppierung: `role_family`

## Gesamtlesung

- Lesung: `adaptive_gewichte_innerhalb_der_gruppen_noch_flach`
- Gruppen: `19`

| Gewicht | Spanne zwischen Gruppen |
|---|---:|
| carry | 0.0085 |
| alignment | 0.0020 |
| strain_relief | 0.0067 |
| sensory | 0.0077 |
| role_experience | 0.8274 |
| path_experience | 1.0000 |

## Gruppen

| Gruppe | Anzahl | Wirkung | Milieu | Adaptiv | Delta | Erfahrung | Rolle | Pfad | Carry | Align | StrainRelief | Sensory | MaxSpan |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| field_stabil::dio_104t | 34 | stabil | milieu_offen | 0.7501 | 0.0400 | 0.3039 | 0.3848 | 0.1360 | 0.2924 | 0.2172 | 0.2736 | 0.2168 | 0.0075 |
| field_stabil::dio_155c | 28 | stabil | milieu_offen | 0.7441 | 0.0407 | 0.2877 | 0.3631 | 0.0714 | 0.2924 | 0.2172 | 0.2738 | 0.2166 | 0.0109 |
| field_stabil::dio_0m9z | 26 | stabil | milieu_rolle_und_pfad_getragen | 0.7395 | 0.0389 | 0.4808 | 0.5321 | 0.2019 | 0.2930 | 0.2178 | 0.2735 | 0.2157 | 0.0089 |
| field_stabil::dio_0l7p | 22 | stabil | milieu_offen | 0.7564 | 0.0424 | 0.3207 | 0.3674 | 0.2159 | 0.2915 | 0.2172 | 0.2742 | 0.2171 | 0.0044 |
| field_stabil::dio_1gp2 | 19 | stabil | milieu_offen | 0.7432 | 0.0403 | 0.3012 | 0.2895 | 0.2303 | 0.2953 | 0.2179 | 0.2745 | 0.2124 | 0.0113 |
| field_stabil::dio_00ly | 16 | stabil | milieu_offen | 0.7539 | 0.0440 | 0.5451 | 0.5573 | 0.4531 | 0.2920 | 0.2174 | 0.2741 | 0.2165 | 0.0103 |
| field_stabil::dio_0h9h | 16 | stabil | milieu_offen | 0.7539 | 0.0437 | 0.2639 | 0.2969 | 0.1250 | 0.2933 | 0.2172 | 0.2742 | 0.2153 | 0.0057 |
| field_stabil::dio_0pz6 | 14 | stabil | milieu_offen | 0.7563 | 0.0423 | 0.1508 | 0.1726 | 0.0446 | 0.2979 | 0.2184 | 0.2690 | 0.2148 | 0.1325 |
| field_stabil::dio_1kpz | 13 | stabil | milieu_rolle_und_pfad_getragen | 0.7640 | 0.0461 | 0.6368 | 0.6474 | 0.5385 | 0.2923 | 0.2175 | 0.2746 | 0.2157 | 0.0038 |
| field_stabil::dio_0g2r | 13 | stabil | milieu_offen | 0.7399 | 0.0426 | 0.4658 | 0.5064 | 0.3846 | 0.2931 | 0.2174 | 0.2741 | 0.2154 | 0.0050 |
| field_stabil::dio_1ewh | 12 | stabil | milieu_offen | 0.7395 | 0.0432 | 0.3889 | 0.4097 | 0.2604 | 0.2921 | 0.2173 | 0.2744 | 0.2162 | 0.0075 |
| field_tragend_unruhig::dio_05yg | 12 | tragend_unruhig | milieu_offen | 0.7156 | 0.0399 | 0.1713 | 0.2361 | 0.0000 | 0.2928 | 0.2189 | 0.2748 | 0.2135 | 0.0116 |
| field_tragend_unruhig::dio_00ja | 12 | tragend_unruhig | milieu_offen | 0.7247 | 0.0394 | 0.3426 | 0.3681 | 0.1146 | 0.2942 | 0.2183 | 0.2753 | 0.2123 | 0.0134 |
| field_stabil::dio_14wj | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7556 | 0.0452 | 1.0000 | 1.0000 | 1.0000 | 0.2913 | 0.2179 | 0.2747 | 0.2161 | 0.0033 |
| field_stabil::dio_0oc3 | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7257 | 0.0442 | 0.8111 | 0.8167 | 0.7000 | 0.2921 | 0.2178 | 0.2744 | 0.2157 | 0.0062 |
| field_stabil::dio_1lsu | 10 | stabil | milieu_rolle_und_pfad_getragen | 0.7345 | 0.0438 | 0.7278 | 0.7417 | 0.6000 | 0.2927 | 0.2179 | 0.2740 | 0.2154 | 0.0077 |
| field_stabil::dio_17ct | 9 | stabil | milieu_offen | 0.7458 | 0.0464 | 0.2284 | 0.2315 | 0.0833 | 0.2921 | 0.2170 | 0.2741 | 0.2168 | 0.0048 |
| field_tragend_unruhig::dio_1v2w | 9 | tragend_unruhig | milieu_offen | 0.7071 | 0.0387 | 0.4815 | 0.5000 | 0.1528 | 0.2944 | 0.2190 | 0.2757 | 0.2109 | 0.0099 |
| field_stabil::dio_09bn | 8 | stabil | milieu_offen | 0.7595 | 0.0489 | 0.4444 | 0.4479 | 0.2969 | 0.2894 | 0.2174 | 0.2747 | 0.2186 | 0.0030 |

## Befund

Diese Diagnose trennt die adaptive Rueckfuehrung von der globalen Mittelung.
Wenn die Spannen klein bleiben, liegt die Gleichfoermigkeit nicht nur am Mehrweltmittel, sondern auch innerhalb der Rollen-/Familiengruppen.

## Wie es weitergeht

Als naechstes sollte die adaptive Erfahrung nicht nur aus Durchschnittswerten, sondern aus Rollenmilieu und Zustandspfad gebildet werden. Dann koennen stabile, randnahe, offene und rekoppelnde Lagen eigene Gewichtungsprofile ausbilden.
