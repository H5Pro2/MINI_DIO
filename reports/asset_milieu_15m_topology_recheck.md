# Weltrelative Topologie-Matrix

Stand: 2026-07-08 11:15:53

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
| BTC_15M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9860 | 0.0140 | 0.0000 | 0.2499 | 0.7025 | 0.5404 | 0.1694 | 0.8392 |
| BTC_15M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9896 | 0.0104 | 0.0000 | 0.2501 | 0.7037 | 0.5418 | 0.1681 | 0.8417 |
| BTC_15M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9866 | 0.0134 | 0.0000 | 0.2491 | 0.7031 | 0.5406 | 0.1684 | 0.8411 |
| BTC_15M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9894 | 0.0106 | 0.0000 | 0.2493 | 0.7039 | 0.5411 | 0.1672 | 0.8429 |
| SOL_15M_2024_START | 4994 | stark_zentriert_wenig_rand | 0.9880 | 0.0120 | 0.0000 | 0.2499 | 0.7013 | 0.5395 | 0.1709 | 0.8372 |
| SOL_15M_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9902 | 0.0098 | 0.0000 | 0.2497 | 0.7023 | 0.5395 | 0.1692 | 0.8401 |
| SOL_15M_2025_START | 4994 | stark_zentriert_wenig_rand | 0.9882 | 0.0118 | 0.0000 | 0.2499 | 0.7031 | 0.5406 | 0.1683 | 0.8419 |
| SOL_15M_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9878 | 0.0122 | 0.0000 | 0.2491 | 0.7029 | 0.5413 | 0.1688 | 0.8399 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_15M_2024_START | zentrum_stabil | 0.9860 | 0.7042 | 0.5429 | 0.1678 | 0.8417 | 0.2537 | 0.2394 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2024_START | offene_variante | 0.0140 | 0.5804 | 0.3690 | 0.2842 | 0.6641 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_09vm |
| BTC_15M_2024_FOLLOW | zentrum_stabil | 0.9896 | 0.7051 | 0.5437 | 0.1668 | 0.8436 | 0.2527 | 0.2424 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_15M_2024_FOLLOW | offene_variante | 0.0104 | 0.5773 | 0.3631 | 0.2902 | 0.6683 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_15yz |
| BTC_15M_2025_START | zentrum_stabil | 0.9866 | 0.7048 | 0.5430 | 0.1668 | 0.8435 | 0.2535 | 0.2399 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2025_START | offene_variante | 0.0134 | 0.5753 | 0.3624 | 0.2916 | 0.6598 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_0xvx |
| BTC_15M_2025_FOLLOW | zentrum_stabil | 0.9894 | 0.7052 | 0.5429 | 0.1659 | 0.8448 | 0.2528 | 0.2421 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_15M_2025_FOLLOW | offene_variante | 0.0106 | 0.5802 | 0.3690 | 0.2858 | 0.6591 | 0.0000 | 1.0000 | dio_mcm_episode_0v3gsdo | dio_0bgi |
| SOL_15M_2024_START | zentrum_stabil | 0.9880 | 0.7027 | 0.5416 | 0.1695 | 0.8393 | 0.2531 | 0.2410 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2024_START | offene_variante | 0.0120 | 0.5811 | 0.3688 | 0.2850 | 0.6661 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0xvx |
| SOL_15M_2024_FOLLOW | zentrum_stabil | 0.9902 | 0.7035 | 0.5412 | 0.1680 | 0.8417 | 0.2526 | 0.2427 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2024_FOLLOW | offene_variante | 0.0098 | 0.5794 | 0.3653 | 0.2853 | 0.6696 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_16i6 |
| SOL_15M_2025_START | zentrum_stabil | 0.9882 | 0.7046 | 0.5427 | 0.1669 | 0.8440 | 0.2531 | 0.2411 | dio_mcm_episode_12tgchq | dio_104t |
| SOL_15M_2025_START | offene_variante | 0.0118 | 0.5792 | 0.3661 | 0.2853 | 0.6635 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1eru |
| SOL_15M_2025_FOLLOW | zentrum_stabil | 0.9878 | 0.7045 | 0.5435 | 0.1673 | 0.8422 | 0.2532 | 0.2408 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_15M_2025_FOLLOW | offene_variante | 0.0122 | 0.5758 | 0.3625 | 0.2918 | 0.6602 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1lid |

## Lesart

Zentrumsnahe Welten: 8
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
