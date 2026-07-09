# Weltrelative Topologie-Matrix

Stand: 2026-07-08 12:03:44

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
| PAXG_2024_5M | 1994 | stark_zentriert_wenig_rand | 0.9930 | 0.0070 | 0.0000 | 0.2397 | 0.7048 | 0.5223 | 0.1623 | 0.8506 |
| PAXG_2024_15M | 1994 | stark_zentriert_wenig_rand | 0.9925 | 0.0075 | 0.0000 | 0.2447 | 0.6977 | 0.5147 | 0.1643 | 0.8431 |
| PAXG_2024_1H | 1994 | stark_zentriert_wenig_rand | 0.9895 | 0.0105 | 0.0000 | 0.2477 | 0.6972 | 0.5182 | 0.1656 | 0.8412 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG_2024_5M | zentrum_stabil | 0.9930 | 0.7057 | 0.5235 | 0.1613 | 0.8519 | 0.2520 | 0.2449 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2024_5M | offene_variante | 0.0070 | 0.5727 | 0.3543 | 0.2966 | 0.6654 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_1d3j |
| PAXG_2024_15M | zentrum_stabil | 0.9925 | 0.6986 | 0.5158 | 0.1634 | 0.8443 | 0.2521 | 0.2446 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2024_15M | offene_variante | 0.0075 | 0.5881 | 0.3642 | 0.2829 | 0.6785 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_00hc |
| PAXG_2024_1H | zentrum_stabil | 0.9895 | 0.6985 | 0.5199 | 0.1642 | 0.8431 | 0.2529 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2024_1H | offene_variante | 0.0105 | 0.5808 | 0.3592 | 0.2891 | 0.6668 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_19yo |

## Lesart

Zentrumsnahe Welten: 3
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
