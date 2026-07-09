# Weltrelative Topologie-Matrix

Stand: 2026-06-19 16:17:23

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
| SOL_2024_5M_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8250 | 0.1394 | 0.0356 | 0.2503 | 0.6438 | 0.3992 | 0.1933 | 0.8655 |
| SOL_2024_1H_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8129 | 0.1585 | 0.0286 | 0.2508 | 0.6442 | 0.3985 | 0.1917 | 0.8662 |
| BTC_2024_5M_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8340 | 0.1379 | 0.0281 | 0.2503 | 0.6456 | 0.3996 | 0.1893 | 0.8677 |
| BTC_2024_1H_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8320 | 0.1339 | 0.0341 | 0.2497 | 0.6471 | 0.4013 | 0.1877 | 0.8687 |
| KAS_2024_5M_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8104 | 0.1585 | 0.0311 | 0.2487 | 0.6441 | 0.3994 | 0.1926 | 0.8656 |
| KAS_2024_1H_RECEPTOR | 1994 | zentrum_mit_rand_und_uebergang | 0.8129 | 0.1535 | 0.0336 | 0.2497 | 0.6434 | 0.3971 | 0.1927 | 0.8662 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOL_2024_5M_RECEPTOR | zentrum_stabil | 0.8250 | 0.6506 | 0.4039 | 0.1806 | 0.8803 | 0.3033 | 0.0930 | dio_mcm_episode_1t5bcxp | dio_0y8z |
| SOL_2024_5M_RECEPTOR | offene_variante | 0.1394 | 0.6191 | 0.3810 | 0.2385 | 0.8150 | 0.0000 | 0.9892 | dio_mcm_episode_1t5bcxp | dio_1kpm |
| SOL_2024_5M_RECEPTOR | spannungsrand_kippnaehe | 0.0356 | 0.5811 | 0.3604 | 0.3103 | 0.7208 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_04dy |
| SOL_2024_1H_RECEPTOR | zentrum_stabil | 0.8129 | 0.6515 | 0.4036 | 0.1782 | 0.8814 | 0.3085 | 0.0790 | dio_mcm_episode_1t5bcxp | dio_0xvr |
| SOL_2024_1H_RECEPTOR | offene_variante | 0.1585 | 0.6191 | 0.3808 | 0.2380 | 0.8179 | 0.0000 | 0.9937 | dio_mcm_episode_1t5bcxp | dio_0un2 |
| SOL_2024_1H_RECEPTOR | spannungsrand_kippnaehe | 0.0286 | 0.5745 | 0.3496 | 0.3183 | 0.7022 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_12gk |
| BTC_2024_5M_RECEPTOR | zentrum_stabil | 0.8340 | 0.6523 | 0.4046 | 0.1766 | 0.8814 | 0.3001 | 0.1028 | dio_mcm_episode_1t5bcxp | dio_1oem |
| BTC_2024_5M_RECEPTOR | offene_variante | 0.1379 | 0.6184 | 0.3790 | 0.2395 | 0.8157 | 0.0000 | 0.9891 | dio_mcm_episode_1t5bcxp | dio_0nvl |
| BTC_2024_5M_RECEPTOR | spannungsrand_kippnaehe | 0.0281 | 0.5772 | 0.3544 | 0.3184 | 0.7157 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1q4y |
| BTC_2024_1H_RECEPTOR | zentrum_stabil | 0.8320 | 0.6545 | 0.4060 | 0.1737 | 0.8842 | 0.3002 | 0.0989 | dio_mcm_episode_1t5bcxp | dio_0zn5 |
| BTC_2024_1H_RECEPTOR | offene_variante | 0.1339 | 0.6177 | 0.3822 | 0.2427 | 0.8103 | 0.0037 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0hwx |
| BTC_2024_1H_RECEPTOR | spannungsrand_kippnaehe | 0.0341 | 0.5813 | 0.3593 | 0.3122 | 0.7213 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1ema |
| KAS_2024_5M_RECEPTOR | zentrum_stabil | 0.8104 | 0.6511 | 0.4047 | 0.1795 | 0.8801 | 0.3082 | 0.0767 | dio_mcm_episode_1t5bcxp | dio_04xs |
| KAS_2024_5M_RECEPTOR | offene_variante | 0.1585 | 0.6199 | 0.3798 | 0.2361 | 0.8188 | 0.0032 | 0.9905 | dio_mcm_episode_1t5bcxp | dio_1c6r |
| KAS_2024_5M_RECEPTOR | spannungsrand_kippnaehe | 0.0311 | 0.5823 | 0.3596 | 0.3110 | 0.7259 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_0vim |
| KAS_2024_1H_RECEPTOR | zentrum_stabil | 0.8129 | 0.6506 | 0.4020 | 0.1791 | 0.8809 | 0.3072 | 0.0777 | dio_mcm_episode_1t5bcxp | dio_04xs |
| KAS_2024_1H_RECEPTOR | offene_variante | 0.1535 | 0.6197 | 0.3802 | 0.2381 | 0.8211 | 0.0033 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_10tk |
| KAS_2024_1H_RECEPTOR | spannungsrand_kippnaehe | 0.0336 | 0.5783 | 0.3560 | 0.3157 | 0.7170 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0c5m |

## Lesart

Zentrumsnahe Welten: 6
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
