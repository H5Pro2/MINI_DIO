# Weltrelative Topologie-Matrix

Stand: 2026-07-08 11:27:33

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
| BTC_5M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9866 | 0.0134 | 0.0000 | 0.2493 | 0.7028 | 0.5405 | 0.1687 | 0.8405 |
| BTC_5M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9942 | 0.0058 | 0.0000 | 0.2497 | 0.7031 | 0.5399 | 0.1676 | 0.8420 |
| BTC_5M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9908 | 0.0092 | 0.0000 | 0.2497 | 0.7031 | 0.5398 | 0.1675 | 0.8425 |
| BTC_5M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9886 | 0.0114 | 0.0000 | 0.2501 | 0.7036 | 0.5408 | 0.1673 | 0.8428 |
| BTC_15M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9860 | 0.0140 | 0.0000 | 0.2499 | 0.7025 | 0.5404 | 0.1694 | 0.8392 |
| BTC_15M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9896 | 0.0104 | 0.0000 | 0.2501 | 0.7037 | 0.5418 | 0.1681 | 0.8417 |
| BTC_15M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9866 | 0.0134 | 0.0000 | 0.2491 | 0.7031 | 0.5406 | 0.1684 | 0.8411 |
| BTC_15M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9894 | 0.0106 | 0.0000 | 0.2493 | 0.7039 | 0.5411 | 0.1672 | 0.8429 |
| BTC_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9868 | 0.0132 | 0.0000 | 0.2493 | 0.7035 | 0.5418 | 0.1690 | 0.8405 |
| BTC_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9884 | 0.0116 | 0.0000 | 0.2488 | 0.7019 | 0.5363 | 0.1675 | 0.8413 |
| BTC_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9870 | 0.0130 | 0.0000 | 0.2493 | 0.7047 | 0.5428 | 0.1676 | 0.8428 |
| BTC_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9885 | 0.0115 | 0.0000 | 0.2493 | 0.7031 | 0.5372 | 0.1662 | 0.8435 |
| SOL_5M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9886 | 0.0114 | 0.0000 | 0.2493 | 0.7014 | 0.5391 | 0.1699 | 0.8382 |
| SOL_5M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9898 | 0.0102 | 0.0000 | 0.2491 | 0.7014 | 0.5391 | 0.1700 | 0.8383 |
| SOL_5M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9904 | 0.0096 | 0.0000 | 0.2497 | 0.7018 | 0.5392 | 0.1696 | 0.8396 |
| SOL_5M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9880 | 0.0120 | 0.0000 | 0.2497 | 0.7028 | 0.5395 | 0.1677 | 0.8426 |
| SOL_15M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9880 | 0.0120 | 0.0000 | 0.2499 | 0.7013 | 0.5395 | 0.1709 | 0.8372 |
| SOL_15M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9902 | 0.0098 | 0.0000 | 0.2497 | 0.7023 | 0.5395 | 0.1692 | 0.8401 |
| SOL_15M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9882 | 0.0118 | 0.0000 | 0.2499 | 0.7031 | 0.5406 | 0.1683 | 0.8419 |
| SOL_15M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9878 | 0.0122 | 0.0000 | 0.2491 | 0.7029 | 0.5413 | 0.1688 | 0.8399 |
| SOL_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9884 | 0.0116 | 0.0000 | 0.2497 | 0.7019 | 0.5401 | 0.1700 | 0.8384 |
| SOL_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9897 | 0.0103 | 0.0000 | 0.2499 | 0.7008 | 0.5363 | 0.1688 | 0.8384 |
| SOL_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9860 | 0.0140 | 0.0000 | 0.2493 | 0.7021 | 0.5399 | 0.1700 | 0.8391 |
| SOL_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9888 | 0.0112 | 0.0000 | 0.2499 | 0.7019 | 0.5369 | 0.1678 | 0.8408 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_5M_2024_START | zentrum_stabil | 0.9866 | 0.7045 | 0.5429 | 0.1671 | 0.8429 | 0.2535 | 0.2399 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_5M_2024_START | offene_variante | 0.0134 | 0.5789 | 0.3668 | 0.2856 | 0.6608 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_00hc |
| BTC_5M_2024_FOLLOW | zentrum_stabil | 0.9942 | 0.7038 | 0.5410 | 0.1669 | 0.8429 | 0.2516 | 0.2457 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_5M_2024_FOLLOW | offene_variante | 0.0058 | 0.5801 | 0.3594 | 0.2876 | 0.6756 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1dcc |
| BTC_5M_2025_START | zentrum_stabil | 0.9908 | 0.7043 | 0.5415 | 0.1663 | 0.8442 | 0.2524 | 0.2431 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_5M_2025_START | offene_variante | 0.0092 | 0.5748 | 0.3596 | 0.2948 | 0.6589 | 0.0000 | 1.0000 | dio_mcm_episode_0db8j50 | dio_1nkp |
| BTC_5M_2025_FOLLOW | zentrum_stabil | 0.9886 | 0.7050 | 0.5428 | 0.1659 | 0.8449 | 0.2530 | 0.2414 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_5M_2025_FOLLOW | offene_variante | 0.0114 | 0.5795 | 0.3687 | 0.2847 | 0.6601 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_00hc |
| BTC_15M_2024_START | zentrum_stabil | 0.9860 | 0.7042 | 0.5429 | 0.1678 | 0.8417 | 0.2537 | 0.2394 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2024_START | offene_variante | 0.0140 | 0.5804 | 0.3690 | 0.2842 | 0.6641 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_09vm |
| BTC_15M_2024_FOLLOW | zentrum_stabil | 0.9896 | 0.7051 | 0.5437 | 0.1668 | 0.8436 | 0.2527 | 0.2424 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_15M_2024_FOLLOW | offene_variante | 0.0104 | 0.5773 | 0.3631 | 0.2902 | 0.6683 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_15yz |
| BTC_15M_2025_START | zentrum_stabil | 0.9866 | 0.7048 | 0.5430 | 0.1668 | 0.8435 | 0.2535 | 0.2399 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2025_START | offene_variante | 0.0134 | 0.5753 | 0.3624 | 0.2916 | 0.6598 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_0xvx |
| BTC_15M_2025_FOLLOW | zentrum_stabil | 0.9894 | 0.7052 | 0.5429 | 0.1659 | 0.8448 | 0.2528 | 0.2421 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2025_FOLLOW | offene_variante | 0.0106 | 0.5802 | 0.3690 | 0.2858 | 0.6591 | 0.0000 | 1.0000 | dio_mcm_episode_0v3gsdo | dio_0bgi |
| BTC_1H_2024_START | zentrum_stabil | 0.9868 | 0.7051 | 0.5441 | 0.1674 | 0.8429 | 0.2534 | 0.2403 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_1H_2024_START | offene_variante | 0.0132 | 0.5798 | 0.3678 | 0.2863 | 0.6650 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1j51 |
| BTC_1H_2024_FOLLOW | zentrum_stabil | 0.9884 | 0.7033 | 0.5383 | 0.1661 | 0.8433 | 0.2531 | 0.2413 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_1H_2024_FOLLOW | offene_variante | 0.0116 | 0.5794 | 0.3686 | 0.2893 | 0.6667 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_00hc |
| BTC_1H_2025_START | zentrum_stabil | 0.9870 | 0.7064 | 0.5452 | 0.1660 | 0.8451 | 0.2536 | 0.2402 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_1H_2025_START | offene_variante | 0.0130 | 0.5787 | 0.3651 | 0.2883 | 0.6687 | 0.0000 | 1.0000 | dio_mcm_episode_1121lk2 | dio_0ku7 |
| BTC_1H_2025_FOLLOW | zentrum_stabil | 0.9885 | 0.7046 | 0.5392 | 0.1648 | 0.8456 | 0.2533 | 0.2414 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_1H_2025_FOLLOW | offene_variante | 0.0115 | 0.5764 | 0.3633 | 0.2927 | 0.6655 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_15yz |
| SOL_5M_2024_START | zentrum_stabil | 0.9886 | 0.7028 | 0.5411 | 0.1685 | 0.8402 | 0.2532 | 0.2414 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_5M_2024_START | offene_variante | 0.0114 | 0.5785 | 0.3664 | 0.2867 | 0.6629 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_09vm |
| SOL_5M_2024_FOLLOW | zentrum_stabil | 0.9898 | 0.7027 | 0.5409 | 0.1687 | 0.8401 | 0.2527 | 0.2424 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_5M_2024_FOLLOW | offene_variante | 0.0102 | 0.5780 | 0.3628 | 0.2874 | 0.6698 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1d3j |
| SOL_5M_2025_START | zentrum_stabil | 0.9904 | 0.7030 | 0.5409 | 0.1685 | 0.8413 | 0.2525 | 0.2430 | dio_mcm_episode_12tgchq | dio_104t |
| SOL_5M_2025_START | offene_variante | 0.0096 | 0.5788 | 0.3664 | 0.2860 | 0.6587 | 0.0000 | 1.0000 | dio_mcm_episode_0v3gsdo | dio_0q3j |
| SOL_5M_2025_FOLLOW | zentrum_stabil | 0.9880 | 0.7043 | 0.5416 | 0.1663 | 0.8448 | 0.2531 | 0.2410 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_5M_2025_FOLLOW | offene_variante | 0.0120 | 0.5811 | 0.3669 | 0.2832 | 0.6671 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_04ut |
| SOL_15M_2024_START | zentrum_stabil | 0.9880 | 0.7027 | 0.5416 | 0.1695 | 0.8393 | 0.2531 | 0.2410 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2024_START | offene_variante | 0.0120 | 0.5811 | 0.3688 | 0.2850 | 0.6661 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0xvx |
| SOL_15M_2024_FOLLOW | zentrum_stabil | 0.9902 | 0.7035 | 0.5412 | 0.1680 | 0.8417 | 0.2526 | 0.2427 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2024_FOLLOW | offene_variante | 0.0098 | 0.5794 | 0.3653 | 0.2853 | 0.6696 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_16i6 |
| SOL_15M_2025_START | zentrum_stabil | 0.9882 | 0.7046 | 0.5427 | 0.1669 | 0.8440 | 0.2531 | 0.2411 | dio_mcm_episode_12tgchq | dio_104t |
| SOL_15M_2025_START | offene_variante | 0.0118 | 0.5792 | 0.3661 | 0.2853 | 0.6635 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1eru |
| SOL_15M_2025_FOLLOW | zentrum_stabil | 0.9878 | 0.7045 | 0.5435 | 0.1673 | 0.8422 | 0.2532 | 0.2408 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2025_FOLLOW | offene_variante | 0.0122 | 0.5758 | 0.3625 | 0.2918 | 0.6602 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1lid |
| SOL_1H_2024_START | zentrum_stabil | 0.9884 | 0.7033 | 0.5421 | 0.1687 | 0.8404 | 0.2530 | 0.2413 | dio_mcm_episode_12tgchq | dio_104t |
| SOL_1H_2024_START | offene_variante | 0.0116 | 0.5792 | 0.3655 | 0.2867 | 0.6676 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_19v1 |
| SOL_1H_2024_FOLLOW | zentrum_stabil | 0.9897 | 0.7021 | 0.5381 | 0.1676 | 0.8402 | 0.2527 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_1H_2024_FOLLOW | offene_variante | 0.0103 | 0.5822 | 0.3694 | 0.2820 | 0.6708 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_00hc |
| SOL_1H_2025_START | zentrum_stabil | 0.9860 | 0.7039 | 0.5423 | 0.1683 | 0.8417 | 0.2537 | 0.2394 | dio_mcm_episode_12tgchq | dio_104t |
| SOL_1H_2025_START | offene_variante | 0.0140 | 0.5785 | 0.3682 | 0.2891 | 0.6576 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| SOL_1H_2025_FOLLOW | zentrum_stabil | 0.9888 | 0.7033 | 0.5388 | 0.1664 | 0.8427 | 0.2530 | 0.2416 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_1H_2025_FOLLOW | offene_variante | 0.0112 | 0.5786 | 0.3673 | 0.2902 | 0.6656 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1d3j |

## Lesart

Zentrumsnahe Welten: 24
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
