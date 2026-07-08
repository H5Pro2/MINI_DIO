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
| PAXG_2025_5M_HOLDOUT | 1994 | 0.4152 | 0.1510 | 0.3561 | 0.0777 | 0.1565 | 0.0911 | 0.1509 | 0.0828 |
| PAXG_2025_15M_HOLDOUT | 1994 | 0.3932 | 0.1700 | 0.3250 | 0.1118 | 0.1639 | 0.1043 | 0.1802 | 0.0983 |
| PAXG_2025_1H_HOLDOUT | 1994 | 0.3977 | 0.1655 | 0.3104 | 0.1264 | 0.1665 | 0.1096 | 0.1819 | 0.1050 |

## Randdruck-Spitzen


### PAXG_2025_5M_HOLDOUT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 18 | 0.9998 | tragend_unruhig | dio_0ind | dio_mcm_episode_16da5fv | 0.3080 | 0.3837 | 0.2442 | 0.4709 |
| 1191 | 0.9997 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3088 | 0.3795 | 0.2554 | 0.4823 |
| 12 | 0.9984 | tragend_unruhig | dio_03h4 | dio_mcm_episode_14p9ds2 | 0.2856 | 0.3657 | 0.1276 | 0.4648 |
| 1240 | 0.9976 | stabil | dio_0ind | dio_mcm_episode_0iwh9d2 | 0.2814 | 0.3791 | 0.2487 | 0.4498 |
| 325 | 0.9972 | stabil | dio_0g0b | dio_mcm_episode_1i3ov0z | 0.2792 | 0.3486 | 0.1284 | 0.4603 |
| 1290 | 0.9965 | tragend_unruhig | dio_0zzl | dio_mcm_episode_16bqw8k | 0.2869 | 0.3218 | 0.2804 | 0.4054 |
| 1725 | 0.9958 | stabil | dio_1lmb | dio_mcm_episode_1rj8742 | 0.2782 | 0.3369 | 0.1991 | 0.3822 |
| 689 | 0.9957 | tragend_unruhig | dio_13zi | dio_mcm_episode_0xg0gjh | 0.2925 | 0.3109 | 0.3613 | 0.3840 |
| 1223 | 0.9947 | stabil | dio_0zac | dio_mcm_episode_1i3ov0z | 0.2568 | 0.3640 | 0.1127 | 0.4393 |
| 33 | 0.9935 | stabil | dio_1r19 | dio_mcm_episode_040m1po | 0.2586 | 0.3187 | 0.0924 | 0.3921 |

### PAXG_2025_15M_HOLDOUT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 413 | 0.9986 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3128 | 0.3902 | 0.2644 | 0.4698 |
| 1557 | 0.9984 | tragend_unruhig | dio_0ku7 | dio_mcm_episode_0v36bqm | 0.3385 | 0.3578 | 0.5060 | 0.4960 |
| 1141 | 0.9978 | tragend_unruhig | dio_1w5j | dio_mcm_episode_16da5fv | 0.2998 | 0.3774 | 0.1958 | 0.4790 |
| 684 | 0.9976 | tragend_unruhig | dio_1c6r | dio_mcm_episode_0ezbiel | 0.3168 | 0.3719 | 0.3393 | 0.4662 |
| 4 | 0.9974 | tragend_unruhig | dio_03h4 | dio_mcm_episode_16da5fv | 0.2992 | 0.3812 | 0.1877 | 0.4679 |
| 1417 | 0.9969 | tragend_unruhig | dio_19yo | dio_mcm_episode_0ezbiel | 0.3097 | 0.3570 | 0.3178 | 0.4705 |
| 1439 | 0.9966 | tragend_unruhig | dio_00hc | dio_mcm_episode_0db8j50 | 0.3190 | 0.3531 | 0.4044 | 0.4569 |
| 397 | 0.9963 | tragend_unruhig | dio_0xvx | dio_mcm_episode_11d7ugg | 0.3110 | 0.3769 | 0.2549 | 0.4710 |
| 1712 | 0.9963 | tragend_unruhig | dio_1txj | dio_mcm_episode_1121lk2 | 0.2968 | 0.3700 | 0.1977 | 0.4710 |
| 1785 | 0.9952 | tragend_unruhig | dio_0jwh | dio_mcm_episode_0ee97be | 0.3400 | 0.3284 | 0.5831 | 0.4557 |

### PAXG_2025_1H_HOLDOUT

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1831 | 1.0000 | tragend_unruhig | dio_179e | dio_mcm_episode_0epbwpm | 0.3308 | 0.4130 | 0.2896 | 0.5511 |
| 1898 | 0.9990 | tragend_unruhig | dio_0pbh | dio_mcm_episode_16da5fv | 0.3059 | 0.3908 | 0.1691 | 0.5380 |
| 1438 | 0.9987 | tragend_unruhig | dio_17qo | dio_mcm_episode_0db8j50 | 0.3138 | 0.3524 | 0.3612 | 0.4662 |
| 896 | 0.9978 | tragend_unruhig | dio_010q | dio_mcm_episode_0xg6rjf | 0.2998 | 0.3675 | 0.2481 | 0.4371 |
| 922 | 0.9974 | tragend_unruhig | dio_00hc | dio_mcm_episode_19yyogk | 0.3089 | 0.3443 | 0.3705 | 0.4302 |
| 1069 | 0.9967 | tragend_unruhig | dio_1eru | dio_mcm_episode_11388rh | 0.3034 | 0.3391 | 0.3344 | 0.4405 |
| 678 | 0.9966 | stabil | dio_0bk5 | dio_mcm_episode_1qlxgj7 | 0.2737 | 0.3731 | 0.0306 | 0.4568 |
| 1456 | 0.9959 | stabil | dio_0n3h | dio_mcm_episode_1qlxgj7 | 0.2711 | 0.3517 | 0.0569 | 0.4699 |
| 1277 | 0.9953 | stabil | dio_0zac | dio_mcm_episode_1qlxgj7 | 0.2741 | 0.3452 | 0.1286 | 0.4143 |
| 1708 | 0.9950 | stabil | dio_1lmb | dio_mcm_episode_1qlxgj7 | 0.2814 | 0.3413 | 0.2074 | 0.3911 |

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
