# Weltrelative Topologie-Matrix

Stand: 2026-06-21 16:13:13

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
| BTC2025_QUIET | 3994 | stark_zentriert_wenig_rand | 0.8413 | 0.1482 | 0.0105 | 0.2501 | 0.7006 | 0.5226 | 0.1561 | 0.8481 |
| BTC2025_STRESS | 3994 | stark_zentriert_wenig_rand | 0.8247 | 0.1610 | 0.0143 | 0.2501 | 0.6989 | 0.5214 | 0.1581 | 0.8449 |
| SOL2024_QUIET | 3994 | stark_zentriert_wenig_rand | 0.8020 | 0.1868 | 0.0113 | 0.2499 | 0.6978 | 0.5204 | 0.1589 | 0.8430 |
| SOL2024_STRESS | 3994 | stark_zentriert_wenig_rand | 0.8005 | 0.1860 | 0.0135 | 0.2499 | 0.6975 | 0.5207 | 0.1597 | 0.8416 |
| SOL2025_QUIET | 3994 | gemischte_rollenordnung | 0.7892 | 0.1993 | 0.0115 | 0.2499 | 0.6976 | 0.5208 | 0.1595 | 0.8415 |
| SOL2025_STRESS | 3994 | stark_zentriert_wenig_rand | 0.8217 | 0.1647 | 0.0135 | 0.2499 | 0.6990 | 0.5223 | 0.1582 | 0.8445 |
| KAS2024_5M | 1994 | stark_zentriert_wenig_rand | 0.8079 | 0.1795 | 0.0125 | 0.2503 | 0.6930 | 0.5087 | 0.1606 | 0.8430 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC2025_QUIET | zentrum_stabil | 0.8413 | 0.7092 | 0.5340 | 0.1467 | 0.8613 | 0.2973 | 0.1452 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_QUIET | offene_variante | 0.1482 | 0.6603 | 0.4706 | 0.1987 | 0.7832 | 0.0000 | 0.7922 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_QUIET | spannungsrand_kippnaehe | 0.0105 | 0.5787 | 0.3503 | 0.3062 | 0.7108 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1ghk |
| BTC2025_STRESS | zentrum_stabil | 0.8247 | 0.7089 | 0.5345 | 0.1471 | 0.8604 | 0.3030 | 0.1257 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_STRESS | offene_variante | 0.1610 | 0.6586 | 0.4697 | 0.2009 | 0.7792 | 0.0016 | 0.8212 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_STRESS | spannungsrand_kippnaehe | 0.0143 | 0.5720 | 0.3495 | 0.3093 | 0.6909 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1a0q |
| SOL2024_QUIET | zentrum_stabil | 0.8020 | 0.7078 | 0.5328 | 0.1476 | 0.8592 | 0.3116 | 0.1165 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2024_QUIET | offene_variante | 0.1868 | 0.6629 | 0.4775 | 0.1981 | 0.7829 | 0.0013 | 0.7788 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2024_QUIET | spannungsrand_kippnaehe | 0.0113 | 0.5688 | 0.3440 | 0.3150 | 0.6852 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| SOL2024_STRESS | zentrum_stabil | 0.8005 | 0.7078 | 0.5334 | 0.1480 | 0.8586 | 0.3125 | 0.1132 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2024_STRESS | offene_variante | 0.1860 | 0.6624 | 0.4787 | 0.1992 | 0.7792 | 0.0000 | 0.7847 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2024_STRESS | spannungsrand_kippnaehe | 0.0135 | 0.5725 | 0.3506 | 0.3098 | 0.6936 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| SOL2025_QUIET | zentrum_stabil | 0.7892 | 0.7082 | 0.5341 | 0.1476 | 0.8586 | 0.3166 | 0.1095 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_QUIET | offene_variante | 0.1993 | 0.6628 | 0.4780 | 0.1979 | 0.7818 | 0.0013 | 0.7638 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2025_QUIET | spannungsrand_kippnaehe | 0.0115 | 0.5743 | 0.3512 | 0.3084 | 0.7037 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| SOL2025_STRESS | zentrum_stabil | 0.8217 | 0.7090 | 0.5350 | 0.1472 | 0.8600 | 0.3038 | 0.1237 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_STRESS | offene_variante | 0.1647 | 0.6600 | 0.4725 | 0.2007 | 0.7804 | 0.0030 | 0.8191 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2025_STRESS | spannungsrand_kippnaehe | 0.0135 | 0.5712 | 0.3522 | 0.3101 | 0.6805 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18i0 |
| KAS2024_5M | zentrum_stabil | 0.8079 | 0.7033 | 0.5219 | 0.1489 | 0.8589 | 0.3097 | 0.1142 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_5M | offene_variante | 0.1795 | 0.6548 | 0.4607 | 0.2035 | 0.7813 | 0.0000 | 0.8101 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| KAS2024_5M | spannungsrand_kippnaehe | 0.0125 | 0.5723 | 0.3487 | 0.3070 | 0.6952 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18i0 |

## Lesart

Zentrumsnahe Welten: 6
Gemischte Rollenordnung: 1
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
