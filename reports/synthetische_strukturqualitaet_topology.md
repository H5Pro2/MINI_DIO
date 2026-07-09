# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:25:49

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
| SYNTH_RUHE_DRIFT | 994 | stark_zentriert_wenig_rand | 1.0000 | 0.0000 | 0.0000 | 0.2193 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| SYNTH_BRUCH_RAND | 7994 | stark_zentriert_wenig_rand | 0.9994 | 0.0006 | 0.0000 | 0.2489 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| KONTROLL_EXPANSION_2023 | 9994 | stark_zentriert_wenig_rand | 0.9859 | 0.0141 | 0.0000 | 0.2478 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |
| BTC_2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.9902 | 0.0098 | 0.0000 | 0.2495 | 0.7075 | 0.5529 | 0.1698 | 0.8424 |
| DOGE_2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.9911 | 0.0089 | 0.0000 | 0.2498 | 0.7069 | 0.5526 | 0.1706 | 0.8413 |
| PAXG_2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8725 | 0.1202 | 0.0073 | 0.2473 | 0.7144 | 0.5410 | 0.1517 | 0.8561 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_RUHE_DRIFT | zentrum_stabil | 1.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 | 0.2505 | 0.2505 | dio_mcm_episode_0lx7o7j | dio_1fll |
| SYNTH_BRUCH_RAND | zentrum_stabil | 0.9994 | 0.7508 | 0.6071 | 0.1250 | 0.9091 | 0.2502 | 0.2496 | dio_mcm_episode_0kvw1tc | dio_1fll |
| SYNTH_BRUCH_RAND | offene_variante | 0.0006 | 0.5804 | 0.3426 | 0.3003 | 0.6650 | 0.0000 | 1.0000 | dio_mcm_episode_16da5fv | dio_0kcg |
| KONTROLL_EXPANSION_2023 | zentrum_stabil | 0.9859 | 0.7097 | 0.5564 | 0.1687 | 0.8433 | 0.2536 | 0.2393 | dio_mcm_episode_12tgchq | dio_104t |
| KONTROLL_EXPANSION_2023 | offene_variante | 0.0141 | 0.5786 | 0.3713 | 0.2900 | 0.6537 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_17qo |
| BTC_2025_5M_10K | zentrum_stabil | 0.9902 | 0.7088 | 0.5547 | 0.1686 | 0.8442 | 0.2525 | 0.2426 | dio_mcm_episode_12tgchq | dio_104t |
| BTC_2025_5M_10K | offene_variante | 0.0098 | 0.5798 | 0.3699 | 0.2869 | 0.6582 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1c6r |
| DOGE_2025_5M_10K | zentrum_stabil | 0.9911 | 0.7081 | 0.5543 | 0.1695 | 0.8429 | 0.2523 | 0.2433 | dio_mcm_episode_12tgchq | dio_104t |
| DOGE_2025_5M_10K | offene_variante | 0.0089 | 0.5769 | 0.3661 | 0.2905 | 0.6583 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_0ku7 |
| PAXG_2025_5M_10K | zentrum_stabil | 0.8725 | 0.7222 | 0.5513 | 0.1437 | 0.8673 | 0.2866 | 0.1546 | dio_mcm_episode_1hdpu9s | dio_104t |
| PAXG_2025_5M_10K | offene_variante | 0.1202 | 0.6654 | 0.4779 | 0.2008 | 0.7839 | 0.0000 | 0.8976 | dio_mcm_episode_1hdpu9s | dio_00ja |
| PAXG_2025_5M_10K | spannungsrand_kippnaehe | 0.0073 | 0.5819 | 0.3508 | 0.3042 | 0.7091 | 0.0000 | 1.0000 | dio_mcm_episode_1hdpu9s | dio_00hc |

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
