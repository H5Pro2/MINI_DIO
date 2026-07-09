# Weltrelative Topologie-Matrix

Stand: 2026-06-19 12:07:09

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
| STABLE_2026_10K | 9994 | zentrum_mit_rand_und_uebergang | 0.8286 | 0.1279 | 0.0435 | 0.2492 | 0.6549 | 0.4125 | 0.1763 | 0.8670 |
| STRESS_2023_NEG_10K | 9994 | zentrum_mit_rand_und_uebergang | 0.8318 | 0.1278 | 0.0404 | 0.2494 | 0.6543 | 0.4098 | 0.1760 | 0.8655 |
| EXPANSION_2023_POS_10K | 9994 | zentrum_mit_rand_und_uebergang | 0.8216 | 0.1390 | 0.0394 | 0.2484 | 0.6534 | 0.4097 | 0.1781 | 0.8656 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| STABLE_2026_10K | zentrum_stabil | 0.8286 | 0.6622 | 0.4165 | 0.1588 | 0.8752 | 0.3015 | 0.0975 | dio_mcm_episode_183drjy | dio_1xk5 |
| STABLE_2026_10K | offene_variante | 0.1279 | 0.6260 | 0.3939 | 0.2410 | 0.8360 | 0.0016 | 0.9836 | dio_mcm_episode_183drjy | dio_0zcl |
| STABLE_2026_10K | spannungsrand_kippnaehe | 0.0435 | 0.6023 | 0.3914 | 0.3187 | 0.8029 | 0.0000 | 1.0000 | dio_mcm_episode_183drjy | dio_1tyr |
| STRESS_2023_NEG_10K | zentrum_stabil | 0.8318 | 0.6613 | 0.4138 | 0.1594 | 0.8737 | 0.3003 | 0.1018 | dio_mcm_episode_183drjy | dio_1yp1 |
| STRESS_2023_NEG_10K | offene_variante | 0.1278 | 0.6258 | 0.3907 | 0.2388 | 0.8344 | 0.0023 | 0.9781 | dio_mcm_episode_183drjy | dio_13s2 |
| STRESS_2023_NEG_10K | spannungsrand_kippnaehe | 0.0404 | 0.5992 | 0.3870 | 0.3212 | 0.7961 | 0.0000 | 1.0000 | dio_mcm_episode_183drjy | dio_0xkv |
| EXPANSION_2023_POS_10K | zentrum_stabil | 0.8216 | 0.6607 | 0.4141 | 0.1610 | 0.8743 | 0.3036 | 0.0929 | dio_mcm_episode_183drjy | dio_1yp1 |
| EXPANSION_2023_POS_10K | offene_variante | 0.1390 | 0.6250 | 0.3897 | 0.2390 | 0.8324 | 0.0043 | 0.9662 | dio_mcm_episode_183drjy | dio_0xwn |
| EXPANSION_2023_POS_10K | spannungsrand_kippnaehe | 0.0394 | 0.6007 | 0.3884 | 0.3203 | 0.8012 | 0.0000 | 1.0000 | dio_mcm_episode_183drjy | dio_1df2 |

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

## Wie es weitergeht

Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.
