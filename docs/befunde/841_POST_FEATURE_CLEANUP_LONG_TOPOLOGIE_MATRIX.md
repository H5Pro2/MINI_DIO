# Weltrelative Topologie-Matrix

Stand: 2026-06-26 10:00:47

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
| POST_CLEAN_LONG_QUIET_2026_SIDEWAYS | 9994 | gemischte_rollenordnung | 0.7929 | 0.2017 | 0.0054 | 0.2498 | 0.7053 | 0.5380 | 0.1524 | 0.8416 |
| POST_CLEAN_LONG_STRESS_2025 | 9994 | gemischte_rollenordnung | 0.7891 | 0.2044 | 0.0065 | 0.2494 | 0.7043 | 0.5368 | 0.1530 | 0.8405 |
| POST_CLEAN_LONG_EXPANSION_2023_POSITIVE | 9994 | gemischte_rollenordnung | 0.7915 | 0.2003 | 0.0082 | 0.2489 | 0.7049 | 0.5367 | 0.1527 | 0.8415 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| POST_CLEAN_LONG_QUIET_2026_SIDEWAYS | zentrum_stabil | 0.7929 | 0.7153 | 0.5499 | 0.1418 | 0.8591 | 0.3152 | 0.0977 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_LONG_QUIET_2026_SIDEWAYS | offene_variante | 0.2017 | 0.6696 | 0.4962 | 0.1902 | 0.7777 | 0.0005 | 0.8289 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| POST_CLEAN_LONG_QUIET_2026_SIDEWAYS | spannungsrand_kippnaehe | 0.0054 | 0.5723 | 0.3587 | 0.2973 | 0.6614 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1c6r |
| POST_CLEAN_LONG_STRESS_2025 | zentrum_stabil | 0.7891 | 0.7143 | 0.5489 | 0.1424 | 0.8581 | 0.3168 | 0.0989 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_LONG_STRESS_2025 | offene_variante | 0.2044 | 0.6699 | 0.4962 | 0.1896 | 0.7788 | 0.0005 | 0.8096 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| POST_CLEAN_LONG_STRESS_2025 | spannungsrand_kippnaehe | 0.0065 | 0.5692 | 0.3577 | 0.3002 | 0.6522 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1lid |
| POST_CLEAN_LONG_EXPANSION_2023_POSITIVE | zentrum_stabil | 0.7915 | 0.7151 | 0.5489 | 0.1418 | 0.8594 | 0.3153 | 0.0982 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_LONG_EXPANSION_2023_POSITIVE | offene_variante | 0.2003 | 0.6700 | 0.4958 | 0.1900 | 0.7781 | 0.0025 | 0.8192 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| POST_CLEAN_LONG_EXPANSION_2023_POSITIVE | spannungsrand_kippnaehe | 0.0082 | 0.5720 | 0.3625 | 0.2995 | 0.6596 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_17qo |

## Lesart

Zentrumsnahe Welten: 0
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

Als naechstes sollte dieselbe Pruefung mit weiteren Asset- und Zeitrahmenwelten gegengehalten werden.
Ziel ist zu pruefen, ob die stabile Rollenordnung nur SOL-nahe Welten betrifft oder ob sie auch bei deutlich anderer Marktmelodie, anderer Lautheit und anderer Strukturspannung erhalten bleibt.
