# Weltrelative Topologie-Matrix

Stand: 2026-06-22 12:48:33

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
| BTC_5M | 1994 | gemischte_rollenordnung | 0.7934 | 0.1976 | 0.0090 | 0.2497 | 0.6949 | 0.5132 | 0.1545 | 0.8411 |
| BTC_1H | 1994 | gemischte_rollenordnung | 0.7914 | 0.1961 | 0.0125 | 0.2497 | 0.6958 | 0.5146 | 0.1552 | 0.8415 |
| SOL_5M | 1994 | gemischte_rollenordnung | 0.7543 | 0.2372 | 0.0085 | 0.2497 | 0.6925 | 0.5107 | 0.1568 | 0.8372 |
| SOL_1H | 1994 | gemischte_rollenordnung | 0.7823 | 0.2101 | 0.0075 | 0.2503 | 0.6934 | 0.5113 | 0.1559 | 0.8392 |
| KAS_5M | 1994 | gemischte_rollenordnung | 0.7783 | 0.2131 | 0.0085 | 0.2503 | 0.6932 | 0.5107 | 0.1557 | 0.8396 |
| KAS_1H | 1994 | gemischte_rollenordnung | 0.7688 | 0.2202 | 0.0110 | 0.2503 | 0.6927 | 0.5108 | 0.1572 | 0.8374 |
| PAXG_5M | 9994 | stark_zentriert_wenig_rand | 0.8474 | 0.1497 | 0.0029 | 0.2457 | 0.7147 | 0.5403 | 0.1482 | 0.8523 |
| PAXG_1H | 8778 | gemischte_rollenordnung | 0.7919 | 0.2020 | 0.0062 | 0.2469 | 0.7045 | 0.5330 | 0.1532 | 0.8408 |
| DOGE_5M | 9994 | gemischte_rollenordnung | 0.7963 | 0.1968 | 0.0069 | 0.2493 | 0.7050 | 0.5372 | 0.1526 | 0.8413 |
| DOGE_1H | 8778 | gemischte_rollenordnung | 0.7959 | 0.1977 | 0.0065 | 0.2498 | 0.7049 | 0.5371 | 0.1531 | 0.8416 |
| XRP_5M | 9994 | gemischte_rollenordnung | 0.7960 | 0.1958 | 0.0082 | 0.2495 | 0.7054 | 0.5376 | 0.1521 | 0.8419 |
| XRP_1H | 8778 | stark_zentriert_wenig_rand | 0.8136 | 0.1781 | 0.0083 | 0.2496 | 0.7060 | 0.5381 | 0.1524 | 0.8435 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_5M | zentrum_stabil | 0.7934 | 0.7056 | 0.5267 | 0.1431 | 0.8587 | 0.3148 | 0.1056 | dio_mcm_episode_1joiyc3 | dio_104t |
| BTC_5M | offene_variante | 0.1976 | 0.6576 | 0.4664 | 0.1934 | 0.7788 | 0.0025 | 0.7970 | dio_mcm_episode_1joiyc3 | dio_0jkk |
| BTC_5M | spannungsrand_kippnaehe | 0.0090 | 0.5720 | 0.3549 | 0.2989 | 0.6658 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_1x3j |
| BTC_1H | zentrum_stabil | 0.7914 | 0.7076 | 0.5295 | 0.1429 | 0.8600 | 0.3156 | 0.0970 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC_1H | offene_variante | 0.1961 | 0.6562 | 0.4646 | 0.1960 | 0.7778 | 0.0026 | 0.8210 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| BTC_1H | spannungsrand_kippnaehe | 0.0125 | 0.5727 | 0.3565 | 0.2973 | 0.6696 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1j51 |
| SOL_5M | zentrum_stabil | 0.7543 | 0.7041 | 0.5244 | 0.1440 | 0.8576 | 0.3318 | 0.0858 | dio_mcm_episode_1joiyc3 | dio_104t |
| SOL_5M | offene_variante | 0.2372 | 0.6603 | 0.4728 | 0.1923 | 0.7785 | 0.0000 | 0.7463 | dio_mcm_episode_1joiyc3 | dio_00ja |
| SOL_5M | spannungsrand_kippnaehe | 0.0085 | 0.5676 | 0.3505 | 0.3018 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_19yo |
| SOL_1H | zentrum_stabil | 0.7823 | 0.7040 | 0.5242 | 0.1445 | 0.8572 | 0.3199 | 0.1038 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL_1H | offene_variante | 0.2101 | 0.6583 | 0.4687 | 0.1933 | 0.7781 | 0.0000 | 0.7685 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| SOL_1H | spannungsrand_kippnaehe | 0.0075 | 0.5716 | 0.3516 | 0.2978 | 0.6681 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |
| KAS_5M | zentrum_stabil | 0.7783 | 0.7036 | 0.5231 | 0.1441 | 0.8578 | 0.3215 | 0.0986 | dio_mcm_episode_1joiyc3 | dio_104t |
| KAS_5M | offene_variante | 0.2131 | 0.6601 | 0.4715 | 0.1923 | 0.7801 | 0.0000 | 0.7741 | dio_mcm_episode_1joiyc3 | dio_00ja |
| KAS_5M | spannungsrand_kippnaehe | 0.0085 | 0.5719 | 0.3552 | 0.2960 | 0.6686 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_16i6 |
| KAS_1H | zentrum_stabil | 0.7688 | 0.7044 | 0.5251 | 0.1443 | 0.8574 | 0.3255 | 0.0939 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS_1H | offene_variante | 0.2202 | 0.6578 | 0.4689 | 0.1948 | 0.7761 | 0.0000 | 0.7585 | dio_mcm_episode_0e7qvj1 | dio_05yg |
| KAS_1H | spannungsrand_kippnaehe | 0.0110 | 0.5691 | 0.3519 | 0.3023 | 0.6692 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_07eb |
| PAXG_5M | zentrum_stabil | 0.8474 | 0.7223 | 0.5497 | 0.1405 | 0.8645 | 0.2946 | 0.1377 | dio_mcm_episode_0ybr5e3 | dio_104t |
| PAXG_5M | offene_variante | 0.1497 | 0.6742 | 0.4907 | 0.1890 | 0.7864 | 0.0027 | 0.8717 | dio_mcm_episode_0ybr5e3 | dio_00ja |
| PAXG_5M | spannungsrand_kippnaehe | 0.0029 | 0.5761 | 0.3512 | 0.2945 | 0.6838 | 0.0000 | 1.0000 | dio_mcm_episode_0ybr5e3 | dio_19v1 |
| PAXG_1H | zentrum_stabil | 0.7919 | 0.7145 | 0.5451 | 0.1426 | 0.8580 | 0.3143 | 0.1011 | dio_mcm_episode_0b7nep9 | dio_104t |
| PAXG_1H | offene_variante | 0.2020 | 0.6693 | 0.4912 | 0.1903 | 0.7789 | 0.0056 | 0.8111 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| PAXG_1H | spannungsrand_kippnaehe | 0.0062 | 0.5717 | 0.3538 | 0.2997 | 0.6565 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_05cl |
| DOGE_5M | zentrum_stabil | 0.7963 | 0.7152 | 0.5496 | 0.1420 | 0.8589 | 0.3138 | 0.0994 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE_5M | offene_variante | 0.1968 | 0.6684 | 0.4933 | 0.1906 | 0.7765 | 0.0010 | 0.8332 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE_5M | spannungsrand_kippnaehe | 0.0069 | 0.5711 | 0.3561 | 0.2997 | 0.6600 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1c6r |
| DOGE_1H | zentrum_stabil | 0.7959 | 0.7155 | 0.5501 | 0.1421 | 0.8594 | 0.3141 | 0.0955 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE_1H | offene_variante | 0.1977 | 0.6667 | 0.4902 | 0.1926 | 0.7760 | 0.0006 | 0.8478 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| DOGE_1H | spannungsrand_kippnaehe | 0.0065 | 0.5724 | 0.3590 | 0.2986 | 0.6599 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_15yz |
| XRP_5M | zentrum_stabil | 0.7960 | 0.7159 | 0.5504 | 0.1410 | 0.8599 | 0.3140 | 0.0972 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP_5M | offene_variante | 0.1958 | 0.6683 | 0.4932 | 0.1910 | 0.7766 | 0.0005 | 0.8401 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP_5M | spannungsrand_kippnaehe | 0.0082 | 0.5706 | 0.3625 | 0.3007 | 0.6509 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |
| XRP_1H | zentrum_stabil | 0.8136 | 0.7166 | 0.5516 | 0.1417 | 0.8607 | 0.3073 | 0.1063 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP_1H | offene_variante | 0.1781 | 0.6638 | 0.4843 | 0.1942 | 0.7738 | 0.0000 | 0.8720 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| XRP_1H | spannungsrand_kippnaehe | 0.0083 | 0.5724 | 0.3631 | 0.3011 | 0.6532 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_17qo |

## Lesart

Zentrumsnahe Welten: 2
Gemischte Rollenordnung: 10
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
