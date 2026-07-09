# Weltrelative Topologie-Matrix

Stand: 2026-06-19 12:38:28

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
| BTC_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8119 | 0.1389 | 0.0491 | 0.2503 | 0.6484 | 0.3981 | 0.1797 | 0.8657 |
| BTC_2025_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8385 | 0.1133 | 0.0481 | 0.2482 | 0.6498 | 0.4004 | 0.1784 | 0.8666 |
| SOL_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8059 | 0.1515 | 0.0426 | 0.2467 | 0.6451 | 0.3952 | 0.1857 | 0.8636 |
| SOL_2025_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8064 | 0.1434 | 0.0502 | 0.2492 | 0.6467 | 0.3976 | 0.1842 | 0.8647 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_2024_1H_2K | zentrum_stabil | 0.8119 | 0.6555 | 0.4003 | 0.1609 | 0.8752 | 0.3082 | 0.0778 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| BTC_2024_1H_2K | offene_variante | 0.1389 | 0.6233 | 0.3874 | 0.2416 | 0.8328 | 0.0000 | 0.9928 | dio_mcm_episode_1t5bcxp | dio_0htq |
| BTC_2024_1H_2K | spannungsrand_kippnaehe | 0.0491 | 0.6031 | 0.3917 | 0.3156 | 0.8028 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1ql1 |
| BTC_2025_1H_2K | zentrum_stabil | 0.8385 | 0.6562 | 0.4024 | 0.1615 | 0.8754 | 0.2984 | 0.1071 | dio_mcm_episode_1t5bcxp | dio_0pda |
| BTC_2025_1H_2K | offene_variante | 0.1133 | 0.6243 | 0.3937 | 0.2433 | 0.8337 | 0.0000 | 0.9912 | dio_mcm_episode_1t5bcxp | dio_0rg1 |
| BTC_2025_1H_2K | spannungsrand_kippnaehe | 0.0481 | 0.5971 | 0.3810 | 0.3197 | 0.7899 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_19m5 |
| SOL_2024_1H_2K | zentrum_stabil | 0.8059 | 0.6515 | 0.3972 | 0.1687 | 0.8727 | 0.3093 | 0.0778 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| SOL_2024_1H_2K | offene_variante | 0.1515 | 0.6244 | 0.3891 | 0.2395 | 0.8353 | 0.0066 | 0.9570 | dio_mcm_episode_1t5bcxp | dio_0xnb |
| SOL_2024_1H_2K | spannungsrand_kippnaehe | 0.0426 | 0.5980 | 0.3792 | 0.3159 | 0.7920 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1a6h |
| SOL_2025_1H_2K | zentrum_stabil | 0.8064 | 0.6539 | 0.4005 | 0.1659 | 0.8748 | 0.3097 | 0.0765 | dio_mcm_episode_1t5bcxp | dio_1xk5 |
| SOL_2025_1H_2K | offene_variante | 0.1434 | 0.6238 | 0.3873 | 0.2398 | 0.8338 | 0.0035 | 0.9650 | dio_mcm_episode_1t5bcxp | dio_1um9 |
| SOL_2025_1H_2K | spannungsrand_kippnaehe | 0.0502 | 0.5971 | 0.3800 | 0.3195 | 0.7909 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0cbk |

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
