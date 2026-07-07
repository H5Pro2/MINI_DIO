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
| RAND_REPRO_SOL_STRESS_4000_R2 | 3994 | 0.4044 | 0.1547 | 0.3082 | 0.1327 | 0.1691 | 0.1077 | 0.1882 | 0.1045 |
| RAND_REPRO_SYNTH_RECOUP_8000_R2 | 7994 | 0.4400 | 0.0962 | 0.4067 | 0.0572 | 0.1320 | 0.0407 | 0.1121 | 0.0329 |

## Randdruck-Spitzen


### RAND_REPRO_SOL_STRESS_4000_R2

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 1776 | 0.9997 | tragend_unruhig | dio_1gxb | dio_mcm_episode_0ezbiel | 0.3303 | 0.4171 | 0.2824 | 0.5381 |
| 2558 | 0.9995 | tragend_unruhig | dio_13r8 | dio_mcm_episode_1318m49 | 0.3337 | 0.3978 | 0.3633 | 0.5331 |
| 1173 | 0.9994 | tragend_unruhig | dio_04c2 | dio_mcm_episode_0tw2f7y | 0.3553 | 0.3864 | 0.5144 | 0.5663 |
| 276 | 0.9991 | tragend_unruhig | dio_0ind | dio_mcm_episode_11d7ugg | 0.3257 | 0.4133 | 0.2791 | 0.5043 |
| 2092 | 0.9986 | tragend_unruhig | dio_1v68 | dio_mcm_episode_16da5fv | 0.3141 | 0.3897 | 0.2437 | 0.5224 |
| 1759 | 0.9985 | tragend_unruhig | dio_15yz | dio_mcm_episode_0r7nk4p | 0.3260 | 0.3731 | 0.3821 | 0.4987 |
| 720 | 0.9985 | tragend_unruhig | dio_09vm | dio_mcm_episode_0ezbiel | 0.3207 | 0.3798 | 0.3214 | 0.5117 |
| 2459 | 0.9984 | tragend_unruhig | dio_09vm | dio_mcm_episode_1wep5t1 | 0.3101 | 0.3896 | 0.3764 | 0.5348 |
| 1795 | 0.9975 | tragend_unruhig | dio_0bk5 | dio_mcm_episode_14p9ds2 | 0.2911 | 0.3967 | 0.0650 | 0.5090 |
| 1510 | 0.9972 | tragend_unruhig | dio_0z9q | dio_mcm_episode_0db8j50 | 0.3180 | 0.3540 | 0.3912 | 0.4631 |

### RAND_REPRO_SYNTH_RECOUP_8000_R2

| Tick | Randdruck | Effekt | Symbolfamilie | Preview | Strain | Intake | Visual Gap | Hearing Gap |
|---:|---:|---|---|---|---:|---:|---:|---:|
| 600 | 0.9999 | tragend_unruhig | dio_03rd | dio_mcm_episode_16da5fv | 0.3330 | 0.4345 | 0.2333 | 0.5370 |
| 6100 | 0.9998 | tragend_unruhig | dio_1mgn | dio_mcm_episode_14z8zh1 | 0.3176 | 0.4228 | 0.1267 | 0.5705 |
| 1200 | 0.9997 | tragend_unruhig | dio_1nkp | dio_mcm_episode_14z8zh1 | 0.3151 | 0.4175 | 0.1332 | 0.5529 |
| 6700 | 0.9996 | stabil | dio_00wk | dio_mcm_episode_0mtt9o5 | 0.2879 | 0.3853 | 0.0829 | 0.4904 |
| 4100 | 0.9995 | stabil | dio_11wp | dio_mcm_episode_0hgmxfc | 0.2864 | 0.3702 | 0.1318 | 0.4513 |
| 5500 | 0.9988 | stabil | dio_0o0m | dio_mcm_episode_09d5qs9 | 0.2700 | 0.3314 | 0.1575 | 0.3717 |
| 1847 | 0.9985 | stabil | dio_19v1 | dio_mcm_episode_08q1993 | 0.2833 | 0.2925 | 0.4235 | 0.3833 |
| 1801 | 0.9980 | stabil | dio_19v1 | dio_mcm_episode_0067mkb | 0.2808 | 0.2748 | 0.4573 | 0.3645 |
| 1705 | 0.9979 | tragend_unruhig | dio_19v1 | dio_mcm_episode_0xiz1fq | 0.2681 | 0.2727 | 0.4538 | 0.3655 |
| 1760 | 0.9978 | stabil | dio_19v1 | dio_mcm_episode_0067mkb | 0.2731 | 0.2764 | 0.4452 | 0.3645 |

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
