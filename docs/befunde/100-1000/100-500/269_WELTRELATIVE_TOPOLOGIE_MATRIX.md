# Weltrelative Topologie-Matrix

Stand: 2026-06-19 11:11:53

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
| SOL_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8084 | 0.1449 | 0.0466 | 0.2447 | 0.6447 | 0.3970 | 0.1875 | 0.8645 |
| SOL_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8064 | 0.1510 | 0.0426 | 0.2467 | 0.6447 | 0.3956 | 0.1855 | 0.8632 |
| BTC_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8270 | 0.1339 | 0.0391 | 0.2487 | 0.6467 | 0.3972 | 0.1815 | 0.8653 |
| BTC_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8114 | 0.1394 | 0.0491 | 0.2503 | 0.6480 | 0.3984 | 0.1795 | 0.8654 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOL_2024_5M_2K | zentrum_stabil | 0.8084 | 0.6507 | 0.3987 | 0.1709 | 0.8727 | 0.3083 | 0.0788 | dio_mcm_episode_1t5bcxp | dio_0r0t |
| SOL_2024_5M_2K | offene_variante | 0.1449 | 0.6258 | 0.3914 | 0.2383 | 0.8398 | 0.0035 | 0.9654 | dio_mcm_episode_1t5bcxp | dio_11pe |
| SOL_2024_5M_2K | spannungsrand_kippnaehe | 0.0466 | 0.5992 | 0.3849 | 0.3175 | 0.7974 | 0.0108 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1mae |
| SOL_2024_1H_2K | zentrum_stabil | 0.8064 | 0.6511 | 0.3976 | 0.1686 | 0.8724 | 0.3091 | 0.0790 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| SOL_2024_1H_2K | offene_variante | 0.1510 | 0.6241 | 0.3894 | 0.2393 | 0.8348 | 0.0066 | 0.9535 | dio_mcm_episode_1t5bcxp | dio_07si |
| SOL_2024_1H_2K | spannungsrand_kippnaehe | 0.0426 | 0.5977 | 0.3794 | 0.3157 | 0.7917 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1a6h |
| BTC_2024_5M_2K | zentrum_stabil | 0.8270 | 0.6526 | 0.3995 | 0.1655 | 0.8733 | 0.3014 | 0.0964 | dio_mcm_episode_1t5bcxp | dio_1yp1 |
| BTC_2024_5M_2K | offene_variante | 0.1339 | 0.6241 | 0.3870 | 0.2385 | 0.8351 | 0.0075 | 0.9813 | dio_mcm_episode_1t5bcxp | dio_149i |
| BTC_2024_5M_2K | spannungsrand_kippnaehe | 0.0391 | 0.5977 | 0.3846 | 0.3251 | 0.7992 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_17l1 |
| BTC_2024_1H_2K | zentrum_stabil | 0.8114 | 0.6551 | 0.4007 | 0.1607 | 0.8749 | 0.3084 | 0.0779 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| BTC_2024_1H_2K | offene_variante | 0.1394 | 0.6230 | 0.3876 | 0.2413 | 0.8323 | 0.0000 | 0.9892 | dio_mcm_episode_1t5bcxp | dio_0htq |
| BTC_2024_1H_2K | spannungsrand_kippnaehe | 0.0491 | 0.6027 | 0.3920 | 0.3154 | 0.8025 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1ql1 |

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

## Wie es weitergeht

Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.
