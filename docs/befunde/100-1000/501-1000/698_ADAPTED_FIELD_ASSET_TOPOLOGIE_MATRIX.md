# Weltrelative Topologie-Matrix

Stand: 2026-06-22 12:28:10

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
| BTC_2024_5M_2K | 1994 | gemischte_rollenordnung | 0.7934 | 0.1976 | 0.0090 | 0.2497 | 0.6949 | 0.5132 | 0.1545 | 0.8411 |
| SOL_2024_5M_2K | 1994 | gemischte_rollenordnung | 0.7543 | 0.2372 | 0.0085 | 0.2497 | 0.6925 | 0.5107 | 0.1568 | 0.8372 |
| KAS_2024_5M_2K | 1994 | gemischte_rollenordnung | 0.7783 | 0.2131 | 0.0085 | 0.2503 | 0.6932 | 0.5107 | 0.1557 | 0.8396 |
| PAXG_2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8474 | 0.1497 | 0.0029 | 0.2457 | 0.7147 | 0.5403 | 0.1482 | 0.8523 |
| DOGE_2024_5M_10K | 9994 | gemischte_rollenordnung | 0.7963 | 0.1968 | 0.0069 | 0.2493 | 0.7050 | 0.5372 | 0.1526 | 0.8413 |
| XRP_2024_5M_10K | 9994 | gemischte_rollenordnung | 0.7960 | 0.1958 | 0.0082 | 0.2495 | 0.7054 | 0.5376 | 0.1521 | 0.8419 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_2024_5M_2K | zentrum_stabil | 0.7934 | 0.7056 | 0.5267 | 0.1431 | 0.8587 | 0.3148 | 0.1056 | dio_mcm_episode_1joiyc3 | dio_104t |
| BTC_2024_5M_2K | offene_variante | 0.1976 | 0.6576 | 0.4664 | 0.1934 | 0.7788 | 0.0025 | 0.7970 | dio_mcm_episode_1joiyc3 | dio_0jkk |
| BTC_2024_5M_2K | spannungsrand_kippnaehe | 0.0090 | 0.5720 | 0.3549 | 0.2989 | 0.6658 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_1x3j |
| SOL_2024_5M_2K | zentrum_stabil | 0.7543 | 0.7041 | 0.5244 | 0.1440 | 0.8576 | 0.3318 | 0.0858 | dio_mcm_episode_1joiyc3 | dio_104t |
| SOL_2024_5M_2K | offene_variante | 0.2372 | 0.6603 | 0.4728 | 0.1923 | 0.7785 | 0.0000 | 0.7463 | dio_mcm_episode_1joiyc3 | dio_00ja |
| SOL_2024_5M_2K | spannungsrand_kippnaehe | 0.0085 | 0.5676 | 0.3505 | 0.3018 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_19yo |
| KAS_2024_5M_2K | zentrum_stabil | 0.7783 | 0.7036 | 0.5231 | 0.1441 | 0.8578 | 0.3215 | 0.0986 | dio_mcm_episode_1joiyc3 | dio_104t |
| KAS_2024_5M_2K | offene_variante | 0.2131 | 0.6601 | 0.4715 | 0.1923 | 0.7801 | 0.0000 | 0.7741 | dio_mcm_episode_1joiyc3 | dio_00ja |
| KAS_2024_5M_2K | spannungsrand_kippnaehe | 0.0085 | 0.5719 | 0.3552 | 0.2960 | 0.6686 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_16i6 |
| PAXG_2024_5M_10K | zentrum_stabil | 0.8474 | 0.7223 | 0.5497 | 0.1405 | 0.8645 | 0.2946 | 0.1377 | dio_mcm_episode_0ybr5e3 | dio_104t |
| PAXG_2024_5M_10K | offene_variante | 0.1497 | 0.6742 | 0.4907 | 0.1890 | 0.7864 | 0.0027 | 0.8717 | dio_mcm_episode_0ybr5e3 | dio_00ja |
| PAXG_2024_5M_10K | spannungsrand_kippnaehe | 0.0029 | 0.5761 | 0.3512 | 0.2945 | 0.6838 | 0.0000 | 1.0000 | dio_mcm_episode_0ybr5e3 | dio_19v1 |
| DOGE_2024_5M_10K | zentrum_stabil | 0.7963 | 0.7152 | 0.5496 | 0.1420 | 0.8589 | 0.3138 | 0.0994 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE_2024_5M_10K | offene_variante | 0.1968 | 0.6684 | 0.4933 | 0.1906 | 0.7765 | 0.0010 | 0.8332 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE_2024_5M_10K | spannungsrand_kippnaehe | 0.0069 | 0.5711 | 0.3561 | 0.2997 | 0.6600 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1c6r |
| XRP_2024_5M_10K | zentrum_stabil | 0.7960 | 0.7159 | 0.5504 | 0.1410 | 0.8599 | 0.3140 | 0.0972 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP_2024_5M_10K | offene_variante | 0.1958 | 0.6683 | 0.4932 | 0.1910 | 0.7766 | 0.0005 | 0.8401 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP_2024_5M_10K | spannungsrand_kippnaehe | 0.0082 | 0.5706 | 0.3625 | 0.3007 | 0.6509 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |

## Lesart

Zentrumsnahe Welten: 1
Gemischte Rollenordnung: 5
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
