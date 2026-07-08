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
| BTC_5M_2024_START | 4994 | 0.4065 | 0.1522 | 0.3144 | 0.1270 | 0.1687 | 0.1075 | 0.1796 | 0.1043 |
| BTC_5M_2024_FOLLOW | 4994 | 0.4149 | 0.1518 | 0.3130 | 0.1203 | 0.1676 | 0.1070 | 0.1756 | 0.1030 |
| BTC_5M_2025_START | 4994 | 0.4049 | 0.1634 | 0.3118 | 0.1199 | 0.1675 | 0.1075 | 0.1728 | 0.1041 |
| BTC_5M_2025_FOLLOW | 4994 | 0.4127 | 0.1520 | 0.3160 | 0.1193 | 0.1673 | 0.1061 | 0.1747 | 0.1023 |
| BTC_15M_2024_START | 4994 | 0.4063 | 0.1506 | 0.3100 | 0.1332 | 0.1694 | 0.1079 | 0.1834 | 0.1046 |
| BTC_15M_2024_FOLLOW | 4994 | 0.4119 | 0.1552 | 0.3106 | 0.1223 | 0.1681 | 0.1067 | 0.1777 | 0.1037 |
| BTC_15M_2025_START | 4994 | 0.4105 | 0.1542 | 0.3102 | 0.1252 | 0.1684 | 0.1069 | 0.1790 | 0.1037 |
| BTC_15M_2025_FOLLOW | 4994 | 0.4131 | 0.1518 | 0.3144 | 0.1207 | 0.1672 | 0.1056 | 0.1749 | 0.1022 |
| BTC_1H_2024_START | 4994 | 0.4091 | 0.1532 | 0.3148 | 0.1229 | 0.1690 | 0.1064 | 0.1829 | 0.1037 |
| BTC_1H_2024_FOLLOW | 3778 | 0.4002 | 0.1596 | 0.3107 | 0.1294 | 0.1675 | 0.1059 | 0.1815 | 0.1031 |
| BTC_1H_2025_START | 4994 | 0.4087 | 0.1534 | 0.3080 | 0.1300 | 0.1676 | 0.1040 | 0.1799 | 0.1005 |
| BTC_1H_2025_FOLLOW | 3754 | 0.3998 | 0.1657 | 0.2991 | 0.1353 | 0.1662 | 0.1039 | 0.1790 | 0.1005 |
| SOL_5M_2024_START | 4994 | 0.4077 | 0.1554 | 0.3074 | 0.1296 | 0.1699 | 0.1078 | 0.1879 | 0.1046 |
| SOL_5M_2024_FOLLOW | 4994 | 0.4021 | 0.1620 | 0.3014 | 0.1346 | 0.1700 | 0.1090 | 0.1851 | 0.1063 |
| SOL_5M_2025_START | 4994 | 0.4079 | 0.1576 | 0.3102 | 0.1243 | 0.1696 | 0.1095 | 0.1804 | 0.1071 |
| SOL_5M_2025_FOLLOW | 4994 | 0.4107 | 0.1546 | 0.3144 | 0.1203 | 0.1677 | 0.1085 | 0.1716 | 0.1059 |
| SOL_15M_2024_START | 4994 | 0.4045 | 0.1564 | 0.3094 | 0.1298 | 0.1709 | 0.1101 | 0.1870 | 0.1077 |
| SOL_15M_2024_FOLLOW | 4994 | 0.4131 | 0.1546 | 0.3080 | 0.1243 | 0.1692 | 0.1089 | 0.1796 | 0.1064 |
| SOL_15M_2025_START | 4994 | 0.4105 | 0.1534 | 0.3116 | 0.1245 | 0.1683 | 0.1081 | 0.1749 | 0.1057 |
| SOL_15M_2025_FOLLOW | 4994 | 0.4045 | 0.1554 | 0.3102 | 0.1300 | 0.1688 | 0.1062 | 0.1838 | 0.1031 |
| SOL_1H_2024_START | 4994 | 0.4137 | 0.1478 | 0.3124 | 0.1262 | 0.1700 | 0.1085 | 0.1854 | 0.1061 |
| SOL_1H_2024_FOLLOW | 3778 | 0.4013 | 0.1596 | 0.2957 | 0.1435 | 0.1688 | 0.1061 | 0.1897 | 0.1028 |
| SOL_1H_2025_START | 4994 | 0.4073 | 0.1554 | 0.3052 | 0.1322 | 0.1700 | 0.1082 | 0.1851 | 0.1059 |
| SOL_1H_2025_FOLLOW | 3754 | 0.4049 | 0.1486 | 0.3047 | 0.1417 | 0.1678 | 0.1047 | 0.1862 | 0.1014 |

## Randdruck-Spitzen


### BTC_5M_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2558 | 0.9998 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3428 | 0.4121 | 0.3811 | 0.5548 |
| 1173 | 0.9997 | tragend_unruhig | dio_04db | dio_mcm_episode_0qxnyfq | 0.3452 | 0.4012 | 0.4091 | 0.5665 |
| 1402 | 0.9991 | tragend_unruhig | dio_0rdh | dio_mcm_episode_11d7ugg | 0.3279 | 0.4078 | 0.2825 | 0.5500 |
| 1111 | 0.9989 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3313 | 0.4044 | 0.3360 | 0.5207 |
| 2092 | 0.9987 | tragend_unruhig | dio_1rc5 | dio_mcm_episode_11d7ugg | 0.3262 | 0.4026 | 0.2851 | 0.5484 |
| 2459 | 0.9985 | tragend_unruhig | dio_11et | dio_mcm_episode_0r7nk4p | 0.3370 | 0.3755 | 0.4347 | 0.5303 |
| 3984 | 0.9983 | tragend_unruhig | dio_17qo | dio_mcm_episode_0r7nk4p | 0.3302 | 0.3892 | 0.3700 | 0.5019 |
| 2834 | 0.9982 | tragend_unruhig | dio_09vm | dio_mcm_episode_0pjmsgw | 0.3272 | 0.3874 | 0.3416 | 0.5240 |
| 2734 | 0.9982 | tragend_unruhig | dio_10as | dio_mcm_episode_16da5fv | 0.3096 | 0.3963 | 0.1796 | 0.5378 |
| 803 | 0.9981 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0r7nk4p | 0.3356 | 0.3736 | 0.4372 | 0.5167 |

### BTC_5M_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4378 | 0.9996 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3439 | 0.3767 | 0.4823 | 0.5256 |
| 3347 | 0.9994 | tragend_unruhig | dio_0xvx | dio_mcm_episode_16da5fv | 0.3117 | 0.3893 | 0.2401 | 0.5003 |
| 3366 | 0.9992 | tragend_unruhig | dio_0akm | dio_mcm_episode_16da5fv | 0.3059 | 0.3830 | 0.2022 | 0.5185 |
| 835 | 0.9987 | tragend_unruhig | dio_10as | dio_mcm_episode_14p9ds2 | 0.2965 | 0.3826 | 0.1373 | 0.5081 |
| 4428 | 0.9986 | tragend_unruhig | dio_15yz | dio_mcm_episode_0db8j50 | 0.3247 | 0.3570 | 0.4232 | 0.4770 |
| 3383 | 0.9985 | tragend_unruhig | dio_1ib4 | dio_mcm_episode_1121lk2 | 0.3045 | 0.3719 | 0.2470 | 0.4775 |
| 4684 | 0.9982 | stabil | dio_12ze | dio_mcm_episode_1b57ksv | 0.2859 | 0.3963 | 0.0374 | 0.4968 |
| 989 | 0.9981 | tragend_unruhig | dio_14bq | dio_mcm_episode_14p9ds2 | 0.2888 | 0.3828 | 0.1062 | 0.4699 |
| 758 | 0.9981 | stabil | dio_0bk5 | dio_mcm_episode_1qlxgj7 | 0.2843 | 0.3955 | 0.0201 | 0.5078 |
| 3814 | 0.9978 | tragend_unruhig | dio_1x3j | dio_mcm_episode_16bqw8k | 0.3009 | 0.3617 | 0.2695 | 0.4403 |

### BTC_5M_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2754 | 0.9996 | tragend_unruhig | dio_04db | dio_mcm_episode_0qxnyfq | 0.3434 | 0.3981 | 0.4068 | 0.5615 |
| 4194 | 0.9994 | tragend_unruhig | dio_0qrn | dio_mcm_episode_1318m49 | 0.3373 | 0.4054 | 0.3653 | 0.5421 |
| 2329 | 0.9993 | tragend_unruhig | dio_1kse | dio_mcm_episode_0dl84tz | 0.3472 | 0.4067 | 0.3834 | 0.5601 |
| 1395 | 0.9993 | tragend_unruhig | dio_043c | dio_mcm_episode_11d7ugg | 0.3234 | 0.4062 | 0.2555 | 0.5453 |
| 3906 | 0.9990 | tragend_unruhig | dio_00vf | dio_mcm_episode_11n7g5f | 0.3210 | 0.3963 | 0.2591 | 0.5544 |
| 101 | 0.9989 | tragend_unruhig | dio_1nkp | dio_mcm_episode_16da5fv | 0.3153 | 0.4113 | 0.1906 | 0.5323 |
| 2154 | 0.9981 | tragend_unruhig | dio_15yz | dio_mcm_episode_0db8j50 | 0.3232 | 0.3752 | 0.3608 | 0.4931 |
| 1462 | 0.9980 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3155 | 0.3859 | 0.2774 | 0.5023 |
| 1248 | 0.9980 | tragend_unruhig | dio_1nkp | dio_mcm_episode_00pmn5j | 0.3004 | 0.4214 | 0.2219 | 0.5473 |
| 462 | 0.9975 | tragend_unruhig | dio_0agf | dio_mcm_episode_16da5fv | 0.3042 | 0.3865 | 0.1925 | 0.4974 |

### BTC_5M_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 3292 | 0.9995 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3454 | 0.3772 | 0.4891 | 0.5275 |
| 1578 | 0.9993 | tragend_unruhig | dio_1qbu | dio_mcm_episode_11d7ugg | 0.3242 | 0.3933 | 0.3128 | 0.5188 |
| 1510 | 0.9993 | tragend_unruhig | dio_116p | dio_mcm_episode_0ze0tw9 | 0.3230 | 0.3922 | 0.2919 | 0.5430 |
| 2296 | 0.9989 | tragend_unruhig | dio_0kcg | dio_mcm_episode_16da5fv | 0.3057 | 0.3959 | 0.1799 | 0.4948 |
| 4678 | 0.9988 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3162 | 0.3773 | 0.3090 | 0.4980 |
| 3125 | 0.9985 | tragend_unruhig | dio_1jmw | dio_mcm_episode_16da5fv | 0.3043 | 0.3879 | 0.1943 | 0.4905 |
| 2476 | 0.9984 | tragend_unruhig | dio_1c6r | dio_mcm_episode_11d7ugg | 0.3144 | 0.3735 | 0.3213 | 0.4610 |
| 2314 | 0.9984 | tragend_unruhig | dio_1hew | dio_mcm_episode_14p9ds2 | 0.2966 | 0.3962 | 0.1163 | 0.4954 |
| 757 | 0.9981 | tragend_unruhig | dio_0rme | dio_mcm_episode_0r7nk4p | 0.3255 | 0.3527 | 0.4321 | 0.4900 |
| 457 | 0.9978 | tragend_unruhig | dio_09vm | dio_mcm_episode_0db8j50 | 0.3142 | 0.3541 | 0.3554 | 0.4796 |

### BTC_15M_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 391 | 0.9997 | tragend_unruhig | dio_17wz | dio_mcm_episode_0r7nk4p | 0.3392 | 0.4033 | 0.3749 | 0.5445 |
| 697 | 0.9993 | tragend_unruhig | dio_1qbu | dio_mcm_episode_11d7ugg | 0.3267 | 0.3987 | 0.3106 | 0.5295 |
| 819 | 0.9993 | tragend_unruhig | dio_0380 | dio_mcm_episode_0tw2f7y | 0.3580 | 0.3868 | 0.5347 | 0.5617 |
| 852 | 0.9990 | tragend_unruhig | dio_00vf | dio_mcm_episode_0z4187a | 0.3224 | 0.3926 | 0.2807 | 0.5518 |
| 467 | 0.9980 | tragend_unruhig | dio_1wm5 | dio_mcm_episode_11d7ugg | 0.3159 | 0.3915 | 0.2796 | 0.4788 |
| 853 | 0.9980 | tragend_unruhig | dio_05vj | dio_mcm_episode_0r7nk4p | 0.3472 | 0.3625 | 0.5450 | 0.5200 |
| 1498 | 0.9979 | tragend_unruhig | dio_09vm | dio_mcm_episode_1wep5t1 | 0.3134 | 0.3874 | 0.3833 | 0.5322 |
| 4259 | 0.9975 | tragend_unruhig | dio_00vf | dio_mcm_episode_0ze0tw9 | 0.3010 | 0.3964 | 0.2924 | 0.5468 |
| 3590 | 0.9975 | tragend_unruhig | dio_1w5j | dio_mcm_episode_16da5fv | 0.3055 | 0.3834 | 0.2130 | 0.4935 |
| 4182 | 0.9973 | tragend_unruhig | dio_1hew | dio_mcm_episode_16da5fv | 0.3047 | 0.3888 | 0.2051 | 0.4762 |

### BTC_15M_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4967 | 1.0000 | tragend_unruhig | dio_04db | dio_mcm_episode_0qxnyfq | 0.3413 | 0.4065 | 0.3734 | 0.5605 |
| 3759 | 0.9995 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3350 | 0.3927 | 0.3864 | 0.5185 |
| 3842 | 0.9994 | tragend_unruhig | dio_09vm | dio_mcm_episode_0db8j50 | 0.3258 | 0.3902 | 0.3274 | 0.5205 |
| 3714 | 0.9991 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3193 | 0.4044 | 0.2514 | 0.5098 |
| 1000 | 0.9989 | tragend_unruhig | dio_00vt | dio_mcm_episode_11d7ugg | 0.3175 | 0.3952 | 0.2749 | 0.4892 |
| 3308 | 0.9985 | tragend_unruhig | dio_1v68 | dio_mcm_episode_16da5fv | 0.3091 | 0.3858 | 0.2100 | 0.5331 |
| 4650 | 0.9984 | tragend_unruhig | dio_15yz | dio_mcm_episode_1wep5t1 | 0.3110 | 0.3877 | 0.4016 | 0.5145 |
| 598 | 0.9983 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3141 | 0.3876 | 0.2794 | 0.4743 |
| 4141 | 0.9981 | tragend_unruhig | dio_1das | dio_mcm_episode_0db8j50 | 0.3212 | 0.3713 | 0.3657 | 0.4763 |
| 3841 | 0.9975 | tragend_unruhig | dio_1oub | dio_mcm_episode_0db8j50 | 0.3196 | 0.3566 | 0.3972 | 0.4627 |

### BTC_15M_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 776 | 0.9998 | tragend_unruhig | dio_1911 | dio_mcm_episode_0tw2f7y | 0.3515 | 0.4019 | 0.4598 | 0.5515 |
| 918 | 0.9996 | tragend_unruhig | dio_04c2 | dio_mcm_episode_0tw2f7y | 0.3540 | 0.3958 | 0.4847 | 0.5636 |
| 1542 | 0.9991 | tragend_unruhig | dio_1rc5 | dio_mcm_episode_11d7ugg | 0.3240 | 0.4003 | 0.2737 | 0.5498 |
| 622 | 0.9985 | tragend_unruhig | dio_17qo | dio_mcm_episode_0ezbiel | 0.3252 | 0.3916 | 0.3277 | 0.5033 |
| 4086 | 0.9983 | tragend_unruhig | dio_1j51 | dio_mcm_episode_1w55blx | 0.3264 | 0.3802 | 0.4959 | 0.5561 |
| 4568 | 0.9975 | tragend_unruhig | dio_1txj | dio_mcm_episode_16da5fv | 0.3117 | 0.3900 | 0.2437 | 0.4920 |
| 1210 | 0.9975 | tragend_unruhig | dio_1ypl | dio_mcm_episode_14p9ds2 | 0.2973 | 0.3982 | 0.0947 | 0.5273 |
| 465 | 0.9973 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3095 | 0.3906 | 0.2285 | 0.4862 |
| 2266 | 0.9972 | tragend_unruhig | dio_1v68 | dio_mcm_episode_16da5fv | 0.3110 | 0.3837 | 0.2480 | 0.5043 |
| 1851 | 0.9971 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3193 | 0.3775 | 0.3354 | 0.4916 |

### BTC_15M_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4477 | 0.9997 | tragend_unruhig | dio_0qrn | dio_mcm_episode_1318m49 | 0.3380 | 0.4057 | 0.3706 | 0.5408 |
| 2350 | 0.9993 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0r7nk4p | 0.3357 | 0.3856 | 0.4121 | 0.5115 |
| 4870 | 0.9992 | tragend_unruhig | dio_17qo | dio_mcm_episode_0r7nk4p | 0.3323 | 0.3946 | 0.3675 | 0.5103 |
| 2820 | 0.9991 | tragend_unruhig | dio_1jmw | dio_mcm_episode_11d7ugg | 0.3194 | 0.4065 | 0.2515 | 0.5012 |
| 2168 | 0.9990 | tragend_unruhig | dio_0pbh | dio_mcm_episode_16da5fv | 0.3152 | 0.3973 | 0.2219 | 0.5387 |
| 573 | 0.9987 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3282 | 0.3791 | 0.3826 | 0.4987 |
| 3274 | 0.9986 | tragend_unruhig | dio_1hew | dio_mcm_episode_14p9ds2 | 0.3037 | 0.4093 | 0.1234 | 0.5151 |
| 3816 | 0.9982 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3320 | 0.4034 | 0.3175 | 0.5110 |
| 958 | 0.9976 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3148 | 0.3642 | 0.3333 | 0.4850 |
| 1241 | 0.9976 | tragend_unruhig | dio_09vm | dio_mcm_episode_1wep5t1 | 0.3035 | 0.3772 | 0.3695 | 0.5205 |

### BTC_1H_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2210 | 0.9998 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3371 | 0.3932 | 0.3896 | 0.5363 |
| 213 | 0.9998 | tragend_unruhig | dio_17wz | dio_mcm_episode_0tw2f7y | 0.3500 | 0.3916 | 0.4742 | 0.5510 |
| 4678 | 0.9994 | tragend_unruhig | dio_1txj | dio_mcm_episode_16da5fv | 0.3186 | 0.4007 | 0.2477 | 0.5223 |
| 2911 | 0.9989 | tragend_unruhig | dio_1lj1 | dio_mcm_episode_0ezbiel | 0.3223 | 0.3779 | 0.3430 | 0.5020 |
| 2189 | 0.9986 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0db8j50 | 0.3250 | 0.3742 | 0.3816 | 0.4822 |
| 3852 | 0.9985 | tragend_unruhig | dio_1jmw | dio_mcm_episode_16da5fv | 0.3095 | 0.3917 | 0.2278 | 0.4809 |
| 1399 | 0.9982 | tragend_unruhig | dio_1v68 | dio_mcm_episode_11d7ugg | 0.3088 | 0.3787 | 0.2502 | 0.4940 |
| 3134 | 0.9980 | tragend_unruhig | dio_1j51 | dio_mcm_episode_1wep5t1 | 0.3109 | 0.3708 | 0.4383 | 0.5148 |
| 3924 | 0.9979 | tragend_unruhig | dio_1qal | dio_mcm_episode_0ze0tw9 | 0.3074 | 0.3747 | 0.2503 | 0.4953 |
| 1512 | 0.9978 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3083 | 0.3853 | 0.2513 | 0.4583 |

### BTC_1H_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 198 | 0.9992 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3385 | 0.3714 | 0.4679 | 0.5063 |
| 2430 | 0.9990 | tragend_unruhig | dio_0xvx | dio_mcm_episode_16da5fv | 0.3111 | 0.3864 | 0.2430 | 0.5016 |
| 3158 | 0.9989 | tragend_unruhig | dio_15yz | dio_mcm_episode_0ezbiel | 0.3186 | 0.3713 | 0.3450 | 0.4808 |
| 757 | 0.9988 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1wep5t1 | 0.3133 | 0.3774 | 0.4423 | 0.5133 |
| 2370 | 0.9983 | tragend_unruhig | dio_0hw2 | dio_mcm_episode_16da5fv | 0.3070 | 0.3803 | 0.2468 | 0.4677 |
| 1891 | 0.9979 | tragend_unruhig | dio_1v68 | dio_mcm_episode_1121lk2 | 0.3016 | 0.3759 | 0.1847 | 0.5258 |
| 3768 | 0.9979 | tragend_unruhig | dio_1wm5 | dio_mcm_episode_11d7ugg | 0.3076 | 0.3757 | 0.2688 | 0.4605 |
| 1589 | 0.9974 | tragend_unruhig | dio_1c6r | dio_mcm_episode_11d7ugg | 0.3069 | 0.3643 | 0.2921 | 0.4554 |
| 3671 | 0.9973 | tragend_unruhig | dio_0f90 | dio_mcm_episode_0db8j50 | 0.3171 | 0.3468 | 0.4037 | 0.4587 |
| 3726 | 0.9971 | stabil | dio_0s9i | dio_mcm_episode_0icnf2v | 0.2892 | 0.3951 | 0.0786 | 0.4744 |

### BTC_1H_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1021 | 0.9993 | tragend_unruhig | dio_19yo | dio_mcm_episode_07rozva | 0.3169 | 0.3965 | 0.2482 | 0.5149 |
| 462 | 0.9990 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3229 | 0.3824 | 0.3384 | 0.5080 |
| 4555 | 0.9988 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3135 | 0.3845 | 0.2622 | 0.5083 |
| 4141 | 0.9988 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1vv5pwy | 0.3251 | 0.3712 | 0.5047 | 0.5256 |
| 1560 | 0.9986 | tragend_unruhig | dio_11et | dio_mcm_episode_1vv5pwy | 0.3169 | 0.3692 | 0.4771 | 0.5410 |
| 1327 | 0.9983 | tragend_unruhig | dio_15yz | dio_mcm_episode_0db8j50 | 0.3181 | 0.3677 | 0.3510 | 0.4790 |
| 1478 | 0.9982 | tragend_unruhig | dio_11et | dio_mcm_episode_0v36bqm | 0.3332 | 0.3558 | 0.4635 | 0.5139 |
| 229 | 0.9980 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3306 | 0.3567 | 0.4598 | 0.4848 |
| 623 | 0.9980 | tragend_unruhig | dio_1c6r | dio_mcm_episode_11d7ugg | 0.3259 | 0.3799 | 0.3467 | 0.4812 |
| 2974 | 0.9975 | tragend_unruhig | dio_10as | dio_mcm_episode_14p9ds2 | 0.2938 | 0.3773 | 0.1369 | 0.4984 |

### BTC_1H_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 659 | 0.9996 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3458 | 0.3778 | 0.4918 | 0.5267 |
| 412 | 0.9994 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3281 | 0.3817 | 0.3753 | 0.4996 |
| 1789 | 0.9992 | tragend_unruhig | dio_1oub | dio_mcm_episode_0r7nk4p | 0.3324 | 0.3813 | 0.4147 | 0.4890 |
| 2161 | 0.9989 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3161 | 0.3968 | 0.2588 | 0.4912 |
| 3016 | 0.9986 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3184 | 0.3728 | 0.3296 | 0.4991 |
| 3295 | 0.9980 | tragend_unruhig | dio_0rme | dio_mcm_episode_0db8j50 | 0.3234 | 0.3625 | 0.3935 | 0.4916 |
| 242 | 0.9974 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3069 | 0.3752 | 0.2631 | 0.4657 |
| 2783 | 0.9973 | tragend_unruhig | dio_0z9q | dio_mcm_episode_1wep5t1 | 0.3069 | 0.3634 | 0.4407 | 0.4955 |
| 3630 | 0.9972 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_1vv5pwy | 0.3131 | 0.3565 | 0.4956 | 0.4975 |
| 3437 | 0.9970 | tragend_unruhig | dio_1qal | dio_mcm_episode_1121lk2 | 0.3013 | 0.3686 | 0.2261 | 0.4870 |

### SOL_5M_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1776 | 0.9997 | tragend_unruhig | dio_1gxb | dio_mcm_episode_0ezbiel | 0.3308 | 0.4171 | 0.2850 | 0.5396 |
| 2558 | 0.9995 | tragend_unruhig | dio_13r8 | dio_mcm_episode_1318m49 | 0.3342 | 0.3986 | 0.3643 | 0.5345 |
| 1173 | 0.9995 | tragend_unruhig | dio_04c2 | dio_mcm_episode_0tw2f7y | 0.3550 | 0.3866 | 0.5107 | 0.5677 |
| 276 | 0.9992 | tragend_unruhig | dio_0ind | dio_mcm_episode_0ezbiel | 0.3263 | 0.4139 | 0.2814 | 0.5062 |
| 4495 | 0.9987 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3385 | 0.3702 | 0.4736 | 0.5028 |
| 720 | 0.9986 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3211 | 0.3807 | 0.3216 | 0.5133 |
| 2092 | 0.9986 | tragend_unruhig | dio_1v68 | dio_mcm_episode_16da5fv | 0.3149 | 0.3901 | 0.2475 | 0.5246 |
| 2459 | 0.9986 | tragend_unruhig | dio_09vm | dio_mcm_episode_1wep5t1 | 0.3101 | 0.3902 | 0.3738 | 0.5364 |
| 1759 | 0.9985 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3262 | 0.3737 | 0.3803 | 0.5013 |
| 1795 | 0.9977 | tragend_unruhig | dio_0bk5 | dio_mcm_episode_14p9ds2 | 0.2934 | 0.3971 | 0.0792 | 0.5113 |

### SOL_5M_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4597 | 0.9998 | tragend_unruhig | dio_1nkp | dio_mcm_episode_0ptme5v | 0.3348 | 0.4005 | 0.3426 | 0.5516 |
| 4378 | 0.9996 | tragend_unruhig | dio_1xkj | dio_mcm_episode_0tw2f7y | 0.3575 | 0.3827 | 0.5457 | 0.5548 |
| 2791 | 0.9992 | tragend_unruhig | dio_1ib4 | dio_mcm_episode_11d7ugg | 0.3178 | 0.3887 | 0.2980 | 0.4842 |
| 1173 | 0.9989 | tragend_unruhig | dio_1lj1 | dio_mcm_episode_0db8j50 | 0.3244 | 0.3767 | 0.3597 | 0.5042 |
| 947 | 0.9988 | tragend_unruhig | dio_19yo | dio_mcm_episode_16da5fv | 0.3093 | 0.3833 | 0.2467 | 0.4834 |
| 2765 | 0.9984 | tragend_unruhig | dio_0xvx | dio_mcm_episode_1121lk2 | 0.3067 | 0.3784 | 0.2408 | 0.4873 |
| 4342 | 0.9980 | tragend_unruhig | dio_1qal | dio_mcm_episode_0ze0tw9 | 0.3073 | 0.3715 | 0.2727 | 0.4715 |
| 652 | 0.9979 | tragend_unruhig | dio_17qo | dio_mcm_episode_0db8j50 | 0.3240 | 0.3573 | 0.4245 | 0.4645 |
| 862 | 0.9978 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3024 | 0.3806 | 0.2159 | 0.4650 |
| 2904 | 0.9971 | tragend_unruhig | dio_03bp | dio_mcm_episode_0ze0tw9 | 0.3036 | 0.3624 | 0.2792 | 0.4563 |

### SOL_5M_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4194 | 0.9999 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3457 | 0.4171 | 0.3832 | 0.5646 |
| 2329 | 0.9995 | tragend_unruhig | dio_17wz | dio_mcm_episode_0r7nk4p | 0.3457 | 0.3934 | 0.4442 | 0.5450 |
| 2754 | 0.9994 | tragend_unruhig | dio_01vc | dio_mcm_episode_0r7nk4p | 0.3372 | 0.3986 | 0.3750 | 0.5417 |
| 4454 | 0.9994 | tragend_unruhig | dio_19mz | dio_mcm_episode_11n7g5f | 0.3363 | 0.4077 | 0.3456 | 0.5522 |
| 3899 | 0.9992 | tragend_unruhig | dio_080m | dio_mcm_episode_0pjmsgw | 0.3266 | 0.3965 | 0.2949 | 0.5479 |
| 3630 | 0.9990 | tragend_unruhig | dio_03iu | dio_mcm_episode_0db8j50 | 0.3395 | 0.3983 | 0.3588 | 0.5443 |
| 3906 | 0.9984 | tragend_unruhig | dio_043c | dio_mcm_episode_163ajqw | 0.3091 | 0.3914 | 0.1785 | 0.5597 |
| 686 | 0.9983 | tragend_unruhig | dio_1qal | dio_mcm_episode_11d7ugg | 0.3160 | 0.3891 | 0.2593 | 0.5241 |
| 2154 | 0.9982 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0ezbiel | 0.3209 | 0.3777 | 0.3495 | 0.4740 |
| 2997 | 0.9982 | tragend_unruhig | dio_0im7 | dio_mcm_episode_0ezbiel | 0.3221 | 0.3709 | 0.3475 | 0.5119 |

### SOL_5M_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1282 | 0.9997 | tragend_unruhig | dio_1rc5 | dio_mcm_episode_0ezbiel | 0.3333 | 0.4105 | 0.3158 | 0.5499 |
| 1883 | 0.9995 | tragend_unruhig | dio_03rd | dio_mcm_episode_07rozva | 0.3249 | 0.4229 | 0.2378 | 0.5208 |
| 2474 | 0.9994 | tragend_unruhig | dio_1eqa | dio_mcm_episode_0pjmsgw | 0.3290 | 0.3912 | 0.3284 | 0.5416 |
| 2405 | 0.9994 | tragend_unruhig | dio_12zj | dio_mcm_episode_07rozva | 0.3233 | 0.4176 | 0.2323 | 0.5318 |
| 3292 | 0.9993 | tragend_unruhig | dio_0im7 | dio_mcm_episode_0qxnyfq | 0.3442 | 0.3832 | 0.4497 | 0.5522 |
| 4678 | 0.9989 | tragend_unruhig | dio_12n7 | dio_mcm_episode_0ze0tw9 | 0.3243 | 0.3905 | 0.3131 | 0.5318 |
| 2776 | 0.9987 | tragend_unruhig | dio_1txj | dio_mcm_episode_11d7ugg | 0.3160 | 0.3937 | 0.2612 | 0.4992 |
| 3955 | 0.9983 | tragend_unruhig | dio_1ypl | dio_mcm_episode_14p9ds2 | 0.3007 | 0.3921 | 0.1377 | 0.5207 |
| 2978 | 0.9976 | tragend_unruhig | dio_1hew | dio_mcm_episode_16da5fv | 0.3001 | 0.3815 | 0.1855 | 0.4806 |
| 4105 | 0.9975 | tragend_unruhig | dio_0bk5 | dio_mcm_episode_14p9ds2 | 0.2941 | 0.3896 | 0.1010 | 0.5124 |

### SOL_15M_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 819 | 0.9995 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3367 | 0.3915 | 0.3925 | 0.5345 |
| 240 | 0.9994 | tragend_unruhig | dio_11et | dio_mcm_episode_0r7nk4p | 0.3332 | 0.3906 | 0.3645 | 0.5429 |
| 4042 | 0.9990 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0r7nk4p | 0.3327 | 0.3894 | 0.3859 | 0.5053 |
| 391 | 0.9990 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0r7nk4p | 0.3369 | 0.3798 | 0.4275 | 0.5227 |
| 4829 | 0.9990 | tragend_unruhig | dio_0ds5 | dio_mcm_episode_14p9ds2 | 0.3023 | 0.4120 | 0.0982 | 0.5251 |
| 913 | 0.9988 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3376 | 0.3756 | 0.4516 | 0.5074 |
| 852 | 0.9985 | tragend_unruhig | dio_03j4 | dio_mcm_episode_0ze0tw9 | 0.3132 | 0.3773 | 0.2618 | 0.5358 |
| 2607 | 0.9982 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3144 | 0.3803 | 0.2964 | 0.4819 |
| 3073 | 0.9980 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3124 | 0.3831 | 0.2816 | 0.4707 |
| 3126 | 0.9973 | tragend_unruhig | dio_0z9q | dio_mcm_episode_1wep5t1 | 0.3070 | 0.3637 | 0.4385 | 0.4933 |

### SOL_15M_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 981 | 0.9998 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0r7nk4p | 0.3409 | 0.3932 | 0.4209 | 0.5267 |
| 4866 | 0.9998 | tragend_unruhig | dio_1lj1 | dio_mcm_episode_0pjmsgw | 0.3305 | 0.3954 | 0.3412 | 0.5315 |
| 3347 | 0.9995 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3219 | 0.4053 | 0.2782 | 0.4943 |
| 1223 | 0.9993 | tragend_unruhig | dio_11et | dio_mcm_episode_0db8j50 | 0.3288 | 0.3786 | 0.3720 | 0.5264 |
| 1933 | 0.9990 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3174 | 0.3921 | 0.2799 | 0.4931 |
| 1723 | 0.9983 | tragend_unruhig | dio_0wna | dio_mcm_episode_16da5fv | 0.3044 | 0.3789 | 0.2364 | 0.4620 |
| 3759 | 0.9982 | tragend_unruhig | dio_1das | dio_mcm_episode_0ezbiel | 0.3148 | 0.3672 | 0.3373 | 0.4652 |
| 4861 | 0.9982 | tragend_unruhig | dio_1oub | dio_mcm_episode_0db8j50 | 0.3234 | 0.3566 | 0.4185 | 0.4711 |
| 1080 | 0.9982 | tragend_unruhig | dio_1yu5 | dio_mcm_episode_11d7ugg | 0.3061 | 0.3770 | 0.2557 | 0.4596 |
| 4650 | 0.9981 | tragend_unruhig | dio_1das | dio_mcm_episode_1wep5t1 | 0.2996 | 0.3798 | 0.3564 | 0.4853 |

### SOL_15M_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 4086 | 0.9997 | tragend_unruhig | dio_04c2 | dio_mcm_episode_0tw2f7y | 0.3589 | 0.3944 | 0.5158 | 0.5739 |
| 918 | 0.9996 | tragend_unruhig | dio_1911 | dio_mcm_episode_0tw2f7y | 0.3537 | 0.4032 | 0.4701 | 0.5550 |
| 1398 | 0.9995 | tragend_unruhig | dio_00vf | dio_mcm_episode_11n7g5f | 0.3287 | 0.4033 | 0.2977 | 0.5558 |
| 1484 | 0.9993 | tragend_unruhig | dio_043c | dio_mcm_episode_163ajqw | 0.3189 | 0.4040 | 0.2102 | 0.5727 |
| 114 | 0.9987 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3205 | 0.3878 | 0.3165 | 0.4915 |
| 2094 | 0.9984 | tragend_unruhig | dio_1v68 | dio_mcm_episode_1121lk2 | 0.3051 | 0.3770 | 0.2123 | 0.5188 |
| 3831 | 0.9983 | tragend_unruhig | dio_06gq | dio_mcm_episode_11d7ugg | 0.3082 | 0.3713 | 0.2584 | 0.4974 |
| 1210 | 0.9975 | stabil | dio_0bk5 | dio_mcm_episode_1qlxgj7 | 0.2879 | 0.4085 | 0.0112 | 0.5146 |
| 2764 | 0.9974 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3258 | 0.3454 | 0.4605 | 0.4723 |
| 999 | 0.9974 | tragend_unruhig | dio_10as | dio_mcm_episode_14p9ds2 | 0.2921 | 0.3830 | 0.1122 | 0.4976 |

### SOL_15M_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 821 | 0.9998 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0qxnyfq | 0.3421 | 0.4141 | 0.3603 | 0.5706 |
| 272 | 0.9992 | tragend_unruhig | dio_1j51 | dio_mcm_episode_0v36bqm | 0.3470 | 0.3794 | 0.4828 | 0.5495 |
| 1241 | 0.9990 | tragend_unruhig | dio_09vm | dio_mcm_episode_0r7nk4p | 0.3333 | 0.3812 | 0.3980 | 0.5260 |
| 4870 | 0.9989 | tragend_unruhig | dio_1das | dio_mcm_episode_0r7nk4p | 0.3281 | 0.3902 | 0.3533 | 0.5033 |
| 2658 | 0.9988 | tragend_unruhig | dio_043c | dio_mcm_episode_163ajqw | 0.3127 | 0.3946 | 0.2021 | 0.5510 |
| 3816 | 0.9986 | tragend_unruhig | dio_179e | dio_mcm_episode_11d7ugg | 0.3359 | 0.4129 | 0.3010 | 0.5432 |
| 3274 | 0.9985 | tragend_unruhig | dio_17qo | dio_mcm_episode_0r7nk4p | 0.3308 | 0.3761 | 0.4058 | 0.5004 |
| 4477 | 0.9982 | tragend_unruhig | dio_0qrn | dio_mcm_episode_0xq028g | 0.3131 | 0.4040 | 0.3668 | 0.5400 |
| 1294 | 0.9982 | tragend_unruhig | dio_13vm | dio_mcm_episode_11d7ugg | 0.3176 | 0.3871 | 0.2957 | 0.4928 |
| 4714 | 0.9976 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3087 | 0.3905 | 0.2280 | 0.4803 |

### SOL_1H_2024_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 60 | 0.9997 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0r7nk4p | 0.3344 | 0.3879 | 0.3991 | 0.5087 |
| 4057 | 0.9996 | tragend_unruhig | dio_0rme | dio_mcm_episode_0r7nk4p | 0.3317 | 0.3838 | 0.3826 | 0.5223 |
| 4285 | 0.9996 | tragend_unruhig | dio_1qbu | dio_mcm_episode_11d7ugg | 0.3287 | 0.3985 | 0.3281 | 0.5275 |
| 3134 | 0.9990 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0r7nk4p | 0.3323 | 0.3750 | 0.4205 | 0.4998 |
| 4441 | 0.9988 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3301 | 0.3724 | 0.4087 | 0.5044 |
| 2466 | 0.9986 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3197 | 0.3764 | 0.3283 | 0.5017 |
| 3924 | 0.9986 | tragend_unruhig | dio_1v68 | dio_mcm_episode_1121lk2 | 0.3117 | 0.3836 | 0.2432 | 0.5205 |
| 3810 | 0.9985 | tragend_unruhig | dio_17qo | dio_mcm_episode_1wep5t1 | 0.3104 | 0.3984 | 0.3735 | 0.5078 |
| 2412 | 0.9984 | tragend_unruhig | dio_17qo | dio_mcm_episode_0db8j50 | 0.3248 | 0.3715 | 0.3827 | 0.4861 |
| 4678 | 0.9978 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3079 | 0.3833 | 0.2503 | 0.4625 |

### SOL_1H_2024_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 757 | 0.9999 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0r7nk4p | 0.3365 | 0.3852 | 0.4177 | 0.5130 |
| 530 | 0.9993 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3072 | 0.3892 | 0.2262 | 0.4700 |
| 198 | 0.9988 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0db8j50 | 0.3224 | 0.3477 | 0.4299 | 0.4759 |
| 1430 | 0.9979 | tragend_unruhig | dio_0chx | dio_mcm_episode_16bqw8k | 0.2989 | 0.3527 | 0.2779 | 0.4392 |
| 654 | 0.9979 | stabil | dio_0bk5 | dio_mcm_episode_1i3ov0z | 0.2839 | 0.3848 | 0.0549 | 0.4888 |
| 1589 | 0.9976 | tragend_unruhig | dio_1clq | dio_mcm_episode_19z4zgi | 0.2922 | 0.3543 | 0.2231 | 0.4351 |
| 3101 | 0.9971 | tragend_unruhig | dio_07eb | dio_mcm_episode_0f95qzt | 0.3134 | 0.3288 | 0.4351 | 0.4357 |
| 1046 | 0.9969 | stabil | dio_13i5 | dio_mcm_episode_1qlxgj7 | 0.2862 | 0.3609 | 0.1743 | 0.4175 |
| 3109 | 0.9968 | tragend_unruhig | dio_12on | dio_mcm_episode_16bqw8k | 0.2957 | 0.3436 | 0.2862 | 0.4278 |
| 175 | 0.9965 | tragend_unruhig | dio_05cl | dio_mcm_episode_16bqw8k | 0.3004 | 0.3319 | 0.3446 | 0.4236 |

### SOL_1H_2025_START

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1455 | 0.9995 | tragend_unruhig | dio_0jqs | dio_mcm_episode_0epbwpm | 0.3306 | 0.4042 | 0.2957 | 0.5768 |
| 1560 | 0.9993 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0r7nk4p | 0.3372 | 0.3889 | 0.4050 | 0.5279 |
| 3576 | 0.9990 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3404 | 0.3814 | 0.4534 | 0.5136 |
| 2369 | 0.9990 | tragend_unruhig | dio_13r8 | dio_mcm_episode_1318m49 | 0.3296 | 0.3928 | 0.3515 | 0.5246 |
| 1021 | 0.9989 | tragend_unruhig | dio_19yo | dio_mcm_episode_0pjmsgw | 0.3276 | 0.3897 | 0.3345 | 0.5237 |
| 2204 | 0.9988 | tragend_unruhig | dio_02kz | dio_mcm_episode_0r7nk4p | 0.3343 | 0.3775 | 0.4107 | 0.5233 |
| 3912 | 0.9986 | tragend_unruhig | dio_0z9q | dio_mcm_episode_1wep5t1 | 0.3165 | 0.3965 | 0.4050 | 0.5359 |
| 2818 | 0.9981 | tragend_unruhig | dio_09l0 | dio_mcm_episode_11d7ugg | 0.3143 | 0.3976 | 0.2541 | 0.4735 |
| 2594 | 0.9978 | tragend_unruhig | dio_1wm5 | dio_mcm_episode_11d7ugg | 0.3145 | 0.3894 | 0.2761 | 0.4762 |
| 229 | 0.9977 | tragend_unruhig | dio_17qo | dio_mcm_episode_0r7nk4p | 0.3289 | 0.3697 | 0.4165 | 0.4866 |

### SOL_1H_2025_FOLLOW

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 2359 | 0.9993 | tragend_unruhig | dio_1j51 | dio_mcm_episode_1vv5pwy | 0.3173 | 0.3795 | 0.4509 | 0.5346 |
| 412 | 0.9989 | tragend_unruhig | dio_1j51 | dio_mcm_episode_0v36bqm | 0.3360 | 0.3584 | 0.4794 | 0.5101 |
| 2783 | 0.9988 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0ezbiel | 0.3189 | 0.3739 | 0.3465 | 0.4709 |
| 3223 | 0.9984 | tragend_unruhig | dio_0h1f | dio_mcm_episode_1121lk2 | 0.3045 | 0.3743 | 0.2186 | 0.5134 |
| 3295 | 0.9984 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3250 | 0.3527 | 0.4349 | 0.4793 |
| 3174 | 0.9981 | tragend_unruhig | dio_1oub | dio_mcm_episode_0db8j50 | 0.3225 | 0.3559 | 0.4169 | 0.4672 |
| 1096 | 0.9981 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3081 | 0.3743 | 0.2790 | 0.4584 |
| 3366 | 0.9980 | tragend_unruhig | dio_19yo | dio_mcm_episode_11d7ugg | 0.3069 | 0.3677 | 0.2687 | 0.4770 |
| 606 | 0.9974 | tragend_unruhig | dio_116p | dio_mcm_episode_1121lk2 | 0.2986 | 0.3644 | 0.2038 | 0.5103 |
| 3607 | 0.9970 | tragend_unruhig | dio_1yu5 | dio_mcm_episode_19z4zgi | 0.3000 | 0.3713 | 0.2335 | 0.4466 |

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
