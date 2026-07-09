# Weltrelative Topologie-Matrix

Stand: 2026-06-19 13:07:37

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
| KAS_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8004 | 0.1575 | 0.0421 | 0.2442 | 0.6451 | 0.3963 | 0.1869 | 0.8645 |
| KAS_2024_15M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8004 | 0.1545 | 0.0451 | 0.2462 | 0.6455 | 0.3964 | 0.1863 | 0.8641 |
| KAS_2024_30M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.7894 | 0.1680 | 0.0426 | 0.2487 | 0.6451 | 0.3959 | 0.1866 | 0.8640 |
| KAS_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.7984 | 0.1560 | 0.0456 | 0.2467 | 0.6445 | 0.3940 | 0.1865 | 0.8639 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| KAS_2024_5M_2K | zentrum_stabil | 0.8004 | 0.6511 | 0.3977 | 0.1702 | 0.8729 | 0.3095 | 0.0708 | dio_mcm_episode_1t5bcxp | dio_0jsu |
| KAS_2024_5M_2K | offene_variante | 0.1575 | 0.6264 | 0.3921 | 0.2377 | 0.8387 | 0.0127 | 0.9618 | dio_mcm_episode_1t5bcxp | dio_0kdn |
| KAS_2024_5M_2K | spannungsrand_kippnaehe | 0.0421 | 0.6013 | 0.3855 | 0.3155 | 0.8020 | 0.0119 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0bqz |
| KAS_2024_15M_2K | zentrum_stabil | 0.8004 | 0.6521 | 0.3988 | 0.1690 | 0.8734 | 0.3120 | 0.0752 | dio_mcm_episode_1t5bcxp | dio_1370 |
| KAS_2024_15M_2K | offene_variante | 0.1545 | 0.6248 | 0.3886 | 0.2386 | 0.8357 | 0.0032 | 0.9383 | dio_mcm_episode_1t5bcxp | dio_09ol |
| KAS_2024_15M_2K | spannungsrand_kippnaehe | 0.0451 | 0.5993 | 0.3803 | 0.3136 | 0.7975 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1bvf |
| KAS_2024_30M_2K | zentrum_stabil | 0.7894 | 0.6518 | 0.3981 | 0.1687 | 0.8733 | 0.3177 | 0.0597 | dio_mcm_episode_1t5bcxp | dio_12w3 |
| KAS_2024_30M_2K | offene_variante | 0.1680 | 0.6243 | 0.3874 | 0.2384 | 0.8342 | 0.0000 | 0.9552 | dio_mcm_episode_1t5bcxp | dio_0k07 |
| KAS_2024_30M_2K | spannungsrand_kippnaehe | 0.0426 | 0.6028 | 0.3887 | 0.3127 | 0.8078 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0xz7 |
| KAS_2024_1H_2K | zentrum_stabil | 0.7984 | 0.6509 | 0.3956 | 0.1689 | 0.8728 | 0.3116 | 0.0710 | dio_mcm_episode_1t5bcxp | dio_1pgl |
| KAS_2024_1H_2K | offene_variante | 0.1560 | 0.6250 | 0.3883 | 0.2379 | 0.8366 | 0.0064 | 0.9486 | dio_mcm_episode_1t5bcxp | dio_0iah |
| KAS_2024_1H_2K | spannungsrand_kippnaehe | 0.0456 | 0.6001 | 0.3859 | 0.3187 | 0.8008 | 0.0110 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1gkk |

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
