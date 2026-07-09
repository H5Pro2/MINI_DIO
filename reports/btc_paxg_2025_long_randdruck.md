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
| PAXG_2025_5M_10K | 9994 | 0.4372 | 0.1167 | 0.3783 | 0.0678 | 0.1517 | 0.1132 | 0.1649 | 0.0744 |
| PAXG_2025_15M_3333 | 3327 | 0.4013 | 0.1614 | 0.3180 | 0.1193 | 0.1652 | 0.1042 | 0.1759 | 0.0982 |
| PAXG_2025_1H_10K | 8754 | 0.4194 | 0.1477 | 0.3308 | 0.1021 | 0.1519 | 0.1052 | 0.1763 | 0.1007 |
| BTC_2025_5M_10K_CURRENT | 9994 | 0.4273 | 0.1350 | 0.3344 | 0.1034 | 0.1698 | 0.1071 | 0.1726 | 0.1034 |
| BTC_2025_15M_3333_CURRENT | 3327 | 0.3989 | 0.1653 | 0.3090 | 0.1268 | 0.1668 | 0.1068 | 0.1783 | 0.1037 |
| BTC_2025_1H_FULL_CURRENT | 8754 | 0.4224 | 0.1393 | 0.3280 | 0.1103 | 0.1691 | 0.1037 | 0.1792 | 0.1002 |

## Randdruck-Spitzen


### PAXG_2025_5M_10K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 8145 | 0.9997 | gespannt | dio_1ghk | dio_mcm_episode_0kvu3mb | 0.3455 | 0.5306 | 0.2530 | 0.3681 |
| 3966 | 0.9993 | kippend | dio_0ilf | dio_mcm_episode_1hdpu9s | 0.3226 | 0.5053 | 0.1494 | 0.3663 |
| 4686 | 0.9993 | gespannt | dio_1ux3 | dio_mcm_episode_0tre8bg | 0.3336 | 0.5017 | 0.2438 | 0.3542 |
| 4317 | 0.9993 | gespannt | dio_11nu | dio_mcm_episode_0feihom | 0.3499 | 0.4811 | 0.3998 | 0.3708 |
| 1191 | 0.9993 | kippend | dio_04u3 | dio_mcm_episode_1hs3jsa | 0.3336 | 0.4949 | 0.2541 | 0.3681 |
| 5137 | 0.9992 | kippend | dio_0a0e | dio_mcm_episode_1hdpu9s | 0.3282 | 0.4855 | 0.2332 | 0.3779 |
| 18 | 0.9992 | gespannt | dio_12x0 | dio_mcm_episode_0tre8bg | 0.3329 | 0.4992 | 0.2434 | 0.3580 |
| 2383 | 0.9988 | kippend | dio_1b4r | dio_mcm_episode_0b7nep9 | 0.3215 | 0.4844 | 0.1919 | 0.3689 |
| 3703 | 0.9986 | gespannt | dio_0n8c | dio_mcm_episode_19m9z8d | 0.3524 | 0.4666 | 0.4643 | 0.3500 |
| 2934 | 0.9985 | kippend | dio_0jpg | dio_mcm_episode_1hdpu9s | 0.3060 | 0.5012 | 0.0431 | 0.3602 |

### PAXG_2025_15M_3333

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 413 | 0.9991 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3127 | 0.3912 | 0.2614 | 0.4695 |
| 1557 | 0.9985 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3325 | 0.3599 | 0.4590 | 0.4946 |
| 4 | 0.9984 | tragend_unruhig | dio_03h4 | dio_mcm_episode_16da5fv | 0.2997 | 0.3823 | 0.1884 | 0.4681 |
| 684 | 0.9981 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0ezbiel | 0.3181 | 0.3737 | 0.3449 | 0.4654 |
| 1712 | 0.9974 | tragend_unruhig | dio_1w5j | dio_mcm_episode_16da5fv | 0.2968 | 0.3711 | 0.1956 | 0.4696 |
| 397 | 0.9972 | tragend_unruhig | dio_0xvx | dio_mcm_episode_16da5fv | 0.3106 | 0.3780 | 0.2500 | 0.4701 |
| 1417 | 0.9972 | tragend_unruhig | dio_19yo | dio_mcm_episode_11d7ugg | 0.3038 | 0.3586 | 0.2734 | 0.4687 |
| 1439 | 0.9971 | tragend_unruhig | dio_00hc | dio_mcm_episode_0db8j50 | 0.3199 | 0.3546 | 0.4081 | 0.4553 |
| 2978 | 0.9970 | tragend_unruhig | dio_09l0 | dio_mcm_episode_19z4zgi | 0.3074 | 0.3820 | 0.2333 | 0.4457 |
| 1322 | 0.9960 | stabil | dio_0bk5 | dio_mcm_episode_1qlxgj7 | 0.2787 | 0.3761 | 0.0559 | 0.4607 |

### PAXG_2025_1H_10K

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 8518 | 0.9997 | gespannt | dio_03rd | dio_mcm_episode_19dxnmz | 0.3303 | 0.4261 | 0.2704 | 0.5191 |
| 1831 | 0.9997 | kippend | dio_1gxb | dio_mcm_episode_1joiyc3 | 0.3274 | 0.4130 | 0.2639 | 0.5503 |
| 6838 | 0.9996 | kippend | dio_1ri1 | dio_mcm_episode_0e7qvj1 | 0.3276 | 0.4041 | 0.2909 | 0.5486 |
| 6789 | 0.9994 | gespannt | dio_1u5q | dio_mcm_episode_0lbg4mm | 0.3619 | 0.3781 | 0.5771 | 0.5705 |
| 6234 | 0.9991 | gespannt | dio_15yz | dio_mcm_episode_0mw7rev | 0.3333 | 0.3753 | 0.4242 | 0.5042 |
| 1898 | 0.9991 | kippend | dio_0pzw | dio_mcm_episode_1joiyc3 | 0.3036 | 0.3901 | 0.1577 | 0.5316 |
| 7174 | 0.9990 | gespannt | dio_17qo | dio_mcm_episode_0mw7rev | 0.3297 | 0.3772 | 0.3936 | 0.5026 |
| 3151 | 0.9989 | kippend | dio_09vm | dio_mcm_episode_0b7nep9 | 0.3273 | 0.3734 | 0.3819 | 0.5136 |
| 5152 | 0.9986 | kippend | dio_0ds5 | dio_mcm_episode_0ykar6i | 0.2931 | 0.4041 | 0.0591 | 0.5138 |
| 4466 | 0.9983 | kippend | dio_14bq | dio_mcm_episode_0ykar6i | 0.2978 | 0.3875 | 0.1588 | 0.4705 |

### BTC_2025_5M_10K_CURRENT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2754 | 0.9997 | tragend_unruhig | dio_04db | dio_mcm_episode_0qxnyfq | 0.3458 | 0.3994 | 0.4192 | 0.5640 |
| 4194 | 0.9996 | tragend_unruhig | dio_19mz | dio_mcm_episode_1318m49 | 0.3376 | 0.4074 | 0.3610 | 0.5446 |
| 1395 | 0.9995 | tragend_unruhig | dio_1gxb | dio_mcm_episode_11d7ugg | 0.3248 | 0.4101 | 0.2554 | 0.5457 |
| 2329 | 0.9995 | tragend_unruhig | dio_17wz | dio_mcm_episode_0dl84tz | 0.3498 | 0.4082 | 0.3969 | 0.5619 |
| 3906 | 0.9993 | tragend_unruhig | dio_1j82 | dio_mcm_episode_163ajqw | 0.3208 | 0.3984 | 0.2500 | 0.5567 |
| 6510 | 0.9991 | tragend_unruhig | dio_116p | dio_mcm_episode_0ze0tw9 | 0.3231 | 0.3908 | 0.2985 | 0.5403 |
| 8292 | 0.9990 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3473 | 0.3735 | 0.5130 | 0.5262 |
| 101 | 0.9989 | tragend_unruhig | dio_10qy | dio_mcm_episode_14p9ds2 | 0.3076 | 0.4150 | 0.1264 | 0.5332 |
| 6578 | 0.9988 | tragend_unruhig | dio_1qbu | dio_mcm_episode_11d7ugg | 0.3233 | 0.3902 | 0.3155 | 0.5172 |
| 2154 | 0.9987 | tragend_unruhig | dio_15yz | dio_mcm_episode_0db8j50 | 0.3266 | 0.3801 | 0.3713 | 0.4958 |

### BTC_2025_15M_3333_CURRENT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 776 | 0.9998 | tragend_unruhig | dio_1911 | dio_mcm_episode_0r7nk4p | 0.3499 | 0.4029 | 0.4478 | 0.5487 |
| 918 | 0.9993 | tragend_unruhig | dio_1911 | dio_mcm_episode_1w55blx | 0.3300 | 0.3963 | 0.4879 | 0.5610 |
| 1542 | 0.9991 | tragend_unruhig | dio_0rdh | dio_mcm_episode_11d7ugg | 0.3229 | 0.4003 | 0.2667 | 0.5477 |
| 622 | 0.9982 | tragend_unruhig | dio_17qo | dio_mcm_episode_0ezbiel | 0.3189 | 0.3921 | 0.2836 | 0.5000 |
| 1210 | 0.9974 | tragend_unruhig | dio_00si | dio_mcm_episode_14p9ds2 | 0.2980 | 0.3990 | 0.0996 | 0.5241 |
| 465 | 0.9970 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3089 | 0.3905 | 0.2264 | 0.4832 |
| 1851 | 0.9968 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3181 | 0.3762 | 0.3317 | 0.4886 |
| 114 | 0.9966 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3127 | 0.3849 | 0.2748 | 0.4757 |
| 1850 | 0.9962 | tragend_unruhig | dio_116p | dio_mcm_episode_1121lk2 | 0.3070 | 0.3708 | 0.2491 | 0.5091 |
| 1646 | 0.9961 | tragend_unruhig | dio_17qo | dio_mcm_episode_1wep5t1 | 0.3117 | 0.3802 | 0.4118 | 0.4958 |

### BTC_2025_1H_FULL_CURRENT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 5412 | 0.9994 | tragend_unruhig | dio_1oub | dio_mcm_episode_0r7nk4p | 0.3297 | 0.3850 | 0.3776 | 0.5016 |
| 6789 | 0.9993 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0r7nk4p | 0.3307 | 0.3843 | 0.3929 | 0.4918 |
| 1021 | 0.9992 | tragend_unruhig | dio_19yo | dio_mcm_episode_0ezbiel | 0.3190 | 0.3937 | 0.2713 | 0.5124 |
| 6650 | 0.9992 | tragend_unruhig | dio_1txj | dio_mcm_episode_16da5fv | 0.3163 | 0.3979 | 0.2336 | 0.5304 |
| 5659 | 0.9991 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1vv5pwy | 0.3292 | 0.3806 | 0.4923 | 0.5279 |
| 7161 | 0.9990 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3178 | 0.3997 | 0.2621 | 0.4936 |
| 462 | 0.9989 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3218 | 0.3803 | 0.3380 | 0.5047 |
| 8016 | 0.9988 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3202 | 0.3755 | 0.3340 | 0.5026 |
| 4555 | 0.9987 | tragend_unruhig | dio_1qal | dio_mcm_episode_0ze0tw9 | 0.3117 | 0.3813 | 0.2593 | 0.5053 |
| 4141 | 0.9986 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1vv5pwy | 0.3272 | 0.3682 | 0.5287 | 0.5229 |

## Lesart

Diese Lupe trennt zwei Ebenen:

```text
Topologie-Matrix: Welche Rolle dominiert im Gesamtbild?
Randdruck-Lupe: Wo entstehen lokale Rand-/Oeffnungsdruecke innerhalb der Welt?
```

Damit kann eine Welt insgesamt zentrumsnah bleiben und trotzdem lokale Randdruckzonen enthalten.
