# Weltrelative Topologie-Matrix

Stand: 2026-07-01 05:12:22

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
| SOL_2024_5M | 1994 | gemischte_rollenordnung | 0.7543 | 0.2372 | 0.0085 | 0.2497 | 0.6925 | 0.5107 | 0.1568 | 0.8372 |
| BTC_2024_5M | 1994 | gemischte_rollenordnung | 0.7934 | 0.1976 | 0.0090 | 0.2497 | 0.6949 | 0.5132 | 0.1545 | 0.8411 |
| KAS_2024_5M | 1994 | gemischte_rollenordnung | 0.7783 | 0.2131 | 0.0085 | 0.2503 | 0.6932 | 0.5107 | 0.1557 | 0.8396 |
| PAXG_2024_5M | 9994 | stark_zentriert_wenig_rand | 0.8474 | 0.1497 | 0.0029 | 0.2457 | 0.7147 | 0.5403 | 0.1482 | 0.8523 |
| DOGE_2024_5M | 9994 | gemischte_rollenordnung | 0.7963 | 0.1968 | 0.0069 | 0.2493 | 0.7050 | 0.5372 | 0.1526 | 0.8413 |
| XRP_2024_5M | 9994 | gemischte_rollenordnung | 0.7960 | 0.1958 | 0.0082 | 0.2495 | 0.7054 | 0.5376 | 0.1521 | 0.8419 |
| STRESS_2024_5M | 9994 | stark_zentriert_wenig_rand | 0.8029 | 0.1907 | 0.0064 | 0.2495 | 0.7052 | 0.5375 | 0.1524 | 0.8421 |
| EXPANSION_2023_5M | 9994 | gemischte_rollenordnung | 0.7915 | 0.2003 | 0.0082 | 0.2489 | 0.7049 | 0.5367 | 0.1527 | 0.8415 |
| SIDEWAYS_2024_5M | 9994 | gemischte_rollenordnung | 0.7776 | 0.2174 | 0.0050 | 0.2502 | 0.7041 | 0.5369 | 0.1533 | 0.8395 |
| SYNTH_BRUCH_RAND | 5994 | stark_zentriert_wenig_rand | 0.9531 | 0.0464 | 0.0005 | 0.2492 | 0.7459 | 0.5981 | 0.1249 | 0.9041 |
| SYNTH_HARMONIE | 5394 | stark_zentriert_wenig_rand | 0.9993 | 0.0006 | 0.0002 | 0.2501 | 0.7570 | 0.6173 | 0.1191 | 0.9169 |
| SYNTH_RAND_DOMINANZ | 6994 | stark_zentriert_wenig_rand | 0.9312 | 0.0681 | 0.0007 | 0.2501 | 0.7410 | 0.5906 | 0.1296 | 0.8971 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOL_2024_5M | zentrum_stabil | 0.7543 | 0.7041 | 0.5244 | 0.1440 | 0.8576 | 0.3318 | 0.0858 | dio_mcm_episode_1joiyc3 | dio_104t |
| SOL_2024_5M | offene_variante | 0.2372 | 0.6603 | 0.4728 | 0.1923 | 0.7785 | 0.0000 | 0.7463 | dio_mcm_episode_1joiyc3 | dio_00ja |
| SOL_2024_5M | spannungsrand_kippnaehe | 0.0085 | 0.5676 | 0.3505 | 0.3018 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_19yo |
| BTC_2024_5M | zentrum_stabil | 0.7934 | 0.7056 | 0.5267 | 0.1431 | 0.8587 | 0.3148 | 0.1056 | dio_mcm_episode_1joiyc3 | dio_104t |
| BTC_2024_5M | offene_variante | 0.1976 | 0.6576 | 0.4664 | 0.1934 | 0.7788 | 0.0025 | 0.7970 | dio_mcm_episode_1joiyc3 | dio_0jkk |
| BTC_2024_5M | spannungsrand_kippnaehe | 0.0090 | 0.5720 | 0.3549 | 0.2989 | 0.6658 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_1x3j |
| KAS_2024_5M | zentrum_stabil | 0.7783 | 0.7036 | 0.5231 | 0.1441 | 0.8578 | 0.3215 | 0.0986 | dio_mcm_episode_1joiyc3 | dio_104t |
| KAS_2024_5M | offene_variante | 0.2131 | 0.6601 | 0.4715 | 0.1923 | 0.7801 | 0.0000 | 0.7741 | dio_mcm_episode_1joiyc3 | dio_00ja |
| KAS_2024_5M | spannungsrand_kippnaehe | 0.0085 | 0.5719 | 0.3552 | 0.2960 | 0.6686 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_16i6 |
| PAXG_2024_5M | zentrum_stabil | 0.8474 | 0.7223 | 0.5497 | 0.1405 | 0.8645 | 0.2946 | 0.1377 | dio_mcm_episode_0ybr5e3 | dio_104t |
| PAXG_2024_5M | offene_variante | 0.1497 | 0.6742 | 0.4907 | 0.1890 | 0.7864 | 0.0027 | 0.8717 | dio_mcm_episode_0ybr5e3 | dio_00ja |
| PAXG_2024_5M | spannungsrand_kippnaehe | 0.0029 | 0.5761 | 0.3512 | 0.2945 | 0.6838 | 0.0000 | 1.0000 | dio_mcm_episode_0ybr5e3 | dio_19v1 |
| DOGE_2024_5M | zentrum_stabil | 0.7963 | 0.7152 | 0.5496 | 0.1420 | 0.8589 | 0.3138 | 0.0994 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE_2024_5M | offene_variante | 0.1968 | 0.6684 | 0.4933 | 0.1906 | 0.7765 | 0.0010 | 0.8332 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE_2024_5M | spannungsrand_kippnaehe | 0.0069 | 0.5711 | 0.3561 | 0.2997 | 0.6600 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1c6r |
| XRP_2024_5M | zentrum_stabil | 0.7960 | 0.7159 | 0.5504 | 0.1410 | 0.8599 | 0.3140 | 0.0972 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP_2024_5M | offene_variante | 0.1958 | 0.6683 | 0.4932 | 0.1910 | 0.7766 | 0.0005 | 0.8401 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP_2024_5M | spannungsrand_kippnaehe | 0.0082 | 0.5706 | 0.3625 | 0.3007 | 0.6509 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |
| STRESS_2024_5M | zentrum_stabil | 0.8029 | 0.7152 | 0.5499 | 0.1419 | 0.8591 | 0.3113 | 0.1016 | dio_mcm_episode_0b7nep9 | dio_104t |
| STRESS_2024_5M | offene_variante | 0.1907 | 0.6673 | 0.4913 | 0.1916 | 0.7769 | 0.0005 | 0.8499 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| STRESS_2024_5M | spannungsrand_kippnaehe | 0.0064 | 0.5706 | 0.3560 | 0.2987 | 0.6590 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_0ku7 |
| EXPANSION_2023_5M | zentrum_stabil | 0.7915 | 0.7151 | 0.5489 | 0.1418 | 0.8594 | 0.3153 | 0.0982 | dio_mcm_episode_0e7qvj1 | dio_104t |
| EXPANSION_2023_5M | offene_variante | 0.2003 | 0.6700 | 0.4958 | 0.1900 | 0.7781 | 0.0025 | 0.8192 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| EXPANSION_2023_5M | spannungsrand_kippnaehe | 0.0082 | 0.5720 | 0.3625 | 0.2995 | 0.6596 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_17qo |
| SIDEWAYS_2024_5M | zentrum_stabil | 0.7776 | 0.7143 | 0.5490 | 0.1423 | 0.8577 | 0.3216 | 0.0954 | dio_mcm_episode_0b7nep9 | dio_104t |
| SIDEWAYS_2024_5M | offene_variante | 0.2174 | 0.6706 | 0.4975 | 0.1892 | 0.7785 | 0.0009 | 0.7860 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SIDEWAYS_2024_5M | spannungsrand_kippnaehe | 0.0050 | 0.5718 | 0.3588 | 0.2981 | 0.6588 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_15yz |
| SYNTH_BRUCH_RAND | zentrum_stabil | 0.9531 | 0.7494 | 0.6031 | 0.1223 | 0.9096 | 0.2624 | 0.2132 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SYNTH_BRUCH_RAND | offene_variante | 0.0464 | 0.6764 | 0.4994 | 0.1766 | 0.7922 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| SYNTH_BRUCH_RAND | spannungsrand_kippnaehe | 0.0005 | 0.5745 | 0.3195 | 0.3190 | 0.6613 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_0kcg |
| SYNTH_HARMONIE | zentrum_stabil | 0.9993 | 0.7571 | 0.6175 | 0.1190 | 0.9170 | 0.2503 | 0.2495 | dio_mcm_episode_0qvodoj | dio_1fll |
| SYNTH_HARMONIE | offene_variante | 0.0006 | 0.6112 | 0.3802 | 0.2449 | 0.7668 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_0trm |
| SYNTH_HARMONIE | spannungsrand_kippnaehe | 0.0002 | 0.5792 | 0.3456 | 0.2866 | 0.6948 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_13i5 |
| SYNTH_RAND_DOMINANZ | zentrum_stabil | 0.9312 | 0.7468 | 0.5987 | 0.1247 | 0.9066 | 0.2685 | 0.1947 | dio_mcm_episode_08lp0ua | dio_1fll |
| SYNTH_RAND_DOMINANZ | offene_variante | 0.0681 | 0.6632 | 0.4828 | 0.1946 | 0.7693 | 0.0000 | 1.0000 | dio_mcm_episode_14l8khu | dio_1v2w |
| SYNTH_RAND_DOMINANZ | spannungsrand_kippnaehe | 0.0007 | 0.5885 | 0.3400 | 0.2996 | 0.6825 | 0.0000 | 1.0000 | dio_mcm_episode_0r9ht2p | dio_11v0 |

## Lesart

Zentrumsnahe Welten: 5
Gemischte Rollenordnung: 7
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
