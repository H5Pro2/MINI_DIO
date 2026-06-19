# Weltrelative Topologie-Matrix

Stand: 2026-06-19 19:43:44

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
| SOL_2023_NEG_STRESS_10K_RECEPTOR | 9994 | zentrum_mit_rand_und_uebergang | 0.8406 | 0.1302 | 0.0292 | 0.2497 | 0.6531 | 0.4131 | 0.1835 | 0.8683 |
| SOL_2024_SIDEWAYS_5K_RECEPTOR | 4994 | zentrum_mit_rand_und_uebergang | 0.8324 | 0.1378 | 0.0298 | 0.2501 | 0.6472 | 0.4038 | 0.1889 | 0.8664 |
| SOL_2025_STRESS_5K_RECEPTOR | 4994 | zentrum_mit_rand_und_uebergang | 0.8240 | 0.1508 | 0.0252 | 0.2495 | 0.6467 | 0.4044 | 0.1904 | 0.8660 |
| SOL_2026_STABLE_5K_RECEPTOR | 4994 | zentrum_mit_rand_und_uebergang | 0.8396 | 0.1282 | 0.0322 | 0.2501 | 0.6501 | 0.4087 | 0.1860 | 0.8694 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOL_2023_NEG_STRESS_10K_RECEPTOR | zentrum_stabil | 0.8406 | 0.6609 | 0.4199 | 0.1703 | 0.8818 | 0.2973 | 0.1086 | dio_mcm_episode_183drjy | dio_0xvr |
| SOL_2023_NEG_STRESS_10K_RECEPTOR | offene_variante | 0.1302 | 0.6196 | 0.3816 | 0.2388 | 0.8155 | 0.0008 | 0.9954 | dio_mcm_episode_183drjy | dio_1rtv |
| SOL_2023_NEG_STRESS_10K_RECEPTOR | spannungsrand_kippnaehe | 0.0292 | 0.5785 | 0.3576 | 0.3158 | 0.7132 | 0.0000 | 1.0000 | dio_mcm_episode_183drjy | dio_0w7y |
| SOL_2024_SIDEWAYS_5K_RECEPTOR | zentrum_stabil | 0.8324 | 0.6544 | 0.4097 | 0.1762 | 0.8801 | 0.3005 | 0.1010 | dio_mcm_episode_1t5bcxp | dio_19tt |
| SOL_2024_SIDEWAYS_5K_RECEPTOR | offene_variante | 0.1378 | 0.6187 | 0.3791 | 0.2390 | 0.8158 | 0.0000 | 0.9884 | dio_mcm_episode_1t5bcxp | dio_0k4l |
| SOL_2024_SIDEWAYS_5K_RECEPTOR | spannungsrand_kippnaehe | 0.0298 | 0.5785 | 0.3542 | 0.3138 | 0.7189 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_076u |
| SOL_2025_STRESS_5K_RECEPTOR | zentrum_stabil | 0.8240 | 0.6537 | 0.4098 | 0.1779 | 0.8795 | 0.3033 | 0.0906 | dio_mcm_episode_1t5bcxp | dio_1oem |
| SOL_2025_STRESS_5K_RECEPTOR | offene_variante | 0.1508 | 0.6195 | 0.3826 | 0.2385 | 0.8160 | 0.0013 | 0.9960 | dio_mcm_episode_1t5bcxp | dio_0cxq |
| SOL_2025_STRESS_5K_RECEPTOR | spannungsrand_kippnaehe | 0.0252 | 0.5818 | 0.3590 | 0.3104 | 0.7224 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_07ov |
| SOL_2026_STABLE_5K_RECEPTOR | zentrum_stabil | 0.8396 | 0.6573 | 0.4142 | 0.1731 | 0.8831 | 0.2979 | 0.1068 | dio_mcm_episode_1t5bcxp | dio_0xvr |
| SOL_2026_STABLE_5K_RECEPTOR | offene_variante | 0.1282 | 0.6196 | 0.3834 | 0.2386 | 0.8148 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0hly |
| SOL_2026_STABLE_5K_RECEPTOR | spannungsrand_kippnaehe | 0.0322 | 0.5840 | 0.3650 | 0.3142 | 0.7285 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_16o4 |

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
