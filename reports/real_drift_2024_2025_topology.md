# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:46:37

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
| REAL_DRIFT_2024_A | 9994 | stark_zentriert_wenig_rand | 0.9930 | 0.0070 | 0.0000 | 0.2499 | 0.7068 | 0.5527 | 0.1710 | 0.8408 |
| REAL_DRIFT_2024_A_FOLLOW | 9994 | stark_zentriert_wenig_rand | 0.9922 | 0.0078 | 0.0000 | 0.2493 | 0.7059 | 0.5523 | 0.1720 | 0.8387 |
| REAL_DRIFT_2025_A | 9994 | stark_zentriert_wenig_rand | 0.9919 | 0.0081 | 0.0000 | 0.2495 | 0.7066 | 0.5533 | 0.1714 | 0.8395 |
| REAL_DRIFT_2025_A_FOLLOW | 9994 | stark_zentriert_wenig_rand | 0.9924 | 0.0076 | 0.0000 | 0.2492 | 0.7058 | 0.5525 | 0.1723 | 0.8379 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_DRIFT_2024_A | zentrum_stabil | 0.9930 | 0.7076 | 0.5540 | 0.1702 | 0.8421 | 0.2518 | 0.2448 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2024_A | offene_variante | 0.0070 | 0.5812 | 0.3664 | 0.2831 | 0.6662 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_1c6r |
| REAL_DRIFT_2024_A_FOLLOW | zentrum_stabil | 0.9922 | 0.7069 | 0.5538 | 0.1711 | 0.8401 | 0.2520 | 0.2442 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2024_A_FOLLOW | offene_variante | 0.0078 | 0.5801 | 0.3670 | 0.2874 | 0.6688 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| REAL_DRIFT_2025_A | zentrum_stabil | 0.9919 | 0.7077 | 0.5548 | 0.1704 | 0.8409 | 0.2521 | 0.2439 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2025_A | offene_variante | 0.0081 | 0.5783 | 0.3653 | 0.2876 | 0.6606 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_0xvx |
| REAL_DRIFT_2025_A_FOLLOW | zentrum_stabil | 0.9924 | 0.7068 | 0.5539 | 0.1714 | 0.8392 | 0.2520 | 0.2443 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_2025_A_FOLLOW | offene_variante | 0.0076 | 0.5798 | 0.3688 | 0.2869 | 0.6631 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1v68 |

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
