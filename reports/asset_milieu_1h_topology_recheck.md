# Weltrelative Topologie-Matrix

Stand: 2026-07-08 10:57:08

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
| BTC_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9868 | 0.0132 | 0.0000 | 0.2493 | 0.7035 | 0.5418 | 0.1690 | 0.8405 |
| BTC_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9884 | 0.0116 | 0.0000 | 0.2488 | 0.7019 | 0.5363 | 0.1675 | 0.8413 |
| BTC_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9870 | 0.0130 | 0.0000 | 0.2493 | 0.7047 | 0.5428 | 0.1676 | 0.8428 |
| BTC_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9885 | 0.0115 | 0.0000 | 0.2493 | 0.7031 | 0.5372 | 0.1662 | 0.8435 |
| PAXG_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9876 | 0.0124 | 0.0000 | 0.2457 | 0.7036 | 0.5375 | 0.1684 | 0.8418 |
| PAXG_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9897 | 0.0103 | 0.0000 | 0.2440 | 0.7006 | 0.5320 | 0.1685 | 0.8399 |
| PAXG_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9942 | 0.0058 | 0.0000 | 0.2475 | 0.7038 | 0.5399 | 0.1679 | 0.8420 |
| PAXG_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9896 | 0.0104 | 0.0000 | 0.2493 | 0.7028 | 0.5353 | 0.1654 | 0.8445 |
| XRP_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9864 | 0.0136 | 0.0000 | 0.2489 | 0.7035 | 0.5415 | 0.1687 | 0.8410 |
| XRP_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9876 | 0.0124 | 0.0000 | 0.2501 | 0.7032 | 0.5372 | 0.1659 | 0.8445 |
| XRP_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9844 | 0.0156 | 0.0000 | 0.2495 | 0.7028 | 0.5408 | 0.1694 | 0.8401 |
| XRP_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9893 | 0.0107 | 0.0000 | 0.2493 | 0.7021 | 0.5365 | 0.1670 | 0.8414 |
| DOGE_1H_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9882 | 0.0118 | 0.0000 | 0.2499 | 0.7037 | 0.5413 | 0.1680 | 0.8422 |
| DOGE_1H_2024_FOLLOW | 3778 | stark_zentriert_wenig_rand | 0.9873 | 0.0127 | 0.0000 | 0.2499 | 0.7014 | 0.5358 | 0.1678 | 0.8403 |
| DOGE_1H_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9864 | 0.0136 | 0.0000 | 0.2501 | 0.7029 | 0.5414 | 0.1695 | 0.8399 |
| DOGE_1H_2025_FOLLOW | 3754 | stark_zentriert_wenig_rand | 0.9864 | 0.0136 | 0.0000 | 0.2499 | 0.7017 | 0.5360 | 0.1674 | 0.8410 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_1H_2024_START | zentrum_stabil | 0.9868 | 0.7051 | 0.5441 | 0.1674 | 0.8429 | 0.2534 | 0.2403 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_1H_2024_START | offene_variante | 0.0132 | 0.5798 | 0.3678 | 0.2863 | 0.6650 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1j51 |
| BTC_1H_2024_FOLLOW | zentrum_stabil | 0.9884 | 0.7033 | 0.5383 | 0.1661 | 0.8433 | 0.2531 | 0.2413 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_1H_2024_FOLLOW | offene_variante | 0.0116 | 0.5794 | 0.3686 | 0.2893 | 0.6667 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_00hc |
| BTC_1H_2025_START | zentrum_stabil | 0.9870 | 0.7064 | 0.5452 | 0.1660 | 0.8451 | 0.2536 | 0.2402 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_1H_2025_START | offene_variante | 0.0130 | 0.5787 | 0.3651 | 0.2883 | 0.6687 | 0.0000 | 1.0000 | dio_mcm_episode_1121lk2 | dio_0ku7 |
| BTC_1H_2025_FOLLOW | zentrum_stabil | 0.9885 | 0.7046 | 0.5392 | 0.1648 | 0.8456 | 0.2533 | 0.2414 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_1H_2025_FOLLOW | offene_variante | 0.0115 | 0.5764 | 0.3633 | 0.2927 | 0.6655 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_15yz |
| PAXG_1H_2024_START | zentrum_stabil | 0.9876 | 0.7051 | 0.5396 | 0.1670 | 0.8441 | 0.2532 | 0.2407 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_1H_2024_START | offene_variante | 0.0124 | 0.5815 | 0.3670 | 0.2837 | 0.6618 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_19yo |
| PAXG_1H_2024_FOLLOW | zentrum_stabil | 0.9897 | 0.7018 | 0.5337 | 0.1674 | 0.8416 | 0.2527 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_1H_2024_FOLLOW | offene_variante | 0.0103 | 0.5826 | 0.3688 | 0.2793 | 0.6707 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1lid |
| PAXG_1H_2025_START | zentrum_stabil | 0.9942 | 0.7045 | 0.5409 | 0.1672 | 0.8430 | 0.2516 | 0.2457 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_1H_2025_START | offene_variante | 0.0058 | 0.5808 | 0.3678 | 0.2844 | 0.6669 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_16i6 |
| PAXG_1H_2025_FOLLOW | zentrum_stabil | 0.9896 | 0.7041 | 0.5371 | 0.1641 | 0.8463 | 0.2528 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_1H_2025_FOLLOW | offene_variante | 0.0104 | 0.5778 | 0.3630 | 0.2890 | 0.6690 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_00hc |
| XRP_1H_2024_START | zentrum_stabil | 0.9864 | 0.7052 | 0.5439 | 0.1671 | 0.8435 | 0.2536 | 0.2397 | dio_mcm_episode_1qlxgj7 | dio_104t |
| XRP_1H_2024_START | offene_variante | 0.0136 | 0.5789 | 0.3692 | 0.2892 | 0.6580 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_1c6r |
| XRP_1H_2024_FOLLOW | zentrum_stabil | 0.9876 | 0.7048 | 0.5394 | 0.1643 | 0.8467 | 0.2533 | 0.2407 | dio_mcm_episode_1qlxgj7 | dio_104t |
| XRP_1H_2024_FOLLOW | offene_variante | 0.0124 | 0.5761 | 0.3624 | 0.2918 | 0.6646 | 0.0000 | 1.0000 | dio_mcm_episode_11d7ugg | dio_13r8 |
| XRP_1H_2025_START | zentrum_stabil | 0.9844 | 0.7048 | 0.5436 | 0.1675 | 0.8429 | 0.2541 | 0.2382 | dio_mcm_episode_1qlxgj7 | dio_104t |
| XRP_1H_2025_START | offene_variante | 0.0156 | 0.5784 | 0.3657 | 0.2884 | 0.6645 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_19v1 |
| XRP_1H_2025_FOLLOW | zentrum_stabil | 0.9893 | 0.7035 | 0.5384 | 0.1656 | 0.8434 | 0.2528 | 0.2421 | dio_mcm_episode_1qlxgj7 | dio_104t |
| XRP_1H_2025_FOLLOW | offene_variante | 0.0107 | 0.5752 | 0.3625 | 0.2937 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_05cl |
| DOGE_1H_2024_START | zentrum_stabil | 0.9882 | 0.7052 | 0.5434 | 0.1666 | 0.8444 | 0.2531 | 0.2411 | dio_mcm_episode_12tgchq | dio_104t |
| DOGE_1H_2024_START | offene_variante | 0.0118 | 0.5779 | 0.3653 | 0.2885 | 0.6620 | 0.0000 | 1.0000 | dio_mcm_episode_11d7ugg | dio_19yo |
| DOGE_1H_2024_FOLLOW | zentrum_stabil | 0.9873 | 0.7029 | 0.5379 | 0.1663 | 0.8425 | 0.2534 | 0.2405 | dio_mcm_episode_1qlxgj7 | dio_104t |
| DOGE_1H_2024_FOLLOW | offene_variante | 0.0127 | 0.5838 | 0.3688 | 0.2819 | 0.6712 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0f90 |
| DOGE_1H_2025_START | zentrum_stabil | 0.9864 | 0.7046 | 0.5438 | 0.1678 | 0.8424 | 0.2536 | 0.2397 | dio_mcm_episode_1qlxgj7 | dio_104t |
| DOGE_1H_2025_START | offene_variante | 0.0136 | 0.5768 | 0.3669 | 0.2913 | 0.6574 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_19v1 |
| DOGE_1H_2025_FOLLOW | zentrum_stabil | 0.9864 | 0.7035 | 0.5384 | 0.1657 | 0.8434 | 0.2536 | 0.2398 | dio_mcm_episode_1qlxgj7 | dio_104t |
| DOGE_1H_2025_FOLLOW | offene_variante | 0.0136 | 0.5766 | 0.3650 | 0.2931 | 0.6634 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0z9q |

## Lesart

Zentrumsnahe Welten: 16
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
