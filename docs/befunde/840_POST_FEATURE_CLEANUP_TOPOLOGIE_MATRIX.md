# Weltrelative Topologie-Matrix

Stand: 2026-06-26 01:09:56

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
| POST_CLEAN_SOL_2024_5M | 1994 | gemischte_rollenordnung | 0.7543 | 0.2372 | 0.0085 | 0.2497 | 0.6925 | 0.5107 | 0.1568 | 0.8372 |
| POST_CLEAN_BTC_2024_5M | 1994 | gemischte_rollenordnung | 0.7934 | 0.1976 | 0.0090 | 0.2503 | 0.6949 | 0.5132 | 0.1545 | 0.8411 |
| POST_CLEAN_KAS_2024_5M | 1994 | gemischte_rollenordnung | 0.7783 | 0.2131 | 0.0085 | 0.2503 | 0.6932 | 0.5107 | 0.1557 | 0.8396 |
| POST_CLEAN_PAXG_2024_5M | 1994 | stark_zentriert_wenig_rand | 0.8310 | 0.1620 | 0.0070 | 0.2457 | 0.7029 | 0.5135 | 0.1515 | 0.8504 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| POST_CLEAN_SOL_2024_5M | zentrum_stabil | 0.7543 | 0.7041 | 0.5244 | 0.1440 | 0.8576 | 0.3318 | 0.0858 | dio_mcm_episode_1joiyc3 | dio_104t |
| POST_CLEAN_SOL_2024_5M | offene_variante | 0.2372 | 0.6603 | 0.4728 | 0.1924 | 0.7785 | 0.0000 | 0.7463 | dio_mcm_episode_1joiyc3 | dio_00ja |
| POST_CLEAN_SOL_2024_5M | spannungsrand_kippnaehe | 0.0085 | 0.5676 | 0.3504 | 0.3018 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_19yo |
| POST_CLEAN_BTC_2024_5M | zentrum_stabil | 0.7934 | 0.7056 | 0.5267 | 0.1432 | 0.8586 | 0.3154 | 0.1056 | dio_mcm_episode_1joiyc3 | dio_104t |
| POST_CLEAN_BTC_2024_5M | offene_variante | 0.1976 | 0.6576 | 0.4664 | 0.1935 | 0.7788 | 0.0025 | 0.7970 | dio_mcm_episode_1joiyc3 | dio_0jkk |
| POST_CLEAN_BTC_2024_5M | spannungsrand_kippnaehe | 0.0090 | 0.5720 | 0.3549 | 0.2989 | 0.6658 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_1x3j |
| POST_CLEAN_KAS_2024_5M | zentrum_stabil | 0.7783 | 0.7036 | 0.5231 | 0.1441 | 0.8578 | 0.3215 | 0.0979 | dio_mcm_episode_1joiyc3 | dio_104t |
| POST_CLEAN_KAS_2024_5M | offene_variante | 0.2131 | 0.6600 | 0.4715 | 0.1923 | 0.7801 | 0.0000 | 0.7765 | dio_mcm_episode_1joiyc3 | dio_00ja |
| POST_CLEAN_KAS_2024_5M | spannungsrand_kippnaehe | 0.0085 | 0.5719 | 0.3551 | 0.2960 | 0.6686 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_16i6 |
| POST_CLEAN_PAXG_2024_5M | zentrum_stabil | 0.8310 | 0.7123 | 0.5256 | 0.1418 | 0.8645 | 0.2987 | 0.1249 | dio_mcm_episode_1q3us3f | dio_104t |
| POST_CLEAN_PAXG_2024_5M | offene_variante | 0.1620 | 0.6605 | 0.4591 | 0.1953 | 0.7857 | 0.0124 | 0.8607 | dio_mcm_episode_1jx2k4i | dio_05yg |
| POST_CLEAN_PAXG_2024_5M | spannungsrand_kippnaehe | 0.0070 | 0.5702 | 0.3469 | 0.2989 | 0.6707 | 0.0000 | 1.0000 | dio_mcm_episode_1hdpu9s | dio_1d3j |

## Lesart

Zentrumsnahe Welten: 1
Gemischte Rollenordnung: 3
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
