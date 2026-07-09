# Weltrelative Topologie-Matrix

Stand: 2026-06-19 13:41:57

## Zweck

Diese Diagnose prueft, ob MINI_DIO unter `world_relative` weiterhin eine passive Topologie ausbildet.
Die Topologie wird nicht ueber feste `dio_*`-Namen gelesen.
Gelesen werden Rollenqualitaeten aus Innenfeldwirkung, Rekopplung, Carry, Strain und Sinnes-MCM-Kopplung.

Die Diagnose erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Hierarchie

1. Grundfrage: Bleibt eine Rollen-Topologie sichtbar, wenn die Sinnesaufnahme weltrelativ wird?
2. Unterpruefung: Welche Rollenanteile tragen Zentrum, Rand/Kippnaehe, offene Variante und Rekopplungsnaehe?
3. Folgeschritt: Vergleich gegen ruhigere, laengere und staerker gespannte Welten.

## Kurzbefund

| Welt | Episoden | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| KAS_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8004 | 0.1575 | 0.0421 | 0.2442 | 0.6451 | 0.3963 | 0.1869 | 0.8645 |
| KAS_2024_15M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8004 | 0.1545 | 0.0451 | 0.2462 | 0.6455 | 0.3964 | 0.1863 | 0.8641 |
| KAS_2024_30M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.7894 | 0.1680 | 0.0426 | 0.2487 | 0.6451 | 0.3959 | 0.1866 | 0.8640 |
| KAS_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.7984 | 0.1560 | 0.0456 | 0.2467 | 0.6445 | 0.3940 | 0.1865 | 0.8639 |
| SOL_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8074 | 0.1454 | 0.0471 | 0.2447 | 0.6451 | 0.3966 | 0.1877 | 0.8648 |
| SOL_2024_15M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8059 | 0.1489 | 0.0451 | 0.2462 | 0.6452 | 0.3953 | 0.1860 | 0.8640 |
| SOL_2024_30M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8014 | 0.1605 | 0.0381 | 0.2472 | 0.6460 | 0.3965 | 0.1847 | 0.8646 |
| SOL_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8059 | 0.1515 | 0.0426 | 0.2467 | 0.6451 | 0.3952 | 0.1857 | 0.8636 |
| BTC_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8280 | 0.1324 | 0.0396 | 0.2487 | 0.6470 | 0.3968 | 0.1818 | 0.8656 |
| BTC_2024_15M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8415 | 0.1113 | 0.0471 | 0.2497 | 0.6480 | 0.3963 | 0.1790 | 0.8649 |
| BTC_2024_30M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8220 | 0.1284 | 0.0496 | 0.2492 | 0.6482 | 0.3981 | 0.1803 | 0.8670 |
| BTC_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8119 | 0.1389 | 0.0491 | 0.2503 | 0.6484 | 0.3981 | 0.1797 | 0.8657 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| KAS_2024_5M_2K | zentrum_stabil | 0.8004 | 0.6511 | 0.3977 | 0.1702 | 0.8729 | 0.3095 | 0.0708 | dio_mcm_episode_1t5bcxp | dio_0jsu |
| KAS_2024_5M_2K | offene_variante | 0.1575 | 0.6264 | 0.3921 | 0.2377 | 0.8387 | 0.0127 | 0.9618 | dio_mcm_episode_1t5bcxp | dio_0kdn |
| KAS_2024_5M_2K | spannungsrand_kippnaehe | 0.0421 | 0.6013 | 0.3855 | 0.3155 | 0.8020 | 0.0119 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0bqz |
| KAS_2024_15M_2K | zentrum_stabil | 0.8004 | 0.6521 | 0.3988 | 0.1690 | 0.8734 | 0.3120 | 0.0752 | dio_mcm_episode_1t5bcxp | dio_1370 |
| KAS_2024_15M_2K | offene_variante | 0.1545 | 0.6248 | 0.3886 | 0.2386 | 0.8357 | 0.0032 | 0.9383 | dio_mcm_episode_1t5bcxp | dio_09ol |
| KAS_2024_15M_2K | spannungsrand_kippnaehe | 0.0451 | 0.5993 | 0.3803 | 0.3136 | 0.7975 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1bvf |
| KAS_2024_30M_2K | zentrum_stabil | 0.7894 | 0.6518 | 0.3981 | 0.1687 | 0.8733 | 0.3177 | 0.0597 | dio_mcm_episode_1t5bcxp | dio_12w3 |
| KAS_2024_30M_2K | offene_variante | 0.1680 | 0.6243 | 0.3874 | 0.2384 | 0.8342 | 0.0000 | 0.9552 | dio_mcm_episode_1t5bcxp | dio_0k07 |
| KAS_2024_30M_2K | spannungsrand_kippnaehe | 0.0426 | 0.6028 | 0.3887 | 0.3127 | 0.8078 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0xz7 |
| KAS_2024_1H_2K | zentrum_stabil | 0.7984 | 0.6509 | 0.3956 | 0.1689 | 0.8728 | 0.3116 | 0.0710 | dio_mcm_episode_1t5bcxp | dio_1pgl |
| KAS_2024_1H_2K | offene_variante | 0.1560 | 0.6250 | 0.3883 | 0.2379 | 0.8366 | 0.0064 | 0.9486 | dio_mcm_episode_1t5bcxp | dio_0iah |
| KAS_2024_1H_2K | spannungsrand_kippnaehe | 0.0456 | 0.6001 | 0.3859 | 0.3187 | 0.8008 | 0.0110 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1gkk |
| SOL_2024_5M_2K | zentrum_stabil | 0.8074 | 0.6511 | 0.3982 | 0.1710 | 0.8731 | 0.3087 | 0.0770 | dio_mcm_episode_1t5bcxp | dio_0r0t |
| SOL_2024_5M_2K | offene_variante | 0.1454 | 0.6263 | 0.3917 | 0.2383 | 0.8405 | 0.0034 | 0.9690 | dio_mcm_episode_1t5bcxp | dio_11pe |
| SOL_2024_5M_2K | spannungsrand_kippnaehe | 0.0471 | 0.5999 | 0.3852 | 0.3173 | 0.7983 | 0.0106 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1mae |
| SOL_2024_15M_2K | zentrum_stabil | 0.8059 | 0.6512 | 0.3964 | 0.1688 | 0.8723 | 0.3086 | 0.0753 | dio_mcm_episode_1t5bcxp | dio_1370 |
| SOL_2024_15M_2K | offene_variante | 0.1489 | 0.6267 | 0.3931 | 0.2382 | 0.8388 | 0.0101 | 0.9697 | dio_mcm_episode_1t5bcxp | dio_074v |
| SOL_2024_15M_2K | spannungsrand_kippnaehe | 0.0451 | 0.5988 | 0.3847 | 0.3213 | 0.7988 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0g3g |
| SOL_2024_30M_2K | zentrum_stabil | 0.8014 | 0.6522 | 0.3975 | 0.1669 | 0.8730 | 0.3110 | 0.0688 | dio_mcm_episode_1t5bcxp | dio_10zr |
| SOL_2024_30M_2K | offene_variante | 0.1605 | 0.6258 | 0.3930 | 0.2410 | 0.8393 | 0.0063 | 0.9781 | dio_mcm_episode_1t5bcxp | dio_0vw7 |
| SOL_2024_30M_2K | spannungsrand_kippnaehe | 0.0381 | 0.5994 | 0.3908 | 0.3217 | 0.7944 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_03lp |
| SOL_2024_1H_2K | zentrum_stabil | 0.8059 | 0.6515 | 0.3972 | 0.1687 | 0.8727 | 0.3093 | 0.0778 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| SOL_2024_1H_2K | offene_variante | 0.1515 | 0.6244 | 0.3891 | 0.2395 | 0.8353 | 0.0066 | 0.9570 | dio_mcm_episode_1t5bcxp | dio_0xnb |
| SOL_2024_1H_2K | spannungsrand_kippnaehe | 0.0426 | 0.5980 | 0.3792 | 0.3159 | 0.7920 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1a6h |
| BTC_2024_5M_2K | zentrum_stabil | 0.8280 | 0.6530 | 0.3990 | 0.1658 | 0.8736 | 0.3010 | 0.0963 | dio_mcm_episode_1t5bcxp | dio_1yp1 |
| BTC_2024_5M_2K | offene_variante | 0.1324 | 0.6246 | 0.3871 | 0.2388 | 0.8358 | 0.0076 | 0.9886 | dio_mcm_episode_1t5bcxp | dio_149i |
| BTC_2024_5M_2K | spannungsrand_kippnaehe | 0.0396 | 0.5981 | 0.3839 | 0.3248 | 0.7994 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_17l1 |
| BTC_2024_15M_2K | zentrum_stabil | 0.8415 | 0.6543 | 0.3986 | 0.1624 | 0.8736 | 0.2968 | 0.1097 | dio_mcm_episode_183drjy | dio_1qlh |
| BTC_2024_15M_2K | offene_variante | 0.1113 | 0.6217 | 0.3843 | 0.2421 | 0.8270 | 0.0045 | 0.9955 | dio_mcm_episode_1t5bcxp | dio_15pu |
| BTC_2024_15M_2K | spannungsrand_kippnaehe | 0.0471 | 0.5977 | 0.3843 | 0.3259 | 0.7976 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_06h2 |
| BTC_2024_30M_2K | zentrum_stabil | 0.8220 | 0.6547 | 0.4000 | 0.1626 | 0.8759 | 0.3038 | 0.0891 | dio_mcm_episode_1t5bcxp | dio_0sy1 |
| BTC_2024_30M_2K | offene_variante | 0.1284 | 0.6244 | 0.3896 | 0.2407 | 0.8354 | 0.0039 | 0.9922 | dio_mcm_episode_1t5bcxp | dio_0rco |
| BTC_2024_30M_2K | spannungsrand_kippnaehe | 0.0496 | 0.6008 | 0.3883 | 0.3165 | 0.8013 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1nm6 |
| BTC_2024_1H_2K | zentrum_stabil | 0.8119 | 0.6555 | 0.4003 | 0.1609 | 0.8752 | 0.3082 | 0.0778 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| BTC_2024_1H_2K | offene_variante | 0.1389 | 0.6233 | 0.3874 | 0.2416 | 0.8328 | 0.0000 | 0.9928 | dio_mcm_episode_1t5bcxp | dio_0htq |
| BTC_2024_1H_2K | spannungsrand_kippnaehe | 0.0491 | 0.6031 | 0.3917 | 0.3156 | 0.8028 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1ql1 |

## Lesart

Zentrumsnahe Welten: 12
Gemischte Rollenordnung: 0
Randlastige Welten: 0

Die aktuelle Matrix spricht fuer eine Rollen-Topologie, nicht fuer eine starre geometrische Form.

```text
Zentrum      = stabile Innenfeldwirkung
Rand/Kipp    = lokale Spannung und Bruchnaehe
Offen        = tragende, aber noch nicht fest gereifte Variante
Rekopplung   = Qualitaet, die Zentrum und Uebergang stabilisiert
```

Wichtig: Die numerischen Einteilungen sind Diagnosehilfen.
Sie sind keine Regeln fuer MINI_DIO und keine universellen MCM-Grenzen.

## Wie es weitergeht

Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.
