# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:37:33

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
| REAL_DRIFT_2023_A | 9994 | stark_zentriert_wenig_rand | 0.9881 | 0.0119 | 0.0000 | 0.2479 | 0.7077 | 0.5524 | 0.1703 | 0.8415 |
| REAL_DRIFT_2023_A_FOLLOW | 9994 | stark_zentriert_wenig_rand | 0.9887 | 0.0113 | 0.0000 | 0.2475 | 0.7067 | 0.5522 | 0.1716 | 0.8391 |
| REAL_DRIFT_2023_B | 9994 | stark_zentriert_wenig_rand | 0.9894 | 0.0106 | 0.0000 | 0.2470 | 0.7070 | 0.5520 | 0.1712 | 0.8397 |
| REAL_DRIFT_2023_B_FOLLOW | 9994 | stark_zentriert_wenig_rand | 0.9895 | 0.0105 | 0.0000 | 0.2474 | 0.7080 | 0.5528 | 0.1701 | 0.8426 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_DRIFT_2023_A | zentrum_stabil | 0.9881 | 0.7092 | 0.5547 | 0.1689 | 0.8437 | 0.2531 | 0.2410 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2023_A | offene_variante | 0.0119 | 0.5786 | 0.3667 | 0.2902 | 0.6646 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| REAL_DRIFT_2023_A_FOLLOW | zentrum_stabil | 0.9887 | 0.7081 | 0.5543 | 0.1702 | 0.8412 | 0.2529 | 0.2415 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2023_A_FOLLOW | offene_variante | 0.0113 | 0.5796 | 0.3698 | 0.2889 | 0.6562 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_05cl |
| REAL_DRIFT_2023_B | zentrum_stabil | 0.9894 | 0.7084 | 0.5540 | 0.1699 | 0.8417 | 0.2527 | 0.2420 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2023_B | offene_variante | 0.0106 | 0.5769 | 0.3654 | 0.2937 | 0.6548 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_15yz |
| REAL_DRIFT_2023_B_FOLLOW | zentrum_stabil | 0.9895 | 0.7094 | 0.5547 | 0.1689 | 0.8446 | 0.2527 | 0.2421 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2023_B_FOLLOW | offene_variante | 0.0105 | 0.5789 | 0.3694 | 0.2872 | 0.6571 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0ku7 |

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
