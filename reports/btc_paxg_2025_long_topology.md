# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:12:53

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
| PAXG_2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8725 | 0.1202 | 0.0073 | 0.2473 | 0.7144 | 0.5410 | 0.1517 | 0.8561 |
| PAXG_2025_15M_3333 | 3327 | stark_zentriert_wenig_rand | 0.9922 | 0.0078 | 0.0000 | 0.2459 | 0.7025 | 0.5305 | 0.1652 | 0.8449 |
| PAXG_2025_1H_10K | 8754 | stark_zentriert_wenig_rand | 0.8098 | 0.1857 | 0.0045 | 0.2485 | 0.7061 | 0.5357 | 0.1519 | 0.8437 |
| BTC_2025_5M_10K_CURRENT | 9994 | stark_zentriert_wenig_rand | 0.9902 | 0.0098 | 0.0000 | 0.2495 | 0.7075 | 0.5529 | 0.1698 | 0.8424 |
| BTC_2025_15M_3333_CURRENT | 3327 | stark_zentriert_wenig_rand | 0.9856 | 0.0144 | 0.0000 | 0.2492 | 0.7007 | 0.5328 | 0.1668 | 0.8418 |
| BTC_2025_1H_FULL_CURRENT | 8754 | stark_zentriert_wenig_rand | 0.9897 | 0.0103 | 0.0000 | 0.2488 | 0.7083 | 0.5532 | 0.1691 | 0.8429 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG_2025_5M_10K | zentrum_stabil | 0.8725 | 0.7222 | 0.5513 | 0.1437 | 0.8673 | 0.2866 | 0.1546 | dio_mcm_episode_1hdpu9s | dio_104t |
| PAXG_2025_5M_10K | offene_variante | 0.1202 | 0.6654 | 0.4779 | 0.2008 | 0.7839 | 0.0000 | 0.8976 | dio_mcm_episode_1hdpu9s | dio_00ja |
| PAXG_2025_5M_10K | spannungsrand_kippnaehe | 0.0073 | 0.5819 | 0.3508 | 0.3042 | 0.7091 | 0.0000 | 1.0000 | dio_mcm_episode_1hdpu9s | dio_00hc |
| PAXG_2025_15M_3333 | zentrum_stabil | 0.9922 | 0.7035 | 0.5318 | 0.1643 | 0.8463 | 0.2520 | 0.2442 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_15M_3333 | offene_variante | 0.0078 | 0.5800 | 0.3555 | 0.2899 | 0.6679 | 0.0000 | 1.0000 | dio_mcm_episode_16da5fv | dio_03h4 |
| PAXG_2025_1H_10K | zentrum_stabil | 0.8098 | 0.7154 | 0.5472 | 0.1423 | 0.8595 | 0.3078 | 0.1123 | dio_mcm_episode_0b7nep9 | dio_104t |
| PAXG_2025_1H_10K | offene_variante | 0.1857 | 0.6689 | 0.4902 | 0.1905 | 0.7792 | 0.0043 | 0.8327 | dio_mcm_episode_0b7nep9 | dio_00ja |
| PAXG_2025_1H_10K | spannungsrand_kippnaehe | 0.0045 | 0.5694 | 0.3516 | 0.3023 | 0.6611 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| BTC_2025_5M_10K_CURRENT | zentrum_stabil | 0.9902 | 0.7088 | 0.5547 | 0.1686 | 0.8442 | 0.2525 | 0.2426 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_2025_5M_10K_CURRENT | offene_variante | 0.0098 | 0.5798 | 0.3699 | 0.2869 | 0.6582 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1c6r |
| BTC_2025_15M_3333_CURRENT | zentrum_stabil | 0.9856 | 0.7025 | 0.5353 | 0.1650 | 0.8445 | 0.2537 | 0.2391 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_2025_15M_3333_CURRENT | offene_variante | 0.0144 | 0.5755 | 0.3632 | 0.2920 | 0.6593 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| BTC_2025_1H_FULL_CURRENT | zentrum_stabil | 0.9897 | 0.7097 | 0.5552 | 0.1679 | 0.8448 | 0.2527 | 0.2423 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_2025_1H_FULL_CURRENT | offene_variante | 0.0103 | 0.5775 | 0.3666 | 0.2908 | 0.6608 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0ku7 |

## Lesart

Zentrumsnahe Welten: 6
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
