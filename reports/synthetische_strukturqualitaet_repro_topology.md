# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:32:14

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
| SYNTH_RUHE_ORIG | 994 | stark_zentriert_wenig_rand | 1.0000 | 0.0000 | 0.0000 | 0.2193 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| SYNTH_RUHE_REPRO | 994 | stark_zentriert_wenig_rand | 1.0000 | 0.0000 | 0.0000 | 0.2193 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| SYNTH_BRUCH_RAND_ORIG | 7994 | stark_zentriert_wenig_rand | 0.9994 | 0.0006 | 0.0000 | 0.2489 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| SYNTH_BRUCH_RAND_REPRO | 7994 | stark_zentriert_wenig_rand | 0.9994 | 0.0006 | 0.0000 | 0.2489 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| KONTROLL_EXPANSION_ORIG | 9994 | stark_zentriert_wenig_rand | 0.9859 | 0.0141 | 0.0000 | 0.2478 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |
| KONTROLL_EXPANSION_REPRO | 9994 | stark_zentriert_wenig_rand | 0.9859 | 0.0141 | 0.0000 | 0.2478 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_RUHE_ORIG | zentrum_stabil | 1.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 | 0.2505 | 0.2505 | dio_mcm_episode_0lx7o7j | dio_1fll |
| SYNTH_RUHE_REPRO | zentrum_stabil | 1.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 | 0.2505 | 0.2505 | dio_mcm_episode_0lx7o7j | dio_1fll |
| SYNTH_BRUCH_RAND_ORIG | zentrum_stabil | 0.9994 | 0.7508 | 0.6071 | 0.1250 | 0.9091 | 0.2502 | 0.2496 | dio_mcm_episode_0kvw1tc | dio_1fll |
| SYNTH_BRUCH_RAND_ORIG | offene_variante | 0.0006 | 0.5804 | 0.3426 | 0.3003 | 0.6650 | 0.0000 | 1.0000 | dio_mcm_episode_16da5fv | dio_0kcg |
| SYNTH_BRUCH_RAND_REPRO | zentrum_stabil | 0.9994 | 0.7508 | 0.6071 | 0.1250 | 0.9091 | 0.2502 | 0.2496 | dio_mcm_episode_0kvw1tc | dio_1fll |
| SYNTH_BRUCH_RAND_REPRO | offene_variante | 0.0006 | 0.5804 | 0.3426 | 0.3003 | 0.6650 | 0.0000 | 1.0000 | dio_mcm_episode_16da5fv | dio_0kcg |
| KONTROLL_EXPANSION_ORIG | zentrum_stabil | 0.9859 | 0.7097 | 0.5564 | 0.1687 | 0.8433 | 0.2536 | 0.2393 | dio_mcm_episode_12tgchq | dio_104t |
| KONTROLL_EXPANSION_ORIG | offene_variante | 0.0141 | 0.5786 | 0.3713 | 0.2900 | 0.6537 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| KONTROLL_EXPANSION_REPRO | zentrum_stabil | 0.9859 | 0.7097 | 0.5564 | 0.1687 | 0.8433 | 0.2536 | 0.2393 | dio_mcm_episode_12tgchq | dio_104t |
| KONTROLL_EXPANSION_REPRO | offene_variante | 0.0141 | 0.5786 | 0.3713 | 0.2900 | 0.6537 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |

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
