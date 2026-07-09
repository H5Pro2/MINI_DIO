# Weltrelative Topologie-Matrix

Stand: 2026-06-21 22:13:49

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
| SIDEWAYS_2024_10K | 9994 | stark_zentriert_wenig_rand | 0.8087 | 0.1822 | 0.0091 | 0.2499 | 0.7029 | 0.5349 | 0.1576 | 0.8421 |
| POS_STRESS_2024_10K | 9994 | stark_zentriert_wenig_rand | 0.8224 | 0.1699 | 0.0077 | 0.2497 | 0.7036 | 0.5352 | 0.1570 | 0.8439 |
| NEG_STRESS_2024_10K | 9994 | stark_zentriert_wenig_rand | 0.8319 | 0.1569 | 0.0112 | 0.2499 | 0.7039 | 0.5353 | 0.1568 | 0.8447 |
| LATE_POS_2024_10K | 9994 | stark_zentriert_wenig_rand | 0.8078 | 0.1830 | 0.0092 | 0.2496 | 0.7019 | 0.5337 | 0.1587 | 0.8411 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SIDEWAYS_2024_10K | zentrum_stabil | 0.8087 | 0.7126 | 0.5470 | 0.1469 | 0.8580 | 0.3091 | 0.1189 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SIDEWAYS_2024_10K | offene_variante | 0.1822 | 0.6660 | 0.4900 | 0.1976 | 0.7791 | 0.0005 | 0.7946 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SIDEWAYS_2024_10K | spannungsrand_kippnaehe | 0.0091 | 0.5754 | 0.3566 | 0.3075 | 0.6934 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| POS_STRESS_2024_10K | zentrum_stabil | 0.8224 | 0.7126 | 0.5465 | 0.1471 | 0.8585 | 0.3038 | 0.1258 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POS_STRESS_2024_10K | offene_variante | 0.1699 | 0.6657 | 0.4892 | 0.1982 | 0.7793 | 0.0012 | 0.8174 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| POS_STRESS_2024_10K | spannungsrand_kippnaehe | 0.0077 | 0.5755 | 0.3516 | 0.3055 | 0.7062 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1sp4 |
| NEG_STRESS_2024_10K | zentrum_stabil | 0.8319 | 0.7135 | 0.5476 | 0.1465 | 0.8595 | 0.3006 | 0.1261 | dio_mcm_episode_0e7qvj1 | dio_104t |
| NEG_STRESS_2024_10K | offene_variante | 0.1569 | 0.6622 | 0.4829 | 0.2004 | 0.7773 | 0.0000 | 0.8540 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| NEG_STRESS_2024_10K | spannungsrand_kippnaehe | 0.0112 | 0.5742 | 0.3531 | 0.3073 | 0.6953 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| LATE_POS_2024_10K | zentrum_stabil | 0.8078 | 0.7115 | 0.5453 | 0.1481 | 0.8570 | 0.3093 | 0.1173 | dio_mcm_episode_0e7qvj1 | dio_104t |
| LATE_POS_2024_10K | offene_variante | 0.1830 | 0.6662 | 0.4912 | 0.1977 | 0.7783 | 0.0011 | 0.7983 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| LATE_POS_2024_10K | spannungsrand_kippnaehe | 0.0092 | 0.5744 | 0.3534 | 0.3077 | 0.6938 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1ia5 |

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
