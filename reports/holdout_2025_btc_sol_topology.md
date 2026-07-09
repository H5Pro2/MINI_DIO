# Weltrelative Topologie-Matrix

Stand: 2026-07-08 12:26:25

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
| BTC_2025_5M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9880 | 0.0120 | 0.0000 | 0.2497 | 0.6950 | 0.5179 | 0.1658 | 0.8406 |
| BTC_2025_15M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9835 | 0.0165 | 0.0000 | 0.2492 | 0.6971 | 0.5218 | 0.1650 | 0.8427 |
| BTC_2025_30M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9819 | 0.0181 | 0.0000 | 0.2492 | 0.6973 | 0.5224 | 0.1649 | 0.8417 |
| BTC_2025_1H_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9855 | 0.0145 | 0.0000 | 0.2503 | 0.6989 | 0.5238 | 0.1638 | 0.8442 |
| SOL_2025_5M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9870 | 0.0130 | 0.0000 | 0.2497 | 0.6938 | 0.5174 | 0.1673 | 0.8376 |
| SOL_2025_15M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9875 | 0.0125 | 0.0000 | 0.2503 | 0.6979 | 0.5226 | 0.1646 | 0.8448 |
| SOL_2025_30M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9870 | 0.0130 | 0.0000 | 0.2503 | 0.6955 | 0.5188 | 0.1659 | 0.8415 |
| SOL_2025_1H_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9835 | 0.0165 | 0.0000 | 0.2492 | 0.6960 | 0.5202 | 0.1663 | 0.8409 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_2025_5M_HOLDOUT | zentrum_stabil | 0.9880 | 0.6964 | 0.5198 | 0.1643 | 0.8427 | 0.2533 | 0.2411 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_2025_5M_HOLDOUT | offene_variante | 0.0120 | 0.5781 | 0.3598 | 0.2874 | 0.6666 | 0.0000 | 1.0000 | dio_mcm_episode_16da5fv | dio_17qo |
| BTC_2025_15M_HOLDOUT | zentrum_stabil | 0.9835 | 0.6992 | 0.5246 | 0.1628 | 0.8458 | 0.2545 | 0.2376 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_2025_15M_HOLDOUT | offene_variante | 0.0165 | 0.5721 | 0.3586 | 0.2955 | 0.6557 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_0xvx |
| BTC_2025_30M_HOLDOUT | zentrum_stabil | 0.9819 | 0.6995 | 0.5252 | 0.1627 | 0.8450 | 0.2549 | 0.2365 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_2025_30M_HOLDOUT | offene_variante | 0.0181 | 0.5788 | 0.3660 | 0.2872 | 0.6672 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_0ku7 |
| BTC_2025_1H_HOLDOUT | zentrum_stabil | 0.9855 | 0.7007 | 0.5263 | 0.1618 | 0.8468 | 0.2539 | 0.2392 | dio_mcm_episode_1qlxgj7 | dio_104t |
| BTC_2025_1H_HOLDOUT | offene_variante | 0.0145 | 0.5756 | 0.3601 | 0.2935 | 0.6658 | 0.0000 | 1.0000 | dio_mcm_episode_0db8j50 | dio_1w0r |
| SOL_2025_5M_HOLDOUT | zentrum_stabil | 0.9870 | 0.6953 | 0.5194 | 0.1658 | 0.8398 | 0.2536 | 0.2403 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_2025_5M_HOLDOUT | offene_variante | 0.0130 | 0.5837 | 0.3702 | 0.2782 | 0.6743 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0vfj |
| SOL_2025_15M_HOLDOUT | zentrum_stabil | 0.9875 | 0.6994 | 0.5246 | 0.1632 | 0.8471 | 0.2534 | 0.2407 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_2025_15M_HOLDOUT | offene_variante | 0.0125 | 0.5833 | 0.3696 | 0.2782 | 0.6651 | 0.0000 | 1.0000 | dio_mcm_episode_1t36jh9 | dio_13vm |
| SOL_2025_30M_HOLDOUT | zentrum_stabil | 0.9870 | 0.6970 | 0.5209 | 0.1642 | 0.8439 | 0.2536 | 0.2403 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_2025_30M_HOLDOUT | offene_variante | 0.0130 | 0.5789 | 0.3604 | 0.2882 | 0.6659 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_034e |
| SOL_2025_1H_HOLDOUT | zentrum_stabil | 0.9835 | 0.6980 | 0.5228 | 0.1642 | 0.8439 | 0.2545 | 0.2376 | dio_mcm_episode_1qlxgj7 | dio_104t |
| SOL_2025_1H_HOLDOUT | offene_variante | 0.0165 | 0.5786 | 0.3645 | 0.2886 | 0.6638 | 0.0000 | 1.0000 | dio_mcm_episode_0xg6rjf | dio_1j51 |

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
