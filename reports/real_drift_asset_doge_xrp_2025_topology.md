# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:59:16

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
| REAL_DRIFT_DOGE_2025_A | 4994 | stark_zentriert_wenig_rand | 0.9910 | 0.0090 | 0.0000 | 0.2501 | 0.7021 | 0.5400 | 0.1694 | 0.8395 |
| REAL_DRIFT_DOGE_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9886 | 0.0114 | 0.0000 | 0.2499 | 0.7035 | 0.5405 | 0.1672 | 0.8432 |
| REAL_DRIFT_XRP_2025_A | 4994 | stark_zentriert_wenig_rand | 0.9894 | 0.0106 | 0.0000 | 0.2499 | 0.7025 | 0.5404 | 0.1689 | 0.8401 |
| REAL_DRIFT_XRP_2025_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9886 | 0.0114 | 0.0000 | 0.2497 | 0.7047 | 0.5422 | 0.1664 | 0.8448 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_DRIFT_DOGE_2025_A | zentrum_stabil | 0.9910 | 0.7033 | 0.5417 | 0.1682 | 0.8412 | 0.2524 | 0.2433 | dio_mcm_episode_1qlxgj7 | dio_104t |
| REAL_DRIFT_DOGE_2025_A | offene_variante | 0.0090 | 0.5754 | 0.3621 | 0.2925 | 0.6572 | 0.0000 | 1.0000 | dio_mcm_episode_0ze0tw9 | dio_00hc |
| REAL_DRIFT_DOGE_2025_FOLLOW | zentrum_stabil | 0.9886 | 0.7049 | 0.5426 | 0.1658 | 0.8453 | 0.2530 | 0.2414 | dio_mcm_episode_0iwh9d2 | dio_104t |
| REAL_DRIFT_DOGE_2025_FOLLOW | offene_variante | 0.0114 | 0.5761 | 0.3621 | 0.2906 | 0.6657 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0dtf |
| REAL_DRIFT_XRP_2025_A | zentrum_stabil | 0.9894 | 0.7038 | 0.5422 | 0.1676 | 0.8419 | 0.2528 | 0.2421 | dio_mcm_episode_1qlxgj7 | dio_104t |
| REAL_DRIFT_XRP_2025_A | offene_variante | 0.0106 | 0.5790 | 0.3652 | 0.2896 | 0.6699 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| REAL_DRIFT_XRP_2025_FOLLOW | zentrum_stabil | 0.9886 | 0.7061 | 0.5442 | 0.1650 | 0.8468 | 0.2530 | 0.2414 | dio_mcm_episode_0iwh9d2 | dio_104t |
| REAL_DRIFT_XRP_2025_FOLLOW | offene_variante | 0.0114 | 0.5807 | 0.3677 | 0.2852 | 0.6669 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0xvx |

## Lesart

Zentrumsnahe Welten: 4
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
