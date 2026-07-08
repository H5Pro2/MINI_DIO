# Relative Randdruck-Lupe

## Zweck

Diese Diagnose liest innerhalb jeder Welt konkurrierende Druckprofile.
Sie ersetzt keine Runtime-Mechanik und erzeugt kein Gate.

Gelesene Profile:

```text
randdruck        = Strain, Intake-Druck, Gap und schwache Rekopplung
offene_variante  = Spannung, Gap, Carry, Rekopplung und Nachhall
rekopplung       = Rekopplung, Sinneskopplung, Carry und geringe Last
daempfung        = geringe Aufnahme, geringe Gap-Spannung und stabile Kopplung
```

Die Werte sind relative Druckprofile innerhalb der jeweiligen Welt.
Sie sind keine universellen MCM-Grenzen.

## Kurzbefund

| Welt | Episoden | Randdruck | Offen | Rekopplung | Daempfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SYNTH_RUHE_ORIG | 994 | 0.3994 | 0.1509 | 0.2706 | 0.1791 | 0.1182 | 0.0164 | 0.0844 | 0.0053 |
| SYNTH_RUHE_REPRO | 994 | 0.3994 | 0.1509 | 0.2706 | 0.1791 | 0.1182 | 0.0164 | 0.0844 | 0.0053 |
| SYNTH_BRUCH_RAND_ORIG | 7994 | 0.4567 | 0.0997 | 0.3914 | 0.0522 | 0.1251 | 0.0255 | 0.1065 | 0.0147 |
| SYNTH_BRUCH_RAND_REPRO | 7994 | 0.4567 | 0.0997 | 0.3914 | 0.0522 | 0.1251 | 0.0255 | 0.1065 | 0.0147 |
| KONTROLL_EXPANSION_ORIG | 9994 | 0.4260 | 0.1328 | 0.3387 | 0.1026 | 0.1704 | 0.1043 | 0.1842 | 0.1005 |
| KONTROLL_EXPANSION_REPRO | 9994 | 0.4260 | 0.1328 | 0.3387 | 0.1026 | 0.1704 | 0.1043 | 0.1842 | 0.1005 |

## Randdruck-Spitzen


### SYNTH_RUHE_ORIG

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 497 | 1.0000 | stabil | dio_14wj | dio_mcm_episode_0lx7o7j | 0.1432 | 0.0341 | 0.1815 | 0.0085 |
| 424 | 0.9743 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1282 | 0.0295 | 0.1055 | 0.0206 |
| 530 | 0.9729 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1288 | 0.0297 | 0.1031 | 0.0249 |
| 529 | 0.9687 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1279 | 0.0304 | 0.0939 | 0.0262 |
| 629 | 0.9679 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1278 | 0.0299 | 0.0985 | 0.0200 |
| 423 | 0.9673 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1276 | 0.0287 | 0.1044 | 0.0190 |
| 425 | 0.9668 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1279 | 0.0285 | 0.1053 | 0.0198 |
| 375 | 0.9661 | stabil | dio_0g3b | dio_mcm_episode_0lx7o7j | 0.1270 | 0.0295 | 0.1001 | 0.0168 |
| 273 | 0.9661 | stabil | dio_0g3b | dio_mcm_episode_0lx7o7j | 0.1300 | 0.0288 | 0.0965 | 0.0137 |
| 531 | 0.9642 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1284 | 0.0284 | 0.1046 | 0.0226 |

### SYNTH_RUHE_REPRO

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 497 | 1.0000 | stabil | dio_14wj | dio_mcm_episode_0lx7o7j | 0.1432 | 0.0341 | 0.1815 | 0.0085 |
| 424 | 0.9743 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1282 | 0.0295 | 0.1055 | 0.0206 |
| 530 | 0.9729 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1288 | 0.0297 | 0.1031 | 0.0249 |
| 529 | 0.9687 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1279 | 0.0304 | 0.0939 | 0.0262 |
| 629 | 0.9679 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1278 | 0.0299 | 0.0985 | 0.0200 |
| 423 | 0.9673 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1276 | 0.0287 | 0.1044 | 0.0190 |
| 425 | 0.9668 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1279 | 0.0285 | 0.1053 | 0.0198 |
| 375 | 0.9661 | stabil | dio_0g3b | dio_mcm_episode_0lx7o7j | 0.1270 | 0.0295 | 0.1001 | 0.0168 |
| 273 | 0.9661 | stabil | dio_0g3b | dio_mcm_episode_0lx7o7j | 0.1300 | 0.0288 | 0.0965 | 0.0137 |
| 531 | 0.9642 | stabil | dio_1fll | dio_mcm_episode_0lx7o7j | 0.1284 | 0.0284 | 0.1046 | 0.0226 |

### SYNTH_BRUCH_RAND_ORIG

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 3528 | 1.0000 | tragend_unruhig | dio_1nkp | dio_mcm_episode_163ajqw | 0.3252 | 0.4074 | 0.2216 | 0.5620 |
| 504 | 0.9998 | tragend_unruhig | dio_0kcg | dio_mcm_episode_16da5fv | 0.3128 | 0.4040 | 0.2023 | 0.5086 |
| 1008 | 0.9998 | tragend_unruhig | dio_0im7 | dio_mcm_episode_11n7g5f | 0.3224 | 0.3834 | 0.2632 | 0.5520 |
| 3888 | 0.9996 | stabil | dio_1b1g | dio_mcm_episode_0kvw1tc | 0.2713 | 0.3590 | 0.0433 | 0.4651 |
| 2520 | 0.9994 | stabil | dio_0h4u | dio_mcm_episode_0kvw1tc | 0.2636 | 0.3330 | 0.0723 | 0.4308 |
| 2016 | 0.9993 | tragend_unruhig | dio_0una | dio_mcm_episode_0xsyn4p | 0.2792 | 0.2445 | 0.4555 | 0.3336 |
| 3024 | 0.9993 | stabil | dio_0o0m | dio_mcm_episode_0kvw1tc | 0.2619 | 0.3263 | 0.1076 | 0.3777 |
| 3529 | 0.9989 | stabil | dio_1dy1 | dio_mcm_episode_12k5tow | 0.2438 | 0.2623 | 0.1921 | 0.2879 |
| 1848 | 0.9989 | stabil | dio_1amt | dio_mcm_episode_1yxc2ug | 0.2537 | 0.2325 | 0.3262 | 0.2974 |
| 1603 | 0.9986 | stabil | dio_1xwq | dio_mcm_episode_13llj7l | 0.2302 | 0.2486 | 0.1112 | 0.3164 |

### SYNTH_BRUCH_RAND_REPRO

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 3528 | 1.0000 | tragend_unruhig | dio_1nkp | dio_mcm_episode_163ajqw | 0.3252 | 0.4074 | 0.2216 | 0.5620 |
| 504 | 0.9998 | tragend_unruhig | dio_0kcg | dio_mcm_episode_16da5fv | 0.3128 | 0.4040 | 0.2023 | 0.5086 |
| 1008 | 0.9998 | tragend_unruhig | dio_0im7 | dio_mcm_episode_11n7g5f | 0.3224 | 0.3834 | 0.2632 | 0.5520 |
| 3888 | 0.9996 | stabil | dio_1b1g | dio_mcm_episode_0kvw1tc | 0.2713 | 0.3590 | 0.0433 | 0.4651 |
| 2520 | 0.9994 | stabil | dio_0h4u | dio_mcm_episode_0kvw1tc | 0.2636 | 0.3330 | 0.0723 | 0.4308 |
| 2016 | 0.9993 | tragend_unruhig | dio_0una | dio_mcm_episode_0xsyn4p | 0.2792 | 0.2445 | 0.4555 | 0.3336 |
| 3024 | 0.9993 | stabil | dio_0o0m | dio_mcm_episode_0kvw1tc | 0.2619 | 0.3263 | 0.1076 | 0.3777 |
| 3529 | 0.9989 | stabil | dio_1dy1 | dio_mcm_episode_12k5tow | 0.2438 | 0.2623 | 0.1921 | 0.2879 |
| 1848 | 0.9989 | stabil | dio_1amt | dio_mcm_episode_1yxc2ug | 0.2537 | 0.2325 | 0.3262 | 0.2974 |
| 1603 | 0.9986 | stabil | dio_1xwq | dio_mcm_episode_13llj7l | 0.2302 | 0.2486 | 0.1112 | 0.3164 |

### KONTROLL_EXPANSION_ORIG

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 374 | 0.9999 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3483 | 0.4190 | 0.3953 | 0.5675 |
| 525 | 0.9998 | tragend_unruhig | dio_179e | dio_mcm_episode_0pjmsgw | 0.3370 | 0.4204 | 0.3177 | 0.5481 |
| 2303 | 0.9994 | tragend_unruhig | dio_19mz | dio_mcm_episode_1318m49 | 0.3369 | 0.4048 | 0.3671 | 0.5363 |
| 6893 | 0.9994 | tragend_unruhig | dio_04db | dio_mcm_episode_0r7nk4p | 0.3353 | 0.3967 | 0.3618 | 0.5488 |
| 3713 | 0.9991 | tragend_unruhig | dio_12n7 | dio_mcm_episode_1318m49 | 0.3336 | 0.4007 | 0.3544 | 0.5350 |
| 635 | 0.9990 | tragend_unruhig | dio_0766 | dio_mcm_episode_0ezbiel | 0.3273 | 0.4184 | 0.2736 | 0.5109 |
| 408 | 0.9988 | tragend_unruhig | dio_17qo | dio_mcm_episode_0ezbiel | 0.3248 | 0.4022 | 0.2903 | 0.5174 |
| 5086 | 0.9987 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3256 | 0.3886 | 0.3266 | 0.5265 |
| 7728 | 0.9986 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3259 | 0.3991 | 0.3133 | 0.5128 |
| 3853 | 0.9985 | tragend_unruhig | dio_11et | dio_mcm_episode_0r7nk4p | 0.3317 | 0.3808 | 0.3834 | 0.5321 |

### KONTROLL_EXPANSION_REPRO

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 374 | 0.9999 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3483 | 0.4190 | 0.3953 | 0.5675 |
| 525 | 0.9998 | tragend_unruhig | dio_179e | dio_mcm_episode_0pjmsgw | 0.3370 | 0.4204 | 0.3177 | 0.5481 |
| 2303 | 0.9994 | tragend_unruhig | dio_19mz | dio_mcm_episode_1318m49 | 0.3369 | 0.4048 | 0.3671 | 0.5363 |
| 6893 | 0.9994 | tragend_unruhig | dio_04db | dio_mcm_episode_0r7nk4p | 0.3353 | 0.3967 | 0.3618 | 0.5488 |
| 3713 | 0.9991 | tragend_unruhig | dio_12n7 | dio_mcm_episode_1318m49 | 0.3336 | 0.4007 | 0.3544 | 0.5350 |
| 635 | 0.9990 | tragend_unruhig | dio_0766 | dio_mcm_episode_0ezbiel | 0.3273 | 0.4184 | 0.2736 | 0.5109 |
| 408 | 0.9988 | tragend_unruhig | dio_17qo | dio_mcm_episode_0ezbiel | 0.3248 | 0.4022 | 0.2903 | 0.5174 |
| 5086 | 0.9987 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3256 | 0.3886 | 0.3266 | 0.5265 |
| 7728 | 0.9986 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3259 | 0.3991 | 0.3133 | 0.5128 |
| 3853 | 0.9985 | tragend_unruhig | dio_11et | dio_mcm_episode_0r7nk4p | 0.3317 | 0.3808 | 0.3834 | 0.5321 |

## Lesart

Diese Lupe trennt zwei Ebenen:

```text
Topologie-Matrix: Welche Rolle dominiert im Gesamtbild?
Randdruck-Lupe: Wo entstehen lokale Rand-/Oeffnungsdruecke innerhalb der Welt?
```

Damit kann eine Welt insgesamt zentrumsnah bleiben und trotzdem lokale Randdruckzonen enthalten.

## Wie es weitergeht

Als naechstes sollte diese Lupe gegen echte Stressfenster und synthetische Randfenster verglichen werden.
Entscheidend ist, ob Randdruck nur kurz aufflackert, ob er rekoppelt oder ob er zu stabilen offenen Bedeutungsinseln reift.
