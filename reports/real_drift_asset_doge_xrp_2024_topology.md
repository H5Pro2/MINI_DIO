# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:53:34

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
| REAL_DRIFT_DOGE_2024_A | 4994 | stark_zentriert_wenig_rand | 0.9866 | 0.0134 | 0.0000 | 0.2491 | 0.7024 | 0.5398 | 0.1691 | 0.8397 |
| REAL_DRIFT_DOGE_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9920 | 0.0080 | 0.0000 | 0.2489 | 0.7034 | 0.5403 | 0.1674 | 0.8428 |
| REAL_DRIFT_XRP_2024_A | 4994 | stark_zentriert_wenig_rand | 0.9858 | 0.0142 | 0.0000 | 0.2485 | 0.7033 | 0.5406 | 0.1681 | 0.8417 |
| REAL_DRIFT_XRP_2024_FOLLOW | 4994 | stark_zentriert_wenig_rand | 0.9864 | 0.0136 | 0.0000 | 0.2487 | 0.7032 | 0.5405 | 0.1680 | 0.8413 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_DRIFT_DOGE_2024_A | zentrum_stabil | 0.9866 | 0.7041 | 0.5422 | 0.1675 | 0.8422 | 0.2535 | 0.2399 | dio_mcm_episode_1qlxgj7 | dio_104t |
| REAL_DRIFT_DOGE_2024_A | offene_variante | 0.0134 | 0.5765 | 0.3648 | 0.2878 | 0.6578 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_1v68 |
| REAL_DRIFT_DOGE_2024_FOLLOW | zentrum_stabil | 0.9920 | 0.7044 | 0.5417 | 0.1665 | 0.8443 | 0.2521 | 0.2440 | dio_mcm_episode_1qlxgj7 | dio_104t |
| REAL_DRIFT_DOGE_2024_FOLLOW | offene_variante | 0.0080 | 0.5803 | 0.3646 | 0.2869 | 0.6607 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_00hc |
| REAL_DRIFT_XRP_2024_A | zentrum_stabil | 0.9858 | 0.7052 | 0.5431 | 0.1663 | 0.8444 | 0.2537 | 0.2393 | dio_mcm_episode_1qlxgj7 | dio_104t |
| REAL_DRIFT_XRP_2024_A | offene_variante | 0.0142 | 0.5751 | 0.3639 | 0.2915 | 0.6552 | 0.0000 | 1.0000 | dio_mcm_episode_0xg6rjf | dio_00hc |
| REAL_DRIFT_XRP_2024_FOLLOW | zentrum_stabil | 0.9864 | 0.7049 | 0.5429 | 0.1664 | 0.8438 | 0.2536 | 0.2397 | dio_mcm_episode_12tgchq | dio_104t |
| REAL_DRIFT_XRP_2024_FOLLOW | offene_variante | 0.0136 | 0.5791 | 0.3678 | 0.2867 | 0.6619 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_00hc |

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
