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
| PRESSURE_LONG_STABLE_10K | 9994 | 0.4254 | 0.1354 | 0.3315 | 0.1078 | 0.1702 | 0.1049 | 0.1807 | 0.1017 |
| PRESSURE_LONG_STRESS_10K | 9994 | 0.4265 | 0.1360 | 0.3309 | 0.1067 | 0.1708 | 0.1056 | 0.1831 | 0.1017 |
| PRESSURE_LONG_EXPANSION_10K | 9994 | 0.4242 | 0.1397 | 0.3323 | 0.1039 | 0.1708 | 0.1074 | 0.1784 | 0.1043 |
| PRESSURE_SYNTH_RAND_KIPP_9K | 8994 | 0.4734 | 0.0654 | 0.3915 | 0.0697 | 0.1384 | 0.0505 | 0.1286 | 0.0416 |
| PRESSURE_SYNTH_RAND_KIPP_FIXED_9K | 8994 | 0.4629 | 0.0682 | 0.3705 | 0.0985 | 0.1390 | 0.0488 | 0.1568 | 0.0243 |

## Randdruck-Spitzen


### PRESSURE_LONG_STABLE_10K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4607 | 0.9999 | tragend_unruhig | dio_04db | dio_mcm_episode_0qxnyfq | 0.3457 | 0.3964 | 0.4244 | 0.5655 |
| 3037 | 0.9999 | tragend_unruhig | dio_04c2 | dio_mcm_episode_0vd5xfl | 0.3482 | 0.3930 | 0.4561 | 0.5552 |
| 3461 | 0.9998 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3449 | 0.4141 | 0.3886 | 0.5583 |
| 4306 | 0.9996 | tragend_unruhig | dio_1j51 | dio_mcm_episode_0r7nk4p | 0.3420 | 0.3875 | 0.4330 | 0.5430 |
| 3293 | 0.9993 | tragend_unruhig | dio_17qo | dio_mcm_episode_0r7nk4p | 0.3292 | 0.3911 | 0.3643 | 0.4935 |
| 7257 | 0.9992 | tragend_unruhig | dio_1qbu | dio_mcm_episode_0ze0tw9 | 0.3185 | 0.3879 | 0.2856 | 0.5168 |
| 5750 | 0.9990 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3353 | 0.3782 | 0.4249 | 0.5158 |
| 1238 | 0.9990 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3199 | 0.3870 | 0.3077 | 0.5021 |
| 5213 | 0.9989 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3385 | 0.3722 | 0.4636 | 0.5111 |
| 6646 | 0.9988 | tragend_unruhig | dio_1eqa | dio_mcm_episode_16da5fv | 0.3091 | 0.3829 | 0.2231 | 0.5153 |

### PRESSURE_LONG_STRESS_10K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2314 | 0.9999 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0r7nk4p | 0.3388 | 0.4078 | 0.3668 | 0.5477 |
| 7583 | 0.9998 | tragend_unruhig | dio_17wz | dio_mcm_episode_0r7nk4p | 0.3435 | 0.4042 | 0.4035 | 0.5449 |
| 4267 | 0.9997 | tragend_unruhig | dio_0khz | dio_mcm_episode_1318m49 | 0.3357 | 0.4056 | 0.3521 | 0.5422 |
| 2406 | 0.9996 | tragend_unruhig | dio_1j51 | dio_mcm_episode_0r7nk4p | 0.3422 | 0.3834 | 0.4467 | 0.5390 |
| 9746 | 0.9994 | tragend_unruhig | dio_0jqs | dio_mcm_episode_0ze0tw9 | 0.3245 | 0.3924 | 0.3005 | 0.5467 |
| 5115 | 0.9990 | tragend_unruhig | dio_15yz | dio_mcm_episode_0ezbiel | 0.3234 | 0.3826 | 0.3420 | 0.4979 |
| 8900 | 0.9988 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1vv5pwy | 0.3193 | 0.3791 | 0.4726 | 0.5192 |
| 8804 | 0.9985 | tragend_unruhig | dio_0s9i | dio_mcm_episode_14p9ds2 | 0.2988 | 0.4114 | 0.0888 | 0.5052 |
| 2353 | 0.9984 | tragend_unruhig | dio_17qo | dio_mcm_episode_0db8j50 | 0.3250 | 0.3714 | 0.3889 | 0.4813 |
| 4026 | 0.9981 | tragend_unruhig | dio_1qal | dio_mcm_episode_1121lk2 | 0.3046 | 0.3744 | 0.2245 | 0.5055 |

### PRESSURE_LONG_EXPANSION_10K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2314 | 0.9998 | tragend_unruhig | dio_0rdh | dio_mcm_episode_0pjmsgw | 0.3360 | 0.4154 | 0.3252 | 0.5474 |
| 3089 | 0.9997 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3376 | 0.4059 | 0.3595 | 0.5521 |
| 2465 | 0.9995 | tragend_unruhig | dio_1911 | dio_mcm_episode_0r7nk4p | 0.3476 | 0.3992 | 0.4474 | 0.5383 |
| 2448 | 0.9993 | tragend_unruhig | dio_1gxb | dio_mcm_episode_16da5fv | 0.3219 | 0.4094 | 0.2407 | 0.5369 |
| 386 | 0.9988 | tragend_unruhig | dio_00vf | dio_mcm_episode_11n7g5f | 0.3218 | 0.3950 | 0.2696 | 0.5530 |
| 7063 | 0.9987 | tragend_unruhig | dio_1qbu | dio_mcm_episode_11d7ugg | 0.3271 | 0.3937 | 0.3314 | 0.5221 |
| 307 | 0.9987 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3245 | 0.3957 | 0.3073 | 0.5208 |
| 4446 | 0.9987 | tragend_unruhig | dio_150j | dio_mcm_episode_11d7ugg | 0.3277 | 0.3941 | 0.3422 | 0.5125 |
| 653 | 0.9987 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3226 | 0.4042 | 0.2853 | 0.4962 |
| 4443 | 0.9986 | tragend_unruhig | dio_0myo | dio_mcm_episode_16da5fv | 0.3138 | 0.3981 | 0.2058 | 0.5435 |

### PRESSURE_SYNTH_RAND_KIPP_9K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 500 | 0.9999 | tragend_unruhig | dio_03rd | dio_mcm_episode_16da5fv | 0.3319 | 0.4285 | 0.2454 | 0.5282 |
| 1400 | 0.9999 | tragend_unruhig | dio_12zj | dio_mcm_episode_07rozva | 0.3264 | 0.4164 | 0.2485 | 0.5472 |
| 7800 | 0.9998 | tragend_unruhig | dio_0y3b | dio_mcm_episode_19fc32i | 0.3060 | 0.4306 | 0.0324 | 0.5609 |
| 8700 | 0.9997 | tragend_unruhig | dio_0owd | dio_mcm_episode_16da5fv | 0.3043 | 0.3885 | 0.2135 | 0.4553 |
| 6600 | 0.9996 | stabil | dio_1esj | dio_mcm_episode_0hgmxfc | 0.2866 | 0.3667 | 0.1516 | 0.4379 |
| 1401 | 0.9995 | stabil | dio_1adq | dio_mcm_episode_0m1vsbx | 0.2838 | 0.3522 | 0.1815 | 0.4128 |
| 2425 | 0.9988 | tragend_unruhig | dio_16i6 | dio_mcm_episode_0x60uui | 0.2800 | 0.2689 | 0.3984 | 0.3405 |
| 2535 | 0.9987 | stabil | dio_16i6 | dio_mcm_episode_1yxc2ug | 0.2649 | 0.2810 | 0.3973 | 0.3564 |
| 2824 | 0.9985 | stabil | dio_16i6 | dio_mcm_episode_1yxc2ug | 0.2761 | 0.2754 | 0.4170 | 0.3555 |
| 7300 | 0.9984 | stabil | dio_1wge | dio_mcm_episode_09d5qs9 | 0.2579 | 0.3083 | 0.1487 | 0.3349 |

### PRESSURE_SYNTH_RAND_KIPP_FIXED_9K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1400 | 0.9999 | tragend_unruhig | dio_1rc5 | dio_mcm_episode_0ptme5v | 0.3425 | 0.4221 | 0.3375 | 0.5779 |
| 7800 | 0.9999 | tragend_unruhig | dio_1xxt | dio_mcm_episode_19gxzdb | 0.3619 | 0.4052 | 0.4661 | 0.5948 |
| 500 | 0.9992 | tragend_unruhig | dio_0dyg | dio_mcm_episode_19fc32i | 0.3116 | 0.4465 | 0.0421 | 0.5535 |
| 2425 | 0.9974 | tragend_unruhig | dio_0vxu | dio_mcm_episode_02ntbi9 | 0.2735 | 0.2509 | 0.4740 | 0.2292 |
| 2590 | 0.9966 | tragend_unruhig | dio_0rin | dio_mcm_episode_02ntbi9 | 0.2738 | 0.2387 | 0.5151 | 0.2124 |
| 1401 | 0.9944 | stabil | dio_17xs | dio_mcm_episode_0lrw6my | 0.2622 | 0.2789 | 0.2478 | 0.3428 |
| 8700 | 0.9941 | stabil | dio_016z | dio_mcm_episode_0c05m49 | 0.2592 | 0.3428 | 0.0375 | 0.3958 |
| 1759 | 0.9935 | tragend_unruhig | dio_1w0r | dio_mcm_episode_1rph1m4 | 0.2799 | 0.1979 | 0.6385 | 0.2333 |
| 1883 | 0.9935 | tragend_unruhig | dio_09vz | dio_mcm_episode_0kow7o8 | 0.3098 | 0.1906 | 0.9552 | 0.1084 |
| 7801 | 0.9925 | tragend_unruhig | dio_0npu | dio_mcm_episode_0f95qzt | 0.2694 | 0.2581 | 0.3985 | 0.2293 |

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
